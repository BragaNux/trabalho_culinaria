import time
from pathlib import Path
from dotenv import load_dotenv
import chromadb
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

CHROMA_DIR = "chroma_db"
COLLECTION = "material"
TOP_K = 3

_collection = None
_embeddings = None


def _get_collection():
    global _collection, _embeddings
    if _collection is None:
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        _collection = client.get_or_create_collection(COLLECTION)
        _embeddings = HuggingFaceEmbeddings(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
    return _collection, _embeddings


@tool
def buscar_documentos(pergunta: str) -> str:
    """Busca trechos relevantes do material indexado para responder à pergunta."""
    col, emb = _get_collection()
    count = col.count()
    if count == 0:
        return "Nenhum documento indexado. Adicione PDFs em documentos/ e rode: python src/ingestao.py"
    vec = emb.embed_query(pergunta)
    results = col.query(
        query_embeddings=[vec],
        n_results=min(TOP_K, count),
        include=["documents", "metadatas"],
    )
    trechos = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        fonte = Path(meta.get("source", "desconhecido")).name
        pagina = meta.get("page", "?")
        trechos.append(f"[{fonte} — p. {pagina}]\n{doc}")
    return "\n\n---\n\n".join(trechos) if trechos else "Nenhum trecho relevante encontrado."


@tool
def classificar_urgencia(descricao: str) -> str:
    """Classifica a urgência da dúvida de culinária como 'alta' ou 'baixa'."""
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    resp = llm.invoke(
        "Classifique a urgência da dúvida abaixo baseando-se no contexto de culinária.\n"
        "Responda APENAS com uma palavra: alta ou baixa.\n"
        "Use 'alta' se mencionar prazo imediato, emergências físicas na cozinha (fogo na panela, queimaduras, cortes), "
        "comida queimando no forno, ou prazos curtos urgentes para preparar refeição (visita chegando em minutos, jantar hoje urgente, etc).\n"
        "Use 'baixa' para dúvidas normais sobre ingredientes, receitas sem pressa extrema ou substituições normais.\n\n"
        f"Dúvida: {descricao}"
    )
    return resp.content.strip().lower()


def criar_agente() -> AgentExecutor:
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    tools = [buscar_documentos, classificar_urgencia]
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Você é o 'Chef Assistente', um assistente virtual especialista em culinária que responde dúvidas com base no material fornecido. "
            "Sempre use a ferramenta 'buscar_documentos' para encontrar receitas, substituições ou dicas de sobrevivência antes de responder. "
            "Use a ferramenta 'classificar_urgencia' para determinar a prioridade da dúvida (alta ou baixa). "
            "Responda em português brasileiro de forma muito clara, empática e prestativa, mantendo a etiqueta de um chef profissional. "
            "Cite obrigatoriamente as fontes consultadas no formato exato [nome_do_arquivo.pdf — p. X] no final ou ao longo da sua resposta.",
        ),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(
        agent=agent, tools=tools, verbose=False, return_intermediate_steps=True
    )


def executar(pergunta: str, usuario_id: str = "anonimo") -> dict:
    agente = criar_agente()
    inicio = time.time()
    resultado = agente.invoke({"input": pergunta})
    latencia = round(time.time() - inicio, 2)

    tools_usadas, fontes, contexts, urgencia = [], [], [], "baixa"
    for action, observation in resultado.get("intermediate_steps", []):
        tools_usadas.append(action.tool)
        if action.tool == "buscar_documentos":
            contexts.append(observation)
            for linha in observation.split("\n"):
                if linha.startswith("[") and "—" in linha:
                    fontes.append(linha[1:].split("]")[0])
        elif action.tool == "classificar_urgencia":
            urgencia = observation.strip()

    return {
        "resposta": resultado["output"],
        "fontes": list(dict.fromkeys(fontes)),
        "urgencia": urgencia,
        "tools_utilizadas": list(dict.fromkeys(tools_usadas)),
        "latencia_s": latencia,
        "contexts": contexts,
    }
