# Materiais por parte da malha — Modo 3: ID map (seleção por cor)

22/10/2026 · Rodrigo

> Os nomes de menus do 3DCoatTextura mudam entre versões. Se alguma opção não estiver no lugar indicado, confira na versão 2026 do laboratório e anote a diferença para a turma.

## Visão geral

Um **ID map** é uma textura de cores chapadas, uma cor por parte do modelo: tábuas em vermelho, aros em azul, pregos em amarelo. Ela não aparece no jogo. Serve só para dizer ao programa onde fica cada parte.

No Substance, você usa o ID map com o *Color Selection* na máscara da pasta. No 3DCoatTextura, o ID map vira uma **camada**, e a ferramenta **Select** escolhe uma cor dela e transforma essa área numa seleção (congelamento). A partir da seleção, você cria a máscara da parte ou aplica o material direto.

**Quando usar:** peças com **muitas partes** ou partes que não coincidem com materiais e objetos do Blender (uma faixa de tinta, um entalhe, uma área de couro dentro da mesma malha). É também o caminho natural quando o modelo vem com bake de high poly, que já pode gerar o ID map junto (Semanas 11–12).

**Exemplo usado no tutorial:** o barril da Semana 2, com tábuas, aros e pregos.

**Resultado esperado:** o ID map importado como camada e uma camada de máscara (ou de material) por parte, criada a partir das cores do ID.

## Etapa 1 — Criar o ID map no Blender

O 3DCoatTextura não gera ID map a partir de um high poly. O mapa precisa vir pronto.

1. **Pinte as partes com cores chapadas.** Crie um material por parte (`ID_Tabuas`, `ID_Aros`, `ID_Pregos`) com cores bem diferentes e saturadas (vermelho puro, azul puro, amarelo puro), ou pinte *Color Attributes* (cores de vértice) por face.
   - *Por quê:* a seleção por cor funciona por tolerância. Cores parecidas (dois marrons) se misturam na seleção; cores puras e distantes nunca se confundem.
2. **Asse a cor sem luz.** Em *Render Properties → Bake*, use o tipo *Diffuse* com só *Color* ligado (desligue *Direct* e *Indirect*), numa imagem nova do tamanho da textura final (1024 × 1024).
   - Se houver high poly, faça esse bake **do high para a low**, junto com o normal: o ID segue as partes esculpidas.
   - *Por quê:* sem luz, cada parte sai com uma cor única e uniforme. Com luz, a sombra muda a cor e a seleção falha nas áreas escuras.
3. **Salve o ID map em PNG** e exporte a low poly em FBX, como de costume.
   - *Por quê:* PNG não tem compressão com perda. Em JPG, as bordas entre as cores ganham ruído e a seleção fica serrilhada.

**Evidência:** o PNG do ID aberto no Krita ou no Blender, com uma cor uniforme por parte e bordas limpas.

## Etapa 2 — Importar o ID map no 3DCoatTextura

1. **Importe o modelo** em Per-Pixel Painting, como de costume.
2. **Importe o ID map como camada.** *Textures → Import Layers Colors* e escolha o PNG. (Se não estiver ali na versão do laboratório, procure no menu *Layers* a importação de *Layers Color*.)
   - *Por quê:* o ID entra como uma camada comum na pilha, que pode ser usada para seleção e máscaras.
3. **Renomeie a camada para `ID` e deixe-a no topo.** Ela pode ficar visível enquanto você seleciona e oculta no resto do tempo.
   - *Por quê:* a seleção por cor lê o que está visível. Com o ID por cima de tudo, as cores dele não se misturam com os materiais.

**Evidência:** print do modelo coberto pelas cores do ID, com as cores certas nas partes certas.

## Etapa 3 — Selecionar uma parte pela cor

1. **Deixe só a camada `ID` visível** (Alt+clique no olho).
2. **Pegue a ferramenta Select** e clique sobre a cor dos aros. Ajuste a tolerância se a seleção pegar cores vizinhas ou deixar falhas.
   - `Shift` + clique adiciona outra cor à seleção (aros **e** pregos, por exemplo). `Ctrl` + clique remove.
   - *Por quê:* é o *Color Selection* do Substance. A ferramenta Select transforma a área daquela cor numa seleção, que o 3DCoatTextura representa como área congelada.
3. **Confira o lado da seleção.** Faça um teste rápido: numa camada nova, pinte uma pincelada larga passando pelos aros e pelas tábuas.
   - Se a tinta ficou **só nos aros**, a seleção está pronta. Desfaça o teste (`Ctrl+Z`).
   - Se a tinta ficou **só fora dos aros**, use *Freeze → Invert Freeze/Selection* e teste de novo.
   - *Por quê:* dependendo da versão, a seleção protege a área clicada ou o resto. O teste mostra qual é o caso em dois segundos e evita aplicar o material do lado errado.

**Evidência:** a pincelada de teste aparecendo só na parte escolhida.

## Etapa 4 — Transformar a seleção em máscara (recomendado)

Com a seleção pronta, crie uma máscara da parte para usar com **Clipping Mask**. Assim a seleção vira algo permanente e editável.

1. **Crie a camada `M Aros`** (dentro de uma pasta `Aros – Metal`, se quiser organizar como no Substance).
2. **Preencha só a área selecionada.** *Freeze → Fill Unfrozen*, com qualquer cor.
3. **Desfaça a seleção.** *Freeze → Unfreeze All*.
   - *Por quê:* agora a parte está registrada numa camada. Você não precisa mais do ID para essa parte, e pode corrigir a máscara com pincel ou borracha.
4. **Aplique o material e prenda à máscara.** Crie `Aros – Smart Material metal` acima de `M Aros`, prenda o Smart Material (*Attach*), use *Fill Entire Layer* e, no painel **Layer Blending** da camada (botão direito na camada → *Layer Blending*), defina **Clip Mask Layer** = `M Aros`.
   - *Por quê:* o material fica no objeto todo, mas só aparece onde a máscara tem tinta. Se a máscara mudar, o material acompanha sem refazer o Fill.
5. **Repita para cada cor do ID.**

**Alternativa direta (sem máscara):** com a seleção ativa, crie a camada do material, prenda o Smart Material e preencha. O material cai só na parte. Depois, *Unfreeze All*. É mais rápido, mas para mudar a área depois será preciso selecionar de novo pelo ID e refazer o Fill.

**Evidência:** com o `ID` oculto, cada parte com seu material e nenhuma área vazando para a vizinha.

## Etapa 5 — Toque autoral com pincel

Crie uma camada de pincel por parte (`Aros – desgaste (pincel)`) e prenda-a à máscara da parte (*Clip Mask Layer*). Pinte com alphas e stencils sem se preocupar com a fronteira.

- *Por quê:* a máscara gerada pelo ID protege as partes vizinhas, e o pincel dá a intenção que o ID não tem.

## Problemas comuns

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| A seleção pega duas partes | Cores do ID parecidas | Usar cores puras e distantes no Blender, ou baixar a tolerância |
| A seleção deixa falhas e bordas serrilhadas | ID salvo em JPG, ou bake com luz | Assar só a cor (sem *Direct/Indirect*) e salvar em PNG |
| A seleção pega cores dos materiais, não do ID | Outras camadas visíveis | Deixar só a camada `ID` visível (Etapa 3) |
| O material caiu fora da parte | Seleção invertida | Fazer o teste da Etapa 3 e usar *Invert Freeze/Selection* |
| As cores do ID estão nas partes erradas | UV mudou depois do bake | Refazer o bake com o UV final |
| Esqueci o ID visível e ele saiu na exportação | Camada `ID` ligada | Ocultar ou excluir a camada `ID` antes de exportar |

## Checklist de autoavaliação

- [ ] O ID map tem uma cor pura e uniforme por parte, em PNG.
- [ ] O ID entrou como camada e está nas partes certas.
- [ ] Testei o lado da seleção antes de aplicar o material.
- [ ] Cada parte tem uma máscara `M` (ou camada de material) criada a partir do ID.
- [ ] A camada `ID` está oculta ou foi excluída antes da exportação.

## Para a crítica

Mostre o ID map ao lado do resultado final e explique **por que você dividiu a peça nessas partes**: o que cada parte conta sobre o material e o uso do objeto?

## Fontes

- [3DCoat — ID map (Import Layers Colors)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/)
- [3DCoat — Paint Tool Panel (ferramenta Select)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-room-tools/)
- [3DCoat — Freeze (Fill Unfrozen, Invert Freeze/Selection)](https://3dcoat.com/documentation/manual/interface-and-navigation/freeze-menu/)
- [3DCoat — Blending Panel (Clip Mask Layer)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/)
- [Blender Manual — Render Baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)
