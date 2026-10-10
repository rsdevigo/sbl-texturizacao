# Cursos e playlists — 3DCoatTextura para quem vem do Substance Painter

> Levantamento feito em outubro de 2026. Links, preços e datas de atualização mudam com frequência, então confira antes de indicar à turma.

---

## Leia antes: o que muda para quem vem do Substance

- **Não encontrei curso pago (Udemy ou similar) feito especificamente para quem migra do Substance Painter para o 3DCoatTextura.** A estratégia mais eficiente é usar o mapa de equivalências abaixo, depois os vídeos curtos oficiais da Pilgway e, por fim, um curso completo só para ver o fluxo de ponta a ponta.
- Quase todos os cursos usam o **3DCoat completo**. O 3DCoatTextura tem apenas o **Paint Room** e o **Render Room**. Pule as seções de Sculpt, Retopo, UV e Voxels: na disciplina, a modelagem e o UV são feitos no Blender.
- Boa parte do material foi gravada em versões antigas (2021–2024). Os conceitos de camadas, Smart Materials, bake de AO/Curvature e exportação continuam valendo, mas a interface muda. Os recursos novos da 2026 (texturização não destrutiva por nós, **NGMaterials/NGMasks**, 30 canais de material) ainda têm pouco tutorial publicado.

### Mapa de equivalências: Substance Painter → 3DCoatTextura

As equivalências são aproximadas e servem para orientar a busca nos vídeos. A lógica de cada ferramenta não é idêntica.

| No Substance Painter | No 3DCoatTextura | Observação para a migração |
|---|---|---|
| Texture Set / projeto | Projeto em **Per-Pixel Painting** (importar malha com UV) | É o modo usado na disciplina (Semana 7). |
| Bake de mesh maps (AO, Curvature, Normal…) | Cálculo de AO/Curvature no menu **Textures**, e bake a partir de high-poly | No Textura, o bake de high-poly para low-poly da disciplina é feito no Blender (Semana 11). |
| Fill Layer + Material | Camada com **Fill** ou **Smart Material** aplicado | No 3DCoat, o Smart Material pode ser "preso" à camada e ajustado depois. |
| Smart Material / Smart Mask / Generators | **Smart Materials** com condições (cavidade, AO, curvatura) e, na 2026, **NGMaterials/NGMasks** por nós | Equivalente mais próximo dos generators do Substance. |
| Máscaras de camada (black/white mask) | Máscaras de camada, **Clipping Mask** e camadas de máscara | O conceito é igual, mas os nomes e a posição no painel mudam. |
| Canais (Base Color, Roughness, Metallic, Height, Normal) | Canais **Color, Roughness, Metallic, Depth** (Depth gera o Normal na exportação) | Pintar relevo no **Depth** equivale a pintar Height no Substance. |
| Viewport Iray | **Render Room** | Use para avaliar o material antes de exportar. |
| Export Textures (presets Unity/Unreal) | **Export Textures** com construtor de presets | Monte e salve o preset da Unity usado na disciplina. |

---

## 1. Ponto de partida rápido (gratuito e oficial)

| Recurso | Formato | Por que indicar | Link |
|---|---|---|---|
| Canal oficial PILGWAY 3DCoat | YouTube | Fonte primária: vídeos de recursos novos de cada versão, incluindo a 2026. | https://www.youtube.com/c/PILGWAY3DCoat/featured |
| Página de tutoriais do 3DCoatTextura | Site oficial | Lista curada pela própria Pilgway para a edição Textura. | https://pilgway.com/tutorials/3dcoattextura |
| Playlist **Quick Start: Paint Workspace** | YouTube (playlist) | Introdução curta ao Paint Room. É a primeira coisa a assistir. | https://www.youtube.com/watch?v=xssClRNzVzQ&list=PLvD5VNbc8nSPgUgFTMJn_ahAbUVFeTmTF |
| Playlist **Paint Workspace** | YouTube (playlist) | Aprofunda as ferramentas do espaço de pintura. | https://www.youtube.com/watch?v=2ywZ_5K9OLU&list=PLlQ3JITh9bXOuaUh9D48o_i0l_HqGLFt4 |
| Playlist **Paint Tools** | YouTube (playlist) | Pincéis, preenchimento e ferramentas de pintura em um projeto prático. | https://www.youtube.com/watch?v=1LFEOSBraJ0&list=PLlQ3JITh9bXMvBlrpIqwB-CcnJiIfwHxN |
| **PBR Smart Materials** (Phil Nolan) | YouTube | Equivalente direto dos Smart Materials do Substance: parâmetros e personalização. | https://youtu.be/FXHAA8Q6wBg?list=PLlQ3JITh9bXOcshH7ALiXsMJlP4hrZjd4 |
| **PBR Preview Options** | YouTube | Configuração da visualização PBR (equivale a ajustar o viewport do Substance). | https://youtu.be/kkUGC7A4DhU?list=PLlQ3JITh9bXOcshH7ALiXsMJlP4hrZjd4 |
| Documentação oficial | Site | Referência de menus. Tem navegação em português, mas parte do conteúdo continua em inglês. | https://3dcoat.com/documentation/ |

## 2. Específico do 3DCoatTextura

| Recurso | Autor | Conteúdo | Link |
|---|---|---|---|
| Introduction to 3D Coat Textura — Part 1 | TheNerdForum | Interface e aplicação de normais. | https://www.youtube.com/watch?v=R59R-ughX80 |
| Introduction to 3D Coat Textura — Part 2 | TheNerdForum | Bake, materiais e seam strips. | https://www.youtube.com/watch?v=tdU_4JABm8M |
| 3DCoat Textura Overview | askNK | Visão geral da edição Textura. | https://www.youtube.com/watch?v=C0OxAx2yfnI |
| 3D Coat TEXTURA review: Better Than Substance Painter in 2025? | YouTube | Comparação direta com o Substance. Bom para alinhar expectativas de quem está migrando. | https://www.youtube.com/watch?v=M9o12dpiEbc |

## 3. Fluxo de texturização de game assets (prática guiada)

Esses vídeos mostram o processo completo em um asset. São úteis para ver na prática como Smart Materials e máscaras substituem o fluxo de camadas do Substance.

| Recurso | Autor | Foco | Link |
|---|---|---|---|
| Texturing Game Assets (timelapse) | TheNerdForum | Rádio militar texturizado com Smart Materials. | https://www.youtube.com/watch?v=YF4bJczvoY0 |
| Texturing Metal Door | TheNerdForum | Normal Map, bake de AO e ferrugem. Relaciona-se às Semanas 7–9. | https://www.youtube.com/watch?v=jTWiOYZgi_w |
| Texturing Sci-Fi Security Keypad | TheNerdForum | Aplicação de materiais PBR. | https://www.youtube.com/watch?v=PYlLPuTRqR0 |
| Create Handpainted WoW Style Textures with 3DCOAT | hart | Pintura hand-painted completa. Indicado para a trilha estilizada. | https://www.youtube.com/watch?v=LAJchhRyuPA |
| Using Reference Images | Pilgway | Uso de referências durante a pintura. | https://youtu.be/fiAO5uO2m7E?list=PLlQ3JITh9bXOcshH7ALiXsMJlP4hrZjd4 |
| Baking in 3DCoat 2025 | Pilgway | Bake de Normal Map. Usa recursos do 3DCoat completo, então serve como referência conceitual. | https://youtu.be/sW12MztTcCM |

## 4. Cursos completos (Udemy)

Nenhum destes cursos é feito para o Textura. Use apenas as seções de pintura, bake e exportação.

| Curso | Instrutor | Duração / atualização | O que aproveitar | Link |
|---|---|---|---|---|
| **Intro to 3D Coat: From Noob to Cook** | Anton Tenitsky | 8h05, atualizado em out/2024, nota 4,2 | Seções de bake, pintura e PBR. Pule sculpt e retopo. É o curso mais recente e completo encontrado. | https://www.udemy.com/course/intro-to-3d-coat-from-noob-to-cook/ |
| **Game Asset Crash Course — 3D Modeling in Blender and 3D-Coat** | Concept Courses / Timothy Trankle | 2h29, atualizado em abr/2019, nota 4,5 | É o pipeline mais próximo da disciplina: Blender → Smart Materials no 3DCoat → bake → Unity. A interface está defasada. | https://www.udemy.com/course/game-asset-crash-course-3d-modeling-in-blender-and-3d-coat/ |
| **Handpainted 3D Weapon Course [FULL WORKFLOW]** | Romans Busels | 7h05, atualizado em nov/2023, nota 4,6 | Pintura hand-painted no 3DCoat. Indicado para a trilha estilizada. | https://www.udemy.com/course/handpainted-3d-weapon-course/ |
| Simple Game Ready Asset Creation in 3D Coat | Robert Alvord | 2h11, atualizado em jun/2014 | Apenas histórico: interface muito antiga. Não recomendado como primeira opção. | https://www.udemy.com/course/simple-game-ready-asset-creation-in-3d-coat/ |

Alternativa fora da Udemy: **Intro to 3D Coat: Noob to Cook** (mesmo autor, Anton Tenitsky), vendido no Gumroad. Confira se o conteúdo é o mesmo da versão Udemy antes de comprar. Link: https://tenitsky.gumroad.com/l/intro3dcoat

---

## Trilha sugerida de estudo (≈6–8 h) para quem já domina o Substance

1. **Mapa de equivalências** (acima, 15 min): ajuda a não procurar no 3DCoat o botão que existia no Substance.
2. **Quick Start: Paint Workspace** + **Introduction to 3D Coat Textura, Partes 1 e 2** (≈1 h): interface, importação e bake.
3. **PBR Smart Materials** + **PBR Preview Options** (≈30 min): o equivalente aos Smart Materials do Substance.
4. **Texturing Metal Door** ou **Texturing Game Assets** (≈1 h): o fluxo completo em um asset.
5. **3D Coat TEXTURA review** (≈20 min): vantagens e limites em relação ao Substance.
6. **Intro to 3D Coat: From Noob to Cook**, só as seções de pintura, bake e exportação (≈3–4 h).
7. Recursos novos da 2026 (NGMaterials/NGMasks): acompanhe no canal oficial, porque ainda há poucos tutoriais de terceiros.

## Pendências

- [ ] Assistir aos vídeos do item 2 e confirmar se a interface bate com o 3DCoatTextura 2026 instalado no laboratório.
- [ ] Buscar tutoriais em português (não encontrei playlists consolidadas em PT-BR no levantamento).
- [ ] Atualizar esta lista quando a Pilgway publicar tutoriais oficiais de NGMaterials/NGMasks.
