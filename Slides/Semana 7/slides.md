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

# O material sai do Blender

## Migração para o 3D Coat: mesh maps e Smart Materials

**Semana 7** — AO, Curvature e Normal direto da malha

<!--
Notas: Abertura da mini aula (20 min). Unidade II, entre a Semana 6 e a CF2 (Semana 8). Mudança de ferramenta desta semana: o Blender deixa de ser onde o material é montado e passa a ser só exportação/reconexão. O 3D Coat entra como ferramenta dedicada de texturização — e entra cedo, porque a partir de hoje as duas trilhas visuais (fotorrealista e estilizada) usam o MESMO fluxo de ferramenta, divergindo só na camada de Color. Saída da semana: primeiro material PBR completo dentro do 3D Coat (Color + Roughness + Metallic + Normal via bake/pintura). SSS não é abordado hoje — vai para a Semana 8.
-->

---

## Objetivos de hoje

Ao final da semana você será capaz de:

- Explicar o que são **mesh maps** (AO, Curvature, Normal) e por que não exigem high-poly
- Exportar do Blender e importar no 3D Coat em **Per-Pixel Painting** (Metalness PBR)
- Reconhecer os três **Rooms** do 3D Coat e a lógica de camadas por canal
- **Bakear** AO e Curvature direto da malha e usá-los como máscara de desgaste
- Pintar um **Normal Map real** no canal Depth — sem nós procedurais

<!--
Notas: Ler rápido. Cada objetivo retorna ao longo da aula. Objetivo 9 do plano (situar o bake dentro do conceito de texturização procedural da Semana 1) fica para o slide de panorama mais adiante. SSS não é tratado hoje — Semana 8.
-->

---

<!-- _class: question -->

# Essa profundidade veio de onde? Eu não pintei nada ainda.

<!--
Notas: Abrir com comparação visual no projetor (imagens estáticas), três versões do mesmo asset de parede de pedra: (1) só Albedo — Semana 6. (2) + Ambient Occlusion multiplicado sobre o Albedo — reentrâncias escurecem. (3) + Curvature como máscara — arestas recebem desgaste/brilho diferenciado. Conduzir a turma a perceber que a resposta é a própria geometria do asset: reentrâncias, bordas e bevels. Aguardar 2-3 respostas antes de revelar o conceito.

[!FIGURA — produzir novo material, o conteúdo mudou de Blender-procedural para 3D Coat/mesh maps]
Objetivo didático: provocar a turma a perceber que a profundidade nasce da geometria, não de pintura manual, ancorando o conceito de mesh map antes da definição.
Arquivo sugerido: assets/parede_ao_curvature_tres_estagios.webp (não existe ainda — precisa ser produzido)
Descrição: a mesma parede de pedra em três painéis lado a lado — (1) só Albedo, (2) + AO multiplicado, (3) + Curvature como máscara de desgaste nas arestas.
Como produzir: no 3D Coat, importar o asset de demonstração com a textura seamless da Semana 6 no Color, capturar o Render Room sem máscara, gerar AO e capturar de novo, gerar Curvature e aplicar como máscara de desgaste e capturar uma terceira vez. Compor os três lado a lado no Krita com rótulos.
-->

---

## Mesh maps: informação que já mora na malha

**Ambient Occlusion (AO)** — mede o quanto cada ponto está "protegido" da luz ambiente pela geometria ao redor. Frestas e cantos internos escurecem; superfícies expostas clareiam.

**Curvature (Cavity)** — mede convexidade/concavidade. Arestas e quinas recebem um valor; sulcos e frestas recebem outro — o mapa mais útil para simular desgaste de uso.

<div class="tip">

Nenhum dos dois exige **high-poly**: nascem do próprio bevel e da topologia do asset de jogo que você já modelou.

</div>

<!--
Notas: Ponto central da mini aula. Ferramentas como 3D Coat e Substance Painter extraem essa informação direto da malha 3D. AO simula acúmulo natural de sombra/sujeira em reentrâncias. Curvature é o mapa mais útil para desgaste: bordas são onde a pintura descasca e o metal fica exposto — o oposto das reentrâncias.
-->

---

## Normal Map: agora nasce do pincel, não do ruído

Em produções com high-poly, o Normal vem da diferença entre a malha detalhada e a de jogo. **Aqui, sem high-poly dedicado, o caminho é outro.**

Pinta-se micro-detalhe direto no canal **Depth** do 3D Coat — trincas, entalhes, rebites, veios — usando pincéis e alphas. O software converte essa profundidade pintada em um Normal Map real na exportação.

<div class="best">

Nada de Noise Texture. O relevo desta semana tem **autoria**: cada marca é uma decisão sobre onde o objeto foi tocado ou golpeado.

</div>

<!--
Notas: Diferença central em relação ao que a Semana 6 e a Apostila (Cap. 13) descrevem como via alternativa. O Normal Map desta semana nasce de pintura de profundidade, não de matemática de ruído. Preparar a turma para a Demonstração, onde isso é feito ao vivo.
-->

---

## O que muda (e o que não muda) desde a Semana 6

O **Albedo** fotográfico ou estilizado da Semana 6 continua sendo a base de cor — nada disso se perde.

O que muda é **onde** e **como** as camadas seguintes são construídas:

| Semana 6 (Blender) | Semana 7 (3D Coat) |
|---|---|
| Nós no Shader Editor | Camadas e máscaras no Paint Room |
| Roughness/Normal por matemática | Roughness/Normal a partir da malha e do pincel |
| Blender monta o material | Blender só exporta e recebe de volta |

<!--
Notas: Reforçar que não é um recomeço — é uma migração de ferramenta. O UV e o Albedo da Semana 6 seguem valendo; a diferença é o lugar onde o resto do material é construído. Isso tranquiliza estudantes que investiram tempo na textura seamless da semana passada.
-->

---

<!-- _class: comparison -->

## As duas trilhas — mesmo fluxo, camada de Color diferente

**Fotorrealista**
A foto da Semana 6 entra como camada de Color base. AO/Curvature multiplicam por cima, reforçando sombra de contato e desgaste nas bordas — refinamento físico sobre uma base já realista.

**Estilizada**
Um **Smart Material** (ou camadas equivalentes) substitui a foto. Os mesmos mapas de AO/Curvature funcionam como máscara automática de onde sujeira, brilho e desgaste aparecem — a mesma lógica do Substance Painter.

<!--
Notas: Nos dois casos o resultado técnico é equivalente: Color + Roughness + Normal ativos, com máscaras de AO/Curvature orientando o desgaste. Quem baixou textura estilizada pronta na Semana 6 usa essa imagem como ponto de partida da camada de Color, igual à trilha fotorrealista usa a foto. Se a biblioteca de Smart Materials do laboratório for limitada, montar manualmente: camada de Color + variação com Brush + camada de desgaste mascarada por AO/Curvature — o conceito pedagógico é o mesmo.
-->

---

<!-- _class: three-columns -->

## Os três Rooms do 3D Coat

**Paint Room**
Espaço principal. Pincéis, stencils, alphas e camadas com máscara em qualquer canal PBR — Color, Roughness, Metallic, Normal/Depth.

**UV Room**
Visualização das UVs já prontas do Blender. Serve para conferir se o mapa importou corretamente — não para desenrolar do zero.

**Render Room**
Renderização de alta qualidade com iluminação HDR, para avaliar o resultado antes de exportar.

<!--
Notas: Orientação de interface, rápida. No workflow da disciplina os UVs já chegam prontos do Blender — o UV Room é checagem, não produção. Nomes exatos de painéis variam por versão do 3D Coat; verificar antes da aula.
-->

---

<!-- _class: timeline -->

## O percurso da migração

1. **Exportar** o asset do Blender — `.obj`/`.fbx`, UV incluída
2. **Importar** no 3D Coat — Per-Pixel Painting, Metalness PBR, 1024×1024
3. **Color** — trazer a textura da Semana 6 (ou Smart Material) como camada base
4. **Bakear AO e Curvature** direto da malha
5. **Desgaste** — nova camada em Multiply, mascarada por AO/Curvature
6. **Depth** — pintar 2–3 marcas de profundidade → Normal Map real

<!--
Notas: Roteiro da Demonstração (20 min) e também da Produção em Estúdio. Passo 1: File → Export → FBX, preferir FBX com mais de um objeto. Passo 2: File → Import for Per-Pixel Painting, confirmar UV e resolução. Passo 4: painel de geração varia por versão — geralmente em Textures ou como Fill Layer com gerador procedural; alternativa manual se instável: pincel de opacidade baixa nas reentrâncias/arestas. Passo 6: canal Roughness recebe o mesmo tratamento por Curvature logo em seguida (arestas mais polidas).

[!FIGURA — produzir novo material, o diagrama Noise/Bump/ColorRamp do deck anterior não se aplica mais]
Objetivo didático: dar suporte visual ao roteiro de 6 passos da migração Blender → 3D Coat.
Arquivo sugerido: assets/fluxo_migracao_3dcoat.png (não existe ainda — precisa ser produzido, por exemplo via o mesmo pipeline de mermaid → imagem já usado no deck da Semana 7 anterior)
Descrição: fluxograma linear com os 6 passos acima, destacando que os passos 4 e 6 usam a mesma máscara de Curvature.
-->

---

## Geração procedural: continua existindo, mas não é o fluxo de hoje

*"Existe um segundo caminho para Normal e Roughness que vocês não vão usar hoje: nós matemáticos no Blender — Noise, Bump, ColorRamp, como no Capítulo 13 da Apostila."*

<div class="curiosity">

Mesmo princípio de **raster vs. procedural** da Semana 1 — só que aplicado a mapas de suporte, não ao Albedo inteiro. Vantagem dos nós: nunca repete um pixel; desvantagem: controle artístico mais indireto.

</div>

<!--
Notas: Panorama de 3 min, não uma segunda mini aula. A partir de hoje o fluxo oficial da disciplina é o bake e a pintura dentro do 3D Coat. Leitura complementar recomendada, não avaliada nesta semana: Apostila, Parte IV, Cap. 13 — Texturização Procedural. Quem quiser comparar as duas técnicas pode aplicar nós em um Asset Secundário do kit mais adiante.
-->

---

## Erros comuns

<div class="error">

**AO/Curvature como cor final** — o mapa é conectado direto ao Color, apagando a textura de base. Deve entrar como camada auxiliar em Multiply/Overlay, nunca como base.

</div>

<div class="error">

**UV ausente ou incorreto na importação** — malha aparece esticada ou uniforme no Paint Room. Reexportar como `.fbx` ou conferir "UV Coords" no export `.obj`.

</div>

<div class="error">

**Normal via Depth exagerado ou sutil demais** — força de pincel padrão gera cratera ou relevo imperceptível. Calibrar comparando com referência no Render Room.

</div>

<!--
Notas: Os três erros mais frequentes da semana, alinhados ao bloco de dificuldades do plano. Circular no estúdio caçando exatamente estes padrões. Perguntas de mediação: "Essa camada de AO está em que modo de mistura?" / "Você usou o Curvature para clarear as arestas ou só pintou onde achou bonito?"
-->

---

<!-- _class: industry -->

## Na indústria

Bakear mesh maps direto da geometria e aplicar materiais com camadas e máscaras automáticas é o fluxo padrão de ferramentas como **Substance Painter** — Smart Materials reagem à curvatura e ao AO do asset exatamente como vocês estão fazendo hoje no 3D Coat.

Essa é a mesma lógica usada em produções AAA para "envelhecer" props e ambientes de forma consistente, sem repintar cada aresta manualmente.

<!--
Notas: Contextualizar o valor profissional. O 3D Coat e o Substance Painter compartilham o mesmo princípio conceitual (camadas mascaradas por mapas gerados da malha) — o estudante que domina esse fluxo aqui transfere a lógica para qualquer ferramenta de mercado equivalente.
-->

---

<!-- _class: summary-slide -->

# Resumo

- **Mesh maps** (AO, Curvature) nascem da malha — sem high-poly
- **Normal** desta semana vem de pintura no canal **Depth**, não de ruído
- Fluxo: exportar do Blender → importar no 3D Coat → Color → bake AO/Curvature → Depth
- Duas trilhas, **mesmo fluxo**: fotorrealista (foto + máscara) × estilizada (Smart Material + máscara)
- Meta do estúdio: **Color + Roughness + Normal** ativos no Asset 01
- **SSS** fica para a Semana 8 — hoje não entra no vocabulário da aula

<!--
Notas: Amarrar a mini aula. Cada item retorna na demonstração e no estúdio. Hoje é crítica INFORMAL; o foco é ler profundidade e coerência do material no trabalho dos colegas. Na Semana 8 (CF2, crítica FORMAL) o material é refinado e os quatro mapas PBR são exportados.
-->

---

## No estúdio: primeira migração para o 3D Coat

Exporte o Asset 01, importe no 3D Coat e monte **Color + Roughness + Normal** — seguindo sua trilha visual.

<div class="tip">

Quem chegou sem o Albedo do Asset 02 no Blender: os primeiros 15 min são para concluí-lo, antes de migrar qualquer coisa.

</div>

<!--
Notas: Consigna do estúdio (50 min). Bloco A (~15 min): concluir Albedo do Asset 02 no Blender, para quem ainda não tem. Bloco B (~35 min, toda a turma): exportar Asset 01, importar em Per-Pixel Painting/Metalness PBR/1024x1024, Color com textura da Semana 6 ou Smart Material, bakear AO/Curvature, camada de desgaste mascarada, Roughness guiado por Curvature, 2-3 marcas de Depth. Salvar: [Nome]_Asset01_3DCoat_S07. Papel do professor: verificar alinhamento de UV, uso de AO/Curvature como máscara (não como cor final) e coerência com a trilha escolhida.
-->

---

## Agora: demonstração

A seguir, a migração **ao vivo**: exportar do Blender, importar no 3D Coat, trazer o Color da Semana 6, bakear AO/Curvature e começar o Normal via Depth.

Blender à esquerda, 3D Coat à direita.

<!--
Notas: Transição para a Demonstração de 20 min. Setup: Blender aberto com asset de demonstração (parede simples, textura seamless de pedra já no Albedo). 3D Coat aberto em outra janela. Seguir os 6 passos do slide "O percurso da migração". Fechar com: "eu não pintei nada com a mão até o passo 5 — essa profundidade toda veio da própria malha."

[!FIGURA — produzir novo material, a imagem do deck anterior (Shader Editor / Viewport) não representa mais o fluxo desta semana]
Objetivo didático: dar à turma um alvo visual do resultado esperado e antecipar o layout de tela da demonstração.
Arquivo sugerido: assets/demo_migracao_3dcoat.webp (não existe ainda — precisa ser produzido)
Descrição: tela dividida — à esquerda o Blender com o asset exportado, à direita o 3D Coat no Paint Room mostrando o painel de Layers com AO/Curvature já bakeados.
Como produzir: capturar as duas janelas lado a lado durante um ensaio da demonstração e compor no Krita.
-->
