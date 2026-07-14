# Plano de Aula — Semana 11
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** III — Pintura Digital e Bake
**Tema:** Bake de texturas: Normal Map e Ambient Occlusion
**Apostila:** Parte V, Cap. 15 — Bake de Texturas (no Blender: Normal Map e Ambient Occlusion). Leitura de apoio para esta CF4: Parte VI, Cap. 23 — Controle de Qualidade de Materiais
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF4** (peso de 25% no Portfolio de Artefatos)

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 finalizado: base PBR + camadas de desgaste (EdgeWear, Dirt, Scratches), mapas exportados e conectados no Blender — Semana 9
- Asset 02 finalizado: base PBR + stencil(s) integrado(s) em pelo menos dois canais + desgaste complementar quando aplicável, mapas exportados e conectados no Blender — Semana 10
- Moodboard atualizado com referências do tema do kit — Semana 1 (atualização contínua)
- Ficha de autoavaliação da Rubrica Mestre preenchida **antes** desta aula (disponibilizada no ambiente virtual ao final da Semana 10)

> **Nota de transição:** As Semanas 9 e 10 desenvolveram a texturização artística inteiramente dentro do 3D Coat: pintura livre e stencil, ambos trabalhando diretamente sobre a malha final (low poly) do asset. Esta semana introduz uma peça de workflow que não existia até agora: a possibilidade de **esculpir ou modelar detalhe em uma malha auxiliar de alta resolução e transferir esse detalhe para o low poly através do bake**. Isso não substitui o que foi aprendido — um Normal Map de bake convive no mesmo material com o EdgeWear e o Dirt pintados à mão. O bake resolve um problema que a pintura livre não resolve bem: detalhe de **geometria real** (chanfros, entalhes profundos, sobreposição de placas) que seria caro ou tecnicamente difícil de modelar diretamente na malha de produção.

> **Atenção — Crítica Formal (CF4):** Esta é a 4ª das 6 críticas formais da disciplina e a primeira em que o Critério 6 (Bake) entra em avaliação. A partir desta semana, C4 (Materiais PBR) e C5 (Texturização) já avaliados desde CF2/CF3 são reavaliados sobre o estado atual dos dois assets, e C9 (Apresentação) passa de observação para nota formal. O professor deve reservar tempo estruturado para a apresentação individual — esta não é uma crítica circulante como nas semanas anteriores.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o conceito de bake de textura e diferenciar o papel do mesh **high-poly** (fonte de detalhe) do mesh **low-poly** (destino de produção).
2. Identificar os tipos de mapa de bake mais usados em produção de jogos — **Normal Map**, **Ambient Occlusion**, **Curvature**, **ID Map** e **Thickness** — e reconhecer para que serve cada um (o foco produtivo desta semana é Normal e AO; Curvature e ID Map serão aprofundados na Semana 12).
3. Configurar corretamente os parâmetros de um bake no Blender: seleção de objetos high-poly/low-poly, **cage** (malha de projeção), **ray distance** (distância de captura) e resolução do mapa de destino.
4. Executar um bake de Normal Map e de Ambient Occlusion sem artefatos visíveis (sem manchas em superfícies planas, sem vazamento — *bleeding* — entre ilhas de UV).
5. Integrar o Normal Map e o AO baked ao material já existente no 3D Coat/Blender, convivendo com as camadas de desgaste e stencil pintadas nas semanas anteriores.
6. Apresentar formalmente o estado atual dos dois assets do kit na Crítica Formal 4, justificando decisões técnicas e artísticas com base nos critérios da rubrica.

---

## Critérios avaliados nesta semana — CF4 (peso 25% no PA)

> 🔴 **Crítica Formal.** Esta semana atribui nota. Consultar a tabela **Critérios Ativos por Crítica Formal** da Rubrica Mestre antes de preencher a Ficha de Crítica Formal (Instrumento 1).

| Critério | Status na CF4 | O que observar |
|---|---|---|
| C1 — Processo de Projeto | ✓ Nota | Registro de processo desde a CF3: versões nomeadas, anotações de decisões, incorporação de feedback das Semanas 9 e 10 |
| C2 — Direção Artística | ✓ Nota | Coerência visual entre Asset 01 e Asset 02; o bake reforça ou compromete a identidade visual do kit? |
| C3 — UV Mapping | — Não aplicável nesta CF | — |
| C4 — Materiais PBR | ✓ Nota | Os canais PBR permanecem fisicamente plausíveis após a integração do Normal Map de bake? Não há conflito entre o Normal procedural da S7 e o novo Normal baked? |
| C5 — Texturização | ✓ Nota | O detalhe de bake se soma à narrativa de desgaste já construída, ou os dois parecem desconectados? |
| C6 — Bake | ✓ **Nota — primeira vez avaliado** | Qualidade técnica do bake: ausência de artefatos, cage bem ajustada, Normal Map com transferência fiel, AO sem bleeding |
| C7 — Otimização | — Não aplicável nesta CF | — |
| C8 — Integração na Unity | — Não aplicável nesta CF | — |
| C9 — Apresentação | ✓ **Nota — passa de observação para nota nesta CF** | Organização da entrega, clareza da apresentação individual, capacidade de responder perguntas técnicas |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado aos colegas durante a apresentação formal dos outros estudantes |

> **Lembrete de peso:** A CF4 corresponde a 25% da nota do Portfolio de Artefatos (PA) — o maior peso entre as críticas formais realizadas até agora, refletindo que o estudante já deveria dominar o processo básico de crítica e estar em trajetória de aprofundamento técnico.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Computadores com 3D Coat instalado (versão 2023 ou superior)
- Arquivos `.blend` do Asset 01 (S09) e Asset 02 (S10) de cada estudante, com UV já finalizado desde a Unidade I
- Arquivo de demonstração do professor: par de meshes já preparado — versão low-poly de produção e versão high-poly com detalhe esculpido/modelado (chanfros, entalhes) do **mesmo** asset, ambos com a mesma origem/escala
- Projetor para demonstração e para a Crítica Formal
- Ficha de Crítica Formal (Instrumento 1 da Rubrica Mestre) impressa ou digital, uma por estudante
- Ficha de Autoavaliação (Instrumento 2) preenchida por cada estudante, trazida para a aula
- Apostila — Parte V, Cap. 15 — disponibilizada antes da aula. Parte VI, Cap. 23 (Controle de Qualidade de Materiais) recomendado como leitura de apoio para a autoavaliação desta CF4

> **Preparação do par high-poly/low-poly de demonstração:** É essencial que o par já exista pronto antes da aula — modelar ao vivo consumiria o tempo da demonstração. O high-poly deve ter detalhe claramente superior (chanfros definidos, profundidade real nos entalhes) para que o resultado do bake seja visualmente convincente quando projetado no low-poly.

> **Preparação da Crítica Formal:** Organizar a ordem de apresentação dos estudantes antes da aula (lista visível, ordem alfabética ou sorteio) para evitar tempo perdido decidindo quem apresenta primeiro. Calcular o tempo disponível: 20 minutos para toda a turma na CF4 é apertado — para turmas grandes, considerar formato de apresentação em duplas simultâneas com o professor circulando, ou reservar parte do tempo de estúdio do encontro 2 para completar apresentações que não couberam nos 20 minutos formais.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**O que é bake e por que transferir detalhe de uma malha para outra**

Objetivo: estabelecer o conceito central de bake — transferência de informação de superfície de uma malha para outra através de projeção via UV — e apresentar o vocabulário técnico necessário para operar a ferramenta no Blender com segurança.

**Abertura:**

Exibir no projetor um objeto simples (ex: um baú do kit) em duas versões: a versão low-poly de produção, com arestas retas e sem chanfro, e a mesma peça com um Normal Map de bake aplicado, exibindo chanfros e profundidade nos entalhes da tampa. Perguntar à turma: *"As duas malhas têm exatamente o mesmo número de polígonos. Por que a segunda parece ter mais detalhe físico?"*

Deixar 2–3 respostas. Direcionar para a ideia central: o Normal Map engana a luz — ele não adiciona geometria, mas informa ao motor de renderização como a luz deveria se comportar *como se* houvesse geometria ali. O bake é o processo de capturar essa informação de uma malha que **tem** a geometria real (high-poly) e gravá-la em uma textura que a malha **sem** a geometria (low-poly) pode usar.

---

**Conteúdo a cobrir:**

**1. High-poly vs. low-poly: dois papéis, uma mesma peça**

O **low-poly** é a malha de produção: otimizada para performance, com contagem de polígonos adequada ao motor de jogo, e é a malha que já foi UV mapeada nas Semanas 2 a 4. O **high-poly** é uma malha auxiliar, criada apenas para existir durante o processo de bake — nunca é exportada para o jogo. Pode ter milhões de polígonos, subdivisão pesada, esculpido em detalhe (SubD + chanfros no Blender, ou escultura orgânica se o tema pedir).

*"O high-poly nunca aparece no jogo. Ele existe só para ser fotografado pelo bake e depois pode até ser descartado. A malha que joga é sempre o low-poly — mas com a 'memória' do detalhe do high-poly gravada em textura."*

**2. Os cinco tipos canônicos de mapa de bake**

Apresentar como visão geral — o foco produtivo desta semana é apenas nos dois primeiros:

- **Normal Map:** captura a direção da superfície do high-poly (orientação de cada normal de face) e grava como informação de cor RGB. É o mapa mais importante — reconstrói a ilusão de profundidade e chanfro.
- **Ambient Occlusion (AO):** captura o quanto cada ponto da superfície está "abrigado" da luz ambiente por geometria vizinha — frestas, cantos e reentrâncias ficam mais escuros. Funciona como um mapa de sombreamento de contato.
- **Curvature:** detecta onde a superfície do high-poly é convexa (arestas, cantos salientes) ou côncava (sulcos, frestas). Muito usado como máscara para direcionar automaticamente onde aplicar desgaste ou sujeira — conteúdo aprofundado na **Semana 12**.
- **ID Map (Material ID):** atribui uma cor sólida por material ou grupo de faces do high-poly, servindo como máscara de seleção rápida na texturização — também aprofundado na **Semana 12**.
- **Thickness:** mede a espessura da geometria em cada ponto — usado para simular subsurface scattering em materiais orgânicos ou translúcidos.

*"Vocês vão sair desta aula sabendo bakear dois desses cinco. Os outros três, vocês já sabem que existem e para que servem — isso já é metade do caminho para usá-los bem na semana que vem."*

**3. Parâmetros críticos de configuração**

- **Cage (malha de projeção):** uma versão extrudida do low-poly que define o "envelope" dentro do qual o Blender procura a superfície do high-poly para capturar. Sem cage bem ajustada, o bake pode capturar a face errada da geometria (artefato clássico: informação "vazada" de outra parte do modelo).
- **Ray Distance / Extrusion:** a distância que o raio de captura viaja a partir do low-poly em busca do high-poly. Muito curta: partes do detalhe não são capturadas. Muito longa: risco de capturar geometria de partes vizinhas do modelo (bleeding).
- **Resolução do mapa de destino:** deve corresponder à resolução de trabalho do asset (1024 ou 2048, coerente com os mapas já exportados nas semanas anteriores).
- **Margin / Padding:** espaço de segurança nas bordas das ilhas de UV para evitar que o bake "vaze" durante a compressão ou o mipmap — o mesmo princípio de padding UV visto na Semana 4, agora aplicado à qualidade do bake.

**4. Onde o bake se encontra com o que já foi aprendido**

O Normal Map de bake não substitui o Normal procedural criado na Semana 7 nem o desgaste pintado nas Semanas 9 e 10 — ele se **soma**. No 3D Coat, o Normal Map baked entra como uma camada adicional no canal Normal (ou como base, dependendo do fluxo escolhido), e o EdgeWear/Dirt continuam sendo pintados por cima ou ao redor dele.

> **Nota do professor:** Esta é uma mini aula mais densa tecnicamente do que as anteriores — é inevitável, pois bake tem parâmetros que precisam ser entendidos antes de a ferramenta ser usada com segurança (ao contrário de pintura livre, onde o erro é visualmente óbvio e corrigível na hora). Resistir à tentação de aprofundar Curvature e ID Map agora — eles voltam na Semana 12 com tempo dedicado.

---

### Demonstração — 20 minutos

**Setup completo de bake de Normal Map e AO no Blender**

**Setup (1 min):**
Abrir o Blender com o par de malhas de demonstração já carregado: high-poly (com chanfros e entalhes esculpidos) e low-poly (mesh de produção, UV já existente) posicionados na mesma origem e escala.

**Percurso da demonstração:**

**Passo 1 — Preparação da cena de bake (4 min):**
1. Renomear os objetos claramente: `Asset_HighPoly` e `Asset_LowPoly` — nomenclatura clara evita selecionar o objeto errado durante o bake.
2. Selecionar primeiro o high-poly, depois **Shift+clicar** no low-poly por último (o Blender bakeia sempre para o objeto ativo por último).
3. No painel de Materiais do low-poly: criar um novo `Image Texture Node` vazio, nomeado `Asset_NormalBake_2048`, com resolução 2048×2048 e Color Space Non-Color. Deixar selecionado no Shader Editor — é para onde o bake será gravado.
4. Ir em `Render Properties → Engine: Cycles` (bake exige Cycles). Abrir a seção `Bake`.

**Passo 2 — Configuração de cage e ray distance (6 min):**
1. Em `Bake → Selected to Active`: ativar. Isso instrui o Blender a bakear do objeto selecionado (high-poly) para o objeto ativo (low-poly).
2. Ativar `Cage`: mostrar a opção de usar uma malha de cage customizada ou o `Extrusion` automático. Para esta demonstração, usar `Extrusion: 0.02m` (ajustar conforme escala do asset) — valor pequeno o suficiente para não capturar geometria vizinha, grande o suficiente para envolver todo o detalhe do high-poly.
3. Mostrar visualmente no viewport (modo wireframe) como o cage aparece como um envelope ao redor do low-poly, e como o high-poly precisa estar contido dentro desse envelope.
4. *"Se o cage for pequeno demais, o raio não alcança o detalhe do high-poly e o bake fica liso. Se for grande demais, o raio pode 'ver' outra parte do modelo e gravar informação errada ali. É tentativa e ajuste — comecem pequeno e aumentem gradualmente."*

**Passo 3 — Execução do bake de Normal Map (4 min):**
1. Em `Bake Type`: selecionar **Normal**.
2. Manter `Space: Tangent` (padrão para uso em motores de jogo e no 3D Coat).
3. Clicar em `Bake`. Aguardar o processamento (comentar sobre o tempo variar conforme a complexidade do high-poly e a resolução).
4. Resultado: mostrar o mapa gerado no Image Editor — textura roxo-azulada característica de um Normal Map em espaço tangente.
5. Aplicar no viewport Rendered: mostrar o low-poly agora exibindo os chanfros e entalhes do high-poly, sem ter ganho um único polígono.

**Passo 4 — Execução do bake de Ambient Occlusion (3 min):**
1. Criar novo `Image Texture Node`: `Asset_AOBake_2048`, Color Space Non-Color.
2. Em `Bake Type`: selecionar **Ambient Occlusion**.
3. Clicar em `Bake`.
4. Resultado: mostrar o mapa em escala de cinza, com escurecimento nas frestas e cantos do high-poly.
5. *"Reparem que a AO sozinha, sem cor nenhuma, já dá uma leitura de profundidade forte. É por isso que ela é multiplicada sobre o Albedo depois — vamos ver isso no estúdio."*

**Passo 5 — Verificação de artefatos (2 min):**
1. Ampliar o Normal Map no Image Editor: apontar para uma ilha de UV e mostrar como teria aparência se houvesse bleeding (informação de uma ilha vazando para a ilha vizinha) — se disponível, mostrar um exemplo de erro preparado previamente para contraste.
2. Verificar no viewport: rotacionar o asset e observar se há "manchas" inesperadas em superfícies que deveriam ser planas — sinal clássico de cage mal ajustada.
3. *"Sempre verifiquem o resultado rotacionando o objeto antes de considerar o bake pronto. Um artefato que não aparece de um ângulo pode aparecer claramente de outro."*

> **Nota do professor:** Não é necessário demonstrar Curvature nesta sessão — ele é mencionado na mini aula apenas conceitualmente e retorna com demonstração completa na Semana 12. O foco aqui é que o estudante saia com o fluxo completo de Normal + AO dominado, pois é isso que será exigido na CF4.

---

### Produção em Estúdio — 50 minutos

**Criação de detalhe high-poly e execução do bake**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com um objetivo: escolher uma parte do Asset 01 ou do Asset 02 que se beneficiaria de detalhe de geometria real — um chanfro, um entalhe, uma sobreposição de placas — e criar uma versão high-poly dessa parte. Depois, executar o bake de Normal Map e AO para o low-poly. Não precisa ser o asset inteiro: pode ser só uma parte, como a tampa de um baú ou a borda de um escudo. O objetivo de hoje é dominar o fluxo técnico, não cobrir o asset inteiro de detalhe."*

**Atividade estruturada:**

**Etapa 1 — Seleção da área e planejamento (≈10 min):**
1. Abrir o arquivo `.blend` do Asset 01 ou Asset 02 (recomendação: escolher o asset com maior potencial de detalhe geométrico — bordas, dobradiças, entalhes).
2. Identificar uma área específica que se beneficiaria de detalhe de geometria: *"Que parte deste objeto, se fosse esculpida ou modelada com mais detalhe, mudaria a leitura do material?"*
3. Duplicar o objeto (ou a parte selecionada): renomear a cópia como `[Nome]_HighPoly` e o original como `[Nome]_LowPoly`.

**Etapa 2 — Criação do detalhe high-poly (≈20 min):**
1. Na cópia high-poly: adicionar detalhe via Modificador `Bevel` (chanfros), `Subdivision Surface` + edição manual, ou esculpir diretamente (Sculpt Mode) se o tema pedir superfície orgânica/irregular.
2. Manter a silhueta geral compatível com o low-poly — o bake só funciona bem se as duas malhas ocupam aproximadamente o mesmo espaço.
3. Aplicar os modificadores antes do bake (`Ctrl+A → Visual Geometry to Mesh` ou aplicar modificador diretamente).

**Etapa 3 — Configuração e execução do bake (≈15 min):**
1. Selecionar high-poly, depois Shift+clicar no low-poly (ativo por último).
2. No material do low-poly: criar os dois Image Texture Nodes de destino (`_NormalBake` e `_AOBake`), resolução coerente com os demais mapas do asset.
3. Configurar `Selected to Active`, `Cage` com extrusion ajustada ao tamanho do detalhe.
4. Executar bake de Normal Map. Verificar rotacionando o viewport.
5. Executar bake de Ambient Occlusion. Verificar.
6. Se houver artefatos: ajustar extrusion do cage e refazer o bake — normal fazer 2 a 3 tentativas até o resultado ficar limpo.

**Etapa 4 — Registro de processo (≈5 min):**
1. Salvar o arquivo: `[Nome]_Asset0X_Bake_S11.blend` (preservando o arquivo da semana anterior).
2. Screenshot comparativo: low-poly sem bake vs. low-poly com Normal + AO aplicados.

**Papel do professor:**

Circular verificando três pontos em cada estação:

- **A escala do high-poly e do low-poly coincide?** Erro comum: duplicar e mover acidentalmente um dos objetos, fazendo o bake capturar vazio ou geometria errada. Verificar com `Object → Snap → Selection to Cursor` se necessário realinhar.
- **O cage está bem dimensionado?** Pedir para o estudante rotacionar o asset após o bake e apontar qualquer mancha ou vazamento — a maior parte dos problemas de bake se resolve ajustando a extrusion do cage, não recomeçando do zero.
- **O objetivo é dominar o processo, não cobrir o asset inteiro?** Reforçar que um bake pequeno e limpo em uma área vale mais nesta etapa do que um bake ambicioso e cheio de artefatos.

Perguntas de mediação circulante:
- *"Se você olhasse só o low-poly, sem saber que existe um high-poly por trás, você acreditaria que aquele detalhe é real?"*
- *"Onde nesse asset a diferença entre high-poly e low-poly mais aparece? É ali que o bake tem mais impacto."*
- *"O Normal Map baked está competindo ou dialogando com o desgaste que você já pintou nas Semanas 9 e 10? Um chanfro recém-modelado com desgaste de anos de uso faz sentido para o seu tema?"*

---

## ENCONTRO 2 (1h30)

### Crítica Formal (CF4) — 20 minutos

**Formato: Apresentação individual estruturada**

Esta é uma crítica 🔴 **FORMAL** — diferente das críticas circulantes das semanas anteriores. Cada estudante apresenta individualmente, o professor preenche a Ficha de Crítica Formal (Instrumento 1) comparando com a autoavaliação do estudante (Instrumento 2), e a nota atribuída compõe 25% do PA.

**Protocolo:**

**Preparação (antes do início):**
- Confirmar que todos trouxeram a Ficha de Autoavaliação preenchida.
- Ordem de apresentação definida previamente e visível para a turma.
- Cada estudante prepara: Asset 01 e Asset 02 abertos no Blender (viewport Rendered), com os mapas de bake da S11 já conectados; renders comparativos (antes/depois do bake) prontos para exibir.

**Abertura (1 min):**
*"Cada apresentação tem cerca de 2 minutos: mostrem o Asset 01 e o Asset 02, expliquem o que mudou desde a última crítica formal (Semana 8) e destaquem especificamente o que o bake desta semana adicionou. Depois, uma pergunta rápida da turma ou minha. Vou preencher a ficha durante a apresentação de vocês — sem afetar o ritmo."*

**Apresentações (≈16 min para a turma, ajustar tempo por estudante conforme o tamanho da turma):**

Roteiro sugerido para cada estudante (⏱ ~2 min):
1. Mostrar Asset 01: destacar desgaste (S09) e agora o bake de Normal/AO, se aplicado a essa peça.
2. Mostrar Asset 02: destacar stencil integrado (S10) e o bake, se aplicado a essa peça.
3. Uma frase de autoavaliação: *"O que eu acho que está no nível mais alto no meu trabalho esta semana é [X], e o que eu sei que ainda precisa de trabalho é [Y]."*
4. Uma pergunta do professor ou de um colega, registrada como parte de C10 do colega que perguntou.

O professor preenche a Ficha de Crítica Formal (Instrumento 1) para C1, C2, C4, C5, C6 e C9 durante cada apresentação, comparando mentalmente com a autoavaliação entregue. Diferenças relevantes entre a autopercepção do estudante e a avaliação do professor são material valioso para o feedback escrito.

**Síntese coletiva (3 min):**
*"Vi um salto real na turma entre Normal Maps limpos e alguns com artefato que ainda precisa de ajuste de cage. Isso é normal na primeira semana de bake — vamos resolver isso hoje no estúdio. A meta para o fechamento de hoje: qualquer artefato identificado na apresentação de vocês sai corrigido antes de irem embora."*

> **Nota sobre o feedback escrito:** A Ficha de Crítica Formal exige um "ponto mais forte" e uma "prioridade de melhoria" por estudante. Preencher esses campos imediatamente após cada apresentação, enquanto o contexto está fresco — não deixar para o final do bloco de 20 minutos.

---

### Produção em Estúdio — 60 minutos

**Correção de artefatos, refinamento e integração final**

**Consigna:**

> *"Sessenta minutos com foco na prioridade de melhoria que cada um recebeu na crítica formal de hoje. Se o problema foi um artefato de bake, corrijam o cage e regravem. Se foi falta de integração entre o bake e o desgaste pintado, ajustem isso no 3D Coat. Se os dois assets já estão sólidos, usem o tempo para aplicar bake em uma segunda área do kit."*

**Atividade estruturada:**

**Bloco 1 — Correção de artefatos identificados na CF4 (≈20 min):**

Para estudantes com problemas de bake apontados na apresentação:
1. Revisar a extrusion do cage: aumentar ou diminuir em incrementos pequenos (ex: de 0.02m para 0.015m ou 0.03m).
2. Verificar se as UVs têm padding suficiente (revisar princípios da Semana 4) — bleeding entre ilhas geralmente se resolve aumentando a margem entre elas ou o `Margin` do bake.
3. Regravar o bake e verificar rotacionando o viewport antes de declarar resolvido.

**Bloco 2 — Integração do bake ao material no 3D Coat (≈20 min):**

Para estudantes com bake tecnicamente limpo:
1. Importar o Normal Map baked como uma camada adicional no canal Normal do 3D Coat (ou combinar com o Normal procedural existente, se o fluxo do estudante usar ambos).
2. Importar o AO baked: usar como camada de Multiply sobre o canal Color, opacidade ajustável (60–80%), para reforçar visualmente as frestas e cantos já criados pelo Dirt pintado nas Semanas 9–10.
3. Verificar no Render Room: o bake reforça ou desconecta da narrativa de desgaste já existente? Ajustar opacidade das camadas para que os dois sistemas de detalhe (pintado + bakeado) leiam como uma única superfície coerente.

**Bloco 3 — Segunda aplicação de bake, se houver tempo (≈15 min):**

Para estudantes com ambos os assets já resolvidos:
1. Repetir o processo de high-poly → bake em uma segunda área do kit (outro asset ou outra parte do mesmo asset).
2. Priorizar áreas com maior potencial de leitura visual à distância de uso (bordas expostas, pontos focais da composição do kit).

**Bloco 4 — Exportação e registro final (≈5 min):**
1. Exportar Normal Map e AO finalizados do Blender (`Image → Save As`).
2. Salvar arquivo Blender atualizado: `[Nome]_Asset0X_Bake_S11_Final.blend`.
3. Screenshot comparativo final: high-poly, low-poly sem bake, low-poly com bake integrado ao material completo.

**Papel do professor:**

- Para estudantes que corrigiram o artefato rapidamente: direcionar para o Bloco 3 (segunda aplicação) em vez de deixá-los ociosos.
- Para estudantes com dificuldade persistente de artefato: verificar se o problema é de escala entre os objetos (causa mais comum de bake completamente vazio ou "achatado") antes de insistir em ajustar o cage.
- Perguntas de mediação: *"O bake que você regravou agora está melhor porque você mudou um parâmetro específico, ou porque tentou várias vezes até dar certo? Consegue explicar qual parâmetro resolveu?"* — a resposta revela se houve aprendizagem do processo ou apenas tentativa e erro sem compreensão.

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese da CF4)**
*"Hoje foi a quarta crítica formal do semestre e a primeira que avaliou Bake. A maioria de vocês está conectando três sistemas de detalhe agora: o material PBR de base, o desgaste pintado à mão e o detalhe capturado por bake. Essa sobreposição de camadas é exatamente como texturização profissional funciona — nenhuma técnica sozinha resolve tudo."*

2. **(3 min — Reflexão de processo)**
Pergunta aberta: *"Qual foi a diferença entre a autoavaliação que vocês escreveram antes da aula e o que eu disse durante a apresentação? Se houve diferença, para qual lado ela pendeu — vocês se avaliaram melhor ou pior do que eu avaliei?"*

Deixar 2–3 respostas. O objetivo é desenvolver a calibração entre autopercepção e avaliação externa — uma habilidade central de C1 (Processo) e C10 (Participação) que se desenvolve ao longo do semestre.

3. **(2 min — Antecipação da Semana 12)**
*"Semana que vem: bake avançado — ID Map e Curvature. Vocês vão aprender a usar esses dois mapas como base de mascaramento automático no 3D Coat, o que acelera bastante a texturização de detalhe. Antes de chegar: pensem em qual asset do kit teria mais de um material distinto (ex: madeira + metal no mesmo objeto) — esse é o candidato ideal para ID Map."*

4. **(2 min — Confirmação das entregas e devolução da nota)**
Informar prazo para devolução da Ficha de Crítica Formal preenchida (feedback escrito) e recapitular nomenclatura de entrega.

---

## Possíveis Dificuldades

**1. Escala entre high-poly e low-poly não coincide — bake vazio ou completamente distorcido**
Ocorre quando o estudante duplica o objeto e o modificador ou uma transformação acidental altera a escala de um dos dois. O bake resultante aparece como ruído aleatório ou área completamente lisa sem nenhuma informação. Estratégia: antes de qualquer ajuste de cage, verificar no painel `N` do viewport se a escala (Scale X/Y/Z) de ambos os objetos é idêntica (idealmente 1.0 após `Ctrl+A → Apply Scale`). Esse é o primeiro ponto de verificação, sempre — antes de mexer em qualquer parâmetro de bake.

**2. Cage mal ajustada — bleeding de geometria vizinha**
Extrusion grande demais faz o raio de captura "enxergar" outra parte do modelo, gravando informação de uma face errada. O sintoma é uma mancha ou padrão inesperado que não corresponde a nenhum detalhe do high-poly local. Estratégia: reduzir a extrusion em incrementos pequenos (metade do valor anterior) e regravar até o artefato desaparecer. Se persistir mesmo com extrusion mínima, verificar se há geometria sobreposta ou duplicada na cena.

**3. Confusão na ordem de seleção dos objetos**
O Blender bakeia para o objeto **ativo** (selecionado por último). Se o estudante seleciona na ordem errada, o bake tenta gravar no high-poly (que não tem UV de produção) ou falha silenciosamente. Estratégia: ensinar a checagem visual — o objeto ativo aparece com contorno laranja mais claro que os demais selecionados. Antes de clicar em Bake, confirmar visualmente qual objeto está ativo.

**4. Modelagem de detalhe high-poly consumindo tempo demais**
Alguns estudantes se envolvem em esculpir um nível de detalhe muito além do necessário para o bake funcionar, comprometendo o tempo restante da sessão. Estratégia: lembrar que o high-poly só precisa ter detalhe suficiente para ser capturado em 1024–2048px — detalhe microscópico não sobrevive à resolução do bake. Estabelecer um limite de tempo firme (ex: 15 minutos) para a etapa de modelagem antes de avançar ao bake.

**5. Bake tecnicamente limpo mas visualmente desconectado do desgaste já pintado**
O Normal Map de bake fica perfeito isoladamente, mas quando combinado com o EdgeWear e o Dirt das Semanas 9–10, o resultado parece "duas texturas coladas" — o chanfro bakeado é nítido demais comparado ao desgaste orgânico ao redor. Estratégia: reforçar que a integração continua sendo trabalho de pintura livre — usar uma leve camada de Dirt ou EdgeWear sobre a área recém-bakeada para que ela receba o mesmo tratamento narrativo do resto do asset.

**6. Ansiedade de apresentação na Crítica Formal**
Diferente das críticas informais das semanas anteriores, a CF4 tem formato individual e atribui nota, o que aumenta a tensão de alguns estudantes, especialmente os que tiveram mais dificuldade técnica na semana. Estratégia: abrir a crítica reforçando que o objetivo é registrar o estado atual do processo, não julgar um resultado final — e que a Ficha de Autoavaliação já trazida pelo estudante é parte legítima da nota, não apenas um formulário burocrático.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe por onde começar a criar o high-poly | Pedir que aponte, no low-poly já existente, uma aresta ou face que "deveria" ter profundidade real mas está achatada por questão de otimização de polígonos. Essa é a área correta para começar — o high-poly nasce de uma limitação já identificada no low-poly, não de uma ideia aberta. |
| Estudante frustrado após múltiplas tentativas de bake com artefato | Isolar variáveis: pedir para desativar o cage customizado e usar o extrusion automático padrão primeiro, confirmar que funciona sem artefato grosseiro, e só depois reintroduzir ajustes finos. Resolver o problema em etapas pequenas evita que o estudante mude três parâmetros ao mesmo tempo e perca o rastro do que funcionou. |
| Estudante com autoavaliação muito distante da avaliação do professor na CF4 | Não corrigir publicamente durante a apresentação — anotar a diferença na ficha e conversar individualmente durante o estúdio, pedindo que o estudante aponte a evidência concreta que embasou sua autoavaliação. A calibração se constrói com evidência, não com a opinião do professor imposta. |
| Estudante que termina rápido e com qualidade | Propor um segundo bake em outra parte do kit, ou introduzir uma pergunta antecipada da Semana 12: *"Se esse asset tivesse dois materiais diferentes — por exemplo, madeira e reforço metálico — como você acha que separaria isso automaticamente na textura? Pesquise 'Material ID' e me conte o que encontrou."* |
| Estudante confuso sobre por que o Normal Map de bake e o Normal procedural da Semana 7 coexistem | Explicar com analogia: *"O procedural da Semana 7 é como uma textura de pele — repete um padrão geral (poros, rugosidade fina) por toda a superfície. O bake de hoje é como uma cicatriz específica — um detalhe único, localizado, que só existe naquele ponto exato porque veio de uma geometria real ali."* Os dois podem estar no mesmo canal Normal, em camadas separadas. |
| Estudante nervoso antes de apresentar na Crítica Formal | Lembrar que a ficha de autoavaliação já registra a reflexão do estudante antes mesmo de abrir a boca — a apresentação é uma confirmação verbal do que já foi pensado, não uma prova surpresa. Sugerir que comece pela frase mais fácil: "o que eu mais gostei de ter feito esta semana foi...". |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Objeto high-poly e low-poly presentes no arquivo `.blend`, com escala e origem coincidentes | C6 — Bake | A geometria auxiliar existe e está corretamente posicionada em relação ao low-poly de produção? |
| Normal Map baked aplicado ao low-poly sem artefatos visíveis em nenhum ângulo de câmera testado | C6 — Bake | O mapa transfere fielmente o detalhe do high-poly? Há manchas, bleeding ou vazamento de geometria vizinha? |
| Ambient Occlusion baked sem bleeding entre ilhas de UV, integrado como Multiply sobre o Albedo | C6 — Bake | A AO reforça frestas e cantos de forma coerente com a geometria? O modo de mistura está correto? |
| Comparativo visual high-poly / low-poly-sem-bake / low-poly-com-bake, documentado com screenshots | C1 — Processo de Projeto | A evolução técnica está documentada de forma que qualquer pessoa entenda o que o bake mudou, sem explicação verbal? |
| Bake integrado de forma coerente ao desgaste já pintado (EdgeWear, Dirt, Scratches) e aos stencils das semanas anteriores | C5 — Texturização | O novo detalhe de geometria dialoga com a narrativa de uso já construída, ou parece um elemento isolado e recém-adicionado? |
| Coerência entre Asset 01 e Asset 02 mantida após a introdução do bake | C2 — Direção Artística | O nível de detalhe geométrico introduzido é proporcional e consistente entre os dois assets do kit? |
| Apresentação individual na CF4: clareza da fala, organização dos arquivos exibidos, capacidade de responder perguntas técnicas sobre os parâmetros de bake usados | C9 — Apresentação | O estudante consegue explicar as decisões de cage, extrusion e resolução tomadas, sem depender de leitura de anotações? |
| Ficha de Autoavaliação preenchida com evidência específica por critério, entregue antes da apresentação | C1 — Processo de Projeto | A autoavaliação aponta evidência concreta no próprio trabalho, ou é genérica ("acho que está bom")? |
| Feedback dado a colegas durante a Crítica Formal com observação técnica específica | C10 — Participação (obs.) | A pergunta ou comentário do estudante durante a apresentação de um colega referencia um critério técnico observável (cage, artefato, integração), ou é genérico? |

---

## Entrega da Semana 11

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo Blender com objeto high-poly e low-poly do asset trabalhado, mais o material atualizado com bake integrado | `.blend` com sufixo `_Asset0X_Bake_S11_Final` | Até o fim do segundo encontro |
| Normal Map e AO Map exportados | `.png` na resolução de trabalho do asset (1024 ou 2048), pasta `_Bake_S11` | Até o fim do segundo encontro |
| Screenshot comparativo: high-poly / low-poly sem bake / low-poly com bake integrado ao material completo | `.png` com sufixo `_Comparativo_Bake_S11` | Até o fim do segundo encontro |
| Ficha de Autoavaliação (Instrumento 2) preenchida | Documento digital ou impresso, entregue antes da apresentação | Início do segundo encontro |
| Ficha de Crítica Formal (Instrumento 1), preenchida pelo professor | Devolução com feedback escrito | Conforme cronograma de devolução da disciplina |

> **Nota sobre a nota da CF4:** A nota atribuída nesta semana corresponde a 25% do Portfolio de Artefatos (PA), o maior peso entre as críticas realizadas até agora. O feedback escrito da Ficha de Crítica Formal deve destacar claramente o ponto mais forte e a prioridade de melhoria de cada estudante, servindo de guia direto para a Semana 12.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 11 | 2026*
