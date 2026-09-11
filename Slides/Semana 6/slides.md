---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 06"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# A costura é um problema técnico

## Não estético

**Semana 6** — Criação de texturas seamless e tileable

<!--
Notas: Abertura da mini aula (20 min). Unidade II, entre a crítica formal da Semana 5 e a CF2 (Semana 8). Mensagem central no subtítulo: a costura de uma textura não é falta de talento artístico — é uma imagem cujas bordas não são contínuas. Marco da semana: pela primeira vez uma IMAGEM REAL entra no pipeline (fotografada OU pintada, dependendo da trilha visual do estudante). Nas Semanas 3-5 o Albedo era cor plana; agora vira uma superfície com variação e história. Não é tutorial de cliques: é entender por que a repetição precisa ser invisível — em qualquer trilha.
-->

---

## Objetivos de hoje

Ao final da semana você será capaz de:

- Explicar **o que é** uma textura seamless e por que jogos precisam dela
- Diferenciar **offset+patch** de uma repetição direta de foto ou pintura
- Criar uma textura seamless a partir de uma foto **ou** de uma pintura estilizada no **Krita**
- Conectar a textura ao canal **Albedo** do Asset 01 no Blender
- Localizar mapas PBR em fontes livres, fotográficas ou estilizadas

<!--
Notas: Ler rápido. Cada objetivo retorna ao longo da aula. Não antecipar Normal Map nem geração de mapas via 3D Coat (Semana 7) — hoje só o Albedo deixa de ser cor e passa a ser imagem. Manter os valores de Metallic e Roughness calibrados na Semana 5, em qualquer trilha visual.
-->

---

<!-- _class: comparison -->

## Duas trilhas visuais, um mesmo pipeline

**Fotorrealista**
- Textura de origem fotográfica
- Material lido como "escaneado do mundo real"

**Estilizada**
- Textura de origem pintada/ilustrada
- Material lido como desenhado com intenção artística

<div class="tip">

Mesmo fluxo de ferramentas nas duas — Krita hoje, 3D Coat a partir da Semana 7. A diferença está só na fonte da imagem. Nenhuma trilha vale mais nota: a escolha precisa ser coerente com o moodboard das Semanas 1–3.

</div>

<!--
Notas: Slide novo desta revisão. A partir de hoje cada estudante começa a definir se o Hero Asset persegue fotorrealismo ou estilização. Deixar claro que o requisito técnico de seamless (continuidade de borda) é idêntico nas duas — a diferença é só de onde vem a imagem e, mais adiante (Semana 7), como o material entra no 3D Coat. Se algum estudante estiver em dúvida, adiantar que existe um slide de apoio para essa decisão mais à frente na aula.
-->

---

## Recapitulação rápida (5 min): empacotamento avançado de UV

Antes do conteúdo novo, retomamos o que ficou pendente da **Semana 4**: o add-on **UVPackmaster** permite empacotar UV islands com rotação livre e aproveitamento de formas irregulares — resultado mais eficiente que o Pack Islands nativo, especialmente para islands orgânicas.

<div class="tip">

Vale a pena reabrir o Pack Islands do Asset 01 ou 02 com essa ferramenta antes de aplicar a textura de hoje? Se sim, façam isso nos primeiros minutos do estúdio.

</div>

<!--
Notas: Abertura da mini aula — os 5 primeiros minutos, antes de entrar no conteúdo novo de textura seamless. Mostrar rapidamente (ou descrever com uma imagem, se o add-on não estiver instalado no laboratório) a diferença de aproveitamento de espaço entre um Pack Islands nativo e um empacotamento via UVPackmaster no mesmo asset — reaproveitar o mesmo asset de demonstração da Semana 4, se possível. Não é essencial ter o add-on instalado: se indisponível, mencionar apenas verbalmente. Fechar com a pergunta do slide e seguir para o conteúdo novo da semana.
-->

---

<!-- _class: question -->

# O que está errado nesta parede?

<!--
Notas: Abrir com esta pergunta usando a imagem estática de comparação no projetor (sem abrir software ainda). Aguardar 2-3 respostas — o objetivo é que a turma IDENTIFIQUE a costura antes de nomear o conceito. Vão dizer "tem uma linha", "a pedra se repete igual". Confirmar e revelar o conceito no slide seguinte.

[!FIGURA]
Objetivo didático: provocar a turma a enxergar a costura por conta própria, ancorando o conceito na percepção antes da definição.
Arquivo sugerido: assets/parede_costura_vs_seamless.webp
Descrição: uma parede de jogo em duas versões lado a lado. À esquerda, uma textura de pedra 512x512 repetida sem tratamento — linhas de corte (costuras) visíveis em grade. À direita, a MESMA parede com a textura tornada seamless — a repetição não é perceptível.
Como produzir: no Blender, aplicar uma textura de pedra 512x512 num plano grande com escala de repetição alta (nó Mapping com Scale elevado) e renderizar — as costuras aparecem. Tornar a mesma textura seamless no Krita (offset+patch), reaplicar e renderizar de novo. Compor as duas capturas lado a lado no Krita com rótulos "sem tratamento / seamless".
-->

---

## O que é uma textura seamless

Uma imagem cujas bordas **esquerda/direita** e **topo/base** são contínuas.

Quando repetida lado a lado, o olho **não** detecta a transição entre tiles.

<div class="industry">

Paredes, pisos e terrenos são maiores que um tile. A solução eficiente é repetir uma textura pequena — mas só funciona se ela for seamless. Vale tanto para uma foto quanto para uma pintura digital.

</div>

<!--
Notas: Fixar o conceito central. Superfícies grandes de jogo são maiores que uma única tile. Usar textura pequena repetida é a opção mais eficiente em memória — mas exige seamless. A alternativa (textura única cobrindo tudo) existe, mas não escala para um kit modular. O requisito técnico de continuidade de borda é o mesmo independentemente da trilha visual (fotorrealista ou estilizada). Amarrar ao Projeto Integrador: o kit precisa de superfícies amplas coerentes.
-->

---

## Por que a imagem de origem não é seamless

Uma foto captura **iluminação**, **sombras** e **perspectiva** diferentes em cada borda.

Uma pintura do zero tem o mesmo problema se as pinceladas não foram planejadas para continuar nas bordas.

Ao repetir, essas diferenças aparecem como **linhas de costura** — em foto ou em pintura.

<!--
Notas: O ponto-chave que motiva o método, agora válido para as duas trilhas. A costura não é falha de conteúdo — é diferença entre as bordas. Por isso capturar em iluminação difusa (dia nublado) é tão importante na trilha fotorrealista: sombras duras criam costuras que "giram" com o tile e não se corrigem por offset simples. Na trilha estilizada, o equivalente é uma pincelada que não foi pensada para repetir. Preparar o terreno para a solução: offset.
-->

---

<!-- _class: image-right -->

![](assets/offset_traz_costura_ao_centro.webp)

## O método: offset

Deslocar a imagem **50%** em X e Y.

As bordas — antes invisíveis — vão para o **centro**.

Agora dá para **consertá-las** com pintura, seja sobre foto ou sobre pintura.

<!--
Notas: Explicar o coração do processo. O offset não conserta nada sozinho — ele TRAZ o problema para onde conseguimos vê-lo e pintar. As bordas passam a ser contínuas; o trabalho de patch acontece no centro. No Krita: Filter > Transform > Offset, 50% em cada eixo. O método é idêntico nas duas trilhas visuais — só muda o que se pinta por cima (clone de pixels reais vs. continuação de pinceladas).

[!FIGURA]
Objetivo didático: tornar visível a lógica do offset — o problema não some, ele muda de lugar para poder ser corrigido.
Arquivo sugerido: assets/offset_traz_costura_ao_centro.webp
Descrição: textura de pedra em duas etapas. À esquerda, a imagem original com a costura implícita nas bordas (invisível). À direita, a mesma imagem após offset de 50% — as antigas bordas agora formam uma cruz de costuras no centro da imagem, prontas para o patch.
Como produzir: no Krita, abrir uma foto de pedra, aplicar Filter > Transform > Offset a 50% em X e Y. Capturar antes e depois. Compor lado a lado com uma seta indicando "bordas -> centro".
-->

---

## O patch: cobrir a costura

Com **Clone Stamp** (`S`), amostrar (`Ctrl+clique`) regiões próximas e cobrir a linha.

- Trabalhar em pinceladas **irregulares**, não em linha reta
- Seguir as **formas naturais** do material (veios, juntas, direção da pincelada)
- **Smudge** para suavizar transições
- Na trilha estilizada, pincéis de textura/canvas do Krita ajudam a manter a coerência pintada

<div class="error">

Patch em linha reta troca uma costura por um **padrão de linhas paralelas** — igualmente visível.

</div>

<!--
Notas: O erro nº 1 do estúdio. Clonar em linha reta cria um novo padrão repetitivo. Orientar pinceladas diagonais e irregulares, seguindo a textura do material. O Smudge suaviza os limites do patch. Mostrar isso ao vivo na demonstração com o Wrap Around ativo. Para quem estiver criando uma textura estilizada do zero (sem foto de origem), os pincéis padrão do Krita com textura de papel/canvas ajudam a manter o resultado coerente com um universo pintado.
-->

---

<!-- _class: image-left -->

![](assets/krita_wrap_around.webp)

## Wrap Around: o feedback em tempo real

Atalho `W` no Krita: pré-visualiza a **repetição enquanto você pinta**.

Sem exportar e testar a cada ajuste — em foto ou em pintura.

<div class="tip">

Recue 2 passos do monitor. Se precisar se **concentrar** para achar a costura, ela já não incomoda o jogador. Essa é a régua.

</div>

<!--
Notas: O Wrap Around (W) é o único feedback confiável em tempo real — o estudante vê a costura ANTES de ir para o Blender, na trilha fotorrealista ou na estilizada. Erro comum nº 2: o PNG isolado parece perfeito, mas a costura só aparece quando tilea. Insistir no uso do Wrap Around durante todo o processo, não só no fim. A régua do "bom o suficiente" é uma decisão artística, não técnica.

[!FIGURA]
Objetivo didático: mostrar como o Wrap Around revela costuras que são invisíveis na imagem isolada.
Arquivo sugerido: assets/krita_wrap_around.webp
Descrição: captura de tela do Krita com uma textura de pedra em modo Wrap Around ativo, exibindo a repetição em grade 3x3. Uma costura residual aparece destacada por um círculo vermelho anotado.
Como produzir: no Krita, abrir uma textura de pedra parcialmente tratada, pressionar W para ativar o Wrap Around, dar zoom out até ver a repetição em grade. Capturar a tela e anotar a costura residual com um círculo no próprio Krita.
-->

---

<!-- _class: diagram -->

## O ciclo de trabalho da semana

![diagram](assets/mermaid-1.png)

<!--
Notas: Núcleo procedimental da semana. O ciclo Krita -> Blender vai se repetir várias vezes no estúdio — é normal, nas duas trilhas visuais. Reforçar o loop C->D->C: verificar no Wrap Around, voltar ao patch se houver costura. O GitHub Action converte o bloco mermaid em imagem automaticamente.
-->

---

## Fontes de texturas PBR gratuitas — duas trilhas

**Trilha fotorrealista**
- **Poly Haven** (polyhaven.com) — mapas PBR completos, licença CC0
- **AmbientCG** (ambientcg.com) — grande variedade por categoria, CC0

**Trilha estilizada**
- Coleções "Painted"/"Stylized" (ex.: Poliigon) e pacotes seamless hand-painted no itch.io

<div class="tip">

Fotorrealista já vem quase seamless com Albedo, Normal, Roughness e AO. Estilizada costuma trazer só o Albedo pronto — Metallic/Roughness você calibra à mão, como na Semana 5.

</div>

<!--
Notas: Deixar claro que baixar textura pronta NÃO isenta de entender o seamless, em nenhuma trilha. Se o estudante baixa do Poly Haven ou de um banco estilizado, precisa documentar por que é seamless (apontar continuidade de bordas no Wrap Around) e adaptar cor/detalhe ao tema. "Baixar é válido. Entregar sem entender não é." Erro comum nº 6 do plano. Se a internet do lab for instável, ter um pen drive com 5-6 texturas de cada trilha preparadas (pedra, madeira, metal, concreto, tijolos).
-->

---

## Ainda não decidiu a trilha visual?

Volte ao moodboard das Semanas 1–3: as referências são **fotos** de ambientes reais, ou **ilustrações/concept art**?

<div class="tip">

Sem certeza? Comece pela trilha **estilizada** — mais segura para quem não tem acesso fácil a fotografia de boa qualidade. A decisão pode ser revisitada até a Semana 7.

</div>

<!--
Notas: Slide novo desta revisão, endereça a dificuldade nº 7 do plano de aula. Alguns estudantes chegam à Semana 6 sem ter decidido a trilha. Usar o próprio moodboard como critério de decisão. Nenhuma trilha é tecnicamente mais fácil nem vale mais nota — mas para quem não tem boa fotografia disponível, a estilizada reduz o risco de imagem de origem ruim.
-->

---

## Escala importa tanto quanto seamless

A textura pode estar perfeita e ainda parecer **errada** no asset.

- Tiles **grandes demais**: pedras gigantes, quebra a crença
- Tiles **pequenos demais**: pedras minúsculas, vira ruído

Ajustar com o nó **Mapping** + **Texture Coordinate** no Blender.

<!--
Notas: Erro comum nº 5. Escala não é problema do seamless — é de mapeamento. Adicionar nó Mapping (Shift+A > Vector > Mapping) entre Texture Coordinate e Image Texture, ajustar Scale em X e Y. Referência física: uma pedra de parede medieval tem 20-40 cm — quanto isso é em relação ao Asset 01?
-->

---

## Preserve o material da Semana 5

Ao conectar a textura ao **Base Color**, **não** perca o resto.

- **Metallic** e **Roughness** devem manter os valores calibrados
- Trocar o Albedo **não** significa zerar os outros canais

<div class="error">

Adicionar o nó Image Texture e, sem querer, desconectar Metallic/Roughness — que voltam ao padrão.

</div>

<!--
Notas: Erro comum recorrente. Ao adicionar o Image Texture, o estudante às vezes desfaz outros inputs. Verificar no Principled BSDF: Base Color conectado ao Image Texture, Metallic e Roughness com valores não-padrão coerentes com o material (ex: o Roughness 0.85 da pedra calibrado na Semana 5 continua lá?). Vale para as duas trilhas — o Albedo muda, o restante do material calibrado não.
-->

---

## Erros comuns

<div class="error">

**Patch em linha reta** — troca a costura por um padrão de linhas paralelas.

</div>

<div class="error">

**Confiar no PNG isolado** — a costura só aparece quando tilea. Use o Wrap Around.

</div>

<div class="error">

**Imagem de origem com sombra dura ou pincelada direcional** — o gradiente "gira" com o tile e não se corrige por offset simples.

</div>

<!--
Notas: Os três erros mais frequentes da semana, alinhados ao bloco de dificuldades do plano, agora cobrindo as duas trilhas. Circular no estúdio caçando exatamente estes padrões. Para sombra dura: orientar imagens de dia nublado / iluminação difusa; se a sombra for leve, suavizar com Dodge/Burn ou níveis antes do offset. Para pincelada direcional forte na trilha estilizada, o princípio é o mesmo: suavizar antes de aplicar o offset.
-->

---

<!-- _class: industry -->

## Na indústria

Bibliotecas como Quixel Megascans e Poliigon existem porque poucos estúdios pintam textura seamless do zero — a competência real de produção é adaptar e integrar referência de qualidade ao material do próprio projeto, não recriar tudo manualmente. Isso vale tanto para bibliotecas fotográficas quanto para bibliotecas de texturas pintadas usadas em jogos estilizados.

Saber reconhecer (e corrigir) uma textura que não fecha em tile é tão valorizado quanto saber produzir uma do zero — é o defeito mais rápido de notar em qualquer render de superfície repetida.

<!--
Notas: Contextualizar o valor profissional. O uso de bibliotecas de textura (escaneada ou pintada) é rotina em produção — a habilidade técnica cobrada do artista é curadoria, adaptação e correção de seams, não produção manual de tudo, em nenhuma das duas trilhas. Amarra à Semana 13/14: a mesma atenção a costura sem descontinuidade volta no tiling de trim sheets.
-->

---

<!-- _class: summary-slide -->

# Resumo

- **Seamless** = bordas contínuas; a repetição fica invisível — em foto ou em pintura
- **Offset** traz a costura das bordas para o centro
- **Patch** irregular cobre a costura sem criar novo padrão
- **Wrap Around (W)** é o feedback em tempo real
- Preserve **Metallic** e **Roughness** ao conectar o Albedo, em qualquer trilha

<!--
Notas: Amarrar a mini aula. Cada item retorna na demonstração e no estúdio. Não reler tudo — apontar a conexão com a demo (pedra seamless no Krita -> Blender, com uma comparação rápida com o caso estilizado ao final). Lembrar: hoje é crítica INFORMAL; o foco é ler costura e coerência temática (e coerência de trilha) no trabalho dos colegas.
-->

---

## No estúdio: textura do Asset 01

Crie uma textura seamless do **material principal** do Asset 01, na trilha visual do seu kit.

Quatro caminhos: criar de foto própria/internet, adaptar do Poly Haven/AmbientCG, criar ou baixar estilizada, ou baixar pronta se o tempo for curto.

<div class="tip">

O que importa é chegar a um **PNG seamless** aplicado ao Albedo do Asset 01 no Blender — com Metallic e Roughness preservados, e a trilha coerente com o moodboard.

</div>

<!--
Notas: Consigna do estúdio (50 min). Se o Asset 01 é parede de pedra medieval, a textura é pedra; se é caixa de metal Sci-Fi, é metal com ferrugem — fotorrealista ou estilizado, conforme a trilha já escolhida. Amarrar ao moodboard: não é "pedra genérica", é AQUELA pedra do tema. Nomenclatura: [Nome]_[material]_seamless_S06.png. Salvar o .kra nativo com as camadas — vai poupar trabalho na Semana 7 (migração para o 3D Coat).
-->

---

## Agora: demonstração

A seguir, uma **pedra seamless ao vivo**: foto → offset → patch → Blender — com uma comparação rápida ao final contra o mesmo processo em uma textura estilizada.

Krita à esquerda com Wrap Around, Blender à direita com o Asset 01.

![large](assets/demo_seamless_krita_blender.webp)

<!--
Notas: Transição para a demonstração de 20 min. Sequência: importar foto -> Wrap Around mostra costura -> Offset 50% -> patch com Clone Stamp -> verificar no Wrap Around -> exportar PNG -> Blender: nó Image Texture no Base Color -> comparar com o Albedo plano da Semana 5 -> fechar mostrando o mesmo processo já aplicado a uma textura pintada estilizada, reforçando que o critério de "está seamless?" é idêntico nas duas trilhas. Deixar uma costura residual é didaticamente valioso: mostrar o ciclo Krita -> Blender -> Reload.

[!FIGURA]
Objetivo didático: dar à turma um alvo visual do resultado esperado e antecipar o layout de tela da demonstração.
Arquivo sugerido: assets/demo_seamless_krita_blender.webp
Descrição: tela dividida. À esquerda, o Krita com uma textura de pedra em Wrap Around (repetição em grade sem costuras). À direita, o Blender em Viewport Rendered com o Asset 01 recebendo a mesma textura de pedra no canal Albedo, sob HDRI neutra.
Como produzir: no Krita, finalizar uma pedra seamless e ativar o Wrap Around. No Blender, aplicar o PNG exportado ao Base Color do Principled BSDF do Asset 01 em Viewport Rendered. Capturar as duas telas e compô-las lado a lado no Krita.
-->
