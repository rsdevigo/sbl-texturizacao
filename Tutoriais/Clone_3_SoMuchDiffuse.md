# Clone 3 — SoMuchDiffuse no 3DCoat

20/10/2026 · Rodrigo

## O que vamos clonar

O SoMuchDiffuse é o mais completo dos três: em vez de só combinar máscaras, ele **simula um rig de luz** e grava o resultado no diffuse. O clone divide o trabalho em três partes: Smart Material (forma), rig de luz assado por módulo (luz) e pós-processo (acabamento).

Diferente dos outros dois, este produto tem [documentação pública](https://www.somuchmonsters.com/somuchmaterials-documentation) dos controles. Por isso o clone segue a lista oficial, controle por controle.

| Grupo do SoMuchDiffuse | Controles principais | Equivalente no clone | Parte |
| --- | --- | --- | --- |
| Diffuse Options | Diffuse Color, Shadow Color | Base + camada de sombra em Multiply | A |
| Top Down | Gradient (posição ou lit), Spread, Invert | Degradê de topo assado | B |
| Cavity | Color, Clipping, Contrast, Soft Cavity, Worldspace Intensity | Cavidade nítida + cavidade suave + limpeza no lado iluminado | A e B |
| Ambient Occlusion | Occlusion Color, Spread | Camada de oclusão com cor própria | A |
| Thickness | Color, Spread | Mapa Thickness como máscara | A |
| Specular | Number of Lights, Rig Height, Light Rotation, Exponent | Luzes do Render Room + Light Baking | B |
| Specular Edges | Edge Color, Edge Exponent | Borda × máscara de luz | B |
| Underlight | Gradient Top/Bottom, Intensity, Spread | Luz rebatida de baixo | B |
| WSN Mask | Máscara da parte de baixo | Brilho apagado nas faces voltadas para baixo | B |
| Post Process | Cel Shading, Highlight HSL | Ajustes finais no 3DCoat, Krita ou shader | C |
| Overrides | Baked Lighting on/off | Saída única ou separada | C |

**Antes de começar:** faça o [Clone 1](/Tutoriais/Clone_1_SimpleDiffuse.md). A Parte A parte dele.

## Preparação: os mapas que alimentam as máscaras

O SoMuchDiffuse parte de mapas assados do high poly. O clone precisa de AO e curvatura (os mesmos do Clone 1) e de mais dois mapas: thickness e, opcionalmente, directional occlusion.

1. **Importe o low poly (e o normal map, se houver).** Em *File → Import*, carregue o módulo para o *Paint Room* (UV/Per-pixel painting). O normal map assado do high poly no Blender é **opcional**: se houver, aplique-o numa camada e dê Alt+clique no olho dela, para que só ela fique visível.
   - *Por quê:* a curvatura do 3DCoat é calculada a partir da malha e do relevo visível, e outras camadas visíveis contaminam o cálculo. Sem normal map, as máscaras enxergam só a geometria da low poly, então chanfre (bevel) as quinas importantes no Blender para a borda ter onde aparecer.
2. **Calcule a oclusão (AO).** Em *Edit → Calculate Occlusion and Curvature maps*. Confira também, em *Edit → Preferences → Tools*, se o RGB Cavity está ativo (padrão desde a 2021.53).
   - *Por quê:* as camadas de sombra e de cor de oclusão (2 e 5) leem o AO. O Cavity RGB libera o *Cavity Area Width*, usado nas cavidades.
3. **Curvatura em duas escalas.** Calcule uma vez com intensidade alta (cavity nítida) e guarde. Depois calcule com intensidade baixa e long-range alto (curvatura suave).
   - *Por quê:* o original separa *Cavity* de *Soft Cavity* e tem *Curvature Blur*. Duas escalas reproduzem isso: uma desenha a fresta, a outra o volume.
4. **Thickness.** Em *Light Baking*, tipo *Thickness*. Grave numa camada oculta chamada `MAP_thickness`.
   - *Por quê:* é a máscara do grupo Thickness do original, que marca partes finas onde a luz atravessa.
5. **Directional Occlusion (opcional).** Em *Light Baking*, tipo *Directional Occlusion*.
   - *Por quê:* ao contrário do AO comum, ela considera a direção da luz. Pode substituir a máscara *Worldspace Intensity*, que limpa a sujeira do lado iluminado.

**Evidência:** antes de seguir, mostre ao colega ao lado os mapas de AO, as duas curvaturas e o thickness. Escuro nas frestas, claro nas quinas vivas e claro nas partes finas significa que deu certo.

## Parte A — Smart Material (forma)

Duplique o Clone 1 como `CLONE_SoMuchDiffuse`, **remova as camadas 6 a 8 do Clone 1** (gradientes por condição e variação: aqui a luz de topo e a de baixo vêm do rig assado na Parte B) e reorganize as camadas assim:

| # | Camada | Condition | Modo | Cor | Opacidade |
| --- | --- | --- | --- | --- | --- |
| 1 | `01 Diffuse Color` | Always | Normal | Cor média | 100% |
| 2 | `02 Shadow Color` | Shadow (oclusão), contraste baixo | Multiply | Cor escolhida (ex.: roxo médio) | 40 a 60% |
| 3 | `03 Cavity – clipping/contrast` | More on concave, nítida | Multiply | Escura e saturada | 70% |
| 4 | `04 Soft Cavity` | More on concave, largura alta | Multiply | Igual à cavidade | 25% |
| 5 | `05 Occlusion Color` | Shadow, contraste médio | Multiply | Cor própria do AO (ex.: azul escuro) | 30% |
| 6 | `06 Thickness` | Máscara `MAP_thickness` | Screen | Clara e saturada | 20% |

1. **Use Multiply com uma cor escolhida na sombra (2).**
   - *Por quê:* no original, a *Shadow Color* é multiplicada sobre a *Diffuse Color*. Multiply com uma cor média escurece e tinge ao mesmo tempo, que é o comportamento do produto. Teste roxo, azul ou vinho, conforme o tema.
2. **Separe cavidade nítida (3) e suave (4).**
   - *Por quê:* *Cavity Clipping* e *Contrast* viram largura e contraste da camada 3. *Soft Cavity* e *Smooth Curvature Opacity* viram a camada 4, com largura maior e opacidade baixa.
3. **Dê ao AO uma cor própria (5).**
   - *Por quê:* o original tem *Occlusion Color* separada da *Shadow Color*. Usar outro tom no AO gera uma segunda camada de cor nas áreas fechadas, o que dá riqueza ao estilo.
4. **Thickness em Screen (6).** Só para materiais finos (tecido, folha, couro, cristal). Em pedra e metal, desligue.
   - *Por quê:* Screen clareia sem estourar, imitando a luz que atravessa.

## Parte B — Rig de luz e especular pintado

Esta é a parte que distingue o SoMuchDiffuse. O rig é montado uma vez, salvo, e reaproveitado em todos os módulos do kit.

1. **Monte o rig no Render Room.** Comece com 3 luzes distribuídas ao redor do objeto, na mesma altura (40 a 60° acima do horizonte). Salve a cena de luz como preset do grupo.
   - *Por quê:* é o equivalente a *Number of Lights*, *Specular Rig Height* e *Specular Light Rotation*. Luzes espalhadas acendem todos os lados, e o objeto lê bem de qualquer ângulo de câmera. 1 luz dá mais drama, 4 a 8 luzes dão leitura mais uniforme.
2. **Camada 7 — Top Down.** Asse com *Light Baking → Light From Render Room* numa camada em *Overlay*, com cor quente, a 30 a 40%.
   - *Por quê:* é o *Diffuse Gradient* com *Gradient Type: lit*. A opacidade faz o papel do *Spread*.
3. **Camada 8 — Specular.** Asse de novo, agora com as luzes mais concentradas (spot estreito ou intensidade alta), numa camada em *Add* ou *Screen*, a 20 a 30%.
   - *Por quê:* é o highlight especular pintado. O *Specular Exponent* do original controla o tamanho do brilho, e aqui quem faz isso é a abertura da luz: luz estreita dá brilho pequeno e duro.
4. **Camada 9 — Specular Edge.** Copie a camada de borda do Clone 1 e use a camada 8 como máscara (ou pinte a borda só onde a 8 acende). Cor quase branca e quente.
   - *Por quê:* o *Specular Edge* do original só aparece nas bordas que recebem luz. Brilho em todas as bordas parece plástico.
5. **Camada 10 — Underlight.** Uma luz fraca vinda de baixo, assada numa camada em *Screen*, com a cor do chão (terra, grama), a 15 a 25%.
   - *Por quê:* é o grupo *Underlight* (Gradient Top/Bottom, Intensity, Spread). Separa a peça do piso.
6. **Máscara da parte de baixo (WSN).** Apague com borracha ou máscara as camadas 8 e 9 nas faces voltadas para baixo.
   - *Por quê:* a *WSN Mask* do original impede brilho especular embaixo do objeto. Brilho embaixo desmente a direção da luz.
7. **Limpe a sujeira do lado iluminado.** Reduza a opacidade das camadas 3 e 4 onde a camada 7 está mais forte (máscara pintada ou *Directional Occlusion* como máscara).
   - *Por quê:* é o *Worldspace Intensity*. No lado da luz, frestas aparecem menos, e isso reforça a direção.

## Parte C — Pós-processo e saída

1. **Highlight HSL.** Selecione as áreas mais claras (camadas 7 a 9) e aplique um ajuste de matiz/saturação: matiz +5 a +10° para o amarelo, saturação +10 a +15%. Faça no menu de ajustes de camada do 3DCoat ou exporte para o Krita.
   - *Por quê:* é o *Highlight HSL* do original (*Highlight Clip* isola a faixa clara, *Hue/Saturation* deslocam a cor). Luz quente e saturada lê como sol.
2. **Cel shading (opcional).** Para um visual toon, faça o corte luz/sombra no shader do Unity: um *Shader Graph* com *Step* ou *Smoothstep* sobre a luminância, com dois parâmetros equivalentes a *Cel Bias* (ponto de corte) e *Cel Softness* (suavidade).
   - *Por quê:* posterizar a textura pintada cria serrilhado. No shader, o corte fica limpo e ajustável em tempo real.
3. **Escolha a saída.** O original tem *Override Use Baked Lighting*: ligado, tudo vai para um diffuse único; desligado, sai Diffuse + Specular + Gloss separados.

| Saída | Camadas exportadas | Shader no Unity | Quando usar |
| --- | --- | --- | --- |
| Baked (diffuse único) | 1 a 10 + HSL | URP/Unlit | Cena com luz fixa, estilo hand-painted puro |
| Separada | Diffuse: 1 a 6 · Specular: 8 e 9 numa textura à parte | URP/Simple Lit ou Shader Graph | Luz dinâmica (tochas, dia e noite) |

- *Por quê:* separar a luz pintada da cor permite que o motor reaja à iluminação sem perder o estilo.

## Versão PBR — clones do SoMuchRoughness e do SoMuchSpecular

O pacote SoMuchMaterials tem dois irmãos do SoMuchDiffuse com os mesmos controles de forma e luz. A diferença é o destino do brilho: em vez de pintado no diffuse, ele vai para canais que o motor lê.

| Gerador | Saídas | Controles exclusivos (documentação) | O que isso revela |
| --- | --- | --- | --- |
| SMM\_SoMuchDiffuse | Diffuse | *Override Use Baked Lighting* | Toda a luz vai para a cor |
| SMM\_SoMuchRoughness | Diffuse, Metal, Roughness | *Is Metal*, *Use Roughness Slider* | O brilho especular vira roughness; o metal é binário |
| SMM\_SoMuchSpecular | Diffuse, Specular, Gloss | *Override Gloss*, *Override Use Baked Spec* | O brilho vira cor especular + gloss; a faixa de gloss é padronizada |

Três regras saem da documentação e valem para os dois clones PBR:

- **Metal é binário.** *Is Metal* põe metalness em branco (1) ou preto (0), sem meio-termo. Quando é metal, parte da *Specular Color* é misturada no diffuse, porque a cor do metal vem do seu reflexo (ouro amarelo, cobre laranja).
- **A rugosidade tem uma base única.** *Use Roughness Slider* troca os valores de preset por um controle de intensidade base. Os outros controles (borda, cavidade, AO) modulam a partir dela.
- **A faixa de gloss é igual para o kit inteiro.** *Override Gloss* existe para ajustar a faixa ao motor, e a documentação pede que ela seja a mesma em todos os materiais, para o brilho ficar consistente.

### Clone 3R — Metal/Roughness (SoMuchRoughness)

Duplique `CLONE_SoMuchDiffuse` como `CLONE_SoMuchRoughness`. Mantenha as camadas 1 a 6 (Parte A) e trate as de luz assim:

| # | Camada | Color | Glossiness | Metalness |
| --- | --- | --- | --- | --- |
| 1 | `01 Diffuse Color` | Igual | Base do kit (ex.: 0.30) | 0 ou 1 (*Is Metal*) |
| 2 | `02 Shadow Color` | Opacidade cai para 20 a 30% | — | — |
| 3 | `03 Cavity` | Igual | 0.10 (mais áspero) | 0 |
| 4 | `04 Soft Cavity` | Igual | — | — |
| 5 | `05 Occlusion Color` | Opacidade cai para 15 a 20% | 0.20 | — |
| 6 | `06 Thickness` | Igual | — | — |
| 7 | `07 Top Down` | Opcional, no máximo 15% | — | — |
| 8 | `08 Specular` | **Desligada** | — | — |
| 9 | `09 Specular Edge` | Clara, 30% | **0.70** (borda polida) | — |
| 10 | `10 Underlight` | Opcional, 10% | — | — |

"—" significa que a camada não mexe naquele canal. No *Smart Material Editor*, deixe o canal sem valor ou com opacidade zero. Se a sua versão não permitir, repita o valor da camada de baixo.

1. **Desligue o especular pintado (8).**
   - *Por quê:* agora quem desenha o brilho é a luz da cena. Brilho pintado mais brilho real dá um reflexo duplo que não se move com a câmera.
2. **Transforme a borda especular (9) em gloss.**
   - *Por quê:* é o *Edge Exponent* do original. Bordas gastas ficam polidas e pegam reflexo; no PBR, isso é gloss alto, não cor clara.
3. **Cavidade e AO baixam o gloss.**
   - *Por quê:* é o *Cavity Intensity* e o *AO Intensity* do grupo Specular. Sujeira acumulada é fosca, e isso impede reflexo dentro das frestas.
4. **Para metal: Metalness 1 e cor de reflexo na base.** Base com a cor do metal mais clara e saturada (ouro #E6B85C, cobre #D08A5A, ferro #9AA0A6). Cavidade com Metalness 0, como sujeira.
   - *Por quê:* é o *Is Metal* do original. Com metalness 1, a cor do diffuse vira a cor do reflexo; se ela for escura, o metal fica preto no Unity.
5. **Reduza a luz assada (2, 5, 7, 10).**
   - *Por quê:* o motor já vai sombrear. Manter um pouco preserva o estilo; manter tudo deixa a peça escura demais.

### Clone 3S — Specular/Gloss (SoMuchSpecular)

Mesma pilha do 3R, mas o brilho vai para uma cor especular em vez de metalness. Esse fluxo dá mais controle artístico: dá para tingir o reflexo de qualquer material.

| Canal | Não-metal (pedra, madeira, tecido) | Metal |
| --- | --- | --- |
| Diffuse | Cor normal | Escuro (quase preto), a cor sai do especular |
| Specular | Cinza escuro neutro, por volta de #3B3B3B | Cor do metal (ouro #E6B85C) |
| Gloss | Faixa do kit (ex.: 0.15 a 0.40) | Faixa do kit (ex.: 0.40 a 0.80) |

1. **Defina a faixa de gloss do kit antes de tudo.** Ex.: mínimo 0.10, máximo 0.80, para todos os materiais do grupo.
   - *Por quê:* é o *Override Gloss*. Se cada material usar uma faixa, peças vizinhas brilham de jeitos diferentes sob a mesma luz.
2. **Cavidade e AO escurecem o especular.**
   - *Por quê:* é o *Cavity/AO Intensity* do grupo Specular: frestas não refletem.
3. **Borda clareia o especular e sobe o gloss.**
   - *Por quê:* é o *Edge Color* e o *Edge Exponent*: o reflexo se concentra nas quinas.
4. **(Estilo extremo) Multiplique o especular pela luz de topo assada.**
   - *Por quê:* é o *Override Use Baked Spec*: um "mask de luz pesado" no especular. As partes de cima brilham mais mesmo sob luz neutra. Use só se o tema pedir um visual bem estilizado.

### No Unity (URP)

| Clone | Shader | Mapas |
| --- | --- | --- |
| 3R | URP/Lit, *Workflow Mode: Metallic* | Base Map, Metallic Map (smoothness no alfa), Normal Map |
| 3S | URP/Lit, *Workflow Mode: Specular* | Base Map, Specular Map (smoothness no alfa), Normal Map |

- O Glossiness do 3DCoat equivale ao Smoothness do Unity (roughness invertido). Ao exportar, empacote o gloss no **alfa** do mapa de Metallic ou Specular, que é onde o URP lê o smoothness.
- Exporte o normal no formato **OpenGL (Y+)**, que é o do Unity. É o mesmo ajuste do controle *Normal Format* do original.
- *Por quê do URP/Lit aqui:* agora os canais existem para a luz real reagir a eles. O shader Unlit ignoraria roughness, metal e normal.

## Teste e checklist

**Teste de comparação:** aplique os três clones no mesmo módulo. O Clone 3 deve mostrar luz com direção clara, brilho só no lado iluminado e a parte de baixo separada do chão.

- [ ] O rig de luz está salvo e é o mesmo em todos os módulos.
- [ ] A sombra usa uma cor escolhida em Multiply, e o AO tem cor própria.
- [ ] Existem duas cavidades (nítida e suave) com funções diferentes.
- [ ] O brilho especular aparece só nas bordas e faces iluminadas.
- [ ] Não há brilho nas faces voltadas para baixo.
- [ ] O underlight separa a peça do piso no Unity.
- [ ] As frestas são mais fracas no lado iluminado.
- [ ] A saída escolhida (baked ou separada) combina com o shader usado.

**Limite do clone:** o original recalcula a luz ao mexer num slider. No 3DCoat, mudar a luz exige assar de novo as camadas 7 a 10. Por isso o rig deve ser decidido cedo, junto com o tema do kit.

**Fontes:** [SoMuchMaterials — produto](https://www.somuchmonsters.com/somuchdiffuse) · [SoMuchMaterials — documentação](https://www.somuchmonsters.com/somuchmaterials-documentation) · [3DCoat — Light Baking](https://3dcoat.com/documentation/?p=10277) · [3DCoat — Cavity and Curvature](https://3dcoat.com/documentation/?p=10661)
