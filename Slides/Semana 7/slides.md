---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 07"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Texturização

## Profundidade direto da malha

**Semana 7** — Migração para o 3D Coat: mesh maps (AO, Curvature, Normal) e Smart Materials

<!--
Notas: Marcar a virada de ferramenta: o Blender deixa de montar o material e passa a só exportar a malha e receber os mapas de volta. O 3D Coat entra como ferramenta dedicada — e as duas trilhas visuais passam a usar o mesmo fluxo de ferramenta a partir de hoje. Sem crítica formal — a CF2 é na Semana 8.
-->

---

## Onde vocês estão

Semana 6: Hero Asset com textura seamless aplicada ao Albedo, trilha visual já definida.

Hoje: a mesma malha gera profundidade sozinha — sem nós, sem high-poly.

<!--
Notas: Recapitular em uma frase. Não reabrir o conteúdo técnico de seamless da Semana 6 — isso já foi ensinado. Só situar a transição de ferramenta.
-->

---

<div class="objectives">

Ao final da semana você será capaz de:

- Explicar o que são mesh maps (AO, Curvature, Normal) e por que dispensam high-poly
- Exportar do Blender e importar o Hero Asset no 3D Coat (Per-Pixel Painting, Metalness PBR)
- Reconhecer os três espaços de trabalho do 3D Coat (Paint Room, UV Room, Render Room)
- Bakear AO e Curvature e usá-los como máscara de desgaste
- Pintar um Normal Map real no canal Depth, sem nós procedurais
- Montar um material com Color, Roughness e Normal ativos, em qualquer trilha visual

</div>

<!--
Notas: Os três primeiros objetivos são conceituais/mini aula; os demais são o trabalho prático de hoje no estúdio.
-->

---

<!-- _class: question -->

# De onde vem essa profundidade, se eu não pintei nada?

![diagram](assets/parede_ao_curvature_comparacao.webp)

<!--
Notas: Mostrar 3 versões da mesma parede: (1) só Albedo (resultado da Semana 6), (2) com AO multiplicado por cima, (3) com Curvature também aplicado como máscara. Perguntar de onde vem a informação — conduzir a turma a perceber que é a própria geometria (reentrâncias, bordas, bevels), não uma imagem externa.

[!FIGURA]
Objetivo didático — Evidenciar que AO e Curvature nascem da geometria, sem exigir high-poly nem pintura manual.
Arquivo sugerido — assets/parede_ao_curvature_comparacao.webp
Descrição — Três renders lado a lado da mesma parede de pedra: (1) só Albedo/textura seamless da Semana 6, (2) com mapa de AO multiplicado (reentrâncias mais escuras), (3) com Curvature também aplicado (arestas com desgaste/brilho diferenciado).
Como produzir — Renderizar no 3D Coat (Render Room) o mesmo asset de demonstração em três estados de camada: só Color, Color+AO, Color+AO+Curvature.
-->

---

## Mesh maps: profundidade sem high-poly

**Ambient Occlusion (AO)** — mede o quanto cada ponto está "protegido" da luz ambiente. Reentrâncias escurecem, superfícies expostas clareiam.

**Curvature (Cavity)** — mede convexidade/concavidade. Arestas recebem um valor, frestas outro — é o mapa mais útil para simular desgaste de uso.

<!--
Notas: Frestas/cantos internos = mais escuros no AO (é onde sujeira e sombra de contato se acumulam). Arestas/quinas = onde a pintura descasca e o metal fica exposto — o oposto do que acontece nas reentrâncias.
-->

---

## Normal Map: da pintura, não do ruído

Sem high-poly dedicado, o caminho é pintar micro-detalhe direto no canal **Depth** do 3D Coat.

Entalhes, rachaduras, rebites — o software converte a profundidade pintada em Normal Map real na exportação.

<div class="tip">

AO e Curvature nascem da malha de jogo que vocês já modelaram — com os bevels e reentrâncias que ela já tem.

</div>

<!--
Notas: Diferença central em relação ao workflow tradicional de produções AAA: lá o Normal nasce da diferença high-poly/low-poly. Aqui, sem high-poly, o Normal nasce de pintura de profundidade.
-->

---

## O que muda em relação à Semana 6

O Albedo fotográfico ou estilizado continua sendo a base de cor.

O que muda: Roughness, Normal e desgaste agora são **camadas e máscaras no 3D Coat**, geradas da própria malha — não nós no Shader Editor.

<!--
Notas: Reforçar que não é um recomeço — é uma troca de ferramenta para a mesma tarefa de refinar o material.
-->

---

## Duas trilhas, mesmo fluxo de ferramenta

**Fotorrealista:** a foto da Semana 6 entra como camada de Color. AO/Curvature reforçam sombra de contato e desgaste nas bordas por cima dela.

**Estilizada:** um Smart Material (ou camadas equivalentes) substitui a foto. Os mesmos AO/Curvature guiam onde a sujeira e o desgaste aparecem.

<div class="tip">

Nos dois casos, o resultado técnico é equivalente: Color + Roughness + Normal ativos, com máscara de AO/Curvature.

</div>

<!--
Notas: Quem já baixou uma textura estilizada pronta na Semana 6 usa essa imagem como ponto de partida da camada de Color, do mesmo jeito que a trilha fotorrealista usa a foto.
-->

---

## Os três espaços do 3D Coat

**Paint Room** — onde vocês pintam: pincéis, stencils, alphas, camadas com máscara, em qualquer canal PBR.

**UV Room** — conferir se o UV do Blender importou corretamente (o UV já chega pronto).

**Render Room** — visualização em alta qualidade com HDR, para avaliar antes de exportar.

<!--
Notas: No workflow da disciplina os UVs já chegam prontos do Blender — o UV Room serve principalmente para conferência, não para editar UV do zero.
-->

---

## Existe uma via alternativa: nós no Blender

Noise Texture, Bump, ColorRamp — o mesmo princípio raster vs. procedural da Semana 1, aplicado a mapas de suporte.

<div class="tip">

Vantagem: nunca repete um pixel. Desvantagem: controle artístico mais indireto.

</div>

A partir de hoje, o fluxo **oficial** da disciplina é o bake e a pintura dentro do 3D Coat — os nós ficam como leitura complementar (Apostila, Cap. 13), não avaliada.

<!--
Notas: Panorama de 3 min, não é conteúdo obrigatório. Nota: o Subsurface Scattering (SSS) não entra hoje — é apresentado na Semana 8, para não sobrecarregar esta mini aula.
-->

---

<!-- _class: invert -->

## Na indústria

Bake de mesh maps + camadas + máscara é o mesmo princípio do Substance Painter — o padrão de mercado em texturização de jogos.

Nas duas trilhas, o resultado técnico converge: Color, Roughness e Normal ativos.

<!--
Notas: Amarrar a C4 (Materiais PBR) e C5 (Texturização), observados hoje e avaliados formalmente na CF2 (Semana 8).
-->

---

<!-- _class: summary-slide -->

# Resumo

- **AO e Curvature** nascem da geometria — sem high-poly, sem imagem externa
- **Normal** vem de pintura no canal Depth, não de nós procedurais
- **Duas trilhas, mesmo fluxo**: foto ou Smart Material, guiados pela mesma máscara
- Hoje é observação — a **CF2** avalia o material completo na Semana 8

<!--
Notas: Fechar a mini aula amarrando os conceitos antes da demonstração.
-->

---

## Agora: demonstração

Exportar do Blender, importar no 3D Coat, trazer a textura da Semana 6 como Color.

Bakear AO e Curvature, pintar o primeiro Normal via Depth, ajustar Roughness guiado por Curvature.

![diagram](assets/demo_3dcoat_bake_workflow.webp)

<!--
Notas: Transição para os 20 min de demonstração. Passo a passo: (1) exportar FBX com UV, (2) importar Per-Pixel Painting / Metalness PBR / 1024×1024, (3) camada de Color com a textura da Semana 6, (4) bake de AO e Curvature + camada de desgaste em modo Multiply, (5) Normal via pincel de Depth (rachadura, entalhe), (6) Roughness com Fill base + camada guiada por Curvature.

[!FIGURA]
Objetivo didático — Mostrar a sequência do fluxo de migração Blender → 3D Coat até o material com três canais ativos.
Arquivo sugerido — assets/demo_3dcoat_bake_workflow.webp
Descrição — Sequência de 4 capturas de tela do 3D Coat lado a lado: malha recém-importada sem textura, com camada de Color aplicada, com AO/Curvature bakeados e aplicados como máscara de desgaste, e com as primeiras marcas de Normal pintadas no Depth.
Como produzir — Capturar no 3D Coat usando o asset de demonstração do professor (parede simples com textura seamless da Semana 6), salvando cada etapa do Paint Room.
-->

---

<!-- _class: chapter -->

<span class="chapter-number">07</span>

# Produção em estúdio

Do Blender ao 3D Coat: migrando o Hero Asset Referência

<!--
Notas: Divisória entre a mini aula e o estúdio. Os slides a seguir ficam projetados durante a produção — servem de consigna e timebox visíveis, apresentados um a um conforme a etapa correspondente começa.
-->

---

<!-- _class: exercise -->

## Etapa 1 — Exportar e importar no 3D Coat

**≈10 minutos.**

Exportem o Hero Asset do Blender (`.obj`/`.fbx`, com UV incluído).

Importem no 3D Coat: Per-Pixel Painting, workflow Metalness PBR, resolução 1024×1024.

<!--
Notas: Encontro 1. Verificar se o UV importou corretamente no UV Room. Em computadores mais lentos, orientar para 512×512.
-->

---

<!-- _class: exercise -->

## Etapa 2 — Camada de Color

**≈10 minutos.**

Trilha fotorrealista: tragam a textura seamless da Semana 6 como camada base de Color.

Trilha estilizada: apliquem um Smart Material (ou montem camadas equivalentes).

<!--
Notas: Verificar se a base de Color está alinhada ao UV — se saiu distorcida, conferir se o UV exportado é o mesmo usado na criação da textura.
-->

---

<!-- _class: exercise -->

## Etapa 3 — Bake de AO/Curvature + desgaste

**≈15 minutos.**

Gerem/bakeiem AO e Curvature a partir da malha.

Criem uma camada de desgaste (modo Multiply) usando AO/Curvature como máscara sobre o Color.

<div class="warning">

AO/Curvature são sempre camada auxiliar por cima da base — nunca a cor final.

</div>

<!--
Notas: Erro comum: aplicar o AO direto no canal Color, apagando a textura de base. Reforçar modo de mistura Multiply/Overlay com opacidade controlada.
-->

---

<!-- _class: exercise -->

## Etapa 4 — Roughness e Normal via Depth

**≈15 minutos.**

Roughness: Fill base + camada guiada por Curvature (arestas mais polidas).

Normal/Depth: pintem 2–3 marcas de profundidade (rachaduras, entalhes) coerentes com o tema.

Salvem: `[Nome]_HeroAsset_3DCoat_S07.3b`.

<!--
Notas: Meta do estúdio de hoje: pelo menos três canais ativos (Color, Roughness, Normal). Perguntar: "essas marcas de profundidade contam uma história? Onde esse objeto seria mais golpeado no universo do kit?"
-->

---

<!-- _class: exercise -->

## Crítica coletiva informal — 20 minutos

**Rodada circulante, 4–5 estações.**

O desgaste das arestas parece físico? As reentrâncias escurecem de forma crível? O Smart Material responde à geometria, ou parece só colado por cima?

<!--
Notas: Abertura do Encontro 2. Fechar nomeando o erro mais comum (tipicamente opacidade excessiva da máscara, ou máscara não conectada ao modo de mistura correto) e o estado geral das duas trilhas.
-->

---

<!-- _class: exercise -->

## Fechamento dos três canais — ≈30 minutos

Quem ainda não completou: revisem Color (alinhado, coerente com a trilha), Roughness (guiado por Curvature) e Normal (2–3 marcas coerentes com o tema).

Salvem: `[Nome]_HeroAsset_3DCoat_S07.3b` (atualizado).

<!--
Notas: Prioridade de quem ainda não tem os três canais ativos. Quem já está satisfeito pode seguir direto para o aprofundamento.
-->

---

<!-- _class: exercise -->

## Aprofundamento — tempo restante

Reforcem o Normal com uma segunda camada de Depth em escala menor (micro sobre macro).

Ou testem um Smart Material diferente e comparem visualmente. Ou explorem o canal Subsurface, se houver elemento orgânico (sem cobrança — o SSS é formalizado na Semana 8).

<!--
Notas: Para quem já tem os três canais fechados. Alternativa: comparar o bake do 3D Coat com a técnica de nós procedurais do Blender (Cap. 13) em uma segunda superfície.
-->

---

<!-- _class: exercise -->

## Antes de sair

Confirmem as entregas de hoje:

- Hero Asset no 3D Coat com **Color + Roughness + Normal ativos** (`_HeroAsset_3DCoat_S07`)
- Screenshot do painel de **Layers** (camadas nomeadas)
- Screenshot comparativo **antes/depois** das máscaras de AO/Curvature e do Normal

<div class="warning">

Sem crítica formal hoje. Na semana que vem: **CF2** — apresentem esse material explicando a trilha e as decisões de máscara.

</div>

<!--
Notas: Fechamento (10 min): "Hoje vocês montaram um material PBR completo pela primeira vez dentro do 3D Coat — com profundidade vinda da própria malha e do pincel, não de nós matemáticos." Ponte: na Semana 8 o material é refinado e exportado com os quatro mapas PBR completos.
-->
