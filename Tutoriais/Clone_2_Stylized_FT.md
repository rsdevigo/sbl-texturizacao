# Clone 2 — Stylized FT no 3DCoat

20/10/2026 · Rodrigo

## O que vamos clonar

O clone é um Smart Material de 8 camadas que combina um **padrão pintado** (tábuas, blocos, placas) com **mistura de tons quentes e frios**. Ele vai além do Clone 1 porque o material ganha identidade: madeira parece madeira antes de qualquer detalhe.

O [Stylized FT](https://flippednormals.com/product/stylized-ft-smart-material-for-substance-painter-54727), de Fred Taylor, se descreve como baseado em "pattern generation and shade blending". O gerador irmão, [FT Diffuse](https://www.artstation.com/marketplace/p/j8mRg/stylized-texture-generator-for-substance-painter-ft-diffuse), lista os controles. O node graph não é público, então o clone reproduz os controles, não o arquivo.

| Controle do FT | Equivalente no clone |
| --- | --- |
| Pattern generation | Textura tileável pintada no Krita (Color + Depth) |
| Shade blending | Camadas de sombra fria e luz quente com matiz deslocado |
| Cavity | Camada *More on concave* |
| Edges (Intensity / Contrast) | Opacidade e contraste da camada *More on convex* |
| Top gradient (Position) | Camada de topo assada por módulo (Light Baking) |
| Bottom gradient (Position) | Camada de base escura assada por módulo |
| Ambient Occlusion | Camada de oclusão suave |
| Roughness / Metallic | Versão PBR opcional |

**Antes de começar:** faça a Etapa 1 do [tutorial geral](/Tutoriais/Tutorial_Smart_Material_Diffuse_3DCoat.md) e o [Clone 1](/Tutoriais/Clone_1_SimpleDiffuse.md). Este clone parte da estrutura dele.

## Criando os padrões no Krita

O padrão é o coração do FT. Cada material recebe um mapa em tons de cinza, 1024 × 1024 px e tileável, pintado com pinceladas visíveis.

1. **Ative o modo tile.** No Krita, use *View → Wrap Around Mode* (tecla W).
   - *Por quê:* você pinta vendo a repetição, e as emendas somem antes de chegar ao 3DCoat.
2. **Pinte em 3 valores.** Fundo cinza médio (50%), formas em cinza claro (70 a 80%), separações em cinza escuro (20 a 30%).
   - *Por quê:* o mesmo mapa vai para *Color* (como máscara de tom) e para *Depth* (como relevo). Com 3 valores bem definidos, as duas leituras ficam limpas.
3. **Pinte o padrão de cada material:**
   - **Madeira (`PAT_tabuas.png`):** 4 a 6 tábuas verticais com larguras levemente diferentes, veios longos em cinza escuro e 1 ou 2 nós.
   - **Pedra (`PAT_blocos.png`):** blocos irregulares em fiadas alternadas, juntas escuras de 8 a 12 px, quinas arredondadas.
   - **Metal (`PAT_placas.png`):** 2 × 2 placas com rebites nos cantos e um friso escuro de 4 a 6 px entre elas.
   - *Por quê:* irregularidade controlada é a marca do estilizado. Linhas perfeitas parecem procedurais; linhas tortas demais parecem desleixo.
4. **Exporte em PNG 16 bits, escala de cinza.**
   - *Por quê:* 8 bits gera degraus visíveis quando o mapa vira relevo no canal *Depth*.

## Pilha de camadas

As camadas 1 a 6 ficam no Smart Material. As camadas 7 e 8 dependem da posição da peça e são assadas por módulo.

| # | Camada | Condition / fonte | Cor | Opacidade | Onde fica |
| --- | --- | --- | --- | --- | --- |
| 1 | `01 Base – cor` | Always | Cor média | 100% | Smart Material |
| 2 | `02 Padrão – intensidade` | Always + `PAT_*.png` em Color e Depth (Cube) | Base mais clara | 25% | Smart Material |
| 3 | `03 Sombra fria` | Shadow (oclusão) | Escura, matiz 20 a 30° para o frio | 50% | Smart Material |
| 4 | `04 Cavidade` | More on concave | Muito escura e saturada | 70% | Smart Material |
| 5 | `05 AO` | Shadow, contraste baixo | Igual à sombra fria | 25% | Smart Material |
| 6 | `06 Borda – intensidade/contraste` | More on convex | Clara, matiz 10 a 20° para o quente | 60% | Smart Material |
| 7 | `07 Topo – posição` | Light Baking (luz de cima) | Quente, clara | 30 a 40% | Módulo |
| 8 | `08 Base – posição` | Light Baking ou Fill em degradê | Fria, escura | 20 a 30% | Módulo |

## Passo a passo

1. **Duplique o Clone 1.** Em `CLONE_SimpleDiffuse`, use *Duplicate* e renomeie para `CLONE_FT`.
   - *Por quê:* as camadas de base, cavidade, AO e borda já estão prontas. O FT é uma evolução do mesmo esqueleto.
2. **Insira a camada de padrão (2) logo acima da base.** Carregue `PAT_*.png` no canal *Color* e no canal *Depth*, com *Preferred Mapping: Cube*. Mantenha o *Depth* baixo.
   - *Por quê:* no *Color*, o padrão varia o tom. No *Depth*, ele cria relevo, e as camadas de cavidade e borda passam a reagir às juntas e aos veios. É assim que o "pattern generation" conversa com o resto.
   - Cube mapping projeta o padrão pelos 3 eixos, sem depender das UVs. Isso evita costuras em módulos com muitas ilhas.
3. **Converta a sombra em sombra fria (3).** Pegue a cor de sombra do Clone 1 e desloque o matiz 20 a 30° para o azul ou roxo, com um pouco mais de saturação.
   - *Por quê:* este é o *shade blending*. A sombra deixa de ser "base mais escura" e passa a ser outra cor. É a principal diferença visual entre o FT e o SimpleDiffuse.
4. **Aqueça a borda (6).** Desloque o matiz da borda 10 a 20° para o amarelo ou laranja. Use a opacidade como *Intensity* e o contraste da condição como *Contrast*.
   - *Por quê:* quente na luz e frio na sombra cria contraste de temperatura, a assinatura do estilo. Separar intensidade e contraste replica os dois controles de borda do FT.
5. **Asse o degradê de topo (7) e o de base (8) no módulo.** Aplique o material, monte uma luz de cima no Render Room e use *Light Baking* para gravar a luz numa camada em *Screen*. Para a base, use uma camada escura e fria, com degradê de baixo para cima.
   - *Por quê:* o FT tem *Position* nos dois degradês porque a altura da luz muda de peça para peça. No 3DCoat, assar por módulo dá o mesmo controle. Mantenha o mesmo rig de luz em todo o kit.
6. **Confira a ordem de valores.** Cavidade < AO < sombra < base < padrão claro < borda < topo.
   - *Por quê:* se o padrão ficar mais claro que a borda, ele compete com o volume e o objeto achata.

## Presets e versão PBR

Os três presets centrais do FT são madeira, pedra e metal. Cada um troca o padrão e as cores, mantendo a pilha.

| Preset | Padrão | Base | Sombra fria | Borda quente |
| --- | --- | --- | --- | --- |
| `CLONE_FT_Madeira` | `PAT_tabuas.png` | #8A5A3C | #4A2630 (vinho) | #D9A066 |
| `CLONE_FT_Pedra` | `PAT_blocos.png` | #9C9282 | #4E5670 (ardósia) | #E0D2A8 |
| `CLONE_FT_Metal` | `PAT_placas.png` | #7F8A94 | #2E3E52 (petróleo) | #E8E2CC |

Para luz dinâmica no Unity, cada preset ganha uma versão PBR, descrita na seção seguinte.

## Versão PBR

O FT é o único dos três originais que anuncia controles de Roughness e Metallic. No clone, o padrão pintado também comanda o gloss: juntas e veios ficam foscos, superfícies planas ficam um pouco mais lisas. A lógica dos canais segue o SMM\_SoMuchRoughness, detalhada no [Clone 3](/Tutoriais/Clone_3_SoMuchDiffuse.md).

Duplique cada preset com o sufixo `_PBR`, remova as camadas 7 e 8 (degradês assados) e ajuste:

| # | Camada | Color | Glossiness | Metalness |
| --- | --- | --- | --- | --- |
| 1 | `01 Base` | Igual | Base do material (tabela abaixo) | 0 (metal: 1) |
| 2 | `02 Padrão` | Igual | `PAT_*.png` invertido: juntas −0.15 | — |
| 3 | `03 Sombra fria` | Opacidade de 50% para 25% | — | — |
| 4 | `04 Cavidade` | Igual | 0.08 | 0 |
| 5 | `05 AO` | Opacidade de 25% para 15% | — | — |
| 6 | `06 Borda` | Opacidade de 60% para 35% | Base + 0.30 | — |

| Preset PBR | Gloss base | Metalness base | Base (Color) |
| --- | --- | --- | --- |
| `CLONE_FT_Madeira_PBR` | 0.30 | 0 | #8A5A3C |
| `CLONE_FT_Pedra_PBR` | 0.20 | 0 | #9C9282 |
| `CLONE_FT_Metal_PBR` | 0.55 | 1 | #9AA0A6 (mais claro que a versão diffuse) |

"—" = a camada não mexe naquele canal (sem valor ou opacidade zero no canal).

1. **Use o padrão no gloss.** Carregue o mesmo `PAT_*.png` no canal Glossiness da camada 2, invertido, para as partes escuras (juntas, veios) reduzirem o gloss.
   - *Por quê:* o padrão agora define também como a luz desliza na superfície. Uma tábua lisa com juntas foscas lê como madeira mesmo com a luz rasante do Unity.
2. **Mantenha o shade blending, mas mais leve.** A sombra fria e a borda quente continuam na cor, com metade da opacidade.
   - *Por quê:* a temperatura de cor é o que faz o FT parecer FT. A luz do Unity cuida do valor (claro/escuro); a cor pintada cuida do matiz.
3. **Borda com gloss alto, cavidade com gloss baixo.**
   - *Por quê:* equivale aos controles de borda e cavidade do FT aplicados ao roughness. Quinas polidas pegam reflexo e frestas sujas não.
4. **Metal claro e com Metalness 1.**
   - *Por quê:* com metalness 1, a cor da base vira a cor do reflexo (o *Is Metal* do SoMuchRoughness). A sombra fria continua por cima, tingindo o metal de azul nas partes fechadas.

**No Unity:** *URP/Lit* em *Workflow Mode: Metallic*, com Base Map, Metallic Map (gloss no alfa = Smoothness) e Normal Map em OpenGL (Y+). O relevo do canal Depth chega ao Unity pelo normal map.

## Teste e checklist

**Teste de comparação:** aplique o Clone 1 e o Clone 2 no mesmo módulo, lado a lado. A diferença deve ser clara em dois pontos: o padrão identifica o material e as sombras têm outra cor.

- [ ] Os padrões repetem sem emenda visível (teste em um piso 3 × 3).
- [ ] Cavidade e borda reagem às juntas do padrão (canal Depth funcionando).
- [ ] A sombra tem matiz claramente diferente da base.
- [ ] A borda é mais quente que a base.
- [ ] Os degradês de topo e base usam o mesmo rig de luz em todos os módulos.
- [ ] A ordem de valores foi respeitada.
- [ ] Existem 3 presets e, se o projeto pedir, a versão PBR.

**Limite do clone:** o FT original gera os padrões por nodes. Aqui eles são pintados, o que dá mais personalidade ao grupo e menos variação automática.

**Fontes:** [Stylized FT — FlippedNormals](https://flippednormals.com/product/stylized-ft-smart-material-for-substance-painter-54727) · [FT Diffuse — ArtStation](https://www.artstation.com/marketplace/p/j8mRg/stylized-texture-generator-for-substance-painter-ft-diffuse) · [3DCoat — Smart Materials](https://3dcoat.com/documentation/manual/brush-components/smart-materials/) · [3DCoat — Light Baking](https://3dcoat.com/documentation/?p=10277)
