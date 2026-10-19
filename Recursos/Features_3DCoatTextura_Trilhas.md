# Features do 3DCoatTextura 2026 por trilha visual

> Material de apoio publicado no site, no menu **Recursos**.
> Reúne **só as features do 3DCoat** citadas no [Guia_Migracao_Substance_3DCoatTextura.md](/Recursos/Guia_Migracao_Substance_3DCoatTextura.md), com a documentação oficial, um vídeo de referência e o uso em cada trilha.
> Levantamento feito em outubro de 2026. Vários vídeos foram gravados em versões anteriores à 2026: o conceito vale, mas a interface pode estar diferente.

**As três trilhas**

- **PBR Fotorrealista:** a trilha fotorrealista da disciplina. Base fotográfica (textura seamless da Semana 6), valores PBR físicos, desgaste plausível.
- **PBR Estilizado:** canais PBR completos, com formas e cores simplificadas, contraste alto e desgaste legível.
- **Handpainted:** só cor (albedo), com luz, sombra e volume pintados na textura. Shader unlit ou com pouca luz.

---

## 1. Preparação e projeto

| Feature | Documentação | Vídeo | PBR Fotorrealista | PBR Estilizado | Handpainted |
|---|---|---|---|---|---|
| **Importação para Per-Pixel Painting** (malha com UV vinda do Blender) | [Importing into the Painting Room](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/) | [Quick Start: Paint Workspace](https://www.youtube.com/watch?v=xssClRNzVzQ&list=PLvD5VNbc8nSPgUgFTMJn_ahAbUVFeTmTF) | Importar em workflow Roughness/Metalness, 1024² | Igual ao fotorrealista | Importar normalmente; depois trabalhar só no canal Color |
| **Mesh and Texture Resolution** | [Textures Menu](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/) | [Mesh and Texture Resolution](https://youtu.be/jVCJtEejWOM) | 512² em aula, 1024² na entrega | Igual | Resolução maior ajuda nas pinceladas finas. Testar 2048² se o laboratório aguentar |
| **Texture UV Editor** | [Textures Menu](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/) | [Texture UV Editor](https://youtu.be/3xkB7lDsVDY) | Conferir o UV e o alinhamento da foto | Conferir o UV | **Ferramenta central:** pintar em 2D e corrigir costuras |
| **Calculate Curvature / Calculate Occlusion** (mapas da malha) | [Cavity and Curvature maps](https://3dcoat.com/documentation/manual/interface-and-navigation/edit-menu/cavity-and-curvature-maps/) | [Cavity Masking and Painting](https://youtu.be/6Fmks8pjcvw) | Base para desgaste físico e sombra de contato | Base para edge wear exagerado | Base para a primeira passada de luz e sombra, depois repintada à mão |

## 2. Camadas e canais

| Feature | Documentação | Vídeo | PBR Fotorrealista | PBR Estilizado | Handpainted |
|---|---|---|---|---|---|
| **Camadas e canais PBR** (Color, Depth, Gloss/Roughness, Metalness na mesma camada) | [The Layers Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/) · [PBM Channels](https://3dcoat.com/documentation/manual/texturing/pbmchannels/) | [PBR Painting](https://www.youtube.com/watch?v=sl_to5rIjaA) | Todos os canais com valores físicos (Metalness 0 ou 1) | Todos os canais, com cores mais saturadas e Roughness mais uniforme | **Só Color.** Depth, Gloss e Metalness desligados no pincel |
| **Canal Depth** (pintura de relevo que vira Normal na exportação) | [PBM Channels](https://3dcoat.com/documentation/manual/texturing/pbmchannels/) | [Surface Painting](https://www.youtube.com/watch?v=MnOUPX5aw84) | Micro-detalhe: trincas, riscos, poros | Relevo largo e suave: entalhes, chanfros falsos | Não usado. O volume é pintado na cor |
| **Painel de Blending** (modos de mistura, opacidade por canal, Brightness/Contrast) | [The Blending Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/) | [Layer Blending Pop-Up](https://youtu.be/kJdowazoD6Y) | Multiply/Overlay com opacidade baixa para sujeira e AO | Multiply para sombra recortada, Screen para highlights | Multiply (sombra) e Screen/Add (luz) em camadas separadas de pintura |
| **Layer Mask e Clipping Mask** (inclui *Clip Mask Layer*) | [Layer and Clipping Masks](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/layer-and-clipping-masks/) | [Layer and Clipping masks (3DCoat e Textura)](https://www.youtube.com/watch?v=GpNVNtZzh1A) | Restringir desgaste e sujeira a áreas específicas sem destruir a camada | Mesmo uso. Clipping para pintar detalhes só dentro de uma cor base | **Clipping mask** para pintar luz e sombra só dentro de cada área de cor |
| **Pastas de camadas** (group folders) | [The Layers Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/) | [Paint Layer Groups](https://youtu.be/3kDlcThy_Sk) | Organizar por material (metal, madeira) e por tipo de detalhe | Igual. Na 2026, aplicar material ou máscara de nó à pasta | Organizar por etapa: base, sombra, luz, detalhes |

## 3. Generators, materiais e máscaras

| Feature | Documentação | Vídeo | PBR Fotorrealista | PBR Estilizado | Handpainted |
|---|---|---|---|---|---|
| **Conditions** (*More on Shadow*, *More on Convex*, *More on Top*…) | [Conditions (Height/Color) Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/) | [Conditions Painting quick start](https://youtu.be/edGevw9i9R0) | Sujeira em reentrâncias (*More on Concave/Shadow*), desgaste em arestas (*More on Convex*) com Contrast baixo | Mesmas condições com **Contrast alto** (transição recortada) | Primeira passada de luz (*More on Top*), sombra (*More on Shadow*) e highlight (*More on Convex*), depois repintada |
| **Smart Materials** (editor, condições por camada, biblioteca) | [Smart Materials](https://3dcoat.com/documentation/library/smart-materials/) | [Quick Start Smart Materials](https://www.youtube.com/watch?v=5ytMWisvEag) | Materiais físicos (ferrugem, metal pintado, pedra) da biblioteca ou próprios | Biblioteca própria de materiais estilizados do tema do kit | Pouco usado. No máximo como base de cor por condição |
| **Attach + Fill** (prender o material à camada e aplicar) | [Attach a Smart material to a layer](https://3dcoat.com/documentation/?p=6295) · [Layers menu (*Fill Entire Layer*)](https://3dcoat.com/documentation/manual/interface-and-navigation/layers-menu/) | [Adjustments to Paint Layers](https://youtu.be/yZm79zFPH28) | Aplicar e iterar materiais (limpar e preencher de novo a cada ajuste de condição) | Igual | Fill de cor chapada como base de cada área |
| **Node System: `SimpleMask` + `MaterialMix`** (generator procedural) | [Node Editor](https://3dcoat.com/documentation/manual/nodesystem/node-editor/) · [Material nodes](https://3dcoat.com/documentation/manual/nodesystem/gpu-nodes/material/) · [Texturing with nodes](https://3dcoat.com/documentation/2026/07/01/texturing-with-nodes/) | [Rock texturing timelapse (Node System)](https://www.youtube.com/watch?v=Tz8AZEKak5s) | Desgaste não destrutivo com noise realista no *degree map* | **Trilha que mais ganha:** edge wear e sujeira estilizados ajustáveis em tempo real | Opcional: gerar a base de luz e sombra para repintar |
| **NGMasks** (presets: Dirt, Rust, Scratches, Fabric/Wood/Leather, Patterns) | [NGMasks](https://3dcoat.com/documentation/manual/nodesystem/masks/) | [Rock texturing timelapse (Node System)](https://www.youtube.com/watch?v=Tz8AZEKak5s) (sem vídeo oficial específico até o levantamento) | Dirt, Rust e Scratches com parâmetros realistas | Os mesmos presets com contraste alto e escala maior | Pouco usado |
| **NGFilters e Adjust** (filtros de camada: HSV, Levels, Posterize, Brightness/Contrast) | [NGFilters](https://3dcoat.com/documentation/manual/nodesystem/filters/) · [Color nodes](https://3dcoat.com/documentation/manual/nodesystem/gpu-nodes/color-nodes/) | [Adjust](https://youtu.be/1JTdHK-bxPg) | Correção de cor da foto base (HSV, Levels) | **Posterize** e HSV para achatar e saturar a paleta | Ajuste final de matiz e saturação; Posterize para testar a leitura de valores |
| **Importação de ID map** (*Textures → Import Layers Colors*) | [ID map](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/id-map/) | [RGB Masks in 3DCoat](https://youtu.be/XVeuHeDX3Z0) (o mais próximo; não há vídeo oficial de ID map) | Separar materiais de um asset complexo (Semana 12) | Igual | Separar as áreas de cor base |

## 4. Pintura

| Feature | Documentação | Vídeo | PBR Fotorrealista | PBR Estilizado | Handpainted |
|---|---|---|---|---|---|
| **Pincéis e Alphas** | [Brushes general use](https://3dcoat.com/documentation/manual/brush-components/brushes-alphas/) | [Installing Brush Alphas](https://youtu.be/6RLhjYu1Y1w) | Alphas fotográficos de trinca, arranhão e poro | Alphas de formas simples e bordas limpas | **Ferramenta central:** alphas de pincelada, pressão da mesa |
| **Brush Options** (jitter de cor e opacidade, rotação, espaçamento, curvas) | [Brush Options panel](https://3dcoat.com/documentation/manual/brush-components/brush-options/) | [Creating Custom Brush Curves](https://youtu.be/GFFJUTEpv-g) | Jitter sutil para quebrar repetição | Jitter moderado | **Essencial:** jitter de matiz e brilho para variação de cor |
| **Stencils** (projeção de imagem e máscara) | [Stencil & Material preview panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/mask-material-preview-panel/) | [2D Gizmo](https://youtu.be/pxINVJVbDns) | Projetar fotos e decalques realistas (Semana 10) | Símbolos e padrões gráficos do tema | Guias de forma (ornamentos), pintados por cima |
| **Light Baking Tool** (gravar luz na cor; também curvatura local e thickness) | [Light Baking Tool](https://3dcoat.com/documentation/manual/interface-and-navigation/edit-menu/light-baking-tool/) | [Light Baking Tool](https://youtu.be/ZDwyvAj0Wag) | *Thickness* e *Local Curvature* como máscaras extras | *Local Curvature* para bordas mais precisas | **Essencial:** gravar a luz do Render Room na cor e repintar por cima |

## 5. Visualização e exportação

| Feature | Documentação | Vídeo | PBR Fotorrealista | PBR Estilizado | Handpainted |
|---|---|---|---|---|---|
| **Render Room** (HDR, iluminação, pós-efeitos) | [Render](https://3dcoat.com/documentation/manual/workspaces-rooms/render/) | [Render room, intro to 3DCoat](https://youtu.be/QbBYmVFkZ5Y) | Avaliar com HDR realista antes de exportar | Avaliar com HDR neutro, de perto e de longe | Avaliar com pouca luz ou luz plana, que se aproxima do unlit |
| **PBR Preview Options** | [Smart Materials (vídeos)](https://3dcoat.com/documentation/library/smart-materials/) | [PBR Preview Options](https://youtu.be/kkUGC7A4DhU) | Conferir Roughness e Metalness isolados | Igual | Pouco relevante |
| **Exportação de texturas** (presets, workflow Roughness/Metalness) | [Exporting from the Painting Room](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/exporting-from-the-paint-room/) · [Textures Menu](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/) | [New Export Dialog](https://youtu.be/CnqLfhc_n_Q) | Albedo, Roughness, Metallic, Normal (e ORM na Semana 15) | Os mesmos mapas | **Só Albedo**, com shader Unlit na Unity |

---

## 6. Um vídeo de referência por trilha

Vídeos do processo completo, para assistir antes de começar cada trilha.

| Trilha | Vídeo principal | Por que este | Complementar |
|---|---|---|---|
| **PBR Fotorrealista** | [Texturing Metal Door](https://www.youtube.com/watch?v=jTWiOYZgi_w) (TheNerdForum) | Normal, bake de AO e ferrugem em um asset de jogo. É o mais próximo das Semanas 7–9 | [PBR texturing in 3D Coat Tutorial](https://www.youtube.com/watch?v=PrjgZgUuIMA) · [Arid Arch Tutorial](https://www.youtube.com/watch?v=8IC7JK8fYuo) |
| **PBR Estilizado** | [Stylized Wood Texturing — Handpaint PBR](https://www.youtube.com/watch?v=rDEx8ObtXtU) | Mostra o meio-termo entre PBR e pintura à mão, a base do estilo | [Texturing Game Assets (timelapse)](https://www.youtube.com/watch?v=YF4bJczvoY0) · [Rock texturing com nós](https://www.youtube.com/watch?v=Tz8AZEKak5s) |
| **Handpainted** | [Create HANDPAINTED WoW style textures with 3DCOAT](https://www.youtube.com/watch?v=LAJchhRyuPA) | Processo completo hand-painted, da base ao acabamento | [Handpainted Sword Walkthrough](https://www.youtube.com/watch?v=y8w-M9ad0Ek) · [Tutorial Handpainted textures PART 3](https://www.youtube.com/watch?v=r--xIEZpp_Q) |

---

## 7. Resumo: features essenciais por trilha

| Trilha | Essenciais | Secundárias | Pouco usadas |
|---|---|---|---|
| **PBR Fotorrealista** | Calculate Curvature/Occlusion · Conditions · Smart Materials · Canal Depth · Stencils · Exportação | NGMasks · NGFilters · Pastas · ID map | Light Baking (gravar luz na cor) |
| **PBR Estilizado** | Conditions (Contrast alto) · Smart Materials próprios · Node System (`SimpleMask`) · Canal Depth · Exportação | NGFilters (Posterize/HSV) · Brush Options · Stencils | Alphas fotográficos |
| **Handpainted** | Pincéis e Alphas · Brush Options · Texture UV Editor · Clipping Mask · Light Baking Tool | Conditions (primeira passada) · NGFilters/Adjust | Canal Depth · Gloss/Metalness · NGMasks · Smart Materials |

## Pendências

- [ ] Alguns vídeos foram associados pela página da documentação onde aparecem (ex.: *2D Gizmo* para Stencils, *Surface Painting* para o canal Depth). Assistir e confirmar se cobrem o recurso como esperado.
- [ ] Substituir os vídeos de versões antigas por vídeos oficiais da 2026 à medida que a Pilgway publicar (principalmente NGMasks e Node System).
