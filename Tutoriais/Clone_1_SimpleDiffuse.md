# Clone 1 — SimpleDiffuse no 3DCoatTextura

20/10/2026 · Rodrigo

> **3DCoatTextura 2026.** Na versão 2026.11, os Smart Materials padrão da biblioteca foram convertidos para o sistema de nós (*NGMaterials*). Este tutorial monta o material no **Smart Material Editor** (camadas com *Condition Mask*), o fluxo clássico. Antes da aula, confira na versão do laboratório se o botão **+** do painel *Smart Materials* ainda cria um Smart Material desse tipo. Se não criar, monte cada camada em nós: um *SimpleMaterial* com a cor da camada e um *SimpleMask* com o *condition type* equivalente (*More on Convex* → convex, *More on Concave* → concave, *More on Shadow* → in shadow).

## O que vamos clonar

O clone é um Smart Material de 8 camadas que gera uma base hand-painted "de um clique": cor, sombra, cavidade, AO, borda, gradientes de topo e de base e variação de cor. É o mais simples dos três clones e serve de porta de entrada para os outros dois.

O [SimpleDiffuse](https://nhanceschool.gumroad.com/l/SimpleDiffuse) é vendido como um "material generator" para o Substance Painter. A página dele não lista os controles, mas a do [SimplePBR](https://www.artstation.com/marketplace/p/zR5p8/simplepbr-easy-texturing), do mesmo autor, diz incluir o SimpleDiffuse e descreve os controles. O clone reproduz a parte de cor desses controles. A implementação interna não é pública, então este clone continua sendo uma **engenharia reversa pelo resultado**, não uma cópia do arquivo original.

| Controle do original | Equivalente no clone |
| --- | --- |
| Base Color | Camada 1 — Base |
| Shadow (Shadow Color, Spread) | Camada 2 — Sombra |
| Curvature Color | Camada 3 — Cavidade |
| AO (AO Color, Spread) | Camada 4 — AO |
| Edges (Curvature Opacity) | Camada 5 — Borda |
| Gradients (claro de cima, escuro multiplicado de baixo; Gradient Color, Power) | Camadas 6 e 7 — Gradientes de topo e de base |
| Texturizer (variação de cor com ruídos) | Camada 8 — Variação |
| Base Light, Rim Light | Fora deste clone: é o assunto do [Clone 3](/Tutoriais/Clone_3_SoMuchDiffuse.md) (rig de luz e underlight) |
| Post Process (Multiply, Overlay) | Ajustes finais da camada no 3DCoatTextura (opacidade, *Adjust*), se necessário |

**O clone entrega**

- Um Smart Material `CLONE_SimpleDiffuse` que funciona em qualquer módulo com AO e curvatura calculados.
- 7 controles nomeados: cor base, intensidade da sombra, da cavidade e da borda, intensidade dos gradientes de topo e de base e intensidade da variação.
- 3 presets (pedra, madeira, metal), criados por duplicação.

**Antes de começar:** faça a preparação abaixo. Sem AO e curvatura calculados, as condições das camadas não têm o que ler.

## Preparação: os mapas que alimentam as máscaras

Nada no material funciona sem AO e curvatura calculados. Todas as camadas do clone (sombra, cavidade, AO e borda) leem esses mapas.

**Pré-requisitos**

- Um módulo do kit (parede, piso, pilar) com UVs sem sobreposição. A sobreposição quebra AO e curvatura.
- **Opcional:** mapa de normal assado do high poly no Blender (o 3DCoatTextura não faz bake de high para low). Sem ele, o material funciona com a geometria da própria low poly.
- Quinas importantes chanfradas (bevel) no Blender, principalmente se não houver normal map. É no chanfro que a borda ganha largura para aparecer.
- 3DCoatTextura 2026, a versão adotada na disciplina. Os nomes das opções podem variar um pouco entre atualizações.

1. **Importe o low poly (e o normal map, se houver).** Em *File → Import*, carregue o módulo para o *Paint Room* (UV/Per-pixel painting). Se tiver normal map, aplique-o numa camada.
   - *Por quê:* a curvatura do 3DCoatTextura é calculada a partir da malha e do relevo visível. Com normal map, as máscaras enxergam também o detalhe esculpido (rachaduras, entalhes). Sem ele, enxergam só a geometria da low poly: bordas aparecem apenas nas quinas que existem em polígonos e cavidades apenas onde a malha tem reentrâncias.
   - Sem normal map, o detalhe fino pode ser pintado no canal *Depth* antes de calcular a curvatura. As condições passam a reagir a ele, e ele vira normal map na exportação.
2. **Isole o normal map (se houver).** Alt+clique no olho da camada do normal, para que só ela fique visível. Sem normal map, apenas deixe ocultas as outras camadas com relevo.
   - *Por quê:* outras camadas visíveis contaminam o cálculo.
3. **Calcule oclusão e curvatura.** Em *Edit → Calculate Occlusion and Curvature maps*, com a opção *Local Curvature RGB for Cavity map*.
   - Para frestas nítidas (estilo cavity), use intensidade alta (ex.: curvature 400, long-range 10). Para formas grandes e suaves, use intensidade baixa (ex.: curvature 8, long-range 100). Valores de exemplo do [manual](https://3dcoat.com/documentation/?p=10661).
   - *Por quê:* o estilo hand-painted precisa das duas escalas. A local dá o highlight fino da borda e a long-range dá o volume.
4. **Confira o Cavity RGB.** Em *Edit → Preferences → Tools*, verifique se a opção *RGB Cavity "Curvature"* está ativa (no 3DCoatTextura 2026 ela já vem ativa por padrão).
   - *Por quê:* ele libera o controle *Cavity Area Width* no editor, que a camada de cavidade usa para ajustar a largura das frestas.

**Evidência:** antes de seguir, mostre ao colega ao lado os mapas de AO e curvatura. Escuro nas frestas e claro nas quinas vivas significa que deu certo.

## Pilha de camadas

Oito camadas, de baixo para cima. Os valores são um ponto de partida para ajustar no olho.

| # | Nome da camada | Condition Mask | Cor | Opacidade |
| --- | --- | --- | --- | --- |
| 1 | `01 Base – cor` | Always | Cor média do material | 100% |
| 2 | `02 Sombra – intensidade` | More on Shadow | Base mais escura, levemente fria | 50% |
| 3 | `03 Cavidade – intensidade` | More on Concave | Quase preta, fria | 70% |
| 4 | `04 AO – suave` | More on Shadow, contraste baixo | Igual à sombra | 25% |
| 5 | `05 Borda – intensidade` | More on Convex | Base mais clara, levemente quente | 60% |
| 6 | `06 Gradiente topo – intensidade` | More on Top | Base mais clara e quente | 20 a 35% |
| 7 | `07 Gradiente base – intensidade` | More on Bottom | Base mais escura e fria | 20 a 35% |
| 8 | `08 Variação – intensidade` | Always + textura de ruído grande (Cube) | Base com matiz deslocado 5 a 10° | 10 a 20% |

Glossiness e Metalness ficam em zero em todas as camadas. O resultado é só cor.

## Passo a passo

1. **Crie o material.** No painel *Smart Materials*, crie uma pasta `CLONES`, clique no **+** e nomeie `CLONE_SimpleDiffuse`. Abra o *Smart Material Editor*.
   - *Por quê:* uma pasta própria vira um `.3dcpack` único na hora de compartilhar.
2. **Camada 1 — Base.** Cor média, *Condition Mask: Always*.
   - *Por quê:* é a referência de valor de tudo. Escolha um tom médio, para sobrar espaço para escurecer e clarear.
3. **Camada 2 — Sombra.** *Condition Mask* *More on Shadow* com *Contrast* médio, cor mais escura e um pouco mais fria que a base.
   - *Por quê:* é o que transforma uma cor chapada em volume. Diferente do clone FT, aqui o deslocamento de matiz é pequeno: o SimpleDiffuse é a versão "segura" do estilo.
4. **Camada 3 — Cavidade.** *More on Concave*, com *Cavity Width* baixo e *Contrast* alto. Ajuste a largura com *Cavity Area Width*.
   - *Por quê:* desenha o "traço" nas frestas que separa as formas. Fina e escura, ela substitui o lineart que um pintor faria à mão.
5. **Camada 4 — AO suave.** Repita a condição da sombra com contraste baixo e opacidade baixa.
   - *Por quê:* faz a transição entre a fresta nítida (camada 3) e a sombra larga (camada 2). Sem ela, a cavidade parece recortada.
6. **Camada 5 — Borda.** *More on Convex*, cor mais clara e levemente quente. Adicione uma imagem de ruído em *Edge Scattering*.
   - *Por quê:* é o highlight de quina do hand-painted. O ruído quebra a borda, para ela parecer pincelada e não filtro.
7. **Camada 6 — Gradiente de topo.** *Condition Mask: More on Top*, cor mais clara e levemente quente que a base, opacidade de 20 a 35%.
   - *Por quê:* é o gradiente claro de cima do original. O topo da peça recebe a luz do céu, e o gradiente dá leitura de altura ao módulo mesmo sem luz assada.
   - Por ser uma condição, o gradiente fica **dentro** do Smart Material e funciona com um clique em qualquer peça. Ele é calculado pela orientação do objeto no momento do Fill: se a peça for girada depois, refaça o Fill.
8. **Camada 7 — Gradiente de base.** *Condition Mask: More on Bottom*, cor mais escura e um pouco mais fria que a base, opacidade de 20 a 35%. Se o editor da sua versão tiver modo de mistura por camada, use *Multiply*.
   - *Por quê:* é o gradiente escuro "multiplicado" de baixo do original. Ele "assenta" a peça no chão e evita que a parte de baixo fique tão clara quanto o topo.
9. **Camada 8 — Variação.** *Condition Mask: Always*, com uma textura de ruído grande (manchas do tamanho de cerca de 1/4 do objeto) no canal *Color*, *Preferred Mapping: Cube*. Use a cor da base com o matiz deslocado 5 a 10° e opacidade de 10 a 20%.
   - *Por quê:* é o *Texturizer* do original. Superfícies reais nunca têm matiz uniforme, e a variação grande evita o aspecto de "plástico pintado".
   - Prefira um ruído pintado no Krita, com manchas suaves e pouco contraste. Ruído fotográfico de grão fino quebra o estilo.
10. **Nomeie e ordene.** Confira se os nomes seguem a tabela (`01 Base – cor` etc.).
   - *Por quê:* os nomes são a "interface" do material. É assim que ele imita os controles de um produto comercial.

## Presets

Duplique o material (*Duplicate*) e troque só as cores. A estrutura fica igual, e é isso que mantém a coerência do kit.

| Preset | Base | Sombra | Cavidade | Borda | Gradiente topo | Gradiente base |
| --- | --- | --- | --- | --- | --- | --- |
| `CLONE_SD_Pedra` | #9C9282 | #6A6670 | #2A2A33 | #C8BDA6 | #B8AE98 | #4E4A58 |
| `CLONE_SD_Madeira` | #8A5A3C | #5E3A2C | #2A1612 | #B88456 | #A87650 | #3E2622 |
| `CLONE_SD_Metal` | #7F8A94 | #525E6C | #1E2430 | #C6D0D8 | #A6B2BC | #3A4452 |

A camada de variação usa a cor da base de cada preset com o matiz levemente deslocado.

No metal, suba a opacidade da borda para 80 a 90%. O contraste forte nas quinas é o que lê como metal num material sem brilho real.

## Versão PBR

A versão PBR mantém a cor do Clone 1 e acrescenta Glossiness e Metalness por camada, seguindo a lógica do SMM\_SoMuchRoughness (detalhada no [Clone 3](/Tutoriais/Clone_3_SoMuchDiffuse.md)). Use quando o kit tiver luz dinâmica no Unity.

Duplique `CLONE_SimpleDiffuse` como `CLONE_SimpleDiffuse_PBR`:

| # | Camada | Color | Glossiness | Metalness |
| --- | --- | --- | --- | --- |
| 1 | `01 Base` | Igual | Base do kit (pedra 0.20 · madeira 0.30 · metal 0.55) | 0 (metal: 1) |
| 2 | `02 Sombra` | Opacidade de 50% para 25% | — | — |
| 3 | `03 Cavidade` | Igual | 0.10 | 0 |
| 4 | `04 AO` | Opacidade de 25% para 15% | — | — |
| 5 | `05 Borda` | Opacidade de 60% para 35% | Base + 0.30 | — |
| 6 | `06 Gradiente topo` | Opacidade para 10% ou desligada | — | — |
| 7 | `07 Gradiente base` | Opacidade para 10 a 15% | — | — |
| 8 | `08 Variação` | Igual | — | — |

"—" = a camada não mexe naquele canal (sem valor ou opacidade zero no canal).

1. **Reduza a sombra, o AO e os gradientes pintados.**
   - *Por quê:* o Unity vai sombrear o objeto com a luz real. Manter metade da sombra pintada preserva o estilo sem escurecer demais. Os gradientes são luz pintada: com luz dinâmica, o de topo quase some e o de base fica bem leve.
2. **Mova parte do brilho da borda para o gloss.**
   - *Por quê:* no PBR, "quina gasta" é superfície mais lisa, que reflete. Gloss alto faz a borda brilhar de acordo com a posição da luz, em vez de sempre.
3. **Cavidade fosca, sem metal.**
   - *Por quê:* sujeira acumulada não reflete. Mesmo num preset de metal, a cavidade fica com Metalness 0, como poeira ou ferrugem.
4. **Metal: base clara e saturada.** No `CLONE_SD_Metal_PBR`, troque a base para um cinza claro (#9AA0A6) com Metalness 1.
   - *Por quê:* com metalness 1, a cor da base vira a cor do reflexo. Base escura deixa o metal preto no Unity.

**No Unity:** *URP/Lit* em *Workflow Mode: Metallic*, com Base Map, Metallic Map (gloss no alfa, que o URP lê como Smoothness) e Normal Map exportado em OpenGL (Y+).

## Teste e checklist

**Teste de comparação:** coloque lado a lado um print do preview do SimpleDiffuse (página do produto) e o seu módulo com o clone, no mesmo ângulo. Compare valor, contraste de borda, largura da cavidade e a diferença entre topo e base, não a cor exata.

- [ ] O material funciona com um clique, sem pintura manual.
- [ ] Desligando as camadas 2 a 8 uma a uma, cada uma muda algo visível.
- [ ] O topo da peça é mais claro que a parte de baixo (gradientes).
- [ ] A cavidade é mais fina que o AO.
- [ ] A borda acende nas quinas do cubo e quase some na esfera.
- [ ] Os 3 presets usam a mesma estrutura de camadas.
- [ ] A pasta `CLONES` exporta como `.3dcpack` (*Share item folder*).

**Limite do clone:** sem acesso ao arquivo original, a fidelidade é visual. Na crítica, discuta onde o clone difere do preview e por quê.

**Fontes:** [SimpleDiffuse — Gumroad](https://nhanceschool.gumroad.com/l/SimpleDiffuse) · [SimplePBR — ArtStation (lista de controles)](https://www.artstation.com/marketplace/p/zR5p8/simplepbr-easy-texturing) · [3DCoat — Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) · [3DCoat — Smart Materials](https://3dcoat.com/documentation/manual/brush-components/smart-materials/) · [3DCoat — Cavity and Curvature](https://3dcoat.com/documentation/?p=10661)
