# Cronograma Detalhado — Disciplina de Texturização
**Instituto Federal de Mato Grosso do Sul — Campus Dourados**  
Tecnologia em Jogos Digitais | Studio-Based Learning | 17 Semanas | 51 horas

> 🔴 **Crítica FORMAL** nas semanas: 3, 5, 8, 11, 14 e 17  
> 🔵 **Crítica Informal** nas demais semanas

---

## Unidade I — Fundamentos e Mapeamento UV (Semanas 1–4)

---

### Semana 1 🔵
**Tema:** Apresentação da disciplina, pipeline e escolha de tema do Kit Modular

| Campo | Conteúdo |
|---|---|
| **Apostila** | Introdução (Cap. 1) — Visão geral do pipeline de texturização |
| **Mini Aula** (20 min) | O que é textura e material em computação gráfica? Diferença entre raster e procedural. Apresentação do pipeline Blender → 3D Coat → Unity. Introdução ao projeto semestral (Kit Modular de Ambiente). |
| **Demonstração** (20 min) | Tour pela interface do Blender: Shading Workspace, UV Editor e Viewport Shading. Visualização de exemplos de kits modulares prontos (Medieval, Sci-Fi, etc.). |
| **Estúdio** (50+60 min) | Pesquisa e montagem de mood board temático. Cada estudante seleciona 10 referências visuais do tema escolhido e organiza em um painel de referências. |
| **Entrega** | Mood board + definição formal do tema do Kit Modular (documento de uma página com justificativa). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 2 🔵
**Tema:** Fundamentos de mapeamento UV: conceitos e projeção de textura

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 2 — Projeção de textura e mapa UV; Conceitos de texel density e espaço UV |
| **Mini Aula** (20 min) | O que é um mapa UV? Espaço UV (0–1), distorção, sobreposição e texel density. Tipos de projeção: planar, cilíndrica, esférica, cúbica. |
| **Demonstração** (20 min) | Demonstração de projeção UV simples no Blender em um cubo e em uma esfera. Uso do checkerboard texture para verificar distorção. |
| **Estúdio** (50+60 min) | Praticar projeções UV em objetos geométricos simples (cubo, cilindro, esfera) usando os modelos de prática do professor. Aplicar checkerboard e analisar distorção. |
| **Entrega** | Arquivo .blend com 3 objetos UV mapeados (checkerboard aplicado e screenshot do resultado). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 3 🔴 CRÍTICA FORMAL
**Tema:** Abertura de malha com Smart UV Project e Seams manuais

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 2 — Smart UV Project; Cap. 3 — Seams e Unwrap manual no Blender |
| **Mini Aula** (20 min) | Smart UV Project: quando usar e limitações. Seams: lógica de corte para reduzir distorção. Princípios de um bom layout UV (islands, padding, aproveitamento de espaço). |
| **Demonstração** (20 min) | Abertura de malha de um prop simples do kit modular (ex.: barril, caixa, pedra) com seams manuais e unwrap. Organização de UV islands no UV Editor. |
| **Estúdio** (50+60 min) | Os estudantes abrem a malha UV de seu primeiro asset do kit modular com seams manuais. Objetivo: distorção mínima e islands organizadas. |
| **Entrega** | Asset 01 do Kit Modular com UV aberto (arquivo .blend + screenshot do UV layout com checkerboard). |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 4 🔵
**Tema:** Otimização de layout UV: distorção, aproveitamento e densidade de texel

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 3 — Análise de distorção; Otimização de layout e empacotamento de UV islands |
| **Mini Aula** (20 min) | Analisando distorção com Stretch Overlay. Normalização de texel density. Ferramentas de empacotamento (Pack Islands, UVPackmaster). Estratégias de aproveitamento do espaço UV. |
| **Demonstração** (20 min) | Otimização ao vivo de um UV com má distribuição de espaço. Uso do addon UV Squares e empacotamento. Comparação antes/depois. |
| **Estúdio** (50+60 min) | Revisão e otimização do UV do Asset 01 com base no feedback da crítica formal. Abertura do UV de um segundo asset do kit. |
| **Entrega** | Asset 01 revisado + Asset 02 com UV aberto (blends + screenshots). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

## Unidade II — Materiais PBR e Workflow (Semanas 5–8)

---

### Semana 5 🔴 CRÍTICA FORMAL
**Tema:** Fundamentos do Physically Based Rendering (PBR)

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 4 — Fundamentos de PBR; Mapas PBR: Diffuse/Albedo, Metallic e Roughness |
| **Mini Aula** (20 min) | O que é PBR e por que usamos? Modelos físicos de luz: reflexão especular e difusa. Workflow Metallic/Roughness vs. Specular/Glossiness. O papel de cada mapa: Albedo, Metallic, Roughness. |
| **Demonstração** (20 min) | Criação de um material PBR simples no Blender (Principled BSDF) e configuração de cada canal. Comparação de materiais: metal polido, metal enferrujado, madeira e pedra. |
| **Estúdio** (50+60 min) | Criação de 4 materiais PBR simples no Blender para testar os conceitos (metal, plástico, pedra, madeira) com valores coerentes de roughness e metallic. |
| **Entrega** | Arquivo .blend com 4 materiais PBR configurados no Principled BSDF (screenshot do viewport renderizado). |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 6 🔵
**Tema:** Criação de texturas seamless e tileable

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 4 — Texturas seamless; Fontes de texturas e técnicas de criação |
| **Mini Aula** (20 min) | O que é uma textura seamless? Offset e patch em editores de imagem. Uso do Krita para criação de texturas tileable. Fontes de texturas (Poly Haven, AmbientCG). |
| **Demonstração** (20 min) | Criação de uma textura seamless de pedra a partir de uma fotografia usando Krita (offset + patch de bordas). Importação e aplicação no Blender. |
| **Estúdio** (50+60 min) | Cada estudante cria ou adapta uma textura seamless condizente com o tema do seu kit (ex.: textura de parede de pedra, metal enferrujado, madeira). Aplica ao Asset 01. |
| **Entrega** | Textura seamless temática (arquivo PNG 1024×1024 ou superior) + Asset 01 com textura aplicada. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 7 🔵
**Tema:** Mapas PBR avançados: Normal Map, Subsurface e geração procedural

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 4 — Normal Map; Subsurface Scattering; Cap. 5 — Geração procedural no Blender |
| **Mini Aula** (20 min) | Como funciona um Normal Map (espaço tangente vs. espaço objeto). Quando usar Subsurface Scattering. Introdução à geração procedural de texturas com nós no Blender. |
| **Demonstração** (20 min) | Criação de um Normal Map procedural no Blender (Bump → Normal Map node). Configuração de SSS em um material orgânico. Primeiros nós procedurais (Noise Texture, Musgrave). |
| **Estúdio** (50+60 min) | Criação de um material PBR completo (Albedo + Metallic + Roughness + Normal) para um asset do kit usando texturas procedurais como base. |
| **Entrega** | Asset 02 com material PBR completo (todos os canais conectados). Screenshot do node tree e render. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 8 🔴 CRÍTICA FORMAL
**Tema:** Workflow no 3D Coat: camadas, projeção e exportação PBR

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 6 — Introdução ao 3D Coat; Workflow de texturização PBR: camadas e exportação |
| **Mini Aula** (20 min) | Tour pelo 3D Coat: Paint Room, UV Room, Render Room. Sistema de camadas e canais PBR. Importação de mesh com UV do Blender e exportação de mapas. |
| **Demonstração** (20 min) | Importação de um asset com UV pronto para o 3D Coat. Pintura de camadas de Albedo, Roughness e Metallic. Exportação de mapas PBR e configuração no Blender. |
| **Estúdio** (50+60 min) | Importar um dos assets do kit para o 3D Coat e iniciar a texturização PBR por camadas. Aplicar cor base, roughness e metallic coerentes com o tema. |
| **Entrega** | Asset 01 texturizado no 3D Coat: exportação dos mapas PBR (Albedo, Metallic, Roughness) e material configurado no Blender. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

## Unidade III — Pintura Digital e Bake (Semanas 9–12)

---

### Semana 9 🔵
**Tema:** Texturização artística por pintura digital no 3D Coat

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 7 — Pintura digital aplicada a texturas; Ferramentas de pintura no 3D Coat |
| **Mini Aula** (20 min) | Diferença entre texturização fotorrealista e estilizada. Pintura de desgaste, sujeira e detalhes hand-painted. Organização de camadas por tipo de detalhe. |
| **Demonstração** (20 min) | Pintura de desgaste e variação de cor em um material metálico no 3D Coat. Técnicas de edge wear, dirt e scratches com pincéis e alphas. |
| **Estúdio** (50+60 min) | Adicionar detalhes de desgaste, sujeira e variação de cor ao Asset 01 texturizado na semana anterior. Foco em leitura de silhueta e legibilidade do material. |
| **Entrega** | Asset 01 com camadas de detalhe pintadas (edge wear, dirt, scratches) — mapas exportados e render comparativo antes/depois. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 10 🔵
**Tema:** Uso de Stencils em texturização

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 7 — Uso de stencils no 3D Coat; Criação e importação de alphas |
| **Mini Aula** (20 min) | O que é stencil e para que serve. Diferença entre stencil e alpha. Fontes de stencils (ArtStation, criação manual no Krita). Técnicas de projeção e controle de opacidade. |
| **Demonstração** (20 min) | Aplicação de stencil de rachaduras em uma superfície de pedra no 3D Coat. Criação de um stencil personalizado no Krita e importação. |
| **Estúdio** (50+60 min) | Usar stencils para adicionar detalhes específicos do tema ao Asset 02 (ex.: rachaduras em pedra, símbolos, grafites, corrosão). Trabalhar combinação de stencils com pintura livre. |
| **Entrega** | Asset 02 com detalhes aplicados via stencil — mapas exportados e screenshot do processo. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 11 🔴 CRÍTICA FORMAL
**Tema:** Bake de texturas: Normal Map, AO e Curvature

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 8 — Bake de texturas no Blender; Normal Map, Ambient Occlusion e Curvature Map |
| **Mini Aula** (20 min) | O que é bake e por que usar? High-poly vs. low-poly: transferência de detalhe. Tipos de bake: Normal, AO, Curvature, ID Map, Thickness. Configuração de raio de bake e cage. |
| **Demonstração** (20 min) | Setup completo de bake de Normal Map no Blender (high-poly + low-poly do mesmo asset). Configuração de cage, ray distance e resolução. Verificação de artefatos. |
| **Estúdio** (50+60 min) | Os estudantes criam uma versão high-poly de detalhe de um asset e executam o bake de Normal Map e AO. Integração do Normal Map baked ao material no 3D Coat. |
| **Entrega** | Normal Map e AO mapa baked de um asset do kit + material atualizado com o bake integrado. Comparação visual high-poly vs. low-poly com bake. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 12 🔵
**Tema:** Bake avançado: ID Map, Curvature e integração ao workflow PBR

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 8 — ID Map e Curvature Map; Uso de bakes como base de mascaramento no 3D Coat |
| **Mini Aula** (20 min) | ID Map: criação e uso para mascaramento por material. Curvature Map: detecção de arestas e cavidades. Integração do pacote de bakes no 3D Coat como base de geração de detalhe automático. |
| **Demonstração** (20 min) | Configuração de bake de ID Map com materiais coloridos no Blender. Importação do pacote de bakes no 3D Coat e uso do Curvature Map para edge highlight e cavity dirt automáticos. |
| **Estúdio** (50+60 min) | Executar bake completo de um asset (Normal, AO, Curvature, ID Map) e configurar o pacote no 3D Coat. Usar máscaras geradas por bake para distribuir materiais automaticamente. |
| **Entrega** | Pacote completo de bake (4 mapas) de um asset + configuração de material no 3D Coat com uso de máscara por curvature e ID. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

## Unidade IV — Otimização e Integração ao Motor (Semanas 13–16)

---

### Semana 13 🔵
**Tema:** Texture Atlas: unificação de assets em uma única textura

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 9 — Texture Atlas: conceito e criação; Otimização de draw calls |
| **Mini Aula** (20 min) | O que é Texture Atlas e por que reduz draw calls. Planejamento de atlas: quais assets compartilham textura. Organização de UV islands de múltiplos objetos em um único UV. Padding e bleeding. |
| **Demonstração** (20 min) | Criação de um Texture Atlas no Blender combinando 3 assets do kit em um único UV 2048×2048. Reorganização de UV islands e validação de texel density. |
| **Estúdio** (50+60 min) | Os estudantes planejam e executam um Texture Atlas com pelo menos 3 assets do seu kit modular. Reorganização de UVs, re-bake e re-texturização. |
| **Entrega** | Texture Atlas com 3+ assets do kit (UV combinado, mapa de textura único, render dos objetos). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 14 🔴 CRÍTICA FORMAL
**Tema:** Trim Sheets: criação e aplicação para assets modulares

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 9 — Trim Sheets: conceito e workflow; Aplicação em arquitetura modular |
| **Mini Aula** (20 min) | O que é uma Trim Sheet e quando usar. Diferença entre Trim Sheet e Texture Atlas. Planejamento de uma trim: divisão de faixas por tipo de detalhe. Tiling horizontal vs. vertical. |
| **Demonstração** (20 min) | Criação de uma Trim Sheet temática no 3D Coat. Mapeamento de asset de parede modular na Trim Sheet (UV elongado). Validação no Blender e Unity. |
| **Estúdio** (50+60 min) | Cada estudante cria uma Trim Sheet condizente com o tema do kit (ex.: faixa de madeira trabalhada, trilhos de metal, bordas de pedra). Aplica em ao menos um asset arquitetônico. |
| **Entrega** | Trim Sheet temática (PNG 1024×2048 ou equivalente) + asset mapeado na trim, render com comparação de variações usando a mesma trim. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 15 🔵
**Tema:** UDIMs e otimização: compressão, mipmaps e empacotamento de canais

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 10 — UDIMs e Multi Tile Texture; Cap. 11 — Otimização: compressão, mipmaps e channel packing |
| **Mini Aula** (20 min) | UDIMs: o que são e quando usar (assets com alta resolução e múltiplas tiles). Compressão de texturas: BC1, BC3, BC7. Mipmaps: geração automática e manual. Channel packing: R+G+B para economizar samples. |
| **Demonstração** (20 min) | Configuração de UDIMs no Blender para um asset complexo. Demonstração de channel packing (Roughness no R, Metallic no G, AO no B — mapa ORM). Exportação correta de formatos comprimidos. |
| **Estúdio** (50+60 min) | Criar um mapa ORM (channel packed) para os assets do kit. Configurar mipmaps no 3D Coat na exportação. Preparar texturas em tamanhos adequados para engine (power of 2). |
| **Entrega** | Assets do kit com texturas exportadas em formato otimizado: mapa ORM + Albedo + Normal. Tabela de memória estimada de textura antes e depois da otimização. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 16 🔵
**Tema:** Integração na Unity: materiais, lightmap UV e renderização

| Campo | Conteúdo |
|---|---|
| **Apostila** | Cap. 11 — Abertura de malha para lightmap; Cap. 12 — Importação e configuração na Unity; Renderização de modelos texturizados |
| **Mini Aula** (20 min) | Lightmap UV: segunda camada de UV para iluminação baked. Diferença entre UV1 (textura) e UV2 (lightmap). Configuração de materiais PBR na Unity (URP/HDRP). Lightmap baking na Unity. |
| **Demonstração** (20 min) | Abertura de UV2 (lightmap) no Blender. Exportação de FBX e importação na Unity. Configuração de material URP com os mapas exportados. Lightmap bake simples na Unity. |
| **Estúdio** (50+60 min) | Importar os assets do kit na Unity, configurar materiais e executar um lightmap bake simples da cena. Ajustar parâmetros de iluminação e capturar renders finais. |
| **Entrega** | Cena na Unity com todos os assets do kit importados, materiais configurados e lightmap baked. Screenshots da cena renderizada (4 ângulos). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

## Unidade V — Projeto Final e Apresentação (Semana 17)

---

### Semana 17 🔴 CRÍTICA FORMAL
**Tema:** Apresentação e defesa do Kit Modular de Ambiente

| Campo | Conteúdo |
|---|---|
| **Apostila** | Todos os capítulos — Integração semestral |
| **Mini Aula** (20 min) | Orientações finais para a apresentação: estrutura da defesa, tempo, o que mostrar. Critérios de avaliação do Projeto Final. Autoavaliação e reflexão semestral. |
| **Demonstração** (20 min) | Não há demonstração técnica nesta semana. O professor apresenta um exemplo de kit modular completo como referência de padrão esperado. |
| **Estúdio** (50+60 min) | Cada estudante apresenta seu Kit Modular de Ambiente para a turma: 10 minutos de apresentação + 5 minutos de perguntas. Defende decisões técnicas e artísticas. Entrega documentação final e autoavaliação. |
| **Entrega** | Kit Modular completo (todos os assets texturizados, cena na Unity, renders finais) + documento de autoavaliação reflexiva. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

*Disciplina de Texturização — Prof. Rodrigo Devigo — IFMS Campus Dourados*  
*Apostila: https://rsdevigo.github.io/apostila_texturizacao*
