# Plano de Aula — Semana 7
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** II — Materiais PBR e Workflow no 3D Coat (Semanas 6–9)
**Tema:** Migração para o 3D Coat: mesh maps (AO, Curvature, Normal) e Smart Materials
**Apostila:** Parte III, Cap. 10 — Construção e Análise de Materiais Reais (introdução ao 3D Coat); Parte V, Cap. 16 — Normal Maps e Transferência de Detalhes. Leitura complementar (não avaliada): Parte IV, Cap. 13 — Texturização Procedural, para quem quiser a via alternativa de nós no Blender
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — Crítica circulante com ênfase em leitura de profundidade e coerência do material

---

## Pré-requisito da semana

Os estudantes chegam com:

- Hero Asset Referência com UV otimizado + textura seamless aplicada no canal Albedo (Principled BSDF com Metallic e Roughness preservados da Semana 5) — Semana 6
- Arquivo `.kra` do Krita com camadas preservadas para a(s) textura(s) seamless criada(s)
- Trilha visual definida (fotorrealista ou estilizada) — Semana 6
- Compreensão consolidada de: projeção UV, plausibilidade PBR, criação de textura seamless, Krita, fontes livres (fotográficas e estilizadas)

> **Transição pedagógica desta semana:** nas Semanas 5 e 6, o material PBR ganhou forma progressivamente — primeiro com valores planos (Semana 5), depois com uma imagem real no Albedo (Semana 6). A Semana 7 muda de ferramenta: o Blender deixa de ser o lugar onde o material é montado, e passa a ser só o lugar de onde a malha sai (exportação) e para onde os mapas finais voltam (reconexão). O 3D Coat entra como a ferramenta dedicada de texturização do semestre — e entra cedo, porque a partir de hoje as duas trilhas visuais da turma (fotorrealista e estilizada) usam o **mesmo fluxo de ferramenta**, divergindo apenas na forma de preencher os canais. Em vez de gerar o Normal Map por matemática de nós, a turma vai **bakear mapas direto da malha 3D** — Ambient Occlusion e Curvature nascem da própria geometria, sem precisar de high-poly — e vai aplicar o material com camadas e Smart Materials, o mesmo princípio usado em ferramentas de mercado como o Substance Painter. A saída desta semana é o primeiro material PBR **completo dentro do 3D Coat**, aplicado ao Hero Asset Referência: Albedo + Roughness + Metallic + Normal (gerado por bake/pintura), pronto para ser refinado e exportado na Semana 8.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que são mesh maps (Ambient Occlusion, Curvature, Normal) e por que eles podem ser gerados direto da geometria, sem depender de uma imagem externa nem de um asset high-poly dedicado.
2. Exportar o Hero Asset Referência com UV do Blender (`.obj`/`.fbx`) e importá-lo corretamente no 3D Coat em modo Per-Pixel Painting (workflow Metalness PBR).
3. Reconhecer os três espaços de trabalho principais do 3D Coat (Paint Room, UV Room, Render Room) e a lógica de camadas por canal.
4. Bakear/gerar os mapas de Ambient Occlusion e Curvature a partir da malha do Hero Asset Referência, e usá-los como máscara de desgaste.
5. Gerar um Normal Map real pintando micro-detalhe no canal Depth do 3D Coat (trinca, entalhe, rebite), sem depender de nós procedurais do Blender.
6. **Trilha fotorrealista:** projetar a textura seamless fotográfica da Semana 6 como camada de Color base no 3D Coat e usar AO/Curvature como máscara para reforçar desgaste físico nas arestas e reentrâncias.
7. **Trilha estilizada:** aplicar um Smart Material (ou um conjunto de camadas equivalente) sobre o Hero Asset Referência, usando AO/Curvature como máscara automática de sujeira e desgaste nas bordas — a mesma lógica de materiais inteligentes usada no Substance Painter.
8. Montar, ao final da semana, um material PBR com pelo menos três canais ativos no 3D Coat (Color/Albedo, Roughness, Normal), qualquer que seja a trilha visual.
9. Situar o bake de mesh maps desta semana dentro do conceito mais amplo de texturização procedural apresentado na Semana 1 — reconhecendo que a via alternativa de nós do Blender (Apostila, Parte IV, Cap. 13) continua disponível como técnica complementar, não obrigatória.

> O Subsurface Scattering (SSS) não é abordado nesta semana — ele é apresentado na Semana 8, junto ao refinamento final dos canais, para não sobrecarregar esta mini-aula com um conceito novo adicional.

---

## Critérios observados nesta semana

> ⚠️ **Semana sem crítica formal — nenhuma nota é atribuída.** O professor observa e registra evidências nos critérios abaixo para calibrar a avaliação da CF2 (Semana 8). O estudante recebe feedback oral durante o estúdio.

| Critério | O que observar |
|---|---|
| C1 — Processo de Projeto | Organização das camadas no 3D Coat (nomenclatura, uso de máscaras); registro visual do material antes e depois do bake |
| C2 — Direção Artística | Coerência do relevo e da máscara de desgaste com o universo do kit; consistência com a trilha visual escolhida (fotorrealista/estilizada) |
| C4 — Materiais PBR | Construção do material completo dentro do 3D Coat: canais conectados com lógica física correta, independentemente da trilha |
| C5 — Texturização | Primeiro contato observável com camadas e máscaras reais no 3D Coat — será avaliado formalmente na CF2 |
| C10 — Participação (CC) | Qualidade da leitura crítica na critique informal: capacidade de identificar onde o bake ou o Smart Material adiciona ou não credibilidade visual |

> **Progressão do PA — antes da CF2 (Semana 8):** Esta é a segunda semana antes da CF2, que fecha a Unidade II. C4 e C5 estão em desenvolvimento ativo. C5 começa a ser observado de forma substantiva esta semana — a profundidade visual adicionada pelo bake de mesh maps é a evidência central, para as duas trilhas. O professor registra observações para calibrar a avaliação de C4 e C5 na CF2.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x) — para exportação e reconexão futura
- Computadores com 3D Coat instalado (versão 2023 ou superior recomendada) — a partir desta semana, ferramenta principal
- Krita instalado (para eventuais ajustes nas texturas seamless antes da exportação)
- Arquivo `.blend` do Hero Asset Referência de cada estudante (Semanas 4–6)
- Arquivo `.kra` do Krita com as texturas seamless preservadas em camadas
- Arquivo de demonstração do professor: Asset simples (cubo ou parede) com textura seamless já conectada ao Albedo no Blender, exportado como `.obj`
- Acesso à internet, se disponível, para consulta de bibliotecas de Smart Materials do 3D Coat ou referência visual de curvatura/AO
- Projetor para demonstração
- Apostila — Parte III, Cap. 10 e Parte V, Cap. 16 — disponibilizadas antes da aula
- Pasta de exportação criada previamente no computador de demonstração do professor: `[DEMO]_3DCoat_Exportacao/`

> **Nota sobre versões do 3D Coat:** a interface do 3D Coat varia entre versões — os nomes exatos dos painéis de bake (ex.: "Textures → Ambient Occlusion", "Cavity/Curvature Generator", camadas do tipo "Fill Layer" com gerador procedural) podem mudar. Verificar a versão instalada no laboratório antes da aula e adaptar os nomes de menu conforme necessário. O princípio é estável em todas as versões: AO e Curvature podem ser calculados diretamente da geometria visível, sem exigir um asset high-poly separado — o bevel e a topologia do próprio Hero Asset Referência já fornecem informação suficiente.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Mesh maps: gerando profundidade e máscaras direto da malha, sem nós e sem high-poly**

Objetivo: mostrar que existe uma segunda forma de dar profundidade a um material, além dos nós matemáticos do Blender — o **bake**, que lê a própria geometria do asset e converte isso em textura. E mostrar que esse mesmo bake serve de base tanto para reforçar uma textura fotográfica (trilha realismo) quanto para guiar um Smart Material (trilha estilizada).

**Desenvolvimento:**

Abrir com uma comparação visual no projetor (imagens estáticas):

Mostrar três versões do mesmo asset de parede de pedra:
1. Material com apenas Albedo conectado (resultado da Semana 6).
2. O mesmo asset com um mapa de Ambient Occlusion multiplicado sobre o Albedo — as reentrâncias escurecem, dando volume.
3. O mesmo asset com Curvature também aplicado como máscara — as arestas e saliências recebem desgaste/brilho diferenciado, como se tivessem sido tocadas e polidas pelo uso.

Perguntar: *"De onde vem essa informação? Eu não pintei nada ainda — ela veio de quê?"* — conduzir a turma a perceber que a resposta é a própria geometria do asset: reentrâncias, bordas e bevels.

---

**Conteúdo a cobrir:**

**1. O que são mesh maps e por que não exigem high-poly**

Ferramentas de texturização como o 3D Coat e o Substance Painter conseguem extrair informação direto da malha 3D:

- **Ambient Occlusion (AO):** mede o quanto cada ponto da superfície está "protegido" da luz ambiente por geometria ao redor. Frestas, cantos internos e áreas côncavas recebem valores mais escuros; superfícies expostas recebem valores mais claros. Isso simula o acúmulo natural de sombra em reentrâncias — sujeira, poeira e sombra de contato tendem a se acumular exatamente onde o AO é mais escuro.
- **Curvature (ou Cavity):** mede a convexidade/concavidade da superfície. Arestas e quinas (convexas) recebem um valor; frestas e sulcos (côncavos) recebem outro. É o mapa mais útil para simular desgaste de uso: bordas e cantos são justamente onde a pintura descasca, o metal fica exposto e a poeira é limpa pelo contato — o oposto do que acontece nas reentrâncias.
- **Normal (via bake):** em produções com high-poly, o Normal nasce da diferença entre a malha detalhada e a malha de jogo. Neste curso, sem high-poly dedicado, o caminho prático é outro: pintar micro-detalhe diretamente no canal **Depth** do 3D Coat (pequenos entalhes, rachaduras, rebites, veios) usando pincéis e alphas — o software converte essa informação de profundidade pintada em um Normal Map real na exportação.

O ponto central: AO e Curvature **não precisam de high-poly** — nascem da malha de jogo que os estudantes já modelaram, com seus bevels e reentrâncias. O Normal Map desta semana nasce de pintura de profundidade, não de matemática de ruído.

**2. Onde isso substitui e onde isso complementa o que foi visto na Semana 6**

O Albedo fotográfico ou estilizado da Semana 6 continua sendo a base de cor. O que muda é como as camadas seguintes (Roughness, Normal, variação de desgaste) são construídas: em vez de nós no Shader Editor do Blender, agora são camadas e máscaras dentro do 3D Coat, geradas a partir da própria malha.

**3. As duas trilhas — mesmo fluxo de ferramenta, abordagem diferente**

- **Trilha fotorrealista:** a textura fotográfica da Semana 6 entra como camada de Color base (projetada sobre o UV, que já é o mesmo UV do Blender). Por cima dela, AO e Curvature funcionam como camadas de multiplicação/máscara para reforçar sombra de contato e desgaste nas bordas — um refinamento físico sobre uma base que já é realista.
- **Trilha estilizada:** em vez de uma foto, o estudante aplica um Smart Material (ou monta uma camada de cor + variação manual, se a biblioteca de Smart Materials do laboratório for limitada) — e usa exatamente os mesmos mapas de AO/Curvature como máscara automática de onde a sujeira, o brilho e o desgaste devem aparecer. Quem já baixou um pacote de textura estilizada pronta na Semana 6 usa essa imagem como ponto de partida da camada de Color, do mesmo jeito que a trilha fotorrealista usa a foto.

Nos dois casos, o resultado técnico ao final da semana é equivalente: um material com Color, Roughness e Normal ativos no 3D Coat, com máscaras de AO/Curvature orientando onde o desgaste acontece.

**4. Os três espaços de trabalho do 3D Coat**

O 3D Coat organiza o trabalho em "Rooms" (salas):

- **Paint Room:** o principal espaço de trabalho. O artista pinta diretamente sobre a malha 3D usando pincéis, stencils, alphas e camadas com máscara, em qualquer canal PBR (Color, Roughness, Metallic, Normal/Depth).
- **UV Room:** visualização e edição básica de UVs já existentes. No workflow da disciplina os UVs já chegam prontos do Blender — o UV Room serve principalmente para conferir se o mapa importou corretamente.
- **Render Room:** visualização de renderização de alta qualidade com iluminação HDR, usada para avaliar o resultado antes de exportar.

**5. Geração procedural como técnica alternativa (panorama, 3 min)**

*"Existe um segundo caminho para gerar Normal e Roughness que vocês não vão usar hoje: nós matemáticos dentro do Blender — Noise Texture, Bump, ColorRamp — como a Apostila descreve no Capítulo 13 (Parte IV). É o mesmo princípio de raster vs. procedural que vimos na Semana 1, só que aplicado a mapas de suporte em vez do Albedo inteiro. A vantagem dos nós é que o material nunca repete um pixel duas vezes e pode ser ajustado sem repintar nada; a desvantagem é o controle artístico mais indireto. Quem quiser comparar as duas técnicas em uma segunda superfície do próprio Hero Asset, a leitura do Capítulo 13 fica disponível — mas a partir de hoje, o fluxo oficial da disciplina é o bake e a pintura dentro do 3D Coat."*

> **Leitura complementar recomendada (não avaliada nesta semana):** Apostila, Parte IV, Cap. 13 — Texturização Procedural.

---

### Demonstração — 20 minutos

**Migração para o 3D Coat: exportação, bake de AO/Curvature e início do Normal via Depth**

**Setup (1 min):**
Ter o Blender aberto com o asset de demonstração (parede simples com textura seamless de pedra já conectada ao Albedo, Semana 6). Ter o 3D Coat aberto em outra janela, pronto para importar.

**Percurso da demonstração:**

**Passo 1 — Exportação do Blender (2 min):**
1. Com o asset de demonstração selecionado: `File → Export → FBX (.fbx)` (preferir FBX quando houver mais de um objeto; `.obj` também funciona para um único objeto).
2. Confirmar que a UV está incluída na exportação.
3. Salvar em `[DEMO]_3DCoat_Exportacao/asset_demo.fbx`.

**Passo 2 — Importação no 3D Coat (3 min):**
1. `File → Import for Per-Pixel Painting` (ou `New Project → Per Pixel Painting`, dependendo da versão).
2. Selecionar o arquivo exportado.
3. Confirmar UV presente, resolução de textura **1024×1024**, workflow **Metalness PBR**.
4. Confirmar. A malha aparece no Paint Room.
5. Reconhecer rapidamente a interface: painel de Layers (direita), Toolbar (esquerda), canais ativos (Color, Roughness, Metallic, Normal/Depth).

**Passo 3 — Trazer a textura seamless da Semana 6 como camada de Color (3 min):**
1. Canal ativo: **Color**.
2. Criar nova camada, renomear para `Base_Color_Foto` (ou `Base_Color_Estilizada`, conforme o caso).
3. Usar a ferramenta de projeção/fill com a textura PNG exportada do Krita na Semana 6 (o UV já é o mesmo, então a projeção deve alinhar automaticamente).
4. Mostrar no Render Room: a base já parece muito próxima do que existia no Blender — só que agora dentro do 3D Coat.

**Passo 4 — Bake/geração de AO e Curvature (6 min):**
1. Localizar o painel de geração de mapas (nome exato varia por versão — geralmente dentro do menu Textures, ou como um tipo de camada procedural/"Fill Layer" com gerador).
2. Gerar o mapa de **Ambient Occlusion**: mostrar como as reentrâncias do asset escurecem automaticamente.
3. Gerar o mapa de **Curvature**: mostrar como as arestas ficam destacadas.
4. Criar uma nova camada `Desgaste_AO_Curvature`, modo Multiply, e usar o AO (ou o Curvature, invertido) como máscara para escurecer levemente as reentrâncias e clarear/saturar levemente as arestas.
5. *"Reparem: eu não pintei nada com a mão até agora. Essa profundidade toda veio da própria malha. A partir daqui, eu só refino."*

**Passo 5 — Normal Map via pintura de Depth (4 min):**
1. Mudar o canal ativo para **Depth/Normal**.
2. Selecionar um pincel com alpha de rachadura ou entalhe.
3. Pintar 2–3 marcas de profundidade sobre a superfície — uma rachadura, um entalhe de ferramenta.
4. Mostrar no Render Room: o relevo aparece como um Normal Map real, gerado pela pintura, não por ruído procedural.

**Passo 6 — Roughness rápido com Curvature como referência (2 min):**
1. Canal ativo: **Roughness**.
2. Fill com valor base (cinza escuro para pedra, roughness alto).
3. Nova camada usando a máscara de Curvature: clarear ligeiramente (roughness mais baixo = mais polido) nas arestas.

> **Nota do professor:** Se o bake de AO/Curvature não estiver disponível ou for instável na versão instalada, uma alternativa funcional é pintar manualmente com um pincel de opacidade baixa nas reentrâncias (escurecendo) e nas arestas (clareando), guiando-se visualmente pela geometria — o resultado pedagógico é equivalente, só perde a automação.

---

### Produção em Estúdio — 50 minutos

**Migração do Hero Asset Referência para o 3D Coat**

**Consigna entregue verbalmente:**

> *"O objetivo deste estúdio é migrar o Hero Asset Referência para o 3D Coat. Exportem do Blender, importem no 3D Coat, tragam sua textura da Semana 6 como camada de Color, gerem AO e Curvature, e pintem um primeiro passe de Normal via Depth. Se vocês são da trilha estilizada, esse é o momento de aplicar um Smart Material (ou montar as camadas equivalentes) usando AO/Curvature como máscara em vez de simplesmente colar a foto. O objetivo do estúdio é ter o Hero Asset Referência com pelo menos três canais ativos no 3D Coat: Color, Roughness e Normal."*

**Atividade estruturada:**

1. Exportar o Hero Asset Referência do Blender como `.obj`/`.fbx` com UV.
2. Importar no 3D Coat em Per-Pixel Painting, Metalness PBR, resolução 1024×1024.
3. Canal Color: criar camada base com a textura seamless da Semana 6 (trilha fotorrealista) ou com o Smart Material / camadas equivalentes escolhidos (trilha estilizada).
4. Gerar/bakear AO e Curvature a partir da malha.
5. Criar uma camada de desgaste usando AO/Curvature como máscara sobre o Color (escurecer reentrâncias, clarear/destacar arestas).
6. Canal Roughness: Fill base + camada guiada por Curvature (arestas mais polidas).
7. Canal Normal/Depth: pintar 2–3 marcas de profundidade (rachaduras, entalhes) coerentes com o tema do kit.
8. Salvar: `[Nome]_HeroAsset_3DCoat_S07.3b` (ou `.3dc`, dependendo da versão).

**Papel do professor:**

Circular e verificar três pontos em cada estação:

- **A base de Color está alinhada ao UV?** Se a projeção da textura da Semana 6 saiu distorcida ou deslocada, verificar se o UV exportado do Blender é o mesmo usado na criação da textura.
- **AO/Curvature estão sendo usados como máscara, não como cor final?** Erro comum: o estudante aplica o mapa de AO diretamente como Color, apagando a textura de base. Reforçar: AO/Curvature entram como camadas em modo Multiply/Overlay com opacidade controlada, por cima da base.
- **A trilha está sendo respeitada?** Estudante da trilha estilizada colando uma foto pura sem nenhuma intervenção de Smart Material, ou estudante da trilha fotorrealista pintando cor livre sem base fotográfica — os dois casos merecem uma pergunta de redirecionamento.

Perguntas de mediação circulante:

- *"Essa camada de AO está em que modo de mistura? Se estiver em Normal, ela vai substituir a cor em vez de escurecer por cima. Muda para Multiply."*
- *"Você usou o Curvature para clarear as arestas ou só pintou onde achou que ficava bonito? Ativa a visualização do próprio mapa de Curvature e compara com o que você pintou."*
- *"Essas marcas de profundidade que você pintou no Depth — elas contam uma história? Onde esse objeto seria mais golpeado ou riscado no universo do kit?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: crítica circulante com ênfase em leitura de profundidade e uso de máscara**

Esta é uma crítica informal. O professor conduz a turma por 4–5 estações, com foco em verificar se o bake de AO/Curvature e o Normal pintado adicionam credibilidade ao material — nas duas trilhas.

**Protocolo:**

**Abertura (2 min):**
Professor define o foco: *"Hoje vamos olhar para profundidade, mas gerada de um jeito novo — direto da malha, ou pintada com pincel, não por nó matemático. Três perguntas guiam a crítica: (1) o desgaste das arestas parece físico e consistente com a máscara de Curvature, ou parece aleatório? (2) as reentrâncias estão mais escuras de forma crível? (3) para quem é estilizado: o Smart Material está respondendo à geometria do asset, ou parece só um padrão colado por cima?"*

**Rodada circulante (15 min — 4–5 estações):**

- *"Onde esse material foi mais tocado, tem uma marca de desgaste visível? Ou está uniforme?"*
- *"Vocês conseguem apontar onde está a máscara de AO funcionando — algum canto que ficou mais escuro por causa da própria geometria?"*
- Para trilha estilizada: *"Esse Smart Material parece pintado para esse asset especificamente, ou parece um material genérico de biblioteca sem ajuste?"*
- Para trilha fotorrealista: *"A foto de base ainda é reconhecível, ou o desgaste pintado por cima já conta uma história própria do objeto?"*

**Fechamento da crítica (3 min):**
Sintetizar os padrões observados:
- Qual o erro mais comum na aplicação da máscara de AO/Curvature (tipicamente: opacidade excessiva escurecendo tudo, ou máscara não conectada corretamente ao modo de mistura)?
- Estado geral das duas trilhas — os materiais estão ganhando identidade e física de superfície?
- Orientação para o estúdio: *"Quem ainda não tem os três canais ativos: prioriza fechar isso primeiro. Quem já está satisfeito: usa o segundo estúdio para aprofundar o detalhe."*

---

### Produção em Estúdio — 60 minutos

**Refinamento e aprofundamento do material PBR do Hero Asset Referência**

**Consigna:**

> *"Sessenta minutos para fechar a semana com um material realmente convincente. Quem ainda não tem os três canais completos: prioriza fechar Color, Roughness e Normal. Quem já está satisfeito: reforça o Normal com mais marcas de Depth, experimenta ajustar a intensidade da máscara de Curvature, testa uma segunda variação de Smart Material ou textura, ou explora o canal Subsurface se o Hero Asset tiver um elemento orgânico (só exploração, sem cobrança de entrega — o SSS será formalizado na Semana 8)."*

**Atividade:**

**Parte 1 — Fechamento dos três canais para quem ainda não completou (≈30 min):**
1. Revisar Color: a base está alinhada ao UV e coerente com a trilha visual?
2. Revisar Roughness: valores fisicamente plausíveis, com variação guiada por Curvature.
3. Revisar Normal/Depth: pelo menos 2–3 marcas de profundidade coerentes com o tema.
4. Salvar: `[Nome]_HeroAsset_3DCoat_S07.3b` (atualizado).

**Parte 2 — Aprofundamento para quem já concluiu os três canais (≈60 min, ou tempo remanescente):**
1. Reforçar o Normal com uma segunda camada de Depth em escala menor (micro-detalhe sobre o macro-detalhe já pintado).
2. Ou: testar um Smart Material diferente sobre o Hero Asset e comparar visualmente com a versão atual — qual comunica melhor o material do kit?
3. Ou: para quem tiver um elemento orgânico no kit (planta, vela, tecido), localizar o canal Subsurface no 3D Coat e testar informalmente um valor baixo — sem cobrança de entrega.
4. Ou: comparar o resultado do bake de AO/Curvature do 3D Coat com a técnica alternativa de nós procedurais do Blender (Apostila, Cap. 13) em uma segunda superfície do próprio Hero Asset, para quem quiser explorar as duas vias.

**Papel do professor:**

- Para estudantes com Metallic incorreto: *"Em PBR físico, Metallic é quase binário: 0 para não-metais, 1 para metais puros. Ferrugem, por exemplo, é tratada como dielétrico (0) com a cor de ferrugem no Color, não como Metallic intermediário."*
- Para estudantes avançados: *"Testa aumentar a opacidade da máscara de Curvature no Roughness — o que muda na leitura de 'objeto usado' versus 'objeto novo'?"*
- Para todos: *"Esse material que vocês estão fechando hoje é o que vai para a Crítica Formal na semana que vem — ele já conta a história do objeto sozinho, sem vocês precisarem explicar?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese técnica)**
*"Hoje vocês montaram um material PBR completo pela primeira vez dentro do 3D Coat — com profundidade vinda da própria malha (AO, Curvature) e do pincel (Normal via Depth), não de nós matemáticos. Esse fluxo é o mesmo, foto ou estilizado — só muda o que vocês colocam na camada de Color. Na Semana 8 vocês vão refinar esse material e fechar a Unidade II com uma exportação completa dos quatro mapas PBR."*

2. **(3 min — Reflexão de processo)**
Pergunta para 2–3 voluntários: *"O Normal que vocês pintaram hoje — ele representa bem o material do kit? Alguém olhando o asset vai conseguir dizer o que aconteceu com esse objeto só pelo relevo? A máscara de AO/Curvature ajudou a contar essa história, ou vocês teriam feito diferente sem ela?"*

3. **(3 min — Antecipação da Semana 8)**
*"Na semana que vem: Crítica FORMAL — a CF2 do semestre. Vocês vão apresentar o material que construíram nas Semanas 6 e 7 no Hero Asset Referência, explicando a trilha escolhida e as decisões de máscara e desgaste. Depois, vamos refinar as camadas, unificar tudo — incluindo o Normal, que sai bakeado do 3D Coat para as duas trilhas — e exportar os quatro mapas PBR completos: Albedo, Metallic, Roughness e Normal. Preparem a autoavaliação antes do segundo encontro."*

4. **(2 min — Confirmação das entregas)**
Recapitular entregas com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Malha importada no 3D Coat sem UV visível ou com UV incorreto**
Acontece quando o arquivo exportado do Blender não incluiu a UV corretamente, ou quando o asset tem múltiplas UV layers. O sintoma é a malha aparecer com textura esticada ou uniforme no Paint Room. Estratégia: reexportar como `.fbx` (inclui UV automaticamente com menos configuração que `.obj`) ou verificar a opção "UV Coords" no export `.obj`. Conferir no UV Room se as ilhas aparecem dentro do quadrado 0–1.

**2. AO/Curvature aplicados como cor final em vez de máscara**
O estudante gera o mapa de AO e o conecta diretamente ao canal Color, apagando a textura de base da Semana 6. Estratégia: reforçar que AO e Curvature são sempre camadas auxiliares em modo Multiply/Overlay/Screen por cima da base — nunca a própria base.

**3. Normal Map via Depth muito sutil ou muito exagerado**
Pincéis de profundidade com força padrão podem gerar um relevo imperceptível (opacidade baixa) ou um relevo tipo "cratera" (opacidade/força alta). Estratégia: comparar com referência visual (foto ou concept art do mesmo material) e calibrar a força do pincel progressivamente, mostrando o antes/depois no Render Room a cada ajuste.

**4. 3D Coat lento ou travando no laboratório**
O 3D Coat é mais pesado que o Blender e pode ter performance reduzida em computadores com menos VRAM — e esse é o primeiro contato da turma com a ferramenta, então o impacto é maior nesta semana. Estratégia: usar resolução 512×512 em vez de 1024 nos computadores mais lentos — o fluxo é idêntico, apenas com menos detalhe. Orientar o estudante a trabalhar em 512 em aula e re-importar em 1024 em casa ou em computador mais potente para a entrega final.

**5. Estudante da trilha estilizada sem acesso a uma biblioteca de Smart Materials**
Nem todo laboratório tem uma biblioteca de Smart Materials instalada ou licenciada. Estratégia: o resultado técnico equivalente pode ser montado manualmente — camada de Color com a textura estilizada da Semana 6, camada de variação com Brush, e camada de desgaste usando AO/Curvature como máscara. O conceito pedagógico (máscara automática guiando desgaste) é o mesmo; só muda se a máscara aciona um material pronto ou uma camada montada à mão.

**6. Estudante avança rápido demais e chega ao Encontro 2 sem trabalho de aprofundamento definido**
Com um único asset como foco, alguns estudantes podem terminar os três canais básicos cedo e ficar sem direção. Estratégia: ter sempre pronta uma lista curta de aprofundamentos válidos (segunda camada de Depth, comparação de Smart Materials, exploração de SSS) para direcionar esse tempo, em vez de deixar o estudante ocioso.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não consegue identificar visualmente o efeito do AO/Curvature | *"Desliga a camada de máscara para ver o antes, liga para ver o depois. Se a diferença for mínima, a opacidade está baixa demais. Se parecer irreal (tudo escuro ou tudo brilhante), está alta demais."* |
| Camadas desorganizadas, sem nomenclatura, difícil de entender o que cada uma faz | *"Renomeia cada camada pelo que ela faz: Base_Color, AO_Desgaste, Roughness_Base. Em projeto real você vai reabrir esse arquivo daqui a duas semanas — se as camadas não tiverem nome, você vai perder tempo relembrando o que é o quê."* |
| Desgaste pintado/mascarado sem lógica de material | Abrir referência (foto ou concept art) ao lado do 3D Coat. *"Onde essa pedra [ou madeira, metal] seria mais tocada e desgastada na vida real? A máscara de Curvature já aponta as arestas — mas você decide a intensidade. Ela precisa representar isso, não só ser bonita."* |
| Metallic em valor intermediário incorreto (ex: 0.3 ou 0.5) | *"Em PBR físico, Metallic é quase binário: 0 para não-metais, 1 para metais puros. Qual é o caso do seu material? Provavelmente 0 ou 1."* |
| Estudante que terminou cedo e quer explorar mais | Propor reforçar o Normal com uma segunda camada de Depth em escala menor (micro sobre macro), ou comparar o resultado do bake com a técnica alternativa de nós do Blender em uma segunda superfície do Hero Asset. |
| Turma geral com dificuldade na navegação do 3D Coat (primeiro contato) | Fazer pausa de 5 minutos para rever os três controles de navegação no projetor: orbitar (botão do meio), zoom (scroll), pan (Shift + botão do meio). Comparar explicitamente com o Blender. Depois voltar ao estúdio. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Hero Asset Referência importado no 3D Coat com Color, Roughness e Normal ativos, qualquer que seja a trilha visual | C4 — Materiais PBR | Verificar no Paint Room/Render Room: os três canais têm pelo menos uma camada com conteúdo (não apenas a camada Base vazia) |
| Camada(s) de desgaste guiadas por AO e/ou Curvature sobre o Color e o Roughness | C5 — Texturização | Comparar o material com e sem as camadas de máscara habilitadas: a diferença deve ser perceptível e coerente com a geometria (reentrâncias mais escuras, arestas mais desgastadas) |
| Normal Map gerado por pintura no canal Depth, com micro-relevo visível e escala coerente com o material do kit | C5 — Texturização | Comparar o render com e sem as marcas de Depth habilitadas: a diferença deve ser perceptível sem ser exagerada |
| Coerência da abordagem (fotorrealista ou estilizada) com o moodboard do kit | C2 — Direção Artística | A base de Color e o tratamento de desgaste comunicam a trilha visual pretendida, sem mistura acidental de linguagem |
| Camadas organizadas e nomeadas por função | C1 — Processo de Projeto | Verificar nomenclatura das camadas no painel Layers; presença de registro visual (screenshot) do material antes e depois do bake |
| Participação na crítica: identificar uso correto ou incorreto de máscara de AO/Curvature no trabalho de colega | C10 — Participação | Qualidade da observação — especificidade técnica (opacidade excessiva, máscara desconectada do modo de mistura) em vez de comentário genérico |

---

## Entrega da Semana 7

| Entrega | Formato | Prazo |
|---|---|---|
| Hero Asset Referência no 3D Coat com material PBR (Color + Roughness + Normal ativos, trilha visual definida) | `.3b`/`.3dc` com sufixo `_HeroAsset_3DCoat_S07` | Até o fim do segundo encontro |
| Screenshot do painel de Layers do Hero Asset Referência (camadas nomeadas visíveis) | `.png` com sufixo `_Layers_S07` | Até o fim do segundo encontro |
| Screenshot de render comparativo do Hero Asset Referência: antes/depois das máscaras de AO/Curvature e do Normal via Depth | `.png` com sufixos `_semMascara_S07` e `_comMascara_S07` | Até o fim do segundo encontro |

> **Nota:** Não há crítica formal nesta semana. O estado do material será consolidado no início da Semana 8, antes da crítica formal (CF2).

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 7 | 2026*
