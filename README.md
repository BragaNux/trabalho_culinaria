# 👨‍🍳 Assistente de Culinária — RAG + Telegram + n8n + Discord

Este projeto implementa um **sistema de atendimento automatizado completo e inteligente** para suporte culinário. Ele foi construído como parte da **Atividade Avaliativa (G2)** da disciplina de Inteligência Artificial.

O assistente utiliza a técnica de **RAG (Retrieval-Augmented Generation)** com banco vetorial local para responder a dúvidas de culinária e segurança com base em manuais em PDF. Ele classifica a urgência da dúvida em tempo real e orquestra o fluxo de mensagens via **n8n**, conectando o **Telegram** como interface de chat e o **Discord** como canal de notificações corporativas por prioridade.

---

## 📐 Arquitetura do Sistema

```
[Usuário]
   │  envia dúvida culinária pelo Telegram
   ▼
[Telegram Bot]                 ← Criado via @BotFather
   │
   ▼ (Túnel HTTPS seguro via localtunnel)
[n8n — Telegram Trigger]       ← Captura o webhook da mensagem
   │
   ▼
[n8n — HTTP Request]           ← Chama o agente FastAPI local (POST /perguntar)
   │
   ▼
[Agente Python — FastAPI]      ← Porta 8000
   ├── RAG (ChromaDB local)    ├── Busca trechos em "livro_receitas_brasileiras.pdf"
   │                           └── Busca trechos em "guia_sobrevivencia_cozinha.pdf"
   ├── Classifica Urgência    ← Llama 3.3 70B via Groq ("alta" para emergências e prazos curtos)
   └── Salva no SQLite         ← Registra histórico completo de dúvidas em "registros.db"
   │
   ├─► [n8n — Telegram Reply]  ← Devolve a resposta com fontes e páginas no chat
   │
   ▼ (Orquestração por prioridade)
[n8n — IF Urgência == alta]
   ├── TRUE  ──► [Discord #alertas-urgentes] ← Canal de emergências de cozinha
   └── FALSE ──► [Discord #duvidas-normais]   ← Canal de dúvidas culinárias comuns
```

---

## 🛠️ Stack Tecnológica

* **LLM**: Groq (Llama 3.3 70B Versatile) para geração de resposta e Llama 3.1 8B para avaliação.
* **Embeddings**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (rodando localmente offline).
* **Banco Vetorial**: ChromaDB (local e persistente).
* **Orquestração**: n8n (rodando via Docker Desktop).
* **Interface de Chat**: Telegram Bot.
* **Alertas e Notificações**: Discord Webhooks (Canais separados por prioridade).
* **Banco de Dados Relacional**: SQLite (armazenamento persistente local de todas as requisições, latências e fontes).
* **Avaliação**: RAGAS (Fidelidade, Relevância da Resposta e Precisão de Contexto).
* **Observabilidade**: LangSmith.

---

## 📂 Estrutura do Projeto

A pasta principal de entrega é `assistente-culinaria/`:

```
assistente-culinaria/
├── documentos/              ← PDFs indexados (Livro de Receitas e Guia de Sobrevivência)
├── scratch/
│   └── gerar_documentos.py  ← Script que gera os PDFs programaticamente usando PyMuPDF
├── src/
│   ├── __init__.py
│   ├── ingestao.py          ← Realiza o text splitting e indexa os PDFs no ChromaDB
│   ├── agente.py            ← Agente LangChain equipado com ferramentas de busca e urgência
│   └── api.py               ← Servidor FastAPI local que registra logs no SQLite registros.db
├── avaliacao/
│   ├── __init__.py
│   ├── golden_set.json      ← 5 perguntas e respostas de controle de qualidade
│   └── rodar_ragas.py       ← Executa a avaliação científica de métricas do Ragas
├── workflow/
│   └── assistente_culinaria_n8n.json ← Workflow n8n pronto para importação
├── prints_entrega/          ← Pasta contendo todos os prints obrigatórios solicitados
├── .env.example             ← Modelo de variáveis de ambiente
├── .gitignore               ← Proteção de arquivos locais
└── requirements.txt         ← Dependências (ajustadas e otimizadas para Python 3.13)
```

---

## 📊 Resultados de Qualidade — Avaliação RAGAS

A avaliação automatizada foi executada no conjunto de dados de referência (Golden Set) com **sucesso absoluto**. Todas as métricas superaram com ampla margem as metas mínimas estabelecidas pelo professor:

| Métrica | Nota do Assistente | Meta Exigida | Status | O que mede |
| :--- | :---: | :---: | :---: | :--- |
| **Faithfulness** (Fidelidade) | **0.7738** | `> 0.70` | **✅ APROVADO** | O bot responde estritamente com base nos PDFs (sem alucinações). |
| **Answer Relevancy** (Relevância) | **0.9100** | `> 0.70` | **✅ APROVADO** | As respostas são diretas e completas para o que foi perguntado. |
| **Context Precision** (Precisão) | **0.8667** | `> 0.60` | **✅ APROVADO** | O resgate de trechos dos PDFs é altamente cirúrgico. |

---

## 🚀 Como Executar o Projeto

### 1. Configurar as Chaves de API
Copie o arquivo `.env.example` para `.env` e preencha com as suas chaves reais:
```env
GROQ_API_KEY=gsk_...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=ls__...
LANGCHAIN_PROJECT=assistente-culinaria
DISCORD_WEBHOOK_URGENTE=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_NORMAL=https://discord.com/api/webhooks/...
TELEGRAM_BOT_TOKEN=...
```

### 2. Iniciar a Ingestão e o Banco Vetorial
Ative o ambiente virtual e execute a indexação:
```bash
.venv\Scripts\activate
python src/ingestao.py
```

### 3. Iniciar a API FastAPI
Suba o servidor local:
```bash
.venv\Scripts\activate
uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
```

### 4. Rodar o n8n com Túnel Localtunnel
1. Em um terminal, inicie o n8n com a URL do seu webhook seguro do localtunnel:
   ```bash
   docker run -it --rm -p 5678:5678 -e WEBHOOK_URL=https://cyan-rice-brush.loca.lt -v n8n_data:/home/node/.n8n n8nio/n8n
   ```
2. Em outro terminal, mantenha o túnel ativo na porta 5678:
   ```bash
   npx localtunnel --port 5678
   ```
3. Acesse o painel pelo link gerado, insira o seu IP público como senha do túnel, importe o arquivo `workflow/assistente_culinaria_n8n.json` e clique em **Publish**!

---

## 📷 Prints de Entrega
Todos os prints obrigatórios (fluxo n8n ativo, chat de Telegram com respostas, notificações no Discord e traces no LangSmith) estão organizados e disponíveis no diretório:
📂 [prints_entrega/](file:///c:/Users/Brayan/Desktop/trabalho_culinaria/assistente-culinaria/prints_entrega/)

Conforme orientação, foi acertado com o professor, conforme apresentação de todo o processo, sendo não preciso entregar o video mostrando todo o processo, pois já apresentei pra ele pessoalmente.
