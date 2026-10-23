# Tutorial — Smart Material estilizado "Diffuse" no 3DCoatTextura

20/10/2026 · Rodrigo

> **3DCoatTextura 2026.** Na versão 2026.11, os Smart Materials padrão da biblioteca foram convertidos para o sistema de nós (*NGMaterials*). Este tutorial monta o material no **Smart Material Editor** (camadas com *Condition Mask*), o fluxo clássico. Antes da aula, confira na versão do laboratório se o botão **+** do painel *Materials* ainda cria um Smart Material desse tipo. Se não criar, monte cada camada em nós: um *SimpleMaterial* com a cor da camada e um *SimpleMask* com o *condition type* equivalente (*More on Convex* → convex, *More on Concave* → concave, *More in Shadow* → in shadow).

## Visão geral

Neste tutorial você monta um Smart Material estilizado no 3DCoatTextura. Ele gera uma textura *hand-painted* só de diffuse, com a luz pintada na cor, pronta para um shader Unlit no Unity. A receita junta as ideias de três produtos do Substance Painter, reconstruídas com recursos nativos do 3DCoatTextura:

| Referência | O que emprestamos | Onde aparece |
| --- | --- | --- |
| [SimpleDiffuse](https://nhanceschool.gumroad.com/l/SimpleDiffuse) | Máscaras básicas (cavidade, AO, borda) sobre a cor | Etapa 3 |
| [Stylized FT](https://flippednormals.com/product/stylized-ft-smart-material-for-substance-painter-54727) | Padrão procedural + mistura de tons quentes e frios | Etapas 2 e 5 |
| [SoMuchDiffuse](https://www.somuchmonsters.com/somuchdiffuse) | Cor de sombra, luz de topo, underlight, thickness, HSL nos highlights | Etapas 2, 4 e 5 |

**A lógica em uma frase:** o material resolve *onde* cada tom aparece (máscaras de forma) e a iluminação pintada resolve *de onde* vem a luz (camadas de luz). Por isso o tutorial separa as duas coisas. O Smart Material guarda o que é reaproveitável, e a luz é assada por peça.

**Pré-requisitos**

- Ter feito o [Tutorial 0 — Primeiros passos no 3DCoatTextura](/Tutoriais/Tutorial_0_Primeiros_Passos_3DCoatTextura.md) (interface, camadas, Attach + Fill, exportação).
- Um módulo do kit (parede, piso, pilar) com UVs sem sobreposição. A sobreposição quebra AO e curvatura.
- Mapa de normal assado do high poly no Blender (opcional; o 3DCoatTextura não faz bake de high para low).
- 3DCoatTextura 2026, a versão adotada na disciplina. Os nomes das opções podem variar um pouco entre atualizações.
- Referência visual do tema escolhido pelo grupo, com ao menos 3 imagens de materiais estilizados.

**Resultado esperado:** um arquivo `.3dcpack` com o Smart Material do grupo e um módulo texturizado, exibido no Unity com shader Unlit.

## Etapa 1 — Preparação: os mapas que alimentam as máscaras

Nada no material funciona sem AO e curvatura calculados. Todas as máscaras das próximas etapas leem esses mapas.

1. **Importe o low poly com o normal map.** Em *File → Import*, carregue o módulo para o sala *Painting* (pintura Per-Pixel) e aplique o normal map numa camada.
   - *Por quê:* a curvatura do 3DCoatTextura é calculada a partir do normal map visível. Sem ele, o low poly não tem detalhe para gerar bordas e frestas.
2. **Isole o normal map.** Alt+clique no olho da camada do normal, para que só ela fique visível.
   - *Por quê:* outras camadas visíveis contaminam o cálculo.
3. **Calcule oclusão e curvatura.** Em *Edit → Calculate Occlusion and Curvature maps*, com a opção *Local Curvature RGB for Cavity map*.
   - Para frestas nítidas (estilo cavity), use intensidade alta (ex.: curvature 400, long-range 10). Para formas grandes e suaves, use intensidade baixa (ex.: curvature 8, long-range 100). Valores de exemplo do [manual](https://3dcoat.com/documentation/?p=10661).
   - *Por quê:* o estilo hand-painted precisa das duas escalas. A local dá o highlight fino da borda e a long-range dá o volume.
4. **Confira o Cavity RGB.** Em *Edit → Preferences → Tools*, verifique se a opção *RGB Cavity "Curvature"* está ativa (no 3DCoatTextura 2026 ela já vem ativa por padrão).
   - *Por quê:* ele libera o controle *Cavity Area Width* no editor, que usaremos para ajustar a largura das frestas.
5. **Asse o Thickness (opcional).** Na *Light Baking Tool* (menu *Edit*), escolha *Map Type: Thickness* e grave numa camada separada, escondida.
   - *Por quê:* é o equivalente ao Thickness do SoMuchDiffuse. Marca as partes finas do objeto (bordas de placas, folhas, tecido), onde a luz "atravessa" e o tom fica mais claro e saturado.

**Evidência:** antes de seguir, mostre ao colega ao lado os mapas de AO e curvatura. Escuro nas frestas e claro nas quinas vivas significa que deu certo.

## Etapa 2 — Cor base e cor de sombra

O salto de qualidade do estilo está aqui: a sombra é uma *cor diferente*, não a base escurecida. É o controle *Shadow Color* do SoMuchDiffuse e o *shade blending* do FT.

1. **Crie o material.** No painel *Materials*, clique no **+**, dê um nome no padrão `GRUPO_Material_Tema` (ex.: `G3_Pedra_Medieval`) e abra o *Smart Material Editor*.
2. **Camada 1 — Base.** Em *Color*, defina a cor média do material, com *Condition Mask* em *Always*. Deixe *Glossiness* e *Metalness* em zero.
   - *Por quê:* no fluxo diffuse-only, brilho e metal serão pintados na cor. Valores PBR só confundem a leitura no viewport.
   - Escolha um valor **médio**, nem muito claro nem muito escuro. Ele precisa de espaço para receber sombras e luzes por cima.
3. **Camada 2 — Cor de sombra.** Nova camada com uma cor mais escura, **mais saturada** e com o **matiz deslocado para o frio** (azul, roxo). Use *Condition Mask* *More in Shadow* (exige o AO calculado) com opacidade entre 40 e 60%.
   - *Por quê:* na pintura tradicional, a sombra recebe a luz fria do céu e ganha saturação. Escurecer para o preto deixa o material "sujo" e sem vida.

| Material | Base (exemplo) | Sombra (exemplo) | Desvio de matiz |
| --- | --- | --- | --- |
| Pedra | cinza-bege #9C9282 | azul-ardósia #4E5670 | para o azul |
| Madeira | marrom médio #8A5A3C | vinho #4A2630 | para o vermelho/roxo |
| Metal | cinza-azul #7F8A94 | azul-petróleo #2E3E52 | para o azul |
| Musgo | verde #6E8A3A | verde-azulado #2C4A40 | para o ciano |

**Critério da crítica:** com só essas duas camadas, o objeto já deve ler volume. Se parecer chapado, aumente o contraste de valor entre base e sombra antes de seguir.

## Etapa 3 — Máscaras de forma: cavidade, AO e bordas

Essas três camadas descrevem a *forma* do objeto, independente de onde a luz vem. Por isso ficam dentro do Smart Material e funcionam em qualquer módulo do kit.

1. **Camada 3 — Cavidade.** Uma cor mais escura e fria que a sombra, com *Condition Mask* *More on Concave*. Ajuste *Cavity Width*, *Cavity Degree* e *Contrast*, e use *Cavity Area Width* (Cavity RGB) para controlar a largura.
   - *Por quê:* é o "traço" que o pintor faz nas frestas para separar as formas. Deve ser **fino e nítido**. Se ficar largo, vira sujeira.
   - Equivalente a *Cavity Clipping/Contrast* do SoMuchDiffuse.
2. **Camada 4 — AO.** Cor de sombra em baixa opacidade (20 a 35%), *Condition Mask* *More in Shadow*.
   - *Por quê:* a cavidade marca a fresta e o AO marca a área *ao redor* dela, onde a luz chega menos. Juntas, dão profundidade em duas escalas.
3. **Camada 5 — Highlight de borda.** Uma cor mais clara e **quente** (amarelada) que a base, com *Condition Mask* *More on Convex* e contraste alto.
   - *Por quê:* imita o desgaste e o brilho nas quinas, a assinatura do hand-painted. A cor quente faz o contraponto à sombra fria da Etapa 2.
   - Use a *Edge Scattering* (uma imagem de ruído) para quebrar a linha da borda e ela não parecer gerada por computador.
4. **Crie controles legíveis.** Renomeie cada camada com a função e o parâmetro principal: `03 Cavidade – largura`, `05 Borda – intensidade`.
   - *Por quê:* quem usar o material depois (o próprio grupo ou outro) precisa saber o que mexer sem abrir camada por camada. É o que os produtos comerciais vendem: controles nomeados.

**Teste rápido:** aplique o material em uma esfera e em um cubo chanfrado. As bordas devem acender no cubo e quase sumir na esfera. Se acenderem na esfera, a curvatura está sensível demais.

## Etapa 4 — Luz pintada: topo, underlight e highlight direcional

A luz depende da posição da peça no mundo. Por isso ela não entra no Smart Material: é assada **por módulo**, em camadas acima do material, com a *Light Baking Tool* (menu *Edit*). É o equivalente ao rig de luzes do SoMuchDiffuse.

1. **Monte a luz na sala Render.** Uma luz principal vinda de cima, levemente de lado (ângulo de 30 a 45°), e uma secundária fraca vinda de baixo. Mantenha a mesma orientação para **todos os módulos do kit**.
   - *Por quê:* se cada módulo tiver luz pintada numa direção, o kit montado no Unity não encaixa visualmente. A consistência da luz é o que une o kit.
2. **Camada 6 — Luz de topo.** Na *Light Baking Tool*, escolha *Map Type: Light From Render Room* e grave numa camada nova, em modo *Screen* ou *Overlay*, com uma cor quente.
   - *Por quê:* o topo das peças recebe a luz do sol ou do céu. É o *top gradient* do FT e a *Gradient Type: lit* do SoMuchDiffuse.
   - Alternativa mais leve: uma camada pintada com a ferramenta *Fill* em degradê vertical.
3. **Camada 7 — Underlight.** Uma camada em *Screen*, em baixa opacidade (15 a 25%), com a luz secundária de baixo e uma cor de rebatimento (o tom do chão: terra, grama, pedra).
   - *Por quê:* sem ela, a parte de baixo vira uma massa escura que se funde com o chão. A luz rebatida separa a peça do piso.
4. **Camada 8 — Brilho especular pintado.** Duplique a camada de borda (Etapa 3) e multiplique-a pela máscara da luz de topo, para o brilho aparecer **só nas bordas iluminadas**. Use *Add* ou *Screen*, com uma cor quase branca e quente.
   - *Por quê:* é o *Specular Edge* do SoMuchDiffuse. Brilho em todas as bordas parece plástico. Só nas bordas que recebem luz, parece material.
5. **Thickness (opcional).** Use a camada da Etapa 1 como máscara de uma cor mais clara e saturada, em baixa opacidade.
   - *Por quê:* simula a luz atravessando partes finas (folhas, tecido, cristais). Em pedra e metal, pule esta camada.

**Regra de ouro:** a luz pintada **nunca** pode ser mais escura que a sombra nem mais clara que o highlight. Pinte nesta ordem de valor: cavidade < AO < sombra < base < luz de topo < highlight especular.

## Etapa 5 — Padrão, variação e ajuste final de cor

Até aqui o material tem volume, mas ainda parece "uma cor só". Esta etapa dá identidade de material e acabamento de pintura.

1. **Camada de padrão (no Smart Material).** Logo acima da base, adicione uma textura tileável em tons de cinza no canal *Color*, como máscara de uma cor um pouco mais clara ou mais escura. Use *Preferred Mapping: Cube* e opacidade de 15 a 30%. Exemplos: veios de madeira, blocos de pedra, placas de metal.
   - *Por quê:* é o *pattern generation* do FT. O padrão diz ao olho "isso é madeira" antes de qualquer detalhe.
   - Pinte o padrão no Krita, com pinceladas visíveis. Um padrão fotográfico quebra o estilo.
   - Use o canal *Depth* do mesmo padrão com valor baixo, para que cavidade e borda também reajam a ele.
2. **Camada de variação.** Um ruído grande (manchas do tamanho de 1/4 do objeto), com deslocamento de matiz de 5 a 10° e opacidade de 10 a 20%.
   - *Por quê:* superfícies reais nunca têm matiz uniforme. A variação grande evita o aspecto de "plástico pintado".
3. **Ajuste HSL nos highlights.** Depois da luz assada, aplique um ajuste de matiz/saturação (menu de ajustes de camada do 3DCoatTextura, ou exporte para o Krita) só nas áreas claras: um pouco mais de saturação e matiz para o amarelo.
   - *Por quê:* é o *Highlight HSL* do SoMuchDiffuse. Luzes quentes e sombras frias criam contraste de temperatura, que lê como luz solar.
4. **Cel shading (opcional).** Se o tema pedir um visual toon, deixe o corte entre luz e sombra mais duro aumentando o contraste das máscaras, ou faça o corte no shader do Unity.
   - *Por quê:* posterizar uma textura pintada costuma criar serrilhados. O shader faz o corte de forma limpa e ajustável.

## Etapa 6 — Salvar, compartilhar e levar para o Unity

1. **Salve o Smart Material com as camadas 1 a 5 e o padrão.** As camadas de luz (6 a 8) ficam fora, no projeto de cada módulo.
   - *Por quê:* o material é reaproveitável em qualquer peça. A luz é específica de cada peça.
2. **Crie as variações do tema.** Use *Duplicate* no material e troque apenas as cores de base, sombra e borda (ex.: pedra clara, pedra musgosa).
   - *Por quê:* se a estrutura de camadas for a mesma, todo o kit mantém a mesma linguagem visual.
3. **Compartilhe a pasta.** Botão direito na pasta do grupo → *Share item folder*. Isso gera o `.3dcpack` para os colegas e para a entrega.
4. **Exporte a textura.** Em *File → Export → Objects & Textures*, exporte o mesh com o mapa de cor (diffuse). Para este fluxo, não é preciso exportar roughness nem metal.
5. **No Unity, use um shader Unlit.** Em URP, crie o material com *Universal Render Pipeline/Unlit* e coloque a textura em *Base Map*.
   - *Por quê:* a luz já está pintada. Um shader Lit soma a luz da cena com a pintada e o resultado fica "duplamente iluminado", com sombras que contradizem a pintura.
   - Se o jogo precisar de luz dinâmica (dia e noite, tochas), faça uma segunda versão **sem** as camadas 6 a 8 e use *Simple Lit*.
6. **Teste o encaixe.** Monte 4 a 6 módulos lado a lado na cena e verifique se a luz de topo, as cores e a largura das bordas são iguais entre as peças.

## Etapa 7 — Versão PBR (luz dinâmica)

Se o kit tiver luz dinâmica (tochas, ciclo dia e noite), faça uma versão PBR do material. A lógica vem dos irmãos do SoMuchDiffuse, o SMM\_SoMuchRoughness (Diffuse/Metal/Roughness) e o SMM\_SoMuchSpecular (Diffuse/Specular/Gloss): as máscaras de forma são as mesmas, mas o brilho sai da cor e vai para canais que o motor lê.

| Camada do material | Versão diffuse-only | Versão PBR |
| --- | --- | --- |
| Base | Cor média | Cor média + gloss base do kit + metalness 0 ou 1 |
| Sombra e AO | 40 a 60% na cor | Metade da opacidade (o motor sombreia) |
| Cavidade | Escura na cor | Escura na cor + gloss baixo + metalness 0 |
| Borda | Clara e quente na cor | Mais fraca na cor + gloss alto |
| Padrão | Tom na cor | Tom na cor + juntas foscas no gloss |
| Luz de topo, underlight | Assadas na cor | Desligadas ou no máximo 15% |
| Brilho especular pintado | Assado na cor | **Desligado**: o motor desenha o reflexo |

1. **Defina uma faixa de gloss para o kit inteiro** (ex.: 0.10 a 0.80).
   - *Por quê:* é o *Override Gloss* do SoMuchSpecular, que pede a mesma faixa em todos os materiais para o brilho ser consistente entre peças vizinhas.
2. **Metal é binário: 0 ou 1.**
   - *Por quê:* é o *Is Metal* do SoMuchRoughness. Com metalness 1, a cor da base vira a cor do reflexo, então ela precisa ser clara e saturada.
3. **Brilho é gloss, não cor.** Bordas sobem o gloss, cavidade e AO baixam.
   - *Por quê:* com luz real, o reflexo se move com a câmera. Brilho pintado ficaria parado e duplicado.
4. **No Unity:** *URP/Lit*, *Workflow Mode: Metallic* (ou *Specular* para o fluxo do SoMuchSpecular). Gloss no alfa do Metallic/Specular Map (= Smoothness) e normal map em OpenGL (Y+).

Os valores por camada estão em cada clone: [Clone 1](/Tutoriais/Clone_1_SimpleDiffuse.md), [Clone 2](/Tutoriais/Clone_2_Stylized_FT.md) e [Clone 3](/Tutoriais/Clone_3_SoMuchDiffuse.md), este com as variantes Metal/Roughness e Specular/Gloss.

## Problemas comuns e checklist

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| Máscaras de cavidade e borda não aparecem | AO e curvatura não calculados, ou normal map oculto | Refazer a Etapa 1 com só o normal visível |
| Manchas pretas em áreas espelhadas | UVs sobrepostas | Separar as UVs, ou usar *Light Based Curvature* |
| Material parece sujo | Sombra e cavidade puxando para o preto | Trocar por cores frias e saturadas (Etapa 2) |
| Bordas acendem em tudo | Curvatura sensível demais | Baixar a intensidade local e subir o contraste |
| Peça parece plástica | Brilho especular em todas as bordas | Limitar o brilho às bordas iluminadas (Etapa 4) |
| Kit não "encaixa" no Unity | Luz assada em direções diferentes | Usar o mesmo rig de luz em todos os módulos |
| Tudo fica claro demais no Unity | Shader Lit somando luz | Usar Unlit (Etapa 6) |

**Checklist de autoavaliação (antes da crítica coletiva)**

- [ ] Com só base + sombra, o objeto já lê volume.
- [ ] A sombra tem matiz diferente da base (não é só mais escura).
- [ ] A cavidade é fina e nítida; o AO é largo e suave.
- [ ] O highlight de borda é quente e quebrado (não é uma linha perfeita).
- [ ] A luz vem da mesma direção em todos os módulos.
- [ ] A ordem de valores (cavidade < AO < sombra < base < luz < highlight) foi respeitada.
- [ ] O padrão identifica o material a 3 metros da tela.
- [ ] As camadas estão nomeadas com função e parâmetro.
- [ ] O `.3dcpack` abre no computador de um colega.

**Para a crítica:** cada grupo apresenta o módulo com as camadas ligadas uma a uma, da 1 à 8, e justifica uma escolha de cor e uma escolha técnica.

## Fontes

- [3DCoat — Cavity and Curvature maps](https://3dcoat.com/documentation/?p=10661)
- [3DCoat — Smart Materials](https://3dcoat.com/documentation/manual/brush-components/smart-materials/)
- [3DCoat — Smart Material Editor e Conditions](https://3dcoat.com/documentation/?p=2212)
- [3DCoat — Light Baking Tool (tipos de mapa)](https://3dcoat.com/documentation/?p=10277)
- [SoMuchMaterials — documentação](https://www.somuchmonsters.com/somuchmaterials-documentation)
- [FT Diffuse — ArtStation Marketplace](https://www.artstation.com/marketplace/p/j8mRg/stylized-texture-generator-for-substance-painter-ft-diffuse)
