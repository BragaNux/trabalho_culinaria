import os
from pathlib import Path
import fitz

def criar_pdf_receitas(caminho):
    doc = fitz.open()
    
    # Página 1: Capa e Introdução
    p1 = doc.new_page()
    rect1 = fitz.Rect(50, 50, 550, 750)
    texto1 = (
        "LIVRO DE RECEITAS CLÁSSICAS BRASILEIRAS\n\n"
        "Este livro contém uma seleção de receitas tradicionais da culinária brasileira, "
        "perfeitas para todas as ocasiões. As receitas apresentam listas detalhadas de "
        "ingredientes, modos de preparo e dicas especiais para garantir o sucesso dos seus pratos."
    )
    p1.insert_textbox(rect1, texto1, fontsize=12, fontname="helv")
    p1.insert_text(fitz.Point(50, 780), "[livro_receitas_brasileiras.pdf - Página 1]", fontsize=8, fontname="helv")

    # Página 2: Feijoada
    p2 = doc.new_page()
    rect2 = fitz.Rect(50, 50, 550, 750)
    texto2 = (
        "RECEITA DE FEIJOADA COMPLETA BRASILEIRA\n\n"
        "Tempo de Preparo: 3 horas | Rendimento: 8 porções\n\n"
        "Ingredientes:\n"
        "- 1 kg de feijão preto\n"
        "- 500g de carne-seca (charque)\n"
        "- 500g de costelinha de porco salgada\n"
        "- 300g de lombo de porco salgado\n"
        "- 200g de paio cortado em rodelas\n"
        "- 200g de linguiça calabresa em rodelas\n"
        "- 150g de bacon picado\n"
        "- 1 cebola grande picada\n"
        "- 4 dentes de alho picados\n"
        "- 3 folhas de louro\n"
        "- Azeite e pimenta-do-reino a gosto\n\n"
        "Modo de Preparo:\n"
        "1. De véspera, coloque as carnes salgadas de molho na água para dessalgar, trocando a água várias vezes. Deixe o feijão preto de molho por 12 horas.\n"
        "2. Cozinhe o feijão com as folhas de louro em fogo brando.\n"
        "3. Em outra panela grande, ferva e cozinhe as carnes dessalgadas até ficarem macias. Escorra.\n"
        "4. Junte as carnes cozidas e as linguiças ao feijão já macio. Deixe ferver em fogo baixo por 30 minutos para apurar o caldo.\n"
        "5. Em uma frigideira, doure o bacon, adicione a cebola e o alho. Refogue bem. Pegue uma concha do feijão cozido, amasse e misture ao refogado. Coloque tudo de volta na panela grande.\n"
        "6. Deixe engrossar por mais 15 minutos. Sirva bem quente com couve mineira refogada e farofa de manteiga."
    )
    p2.insert_textbox(rect2, texto2, fontsize=10, fontname="helv")
    p2.insert_text(fitz.Point(50, 780), "[livro_receitas_brasileiras.pdf - Página 2]", fontsize=8, fontname="helv")

    # Página 3: Pão de Queijo
    p3 = doc.new_page()
    rect3 = fitz.Rect(50, 50, 550, 750)
    texto3 = (
        "RECEITA DE PÃO DE QUEIJO MINEIRO TRADICIONAL\n\n"
        "Tempo de Preparo: 45 minutos | Rendimento: 30 pãezinhos\n\n"
        "Ingredientes:\n"
        "- 500g de polvilho azedo\n"
        "- 1 colher de sopa rasa de sal\n"
        "- 150 ml de óleo de soja\n"
        "- 150 ml de leite integral\n"
        "- 150 ml de água\n"
        "- 3 ovos grandes\n"
        "- 300g de queijo meia cura ralado\n\n"
        "Modo de Preparo:\n"
        "1. Em uma panela grande, junte o leite, o óleo, a água e o sal. Leve ao fogo médio até levantar fervura.\n"
        "2. Coloque o polvilho azedo em uma tigela grande. Despeje a mistura quente sobre o polvilho para escaldá-lo. Misture bem com uma colher grande e aguarde esfriar por 10 minutos.\n"
        "3. Adicione os ovos um a um, misturando bem com as mãos.\n"
        "4. Adicione o queijo meia cura ralado e sove bem a massa até ficar homogênea e sem grudar demais nas mãos.\n"
        "5. Modele bolinhas pequenas e disponha em uma assadeira sem necessidade de untar.\n"
        "6. Asse em forno preaquecido a 180 graus Celsius por aproximadamente 25 a 30 minutos, até dourar levemente por fora.\n\n"
        "Dica de Ouro: Use queijo meia cura ou queijo canastra curado para garantir o sabor típico de Minas Gerais!"
    )
    p3.insert_textbox(rect3, texto3, fontsize=10, fontname="helv")
    p3.insert_text(fitz.Point(50, 780), "[livro_receitas_brasileiras.pdf - Página 3]", fontsize=8, fontname="helv")

    # Página 4: Brigadeiro
    p4 = doc.new_page()
    rect4 = fitz.Rect(50, 50, 550, 750)
    texto4 = (
        "RECEITA DE BRIGADEIRO GOURMET TRADICIONAL\n\n"
        "Tempo de Preparo: 20 minutos | Rendimento: 25 docinhos\n\n"
        "Ingredientes:\n"
        "- 1 lata de leite condensado (395g)\n"
        "- 1 colher de sopa de manteiga sem sal (15g)\n"
        "- 100g de chocolate em pó 50% cacau\n"
        "- 100ml de creme de leite de caixinha\n"
        "- 150g de chocolate granulado de boa qualidade para enrolar\n\n"
        "Modo de Preparo:\n"
        "1. Em uma panela de fundo grosso, junte o leite condensado, a manteiga e o chocolate em pó. Adicione o creme de leite.\n"
        "2. Leve ao fogo baixo e mexa sem parar com uma espátula de silicone resistente ao calor.\n"
        "3. Cozinhe por cerca de 10 a 15 minutos, raspando bem as laterais e o fundo da panela, até que a massa engrosse e comece a se desprender completamente do fundo da panela.\n"
        "4. Despeje o brigadeiro em um prato untado com manteiga e cubra com plástico filme em contato direto para não criar película. Deixe esfriar completamente.\n"
        "5. Unte as mãos com manteiga, modele pequenas bolinhas de 15g, passe-as no chocolate granulado e disponha em forminhas de papel."
    )
    p4.insert_textbox(rect4, texto4, fontsize=10, fontname="helv")
    p4.insert_text(fitz.Point(50, 780), "[livro_receitas_brasileiras.pdf - Página 4]", fontsize=8, fontname="helv")

    # Página 5: Bolo de Cenoura
    p5 = doc.new_page()
    rect5 = fitz.Rect(50, 50, 550, 750)
    texto5 = (
        "RECEITA DE BOLO DE CENOURA FOFINHO COM CALDA DE CHOCOLATE\n\n"
        "Tempo de Preparo: 50 minutos | Rendimento: 12 fatias\n\n"
        "Ingredientes do Bolo:\n"
        "- 3 cenouras médias descascadas e picadas\n"
        "- 3 ovos grandes\n"
        "- 1 xícara de óleo de soja\n"
        "- 2 xícaras de açúcar refinado\n"
        "- 2 xícaras de farinha de trigo\n"
        "- 1 colher de sopa de fermento químico em pó\n"
        "- 1 pitada de sal\n\n"
        "Modo de Preparo do Bolo:\n"
        "1. No liquidificador, bata as cenouras picadas, os ovos e o óleo por 3 minutos até virar um creme liso.\n"
        "2. Em uma tigela grande, peneire a farinha de trigo, o açúcar e o sal. Misture bem.\n"
        "3. Despeje o creme do liquidificador sobre os ingredientes secos e misture delicadamente.\n"
        "4. Acrescente o fermento em pó e mexa suavemente de baixo para cima.\n"
        "5. Despeje a massa em uma assadeira untada e enfarinhada.\n"
        "6. Asse em forno preaquecido a 180 graus Celsius por cerca de 35 a 40 minutos. Teste com um palito antes de tirar.\n\n"
        "Modo de Preparo da Cobertura:\n"
        "1. Em uma panela pequena, junte todos os ingredientes da cobertura (manteiga, chocolate em pó, açúcar, leite).\n"
        "2. Mexa sem parar até levantar fervura e começar a desgrudar do fundo (cerca de 5 minutos).\n"
        "3. Despeje imediatamente quente sobre o bolo já assado para criar aquela casquinha crocante!"
    )
    p5.insert_textbox(rect5, texto5, fontsize=9.5, fontname="helv")
    p5.insert_text(fitz.Point(50, 780), "[livro_receitas_brasileiras.pdf - Página 5]", fontsize=8, fontname="helv")

    doc.save(caminho)
    doc.close()
    print(f"PDF {caminho} criado com sucesso.")

def criar_pdf_sobrevivencia(caminho):
    doc = fitz.open()
    
    # Página 1: Capa e Introdução
    p1 = doc.new_page()
    rect1 = fitz.Rect(50, 50, 550, 750)
    texto1 = (
        "GUIA DE SOBREVIVÊNCIA E SOLUÇÃO DE PROBLEMAS NA COZINHA\n\n"
        "Este guia prático foi criado para ajudar cozinheiros iniciantes e experientes a resolverem "
        "problemas comuns no dia a dia da cozinha, além de fornecer orientações cruciais sobre "
        "primeiros socorros para pequenos incidentes e substituições rápidas de ingredientes essenciais."
    )
    p1.insert_textbox(rect1, texto1, fontsize=12, fontname="helv")
    p1.insert_text(fitz.Point(50, 780), "[guia_sobrevivencia_cozinha.pdf - Página 1]", fontsize=8, fontname="helv")

    # Página 2: Salvar Comida Salgada / Queimada
    p2 = doc.new_page()
    rect2 = fitz.Rect(50, 50, 550, 750)
    texto2 = (
        "COMO SALVAR COMIDA SALGADA OU ARROZ QUEIMADO\n\n"
        "1. Como Salvar Molho ou Sopa Salgada:\n"
        "- Batata Crua: Adicione uma batata média descascada e fatiada ao molho ou sopa e cozinhe por mais 10 minutos. A batata agirá como uma esponja, absorvendo o excesso de sal. Retire a batata antes de servir.\n"
        "- Ingredientes Ácidos: Adicione uma colher de chá de vinagre de maçã ou suco de limão para equilibrar o paladar salgado.\n"
        "- Creme ou Leite: Se a receita permitir, adicione creme de leite ou leite de coco para suavizar o sabor.\n\n"
        "2. Como Salvar Arroz Queimado no Fundo:\n"
        "- Ação Imediata: Desligue o fogo imediatamente ao sentir o cheiro de queimado.\n"
        "- Banho de Água Fria: Sem mexer o arroz, pegue a panela quente e coloque a base dela dentro de uma bacia ou pia com água fria. Isso interrompe o cozimento e evita que o vapor do queimado suba.\n"
        "- Pão de Forma: Coloque uma fatia de pão de forma branco por cima do arroz, tampe a panela e deixe descansar por 5 a 10 minutos. O pão irá absorver totalmente o cheiro e gosto de queimado.\n"
        "- Separação: Retire com cuidado apenas a parte de cima do arroz que não queimou, transferindo para outra travessa. Nunca raspe o fundo queimado da panela!"
    )
    p2.insert_textbox(rect2, texto2, fontsize=10, fontname="helv")
    p2.insert_text(fitz.Point(50, 780), "[guia_sobrevivencia_cozinha.pdf - Página 2]", fontsize=8, fontname="helv")

    # Página 3: Segurança e Primeiros Socorros (Emergências)
    p3 = doc.new_page()
    rect3 = fitz.Rect(50, 50, 550, 750)
    texto3 = (
        "SEGURANÇA NA COZINHA E PRIMEIROS SOCORROS\n\n"
        "ATENÇÃO! Pequenos acidentes domésticos acontecem com frequência. Saiba como agir de forma rápida e segura.\n\n"
        "1. Como Tratar Queimaduras Leves de Primeiro Grau (Emergência):\n"
        "- Resfriamento Imediato: Coloque a área queimada sob água fria corrente por pelo menos 10 a 15 minutos. Isso resfria a pele e evita que a queimadura se aprofunde nas camadas internas.\n"
        "- O Que Não Fazer: Nunca aplique manteiga, pasta de dente, óleo, gelo ou clara de ovo na queimadura. Esses produtos domésticos podem reter o calor na pele e causar infecções graves.\n"
        "- Proteção: Seque suavemente com uma toalha limpa e cubra a área com uma gaze estéril ou pano limpo e sem fiapos. Se surgirem bolhas grandes ou dor extrema, procure assistência médica de emergência imediata.\n\n"
        "2. Como Lidar com Pequenos Cortes:\n"
        "- Pressão Direta: Lave as mãos, depois pressione o corte com uma gaze limpa para estancar o sangramento.\n"
        "- Higienização: Lave bem a área cortada com água corrente e sabão neutro.\n"
        "- Proteção: Aplique uma pomada antisséptica e cubra com um curativo adesivo (band-aid) limpo."
    )
    p3.insert_textbox(rect3, texto3, fontsize=10, fontname="helv")
    p3.insert_text(fitz.Point(50, 780), "[guia_sobrevivencia_cozinha.pdf - Página 3]", fontsize=8, fontname="helv")

    # Página 4: Refeições Expressas em 15 Minutos (Prazos Curtos)
    p4 = doc.new_page()
    rect4 = fitz.Rect(50, 50, 550, 750)
    texto4 = (
        "REFEIÇÕES EXPRESSAS EM 15 MINUTOS (PRAZOS CURTOS)\n\n"
        "Se você está sem tempo, tem visitas chegando ou precisa de uma refeição urgente em 15 minutos, siga estas opções fáceis:\n\n"
        "1. Omelete Cremoso de Ervas:\n"
        "- Ingredientes: 3 ovos, 1 colher de manteiga, cebolinha picada, sal, pimenta e queijo ralado.\n"
        "- Preparo: Bata os ovos com garfo por 1 minuto. Derreta a manteiga em frigideira quente. Despeje os ovos e mexa as bordas em direção ao centro para dar cremosidade. Adicione o queijo e ervas, dobre ao meio e sirva em 5 minutos.\n\n"
        "2. Espaguete Rápido Alho e Óleo:\n"
        "- Ingredientes: 150g de macarrão cabelo de anjo (cozinha em 3 minutos), 3 dentes de alho fatiados, 4 colheres de azeite extra virgem, sal e salsinha.\n"
        "- Preparo: Cozinhe a massa na água fervente com sal por 3 minutos. Em outra frigideira, doure o alho fatiado no azeite quente até ficar dourado e crocante. Escorra o macarrão e junte ao azeite com alho. Misture bem, finalize com salsinha e sirva imediatamente."
    )
    p4.insert_textbox(rect4, texto4, fontsize=9.5, fontname="helv")
    p4.insert_text(fitz.Point(50, 780), "[guia_sobrevivencia_cozinha.pdf - Página 4]", fontsize=8, fontname="helv")

    # Página 5: Substituições de Ingredientes
    p5 = doc.new_page()
    rect5 = fitz.Rect(50, 50, 550, 750)
    texto5 = (
        "SUBSTITUIÇÃO DE INGREDIENTES ESSENCIAIS\n\n"
        "Faltou algum ingrediente no meio da receita? Veja as substituições equivalentes:\n\n"
        "1. Substituir 1 Xícara de Creme de Leite Fresco:\n"
        "- Misture 3/4 de xícara de leite integral com 1/4 de xícara (57g) de manteiga derretida. Misture bem. Use em molhos e sopas.\n\n"
        "2. Substituir 1 Colher de Sopa de Fermento Químico:\n"
        "- Misture 1 colher de chá de bicarbonato de sódio com 1/2 colher de chá de vinagre branco ou suco de limão adicionados diretamente aos líquidos da massa.\n\n"
        "3. Substituir 1 Ovo em Receitas de Bolo:\n"
        "- Use meia banana amassada madura, ou 1/4 de xícara de purê de maçã, ou ainda 1 colher de sopa de sementes de chia hidratadas em 3 colheres de sopa de água por 15 minutos."
    )
    p5.insert_textbox(rect5, texto5, fontsize=10, fontname="helv")
    p5.insert_text(fitz.Point(50, 780), "[guia_sobrevivencia_cozinha.pdf - Página 5]", fontsize=8, fontname="helv")

    doc.save(caminho)
    doc.close()
    print(f"PDF {caminho} criado com sucesso.")

if __name__ == "__main__":
    docs_dir = Path("documentos")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    criar_pdf_receitas(docs_dir / "livro_receitas_brasileiras.pdf")
    criar_pdf_sobrevivencia(docs_dir / "guia_sobrevivencia_cozinha.pdf")
