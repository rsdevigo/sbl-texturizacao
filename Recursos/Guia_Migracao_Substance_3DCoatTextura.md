# Guia de migração: Substance Painter → 3DCoatTextura 2026

> Material de apoio publicado no site, no menu **Recursos**.
> Complementa a lista de cursos em [`Cursos_3DCoatTextura_Migracao_Substance.md`](Cursos_3DCoatTextura_Migracao_Substance.md).
> Levantamento feito em outubro de 2026. Os nomes de menus do 3DCoat mudam entre versões, então confira na instalação do laboratório.

---

## 0. A diferença que muda tudo

| | Substance Painter | 3DCoatTextura |
|---|---|---|
| Lógica da camada | A fill layer cobre o objeto inteiro e a **máscara recorta** | A camada só existe **onde foi pintada ou preenchida** |
| Generator / condição | Procedural, recalculado o tempo todo | **Fill/pincel com condição:** calculado uma vez, no clique (raster). **Nós (NG, 2026):** procedural e recalculado, como no Substance |
| Smart Material | Pasta com fill layers e máscaras | Material de várias camadas com **condições**. Deve ser **preso** à camada (*Attach*) e depois **aplicado** com Fill ou pincel |

Regra prática para quem migra: **Attach define *o quê*, Fill/pincel define *onde*.** Ao mudar a condição no fluxo clássico, limpe a camada e preencha de novo.

---

## 1. Tabela de conversão de ferramentas

| Substance Painter | Equivalente no 3DCoatTextura | Como usar (resumo) | Documentação Substance | Documentação 3DCoat |
|---|---|---|---|---|
| **Generator** (AO, Curvature, Position, Dirt…) | **1) Conditions** (*More on Shadow*, *More on Convex*, *More on Concave*, *More on Top*…) no pincel/Fill ou dentro do Smart Material. **2) Nó `simple mask`** (2026), com *condition type* convex/concave/in shadow. **3) NGMasks** prontas (Dirt, Rust, Scratches) | Pré-requisito: *Edit → Calculate Curvature* e *Edit → Calculate Occlusion*. A via 1 é raster (refazer o Fill a cada ajuste). As vias 2 e 3 são procedurais | [Generator](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/effects/generator) | [Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) · [Texturing with nodes](https://3dcoat.com/documentation/2026/07/01/texturing-with-nodes/) · [NGMasks](https://3dcoat.com/documentation/manual/nodesystem/masks/) |
| **Masking / Mask** (black/white mask) | **Layer Mask** (máscara em tons de cinza ao lado da camada) e **Clipping Mask** (pinta só onde a camada de baixo é opaca). Na transparência da própria camada, o "preto" da máscara corresponde ao que não foi pintado | Clipping: botão direito na camada → opção de clipping. *Clip Mask Layer* e *Invert Clip Mask* ficam no painel de Blending da camada | [Masking and effects](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/interface/layer-stack/masking-and-effects) | [Layer and Clipping Masks](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/layer-and-clipping-masks/) · [Blending Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/) |
| **Filters** (Blur, HSL, Levels, Sharpen…) | **1) Brightness/Contrast** da camada no painel de Blending. **2) Ajustes de camada** (*Adjust*: matiz, saturação, brilho…). **3) NGFilters** (2026): filtros por nós que leem a camada (`inLayerColor`) e devolvem o resultado | Os NGFilters precisam ficar **acima da camada e dentro de um grupo** (pasta) | [Filter](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/effects/filter) · [Levels](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/effects/levels) | [NGFilters](https://3dcoat.com/documentation/manual/nodesystem/filters/) · [Blending Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/) · vídeo oficial [Adjust](https://youtu.be/1JTdHK-bxPg) |
| **Anchors** (Anchor Point: uma camada lê o resultado de outra) | **Não há equivalente direto.** Aproximações: **1) Clip Mask Layer** (uma camada é mascarada pela opacidade de outra). **2) Condições *More on Bumped* / *More on Dent***, que leem o relevo (Depth) da camada atual. **3) Nós de camada** (`inLayerColor`, `inLayerFloat`) no Node Editor para ler dados de camadas | Para o caso clássico (desgaste reagindo a detalhes pintados em height), pinte o detalhe no Depth e use *More on Bumped/Dent* | [Anchor Point](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/effects/anchor-point) | [Blending Panel (Clip Mask Layer)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/) · [Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) · [Node Editor](https://3dcoat.com/documentation/manual/nodesystem/node-editor/) |
| **Brush** (Paint tool, alphas, stencils) | **Pincéis + Alphas** (painel com atalho `T`), **Brush Options** (jitter, rotação, espaçamento), **Stencils** e Smart Material como "material do pincel" | Um único pincel pinta Color, Depth, Gloss e Metalness ao mesmo tempo. Ative ou desative cada canal na barra superior | [Painting](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/painting/painting) | [Brushes general use](https://3dcoat.com/documentation/manual/brush-components/brushes-alphas/) · [Brush Options](https://3dcoat.com/documentation/manual/brush-components/brush-options/) |
| **Group masking** (máscara em pasta) | **Pastas de camadas (group folders)**. No sistema de nós de 2026, dá para aplicar um material ou máscara à **pasta** e controlar todas as camadas dela juntas | Crie a pasta, mova as camadas para dentro e aplique um `simple material` ou uma máscara de nó à pasta. Confira na versão do laboratório | [Layer stack](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/interface/layer-stack/layer-stack) | [GPU Texturing (folders, masks)](https://3dcoat.com/documentation/manual/texturing/) · [Texturing with nodes (folders)](https://3dcoat.com/documentation/2026/07/01/texturing-with-nodes/) |
| **Color ID Map Mask** (Color Selection) | **ID map importado:** *Textures → Import Layers Colors* cria uma camada que serve de máscara ou seleção. **O 3DCoat não gera o ID map a partir do high-poly** (bake no Blender). Alternativa sem ID: **Fill limitado por ângulo de polígono** | O ID map é bakeado no Blender (Semana 12), importado e usado com *Clip Mask Layer* ou como referência de seleção | [Effects (Color Selection)](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/effects/effects) · [Color Map from Mesh (baker)](https://experienceleague.adobe.com/en/docs/substance-3d/bakers/bakers-settings/color-map-from-mesh) | [ID map](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/) |

> **Atenção (máscaras):** a página antiga do painel de Blending diz que o 3DCoat "não suporta máscaras de camada em tons de cinza como o Photoshop ou o Substance". As páginas mais recentes (GPU Texturing, Layer and Clipping Masks) já descrevem *layer masks*. Confira na 2026 do laboratório se a máscara aparece ao lado da camada no painel Layers.

---

## 2. Workflow Blender → 3DCoatTextura → Unity: documentação e vídeos

### 2.1 Observação importante sobre o AppLink

O **AppLink do Blender** envia a malha para a **Modelling Room**, que **não existe no 3DCoatTextura** (ele só tem Paint Room e Render Room). Na disciplina, o caminho seguro é **exportar e importar manualmente** (FBX/OBJ):

1. **Blender:** UV pronto, transformações aplicadas, exportar **FBX** (ou OBJ para um único objeto).
2. **3DCoatTextura:** importar em **Per-Pixel Painting**, workflow **Roughness/Metalness** (o "Metalness PBR" do plano de aula), resolução 1024².
3. **Texturizar:** camadas, condições, Smart Materials e Depth (para gerar o Normal).
4. **Exportar texturas** com o preset da engine (Unity) ou da Blender.
5. **Blender e/ou Unity:** reconectar os mapas (Principled BSDF + nó Normal Map no Blender, ou URP Lit na Unity).

### 2.2 Documentação oficial

| Etapa | Documento | Link |
|---|---|---|
| Blender: exportar FBX | Blender Manual: FBX | https://docs.blender.org/manual/en/latest/files/import_export/fbx.html |
| 3DCoat: visão geral do texturing (canais, camadas, presets de exportação Unity/Blender) | GPU Texturing | https://3dcoat.com/documentation/manual/texturing/ |
| 3DCoat: pintura Per-Pixel | Per-Pixel Painting | https://3dcoat.com/documentation/manual/texturing/per-pixel-painting/ |
| 3DCoat: canais PBR | PBM Channels | https://3dcoat.com/documentation/manual/texturing/pbmchannels/ |
| 3DCoat: exportar texturas e workflows PBR (Roughness/Metalness) | Textures Menu | https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/ |
| 3DCoat: importar ID map bakeado no Blender | ID map | https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/ |
| 3DCoat: gravar luz na cor (hand-painted), bake de Geometry Info/curvatura | Light Baking Tool | https://3dcoat.com/documentation/manual/interface-and-navigation/edit-menu/light-baking-tool/ |
| 3DCoat: AppLink (referência; exige Modelling Room) | Blender applink | https://3dcoat.com/documentation/manual/getting-started/app-links/blender-applink/ |
| Lista oficial de vídeos (seções "3DCoatTextura Videos" e "Workflow with Other Apps") | Video Training Tutorials | https://3dcoat.com/documentation/training-tutorials/ |

### 2.3 Vídeos

| Vídeo | Autor | O que cobre | Link |
|---|---|---|---|
| Introduction to 3D Coat Textura — Part 1 | TheNerdForum | Interface do Textura e importação | https://www.youtube.com/watch?v=R59R-ughX80 |
| Introduction to 3D Coat Textura — Part 2 | TheNerdForum | Bake, materiais, exportação | https://www.youtube.com/watch?v=tdU_4JABm8M |
| Blender 3DCoat PBR Tutorial | (lista oficial) | Fluxo PBR entre Blender e 3DCoat | https://youtu.be/P1mMhLEm3vM |
| Blender Materials to 3DCoat PBR Smart Materials | (lista oficial) | Levar materiais do Blender para Smart Materials | https://youtu.be/T3Pz6nirci0 |
| Blender PBR Shader for 3DCoat Smart Materials | (lista oficial) | Conferir no Blender os mapas exportados do 3DCoat | https://youtu.be/tauzKbaSt88 |
| How to Export Plasticity Objects into 3D Coat… & then back into Blender | (lista oficial) | Ida e volta para o Blender (a parte 3DCoat → Blender é a que interessa) | https://www.youtube.com/watch?v=wc-2ZmodsuM |
| Texture UV Editor | Pilgway | Conferir e pintar no UV dentro do Paint Room | https://youtu.be/3xkB7lDsVDY |
| Mesh and Texture Resolution | Pilgway | Trocar a resolução de trabalho (512 em aula, 1024 na entrega) | https://youtu.be/jVCJtEejWOM |
| Game Asset Crash Course — Blender and 3D-Coat (Udemy, pago) | Concept Courses | O pipeline mais parecido com o da disciplina: Blender → Smart Materials → bake → Unity | https://www.udemy.com/course/game-asset-crash-course-3d-modeling-in-blender-and-3d-coat/ |

---

## 3. Roadmap de migração

Pré-requisito: já saber trabalhar no Substance Painter (camadas, máscaras, generators, exportação). O roadmap aproveita esse conhecimento e foca no que **muda**.

### Fase 0: base comum (≈ 4–6 h, obrigatória para as duas trilhas)

| Etapa | Objetivo | Exercício | Recurso |
|---|---|---|---|
| 0.1 Interface e importação | Abrir um FBX do Blender em Per-Pixel Painting e conferir o UV no Texture Editor | Importar um asset simples (barril ou caixa) | Intro to 3D Coat Textura, Partes 1 e 2 · [Per-Pixel Painting](https://3dcoat.com/documentation/manual/texturing/per-pixel-painting/) |
| 0.2 Camadas e canais | Entender Color, Depth, Gloss e Metalness numa mesma camada e os modos de mistura | Refazer no 3DCoat um material simples já feito no Substance | [GPU Texturing](https://3dcoat.com/documentation/manual/texturing/) · [Blending Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/) |
| 0.3 Generators → Condições | Calcular Curvature/AO e usar *More on Shadow*, *More on Convex* e *More on Top* | Fazer três camadas (sombra, borda, luz de cima) e testar com cores puras (vermelho, verde, azul) | [Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) |
| 0.4 Smart Materials | Criar, editar, prender (*Attach*) e aplicar com Fill, entendendo a lógica raster | Recriar um Smart Material simples do Substance (por exemplo, metal pintado com bordas gastas) | [Attach a Smart material](https://3dcoat.com/documentation/?p=6295) · vídeo [PBR Smart Materials](https://youtu.be/FXHAA8Q6wBg) |
| 0.5 Máscaras | Layer Mask × Clipping Mask × condição | Repetir o 0.3 usando clipping em vez de condição | [Layer and Clipping Masks](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/layer-and-clipping-masks/) |
| 0.6 Exportação | Exportar Roughness/Metalness e montar o material no Blender e na Unity | Abrir o asset da 0.4 no Blender (Principled BSDF) e na Unity (URP Lit) | [Textures Menu](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/) |

**O que desaprender do Substance:** esperar que mudar uma condição atualize o resultado sozinho (no fluxo clássico, limpe e preencha de novo); procurar a "black mask" em toda camada; trabalhar com dezenas de fill layers empilhadas (no 3DCoat, uma camada pode carregar vários canais de uma vez).

---

### Trilha A: Handpainted Texture (≈ 15–20 h)

Objetivo: textura **só de cor (albedo)**, com luz, sombra e volume pintados na própria textura. É o estilo WoW/Dota, para shaders unlit ou com pouca luz.

| Etapa | Foco | Exercício | Recursos |
|---|---|---|---|
| A1 Preparar o projeto | Desativar Depth, Gloss e Metalness no pincel; pintar só Color; visualização com pouca influência de luz | Esfera e cubo: pintar volume só com cor (luz em cima, sombra embaixo) | [Hand-painting in 3DCoat](https://3dcoat.com/articles/article/hand-painting-in-3dcoat/) |
| A2 Base de valores com condições | Usar o que veio do Substance: *More on Top* (luz), *More on Shadow*/*More on Concave* (sombra), *More on Convex* (highlight de borda) como **primeira passada**, depois repintada à mão | Base em 4 camadas: cor chapada → gradiente de luz → sombra de oclusão → highlight | [Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) |
| A3 Pincéis e alphas | Brush Options (jitter de cor e opacidade), alphas de pincelada, pressão da mesa digitalizadora | Pintar madeira estilizada (veios, bordas lascadas) | [Brushes general use](https://3dcoat.com/documentation/manual/brush-components/brushes-alphas/) · [Brush Options](https://3dcoat.com/documentation/manual/brush-components/brush-options/) |
| A4 Pintura no UV (2D) | Pintar no Texture Editor e corrigir costuras | Corrigir as costuras do asset da A3 | vídeo [Texture UV Editor](https://youtu.be/3xkB7lDsVDY) |
| A5 Luz gravada | **Light Baking Tool** para gravar a luz do Render Room na cor e repintar por cima | Gravar a luz em um prop e "quebrar" o resultado com pinceladas | [Light Baking Tool](https://3dcoat.com/documentation/manual/interface-and-navigation/edit-menu/light-baking-tool/) |
| A6 Projeto completo | Prop ou arma hand-painted do começo ao fim | Seguir um walkthrough completo e depois repetir com um asset próprio | [Create HANDPAINTED WoW style textures](https://www.youtube.com/watch?v=LAJchhRyuPA) · [Handpainted Sword Walkthrough](https://www.youtube.com/watch?v=y8w-M9ad0Ek) · [Tutorial Handpainted textures PART 3](https://www.youtube.com/watch?v=r--xIEZpp_Q) · Udemy: [Handpainted 3D Weapon Course](https://www.udemy.com/course/handpainted-3d-weapon-course/) |
| A7 Exportação | Exportar só Albedo e testar na Unity com shader **Unlit** (ou Lit com pouca luz) | Comparar o asset nos dois shaders | [Textures Menu](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/) |

**Critério de sucesso:** o asset "lê" volume e material **sem iluminação da engine**.

---

### Trilha B: PBR Stylized (≈ 15–20 h)

Objetivo: canais PBR completos (Albedo, Roughness, Metallic, Normal) com **formas e cores simplificadas**: tons saturados, desgaste exagerado e legível, Normal suave. É o estilo Fortnite/Overwatch/Sea of Thieves. É o caminho mais natural para quem vem do Substance.

| Etapa | Foco | Exercício | Recursos |
|---|---|---|---|
| B1 Base PBR | Valores de Roughness e Metalness plausíveis (Metalness quase binário), cores mais saturadas que no realista | Paleta de 4 materiais (madeira, metal, pedra, tecido) em esferas | [PBM Channels](https://3dcoat.com/documentation/manual/texturing/pbmchannels/) · [PBR texturing in 3D Coat (Jaakko)](https://creativewithjaakko.com/tutorials/pbr-texturing-in-3d-coat/) |
| B2 Generators estilizados | Condições com **Contrast alto** (transições recortadas) e bordas largas (*More on Convex* + *Cavity Width*) | Edge wear "cartoon" em um prop metálico | [Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) |
| B3 Normal pintado (Depth) | Pintar relevo estilizado (entalhes largos, chanfros falsos) no canal Depth em vez de height + anchors | Pedra estilizada com rachaduras grandes | Plano de Aula da Semana 7 · [Brushes general use](https://3dcoat.com/documentation/manual/brush-components/brushes-alphas/) |
| B4 Smart Materials próprios | Montar uma biblioteca de Smart Materials estilizados reaproveitáveis (é o "smart material da casa", como no Substance) | Criar 3 Smart Materials do tema do Kit Modular | vídeo [PBR Smart Materials](https://youtu.be/FXHAA8Q6wBg) · [Texturing Game Assets (timelapse)](https://www.youtube.com/watch?v=YF4bJczvoY0) |
| B5 Procedural com nós (2026) | `simple mask` + `material mix` + NGMasks: o mais próximo do fluxo **não destrutivo** do Substance | Refazer o edge wear da B2 com nós e comparar o tempo de iteração | [Texturing with nodes](https://3dcoat.com/documentation/2026/07/01/texturing-with-nodes/) · [NGMasks](https://3dcoat.com/documentation/manual/nodesystem/masks/) · [NGFilters](https://3dcoat.com/documentation/manual/nodesystem/filters/) |
| B6 Toque à mão | Pinceladas de cor por cima do PBR (variação de matiz, gradientes) | Adicionar variação pintada ao prop da B2 | [Stylized Wood Texturing — Handpaint PBR](https://www.youtube.com/watch?v=rDEx8ObtXtU) |
| B7 Exportação e engine | Preset da Unity (Roughness/Metalness), conferir o Normal (convenção OpenGL/DirectX) e montar o URP Lit | Asset final na Unity ao lado da versão no Render Room | [Textures Menu](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/) · Udemy: [Game Asset Crash Course](https://www.udemy.com/course/game-asset-crash-course-3d-modeling-in-blender-and-3d-coat/) |

**Critério de sucesso:** o material continua estilizado **com a iluminação da engine**. Roughness e Normal reforçam a leitura sem puxar para o realismo.

---

### Projeto de consolidação (as duas trilhas)

Texturizar o **mesmo asset** do Kit Modular nas duas trilhas (uma versão handpainted e outra PBR stylized) e comparar na Unity. Isso evidencia, para o portfólio e para a crítica, as decisões técnicas de cada abordagem.

## Pendências

- [ ] Confirmar na 2026 do laboratório: posição do seletor *Conditions*, painel NGMasks, Node Editor e máscara de camada.
- [ ] Testar se o AppLink funciona de alguma forma com o Textura (a documentação indica a Modelling Room).
- [ ] Gravar um vídeo curto próprio (5 min) de "Generator AO no 3DCoatTextura" para a turma, já que não há vídeo oficial sobre condições.
