# Plano de Aula — Semana 8
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** II — Materiais PBR e Workflow  
**Tema:** Workflow no 3D Coat: camadas, projeção e exportação PBR  
**Apostila:** Cap. 6 — Introdução ao 3D Coat; Workflow de texturização PBR: camadas e exportação  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔴 FORMAL — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 com material PBR completo no Blender: Albedo (textura seamless), Metallic (valor calibrado), Roughness (Noise + ColorRamp), Normal (Noise + Bump) — Semana 7
- Asset 02 com material PBR avançado (mínimo: Albedo + Normal + Roughness) — Semana 7
- Node trees organizados em frames nomeados e screenshots de render comparativo antes/depois do Normal Map
- UV layouts dos Assets 01 e 02 já otimizados e validados com checkerboard (Semanas 2–4)
- Autoavaliação da Semana 8 **preenchida e entregue antes do segundo encontro** — requisito da crítica formal

> **Nota de transição:** A Semana 7 fechou o primeiro material PBR completo montado internamente no Blender via nós procedurais. Esta semana marca a entrada em uma ferramenta dedicada à texturização: o 3D Coat. A diferença fundamental é de fluxo: no Blender, o material é uma rede de nós matemáticos que geram aparência em tempo real no viewport; no 3D Coat, o artista pinta diretamente sobre a malha 3D, canal por canal, e exporta mapas de imagem reais que podem ser usados em qualquer motor ou ferramenta. Os estudantes já compreendem o que cada canal PBR representa — agora vão controlar esses canais com pincel e camadas, não com nós.

> **Orientação sobre autoavaliação:** A autoavaliação deve ser distribuída digitalmente ou em papel **ao final do primeiro encontro**, para que os estudantes possam preenchê-la antes do segundo encontro. O professor deve comunicar claramente que a autoavaliação é pré-requisito de participação na crítica formal — quem chegar sem ela preenche no lugar antes de apresentar, perdendo tempo de produção.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Identificar os principais espaços de trabalho do 3D Coat (Paint Room, UV Room, Render Room) e sua função no pipeline de texturização.
2. Importar um asset com UV mapeado do Blender para o 3D Coat no modo Per Pixel Painting (PBR workflow).
3. Navegar no sistema de camadas do 3D Coat e criar camadas separadas para cada tipo de informação (cor base, variação de Roughness, variação de Metallic).
4. Pintar os canais PBR básicos diretamente sobre a malha 3D: Color (Albedo), Roughness e Metallic.
5. Exportar os mapas PBR gerados no 3D Coat (Albedo, Roughness, Metallic) em resolução e formato adequados.
6. Configurar o material no Blender utilizando os mapas exportados pelo 3D Coat no lugar dos nós procedurais da semana anterior.
7. (Crítica formal) Apresentar e defender oralmente as decisões de material tomadas durante as Semanas 5–7, utilizando vocabulário técnico correto e a autoavaliação como ponto de partida.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Qualidade da documentação entregue à crítica: organização de pasta, versões salvas, registro visual do processo das Semanas 5–7; incorporação de feedbacks anteriores visível nas iterações |
| C2 — Direção Artística | Coerência da paleta e proposta estética ao longo dos dois assets apresentados; capacidade de verbalizar as escolhas visuais durante a crítica |
| C4 — Materiais PBR | Material PBR construído no Blender (Semanas 5–7) avaliado na crítica formal; início da transição para mapas pintados no 3D Coat |
| C5 — Texturização | Primeiros mapas pintados no 3D Coat: qualidade da cor base, coerência do Roughness pintado, distinção visual entre áreas do material |
| C9 — Apresentação | Qualidade e organização da apresentação na crítica formal: breakdown visual, clareza da defesa oral, uso da autoavaliação |
| C10 — Participação | Qualidade das perguntas e feedbacks oferecidos durante a crítica dos colegas; postura de recepção e negociação de feedback sobre o próprio trabalho |

> **Janela A2 em andamento (Semanas 6–11):** Esta é a terceira semana da janela A2. C5 (Texturização) tem peso crescente e esta semana inicia sua avaliação substantiva com os primeiros mapas pintados no 3D Coat. C9 (Apresentação) é avaliado formalmente pela primeira vez nesta semana — a crítica formal é o momento em que o estudante demonstra não apenas o que produziu, mas como articula suas decisões.

---

## Recursos necessários

- Computadores com 3D Coat instalado (versão 2023 ou superior recomendada)
- Computadores com Blender instalado (3.x ou 4.x) — para configurar o material ao final do estúdio
- Arquivos `.blend` dos Assets 01 e 02 com UVs e materiais das semanas anteriores
- Arquivo de demonstração do professor: asset simples (parede ou cubo) com UV já aberto, exportado como `.obj` ou `.fbx`
- Projetor para demonstração e para a crítica formal
- Fichas de Crítica Formal impressas (Instrumento 1 da Rubrica Mestre) — uma por estudante apresentado
- Fichas de Autoavaliação preenchidas pelos estudantes (Instrumento 2 da Rubrica Mestre)
- Apostila Cap. 6 — disponibilizada antes da aula
- Pasta de exportação criada previamente no computador de demonstração do professor: `[DEMO]_3DCoat_Exportacao/`

> **Nota sobre versões do 3D Coat:** A interface do 3D Coat passou por reorganizações significativas entre versões. Verificar a versão instalada no laboratório antes da aula e adaptar os atalhos e nomes de menu conforme necessário. Os princípios de fluxo (importar → pintar por canal → exportar) são estáveis entre versões, mas nomes de painéis podem variar (ex: "Texture Editor" vs "UV Room" em versões mais antigas).

> **Nota sobre formato de exportação do Blender:** Para importar no 3D Coat, o asset deve ser exportado como `.obj` (com UV) ou `.fbx`. No Blender: `File → Export → Wavefront (.obj)` ou `FBX (.fbx)`. Verificar que a opção "UV Coords" está marcada no export `.obj`. O 3D Coat também pode importar `.fbx` com UV incorporado — preferir `.fbx` se a malha tiver múltiplos objetos.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**O 3D Coat no pipeline: de malha com UV a mapas PBR pintados**

Objetivo: posicionar o 3D Coat dentro do pipeline da disciplina e apresentar sua lógica de trabalho central, sem exigir que os estudantes já estejam com o software aberto neste momento. A comparação com o que foi feito no Blender é o fio condutor — os estudantes já sabem o que são os canais PBR; agora vão entender como o 3D Coat os trata.

**Desenvolvimento:**

Abrir com a seguinte pergunta para a turma: *"Na semana passada, vocês criaram um material PBR no Blender usando nós — Noise Texture, Bump, ColorRamp. Se eu abrir o arquivo de vocês em outro computador e exportar esse asset para a Unity, o material vai junto? Ou precisa ser convertido em alguma coisa?"*

Deixar a turma responder brevemente. A resposta esperada é: os nós funcionam dentro do Blender, mas para exportar para Unity é necessário ter mapas de imagem reais (PNG ou TGA). O 3D Coat é a ferramenta que permite criar esses mapas de forma direta e intuitiva — pintando na superfície do asset.

---

**Conteúdo a cobrir:**

**1. Onde o 3D Coat entra no pipeline**

No pipeline da disciplina: Blender (modelagem + UV) → **3D Coat (texturização)** → Unity (motor).

O 3D Coat recebe a malha com UV do Blender e devolve mapas de imagem (PNG/TGA) que representam cada canal PBR. Esses mapas são então conectados ao material no Blender ou diretamente na Unity.

A diferença fundamental em relação ao workflow de nós da Semana 7: os nós procedurais geram aparência matematicamente a cada render — eles são "virtuais". Os mapas do 3D Coat são imagens reais, permanentes, portáveis para qualquer software. Um mapa exportado do 3D Coat pode ser aberto no Photoshop, editado no Krita, conectado na Unity ou no Unreal sem nenhuma conversão adicional.

**2. Os três espaços de trabalho principais**

O 3D Coat organiza o trabalho em "Rooms" (salas), cada uma com ferramentas e painéis especializados:

- **Paint Room:** o principal espaço de trabalho. Aqui o artista pinta diretamente sobre a malha 3D usando pincéis, stencils e alphas. O Paint Room exibe a malha em perspectiva 3D e permite pintar em qualquer canal PBR (Color, Roughness, Metallic, Normal, etc.) com o mesmo conjunto de ferramentas.

- **UV Room:** visualização e edição básica de UVs já existentes. O 3D Coat pode abrir o mapa UV plano e permite ajustes, mas no workflow da disciplina os UVs já chegam prontos do Blender — o UV Room serve principalmente para conferir se o mapa importou corretamente.

- **Render Room:** visualização de renderização de alta qualidade dentro do 3D Coat, com materiais PBR em iluminação HDR. É usado para avaliar o resultado final antes de exportar, especialmente a interação entre os diferentes canais pintados.

**3. O sistema de camadas e canais no 3D Coat**

O Paint Room trabalha com um sistema de camadas similar ao Photoshop ou Krita — empilhadas de baixo para cima, com modos de mistura (Normal, Multiply, Overlay, etc.) e opacidade. A diferença fundamental: cada camada no 3D Coat não armazena apenas cor — ela armazena informação para **múltiplos canais simultaneamente**.

Cada camada pode conter dados para: Color (Albedo), Roughness, Metallic, Normal/Depth, Opacity. Ao pintar, o artista escolece qual canal está ativo no momento — mas a estrutura de camadas é compartilhada.

Analogia: *"É como se cada camada do Krita tivesse várias 'sub-imagens' invisíveis uma atrás da outra. Quando você pinta no canal de Color, só o Color é afetado. Quando você pinta no canal de Roughness, apenas o Roughness muda — a estrutura de camadas permanece a mesma."*

**4. O workflow da aula em quatro etapas**

1. **Exportar** o asset do Blender como `.obj` ou `.fbx` (com UV)
2. **Importar** no 3D Coat em modo Per Pixel Painting (PBR workflow)
3. **Pintar** os canais: Color (cor base do material), Roughness (variação de rugosidade), Metallic (presença de metal)
4. **Exportar** os mapas como PNG e **conectar** no material do Blender (substituindo os nós procedurais da Semana 7)

> **Nota do professor:** A Mini Aula desta semana é mais descritiva do que conceitual — os estudantes já compreendem os canais PBR pela Semana 5. O foco é contextualizar a ferramenta e estabelecer a lógica antes de ver ao vivo na demonstração. Manter o ritmo e não detalhar demais as funções do Paint Room — a demonstração cobre isso de forma visual e mais eficiente.

---

### Demonstração — 20 minutos

**Importação, pintura de camadas PBR e exportação no 3D Coat**

**Setup (1 min):**  
Abrir o 3D Coat com o arquivo de demonstração já preparado: asset simples (parede de pedra ou caixa de madeira) com UV feito no Blender, exportado como `.obj`. Ter o Blender aberto em outra janela com o material de nós da Semana 7 visível para comparação ao final.

**Percurso da demonstração:**

**Passo 1 — Importação no modo correto (3 min):**
1. No 3D Coat: `File → Import for Per-Pixel Painting` (ou `New Project → Per Pixel Painting`)
2. Navegar até o arquivo `.obj` do asset de demonstração.
3. Na janela de importação: confirmar que o UV está presente (3D Coat detecta automaticamente), selecionar resolução de textura: **1024×1024** para esta aula (explicar: *"Em produção usaríamos 2048 — para a aula, 1024 é suficiente e mais rápido para navegar"*).
4. Selecionar workflow: **Metalness PBR** (não Specular/Glossiness).
5. Confirmar. A malha aparece no Paint Room com UV mapeado.

**Passo 2 — Reconhecimento da interface do Paint Room (3 min):**
1. Mostrar os painéis principais:
   - **Layers** (direita): o painel de camadas — vazio por enquanto, com uma camada Base.
   - **Toolbar** (esquerda): ferramentas de pintura — Brush, Fill, Clone, etc.
   - **Brush settings** (parte superior): tamanho, opacidade, suavidade.
   - **Canais ativos** (parte superior ou lateral dependendo da versão): botões para alternar entre Color, Roughness, Metallic, Normal. Mostrar como mudar o canal ativo.
2. Girar a malha no viewport com botão do meio do mouse: *"A navegação no 3D Coat é similar ao Blender — scroll para zoom, botão do meio para orbitar."*

**Passo 3 — Pintura do canal Color (Albedo) (5 min):**
1. No painel Layers: renomear a camada Base para `Base_Color`.
2. Confirmar que o canal ativo é **Color**.
3. Usar a ferramenta Fill com a cor base do material (ex: cinza pedra ~#8a8580).
4. Criar nova camada: `Camada_Variacao_Cor`. Modo: Overlay. Opacidade: 60%.
5. Com Brush em tamanho grande e opacidade baixa (~30%), pintar variações sutis de ton na superfície — zonas mais escuras, zonas mais quentes.
6. Resultado: a cor deixa de ser uniforme e passa a ter micro-variação. *"Isso é o que evita o aspecto de plástico — nenhuma superfície real é uma cor sólida perfeita."*

**Passo 4 — Pintura do canal Roughness (4 min):**
1. Mudar o canal ativo para **Roughness**.
2. Criar nova camada: `Base_Roughness`. Usar Fill com valor **cinza escuro** (roughness alto ≈ 0.7–0.8 para pedra).
3. *"No 3D Coat, o Roughness é codificado como imagem em escala de cinza: branco = muito rough (matte), preto = muito liso (reflexivo). É o mesmo princípio do Principled BSDF."*
4. Nova camada: `Roughness_Desgaste`. Com Brush, pintar pequenas áreas de roughness mais baixo (cor mais clara = mais liso) nas arestas e projeções do asset — onde o material seria mais polido pelo uso.
5. Mostrar no Render Room: *"Olha como as arestas ficaram levemente mais reflexivas. Isso é desgaste pintado."*

**Passo 5 — Exportação dos mapas (3 min):**
1. `File → Export Textures` (ou Export Color/Roughness/Metallic separadamente, dependendo da versão).
2. Mostrar a janela de exportação: selecionar Albedo (Color), Roughness, Metallic.
3. Formato: **PNG**, resolução: **1024×1024** (mesma da importação).
4. Destinar para a pasta `[DEMO]_3DCoat_Exportacao/`. Confirmar exportação.
5. Abrir a pasta no explorador: mostrar os três arquivos PNG gerados — `Asset_Albedo.png`, `Asset_Roughness.png`, `Asset_Metallic.png`.

**Passo 6 — Conexão no Blender (2 min, rápido):**
1. Mudar para o Blender com o material de nós da Semana 7 aberto.
2. No Shader Editor: `Shift+A → Texture → Image Texture`. Abrir `Asset_Albedo.png`.
3. Conectar ao `Base Color` do Principled BSDF (substituindo o nó de textura seamless anterior).
4. Repetir para Roughness: `Image Texture → Roughness`. Lembrar: mudar o Color Space para **Non-Color**.
5. Mostrar o viewport Rendered: *"O material agora usa os mapas pintados no 3D Coat. O que vocês pintam lá, aparece aqui — e vai aparecer na Unity da mesma forma."*

> **Nota do professor:** Não é necessário completar a conexão do Metallic durante a demonstração se o tempo apertar. Priorizar Albedo e Roughness — são os canais que os estudantes vão trabalhar no estúdio. O Metallic para muitos kits será 0 (não-metálico), então pode ser apenas um valor no Principled BSDF sem mapa dedicado.

---

### Produção em Estúdio — 50 minutos

**Importação do Asset 01 no 3D Coat e início da pintura dos canais PBR**

**Consigna entregue verbalmente:**

> *"O objetivo deste estúdio é ter o Asset 01 importado no 3D Coat e com os três canais básicos iniciados: Color, Roughness e Metallic. Não precisa estar terminado — o segundo encontro tem mais 60 minutos de estúdio. O foco agora é dominar o fluxo: exporta do Blender, importa no 3D Coat, cria camadas, pinta os canais. Antes de sair daqui, quero ver os três canais com pelo menos uma camada base pintada. Façam isso pela ordem da demonstração: primeiro Color, depois Roughness, depois Metallic."*

**Atividade estruturada:**

**Etapa 1 — Exportação do Asset 01 do Blender (≈5 min):**
1. Abrir o `.blend` do Asset 01 com UV otimizado das Semanas 3–4.
2. `File → Export → Wavefront (.obj)` ou `FBX (.fbx)`.
3. Confirmar que "UV Coords" está marcado (no `.obj`) ou que a UV Layer está incluída (no `.fbx`).
4. Salvar em pasta de trabalho local: `[Nome]_Asset01_Para3DCoat/`.
5. Verificar que o arquivo exportado não está vazio (peso mínimo esperado: alguns KB).

**Etapa 2 — Importação no 3D Coat (≈5 min):**
1. `File → Import for Per-Pixel Painting`.
2. Selecionar o arquivo exportado.
3. Resolução: **1024×1024** (pode avançar para 2048 em computadores mais potentes — verificar com o professor).
4. Workflow: **Metalness PBR**.
5. Confirmar importação. Verificar que a malha aparece com UV no Paint Room.

**Etapa 3 — Pintura do canal Color (≈15 min):**
1. No painel Layers, renomear a camada base para `Base_Color`.
2. Canal ativo: **Color**.
3. Usar Fill com a cor base dominante do material do kit (pedra: cinza; madeira: marrom; metal: cinza escuro com tom frio).
4. Criar camada de variação: `Variacao_Cor`, modo Overlay ou Multiply, opacidade 40–60%.
5. Com brush de tamanho médio e opacidade baixa, pintar variações de ton: zonas mais escuras, zonas de acumulação de cor diferente.
6. Salvar o arquivo do 3D Coat: `[Nome]_Asset01.3b` (ou `.3dc` dependendo da versão).

**Etapa 4 — Pintura do canal Roughness (≈15 min):**
1. Mudar canal ativo para **Roughness**.
2. Camada base: `Base_Roughness`. Fill com valor de roughness base do material:
   - Pedra não-polida: ~cinza escuro (roughness 0.7–0.8)
   - Madeira não-envernizada: ~cinza médio (roughness 0.6–0.75)
   - Metal oxidado: ~cinza escuro (roughness 0.65–0.85)
3. Camada de desgaste: `Roughness_Desgaste`. Pintar arestas e projeções com valor mais claro (mais liso) onde o uso deixaria o material polido.
4. Verificar no Render Room: a variação de brilho entre zonas deve ser visível.

**Etapa 5 — Canal Metallic (≈5 min):**
1. Canal ativo: **Metallic**.
2. Para materiais não-metálicos (pedra, madeira, concreto): Fill com preto puro (Metallic = 0). **Não pintar nada adicional.**
3. Para materiais metálicos (ferro, aço): Fill com branco puro (Metallic = 1). Pintar com preto áreas de ferrugem ou tinta onde o metal ficaria exposto.
4. Para materiais mistos: apenas preencher as zonas corretas — sem gradientes suaves, pois Metallic em PBR é quase binário.

**Etapa 6 — Salvar e documentar (≈5 min):**
1. Salvar o arquivo do 3D Coat: `[Nome]_Asset01_S08.3b`.
2. Tirar screenshot do Paint Room com o asset pintado visível.
3. Tirar screenshot do Render Room mostrando o resultado das camadas combinadas.

**Papel do professor:**

Circular verificando três pontos em cada estação:

- **O canal ativo está correto?** Erro mais comum: pintar no canal errado (ex: pintar cor enquanto o canal ativo é Roughness). O resultado é que o Roughness recebe informação de cor e o Color permanece vazio. Verificar o indicador de canal ativo na interface.
- **A variação de Roughness é perceptível?** Uma camada base de Fill uniforme sem camada de variação resulta em roughness idêntico ao que existia na Semana 7. Orientar a criar a segunda camada com brush antes de avançar.
- **O Metallic está correto para o material?** Para kits Medieval, Fantasia ou pós-apocalíptico, a maioria dos assets de pedra e madeira deve ter Metallic = 0. Estudantes que colocam Metallic em valores intermediários em pedra ou madeira devem ser orientados.

Perguntas de mediação circulante:

- *"Qual é a lógica do Roughness nesse material — onde ele seria mais desgastado pelo uso? Pinta primeiro em referências visuais na mente, depois no 3D Coat."*
- *"Esse Fill do Roughness está muito claro — seu material parece plástico brilhante agora. O range de roughness para [pedra/madeira] é mais alto. Qual valor faz sentido?"*
- *"Você está com quantas camadas no Color? Uma só de Fill? Cria uma segunda de variação antes de avançar — sem variação de cor, o material ainda parece uniforme."*

> **Orientação ao final do Estúdio 1:** Comunicar que a autoavaliação deve ser preenchida antes do segundo encontro. Distribuir o Instrumento 2 (Autoavaliação) neste momento se ainda não foi distribuído. Lembrar que a crítica formal começa o segundo encontro — quem chegar sem autoavaliação perde tempo de estúdio para preenchê-la.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva FORMAL — 20 minutos

**Formato: Crítica formal com rubrica, autoavaliação e feedback escrito do professor**

Esta é a terceira crítica formal do semestre (após Semanas 3 e 5). O objeto da crítica é o trabalho das Semanas 5–7: material PBR construído no Blender (Principled BSDF com todos os canais conectados). Os primeiros resultados do 3D Coat (estúdio do Encontro 1) podem ser incluídos como contexto, mas não são o foco avaliativo desta crítica.

**Protocolo:**

**Preparação (antes do início — 2 min antes):**
- Professor confere se todos têm a autoavaliação preenchida. Quem não tem: preenche agora, em 5 minutos, antes de qualquer outra atividade.
- Fichas de Crítica Formal (Instrumento 1) separadas por estudante.
- Projetor ligado e pronto para receber o arquivo do estudante.

**Abertura (2 min):**
Professor define o contexto e os critérios em foco:
*"Esta é a crítica formal da Unidade II. Vocês vão apresentar o material PBR que construíram no Blender nas últimas três semanas. Quero ouvir de cada um: qual material é esse, quais canais estão conectados, e uma escolha que vocês fizeram — de roughness, de variação de cor, de Normal Map — e por que fizeram essa escolha. Depois a turma comenta. Cada apresentação tem dois minutos."*

Os critérios observados hoje: C1 (processo e documentação), C2 (coerência artística), C4 (materiais PBR), C5 (início da texturização), C9 (apresentação oral).

**Rodada de apresentações (15 min — ≈3–4 estudantes, 2 min cada + 1–2 min de feedback):**

Para cada apresentação:

1. **O estudante apresenta** (2 min):
   - Projeta o asset com o material PBR no viewport Rendered do Blender (ou render estático).
   - Descreve: o material, os canais conectados, e uma decisão técnica ou artística que tomou.
   - Lê a própria autoavaliação: o critério em que se avaliou mais alto e o critério em que se avaliou mais baixo, com justificativa.

2. **Feedback da turma** (1 min):
   - Uma pergunta ou observação específica de qualquer colega.
   - O professor pode complementar ou direcionar: *"Alguém vê algo no Roughness que poderia ser diferente?"*

3. **Feedback escrito do professor** (preenchido durante a apresentação na ficha):
   - C4 — O material tem plausibilidade física? Os valores dos canais fazem sentido para o material representado?
   - C5 — Há variação visual? O Normal Map adiciona credibilidade?
   - C9 — A apresentação foi clara e estruturada? O estudante conseguiu justificar as decisões?
   - Ponto forte + prioridade de melhoria.

> **Nota sobre o tempo:** Com turmas grandes (mais de 12 estudantes), não é possível apresentar todos na crítica formal de 20 minutos. Neste caso: sortear 3–4 estudantes para apresentar formalmente e usar a avaliação das Fichas de Crítica como registro para todos os demais. Alternativa: semanas com crítica formal podem ter a crítica expandida para 30 min retirando 10 min do estúdio 2.

**Fechamento da crítica (2 min):**
Sintetizar os padrões observados:
- Qual o critério em que a turma está mais forte? (tipicamente C4 — os materiais PBR estão funcionalmente corretos)
- Qual o critério com maior gap entre autoavaliação e avaliação do professor? (tipicamente C9 — estudantes subavaliam a própria capacidade de apresentação ou C2 — autoavaliam acima no artístico)
- Uma orientação para o estúdio: *"O que ficou mais claro na crítica é [X]. Levem isso para o 3D Coat agora — o que vocês vão pintar deve responder a esse ponto."*

---

### Produção em Estúdio — 60 minutos

**Continuação da texturização no 3D Coat + exportação e configuração no Blender**

**Consigna:**

> *"Sessenta minutos para três objetivos: (1) refinamento das camadas do Asset 01 no 3D Coat — quem chegou com as três camadas base, agora adiciona variação; (2) exportação dos mapas PBR; (3) conexão no Blender e comparação com o material de nós da semana passada. Quem terminar o Asset 01 e tiver tempo: inicia o Asset 02 no 3D Coat com o mesmo fluxo."*

**Atividade estruturada:**

**Bloco 1 — Refinamento das camadas no 3D Coat (≈25 min):**

Para o canal **Color**:
1. Verificar se há pelo menos duas camadas: base (Fill) + variação (Brush com opacidade baixa).
2. Adicionar, se possível, uma terceira camada de detalhe focal: `Detalhe_Cor`, modo Multiply ou Overlay, opacidade 20–30%. Pintar detalhes específicos do tema — sombras de fissuras, manchas de umidade, concentração de cor em áreas de desgaste.
3. Avaliar no Render Room: a cor tem história? Parece que o objeto foi usado?

Para o canal **Roughness**:
1. Verificar as duas camadas: base + desgaste em arestas.
2. Adicionar camada de sujeita/acúmulo: `Roughness_Sujeira`. Pintar em áreas baixas e côncavas com valor mais alto (mais rugoso = acúmulo de sujeira/pó). Modo: Multiply. Opacidade: 40–50%.
3. Resultado esperado: três zonas de Roughness distintas — arestas (polidas), face principal (roughness base), cavidades e partes baixas (muito rugosas).

Para o canal **Metallic**:
1. Para materiais não-metálicos: confirmar que está preenchido com preto. Sem alterações necessárias.
2. Para materiais metálicos ou mistos: verificar que as transições entre metal e não-metal seguem lógica física (ferrugem = não-metal com cor de ferrugem no Albedo, não Metallic intermediário).

**Bloco 2 — Exportação dos mapas PBR (≈10 min):**
1. `File → Export Textures`.
2. Mapas a exportar: **Color (Albedo)**, **Roughness**, **Metallic**.
3. Formato: PNG.
4. Resolução: mesma da importação (1024×1024).
5. Pasta de destino: `[Nome]_Asset01_Mapas_S08/`.
6. Confirmar exportação. Verificar no explorador de arquivos que os três PNGs foram gerados com tamanho esperado (mínimo: alguns KB para mapas 1024×1024).

**Bloco 3 — Configuração do material no Blender com os mapas exportados (≈20 min):**
1. Abrir o `.blend` do Asset 01 com o material de nós da Semana 7.
2. No Shader Editor, **não deletar** os nós da Semana 7 ainda — desabilitar os frames temporariamente com `M` para comparar ao final.
3. Criar um novo material ou duplicar o existente: `[Nome]_Asset01_3DCoat`.
4. Adicionar três nós `Image Texture`:
   - Abrir `Asset_Albedo.png` → conectar ao `Base Color`
   - Abrir `Asset_Roughness.png` → **mudar Color Space para Non-Color** → conectar ao `Roughness`
   - Abrir `Asset_Metallic.png` → **mudar Color Space para Non-Color** → conectar ao `Metallic`
5. Manter o Normal Map procedural da Semana 7 conectado (o 3D Coat não gerou Normal Map ainda — isso virá nas semanas seguintes).
6. No Viewport Rendered: comparar o material com mapas do 3D Coat vs. o material procedural da Semana 7 (habilitar/desabilitar os frames alternadamente).
7. Salvar: `[Nome]_Asset01_3DCoat_S08.blend`.
8. Capturar screenshot do material com mapas do 3D Coat e do node tree simplificado (sem os nós procedurais).

**Bloco 4 — Início do Asset 02 no 3D Coat (se houver tempo — ≈5 min):**
Para estudantes que terminaram o fluxo completo do Asset 01:
1. Exportar Asset 02 do Blender.
2. Importar no 3D Coat (novo projeto ou nova cena).
3. Pintar ao menos a camada base do canal Color.
4. Salvar como `[Nome]_Asset02_3DCoat_S08.3b`.

**Papel do professor:**

- Para estudantes com mapa de Roughness muito uniforme: *"Abre o Render Room. Onde tem diferença de brilho na superfície? Se não tem diferença visível, volta para o Paint Room e intensifica o contraste entre as camadas de Roughness."*
- Para estudantes com Roughness exportado que parece idêntico ao base: *"O que foi exportado tem variação? Abre o PNG no explorador e vê se tem tons diferentes — se o PNG estiver uniforme, a camada de variação não foi pintada com intensidade suficiente."*
- Para estudantes com Color Space errado no Blender: *"O mapa de Roughness está conectado mas o material parece excessivamente reflexivo ou matte demais? Verifica o Color Space do nó Image Texture — precisa estar em Non-Color para mapas que não são Albedo."*
- Para estudantes avançados: *"Você tem o Normal Map procedural da semana passada conectado e os mapas do 3D Coat. São duas fontes diferentes. O que acontece se você desabilitar o Normal Map procedural? O material muda muito? O que você prefere — e por quê?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese da semana)**
*"Hoje vocês cruzaram a fronteira mais importante do pipeline: saíram do mundo dos nós e entraram no mundo dos mapas pintados. O 3D Coat é a ferramenta que vai acompanhar vocês pelo resto do semestre — nas próximas semanas vocês vão pintar desgaste, aplicar stencils, integrar mapas de bake. O fluxo que fizeram hoje — importar, pintar, exportar, conectar — é a base de tudo que vem pela frente."*

2. **(3 min — Reflexão comparativa)**
Pergunta para 2–3 voluntários: *"Compara o material que vocês tinham no Blender no final da Semana 7 com o material de agora, com os mapas do 3D Coat. Visualmente, o que melhorou? O que ficou diferente — não necessariamente melhor, só diferente? O que o 3D Coat permite que o nó procedural não permite?"*

Orientar para que a reflexão conecte a diferença técnica (mapa de imagem vs. nó matemático) com a diferença artística (controle intencional de pintura vs. padrão gerado por ruído).

3. **(3 min — Antecipação da Semana 9)**
*"Na semana que vem: texturização artística — desgaste, sujeira e variação de cor pintados com intenção. Vocês vão aprender edge wear, dirt e a lógica de leitura de silhueta. Antes de chegar na Semana 9, olhem o moodboard de vocês — o tema do kit pede um material envelhecido? Destruído? Novo? Essa decisão vai guiar onde vocês pintam o desgaste. Venham com uma resposta clara: qual é a história do objeto no universo do kit?"*

4. **(2 min — Confirmação das entregas)**
Recapitular as entregas com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Malha importada no 3D Coat sem UV visível ou com UV incorreto**
Acontece quando o arquivo `.obj` foi exportado sem a opção "UV Coords" marcada, ou quando o asset tem múltiplas UV layers e o 3D Coat importa a errada. O sintoma é a malha aparecer com textura esticada ou uniforme no Paint Room. Estratégia: verificar o export no Blender (reexportar com UV Coords ativado) ou usar a exportação `.fbx` que inclui UV automaticamente. No 3D Coat, verificar no UV Room se as ilhas aparecem dentro do quadrado 0–1.

**2. Canal ativo trocado — pintura vai para o canal errado**
É o erro mais frequente em primeiros contatos com o 3D Coat. O estudante pinta cor enquanto o canal ativo é Roughness, ou vice-versa. O resultado é um mapa de Roughness com informação de cor (que vai parecer ruído multicolorido quando exportado) e um Color vazio. Estratégia: verificar sempre o indicador de canal ativo antes de cada sessão de pintura. Criar o hábito de verificar: *"Qual canal está ativo agora?"* antes de aplicar qualquer pincelada.

**3. Mapa de Roughness exportado uniforme (sem variação visível)**
Se as camadas de variação foram pintadas com opacidade muito baixa ou com o modo de mistura errado, o mapa exportado pode ser praticamente um Fill uniforme. O PNG vai parecer um cinza sólido. Estratégia: antes de exportar, abrir o mapa no Render Room e ampliar a vista de Roughness isolado para verificar se há gradação. Se não houver, aumentar a opacidade das camadas de variação ou reforçar a intensidade da pintura antes de exportar.

**4. Color Space incorreto no Blender ao conectar os mapas**
Mapas de Roughness e Metallic conectados com Color Space em "sRGB" (padrão) em vez de "Non-Color" produzem valores incorretos — o material fica excessivamente reflexivo ou completamente matte sem controle. Estratégia: lembrar a regra: somente o mapa Albedo (Color) fica em sRGB. Todos os outros mapas de dados (Roughness, Metallic, Normal, AO) devem ter Color Space em **Non-Color** no nó Image Texture do Blender.

**5. Material no Blender com dois Normal Maps conflitantes**
Ao configurar os mapas do 3D Coat no Blender, o estudante mantém o Normal Map procedural da Semana 7 E tenta conectar um mapa de Normal do 3D Coat (se gerou um). O Principled BSDF aceita apenas uma entrada Normal — a última conexão sobrescreve a anterior sem aviso. Estratégia: orientar a manter apenas o Normal Map procedural da Semana 7 nesta semana (o 3D Coat não foi usado para Normal ainda). Nas semanas seguintes (bake, Semana 11), o Normal Map será substituído pelo baked.

**6. 3D Coat lento ou travando no laboratório**
O 3D Coat é mais pesado que o Blender e pode ter performance reduzida em computadores com menos VRAM. Sintomas: viewport lento ao rodar o asset, pintura com delay, travamento ao trocar de canal. Estratégia: usar resolução 512×512 em vez de 1024 nos computadores mais lentos — o fluxo é idêntico, apenas com menos detalhe. Orientar o estudante a trabalhar em 512 em aula e re-importar em 1024 em casa ou em computador mais potente para a entrega final.

**7. Estudante não traz autoavaliação para a crítica formal**
Sem a autoavaliação preenchida, a crítica formal perde a dimensão de metacognição que é central no SBL. Estratégia: reservar 5 minutos no início do Encontro 2 para preenchimento emergencial. Criar o hábito de comunicar a importância da autoavaliação no fechamento do Encontro 1 — e repetir no início do segundo encontro.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não consegue importar o asset no 3D Coat | Verificar formato do arquivo: tentar `.fbx` se o `.obj` falhou. Verificar se a malha tem UV (abrir no UV Editor do Blender antes de exportar). Como último recurso: usar o arquivo de demonstração do professor como base e substituir pela malha do estudante depois. |
| Estudante pinta com confiança mas sem lógica de material | Parar brevemente: *"Antes de continuar: onde nesse objeto a tinta estaria mais desgastada? Onde a sujeira acumularia? Onde o usuário coloca a mão para pegar? Pinta onde a lógica de uso indica, não onde parece bonito."* |
| Estudante com material muito parecido com o da Semana 7 (sem ganho visível) | *"Compara o antes e o depois no viewport do Blender. Se o material parece igual, a pintura no 3D Coat não adicionou informação nova — você repetiu o que o nó já fazia. O que o nó não fazia? Controle de pincel, detalhe intencional em áreas específicas. Volta para o 3D Coat e pinta algo que o Noise Texture não geraria."* |
| Estudante nervoso ou travado na crítica formal | Redirecionar para a autoavaliação: *"O que você escreveu na sua autoavaliação como ponto forte? Começa mostrando isso."* O documento é um apoio — quem preencheu com honestidade tem um roteiro de apresentação pronto. |
| Turma geral com dificuldade na navegação do 3D Coat | Fazer uma pausa de 5 minutos para rever os três controles de navegação no projetor: orbitar (botão do meio), zoom (scroll), pan (Shift + botão do meio). Comparar explicitamente com o Blender. Depois voltar ao estúdio. |
| Estudante que terminou cedo e quer ir além | Propor: *"Tenta pintar as arestas com brush de tamanho pequeno e opacidade alta no canal de Roughness — simulando desgaste concentrado. Ou: exporta o Normal Map do 3D Coat também (usando o Depth channel) e conecta no Blender junto com o Normal procedural usando um nó de combinação."* |
| Estudante com dificuldade de justificar decisões na crítica | *"Não precisa ter sido a decisão certa — precisa ter sido uma decisão consciente. Por que você escolheu esse tom de roughness? Você olhou referências? Isso é suficiente para justificar."* Reforçar que justificar ≠ acertar. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Asset 01 importado no 3D Coat com canal Color pintado (mínimo: Fill + camada de variação) | C5 — Texturização | Verificar no arquivo `.3b` ou screenshot do Paint Room: há pelo menos duas camadas no Color com variação visível no Render Room? |
| Canal Roughness com ao menos duas camadas (base + desgaste em arestas) e variação perceptível no mapa exportado | C4 — Materiais PBR | Abrir o PNG exportado do Roughness: há gradação de tons? As arestas têm valor diferente do body principal? |
| Canal Metallic preenchido corretamente para o tipo de material (0 para dielétricos, 1 para metais) | C4 — Materiais PBR | Verificar no Paint Room ou no mapa exportado: o preenchimento é coerente com as propriedades físicas do material? |
| Material no Blender configurado com mapas do 3D Coat conectados nos slots corretos (Color Space Non-Color para Roughness e Metallic) | C4 — Materiais PBR | Verificar o Shader Editor: Image Texture do Albedo em sRGB, Roughness e Metallic em Non-Color. Fios chegando às entradas corretas do Principled BSDF. |
| Apresentação oral na crítica formal: descrição do material, canais conectados, e justificativa de ao menos uma decisão técnica ou artística | C9 — Apresentação | Qualidade da justificativa oral: é específica e técnica ("escolhi roughness 0.7 para pedra porque...") ou vaga ("ficou bom")? |
| Autoavaliação preenchida com evidência concreta para cada critério avaliado | C1 — Processo de Projeto | Verificar se a autoavaliação cita evidências observáveis no trabalho (ex: "tenho quatro canais conectados" — não apenas "acho que está bom") |
| Participação na crítica dos colegas: ao menos uma observação específica e construtiva sobre o trabalho apresentado | C10 — Participação | Qualidade do feedback: é observável ("o roughness parece muito uniforme, sem variação de desgaste") ou genérico ("ficou bonito")? |
| Screenshot do Paint Room com camadas visíveis e screenshot do Render Room mostrando o material com os três canais | C1 — Processo de Projeto | Presença dos dois registros com nomenclatura `_S08` e identificação do asset. |

---

## Entrega da Semana 8

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo do 3D Coat com Asset 01 texturizado (canais Color, Roughness e Metallic pintados) | `.3b` ou `.3dc` com sufixo `_Asset01_3DCoat_S08` | Até o fim do segundo encontro |
| Mapas PBR exportados do 3D Coat: Albedo, Roughness, Metallic | `.png` 1024×1024 (ou 2048) com sufixos `_Albedo`, `_Roughness`, `_Metallic` na pasta `_Mapas_S08` | Até o fim do segundo encontro |
| Arquivo Blender com material configurado usando os mapas do 3D Coat | `.blend` com sufixo `_Asset01_3DCoat_S08` | Até o fim do segundo encontro |
| Autoavaliação preenchida com evidências | Instrumento 2 da Rubrica Mestre (físico ou digital) | Até o início do segundo encontro |
| Screenshot do Paint Room (camadas visíveis) e do Render Room | `.png` com sufixos `_PaintRoom_S08` e `_RenderRoom_S08` | Até o fim do segundo encontro |

> **Nota:** A entrega dos mapas do Asset 02 no 3D Coat é opcional nesta semana — será o foco das Semanas 9 e 10. Estudantes que iniciaram o Asset 02 no 3D Coat devem salvar o arquivo `.3b` mesmo que incompleto, para continuar na Semana 9.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 8 | 2026*
