# Materiais por parte da malha — Modo 2: Freeze (congelar)

22/10/2026 · Rodrigo

> Os nomes de menus do 3DCoatTextura mudam entre versões. Se alguma opção não estiver no lugar indicado, confira na versão 2026 do laboratório e anote a diferença para a turma.

## Visão geral

**Freeze** é "proteger" uma área do modelo: enquanto ela está congelada, nenhum pincel ou Fill consegue pintar ali. Para aplicar um material só numa parte, você congela **tudo menos** essa parte, aplica o material e depois descongela.

É como passar fita crepe antes de pintar uma parede: a fita protege, a tinta vai só onde ficou livre.

**Diferença para a Clipping Mask:** aqui o recorte é decidido **antes** do Fill e fica gravado na camada. Se a área da parte mudar depois, é preciso congelar de novo e refazer o Fill. Em troca, a pilha fica mais simples: não há camadas de máscara.

**Quando usar:** peças com poucas partes e fronteiras definidas, aplicação rápida de um material numa área, ou retoques pontuais protegendo a vizinhança.

**Exemplo usado no tutorial:** o barril da Semana 2, com tábuas de madeira e aros de metal.

**Resultado esperado:** cada parte com seu material, cada material numa camada própria com nome de parte, aplicado sem vazar para as partes vizinhas.

## Etapa 1 — Separar as partes no Blender

1. **Atribua um material por parte** (`Tabuas`, `Aros`), ou mantenha as peças soltas como objetos separados no mesmo FBX.
   - *Por quê:* o 3DCoatTextura consegue congelar de uma vez um material inteiro (*Surface Material*) ou um objeto inteiro (*Paint Object*). Sem essa separação, o congelamento precisa ser pintado à mão.
2. **Confira o UV, aplique as transformações e exporte em FBX.**
   - *Por quê:* prefira um único UV com vários materiais apontando para ele. Assim o modelo exporta um conjunto só de texturas.

**Evidência:** no Blender, cada parte com uma cor de material diferente no *Viewport Shading: Solid*, com *Color: Material*.

## Etapa 2 — Congelar tudo menos a parte

O caminho mais direto é congelar a parte desejada e **inverter**.

1. **Congele a parte que vai receber o material.** No menu **Freeze**:
   - **Freeze Surface Material**, se as partes são materiais; ou
   - **Freeze Paint Object**, se as partes são objetos.

   Clique sobre os aros (ou escolha o material/objeto na lista, conforme a versão).
2. **Inverta.** *Freeze → Invert Freeze/Selection*.
   - *Por quê:* agora os aros estão livres e todo o resto (as tábuas) está protegido. Inverter é mais rápido do que congelar uma por uma todas as outras partes.
3. **Confira a área congelada.** O 3DCoatTextura mostra as áreas congeladas com uma trama. Se não aparecer, use *Freeze → Show/Hide Freeze* ou *Toggle Freeze View*.
   - *Por quê:* aplicar o material com o congelamento invertido é o erro mais comum deste modo. Olhar antes custa dois segundos.

**Outras formas de congelar:**

- **Ferramenta Freeze, modos *Convexity* e *Concavity*:** congela por forma, útil para proteger quinas ou frestas.
- **Pincel com a ferramenta Freeze:** pinta o congelamento à mão, para áreas que não coincidem com a malha.
- **Fill com *Fill with freeze*:** na ferramenta Fill, essa opção congela a área em vez de pintá-la. Combina com o escopo *Surface Material*/*Object* e com o **Use max. angle** para hard surface sem preparação.

**Evidência:** print com a trama de congelamento sobre as tábuas e os aros livres.

## Etapa 3 — Aplicar o material na parte livre

1. **Crie uma camada com nome de parte e material:** `Aros – Smart Material metal`. Se quiser organizar como no Substance, coloque-a numa pasta `Aros – Metal`.
2. **Prenda o Smart Material** (botão direito no material → *Attach to the current layer*).
3. **Preencha.** Use o Fill com escopo *Layer*, ou *Freeze → Fill Unfrozen* (preenche só as áreas livres).
   - *Por quê:* o congelamento impede o material de cair nas tábuas. O Smart Material calcula as condições (borda, cavidade) normalmente, só dentro da área livre.
4. **Descongele.** *Freeze → Unfreeze All*.
   - *Por quê:* se você esquecer o congelamento ligado, a próxima camada que pintar vai "falhar" nas tábuas sem motivo aparente.

**Evidência:** a camada do metal, vista sozinha (Alt+clique no olho), tem tinta só nos aros.

## Etapa 4 — Repetir para as outras partes

1. **Congele os aros, inverta, aplique a madeira** numa camada `Tábuas – Smart Material madeira`, descongele.
2. **Guarde o congelamento se for reutilizar.** *Freeze → Store Freezing State* salva o estado atual; *Restore Freezing State* traz de volta.
   - *Por quê:* refazer o Fill de um material (depois de mudar uma cor no Smart Material, por exemplo) exige o mesmo congelamento de antes. Guardar evita refazê-lo à mão.

**Atalho útil — congelar a partir de uma camada.** Botão direito numa camada já pintada → **Freeze Painted Pixels** congela o que ela tem de tinta; **Freeze Transparent Pixels** congela o que ela **não** tem.

- *Por quê:* depois que a camada do metal existe, ela mesma vira o "molde" dos aros. *Freeze Transparent Pixels* nela deixa livres só os aros, para pintar desgaste ou trocar o material sem precisar da Etapa 2 de novo.

## Etapa 5 — Toque autoral com pincel protegido

1. **Congele a vizinhança** (Etapa 2 ou o atalho acima) e crie uma camada `Aros – desgaste (pincel)`.
2. **Pinte com alphas e stencils** sem medo da fronteira.
   - *Por quê:* o congelamento protege as tábuas enquanto você pinta solto nos aros.
3. **Descongele no fim.**

## Problemas comuns

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| O material caiu só nas tábuas (o contrário do desejado) | Faltou inverter, ou inverteu duas vezes | Conferir a trama e usar *Invert Freeze/Selection* |
| O pincel "não pinta" numa área | Congelamento esquecido de uma etapa anterior | *Freeze → Unfreeze All* |
| Mudei o Smart Material e preciso refazer | O recorte está gravado na camada | *Restore Freezing State*, limpar a camada e preencher de novo |
| A borda entre as partes ficou serrilhada ou com fresta | Congelamento com borda dura em baixa resolução | *Smooth Freezing* ou *Expand Frozen Area* / *Contract Frozen Area* antes do Fill |
| *Freeze Surface Material* congela o modelo todo | As partes não chegaram separadas | Voltar à Etapa 1 |

## Checklist de autoavaliação

- [ ] Cada parte tem uma camada (ou pasta) com nome de parte e material.
- [ ] Vista sozinha, cada camada tem tinta só na sua parte.
- [ ] Nenhuma área ficou congelada no fim (*Unfreeze All*).
- [ ] Guardei o estado de congelamento das partes que vou retrabalhar.
- [ ] As pinceladas à mão não vazaram para as partes vizinhas.

## Para a crítica

Mostre uma parte retrabalhada depois da primeira aplicação e explique **como você refez o recorte**: guardou o estado, congelou a partir da camada ou congelou de novo?

## Fontes

- [3DCoat — Freeze (menu)](https://3dcoat.com/documentation/manual/interface-and-navigation/freeze-menu/)
- [3DCoat — Paint Tool Panel (ferramentas Freeze, Select e Fill)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-room-tools/)
- [3DCoat — The Layers Panel (Freeze Painted/Transparent Pixels)](https://3dcoat.com/documentation/manual/interface-and-navigation/the-layers-panel)
- [3DCoat — Attach a Smart Material to a layer](https://3dcoat.com/documentation/?p=6295)
