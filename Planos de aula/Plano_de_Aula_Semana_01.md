# Plano de Aula — Semana 1
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** I — Fundamentos e Mapeamento UV  
**Tema:** Apresentação da disciplina, pipeline e escolha de tema do Kit Modular  
**Apostila:** Cap. 1 — Visão geral do pipeline de texturização  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** Informal (circulante em estúdio)

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Descrever o pipeline de texturização da disciplina (Blender → 3D Coat → Unity) e a função de cada etapa.
2. Diferenciar textura raster de procedural e identificar quando cada abordagem é usada.
3. Selecionar e organizar referências visuais coerentes com um tema de ambiente.
4. Definir formalmente o tema do seu Kit Modular com justificativa visual e descritiva.
5. Navegar nos workspaces básicos do Blender (Shading, UV Editor, Viewport Shading).

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco |
|---|---|
| C1 — Processo de Projeto | Organização da pasta de referências e do moodboard |
| C2 — Direção Artística | Coerência visual das referências e clareza da proposta temática |
| C10 — Participação | Engajamento na crítica informal e na escolha coletiva de temas |

> Os demais critérios (C3–C9) ainda não são exigidos. Esta semana é exclusivamente de orientação, pesquisa e definição de proposta.

---

## Recursos necessários

- Computadores com Blender instalado (versão 3.x ou 4.x)
- Acesso à internet para pesquisa de referências
- Ferramenta de montagem de moodboard: PureRef (recomendado), Google Slides, Figma ou similar
- Projetor para demonstração
- Exemplos de kits modulares prontos (preparados pelo professor): 1 Medieval, 1 Sci-Fi, 1 Pós-apocalíptico
- Apostila — Cap. 1 (disponibilizada antes da aula)

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**O que é textura e material em computação gráfica?**

Objetivo: situar o estudante no vocabulário central da disciplina antes de qualquer ferramenta.

**Desenvolvimento:**

Começar com uma pergunta para a turma: *"Qual a diferença entre a cor de um objeto e o material dele?"* Deixar 2–3 respostas rápidas antes de apresentar o conceito.

**Conteúdo a cobrir:**

- **Textura** = imagem mapeada sobre uma superfície 3D para representar cor, rugosidade, reflexo etc.
- **Material** = conjunto de propriedades que define como a superfície reage à luz (inclui uma ou mais texturas).
- **Raster vs. Procedural:** raster é uma imagem bitmap (pixels); procedural é gerado por algoritmo em tempo real. Vantagens e limitações de cada um.
- **O pipeline da disciplina:** Blender (modelagem + UV) → 3D Coat (texturização PBR manual) → Unity (integração no motor). Cada software tem um papel específico — nenhum é substituível pelo outro nesse fluxo.
- **Projeto semestral:** cada estudante construirá um Kit Modular de Ambiente do início ao fim. Todos os conteúdos do semestre serão aplicados a esse único projeto.

> **Nota do professor:** Evite entrar em detalhes técnicos de PBR ou UV agora. O objetivo desta mini aula é criar senso de trajetória, não de profundidade. Se houver perguntas avançadas, responda com: *"Vamos chegar nisso na semana X."*

---

### Demonstração — 20 minutos

**Tour pelo Blender + exemplos de kits modulares**

**Parte 1 — Blender (10 min):**

Abrir o Blender e mostrar, sem aprofundar:

1. **Shading Workspace** — onde os materiais são configurados. Mostrar o node editor e o Principled BSDF sem explicar cada nó.
2. **UV Editor** — mostrar a aba e um modelo simples já mapeado. Não explicar como mapear — isso vem na Semana 2.
3. **Viewport Shading** — alternar entre Solid, Material Preview e Rendered. Mostrar o impacto visual de cada modo.

O objetivo é que o estudante reconheça esses espaços quando voltar ao software. Não é tutorial — é orientação espacial.

**Parte 2 — Exemplos de kits modulares (10 min):**

Mostrar 2–3 kits modulares de referência (imagens ou vídeo). Para cada um, comentar:
- Qual o tema?
- Que tipos de assets compõem o kit (parede, chão, pilar, detalhe)?
- O que torna o kit visualmente coeso?

> **Nota do professor:** Escolha kits com qualidade de portfólio — ArtStation é boa fonte. Evite mostrar apenas o produto final sem contexto de processo.

---

### Produção em Estúdio — 50 minutos

**Pesquisa e montagem de moodboard**

**Consigna entregue verbalmente:**

> *"Você vai trabalhar com esse tema pelo semestre inteiro. O moodboard não é decoração — é sua bússola visual. Toda decisão de cor, material e detalhe vai ser comparada a ele nas críticas. Escolha bem."*

**Atividade:**

1. Cada estudante define provisoriamente um tema (Medieval, Sci-Fi, Pós-apocalíptico, Fantasia, Cyberpunk ou outro aprovado pelo professor).
2. Pesquisa e coleta no mínimo 10 referências visuais: ambientes, texturas, iluminação e assets do tema.
3. Organiza as referências em um painel visual usando PureRef, Google Slides ou Figma.
4. Começa a redigir um parágrafo de justificativa: *Por que esse tema? Que atmosfera você quer criar? Quais materiais predominam no ambiente?*

**Papel do professor:**

Circular pelo estúdio, fazer perguntas que aprofundem a escolha:
- *"Por que essa referência específica? O que ela te diz sobre o material?"*
- *"Esse tom de iluminação é o que você quer para o kit inteiro?"*
- *"Você já pensou em que tipo de assets vão compor esse ambiente?"*

Não corrigir nem aprovar temas ainda — apenas provocar reflexão.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: Roda de temas**

Cada estudante mostra brevemente (1–2 min) seu moodboard em progresso e declara o tema escolhido. A turma e o professor fazem uma pergunta ou comentário por apresentação.

**Roteiro da crítica:**

1. Estudante mostra o moodboard na tela.
2. Professor pergunta: *"Em uma frase, qual é a atmosfera que você quer comunicar?"*
3. Turma: *"O que mais chamou atenção nessas referências?"*
4. Professor fecha com uma observação sobre coerência visual ou uma sugestão de referência adicional.

**O professor observa e anota (para C10):**
- Quem participou ativamente com perguntas para os colegas
- Quem demonstrou já ter clareza sobre a proposta visual
- Quem ainda está inseguro — esses estudantes recebem atenção individual no estúdio

> **Nota do professor:** Se houver estudantes com o mesmo tema, não há problema. Kits diferentes do mesmo tema são ótimos para comparação visual nas críticas. Se houver temas muito genéricos ("aventura", "floresta"), ajude a estreitar: *"Que período? Que clima? Que estado de conservação dos materiais?"*

---

### Produção em Estúdio — 60 minutos

**Finalização do moodboard e documento de definição de tema**

**Atividade:**

1. Incorporar os feedbacks recebidos na crítica e refinar o moodboard (adicionar, remover ou reorganizar referências).
2. Redigir o **Documento de Definição de Tema** — uma página com:
   - Nome do tema
   - Descrição da atmosfera visual (3–5 frases)
   - Lista de 3 materiais predominantes (ex.: pedra desgastada, madeira úmida, metal enferrujado)
   - Moodboard finalizado anexado ou incorporado
3. Salvar o arquivo na pasta do projeto com nomenclatura: `[Nome]_Kit_[Tema]_Semana01.pdf` ou `.png`.

**Papel do professor:**

Continuar circulando. Priorizar os estudantes que na crítica demonstraram dificuldade de escolha ou moodboards sem coerência visual.

Perguntas mediadoras para quem trava:
- *"Se esse ambiente fosse um personagem, qual seria sua história?"*
- *"Que materiais aparecem com mais frequência nessas referências? Começa por aí."*
- *"Esquece o 3D por agora. Esse ambiente existe em algum filme, jogo ou lugar real que te inspira?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min)** Professor faz uma síntese rápida da semana: *"Hoje estabelecemos o ponto de partida. Tudo que vamos aprender — UV, PBR, bake, otimização — vai ser aplicado a esse kit que vocês escolheram."*
2. **(3 min)** Cada estudante registra no verso do documento (ou em um post-it digital): uma coisa que ainda precisa resolver no seu tema antes da próxima semana.
3. **(3 min)** Apresentação do que vem na Semana 2: *"Na próxima semana, entendemos o que é um mapa UV e por que ele existe. Tragam o Blender instalado e o moodboard finalizado."*
4. **(2 min)** Confirmação das entregas:
   - Moodboard finalizado (arquivo PNG, PDF ou link compartilhável)
   - Documento de definição de tema (1 página)

---

## Possíveis Dificuldades

**1. Paralisia por excesso de opções de tema**  
Alguns estudantes podem ter dificuldade em decidir o tema ou querer combinar vários (ex.: "Sci-Fi medieval"). Estratégia: pedir que escolham o que têm mais referências visuais — a escolha estética vem do repertório visual, não da vontade abstrata.

**2. Moodboards sem coerência visual**  
Referências de estilos incompatíveis misturadas (fotorrealismo + cartoon + low poly). Estratégia: perguntar qual das referências melhor representa o resultado que o estudante quer alcançar e usar essa como âncora visual.

**3. Resistência à definição formal do tema**  
Estudantes que preferem "ver o que rola" sem comprometer com um tema. Estratégia: explicar que o tema é o dispositivo pedagógico — sem ele, os exercícios das próximas semanas ficam sem direção. A escolha pode ser ajustada até a Semana 3, mas não depois.

**4. Desconhecimento total do Blender**  
Possível em turmas com acesso irregular às disciplinas anteriores. Estratégia: não avançar o conteúdo de interface nesta semana — o objetivo é apenas reconhecimento espacial, não operação. Os estudantes com dificuldade técnica serão atendidos nas semanas 2 e 3.

**5. Expectativa de "aula técnica" logo na primeira semana**  
Alguns estudantes podem estranhar que a Semana 1 não envolva software. Estratégia: contextualizar que o moodboard é a ferramenta mais importante da disciplina — artistas profissionais passam dias ou semanas nesta etapa antes de abrir qualquer software.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante travado na escolha do tema | Pedir que liste 3 jogos ou filmes favoritos e identificar o ambiente mais recorrente. |
| Moodboard com referências conflitantes | Pedir que retire tudo que não consegue justificar em 10 segundos. |
| Estudante muito rápido na entrega | Desafiar a adicionar referências de texturas de close-up e não apenas ambientes gerais. |
| Turma agitada na crítica informal | Dar 1 minuto por estudante no cronômetro — brevidade estrutura a discussão. |
| Dois estudantes com o mesmo tema | Incentivar — comparar os dois kits ao longo do semestre é pedagogicamente rico. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Moodboard com 10+ referências | C1 — Processo de Projeto | Organização, variedade e coerência visual das imagens |
| Documento de definição de tema | C2 — Direção Artística | Clareza da proposta, coerência entre referências e descrição textual |
| Participação na roda de temas | C10 — Participação nas Critiques | Qualidade da declaração do tema e da pergunta/comentário feito ao colega |
| Pasta de projeto criada e organizada | C1 — Processo de Projeto | Nomenclatura, estrutura de pastas, versão salva |

> **Nota:** Nenhuma nota é atribuída na Semana 1. O professor registra observações qualitativas para calibrar o acompanhamento individual nas próximas semanas.

---

## Entrega da Semana 1

| Entrega | Formato | Prazo |
|---|---|---|
| Moodboard temático (mín. 10 referências organizadas) | PNG, PDF ou link (PureRef, Figma, Slides) | Até o fim do segundo encontro |
| Documento de Definição de Tema (1 página) | PDF ou DOCX | Até o fim do segundo encontro |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 1 | 2026*
