# Clone 1 — SimpleDiffuse no 3DCoat

20/10/2026 · Rodrigo

## O que vamos clonar

O clone é um Smart Material de 5 camadas que gera uma base hand-painted "de um clique": cor, sombra, cavidade, AO e borda. É o mais simples dos três clones e serve de porta de entrada para os outros dois.

O [SimpleDiffuse](https://nhanceschool.gumroad.com/l/SimpleDiffuse) é vendido como um "material generator" para o Substance Painter. A página não documenta as camadas internas, então este clone é uma **engenharia reversa pelo resultado**: reproduz o comportamento típico de um material diffuse-only, não o arquivo original.

**O clone entrega**

- Um Smart Material `CLONE_SimpleDiffuse` que funciona em qualquer módulo com AO e curvatura calculados.
- 4 controles nomeados: cor base, intensidade da sombra, intensidade da cavidade e intensidade da borda.
- 3 presets (pedra, madeira, metal), criados por duplicação.

**Antes de começar:** faça a Etapa 1 do [tutorial geral](/Tutoriais/Tutorial_Smart_Material_Diffuse_3DCoat.md) (importar com normal map e calcular AO e curvatura). Sem esses mapas, as condições das camadas não têm o que ler.

## Pilha de camadas

Cinco camadas, de baixo para cima. Os valores são um ponto de partida para ajustar no olho.

| # | Nome da camada | Condition | Cor | Opacidade |
| --- | --- | --- | --- | --- |
| 1 | `01 Base – cor` | Always | Cor média do material | 100% |
| 2 | `02 Sombra – intensidade` | Shadow (oclusão) | Base mais escura, levemente fria | 50% |
| 3 | `03 Cavidade – intensidade` | More on concave | Quase preta, fria | 70% |
| 4 | `04 AO – suave` | Shadow (oclusão), contraste baixo | Igual à sombra | 25% |
| 5 | `05 Borda – intensidade` | More on convex | Base mais clara, levemente quente | 60% |

Glossiness e Metalness ficam em zero em todas as camadas. O resultado é só cor.

## Passo a passo

1. **Crie o material.** No painel *Smart Materials*, crie uma pasta `CLONES`, clique no **+** e nomeie `CLONE_SimpleDiffuse`. Abra o *Smart Material Editor*.
   - *Por quê:* uma pasta própria vira um `.3dcpack` único na hora de compartilhar.
2. **Camada 1 — Base.** Cor média, *Condition: Always*.
   - *Por quê:* é a referência de valor de tudo. Escolha um tom médio, para sobrar espaço para escurecer e clarear.
3. **Camada 2 — Sombra.** Condição de oclusão com contraste médio, cor mais escura e um pouco mais fria que a base.
   - *Por quê:* é o que transforma uma cor chapada em volume. Diferente do clone FT, aqui o deslocamento de matiz é pequeno: o SimpleDiffuse é a versão "segura" do estilo.
4. **Camada 3 — Cavidade.** *More on concave*, com *Cavity Width* baixo e *Contrast* alto. Ajuste a largura com *Cavity Area Width*.
   - *Por quê:* desenha o "traço" nas frestas que separa as formas. Fina e escura, ela substitui o lineart que um pintor faria à mão.
5. **Camada 4 — AO suave.** Repita a condição da sombra com contraste baixo e opacidade baixa.
   - *Por quê:* faz a transição entre a fresta nítida (camada 3) e a sombra larga (camada 2). Sem ela, a cavidade parece recortada.
6. **Camada 5 — Borda.** *More on convex*, cor mais clara e levemente quente. Adicione uma imagem de ruído em *Edge Scattering*.
   - *Por quê:* é o highlight de quina do hand-painted. O ruído quebra a borda, para ela parecer pincelada e não filtro.
7. **Nomeie e ordene.** Confira se os nomes seguem a tabela (`01 Base – cor` etc.).
   - *Por quê:* os nomes são a "interface" do material. É assim que ele imita os controles de um produto comercial.

## Presets

Duplique o material (*Duplicate*) e troque só as cores. A estrutura fica igual, e é isso que mantém a coerência do kit.

| Preset | Base | Sombra | Cavidade | Borda |
| --- | --- | --- | --- | --- |
| `CLONE_SD_Pedra` | #9C9282 | #6A6670 | #2A2A33 | #C8BDA6 |
| `CLONE_SD_Madeira` | #8A5A3C | #5E3A2C | #2A1612 | #B88456 |
| `CLONE_SD_Metal` | #7F8A94 | #525E6C | #1E2430 | #C6D0D8 |

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

"—" = a camada não mexe naquele canal (sem valor ou opacidade zero no canal).

1. **Reduza a sombra e o AO pintados.**
   - *Por quê:* o Unity vai sombrear o objeto com a luz real. Manter metade da sombra pintada preserva o estilo sem escurecer demais.
2. **Mova parte do brilho da borda para o gloss.**
   - *Por quê:* no PBR, "quina gasta" é superfície mais lisa, que reflete. Gloss alto faz a borda brilhar de acordo com a posição da luz, em vez de sempre.
3. **Cavidade fosca, sem metal.**
   - *Por quê:* sujeira acumulada não reflete. Mesmo num preset de metal, a cavidade fica com Metalness 0, como poeira ou ferrugem.
4. **Metal: base clara e saturada.** No `CLONE_SD_Metal_PBR`, troque a base para um cinza claro (#9AA0A6) com Metalness 1.
   - *Por quê:* com metalness 1, a cor da base vira a cor do reflexo. Base escura deixa o metal preto no Unity.

**No Unity:** *URP/Lit* em *Workflow Mode: Metallic*, com Base Map, Metallic Map (gloss no alfa, que o URP lê como Smoothness) e Normal Map exportado em OpenGL (Y+).

## Teste e checklist

**Teste de comparação:** coloque lado a lado um print do preview do SimpleDiffuse (página do produto) e o seu módulo com o clone, no mesmo ângulo. Compare valor, contraste de borda e largura da cavidade, não a cor exata.

- [ ] O material funciona com um clique, sem pintura manual.
- [ ] Desligando as camadas 2 a 5 uma a uma, cada uma muda algo visível.
- [ ] A cavidade é mais fina que o AO.
- [ ] A borda acende nas quinas do cubo e quase some na esfera.
- [ ] Os 3 presets usam a mesma estrutura de camadas.
- [ ] A pasta `CLONES` exporta como `.3dcpack` (*Share item folder*).

**Limite do clone:** sem acesso ao arquivo original, a fidelidade é visual. Na crítica, discuta onde o clone difere do preview e por quê.

**Fontes:** [SimpleDiffuse — Gumroad](https://nhanceschool.gumroad.com/l/SimpleDiffuse) · [3DCoat — Smart Materials](https://3dcoat.com/documentation/manual/brush-components/smart-materials/) · [3DCoat — Cavity and Curvature](https://3dcoat.com/documentation/?p=10661)
