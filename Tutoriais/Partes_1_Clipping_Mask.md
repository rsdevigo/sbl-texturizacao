# Materiais por parte da malha — Modo 1: Clipping Mask

22/10/2026 · Rodrigo

> **Modo recomendado.** É o mais parecido com "pasta com máscara" do Substance Painter e o único em que a máscara continua editável depois que os materiais já foram aplicados.
> Os nomes de menus do 3DCoat mudam entre versões. Se alguma opção não estiver no lugar indicado, confira na versão 2026 do laboratório e anote a diferença para a turma.

## Visão geral

No Substance, você cria uma pasta, põe uma máscara preta nela, pinta de branco a parte do modelo (os aros de um barril, por exemplo) e tudo que estiver dentro da pasta só aparece ali.

No 3DCoat, a mesma ideia é feita com **Clipping Mask**:

- uma camada **de máscara** existe só na parte desejada (os aros);
- as camadas de material ficam **presas** (*clipped*) a ela e só aparecem onde a máscara tem tinta.

> **A regra que faz tudo funcionar:** no 3DCoat, a máscara é a **transparência** da camada. Onde a camada de máscara foi pintada ou preenchida, o material aparece. Onde ela é transparente, o material some. Não existe máscara em tons de cinza separada como no Photoshop: a própria camada é a máscara.

**Por que este é o modo preferido**

- **A máscara fica viva.** Se você apagar ou pintar a camada de máscara depois, todos os materiais presos a ela acompanham. Não é preciso refazer o Fill dos Smart Materials.
- **A pilha fica organizada por parte**, como no Substance: uma pasta "Aros – Metal", outra "Tábuas – Madeira".
- **O toque autoral fica protegido.** Pinceladas de desgaste também podem ser presas à máscara e nunca vazam para a parte vizinha.

**Exemplo usado no tutorial:** o barril da Semana 2, com tábuas de madeira e aros de metal. Troque pelo seu Hero Asset ou módulo do kit.

**Resultado esperado:** um modelo com uma pasta por parte, cada pasta com uma camada de máscara e as camadas de material presas a ela, exportado para a Unity.

## Etapa 1 — Separar as partes no Blender

Para preencher a máscara com um clique, o 3DCoat precisa saber onde começa e termina cada parte. Isso se decide no Blender.

1. **Atribua um material por parte.** No barril: `Tabuas` e `Aros`. Use *Material Properties → +* e, no modo de edição, selecione as faces de cada parte e clique em *Assign*.
   - *Por quê:* no 3DCoat, cada material do Blender chega como uma parte separada (*Surface Material*), que pode ser preenchida ou congelada inteira com um clique.
   - Os materiais aqui servem só para **separar áreas**. As cores e texturas deles não importam.
2. **Ou separe em objetos.** Se as partes já são peças soltas (um prego, uma alça), pode deixá-las como objetos diferentes no mesmo FBX.
   - *Por quê:* objetos separados chegam como *Paint Objects*, que também podem ser preenchidos ou congelados inteiros.
3. **Confira o UV e exporte.** UV sem sobreposição, transformações aplicadas, exportação em FBX.
   - *Por quê:* se cada material tiver um UV separado, o 3DCoat pode criar um conjunto de texturas por material. Para o kit modular, prefira **um único UV** (atlas) com vários materiais apontando para ele.

**Evidência:** no Blender, cada parte com uma cor de material diferente no *Viewport Shading → Material*.

## Etapa 2 — Organizar a pilha em pastas

1. **Crie uma pasta por parte.** No painel Layers, use o botão *Create folder group* (ícone de pasta, na barra inferior do painel). Nomeie: `Tábuas – Madeira`, `Aros – Metal`.
   - *Por quê:* é a mesma organização do Substance. Na crítica, desligar uma pasta mostra na hora o que pertence a cada parte.
2. **Dentro de cada pasta, crie a camada de máscara.** Nomeie com o prefixo `M`: `M Aros`, `M Tábuas`. Ela fica **na base da pasta**.
   - *Por quê:* a máscara precisa ficar abaixo das camadas que ela recorta. O prefixo evita confundir máscara com material.

A pilha fica assim (de cima para baixo, como aparece no painel):

```
📁 Aros – Metal
    Aros – desgaste (pincel)      → presa a M Aros
    Aros – Smart Material metal   → presa a M Aros
    M Aros                        ← máscara
📁 Tábuas – Madeira
    Tábuas – sujeira (pincel)     → presa a M Tábuas
    Tábuas – Smart Material madeira → presa a M Tábuas
    M Tábuas                      ← máscara
```

## Etapa 3 — Preencher a camada de máscara só na parte

Escolha **uma** das formas abaixo. Todas produzem o mesmo resultado: a camada `M Aros` com tinta só nos aros.

**A. Fill por parte (o mais rápido, se a Etapa 1 foi feita)**

1. Selecione a camada `M Aros` e escolha uma cor qualquer (cinza médio, por exemplo).
2. Pegue a ferramenta **Fill** e, nas opções, troque o escopo de *Layer* para **Surface Material** (se as partes são materiais) ou **Object** (se são objetos).
3. Clique sobre os aros.
   - *Por quê:* com esse escopo, o Fill pinta exatamente a área daquele material ou objeto e para na fronteira. É o "pintar a máscara de branco" do Substance, em um clique.

**B. Fill por ângulo (sem preparação no Blender, para hard surface)**

1. Na ferramenta **Fill**, ligue **Use max. angle** e ajuste o ângulo.
2. Clique sobre uma face dos aros.
   - *Por quê:* o Fill se espalha pelas faces vizinhas até encontrar uma quina mais fechada que o ângulo definido. Em peças com quinas bem marcadas, isso isola a parte sem material nem ID.

**C. Pincel (para partes orgânicas ou sem fronteira de malha)**

1. Pinte a camada `M Aros` com um pincel duro, na área desejada.
   - *Por quê:* às vezes a parte não coincide com a malha (uma mancha de musgo, uma faixa de tinta). A máscara pintada à mão funciona igual às outras.

> A cor da camada de máscara não importa para os materiais, só a transparência. Se quiser, use a cor base da parte: assim a máscara já serve de "fundo" e nunca aparece um buraco se um material tiver transparência.

**Evidência:** com só as camadas de máscara visíveis, cada parte aparece com tinta e o resto do modelo fica vazio.

## Etapa 4 — Aplicar o material e prendê-lo à máscara

1. **Crie a camada do material** acima de `M Aros`, dentro da pasta. Nomeie `Aros – Smart Material metal`.
2. **Prenda (Attach) o Smart Material.** Clique com o botão direito no material na biblioteca → *Attach to the current layer*.
3. **Preencha a camada inteira.** Botão direito na camada → *Fill entire layer* (ou o Fill com escopo *Layer*).
   - *Por quê:* o material é preenchido no objeto todo. Quem decide onde ele aparece é a máscara, não o Fill. Isso é o que permite mudar a máscara depois sem refazer o material.
4. **Prenda a camada à máscara.** Com a camada do material selecionada, abra o painel de **Blending** da camada e, em **Clip Mask Layer**, escolha `M Aros` na lista.
   - *Por quê:* a partir daqui, a camada só aparece onde `M Aros` tem tinta. Os aros ficam metálicos e as tábuas não são afetadas.
   - Atalho: botão direito numa camada → **Clipping Mask** cria uma camada de máscara nova logo abaixo dela, já ligada.
5. **Repita para cada camada da pasta.** Toda camada nova (outro material, sujeira, desgaste à mão) recebe o mesmo **Clip Mask Layer** = `M Aros`.
   - *Por quê:* várias camadas podem usar a mesma máscara. É o equivalente a "tudo que está dentro da pasta respeita a máscara da pasta".

> **Por que não basta colocar a camada dentro da pasta?** No 3DCoat, a pasta organiza e permite mudar opacidade e modo de mistura do grupo, mas não recorta sozinha. O recorte vem do *Clip Mask Layer* de cada camada.

**Evidência:** gire o modelo e confira que o metal aparece só nos aros. Depois, dê uma pincelada de teste na camada `M Aros` sobre uma tábua: o metal deve aparecer ali também. Desfaça a pincelada (`Ctrl+Z`) e siga.

## Etapa 5 — Editar a máscara depois

É aqui que o modo mostra a vantagem.

1. **Aumente ou corrija a área.** Selecione `M Aros` e pinte com o pincel numa área nova (a ponta de um prego, por exemplo). O metal aparece ali na hora.
2. **Remova área.** Use a borracha na camada `M Aros`. O metal some daquela região.
3. **Inverta, se precisar.** No painel de Blending de uma camada de material, **Invert Clip Mask** faz a camada aparecer **fora** da máscara.
   - *Por quê:* é útil para "tudo menos os aros" sem criar outra máscara.
   - Para conferir a área de uma máscara, `Ctrl+clique` na camada mostra as regiões transparentes como congeladas. Para limpar a visualização: `Ctrl+D` e depois *Freeze → Unfreeze All*.

**Evidência:** dois prints do mesmo ângulo, antes e depois de editar a máscara, com os materiais acompanhando sem nenhum Fill novo.

## Etapa 6 — Toque autoral com pincel

1. **Crie uma camada de pincel** dentro da pasta (`Aros – desgaste (pincel)`) e prenda-a a `M Aros`.
2. **Pinte o desgaste, a sujeira ou os riscos** com alphas e stencils.
   - *Por quê:* como a camada está presa à máscara, a pincelada nunca vaza para as tábuas, mesmo passando o pincel por cima da fronteira. Dá para pintar solto.

## Etapa 7 — Finalizar e exportar

1. **Exporte normalmente** com o preset da Unity.
   - *Por quê:* a exportação usa o resultado visível. O recorte já sai aplicado nos mapas.
2. **(Opcional) Torne o recorte definitivo.** Botão direito numa camada → **Discard Clip Masked Pixels** apaga da camada os pixels escondidos pela máscara.
   - *Por quê:* deixa o arquivo mais leve e evita surpresas se alguém desligar a máscara. Faça só no fim: depois disso, a máscara deixa de ser editável para aquela camada.

## Problemas comuns

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| O material aparece no modelo inteiro | Camada sem *Clip Mask Layer* definido | Abrir o painel de Blending da camada e escolher a máscara |
| O material não aparece em lugar nenhum | Máscara vazia, ou presa à camada errada | Conferir a máscara visível sozinha (Etapa 3) e o nome escolhido na lista |
| O material aparece fora da parte | *Invert Clip Mask* ligado sem querer | Desligar o *Invert Clip Mask* |
| O Fill por *Surface Material* pinta o modelo todo | As partes não chegaram separadas | Voltar à Etapa 1 e conferir os materiais no Blender |
| A borda da máscara ficou serrilhada | Fill por ângulo em malha de poucas faces, ou textura de baixa resolução | Aumentar a resolução de trabalho, ou suavizar a borda da máscara com pincel |
| Pincelada de desgaste vaza para a parte vizinha | Camada de pincel não está presa à máscara | Definir o *Clip Mask Layer* também na camada de pincel |

## Checklist de autoavaliação

- [ ] Cada parte tem uma pasta com nome de parte e material.
- [ ] Cada pasta tem uma camada `M` na base, com tinta só na parte.
- [ ] Todas as camadas da pasta estão presas à máscara da pasta.
- [ ] Editei a máscara e os materiais acompanharam sem refazer o Fill.
- [ ] As pinceladas à mão não vazam para as partes vizinhas.
- [ ] A exportação para a Unity mostra cada material só na sua parte.

## Para a crítica

Mostre a pilha desligando uma pasta por vez e responda: **por que a fronteira entre as partes está onde está?** (decisão de modelagem, de material ou de narrativa da peça).

## Fontes

- [3DCoat — Layer and Clipping Masks](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/layer-and-clipping-masks/)
- [3DCoat — Blending Panel (Clip Mask Layer, Invert Clip Mask)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/)
- [3DCoat — The Layers Panel](https://3dcoat.com/documentation/manual/interface-and-navigation/the-layers-panel)
- [3DCoat — Paint Tool Panel (Fill: Layer, Surface Material, Object, Use max. angle)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-room-tools/)
- [3DCoat — Attach a Smart Material to a layer](https://3dcoat.com/documentation/?p=6295)
