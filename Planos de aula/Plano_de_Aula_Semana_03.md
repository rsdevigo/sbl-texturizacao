# Plano de Aula — Semana 3
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** I — Fundamentos e Mapeamento UV  
**Tema:** Abertura de malha com Seams manuais e Unwrap  
**Apostila:** Parte II, Cap. 5 — UV Unwrapping (Smart UV Project, Seams e Unwrap manual)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** ⭕ FORMAL — autoavaliação obrigatória, rubrica e feedback escrito do professor

---

## Pré-requisito da semana

Os estudantes chegam com:
- Tema do Kit Modular definido e registrado no Documento de Definição de Tema (Semana 1)
- Experiência com os 4 tipos de projeção UV automática (planar, cilíndrica, esférica, cúbica) e checkerboard (Semana 2)
- Familiaridade com o UV Editor no layout dividido com o Viewport (Semana 2)
- Arquivo `.blend` com 3 objetos UV mapeados entregue (Semana 2)

Nenhuma operação de seam ou unwrap manual foi apresentada ainda. Esta é a primeira vez que os estudantes trabalham diretamente em um asset do seu kit modular — não em objetos de prática genéricos.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Identificar as limitações do Smart UV Project e explicar por que ele é insuficiente para assets de produção.
2. Marcar seams em uma malha 3D com base em critérios visuais e estruturais (bordas ocultas, áreas de menor contraste, geometria natural do objeto).
3. Executar o Unwrap manual no Blender e verificar o resultado com checkerboard.
4. Organizar islands no UV Editor: separar, mover, rotacionar e escalar islands manualmente.
5. Identificar problemas no próprio UV layout usando os critérios da Rubrica Mestre (C3) e articular a autoavaliação por escrito antes da crítica formal.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Pasta organizada, arquivo salvo com nomenclatura correta, autoavaliação entregue antes da crítica |
| C2 — Direção Artística | O asset escolhido para esta semana é coerente com o moodboard e representa o tema definido |
| C3 — UV Mapping | **Foco principal:** ausência de sobreposição, distorção mínima, seams em locais não visíveis, islands organizadas |
| C10 — Participação | Qualidade da autoavaliação, apresentação na crítica formal e feedback oferecido ao colega |

> Esta é a **primeira crítica formal** da disciplina. O professor deve comunicar com clareza antes do encontro que a autoavaliação é obrigatória e será comparada com a avaliação do professor durante a crítica.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Arquivo de demonstração preparado pelo professor: um prop temático com geometria moderada — recomenda-se barril, caixote ou bloco de pedra lavrada (formato `.blend`, UV ainda não aberto)
- Textura de checkerboard (embutida no Blender ou PNG externo 1024×1024 com grid de cores)
- Arquivo de Autoavaliação impresso ou compartilhado digitalmente (Instrumento 2 da Rubrica Mestre) — distribuir **antes** do segundo encontro, de preferência no fechamento do primeiro
- Projetor para demonstração e para a crítica formal
- Apostila — Parte II, Cap. 5 — disponibilizada antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Seams: a lógica do corte que o computador não faz por você**

Objetivo: construir o raciocínio por trás do posicionamento de seams antes de qualquer operação técnica.

**Desenvolvimento:**

Abrir com a pergunta da semana passada relembrada: *"Na Semana 2, vocês testaram o Smart UV Project. O que aconteceu com ele num objeto mais complexo do que um cubo?"* Deixar 2–3 respostas antes de prosseguir.

Apresentar a limitação central:

> *"O Smart UV Project corta onde o Blender acha melhor — que é onde o ângulo entre faces é maior. Ele não sabe o que é visível no jogo, não sabe onde fica a frente do objeto, não sabe que a costura de uma bota não aparece no personagem. Seams manuais são o contraponto: você decide onde cortar e por quê."*

**Conteúdo a cobrir:**

**1. O que é um seam**  
Um seam é uma marcação de aresta que instrui o Blender a cortar a malha naquele ponto antes de desdobrar. É o equivalente às dobras de uma caixa de papelão: você escolhe onde abrir para que o objeto "planifique" da forma que você quer. Seams não alteram a geometria — são apenas instruções de corte para o UV.

**2. Critérios para posicionar seams bem**  
- Preferir arestas que ficam ocultas no modelo final: fundos, partes inferiores, interior de encaixes, áreas que ficam contra outras superfícies.
- Seguir a geometria natural do objeto: costuras de barril ficam nas junções das tábuas, não no centro de uma face.
- Em objetos com simetria, um seam no eixo central permite espelhar UV islands e economizar espaço.
- Evitar seams em arestas em destaque, cantos frontais ou superfícies que o jogador sempre verá de perto.

**3. Princípios de um bom layout UV**  
- **Islands:** cada região desdobrada separada por seams forma uma island. O objetivo é ter o menor número de islands necessário sem introduzir distorção.
- **Padding:** espaço em branco entre islands. Evita que texturas "sangrem" de uma island para outra, especialmente em mipmaps. Valor mínimo prático: 4 pixels para texturas de 1024×1024.
- **Aproveitamento de espaço:** ocupar bem o quadrado UV (0–1). Espaço desperdiçado = resolução de textura desperdiçada.

**4. Smart UV Project: quando ainda é útil**  
Para objetos de apoio, fundos ou assets que nunca serão vistos de perto, o Smart UV Project é aceitável. Para assets principais do kit modular — que terão texturização detalhada — seams manuais são obrigatórios.

> **Nota do professor:** Não entre em detalhes sobre padding numérico ou empacotamento automático agora — isso é Semana 4. O foco desta mini aula é o raciocínio de posicionamento de seam, não a otimização de layout. Se um estudante perguntar sobre UVPackmaster ou add-ons de empacotamento, responda: *"Vamos usar isso na Semana 4. Hoje o objetivo é entender a lógica antes de automatizar."*

---

### Demonstração — 20 minutos

**Abertura de malha de um prop com seams manuais no Blender**

**Setup (2 min):**  
Abrir o arquivo de demonstração com o prop (barril, caixote ou pedra). Configurar o layout dividido: Viewport 3D à esquerda, UV Editor à direita. Ativar Material Preview com checkerboard já conectado ao material (ou conectar ao vivo se a turma tiver visto como fazer na Semana 2).

**Parte 1 — Smart UV Project como linha de base (3 min):**  
Entrar em Edit Mode, selecionar tudo (`A`), aplicar Smart UV Project. Mostrar o resultado no UV Editor e no Viewport com checker. Perguntar à turma: *"Onde vocês veem distorção? Onde estão as costuras?"* Identificar 2–3 problemas concretos antes de prosseguir.

**Parte 2 — Marcando seams manualmente (10 min):**  

1. Desfazer o Smart UV Project (`Ctrl+Z`).
2. Mudar para seleção de aresta (`2`).
3. Selecionar arestas estratégicas seguindo os critérios da mini aula: fundo do barril, junção vertical traseira, aro inferior.
4. Para cada grupo de arestas selecionadas: `Edge > Mark Seam` (ou `Ctrl+E` → Mark Seam). Mostrar como as arestas ficam em vermelho.
5. Selecionar tudo (`A`) e executar `U` → **Unwrap**. Observar o novo layout no UV Editor.
6. Comparar com checkerboard: onde a distorção diminuiu em relação ao Smart UV Project?

> Ao vivo, mostrar um seam mal posicionado de propósito (em uma aresta frontal visível) e perguntar: *"Se a textura tivesse uma pintura aqui, o que aconteceria nessa aresta?"* — reforça a lógica visual do critério.

**Parte 3 — Organização das islands (5 min):**  

1. No UV Editor, mostrar como selecionar uma island individualmente (`L` sobre a island).
2. Mover (`G`), rotacionar (`R`) e escalar (`S`) islands — os mesmos atalhos do Viewport 3D.
3. Posicionar as islands dentro do quadrado UV sem sobreposição.
4. Mostrar o Overlay de UV Stretch para verificar distorção residual.

**Fechamento da demo (0 min — integrado):**  
Não há encerramento formal. Transicionar diretamente para o estúdio: *"Agora vocês fazem no asset de vocês. O objetivo não é chegar no perfeito — é chegar no funcional e entender o que cada seam fez."*

> **Nota do professor:** Mantenha o arquivo de demonstração aberto durante o estúdio para que os estudantes possam consultar os atalhos e o processo. Projete-o na tela ou deixe disponível na pasta compartilhada da turma.

---

### Produção em Estúdio — 50 minutos

**Abrir o UV do Asset 01 do Kit Modular com seams manuais**

**Consigna entregue verbalmente:**

> *"Este é o primeiro asset real do kit de vocês. Não é um exercício de prática — é o começo do projeto semestral. O UV que vocês abrirem hoje vai ser a base da texturização nas próximas semanas. Façam com cuidado. Distribuam os seams onde eles fazem sentido para o seu objeto específico — não existe uma resposta única. Existe a justificativa certa."*

**Atividade estruturada:**

1. Abrir o arquivo `.blend` com o Asset 01 do kit (modelagem trazida de disciplinas anteriores ou criada especificamente para o kit — o professor define com antecedência qual asset será a entrega desta semana).
2. Em Edit Mode, identificar as arestas candidatas a seam com base nos critérios apresentados.
3. Marcar seams e executar Unwrap (`U` → Unwrap).
4. Aplicar checkerboard e verificar distorção no Viewport com Material Preview.
5. Organizar as islands no UV Editor: sem sobreposição, todas dentro do quadrado UV (0–1).
6. Ajustar seams adicionais se a distorção for inaceitável e refazer o Unwrap.
7. Salvar com nomenclatura `[Nome]_Asset01_UV_Semana03.blend`.

**Papel do professor:**

Circular pelo estúdio fazendo perguntas diagnósticas que preparem para a crítica formal:

- *"Por que você marcou seam nessa aresta e não na do lado?"*
- *"Onde você acha que essa distorção vai aparecer quando você pintar a textura?"*
- *"Se esse asset fosse visto de frente no jogo, onde o jogador nunca olharia? Coloca o seam lá."*
- *"Você consegue descrever em uma frase o critério que usou para decidir onde cortar?"*

Identificar com antecedência quem vai precisar de mais tempo para concluir o UV antes da crítica e priorizá-los no estúdio do segundo encontro.

> **Nota do professor:** Distribua o formulário de Autoavaliação (Instrumento 2 da Rubrica Mestre) nos **últimos 5 minutos deste encontro**, não no segundo. Isso dá tempo para o estudante refletir antes de chegar na crítica. Instrua: *"Preencham essa autoavaliação em casa ou antes de entrar na aula amanhã. Não é teste — é o ponto de partida da crítica."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva FORMAL — 20 minutos

**Formato: Apresentação individual com autoavaliação e feedback escrito**

Esta é a primeira crítica formal da disciplina. O objetivo é apresentar o trabalho com justificativa, receber feedback estruturado e desenvolver a prática de autoavaliação crítica.

**Preparação (antes do encontro):**  
O professor já coletou ou revisou rapidamente as autoavaliações e identificou 3–4 casos que ilustram situações distintas: UV com seams bem posicionados, UV com distorção evitável, UV com islands desorganizadas e UV com seam em posição visível. Esses casos serão usados como fio condutor da crítica coletiva.

**Roteiro (20 min para 3–4 casos selecionados; turmas maiores ajustam o tempo por caso):**

1. **(2 min de abertura)** Professor apresenta o protocolo: *"Nesta crítica, cada apresentador tem 2 minutos para mostrar o UV e responder a uma pergunta. A turma observa e, ao final de cada apresentação, um colega oferece um feedback específico usando a linguagem da rubrica."*

2. **Para cada caso (3–4 min por caso):**
   - Estudante projeta o UV Editor com checker ativo.
   - Professor faz **uma única pergunta** ao apresentador: *"Por que você escolheu esse seam aqui?"* ou *"Qual foi a decisão mais difícil que você tomou no UV?"*
   - Estudante responde.
   - Um colega (indicado pelo professor) dá um feedback usando a linguagem do C3 da rubrica: *"Eu vejo [observação concreta]. Para chegar no Nível X, eu acho que precisaria de [ação específica]."*
   - Professor complementa em 30 segundos — nunca substitui o feedback do colega, apenas acrescenta.

3. **(3 min de síntese)** Professor aponta os padrões que apareceram na turma:
   - Erro mais comum (ex.: seams em arestas frontais visíveis)
   - Decisão mais acertada observada (ex.: aproveitar a geometria natural para esconder o seam)
   - O que distingue o Nível 2 do Nível 3 no C3 nos trabalhos apresentados

4. **(2 min de conexão com a rubrica)** Professor lê em voz alta a descrição do Nível 3 e do Nível 4 do C3: *"Nível 3 é o mínimo funcional. Nível 4 já exige seams invisíveis. O que falta para o trabalho de vocês chegar lá? Registrem isso na autoavaliação."*

**O professor registra (para C10):**
- Quem apresentou o trabalho com justificativa clara e não apenas descritiva
- Quem ofereceu feedback específico com referência a critério da rubrica
- Quem demonstrou dificuldade de articular a justificativa técnica das decisões

> **Nota do professor:** Ao recolher as autoavaliações (Instrumento 2), compare o nível que o estudante atribuiu a si mesmo com o que você observou. Diferenças significativas (estudante se superestimou ou subestimou muito) são pontos de entrada para a conversa individual no estúdio. Registre observações na Ficha de Crítica Formal (Instrumento 1) para cada estudante apresentado.

---

### Produção em Estúdio — 60 minutos

**Revisão do UV com base na crítica formal e preparação da entrega**

**Consigna:**

> *"Vocês receberam feedback — específico, com critério, com nível de referência. Agora têm 60 minutos para incorporar pelo menos uma melhoria ao UV do Asset 01. Não precisa estar perfeito: precisa estar melhor do que estava e você precisa conseguir me dizer o que mudou e por quê."*

**Atividade:**

1. Rever o UV do Asset 01 à luz do feedback recebido na crítica:
   - Reposicionar seams que estavam em locais visíveis.
   - Corrigir distorção evitável com um seam adicional em área estratégica.
   - Reorganizar islands que estavam fora do quadrado UV ou com sobreposição.
2. Refazer o Unwrap após ajuste de seams e verificar com checkerboard.
3. Organizar as islands finais no UV Editor: sem sobreposição, dentro do espaço UV.
4. Capturar screenshot do UV Editor com checker ativo no Viewport.
5. Salvar arquivo com versão atualizada: `[Nome]_Asset01_UV_Semana03_v2.blend`.
6. Quem concluir com tempo: iniciar a abertura de UV de um segundo asset (a ser entregue formalmente apenas na Semana 4).

**Papel do professor:**

Priorizar atenção individual para:
- Estudantes que na crítica demonstraram confusão sobre o critério de posicionamento de seam (colocam onde "parece certo" sem conseguir justificar).
- Estudantes cujo asset tem geometria mais complexa e que precisarão de mais iterações de unwrap.

Para quem avança rápido:
- *"Ativa o UV Stretch Overlay e me mostra onde ainda tem vermelho. Qual seam você colocaria para reduzir esse estiramento?"*
- *"Seu UV está funcional. O Nível 4 da rubrica diz 'seams invisíveis'. Você consegue auditar cada seam e me dizer: esse seam vai aparecer quando eu texturizar?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min)** Síntese: *"Hoje vocês deram o passo mais importante do UV mapping: pararam de delegar decisões para o algoritmo e começaram a tomar decisões que têm consequência visual. Um seam mal posicionado agora vai aparecer como artefato na textura final. Um seam bem posicionado vai ser invisível. Essa é a diferença entre UV funcional e UV de produção."*

2. **(3 min)** Reflexão individual registrada no formulário de autoavaliação (completar ou revisar a resposta à pergunta de reflexão do Instrumento 2): *"Qual foi a decisão técnica ou artística mais difícil que você tomou nesta semana? O que te fez decidir dessa forma?"* Pedir que 2 estudantes compartilhem voluntariamente.

3. **(3 min)** Antecipação da Semana 4: *"Na semana que vem, vocês vão otimizar o UV que abriram hoje: normalizar texel density, empacotar islands de forma mais eficiente e abrir o UV do Asset 02. A base é o trabalho de hoje — quanto melhor o UV desta semana, menos retrabalho na próxima."*

4. **(2 min)** Confirmação das entregas:
   - Arquivo `.blend` com Asset 01 UV aberto (versão final após a revisão da crítica)
   - Screenshot do UV Editor com checker ativo no Viewport
   - Formulário de Autoavaliação preenchido e entregue ao professor

---

## Possíveis Dificuldades

**1. Confusão entre Unwrap e Smart UV Project**  
Estudantes podem continuar usando Smart UV Project mesmo após a mini aula, por ser o caminho mais curto no menu UV. Estratégia: durante a demonstração, mostrar explicitamente a diferença no menu `U` e criar um hábito verbal: *"Depois que você marcar seams, o comando é sempre Unwrap — não Smart UV."* Reforçar isso no início do estúdio.

**2. Dificuldade em decidir onde posicionar seams**  
É o bloqueio mais comum desta semana. Estudantes com menor vocabulário visual têm dificuldade de identificar "onde o jogador não vai olhar". Estratégia: pedir que o estudante imagine o asset já no jogo e trace o percurso do olhar do jogador — as arestas que ficam fora desse percurso são candidatas a seam. Se isso não funcionar, pedir que identifique a "frente" do objeto e começar com um seam nos fundos.

**3. Seams excessivos resultando em islands demais**  
Estudantes com medo de distorção podem marcar seams em todas as arestas. Resultado: dezenas de islands minúsculas impossíveis de organizar. Estratégia: estabelecer uma heurística prática — *"Tente resolver o UV do objeto com o menor número de seams possível antes de adicionar mais. Um barril simples deve ter entre 3 e 6 islands, não 30."*

**4. Resistência à crítica formal**  
Primeira crítica formal gera ansiedade. Estudantes podem apresentar o trabalho inacabado por receio de exposição, ou apresentar de forma muito descritiva sem justificativa técnica. Estratégia: explicar antes que o objetivo da crítica não é julgar o resultado, mas praticar a justificativa. Um UV com problemas e uma boa explicação das decisões vale mais pedagogicamente do que um UV bom apresentado sem reflexão.

**5. Asset escolhido tem geometria muito complexa para a semana**  
Alguns estudantes podem ter modelado assets detalhados em disciplinas anteriores (personagens, props com muitos detalhes) e tentar aplicar seams em geometria além do que é adequado para esta semana. Estratégia: redirecionar para um asset mais simples do kit (um bloco arquitetônico, um prop básico) e reservar a geometria complexa para as Semanas 3–4 de revisão.

**6. Autoavaliação preenchida sem reflexão ("tudo está no nível 3")**  
É comum na primeira vez. Estudantes preenchem o formulário sem se comprometer com uma avaliação honesta. Estratégia: na comparação durante a crítica, apontar a diferença sem expor o estudante: *"Você se avaliou no nível 3 no C3. Olhando para o seu checker, onde você acha que fica esse nível na rubrica?"* A pergunta convida à revisão sem julgamento.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante trava na escolha do primeiro seam | Pedir que identifique a face "traseira" do objeto e marque todas as arestas que formam o contorno dessa face como seam. Isso cria uma primeira island funcional como ponto de partida. |
| UV com muita distorção após o Unwrap | Perguntar: *"Esse estiramento está em uma face curva ou plana? Face plana com distorção geralmente significa que o seam está impedindo o Blender de abrir bem. Tente adicionar um seam nessa área."* |
| Estudante não consegue articular a justificativa na crítica | Reformular como pergunta mais concreta: *"Me mostra o seam que você ficou mais em dúvida sobre onde colocar. O que te fez escolher esse lugar?"* Tirar o foco de "justificar o todo" para "justificar uma decisão específica". |
| Estudante muito rápido e com UV funcional | Desafiar: *"Quantos seams você tem? Consegue chegar no mesmo resultado (ou melhor) com menos? Cada seam a menos é uma island a menos para organizar na texturização."* |
| Estudante frustrado com resultado do Unwrap | Recontextualizar: *"Se você está vendo a distorção agora, no UV Editor, é porque o checker está funcionando. Você está economizando horas de retrabalho que aconteceriam depois de já ter pintado a textura."* |
| Turma dispersa durante a crítica formal | Atribuir papéis fixos para a crítica: um estudante é o "observador de C3", outro de "C1". Quando o apresentador terminar, o observador respectivo dá o feedback. Estrutura fixa mantém atenção. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Asset 01 com UV aberto e seams manuais | C3 — UV Mapping | Ausência de sobreposição; islands dentro do espaço UV; distorção verificada com checker |
| Posicionamento de seams em locais não visíveis | C3 — UV Mapping | Comparar a posição dos seams com a geometria do asset: estão em arestas que ficariam ocultas no uso real? |
| Arquivo salvo com nomenclatura correta e versionado | C1 — Processo de Projeto | Existência do arquivo com nome correto e versão pós-crítica (_v2) |
| Formulário de Autoavaliação preenchido com reflexão | C1 e C10 | Comparação entre nível declarado pelo estudante e nível observado pelo professor; qualidade da justificativa de evidência |
| Participação na crítica formal (justificativa e feedback) | C10 — Participação | Capacidade de justificar uma decisão técnica com vocabulário da rubrica; qualidade do feedback ao colega (específico, observável, referenciado) |

---

## Entrega da Semana 3

| Entrega | Formato | Prazo |
|---|---|---|
| Asset 01 do Kit Modular com UV aberto via seams manuais e Unwrap | `.blend` (versão pós-crítica, sufixo `_v2`) | Até o fim do segundo encontro |
| Screenshot do UV Editor com checker ativo no Viewport | PNG ou JPG | Até o fim do segundo encontro |
| Formulário de Autoavaliação (Instrumento 2 da Rubrica Mestre) | Impresso ou PDF preenchido | Entregue ao professor no início do segundo encontro |

> **Nota:** Esta é a **primeira semana com registro formal de avaliação**. O professor preenche a Ficha de Crítica Formal (Instrumento 1 da Rubrica Mestre) para cada estudante avaliado na crítica, com atenção especial ao C3. Os critérios C4 a C9 são marcados como "não aplicável". O C1 e o C10 são registrados qualitativamente.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 3 | 2026*
