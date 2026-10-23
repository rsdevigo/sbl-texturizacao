# Tutorial 0 — Primeiros passos no 3DCoatTextura

20/10/2026 · Rodrigo

> Faça este tutorial **antes** dos tutoriais de Smart Material. Ele cobre o mínimo para trabalhar no programa: interface, importação, camadas, pincel, Smart Material pronto e exportação para a Unity.
> Os nomes de menus do 3DCoatTextura mudam entre versões. Se alguma opção não estiver no lugar indicado, confira na versão 2026 instalada no laboratório e anote a diferença para a turma.

## Visão geral

O 3DCoatTextura é a versão do 3DCoat só para texturização. Ele tem **duas salas**: a **Paint Room**, onde se pinta e se monta o material, e a **Render Room**, onde se ilumina e se confere o resultado. Na versão 2026.11, ele também tem o **Node Editor**, onde ficam os materiais e máscaras em nós (*NGMaterials* e *NGMasks*). Ele **não** tem salas de modelagem, escultura nem UV. Por isso, tudo que é malha e UV precisa sair pronto do Blender.

**A ideia que mais confunde no começo:** no 3DCoatTextura, a camada só existe **onde você pintou ou preencheu**. Não há uma camada que cobre o objeto inteiro com uma máscara recortando (como no Substance Painter). E o preenchimento com condição (borda, cavidade, sombra) é calculado **uma vez, no clique**. Se você mudar a condição depois, precisa limpar a camada e preencher de novo.

**Quando usar:** Semana 7 (migração do Hero Asset Referência para o 3DCoatTextura). Serve de base para as Semanas 8 a 10 e para os tutoriais de Smart Material.

**Pré-requisitos**

- Hero Asset Referência com UV aprovado (Semanas 4 e 5).
- Blender e 3DCoatTextura 2026 instalados. Unity com URP.
- Ter lido o [Guia de Migração Substance → 3DCoatTextura](/Recursos/Guia_Migracao_Substance_3DCoatTextura.md), seção 0.

**Resultado esperado:** o Hero Asset aberto no 3DCoatTextura com pelo menos três canais ativos (Color, Roughness e Normal via Depth), salvo em `.3b`, exportado com o preset da Unity e montado num material URP Lit.

**Tempo estimado:** um encontro completo (demonstração + estúdio) para as Etapas 1 a 6, e o segundo encontro da semana para as Etapas 7 a 9.

## Etapa 1 — Preparar o arquivo no Blender

O 3DCoatTextura não conserta malha nem UV. Ele só **recebe** o que o Blender entrega. Quase todo problema das primeiras aulas nasce aqui.

1. **Confira o UV.** Um único mapa de UV, ativo, dentro do quadrado 0–1 e sem sobreposição (a não ser que ela seja intencional).
   - *Por quê:* sem UV Room, o 3DCoatTextura não tem como abrir ou corrigir UV. Ilhas sobrepostas fazem a pintura aparecer em dois lugares e estragam o cálculo de AO e curvatura.
2. **Aplique modificadores e transformações.** Aplique Mirror, Bevel e Array, depois `Ctrl+A → All Transforms`. Confira o UV de novo depois de aplicar.
   - *Por quê:* o UV que vale é o de depois dos modificadores. Escala não aplicada faz o modelo chegar gigante, minúsculo ou girado.
3. **Defina as normais.** Marque as *sharp edges* ou use *Auto Smooth* / *Smooth by Angle*.
   - *Por quê:* normais mal definidas criam manchas no AO e na curvatura, que vão aparecer em todas as máscaras depois.
4. **Exporte em FBX, só a low-poly.** *File → Export → FBX*, com *Selected Objects* marcado.
   - *Por quê:* o FBX leva malha, UV e normais num arquivo só. Mapas assados (Normal, AO, ID) vão como imagens separadas.

Casos especiais (trim sheet, vários materiais, duas camadas de UV) estão nos [Cenários de exportação](/Recursos/Cenarios_Exportacao_Blender_3DCoatTextura.md).

**Evidência:** o FBX abre de novo no Blender (*File → Import → FBX*) no tamanho e na orientação certos, com o UV intacto.

## Etapa 2 — Conhecer a interface

Antes de pintar, gaste dez minutos só navegando. Quem não domina a câmera pinta torto e se frustra.

1. **Identifique as salas.** As abas no topo da janela trocam de sala: *Paint* e *Render*.
   - *Por quê:* a Paint Room é onde 90% do trabalho acontece. A Render Room serve para conferir o material sob outra luz e para montar a luz que será assada nos tutoriais de Smart Material.
2. **Aprenda a câmera.** No padrão do 3DCoatTextura, arraste no **espaço vazio** em volta do modelo: botão esquerdo gira, botão direito aproxima e o botão do meio desloca. Sobre o modelo, use as mesmas combinações segurando `Alt`.
   - Se preferir a navegação do Blender, use a opção *Customize Navigation* (a documentação oficial tem o guia *Customize Navigation as Blender*). Combine com o grupo um padrão único, para que um possa ajudar o outro.
   - *Por quê:* no 3DCoatTextura, o clique sobre o modelo pinta. Girar a câmera sem querer pintar exige saber onde clicar.
3. **Localize os painéis.** Encontre e, se necessário, abra pelo menu *Windows → Panels*:
   - **Layers** (camadas);
   - **Smart Materials** (biblioteca de materiais);
   - **Brushes** e **Alphas** (formato do pincel);
   - **Color** (paleta e seletor de cor);
   - a **barra superior de ferramentas**, onde ficam raio, intensidade e os botões de canal (Color, Depth, Roughness/Gloss, Metalness).
   - *Por quê:* esses cinco lugares concentram quase todas as decisões. Os outros painéis podem ficar fechados por enquanto.
4. **Salve o layout.** Arrume os painéis e salve o espaço de trabalho (*Windows → Store Workspace*; para recuperar, *Windows → Restore Workspace*).
   - *Por quê:* nos computadores do laboratório, a interface costuma voltar ao padrão. Um layout salvo poupa tempo no começo de cada aula.

**Evidência:** girar, aproximar e deslocar a câmera sem deixar nenhuma pincelada no modelo.

## Etapa 3 — Importar o modelo

1. **Abra o modelo para pintura por pixel.** Em *File → Import → Model for Per Pixel Painting* (ou a opção equivalente na tela inicial), selecione o FBX.
   - *Por quê:* o modo Per-Pixel pinta direto nas texturas, usando o UV que veio do Blender. É o modo que gera mapas prontos para a Unity.
2. **Ajuste a janela de importação:**
   - **UV-mapping type:** manter o UV do arquivo (*Keep UV*), sem deixar o programa gerar um UV novo.
   - **Texture width** e **Texture height:** 1024 × 1024 para a entrega. Em aula, 512 deixa o computador mais leve e pode ser aumentada depois em *Textures → Mesh and Texture Resolution*.
   - **Z-up coordinate system**, se o modelo chegar deitado.
   - *Por quê:* a resolução decide o detalhe que a textura aguenta. Trocar no meio do trabalho é possível, mas costuma exigir conferir tudo de novo. O workflow PBR (*Roughness/Metalness*, o padrão da Unity) é escolhido na exportação (Etapa 8).
3. **Confira o UV dentro do 3DCoatTextura.** Abra o *Texture UV Editor* (menu *Textures*) e compare com o UV do Blender.
   - *Por quê:* se o UV chegou diferente, é melhor descobrir agora do que depois de uma hora de pintura.

**Evidência:** print do modelo na Paint Room ao lado do Texture UV Editor, com as mesmas ilhas do Blender.

## Etapa 4 — Camadas e canais

No 3DCoatTextura, uma única camada guarda vários canais ao mesmo tempo: cor, relevo, rugosidade e metal. É diferente do Substance, onde se empilham várias camadas, cada uma com uma função.

1. **Crie uma camada nova** no painel Layers e dê um nome com número e função (`01 Base`, `02 Sombra`, `03 Borda`).
   - *Por quê:* nomes claros tornam a pilha legível para o grupo e para a crítica. É o mesmo padrão usado nos tutoriais de Smart Material.
2. **Teste os canais um por um.** Na barra superior, deixe ligado só o canal **Color** e dê uma pincelada. Desfaça (`Ctrl+Z`), ligue só o **Depth** e pinte de novo. Repita com Roughness/Gloss e Metalness.
   - *Por quê:* o pincel pinta todos os canais ligados de uma vez. O erro mais comum no começo é pintar relevo ou metal sem querer, porque o canal ficou ligado.
   - O **Depth** cria relevo. Na exportação, ele vira o **Normal Map**. É assim que o Hero Asset ganha Normal na Semana 7, sem precisar de high-poly.
3. **Experimente opacidade e modo de mistura.** No painel *Layer Blending* (botão direito na camada → *Layer Blending*), mude a opacidade e teste os modos *Multiply*, *Screen* e *Overlay*.
   - *Por quê:* os tutoriais de Smart Material usam esses três modos o tempo todo (sombra em Multiply, luz em Screen ou Overlay).
4. **Use a visibilidade e o "solo".** Clique no olho para esconder uma camada e use `Alt+clique` no olho para ver só ela.
   - *Por quê:* desligar camadas uma a uma é a forma mais rápida de achar um problema. Também é o roteiro da crítica coletiva.

**Evidência:** uma camada só com cor e outra só com relevo, que somem e voltam ao clicar no olho.

## Etapa 5 — O primeiro pincel e o Fill

1. **Escolha um pincel e um alpha.** No painel Brushes, pegue um pincel redondo simples. No painel Alphas, escolha um formato suave.
   - *Por quê:* o alpha é o formato da ponta do pincel. Um alpha suave perdoa mais e é melhor para aprender.
2. **Ajuste raio e intensidade na barra superior** e pinte algumas pinceladas de cor no modelo.
   - *Por quê:* raio e intensidade são os dois controles que você vai mexer o tempo todo. Vale saber onde ficam antes de qualquer outra coisa.
3. **Teste o Fill.** Escolha a ferramenta de preenchimento (*Fill*) e clique no modelo para preencher uma camada inteira com uma cor.
   - *Por quê:* a cor base de todo material começa com um Fill. Depois disso, condições e pincéis trabalham por cima.

**Evidência:** uma camada de cor base preenchida e outra com pinceladas por cima, com nomes claros.

## Etapa 6 — Calcular AO e curvatura

As condições do 3DCoatTextura (borda, cavidade, sombra) leem dois mapas calculados a partir da malha: oclusão de ambiente (AO) e curvatura. Sem eles, os Smart Materials não sabem onde aplicar cada tom.

1. **Calcule os mapas.** Em *Edit → Calculate Occlusion and Curvature maps*.
   - *Por quê:* esses cálculos são o equivalente aos *generators* do Substance. Eles são feitos uma vez por modelo e servem para todas as camadas.
2. **Teste as condições com cores puras.** Crie três camadas e preencha com *Fill* usando condições diferentes: vermelho em *More on Convex* (bordas), azul em *More on Concave* (cavidades) e verde em *More on Shadow* (áreas fechadas).
   - *Por quê:* cores puras mostram exatamente onde cada condição age. Depois fica fácil trocar pelas cores do material.

**Evidência:** print com as três cores. Vermelho nas quinas, azul nas frestas, verde nas áreas escondidas.

Os detalhes (intensidade local × longo alcance, Cavity RGB, Thickness) estão na Etapa 1 do [Tutorial geral de Smart Material](/Tutoriais/Tutorial_Smart_Material_Diffuse_3DCoat.md).

## Etapa 7 — Usar um Smart Material pronto: Attach + Fill

Um Smart Material é um material de várias camadas, cada uma com sua condição. Ele não é aplicado com um clique só: primeiro você o **prende** à camada (*Attach to the current layer*) e depois **aplica** com Fill ou pincel.

> **Regra prática:** *Attach* define **o quê** (qual material). *Fill* ou pincel define **onde**.

1. **Crie uma camada nova** chamada `10 Smart Material – teste`.
   - *Por quê:* aplicar o material numa camada separada deixa comparar e apagar sem perder o resto.
2. **Escolha um material na biblioteca.** No painel Smart Materials, escolha um material pronto (por exemplo, um metal pintado ou uma madeira).
3. **Prenda o material (Attach).** Com a camada nova selecionada, clique com o botão direito no material na biblioteca → *Attach to the current layer*. Confira se ele aparece no painel *Material Preview*.
   - No 3DCoatTextura 2026.11, os materiais padrão da biblioteca são *NGMaterials* (em nós). Para eles, basta **clicar** no material para que ele vire o material ativo da ferramenta, ou **arrastá-lo** sobre o modelo ou a camada. Se o *Attach to the current layer* não aparecer no menu de um material, é porque ele é um NGMaterial.
   - *Por quê:* sem o Attach, o Fill usa só a cor escolhida no painel Color, e o resultado parece um balde de tinta.
4. **Aplique com Fill.** Com a ferramenta Fill, clique no modelo, ou use o comando de preencher a camada inteira no menu *Layers → Fill Entire Layer*.
   - *Por quê:* o Fill calcula as condições do material sobre o AO e a curvatura da Etapa 6 e grava o resultado na camada.
5. **Mude um parâmetro e refaça.** Abra o material no *Smart Material Editor*, mude a cor de uma camada interna, **limpe a camada** (botão direito na camada → *Make Transparent*) e preencha de novo.
   - *Por quê:* é aqui que se aprende a lógica raster. O resultado **não** se atualiza sozinho. Quem não limpa a camada empilha duas versões do material.
6. **Pinte com o material.** Em vez de Fill, use um pincel com o Smart Material preso para aplicá-lo só em uma área (um desgaste localizado, por exemplo).
   - *Por quê:* o mesmo material serve para preenchimento total e para retoque à mão. Na Semana 9 (pintura de desgaste), esse uso é central.

**Evidência:** dois prints do mesmo modelo, antes e depois de mudar o material e refazer o Fill.

## Etapa 8 — Salvar e exportar

1. **Salve o projeto em `.3b`.** *File → Save As*, com nome no padrão `Sobrenome_HeroAsset_v01.3b`. Aumente a versão a cada sessão.
   - *Por quê:* o `.3b` guarda camadas, materiais e condições. As texturas exportadas não guardam. Sem o `.3b`, não dá para corrigir nada depois da crítica.
2. **Exporte as texturas com o preset da Unity.** Em *File → Export → Objects & Textures*, escolha o preset da **Unity** (workflow *Roughness/Metalness*) e a resolução 1024.
   - *Por quê:* o preset já monta os mapas no formato que a Unity espera, por exemplo a suavidade (*smoothness*) no canal alfa do Metallic.
3. **Confira os arquivos na pasta.** Devem existir, no mínimo: cor (Albedo/Base Color), Metallic (com smoothness no alfa) e Normal.
   - *Por quê:* se algum mapa faltar, quase sempre é um canal que ficou desligado ou um preset errado. É melhor descobrir antes de abrir a Unity.

**Evidência:** pasta com o `.3b` e os mapas exportados, todos com o mesmo prefixo de nome.

## Etapa 9 — Montar o material na Unity

1. **Importe os mapas** para uma pasta do projeto (`Assets/Texturas/HeroAsset/`).
2. **Marque o Normal como normal map.** Selecione a textura Normal e, no Inspector, mude *Texture Type* para *Normal map*.
   - *Por quê:* sem isso, a Unity lê o Normal como uma imagem colorida e o relevo sai errado. A Unity usa a convenção OpenGL (Y+), a mesma do preset.
3. **Crie um material URP Lit** com *Workflow Mode: Metallic*. Ligue a cor em *Base Map*, o Metallic em *Metallic Map* (com *Smoothness → Source: Metallic Alpha* para a suavidade) e o Normal em *Normal Map*.
   - *Por quê:* é o material PBR padrão da Unity. Ele reage à luz da cena, que é o que se espera do Hero Asset nas Semanas 7 e 8.
4. **Compare com o 3DCoatTextura.** Coloque o modelo na cena com uma luz direcional e compare com a Render Room.
   - *Por quê:* diferenças grandes de brilho ou relevo quase sempre vêm de um mapa trocado ou da convenção do Normal.

> **Trilha hand-painted:** quem seguir o estilo pintado (luz assada na cor) vai usar um shader **Unlit**, como explicado na Etapa 6 do [Tutorial geral de Smart Material](/Tutoriais/Tutorial_Smart_Material_Diffuse_3DCoat.md). Para este tutorial, use URP Lit.

**Evidência:** print do Hero Asset na Unity ao lado do mesmo ângulo no 3DCoatTextura.

## Problemas comuns

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| Modelo chega gigante, minúsculo ou deitado | Transformações não aplicadas ou eixo trocado | `Ctrl+A → All Transforms` no Blender; marcar Z-up na importação |
| A pintura aparece em dois lugares | Ilhas de UV sobrepostas ou espelhadas | Separar as ilhas no Blender e exportar de novo (Etapa 1) |
| Pincelada deixa relevo ou brilho estranho | Canal Depth ou Metalness ligado sem querer | Conferir os botões de canal na barra superior antes de pintar |
| Câmera gira e deixa pincelada no modelo | Clique sobre o modelo sem `Alt` | Girar no espaço vazio ou segurar `Alt` (Etapa 2) |
| Condições não fazem nada | AO e curvatura não calculados | Refazer a Etapa 6 |
| Smart Material sai com uma cor só | Material não foi preso (Attach) antes do Fill | Botão direito no material → *Attach to the current layer* e conferir o *Material Preview* (Etapa 7) |
| Mudei o material e nada mudou no modelo | Lógica raster: o Fill já foi calculado | Limpar a camada e preencher de novo |
| Relevo invertido ou "afundado" na Unity | Normal não marcado como normal map, ou convenção trocada | *Texture Type: Normal map*; exportar com o preset da Unity (OpenGL) |
| Material muito brilhante ou fosco na Unity | Smoothness fora do alfa do Metallic | Usar o preset da Unity e *Smoothness → Source: Metallic Alpha* |

## Checklist de autoavaliação

- [ ] O FBX saiu do Blender com UV conferido, modificadores e transformações aplicados.
- [ ] Consigo navegar a câmera sem pintar o modelo.
- [ ] O UV no Texture UV Editor é igual ao do Blender.
- [ ] As camadas têm número e função no nome.
- [ ] Sei ligar e desligar cada canal antes de pintar.
- [ ] Testei as três condições com cores puras.
- [ ] Prendi um Smart Material, apliquei com Fill, mudei um parâmetro e refiz o Fill.
- [ ] Salvei o `.3b` com versão no nome.
- [ ] Exportei com o preset da Unity e montei o material URP Lit.

## Para a crítica

Cada estudante mostra a pilha de camadas, ligando uma a uma, e responde a duas perguntas:

1. **Técnica:** qual etapa deu mais trabalho e qual foi a causa (Blender, importação, canal, condição ou exportação)?
2. **Visual:** o material lê como o que ele deveria ser (madeira, pedra, metal) quando visto na Unity?

## Próximos passos

Com este tutorial feito, siga para os tutoriais de Smart Material estilizado:

1. [Tutorial geral — Smart Material "Diffuse"](/Tutoriais/Tutorial_Smart_Material_Diffuse_3DCoat.md)
2. [Clone 1 — SimpleDiffuse](/Tutoriais/Clone_1_SimpleDiffuse.md) (exercício guiado)
3. [Clone 2 — Stylized FT](/Tutoriais/Clone_2_Stylized_FT.md) e [Clone 3 — SoMuchDiffuse](/Tutoriais/Clone_3_SoMuchDiffuse.md) (aprofundamento por trilha)

## Fontes

- [3DCoat — GPU Texturing (canais, camadas, presets de exportação)](https://3dcoat.com/documentation/manual/texturing/)
- [3DCoat — Per-Pixel Painting](https://3dcoat.com/documentation/manual/texturing/per-pixel-painting/)
- [3DCoat — Importing into the Painting Room](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/importing-into-the-paint-room/)
- [3DCoat — Blending Panel](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/the-layers-panel/the-blending-panel/)
- [3DCoat — Brushes and Alphas](https://3dcoat.com/documentation/manual/brush-components/brushes-alphas/)
- [3DCoat — Conditions Limiter](https://3dcoat.com/documentation/manual/brush-components/conditions-limiter/)
- [3DCoat — Attach a Smart Material to a layer](https://3dcoat.com/documentation/?p=6295)
- [3DCoat — Textures Menu (exportação, resolução)](https://3dcoat.com/documentation/manual/workspaces-rooms/paint/paint-workspace-menus/textures-menu/)
- [Blender Manual — FBX](https://docs.blender.org/manual/en/latest/files/import_export/fbx.html)
- [Introduction to 3D Coat Textura — Parte 1 (TheNerdForum)](https://www.youtube.com/watch?v=R59R-ughX80) e [Parte 2](https://www.youtube.com/watch?v=tdU_4JABm8M)
