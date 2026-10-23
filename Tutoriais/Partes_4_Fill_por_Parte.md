# Materiais por parte da malha — Modo 4: Fill direto por parte

22/10/2026 · Rodrigo

> Os nomes de menus do 3DCoatTextura mudam entre versões. Se alguma opção não estiver no lugar indicado, confira na versão 2026 do laboratório e anote a diferença para a turma.

## Visão geral

É o modo mais rápido: a própria ferramenta **Fill** limita o preenchimento a uma parte do modelo, sem máscara e sem congelamento. Você prende o Smart Material, escolhe o escopo do Fill e clica na parte.

O Fill tem três jeitos de saber onde parar:

| Escopo / opção | Para onde o Fill vai | Precisa de preparação no Blender? |
| --- | --- | --- |
| **Object** | O objeto inteiro em que você clicou (*Paint Object*) | Sim: partes como objetos separados |
| **Surface Material** | O material inteiro em que você clicou | Sim: um material por parte |
| **Use max. angle** | Se espalha pelas faces vizinhas até uma quina mais fechada que o ângulo | Não: usa a própria malha |

**Diferença para os outros modos:** não sobra nada para editar depois. O recorte fica gravado na camada. Se a área mudar, é preciso limpar a camada e preencher de novo.

**Quando usar:** blocagem rápida dos materiais, testes de combinação (madeira clara ou escura?), peças hard surface com partes bem separadas e, principalmente, para preencher a **camada de máscara** do modo Clipping Mask.

**Exemplo usado no tutorial:** o barril da Semana 2, com tábuas de madeira e aros de metal.

**Resultado esperado:** cada parte com seu material, cada material numa camada com nome de parte, aplicado em um clique por parte.

## Etapa 1 — Preparar no Blender (para Object e Surface Material)

1. **Atribua um material por parte** (`Tabuas`, `Aros`), ou deixe as peças soltas como objetos separados no mesmo FBX.
   - *Por quê:* o Fill por *Surface Material* ou por *Object* usa exatamente essa separação como fronteira.
2. **Para o modo por ângulo, marque bem as quinas.** As fronteiras entre as partes devem ser quinas reais da malha (por exemplo, o aro "sobe" da tábua com uma face lateral).
   - *Por quê:* o Fill por ângulo para nas quinas. Se o aro estiver no mesmo plano da tábua, sem quina entre eles, o Fill passa direto.
3. **Confira o UV, aplique as transformações e exporte em FBX.**

**Evidência:** no Blender, cada parte com uma cor de material diferente no *Viewport Shading: Solid*, com *Color: Material*.

## Etapa 2 — Fill por material ou por objeto

1. **Crie a camada `Aros – Smart Material metal`.** Se quiser organizar como no Substance, coloque-a numa pasta `Aros – Metal`.
2. **Prenda o Smart Material.** Botão direito no material na biblioteca → *Attach to the current layer*.
3. **Escolha o escopo.** Na ferramenta **Fill**, troque o escopo de *Layer* para **Surface Material** (partes como materiais) ou **Object** (partes como objetos).
   - *Por quê:* o escopo padrão (*Layer*) preenche o modelo inteiro. Trocar o escopo é o que limita o material à parte.
4. **Ligue o *Preview*,** se disponível, e passe o mouse sobre os aros.
   - *Por quê:* o preview mostra a área antes de gravar. Evita desfazer e refazer.
5. **Clique nos aros.**
6. **Repita para as tábuas** numa camada `Tábuas – Smart Material madeira`.

**Evidência:** cada camada, vista sozinha (Alt+clique no olho), tem tinta só na sua parte.

## Etapa 3 — Fill por ângulo (sem preparação)

1. **Crie a camada e prenda o Smart Material**, como na Etapa 2.
2. **Ligue *Use max. angle*** na ferramenta Fill e comece com um ângulo médio (algo como 30 a 45°).
3. **Clique numa face dos aros** e observe até onde o preenchimento foi.
   - Se **vazou** para as tábuas: diminua o ângulo.
   - Se **parou antes** de cobrir o aro inteiro (nas curvas do aro, por exemplo): aumente o ângulo, ou clique de novo nas áreas que faltaram.
   - *Por quê:* o ângulo define quão fechada uma quina precisa ser para virar fronteira. Em peças curvas, as faces de uma mesma parte também formam pequenos ângulos entre si, então o valor certo fica entre "parar nas curvas" e "vazar nas quinas".

**Evidência:** print do aro inteiro preenchido sem nenhuma tábua atingida.

## Etapa 4 — Trocar ou ajustar um material

O recorte está gravado na camada, então mudar um material segue sempre a mesma rotina:

1. **Ajuste o Smart Material** (ou prenda outro).
2. **Limpe a camada** da parte (botão direito na camada → *Make Transparent*).
3. **Preencha de novo** com o mesmo escopo, clicando na mesma parte.
   - Para refazer com o mesmo material preso, o menu da camada tem **Refill Material**. Confira se ele respeita o escopo na versão do laboratório; se preencher o modelo todo, use o Fill com escopo.
   - *Por quê:* é a lógica raster do fluxo clássico (sem nós). O resultado não se atualiza sozinho.

## Etapa 5 — Proteger a parte para o pincel

O Fill direto não deixa máscara para o pincel respeitar. Para pintar desgaste sem vazar:

1. **Botão direito na camada do material da parte → *Freeze Transparent Pixels*.**
   - *Por quê:* congela tudo onde a camada não tem tinta, ou seja, tudo fora da parte. A própria camada do material vira o molde.
2. **Crie a camada de pincel e pinte.**
3. **Descongele no fim** (*Freeze → Unfreeze All*).

> Se você perceber que vai retrabalhar muito as partes, use o Fill deste tutorial só para preencher camadas de **máscara** e siga o modo **Clipping Mask**. É a combinação mais flexível.

## Problemas comuns

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| O Fill pinta o modelo todo | Escopo em *Layer* | Trocar para *Surface Material* ou *Object* |
| O Fill por material pinta tudo | As partes não chegaram separadas | Voltar à Etapa 1 |
| O Fill por ângulo vaza | Ângulo alto, ou falta quina na fronteira | Diminuir o ângulo, ou criar a quina no Blender |
| O Fill por ângulo para no meio da parte | Ângulo baixo para uma peça curva | Aumentar o ângulo ou clicar nas áreas que faltaram |
| Mudei o material e nada mudou | Lógica raster | Limpar a camada e preencher de novo (Etapa 4) |

## Checklist de autoavaliação

- [ ] Cada parte tem uma camada com nome de parte e material.
- [ ] Vista sozinha, cada camada tem tinta só na sua parte.
- [ ] Sei qual escopo usei em cada parte (objeto, material ou ângulo) para poder refazer.
- [ ] Pintei o desgaste protegido por *Freeze Transparent Pixels* e descongelei no fim.

## Para a crítica

Mostre duas versões da mesma peça com combinações diferentes de material (feitas com este modo) e justifique **qual combinação lê melhor o tema do kit**.

## Fontes

- [3DCoat — Paint Tool Panel (Fill: Layer, Surface Material, Object, Use max. angle, Preview)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-room-tools/)
- [3DCoat — ID map (Fill por ângulo como alternativa ao ID)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/)
- [3DCoat — The Layers Panel (Refill Material, Freeze Transparent Pixels)](https://3dcoat.com/documentation/manual/interface-and-navigation/the-layers-panel)
- [3DCoat — Attach a Smart Material to a layer](https://3dcoat.com/documentation/?p=6295)
