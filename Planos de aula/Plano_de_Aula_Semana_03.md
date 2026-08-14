# Plano de Aula — Semana 3
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** I — Fundamentos, Mapeamento UV e Definição do Hero Asset (Semanas 1–5)
**Tema da semana:** Moodboard temático e definição do Hero Asset Referência
**Apostila:** Revisão da Parte I, Cap. 1 (aplicada à escolha do tema); leitura antecipada da Parte II, Cap. 5 — UV Unwrapping, para a Semana 4
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — Roda de temas

---

## O que já foi ministrado (Semanas 1–2 — não repetir)

Na **Semana 1**, os estudantes foram apresentados ao trabalho interdisciplinar (Pintura Digital e Arte Conceitual, Texturização, Modelagem 3D e Level Design; entregável final = fase caminhável na Unity; tema = mundo fantástico a partir de elementos regionais de MS ou do estado de origem) e participaram da dinâmica de ideação cultural: apresentação de 5 props culturais reais de MS (Cerâmica Terena, Viola de Cocho, Tereré/erva-mate, Complexo Ferroviário Rede Noroeste, Igreja/Catedral colonial), pesquisa em grupo especialista, reagrupamento jigsaw e aplicação de técnicas de ideação forçada (matriz morfológica, SCAMPER, conexões forçadas). Cada estudante saiu com **1–2 ideias individuais de recorte temático, sem compromisso formal**.

Na **Semana 2**, os estudantes tiveram o primeiro contato técnico real com o Blender: conceito de espaço UV (0–1), distorção, sobreposição, os quatro tipos de projeção (planar, cilíndrica, esférica, cúbica) e uso do checkerboard como ferramenta de diagnóstico, praticados em objetos geométricos neutros (cubo, cilindro, esfera, prop neutro) — **sem qualquer amarração temática**.

**Importante:** até aqui, nenhum estudante tem tema, moodboard ou Hero Asset oficiais — apenas ideias em amadurecimento e uma ferramenta técnica (projeção UV) ainda não aplicada a um asset real. Esta é a semana em que isso muda: **o tema e o Hero Asset Referência passam a ser dados oficiais do trabalho de cada estudante a partir de hoje**, e todo material das semanas seguintes vai tratá-los como definidos.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Consolidar um moodboard temático curado (mínimo de 10 referências organizadas) que traduza visualmente o recorte cultural amadurecido desde a Semana 1 em um mundo fantástico coerente.
2. Explicar o conceito de Hero Asset Referência — uma peça única e altamente representativa do tema que funciona como prova de conceito do pipeline completo (UV → PBR → 3D Coat) antes de escalar para o Kit Modular inteiro.
3. Selecionar e justificar por escrito um Hero Asset Referência, avaliando três critérios: legibilidade do tema, viabilidade técnica e potencial de reaproveitamento de linguagem visual no restante do kit.
4. Comunicar oralmente, de forma clara e justificada, a proposta temática e a escolha do Hero Asset para a turma e o professor (primeiro exercício formal de comunicação visual da disciplina).
5. Alinhar com Modelagem 3D e Level Design o briefing do Hero Asset Referência, viabilizando sua modelagem para a Semana 4.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Início do registro formal de processo: pasta de referências organizada (moodboard), primeira decisão documentada e justificada por escrito |
| C2 — Direção Artística | Primeira articulação da proposta visual: paleta e linguagem ainda em formação — nível esperado 2–3 da rubrica, não mais que isso nesta fase |
| C10 — Participação nas Critiques | Engajamento na roda de temas: clareza ao apresentar a própria proposta e qualidade das perguntas/comentários aos colegas |

> C3 (UV Mapping) e C4–C9 ainda não são exigidos — não há UV, material ou textura aplicados a um asset real até aqui. Esta semana não gera nota isolada, mas **abre o processo que será avaliado na Crítica Formal da Semana 4 (C3)**: um moodboard fraco ou um Hero Asset mal justificado nesta semana compromete diretamente a qualidade do que chega à CF1.

---

## Recursos necessários

- Computadores ou dispositivos para apresentação de referências visuais (PDF, PNG ou link de moodboard online — Pinterest, PureRef, Milanote ou equivalente)
- Projetor para a roda de temas
- Modelo de justificativa de Hero Asset (template curto: nome do asset, 1 parágrafo de justificativa) — professor pode distribuir como documento compartilhado
- Apostila — revisão da Parte I, Cap. 1, e leitura antecipada da Parte II, Cap. 5 (disponibilizada antes da aula)
- Canal de comunicação com os professores de Pintura Digital e Arte Conceitual e de Modelagem 3D e Level Design, para alinhar o cronograma de entrega das referências e do briefing do Hero Asset entre as três disciplinas

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**O que é um Hero Asset Referência e por que ele existe**

Objetivo: dar significado técnico e estratégico à escolha que os estudantes vão fazer hoje, antes de pedir que decidam.

**Desenvolvimento:**

Abrir com uma pergunta para a turma: *"Se vocês tivessem que provar, com uma única peça, que o pipeline inteiro — UV, PBR, pintura no 3D Coat — funciona para o tema de vocês, qual peça escolheriam?"* Deixar 2–3 respostas antes de nomear o conceito.

**Conteúdo a cobrir:**

1. **Definição de Hero Asset Referência.** Uma peça única, não necessariamente parte literal do Kit Modular final, que representa com máxima clareza o tema escolhido. Ela funciona como prova de conceito: é nela que cada etapa do pipeline (abertura de UV na Semana 4, material PBR na Semana 6–7, texturização no 3D Coat na Semana 8–9) é testada pela primeira vez, antes de escalar para o conjunto de assets do Kit Modular a partir da Semana 10.

2. **Por que não começar direto pelo Kit Modular.** Modelar, abrir UV e texturizar uma peça só é mais rápido de iterar e corrigir do que descobrir um problema de pipeline depois de já ter dez assets modelados. O Hero Asset é onde os erros são baratos.

3. **Três critérios para escolher um bom Hero Asset:**
   - **Legibilidade do tema:** olhando só para essa peça, dá para reconhecer o mundo fantástico proposto? Ela concentra os elementos mais distintivos do recorte cultural trabalhado desde a Semana 1?
   - **Viabilidade técnica:** a peça tem complexidade adequada a um semestre de aprendizagem — nem tão simples que não desafie o pipeline (um cubo texturizado não prova nada), nem tão complexa que consuma todo o tempo disponível (uma arquitetura inteira não é um Hero Asset, é o Kit Modular inteiro).
   - **Potencial de reaproveitamento:** os materiais, a paleta e a linguagem de desgaste definidos nessa peça poderão ser reaproveitados nos assets secundários e de repetição do kit a partir da Semana 10? Um Hero Asset "isolado" demais do resto do kit gera retrabalho depois.

4. **O papel do moodboard.** O moodboard não é uma coleção de imagens bonitas — é a evidência visual de que a proposta temática é coerente e específica. Um moodboard genérico ("fantasia medieval") não orienta escolha nenhuma; um moodboard específico (por exemplo: cerâmica Terena reinterpretada como arquitetura mágica, paleta de barro queimado e pigmento mineral) já sugere naturalmente qual peça vira o Hero Asset.

> **Nota do professor:** não entre em detalhes técnicos de UV ou material nesta mini aula — isso pertence às Semanas 4 e 6–8. O foco de hoje é decisão de projeto e comunicação visual, não execução técnica. Se surgir a pergunta "como eu abro o UV disso?", responda: *"Isso é semana que vem — hoje o Modelagem 3D e Level Design ainda está desenhando essa peça com vocês. Primeiro escolhemos o quê, depois o como."*

---

### Demonstração — 20 minutos

**Exemplos de Hero Assets de referência e critério de coerência com o moodboard**

**Parte 1 — Exemplos de projetos de referência (12 min):**

1. Apresentar 3–4 exemplos de projetos publicados (ArtStation ou portfólios equivalentes) em que um único asset — uma arma, um altar, uma porta, um totem — funciona claramente como "peça-chave" de um kit modular maior.
2. Para cada exemplo, guiar a turma a identificar: *"O que essa peça está me dizendo sobre o mundo antes mesmo de eu ver o resto do kit?"* — praticando a leitura de legibilidade temática que será exigida deles.
3. Mostrar, quando disponível, o moodboard que provavelmente originou aquele Hero Asset, e apontar a correspondência direta entre referência e execução: paleta, formas, materiais.

**Parte 2 — Critério de avaliação da coerência moodboard → Hero Asset (8 min):**

1. Demonstrar, com um exemplo fictício rápido (pode ser um recorte simples, tipo "ferrovia abandonada + mitologia local"), como transformar um conjunto de referências dispersas em uma escolha de Hero Asset justificável em um parágrafo.
2. Modelar em voz alta a estrutura da justificativa que os estudantes vão escrever: *"Este objeto representa o tema porque [elemento do moodboard] + é viável porque [escopo/técnica] + vai se conectar ao resto do kit porque [material/paleta reaproveitável]."*

> **Nota do professor:** não é necessário abrir Blender ou 3D Coat nesta demonstração — é a primeira aula inteiramente conceitual/curatorial do semestre. Isso é proposital: reforça que decisão de projeto é etapa distinta de execução técnica.

---

### Produção em Estúdio — 50 minutos

**Consolidação do moodboard e primeira definição do Hero Asset**

**Consigna entregue verbalmente:**

> *"Primeira etapa: organizem as referências que vocês já têm de Pintura Digital e Arte Conceitual e das ideias da Semana 1 em um moodboard único, com pelo menos 10 imagens. Não precisa ser bonito ainda — precisa ser específico. Segunda etapa: a partir desse moodboard, listem 2–3 candidatos a Hero Asset e comecem a testar cada um contra os três critérios que vimos: legibilidade, viabilidade, reaproveitamento."*

**Atividade estruturada:**

1. **(20 min) Consolidação do moodboard.** Reunir e organizar referências já produzidas em Pintura Digital e Arte Conceitual, complementando com novas buscas se necessário. Mínimo de 10 referências, organizadas por categoria (paleta, formas/silhueta, materiais, referência cultural direta).
2. **(20 min) Lista de candidatos a Hero Asset.** A partir do moodboard, cada estudante lista 2–3 objetos/peças candidatas e anota, para cada uma, uma frase rápida sobre cada critério (legibilidade / viabilidade / reaproveitamento).
3. **(10 min) Conversa informal em duplas.** Estudantes trocam suas listas em duplas e testam a legibilidade do tema do colega: *"Olhando só para essa lista de candidatos, que mundo eu imagino?"* — feedback rápido antes da decisão final.

**Papel do professor:**

Circular pelo estúdio perguntando:
- *"Esse moodboard me diz um lugar específico, ou poderia ser qualquer fantasia genérica?"*
- *"Se Modelagem 3D e Level Design tivesse que modelar isso essa semana, dá tempo?"*
- *"Essa peça puxa uma paleta ou só um objeto isolado?"*

Identificar estudantes com moodboard ainda disperso ou genérico — eles vão precisar de atenção prioritária no Encontro 2, antes da decisão final do Hero Asset.

> **Nota do professor:** não force a decisão final do Hero Asset ainda neste encontro. O objetivo do Encontro 1 é chegar a candidatos justificáveis; a escolha definitiva e o registro formal acontecem no Encontro 2, já informados pela roda de temas.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: Roda de temas**

Cada estudante apresenta, em até 1 minuto, seu moodboard e o(s) candidato(s) a Hero Asset ainda em aberto.

**Roteiro:**

1. **(1 min por estudante, ajustar conforme tamanho da turma)** Cada estudante mostra o moodboard na tela e diz: *"Meu tema é ___. Meu candidato a Hero Asset é ___, porque ___."*
2. **(comentário rápido da turma e do professor, 1–2 perguntas no máximo por apresentação)** Perguntas focadas nos três critérios: *"Isso está legível?"*, *"Isso é viável em uma semana de modelagem?"*, *"Isso puxa material para o resto do kit?"*
3. **(fechamento, 3–5 min no total)** Professor sistematiza padrões observados na turma: temas que se repetem, riscos comuns (escopo grande demais, moodboard genérico), e reforça que a decisão final acontece hoje, na produção em estúdio que segue.

> **Nota do professor:** o objetivo da roda de temas não é aprovar ou reprovar propostas — é dar à turma um primeiro treino de comunicação visual e justificativa de decisões, competência central da disciplina (C10). Mantenha o ritmo rápido; é preferível ouvir todos brevemente do que aprofundar em poucos.

**Conectar à rubrica:** ao final, mencionar explicitamente: *"O que vocês acabaram de fazer — apresentar uma proposta e justificar por que ela funciona — é exatamente o tipo de comunicação que a Crítica Formal da Semana 4 vai exigir de novo, já com um UV real na tela. Fica mais fácil na segunda vez."*

---

### Produção em Estúdio — 60 minutos

**Fechamento do moodboard curado e definição final do Hero Asset**

**Consigna:**

> *"Com o que ouviram na roda de temas, fechem a decisão. Escolham um único Hero Asset, escrevam a justificativa em um parágrafo usando os três critérios, e finalizem o moodboard como arquivo de entrega. Depois, registrem esse briefing para compartilhar com Modelagem 3D e Level Design — é a peça que eles vão modelar a partir de agora."*

**Atividade:**

1. Decisão final do Hero Asset Referência (um único candidato, não mais uma lista).
2. Redação da justificativa (1 parágrafo, cobrindo legibilidade, viabilidade técnica e potencial de reaproveitamento).
3. Finalização do moodboard como arquivo de entrega (PNG, PDF ou link), com no mínimo 10 referências organizadas.
4. Registro do briefing do Hero Asset para Modelagem 3D e Level Design: descrição textual + referências visuais mais diretas do moodboard, formato definido em conjunto com o professor daquela disciplina (documento compartilhado, formulário ou entrega direta em aula, conforme combinado entre os professores).
5. Nomear os arquivos com o padrão `[Nome]_Moodboard_Semana03` e `[Nome]_HeroAsset_Justificativa_Semana03`.

**Papel do professor:**

Priorizar atenção individual para:
- Estudantes que chegaram ao Encontro 2 com moodboard ainda disperso ou tema pouco específico — ajudar a fechar o recorte antes do fim da aula, mesmo que de forma mais simples.
- Estudantes em dúvida entre dois candidatos a Hero Asset — usar os três critérios como desempate, não a preferência estética isolada.
- Garantir que todos os estudantes tenham, ao final da aula, um Hero Asset único e comunicável a Modelagem 3D e Level Design — a modelagem começa imediatamente após esta semana, e um briefing tardio atrasa a Semana 4 inteira.

Para quem termina rápido: revisar o moodboard de um colega e sugerir, por escrito, uma referência que falta ou uma inconsistência de paleta — pratica leitura crítica antes da Semana 4.

> **Nota do professor:** não permita que a decisão do Hero Asset fique em aberto além deste encontro. O cronograma da Semana 4 depende de Modelagem 3D e Level Design já ter um briefing fechado para modelar.

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min) Síntese rápida pelo professor:** *"A partir de hoje, tema e Hero Asset não são mais 'ideia em amadurecimento' — são dados do projeto de vocês. Tudo que vier a partir da Semana 4 assume que essa decisão está tomada."*

2. **(3 min) Reflexão individual registrada** (post-it físico, digital ou comentário no arquivo):
   *"Complete a frase: 'Escolhi este Hero Asset porque ____. O que mais me preocupa nessa escolha é ____.'"*
   Quem quiser compartilhar, pode — não é obrigatório.

3. **(3 min) Ponte para a Semana 4:** *"Na próxima semana, vocês recebem o Hero Asset Referência modelado por Modelagem 3D e Level Design e abrem o UV dele de verdade — com seams manuais, não mais projeção automática. É a primeira Crítica Formal do semestre: vai valer nota, com rubrica e autoavaliação. Revisem o Nível 3 do Critério 3 na Rubrica Mestre antes de virem para a aula."*

4. **(2 min) Confirmação das entregas:**
   - Moodboard temático curado (PNG, PDF ou link), mínimo 10 referências
   - Justificativa do Hero Asset Referência (1 parágrafo, cobrindo os três critérios)
   - Briefing do Hero Asset compartilhado com Modelagem 3D e Level Design

---

## Possíveis Dificuldades

**1. Moodboard genérico ou disperso demais**
Alguns estudantes chegam com referências bonitas mas sem coerência entre si ("fantasia" em geral, sem recorte cultural específico). Estratégia: voltar à pergunta da Semana 1 — *"Qual dos 5 props vocês trabalharam no jigsaw está por trás dessa referência? Se não conseguem apontar, o recorte ainda está solto demais."*

**2. Indecisão entre múltiplos candidatos a Hero Asset**
Estudante gosta de mais de uma ideia e não consegue escolher. Estratégia: aplicar os três critérios como checklist objetivo e, em caso de empate, priorizar viabilidade técnica — é melhor um Hero Asset viável e bem executado do que um ambicioso e inacabado.

**3. Hero Asset escolhido é, na prática, um ambiente inteiro, não uma peça**
Comum quando o estudante confunde Hero Asset com Kit Modular. Estratégia: perguntar *"Se eu tirasse essa peça de dentro do cenário e colocasse sozinha em um pedestal, ela ainda contaria a história do tema?"* — se a resposta exigir o cenário inteiro ao redor, não é um Hero Asset, é uma cena.

**4. Justificativa escrita superficial ("porque achei bonito")**
Estudante escolhe corretamente mas não consegue articular por quê. Estratégia: usar a estrutura de frase modelada na demonstração ("representa o tema porque... é viável porque... vai se conectar porque...") como andaime obrigatório na primeira vez.

**5. Desalinhamento com Modelagem 3D e Level Design sobre o que é modelável em uma semana**
Estudante escolhe um Hero Asset tecnicamente inviável no prazo (muita complexidade de forma, muitas peças móveis). Estratégia: se possível, ter um canal aberto com o professor de Modelagem 3D e Level Design durante a própria aula para validação rápida de escopo; caso contrário, professor de Texturização aplica um filtro conservador — na dúvida, sugerir simplificar.

**6. Estudante ainda apegado à ideia de "esperar inspirar" em vez de decidir**
Depois de semanas de amadurecimento livre, alguns resistem a fechar a decisão. Estratégia: lembrar que a decisão de hoje não é permanente e imutável — pequenos ajustes de escopo ainda são possíveis nas próximas semanas — mas o pipeline não anda sem uma peça definida para trabalhar.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Moodboard sem recorte cultural específico | Perguntar: *"Qual dos 5 props da Semana 1 está por trás dessa imagem?"* Reconectar à pesquisa já feita, em vez de pedir referências novas do zero. |
| Estudante indeciso entre candidatos | Aplicar os três critérios como checklist; em empate, priorizar viabilidade técnica sobre preferência estética. |
| Hero Asset na verdade é uma cena inteira | *"Se essa peça estivesse sozinha em um pedestal, ainda contaria a história?"* Se não, é preciso recortar uma única peça de dentro da cena. |
| Justificativa vaga ou só estética | Oferecer o andaime de frase (representa porque / é viável porque / se conecta porque) até o estudante conseguir preencher com conteúdo específico. |
| Escopo do Hero Asset inviável para Modelagem 3D e Level Design modelar a tempo | Sugerir simplificação de forma, mantendo os elementos mais legíveis do tema; validar com o professor da outra disciplina quando possível. |
| Turma dispersa na roda de temas | Impor timebox rígido de 1 minuto por estudante com cronômetro visível; comprimir comentários a 1 pergunta por apresentação. |
| Estudante resistente a fechar a decisão | Reforçar que pequenos ajustes de escopo ainda cabem adiante, mas o pipeline da Semana 4 depende de uma peça definida hoje. |

---

## Evidências de Aprendizagem

| Evidência | Objetivo(s) relacionado(s) | Critério da Rubrica | Como avaliar |
|---|---|---|---|
| Moodboard temático curado (mínimo 10 referências, organizadas) | Objetivo 1 | C1 — Processo de Projeto | Existência do registro organizado; especificidade e coerência interna das referências (não genéricas) |
| Justificativa escrita do Hero Asset Referência (1 parágrafo) | Objetivos 2, 3 | C1, C2 — Processo de Projeto / Direção Artística (nível inicial) | Presença explícita dos três critérios (legibilidade, viabilidade, reaproveitamento); clareza da argumentação |
| Participação na roda de temas | Objetivo 4 | C10 — Participação nas Critiques | Clareza da apresentação em até 1 minuto; qualidade das perguntas feitas aos colegas |
| Briefing do Hero Asset compartilhado com Modelagem 3D e Level Design | Objetivo 5 | C1 — Processo de Projeto | Existência e clareza do registro; completude suficiente para viabilizar a modelagem na semana seguinte |

> **Nota:** esta semana não gera nota isolada, mas é a base direta da Crítica Formal da Semana 4 (CF1) — um moodboard fraco ou um Hero Asset mal escolhido hoje compromete diretamente C2 e C3 na próxima semana. O professor registra observações qualitativas individuais sobre especificidade temática e clareza de justificativa, para acompanhamento prioritário até a CF1.

---

## Entrega da Semana 3

| Entrega | Formato | Escopo | Prazo |
|---|---|---|---|
| Moodboard temático curado | PNG, PDF ou link (Pinterest/PureRef/Milanote) | Individual | Até o fim do segundo encontro |
| Justificativa do Hero Asset Referência (1 parágrafo) | Texto (comentário no arquivo, `.txt` ou `.docx`) | Individual | Até o fim do segundo encontro |
| Briefing do Hero Asset para Modelagem 3D e Level Design | Conforme combinado entre os professores (documento compartilhado, formulário ou entrega em aula) | Individual | Até o fim do segundo encontro |

> Não há entrega técnica em Blender/3D Coat nesta semana — a primeira operação sobre o Hero Asset real (abertura de UV) começa na Semana 4, primeira Crítica Formal do semestre.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 3 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
