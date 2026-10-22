# Tutoriais — Smart Materials estilizados no 3DCoat

Criados em 20/10/2026.

| Tutorial | O que ensina |
| --- | --- |
| [Tutorial 0 — Primeiros passos no 3DCoatTextura](/Tutoriais/Tutorial_0_Primeiros_Passos_3DCoatTextura.md) | Interface, importação, camadas e canais, pincel, Attach + Fill, exportação para a Unity. **Faça primeiro.** |
| [Tutorial geral — Smart Material estilizado "Diffuse"](/Tutoriais/Tutorial_Smart_Material_Diffuse_3DCoat.md) | Receita combinada das três referências |
| [Clone 1 — SimpleDiffuse](/Tutoriais/Clone_1_SimpleDiffuse.md) | Máscaras básicas (base, sombra, cavidade, AO, borda), gradientes de topo e de base e variação de cor (8 camadas) |
| [Clone 2 — Stylized FT](/Tutoriais/Clone_2_Stylized_FT.md) | Padrão pintado no Krita + mistura de tons quentes e frios (8 camadas) |
| [Clone 3 — SoMuchDiffuse](/Tutoriais/Clone_3_SoMuchDiffuse.md) | Rig de luz assado, especular pintado, underlight, HSL, cel (10 camadas + pós) |

Progressão sugerida: Tutorial 0 (fundamentos, Semana 7) → Clone 1 (máscaras) → Clone 2 (cor) → Clone 3 (luz). Cada clone parte do anterior.

## Materiais por parte da malha

Cinco modos de aplicar materiais só em uma parte do modelo (o "folder com máscara" do Substance Painter). Cada tutorial é independente.

| Modo | Como recorta | Máscara editável depois? | Quando usar |
| --- | --- | --- | --- |
| [1. Clipping Mask](/Tutoriais/Partes_1_Clipping_Mask.md) **(recomendado)** | Camada de máscara + *Clip Mask Layer* nas camadas da parte | Sim | Fluxo padrão da turma; pasta por parte, como no Substance |
| [2. Freeze](/Tutoriais/Partes_2_Freeze.md) | Congela tudo menos a parte antes do Fill | Não (refazer o congelamento) | Poucas partes, aplicação rápida, retoques protegidos |
| [3. ID map](/Tutoriais/Partes_3_ID_Map.md) | Seleção por cor de um ID map assado no Blender | Sim, se virar máscara do modo 1 | Muitas partes, ou partes que não coincidem com materiais/objetos |
| [4. Fill direto por parte](/Tutoriais/Partes_4_Fill_por_Parte.md) | Escopo do Fill: objeto, material ou ângulo | Não | Blocagem e testes rápidos; preencher as máscaras do modo 1 |
| [5. Nós (2026)](/Tutoriais/Partes_5_Nos_2026.md) | *Out mask* da pasta com imagem preto e branco da parte | Sim (procedural) | Fluxo procedural; testar na versão do laboratório antes |
