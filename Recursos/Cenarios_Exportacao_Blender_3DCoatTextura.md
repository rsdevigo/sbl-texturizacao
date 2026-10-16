# Cenários de exportação: Blender → 3DCoatTextura

> Material de apoio publicado no site, no menu **Recursos**.
> Complementa o [Guia de Migração Substance → 3DCoatTextura](Guia_Migracao_Substance_3DCoatTextura.md) e o Plano de Aula da Semana 7.
> Levantamento feito em outubro de 2026. Os nomes exatos das opções da janela de importação mudam entre versões: confira na 2026 do laboratório.

Ponto de partida: **o 3DCoatTextura não tem UV Room nem salas de modelagem**. Tudo o que for de malha e de UV precisa sair resolvido do Blender. O 3DCoat só consegue *receber* esses estados com algumas opções de importação.

São **10 cenários**, agrupados em quatro perguntas.

---

## A. A malha tem UV?

| # | Cenário | O que acontece no 3DCoatTextura | O que fazer no Blender |
|---|---|---|---|
| 1 | **UV único, sem sobreposição, dentro de 0–1, um material.** É o caso ideal, o do Hero Asset | Importação direta em Per-Pixel Painting, mantendo o UV | Nada além do [checklist](#checklist-de-exportação) |
| 2 | **Sem UV** | Sem UV Room, não dá para abrir UV no Textura. A importação pode até oferecer mapeamento automático, mas o resultado não volta para o Blender nem para a engine de forma confiável | Abrir o UV antes de exportar. Para teste rápido, Smart UV Project; para entrega, seams manuais (Semanas 3–4) |

## B. Como o UV está organizado?

| # | Cenário | O que acontece no 3DCoatTextura | O que fazer no Blender |
|---|---|---|---|
| 3 | **Ilhas sobrepostas ou espelhadas** (simetria, peças repetidas) | O que você pinta num lado aparece no outro. AO e Curvature calculados podem sair errados nas áreas sobrepostas. A importação tem tratamento específico para UV sobreposto, e a *Light Based Curvature* da Light Baking Tool lida melhor com isso | Se a sobreposição for intencional (economia de texel), tudo bem: só não pinte detalhes assimétricos ali. Se não for, separe as ilhas |
| 4 | **UV fora de 0–1 / textura repetindo** (paredes, pisos tileáveis) | A pintura Per-Pixel trabalha no espaço 0–1. A repetição precisa ser feita no material da engine | Pintar a textura tileável num plano 0–1 (ou na trim sheet) e fazer a repetição na Unity, com tiling do material. É o fluxo das Semanas 6 e 14 |
| 5 | **Trim sheet** (várias peças mapeadas sobre faixas da mesma textura) | Na prática é o cenário 3 de propósito: muitas ilhas sobre a mesma área | Texturizar **a trim sheet num plano**, e não as peças. As peças só recebem o UV no Blender |
| 6 | **Vários materiais / UV sets** (objeto com mais de um material, ou vários objetos num FBX) | Cada material vira um conjunto separado de texturas, e a exportação gera um jogo de mapas por material | Decidir antes: **atlas único** (um material, menos draw calls, bom para o kit modular) ou **um material por peça** |
| 7 | **Mais de uma camada de UV** (ex.: `UVMap` + `UVMap.001` para lightmap) | O FBX leva todas, e o 3DCoat pode pegar a errada | Deixar a UV de textura como **primeira e ativa**. A UV de lightmap a Unity gera sozinha |
| — | **UDIM** (vários tiles de UV) | A importação suporta (vira UV sets) | Fora do escopo de jogos da disciplina |

## C. Em que estado está a geometria?

| # | Cenário | O que acontece no 3DCoatTextura | O que fazer no Blender |
|---|---|---|---|
| 8 | **Modificadores não aplicados** (Mirror, Bevel, Subdivision, Array) | O FBX pode exportar a malha com ou sem eles, e o UV final é o de depois dos modificadores. Mirror sem deslocamento de UV cai no cenário 3 | Aplicar os modificadores (ou marcar *Apply Modifiers* no export) e **conferir o UV depois de aplicar** |
| 9 | **Transformações e normais** (escala ou rotação não aplicadas, sombreamento) | Modelo gigante, minúsculo ou girado. Normais e sharp edges mal definidos geram AO/Curvature com artefatos | `Ctrl+A → All Transforms`; definir sharp edges / Auto Smooth; conferir o eixo (a importação tem opção Z-up) |

## D. O que vem junto com a malha?

| # | Cenário | O que acontece no 3DCoatTextura | O que fazer no Blender |
|---|---|---|---|
| 10a | **Par low/high-poly para bake** | O Textura não faz o bake de high para low. Ele recebe a low com os mapas prontos | Fazer o bake de Normal/AO/ID no Blender (Semanas 11–12), exportar só a low e importar os mapas no 3DCoat como camadas |
| 10b | **Modelo que já tem texturas** (ex.: base da Semana 6) | Dá para importar com as texturas, ou trazer cada mapa como camada | Exportar com as imagens ligadas ao material, ou trazer os PNGs à parte |
| 10c | **Modelo alterado depois de começar a texturizar** | Se só a geometria mudou e o UV ficou igual, dá para recarregar e manter a pintura. Se o UV mudou, a pintura precisa ser reprojetada e pode perder qualidade | **Fechar o UV antes de ir para o 3DCoat.** Esse é o principal motivo do Hero Asset ter UV aprovado antes da Semana 7 |

---

## Checklist de exportação

Cobre quase todos os casos:

1. UV de textura único, ativo, dentro de 0–1 (ou sobreposição intencional e documentada).
2. Modificadores aplicados e UV conferido depois de aplicar.
3. Transformações aplicadas, normais e sharp edges definidos.
4. Materiais decididos: atlas ou um por peça.
5. Exportar em FBX, só a low-poly; os bakes vão como imagens à parte.

---

## Documentação

- [Importing into the Painting Room (3DCoat)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/): opções de importação Per-Pixel (UV, Z-up, normais, smoothing groups, UV sobreposto, múltiplos UV tiles, importação de mapas)
- [Textures Menu (3DCoat)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/): importação e exportação de UV e texturas, Mesh and Texture Resolution
- [Light Baking Tool (3DCoat)](https://3dcoat.com/documentation/manual/interface-and-navigation/edit-menu/light-baking-tool/): *Light Based Curvature* para UV sobreposto
- [ID map (3DCoat)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/): importar ID map bakeado no Blender
- [FBX (Blender Manual)](https://docs.blender.org/manual/en/latest/files/import_export/fbx.html): opções de exportação FBX
