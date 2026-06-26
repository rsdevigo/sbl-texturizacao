# PLANO DE ENSINO
## Disciplina: Texturização

**Instituto Federal de Mato Grosso do Sul — Campus Dourados**
Curso Superior de Tecnologia em Jogos Digitais

---

## 1. Identificação da Disciplina

| Campo | Informação |
|---|---|
| **Instituição** | Instituto Federal de Mato Grosso do Sul – Campus Dourados |
| **Curso** | Tecnologia em Jogos Digitais |
| **Disciplina** | Texturização |
| **Carga Horária** | 51 horas (17 semanas × 3 horas semanais) |
| **Período** | 2º Semestre de 2026 |
| **Professor** | Rodrigo Devigo |
| **Encontros** | 2 encontros semanais de 1h30 cada |
| **Metodologia** | Studio-Based Learning (SBL) |

---

## 2. Ementa

Definição de material e textura em computação gráfica. Projeção de textura e mapa de UV. Prática de abertura de malha e mapeamento UV. Utilização de texturas realistas (PBR). Texturas seamless. Mapeamentos de imagem para a criação de materiais utilizando PBR: metallic, roughness, diffuse, normal e subsurface. Workflow de criação para materiais. Geração procedural de elementos em texturas. Texturização artística por meio de pintura digital. Uso de stencil em texturização. Bake de texturas. Texture atlas, trim sheets e otimização. Uso de UDIMs/Multi tile texture/texture array e otimização. Otimização de desempenho em texturas: tamanho de textura, compressão de texturas, mipmaps e junção de mapas em única textura utilizando diferentes canais. Abertura de malha para mapa de iluminação para motores de jogo. Renderização de modelos texturizados.

---

## 3. Objetivo Geral

Capacitar o estudante a desenvolver fluxos de trabalho de texturização para jogos digitais, dominando desde o mapeamento UV e a criação de materiais PBR até a otimização de texturas para motores de jogo, por meio da produção contínua de artefatos integrados a um projeto semestral de Kit Modular de Ambiente.

---

## 4. Objetivos Específicos

- Compreender os fundamentos de materiais e texturas em computação gráfica e renderização em tempo real.
- Realizar abertura de malha e mapeamento UV eficiente no Blender, minimizando distorção e maximizando o aproveitamento do texel.
- Criar materiais fisicamente plausíveis utilizando o workflow PBR (metallic/roughness) com mapas de diffuse, metallic, roughness, normal e subsurface.
- Produzir texturas artísticas por meio de pintura digital e uso de stencils no 3D Coat.
- Executar bake de mapas de iluminação, normal e ambient occlusion a partir de high-poly para low-poly.
- Organizar assets utilizando Texture Atlas, Trim Sheets e UDIMs para otimização de performance.
- Otimizar texturas para motores de jogo considerando tamanho, compressão, mipmaps e empacotamento de canais.
- Importar e configurar materiais PBR na Unity, validando a fidelidade visual entre DCC e motor.
- Comunicar decisões técnicas e artísticas por meio de críticas coletivas e documentação reflexiva.
- Desenvolver autonomia criativa e capacidade de iteração a partir de feedback estruturado.

---

## 5. Competências Desenvolvidas

### 5.1 Competências Técnicas

- Operação do pipeline de texturização: Blender → 3D Coat → Unity.
- Criação e aplicação de UV maps funcionais para assets de jogos.
- Produção de conjuntos de mapas PBR coerentes e fisicamente plausíveis.
- Técnicas de bake (normal, AO, curvature, lightmap) de high-poly para low-poly.
- Organização eficiente de assets com Texture Atlas e Trim Sheets.
- Otimização de texturas para desempenho em tempo real.

### 5.2 Competências Artísticas

- Leitura e análise de referências visuais para reprodução de materiais.
- Pintura digital aplicada a texturas e uso de stencils.
- Consistência visual entre assets de um mesmo Kit Modular.
- Capacidade de iteração e refinamento estético com base em feedback.

### 5.3 Competências de Processo e Comunicação

- Autoavaliação do próprio trabalho a partir de critérios técnicos e artísticos.
- Justificativa verbal e escrita de decisões de projeto.
- Recebimento e incorporação de feedback de pares e do professor.
- Gestão do tempo e organização de arquivos dentro de um fluxo de produção semestral.

---

## 6. Metodologia: Studio-Based Learning (SBL)

A disciplina adota o Studio-Based Learning como abordagem central. O conteúdo não é apresentado de forma expositiva isolada, mas emerge como resposta direta às necessidades do projeto em andamento. Os estudantes trabalham em estúdio durante a maior parte do tempo, com intervenções curtas e objetivas do professor. O projeto integrador — um Kit Modular de Ambiente — perpassa todas as 17 semanas, fornecendo contexto e propósito para cada conteúdo abordado.

### 6.1 Estrutura do Primeiro Encontro (1h30)

- Mini-aula expositiva dialogada: 20 minutos.
- Demonstração técnica com projeção ao vivo: 20 minutos.
- Produção em estúdio com circulação do professor: 50 minutos.

### 6.2 Estrutura do Segundo Encontro (1h30)

- Crítica coletiva — apresentação do trabalho em progresso por estudante(s) sorteado(s): 20 minutos.
- Produção em estúdio com foco em iteração e incorporação do feedback: 60 minutos.
- Fechamento — síntese das aprendizagens e orientação para a próxima etapa: 10 minutos.

### 6.3 Projeto Integrador

Nas semanas 1 e 2, cada estudante escolhe o tema do seu Kit Modular de Ambiente (ex.: Medieval, Fantasia, Sci-Fi, Pós-apocalíptico, Cyberpunk). Todas as entregas ao longo do semestre são peças deste projeto: nenhuma atividade é desconectada do contexto maior. O projeto culmina na Semana 17 com a apresentação e defesa do Kit completo.

### 6.4 Estratégias de Mediação

- Perguntas abertas durante a produção para estimular reflexão (ex.: "Por que você escolheu essa roughness?").
- Feedback em tempo real durante a produção em estúdio.
- Circulação pelo estúdio com registros de progresso individual.
- Uso de referências visuais (mood boards) como base para tomada de decisão artística.
- Compartilhamento de tela e sobreposição de anotações durante as críticas.

---

## 7. Recursos Utilizados

### 7.1 Softwares

- **Blender** — abertura de malha UV, modelagem de referência, bake de texturas, renderização.
- **3D Coat** — texturização PBR, pintura digital, stencils.
- **Unity** — importação de assets, configuração de materiais, iluminação e lightmap baking.
- **Krita** (opcional) — pintura digital e criação de texturas seamless.

### 7.2 Materiais de Apoio

- Apostila da disciplina: <https://rsdevigo.github.io/apostila_texturizacao>
- Projeto Pedagógico do Curso (PPC) — Tecnologia em Jogos Digitais, IFMS Dourados, 2025.
- Mood boards e referências visuais por tema (curados pelo professor em parceria com os estudantes).
- Repositório compartilhado de assets para referência (modelos low-poly para prática de UV e bake).

### 7.3 Hardware e Infraestrutura

- Laboratório de informática com estações equipadas com GPU compatível com viewport rendering.
- Projetor ou tela de demonstração para mini-aulas e críticas.
- Acesso à internet para referências visuais e documentação dos softwares.

---

## 8. Estratégias de Avaliação

A avaliação é contínua, processual e baseada em artefatos produzidos ao longo do semestre. Não há provas ou testes escritos. O estudante é avaliado pela qualidade e evolução do trabalho produzido, pela participação ativa nas críticas coletivas e pela entrega do Projeto Final. A nota final é calculada pela fórmula:

```
NF = (PA × 0,40) + (CC × 0,20) + (PF × 0,40)
```

| Instrumento | Descrição | Peso | Quando |
|---|---|---|---|
| **Portfolio de Artefatos (PA)** | Conjunto de entregas parciais ao longo do semestre: mapas UV, materiais PBR, texturas artísticas e bake. Avaliados com rubrica por entrega. | 40% | Semanas 3–14 |
| **Críticas Coletivas (CC)** | Participação nas críticas semanais como apresentador e como avaliador dos colegas. Avalia comunicação, autoavaliação e incorporação de feedback. | 20% | Semanas 2–16 |
| **Projeto Final – Kit Modular (PF)** | Kit Modular de Ambiente completo com 5–10 assets texturizados, importados e funcionais na Unity. Defesa oral com justificativa das escolhas técnicas e artísticas. | 40% | Semana 17 |

---

## 9. Critérios de Avaliação

| Critério | Insuficiente (0–4) | Básico (5–6) | Satisfatório (7–8) | Excelente (9–10) |
|---|---|---|---|---|
| **Qualidade Técnica UV** | Sobreposição evidente, distorção severa. | UV funcional com distorções menores. | UV bem distribuído, mínima distorção. | UV otimizado, texels uniformes, sem sobreposição. |
| **Qualidade dos Mapas PBR** | Mapas inconsistentes ou ausentes. | Mapas básicos presentes, sem coerência. | Metallic, roughness e normal coerentes. | Mapas fisicamente plausíveis com detalhes de bake. |
| **Leitura Visual do Asset** | O asset não comunica o material. | Materiais perceptíveis sem consistência. | Assets com leitura clara e coerente. | Alta qualidade visual; materiais convincentes no motor. |
| **Otimização e Performance** | Texturas superdimensionadas, sem atlas. | Tamanho razoável, atlas incompleto. | Textures e atlas apropriados à plataforma. | Totalmente otimizado: atlas, mipmaps, compressão. |
| **Documentação e Reflexão** | Sem justificativas das decisões. | Decisões superficialmente justificadas. | Justificativas claras das escolhas técnicas. | Reflexão crítica sobre processo, erros e aprendizados. |

### 9.1 Critérios de Participação nas Críticas Coletivas

- Apresentação clara do trabalho em progresso (o que foi feito, qual foi a intenção, quais dificuldades foram encontradas).
- Autoavaliação honesta com identificação de pontos de melhoria.
- Qualidade do feedback dado aos pares (específico, construtivo, baseado em critérios técnicos ou artísticos).
- Evidência de incorporação de feedback recebido em entregas subsequentes.

---

## 10. Recuperação Paralela

A recuperação paralela ocorre de forma contínua, integrada à dinâmica da disciplina. Estudantes que não atingirem a pontuação mínima em uma entrega do Portfolio de Artefatos (nota < 5,0) terão a oportunidade de retrabalhar o artefato e entregá-lo novamente até a semana seguinte à devolução do feedback. A nota do artefato refeito substitui a nota original.

O professor indicará formalmente, por escrito, os pontos que devem ser revisados. O processo de recuperação paralela não se aplica às Críticas Coletivas, pois sua natureza é processual e presencial.

---

## 11. Recuperação Final

Estudante com nota final entre 4,0 e 6,9 (exclusive) terá direito à Recuperação Final, conforme normativa institucional do IFMS. A recuperação consistirá em:

- Entrega revisada do Projeto Final (Kit Modular de Ambiente) com correções e melhorias documentadas.
- Defesa oral de no mínimo 15 minutos na qual o estudante apresenta as mudanças realizadas e justifica as decisões de revisão.

A nota da Recuperação Final (NR) substituirá apenas a nota do Projeto Final (PF) na fórmula de cálculo, não alterando as notas do Portfolio ou das Críticas Coletivas:

```
NF (recuperação) = (PA × 0,40) + (CC × 0,20) + (NR × 0,40)
```

A nota máxima passível de ser atingida após a Recuperação Final é 7,0 (sete), conforme regulamento acadêmico do IFMS.

---

## 12. Conteúdo Programático por Unidade

### Unidade I — Fundamentos e Mapeamento UV (Semanas 1–4)

- Introdução à disciplina, apresentação do projeto integrador e escolha de temas.
- Definição de material e textura em computação gráfica.
- Projeção de textura e conceitos de mapeamento UV.
- Prática de abertura de malha: Smart UV Project, Seams, Unwrap manual no Blender.
- Análise de distorção e otimização de layout UV.

### Unidade II — Materiais PBR e Workflow (Semanas 5–8)

- Fundamentos do Physically Based Rendering (PBR).
- Mapas PBR: Diffuse/Albedo, Metallic, Roughness, Normal, Subsurface.
- Criação de texturas seamless e tileable.
- Workflow de criação de materiais no 3D Coat: camadas, projeção e exportação.
- Geração procedural de elementos em texturas.

### Unidade III — Pintura Digital e Bake (Semanas 9–12)

- Texturização artística por pintura digital e uso de stencils no 3D Coat.
- Bake de texturas: Normal Map, Ambient Occlusion, Curvature, ID Map.
- Transferência de detalhe de high-poly para low-poly.
- Integração de resultado de bake ao workflow PBR.

### Unidade IV — Otimização e Integração ao Motor (Semanas 13–16)

- Texture Atlas e organização de múltiplos assets em uma única textura.
- Trim Sheets: conceito, criação e aplicação.
- UDIMs e Multi Tile Texture para assets complexos.
- Otimização de performance: tamanho, compressão, mipmaps e empacotamento de canais.
- Abertura de malha para mapa de iluminação (lightmap UV).
- Importação, configuração de materiais e renderização na Unity.

### Unidade V — Projeto Final e Apresentação (Semana 17)

- Finalização do Kit Modular de Ambiente.
- Apresentação e defesa oral com crítica aberta.
- Autoavaliação final documentada.

---

## 13. Cronograma Resumido

| Semana | Conteúdo / Atividade | Entrega / Marco |
|---|---|---|
| 1 | Apresentação da disciplina, SBL, escolha de temas | Tema do Kit definido |
| 2 | Fundamentos de textura e UV; primeiro critique | — |
| 3 | Abertura de malha UV — Smart Unwrap e Seams | UV Map 01 (asset simples) |
| 4 | Layout UV, distorção e otimização | UV Map 02 (asset do projeto) |
| 5 | Fundamentos PBR; criação de Albedo e Normal | — |
| 6 | Metallic, Roughness, Subsurface no 3D Coat | Set PBR 01 (1 material) |
| 7 | Texturas seamless e geração procedural | — |
| 8 | Workflow completo PBR no 3D Coat | Set PBR 02 (2 materiais) |
| 9 | Pintura digital: camadas e máscaras | — |
| 10 | Stencils e detalhamento artístico | Textura Artística 01 |
| 11 | Bake: Normal Map e AO (high→low) | — |
| 12 | Bake avançado: Curvature e ID Map | Bake completo do asset principal |
| 13 | Texture Atlas — conceito e criação | — |
| 14 | Trim Sheets e UDIMs | Atlas / Trim Sheet do Kit |
| 15 | Otimização: compressão, mipmaps, empacotamento | — |
| 16 | Integração na Unity: materiais, lightmap UV | Assets importados na Unity |
| 17 | Apresentação e defesa do Projeto Final | Kit Modular de Ambiente completo |

---

## 14. Bibliografia Básica

- DEVIGO, Rodrigo. *Apostila de Texturização*. IFMS Campus Dourados, 2026. Disponível em: <https://rsdevigo.github.io/apostila_texturizacao>
- AKENINE-MÖLLER, Tomas; HAINES, Eric; HOFFMAN, Naty. *Real-Time Rendering*. 4. ed. Boca Raton: CRC Press, 2018.
- ALLEGORITHMIC. *Substance PBR Guide*. Disponível em: <https://academy.substance3d.com/courses/the-pbr-guide-part-1>

---

## 15. Bibliografia Complementar

- BLENDER FOUNDATION. *Blender Reference Manual*. Disponível em: <https://docs.blender.org/manual/en/latest/>
- 3DCOAT. *3DCoat Documentation*. Disponível em: <https://3dcoat.com/manual/>
- UNITY TECHNOLOGIES. *Unity Manual: Materials and Shaders*. Disponível em: <https://docs.unity3d.com/Manual/Shaders.html>
- MARMOSET. *Toolbag Baking Reference*. Disponível em: <https://marmoset.co/posts/toolbag-baking-reference/>
- FLICK, Javier. *Physically Based Rendering: From Theory to Implementation*. Disponível em: <https://pbr-book.org/>
- DIRECTXTEX. *Block Compression*. Microsoft Docs. Disponível em: <https://docs.microsoft.com/en-us/windows/win32/direct3d11/texture-block-compression>

---

## Aprovação

Dourados, MS, Julho de 2026.

&nbsp;

___

Prof. Rodrigo Devigo
Professor Responsável — Disciplina de Texturização

&nbsp;

___

Coordenação do Curso
Tecnologia em Jogos Digitais — IFMS Campus Dourados
