# Cronograma Detalhado — Disciplina de Texturização
**Instituto Federal de Mato Grosso do Sul — Campus Dourados**
Tecnologia em Jogos Digitais | Studio-Based Learning | 17 Semanas | 51 horas

**Trabalho interdisciplinar:** Texturização, Pintura Digital e Arte Conceitual, e Modelagem 3D e Level Design. Entregável final único: uma fase **caminhável** na Unity, construída a partir de um Kit Modular de Ambiente estilizado, com tema de um mundo fantástico criado a partir de elementos regionais do Mato Grosso do Sul (ou do estado de origem do estudante).

> 🔴 **Crítica FORMAL** nas semanas: 4, 8, 11, 14 e 16
> 🔵 **Crítica Informal** nas demais semanas
> ⚪ Semana 17 — Recuperação (sem crítica coletiva)

---

## Unidade I — Fundamentos, Mapeamento UV e Definição do Hero Asset (Semanas 1–5)

---

### Semana 1 🔵
**Tema:** Apresentação da disciplina, pipeline e do trabalho interdisciplinar

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte I, Cap. 1 — Materiais, Texturas e Representação Visual (fundamentos); Parte VI, Cap. 25 — Pipeline Completo de Texturização para Jogos (visão geral do pipeline) |
| **Mini Aula** (20 min) | O que é textura e material em computação gráfica? Diferença entre raster e procedural. Apresentação do pipeline Blender → 3D Coat → Unity. Apresentação do trabalho interdisciplinar: as três disciplinas envolvidas, o entregável final (fase caminhável na Unity) e o tema (mundo fantástico a partir de elementos regionais do Mato Grosso do Sul ou do estado de origem do estudante). |
| **Demonstração** (20 min) | Tour pela interface do Blender: Shading Workspace, UV Editor e Viewport Shading. Visualização de exemplos de kits modulares prontos (Medieval, Sci-Fi, etc.) e de fases caminháveis simples na Unity. |
| **Estúdio** (50+60 min) | Discussão coletiva sobre o tema regional: levantamento livre de referências culturais, paisagísticas e folclóricas do Mato Grosso do Sul (ou do estado de origem de cada estudante). Início da pesquisa livre, sem compromisso de entrega. |
| **Entrega** | Nenhuma. Semana de abertura e alinhamento do trabalho interdisciplinar. |
| **Crítica** | 🔵 Informal — Roda de conversa sobre os primeiros direcionamentos temáticos, sem cobrança formal. |

---

### Semana 2 🔵
**Tema:** Fundamentos de mapeamento UV: conceitos e projeção de textura

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte II, Cap. 4 — Coordenadas UV e Projeções de Textura |
| **Mini Aula** (20 min) | O que é um mapa UV? Espaço UV (0–1), distorção, sobreposição. Tipos de projeção: planar, cilíndrica, esférica, cúbica. |
| **Demonstração** (20 min) | Demonstração de projeção UV simples no Blender em um cubo e em uma esfera. Uso do checkerboard texture para verificar distorção. |
| **Estúdio** (50+60 min) | Praticar projeções UV em objetos geométricos simples (cubo, cilindro, esfera) usando modelos de prática do professor. Em paralelo, cada estudante acompanha a proposta inicial e o feedback recebido em Pintura Digital e Arte Conceitual para amadurecer o recorte temático. |
| **Entrega** | Arquivo .blend com 3 objetos UV mapeados (checkerboard aplicado e screenshot do resultado). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 3 🔵
**Tema:** Moodboard temático e definição do Hero Asset Referência

| Campo | Conteúdo |
|---|---|
| **Apostila** | Revisão da Parte I, Cap. 1 (aplicada à escolha do tema); leitura antecipada da Parte II, Cap. 5 — UV Unwrapping, para a Semana 4 |
| **Mini Aula** (20 min) | O que é um Hero Asset Referência e por que ele existe: uma peça única, altamente representativa do tema, que funciona como prova de conceito do pipeline completo (UV → PBR → 3D Coat) antes de escalar para o Kit Modular inteiro. Critérios para escolher um bom Hero Asset: legibilidade do tema, viabilidade técnica, potencial de reaproveitamento de linguagem visual no restante do kit. |
| **Demonstração** (20 min) | Exemplos de Hero Assets de projetos de referência (ArtStation) e como eles se conectam a um kit modular mais amplo. Critério de avaliação da coerência entre moodboard e Hero Asset escolhido. |
| **Estúdio** (50+60 min) | Cada estudante consolida seu moodboard temático a partir do material já produzido em Pintura Digital e Arte Conceitual (mínimo de 10 referências organizadas) e define, em diálogo com Modelagem 3D e Level Design, qual será seu Hero Asset Referência — a peça que Modelagem 3D modela nesta mesma semana. |
| **Entrega** | Moodboard temático curado (PNG, PDF ou link) + definição do Hero Asset Referência com justificativa de 1 parágrafo (por que essa peça representa o tema). |
| **Crítica** | 🔵 Informal — Roda de temas: cada estudante declara o tema e o Hero Asset escolhido, turma e professor comentam. |

---

### Semana 4 🔴 CRÍTICA FORMAL
**Tema:** Abertura de UV do Hero Asset Referência — Smart UV Project e seams manuais

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte II, Cap. 5 — UV Unwrapping (Smart UV Project, Seams e Unwrap manual) |
| **Mini Aula** (20 min) | Smart UV Project: quando usar e limitações. Seams: lógica de corte para reduzir distorção. Princípios de um bom layout UV (islands, padding, aproveitamento de espaço). |
| **Demonstração** (20 min) | Abertura de malha de um prop simples com seams manuais e unwrap. Organização de UV islands no UV Editor. |
| **Estúdio** (50+60 min) | Cada estudante recebe o Hero Asset Referência modelado por Modelagem 3D e Level Design nesta mesma semana e abre sua UV com seams manuais. Objetivo: distorção mínima e islands organizadas. |
| **Entrega** | Hero Asset Referência com UV aberto (arquivo .blend + screenshot do UV layout com checkerboard). |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 5 🔵
**Tema:** Revisão de UV com base no feedback da CF1 e fundamentos de PBR (Principled BSDF)

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte II, Cap. 6 — Texel Density e Organização de UVs (revisão rápida de distorção e empacotamento); Parte III, Cap. 8 e Cap. 9 — Fundamentos do PBR e os mapas que compõem um material (Albedo, Metallic, Roughness) |
| **Mini Aula** (20 min) | Revisão rápida de Stretch Overlay, texel density e Pack Islands para corrigir o feedback da CF1. Em seguida, transição para a Unidade II: o que é PBR e por que o modelo Metallic/Roughness é o padrão para jogos em tempo real. |
| **Demonstração** (20 min) | Ajuste ao vivo de um UV com distorção residual usando Pack Islands. Criação de materiais PBR simples no Principled BSDF (Albedo, Metallic, Roughness) com valores fisicamente plausíveis para diferentes materiais de referência. |
| **Estúdio** (50+60 min) | Revisão e otimização do UV do Hero Asset Referência com base no feedback da crítica formal da Semana 4. Em seguida, criação de materiais PBR de teste (valores planos, sem textura ainda) para o tema do kit e aplicação de um material ao Hero Asset Referência. |
| **Entrega** | Hero Asset Referência com UV revisado e material PBR de valores planos aplicado (blend + screenshot atualizado). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

## Unidade II — Materiais PBR e Workflow no 3D Coat (Semanas 6–9)

---

### Semana 6 🔵
**Tema:** Criação de texturas seamless e tileable (trilha fotorrealista ou estilizada)

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte IV, Cap. 12 — Texturas Seamless e Tileables |
| **Mini Aula** (20 min) | O que é uma textura seamless e por que ela é necessária em jogos com superfícies amplas. Duas trilhas de fonte: fotográfica (Poly Haven, AmbientCG) ou estilizada/pintada, ambas exigindo o mesmo tratamento de continuidade de borda. |
| **Demonstração** (20 min) | Criação de uma textura seamless a partir de uma fotografia usando Krita (offset + patch de bordas) e aplicação no Albedo do material PBR já calibrado na Semana 5. Comparação rápida com o caso de uma textura estilizada. |
| **Estúdio** (50+60 min) | Criação de uma textura seamless temática (fotográfica ou estilizada, conforme a trilha visual do estudante) condizente com o Hero Asset Referência, conectada ao Albedo com Metallic/Roughness preservados. |
| **Entrega** | Arquivo .blend do Asset 01 com textura seamless aplicada ao Albedo (PNG 1024×1024 ou superior) + arquivo .kra de origem. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 7 🔵
**Tema:** Migração para o 3D Coat: mesh maps (AO, Curvature, Normal) e Smart Materials

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte III, Cap. 10 — Construção e Análise de Materiais Reais (introdução ao 3D Coat); Parte V, Cap. 16 — Normal Maps e Transferência de Detalhes. Leitura complementar (não avaliada): Parte IV, Cap. 13 — Texturização Procedural, para quem quiser a via alternativa de nós no Blender |
| **Mini Aula** (20 min) | O que são mesh maps (AO, Curvature, Normal) e por que podem ser gerados direto da malha, sem high-poly. As duas trilhas visuais dentro do mesmo fluxo de ferramenta: base fotográfica + máscara de desgaste (fotorrealista) ou Smart Material guiado pela mesma máscara (estilizado). |
| **Demonstração** (20 min) | Exportação do Blender e importação no 3D Coat. Bake de AO e Curvature direto da malha. Normal Map gerado por pintura no canal Depth. |
| **Estúdio** (50+60 min) | Migração do Hero Asset Referência para o 3D Coat: Color (base fotográfica ou Smart Material), máscara de AO/Curvature para desgaste, e Normal via Depth. Mínimo de três canais ativos ao final da semana. |
| **Entrega** | Hero Asset Referência no 3D Coat com Color + Roughness + Normal ativos. Screenshot de camadas e render comparativo antes/depois da máscara. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 8 🔴 CRÍTICA FORMAL — CF2
**Tema:** Refinamento no 3D Coat e exportação PBR unificada (Albedo, Metallic, Roughness, Normal)

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte III, Cap. 10 — Construção e Análise de Materiais Reais (workflow de texturização PBR: camadas e exportação). Leitura de apoio: Parte VI, Cap. 23 — Controle de Qualidade de Materiais |
| **Mini Aula** (20 min) | Subsurface Scattering (SSS) para materiais orgânicos. Lógica de combinar base + máscara + pintura manual sem que nenhuma camada sozinha conte toda a história do material. |
| **Demonstração** (20 min) | Refinamento das camadas de Color e Metallic. Exportação dos quatro mapas PBR (Albedo, Metallic, Roughness, Normal) e configuração completa no Blender, com o nó Normal Map. |
| **Estúdio** (50+60 min) | Cada estudante refina o material do Hero Asset Referência no 3D Coat (Color, Roughness, Metallic), exporta os quatro mapas PBR e reconfigura o material no Blender, sem nós procedurais remanescentes. |
| **Entrega** | Hero Asset Referência texturizado no 3D Coat: exportação dos quatro mapas PBR (Albedo, Metallic, Roughness, Normal) e material configurado no Blender. |
| **Crítica** | 🔴 **FORMAL — CF2** (25% do Portfolio de Artefatos) — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 9 🔵
**Tema:** Texturização artística por pintura digital no 3D Coat

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte IV, Cap. 14 — Pintura Digital para Jogos (aplicada a texturas; ferramentas de pintura no 3D Coat) |
| **Mini Aula** (20 min) | Diferença entre texturização fotorrealista e estilizada. Pintura de desgaste, sujeira e detalhes hand-painted. Organização de camadas por tipo de detalhe. |
| **Demonstração** (20 min) | Pintura de desgaste e variação de cor em um material metálico no 3D Coat. Técnicas de edge wear, dirt e scratches com pincéis e alphas. |
| **Estúdio** (50+60 min) | Adicionar detalhes de desgaste, sujeira e variação de cor ao Hero Asset Referência texturizado na semana anterior. Foco em leitura de silhueta e legibilidade do material. Esta é a semana da SCT (Semana de Ciência e Tecnologia) — ajustar ritmo de estúdio conforme a agenda do evento. |
| **Entrega** | Hero Asset Referência com camadas de detalhe pintadas (edge wear, dirt, scratches) — mapas exportados e render comparativo antes/depois. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

> **Recesso — 12 a 16/10 ("Saco cheio").** Semana não letiva, não faz parte das 17 semanas do cronograma.

---

## Unidade III — Produção do Kit Modular: Bake e Detalhamento (Semanas 10–13)

---

### Semana 10 🔵
**Tema:** Uso de Stencils em texturização

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte V, Cap. 17 — Máscaras, Stencils e Decals (uso de stencils no 3D Coat; criação e importação de alphas) |
| **Mini Aula** (20 min) | O que é stencil e para que serve. Diferença entre stencil e alpha. Fontes de stencils (ArtStation, criação manual no Krita). Técnicas de projeção e controle de opacidade. |
| **Demonstração** (20 min) | Aplicação de stencil de rachaduras em uma superfície de pedra no 3D Coat. Criação de um stencil personalizado no Krita e importação. |
| **Estúdio** (50+60 min) | Uso de stencils para refinar o Hero Asset Referência (símbolos, rachaduras, corrosão) e, para quem já recebeu os primeiros assets modelados por Modelagem 3D e Level Design nesta fase de "Kit modular", início da aplicação da mesma linguagem visual a eles. |
| **Entrega** | Hero Asset Referência (ou primeiro asset do kit) com detalhes aplicados via stencil — mapas exportados e screenshot do processo. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 11 🔴 CRÍTICA FORMAL
**Tema:** Bake de texturas: Normal Map, AO e Curvature

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte V, Cap. 15 — Bake de Texturas (no Blender: Normal Map e Ambient Occlusion). Leitura de apoio: Parte VI, Cap. 23 — Controle de Qualidade de Materiais |
| **Mini Aula** (20 min) | O que é bake e por que usar? High-poly vs. low-poly: transferência de detalhe. Foco em Normal Map e Ambient Occlusion. Configuração de raio de bake e cage. (Curvature, ID Map e Thickness são apresentados na Semana 12.) |
| **Demonstração** (20 min) | Setup completo de bake de Normal Map no Blender (high-poly + low-poly do mesmo asset). Configuração de cage, ray distance e resolução. Verificação de artefatos. |
| **Estúdio** (50+60 min) | Cada estudante executa o bake de Normal Map e AO em um asset do Kit Modular (par low-poly/high-poly preparado em Modelagem 3D e Level Design) e integra o resultado ao material no 3D Coat. |
| **Entrega** | Normal Map e AO baked de um asset do kit + material atualizado com o bake integrado. Comparação visual high-poly vs. low-poly com bake. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 12 🔵
**Tema:** Bake avançado: ID Map, Curvature e integração ao workflow PBR

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte V, Cap. 15 — Bake de Texturas (ID Map e Curvature Map); Parte V, Cap. 17 — Máscaras, Stencils e Decals (uso de bakes como base de mascaramento no 3D Coat) |
| **Mini Aula** (20 min) | Panorama dos tipos de bake (Normal, AO, Curvature, ID Map, Thickness). ID Map: criação e uso para mascaramento por material. Curvature Map: detecção de arestas e cavidades. |
| **Demonstração** (20 min) | Configuração de bake de ID Map com materiais coloridos no Blender. Importação do pacote de bakes no 3D Coat e uso do Curvature Map para edge highlight e cavity dirt automáticos. |
| **Estúdio** (50+60 min) | Executar bake completo (Normal, AO, Curvature, ID Map) de um segundo asset do kit e configurar o pacote no 3D Coat, usando máscaras geradas por bake para distribuir materiais automaticamente. |
| **Entrega** | Pacote completo de bake (4 mapas) de um asset do kit + configuração de material no 3D Coat com uso de máscara por curvature e ID. |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

### Semana 13 🔵
**Tema:** Texture Atlas: unificação de assets em uma única textura

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte V, Cap. 18 — Texture Atlas e Trim Sheets (conceito e criação de atlas; otimização de draw calls) |
| **Mini Aula** (20 min) | O que é Texture Atlas e por que reduz draw calls. Planejamento de atlas: quais assets compartilham textura. Organização de UV islands de múltiplos objetos em um único UV. Padding e bleeding. |
| **Demonstração** (20 min) | Criação de um Texture Atlas no Blender combinando 3 assets do kit em um único UV 2048×2048. Reorganização de UV islands e validação de texel density. |
| **Estúdio** (50+60 min) | Cada estudante planeja e executa um Texture Atlas com pelo menos 3 assets do seu Kit Modular (incluindo o Hero Asset Referência e os assets/props que Modelagem 3D e Level Design já entregou). |
| **Entrega** | Texture Atlas com 3+ assets do kit (UV combinado, mapa de textura único, render dos objetos). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. |

---

## Unidade IV — Otimização, Trim Sheets e Integração na Unity (Semanas 14–15)

---

### Semana 14 🔴 CRÍTICA FORMAL
**Tema:** Trim Sheets: criação e aplicação para assets modulares

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte V, Cap. 18 — Texture Atlas e Trim Sheets (conceito e workflow de trim sheets; aplicação em arquitetura modular). Leitura de apoio: Parte VI, Cap. 23 — Controle de Qualidade de Materiais |
| **Mini Aula** (20 min) | O que é uma Trim Sheet e quando usar. Diferença entre Trim Sheet e Texture Atlas. Planejamento de uma trim: divisão de faixas por tipo de detalhe. Tiling horizontal vs. vertical. |
| **Demonstração** (20 min) | Criação de uma Trim Sheet temática no 3D Coat. Mapeamento de asset arquitetônico modular na Trim Sheet (UV elongado). Validação no Blender e Unity. |
| **Estúdio** (50+60 min) | Cada estudante cria uma Trim Sheet condizente com o tema do kit e aplica em ao menos um asset arquitetônico modular — a peça que sustenta a modularidade da fase caminhável. |
| **Entrega** | Trim Sheet temática (PNG 1024×2048 ou equivalente) + asset mapeado na trim, render com comparação de variações usando a mesma trim. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 15 🔵
**Tema:** UDIMs, otimização e integração completa na Unity

| Campo | Conteúdo |
|---|---|
| **Apostila** | Parte V, Cap. 19 — UDIMs, Texture Arrays e Multi-Tile Texturing; Parte V, Cap. 20 — Compressão, Mipmaps e Packing de Canais; Parte VI, Cap. 21 — Lightmaps e Iluminação em Motores; Parte VI, Cap. 22 — Integração com Unreal Engine e Unity |
| **Mini Aula** (20 min) | UDIMs para assets de alta resolução. Compressão de texturas (BC1, BC3, BC7), mipmaps e channel packing (mapa ORM). Lightmap UV: diferença entre UV1 (textura) e UV2 (lightmap) e por que a fase caminhável precisa dela. |
| **Demonstração** (20 min) | Demonstração de channel packing (Roughness no R, Metallic no G, AO no B). Abertura de UV2 (lightmap) no Blender e reexportação do FBX. Importação de todos os assets do kit na Unity, montagem básica da fase e lightmap bake da cena. |
| **Estúdio** (50+60 min) | Criar mapas ORM para os assets do kit, abrir UV2 nos assets que ainda não têm, importar todos os assets na Unity, montar a fase caminhável (colisão de piso e limites de percurso, sem gameplay adicional) e executar o lightmap bake da cena completa. |
| **Entrega** | Fase caminhável montada na Unity com todos os assets do kit importados, materiais otimizados (ORM) e lightmap baked. Screenshots da cena (4 ângulos) + teste de caminhada (vídeo curto ou gif). |
| **Crítica** | 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro. Esta é a semana do evento institucional Pantanal Game Show — sem relação direta com a entrega, mas vale observar a agenda do campus ao planejar o ritmo de estúdio. |

---

## Unidade V — Projeto Final: Apresentação e Recuperação (Semanas 16–17)

---

### Semana 16 🔴 CRÍTICA FORMAL
**Tema:** Apresentação e defesa do Kit Modular e da fase caminhável

| Campo | Conteúdo |
|---|---|
| **Apostila** | Todos os capítulos — Parte I a VI, Cap. 1 a 25 — Integração semestral. Leitura obrigatória desta semana: Parte VI, Cap. 24 — Apresentação Profissional de Assets (breakdown visual, portfólio e padrão ArtStation) |
| **Mini Aula** (20 min) | Orientações finais para a apresentação: estrutura da defesa, tempo, o que mostrar (breakdown de texturas, jogabilidade da caminhada, integração com Pintura Digital e Arte Conceitual e Modelagem 3D e Level Design). Critérios de avaliação do Projeto Final. Autoavaliação e reflexão semestral. |
| **Demonstração** (20 min) | Não há demonstração técnica nesta semana. O professor apresenta um exemplo de kit modular com fase caminhável como referência de padrão esperado. |
| **Estúdio** (50+60 min) | Cada estudante apresenta seu Kit Modular de Ambiente e a fase caminhável na Unity para a turma: 10 minutos de apresentação + 5 minutos de perguntas. Defende decisões técnicas e artísticas, incluindo a coerência com o tema regional e a integração com as outras duas disciplinas. |
| **Entrega** | Kit Modular completo (todos os assets texturizados) + fase caminhável funcional na Unity + documento de autoavaliação reflexiva. |
| **Crítica** | 🔴 **FORMAL** — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor. |

---

### Semana 17 ⚪ Recuperação
**Tema:** Reposição de entregas e atendimento individual

| Campo | Conteúdo |
|---|---|
| **Apostila** | Conforme necessidade individual de cada estudante em reposição. |
| **Mini Aula** (20 min) | Não há mini aula nova. Revisão pontual de conceitos com base nas lacunas identificadas na Semana 16. |
| **Demonstração** (20 min) | Sob demanda, conforme dificuldades específicas relatadas pelos estudantes em reposição. |
| **Estúdio** (50+60 min) | Atendimento individual aos estudantes que não concluíram entregas formais ao longo do semestre. Finalização e reapresentação pontual do que estiver pendente. |
| **Entrega** | Entregas formais pendentes das Semanas 1 a 16, conforme combinado individualmente com cada estudante. |
| **Crítica** | ⚪ Sem crítica coletiva — feedback individual no atendimento. |

---

*Disciplina de Texturização — Prof. Rodrigo Devigo — IFMS Campus Dourados*
*Apostila: https://rsdevigo.github.io/apostila_texturizacao*
