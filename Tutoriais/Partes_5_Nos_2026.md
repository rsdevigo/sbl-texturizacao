# Materiais por parte da malha — Modo 5: Nós (3DCoatTextura 2026.11)

22/10/2026 · Rodrigo

> **Recurso novo.** O sistema de nós (*Node System*, com o *Node Editor*) chegou ao 3DCoatTextura na versão 2026.11. Confira se o laboratório está nessa versão ou mais nova e anote os nomes dos nós que estiverem diferentes. A documentação escreve os nomes ora em minúsculas ("simple material"), ora juntos (*SimpleMaterial*); aqui usamos a forma junta, que é a dos nós na biblioteca.

## Visão geral

O sistema de nós é o mais próximo do Substance Painter: o material e a máscara ficam **ligados** à camada ou à pasta e se **recalculam** quando você muda um valor ou troca a imagem da máscara. Não é preciso limpar e preencher de novo.

Para materiais por parte, a ideia é:

- uma **pasta** por parte (`Aros – Metal`);
- na pasta, um **material** (nó *SimpleMaterial*);
- e uma **máscara** (nó *out mask*) alimentada por uma imagem em preto e branco da parte, ou por uma condição.

**Diferença para a Clipping Mask:** a Clipping Mask usa uma **camada pintada** como máscara. Aqui, a máscara é um **grafo de nós** e pode combinar a imagem da parte com condições (só as quinas dos aros, por exemplo) sem camadas extras.

**Quando usar:** quando a turma já domina o modo Clipping Mask e quer o fluxo procedural, ou em peças em que se vai ajustar muito material e máscara.

**Exemplo usado no tutorial:** o barril da Semana 2, com tábuas de madeira e aros de metal.

**Resultado esperado:** uma pasta por parte, com material e máscara em nós, ajustáveis sem refazer o Fill.

## Etapa 1 — Preparar a máscara da parte no Blender

O nó de textura lê uma imagem pelo UV. Para cada parte, você precisa de uma imagem **branca na parte e preta no resto**.

1. **Crie um material por parte** no Blender (`Tabuas`, `Aros`).
2. **Gere uma imagem por parte.** O caminho mais simples: asse um ID map (cores chapadas por parte, bake *Diffuse* só com *Color*, salvo em PNG) e, no Krita, crie uma cópia por parte, pintando de branco a cor da parte e de preto todo o resto. Salve como `MASK_Aros.png`, `MASK_Tabuas.png`.
   - *Por quê:* o nó de máscara lê tons de cinza. O branco libera o material, o preto esconde. É exatamente o "preto e branco" da máscara do Substance.
   - O bake e as imagens precisam usar o **UV final**. Se o UV mudar, as máscaras precisam ser refeitas.
3. **Exporte a low poly em FBX** como de costume.

**Evidência:** as imagens de máscara abertas ao lado do UV, com o branco exatamente sobre as ilhas da parte.

## Etapa 2 — Criar a pasta e o material em nós

1. **Crie a pasta da parte** no painel Layers (*Create folder group*) e nomeie `Aros – Metal`. Coloque uma camada dentro dela.
2. **Abra o Node Editor** para a pasta.
3. **Adicione um *SimpleMaterial*,** defina cor, gloss e metal e ligue-o ao **out material**.
   - *Por quê:* o *SimpleMaterial* faz o papel da *fill layer* do Substance: um material que cobre tudo, até que a máscara recorte.
   - Aplicado à **pasta**, o material e a máscara valem para todas as camadas dentro dela. É o "folder com máscara" do Substance.

## Etapa 3 — Ligar a máscara da parte

1. **Adicione um nó *UVWTexture*** e arraste `MASK_Aros.png` para ele (com `Ctrl`).
2. **Ligue a saída dele ao *out mask*.**
   - *Por quê:* o *out mask* transforma o que recebe na transparência da camada ou da pasta. Branco aparece, preto some.
3. **Confira a polaridade.** Se o metal apareceu nas tábuas, ligue o **Invert** daquela entrada.
   - Para ver o que sai de qualquer nó, passe o mouse sobre a saída segurando `Ctrl`; `Ctrl`+clique fixa a visualização.
4. **Ajuste onde a máscara vale.** No *out mask*, o parâmetro **mask mode** controla onde a máscara é aplicada, e o **ranged map** permite refinar a faixa de valores (útil se a máscara tiver bordas suavizadas).
5. **Aplique.** Preencha a camada com *Fill Entire Layer*, ou pinte com pincel ou stencil para aplicar só onde quiser.

**Evidência:** o metal aparecendo só nos aros. Troque a cor do *SimpleMaterial*: o modelo deve atualizar sem nenhum Fill novo.

## Etapa 4 — Combinar a parte com uma condição (opcional)

Para efeitos que ficam **dentro** de uma parte, como desgaste só nas quinas dos aros:

1. **Adicione um *SimpleMask*** com a condição desejada (*convex* para quinas, *concave* para frestas, *in shadow* para áreas fechadas). Calcule os mapas de geometria quando o 3DCoatTextura pedir.
2. **Ligue a máscara da parte (*UVWTexture*) na entrada *degree map*** do *SimpleMask*, e o *SimpleMask* no *out mask*. Ajuste a quantidade com **Mask Degree**.
   - *Por quê:* a condição escolhe a região (quinas) e a imagem da parte limita essa região aos aros. É o "generator dentro da pasta com máscara" do Substance.
   - Se a máscara sumir, aumente um pouco a influência, como sugere a documentação.

## Atalhos da biblioteca de nós

- **NGMasks prontas.** A biblioteca de máscaras em nós (*NGMasks*) traz desgaste, sujeira e riscos editáveis. Escolha o material e aplique uma máscara da biblioteca com um clique; depois, combine com a máscara da parte (Etapa 4) para o efeito ficar só nela.
- **TriPlanar em vez de UVWTexture para grunge e padrões.** O nó *TriPlanar* projeta a textura pelos três eixos, sem depender do UV, e evita marcar as emendas. Use o *UVWTexture* só para a **máscara da parte**, que precisa seguir o UV. O nó *inGizmoTransform* controla posição, rotação e escala do *TriPlanar* e do *UVWTexture* direto na viewport.

## Etapa 5 — Toque autoral com pincel

1. **Crie uma camada de pincel dentro da pasta** `Aros – Metal`.
2. **Pinte com alphas e stencils.**
   - *Por quê:* aplicada à pasta, a máscara também recorta a camada de pincel. Confira na versão do laboratório; se a pincelada vazar, use o modo Clipping Mask para a camada de pincel (*Clip Mask Layer* apontando para uma camada com tinta só nos aros).

## Problemas comuns

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| O material aparece no lugar errado | Polaridade da máscara invertida | Ligar o *Invert* da entrada |
| A máscara não bate com a parte | Imagem de máscara feita com outro UV | Refazer o bake e as máscaras com o UV final |
| A máscara some quando uso o *SimpleMask* | Influência baixa | Aumentar levemente a influência / *Mask Degree* |
| Mudo um valor e nada acontece | Nó não ligado ao *out material* / *out mask*, ou camada não preenchida | Conferir as ligações e usar *Fill Entire Layer* |
| Os nomes dos nós são diferentes | Versão do 3DCoatTextura | Procurar nós equivalentes na versão do laboratório e anotar |

## Checklist de autoavaliação

- [ ] Cada parte tem uma imagem de máscara em preto e branco feita com o UV final.
- [ ] Cada parte tem uma pasta com *SimpleMaterial* e *out mask*.
- [ ] Mudei uma cor ou um valor e o modelo atualizou sem refazer o Fill.
- [ ] Combinei a máscara da parte com uma condição em pelo menos uma parte.
- [ ] Anotei o que estava diferente na versão do laboratório.

## Para a crítica

Mostre o grafo de nós de uma parte e explique **o que cada nó decide**: o quê (material), onde (máscara) e quanto (condição e intensidade).

## Fontes

- [3DCoat — Texturing with nodes (2026)](https://3dcoat.com/documentation/2026/07/01/texturing-with-nodes/)
- [3DCoat — Node Editor](https://3dcoat.com/documentation/manual/nodesystem/node-editor/)
- [3DCoat — ID map](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/)
- [Blender Manual — Render Baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)
