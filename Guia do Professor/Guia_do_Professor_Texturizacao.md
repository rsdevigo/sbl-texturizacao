# Guia do Professor da Disciplina de Texturização

**Instituto Federal de Mato Grosso do Sul — Campus Dourados**
**Curso Superior de Tecnologia em Jogos Digitais**
**Metodologia: Studio-Based Learning (SBL)**
**Projeto Integrador: Kit Modular de Ambiente (Blender → 3D Coat → Unity)**

---

## Como usar este guia

Este documento é um manual operacional. Ele não substitui o Plano de Ensino, a Rubrica Mestre do Projeto Integrador, o Cronograma Detalhado nem os 17 Planos de Aula já produzidos para a disciplina — ele os articula. Qualquer professor que assuma esta disciplina deve conseguir, lendo este guia em conjunto com os demais documentos, conduzir o semestre mantendo a mesma filosofia pedagógica, a mesma estrutura de estúdio e os mesmos critérios de avaliação, independentemente de quem esteja à frente da sala.

O guia parte do princípio de que a disciplina não é um conjunto de aulas sobre texturização, mas um estúdio de produção no qual o conteúdo técnico emerge das necessidades reais do Projeto Integrador. Um professor que chega a este documento sem experiência prévia em SBL encontrará aqui não apenas o que fazer, mas por que fazer — porque a coerência metodológica depende de compreender a lógica por trás de cada decisão, não apenas de reproduzir um roteiro.

---

## 1. Filosofia da Disciplina

### 1.1 Visão geral

A disciplina de Texturização ocupa 17 semanas letivas, com dois encontros semanais de 1h30, totalizando 51 horas. Ela cobre o ciclo completo de produção de superfícies para jogos digitais: mapeamento UV, materiais PBR, pintura digital, bake de high-poly para low-poly, otimização (atlas, trim sheets, UDIMs, compressão) e integração no motor de jogo via Unity. O pipeline de ferramentas — Blender para modelagem e UV, 3D Coat para texturização e pintura, Unity para integração — reproduz, em escala reduzida, o fluxo de trabalho real de um estúdio de desenvolvimento de jogos.

A disciplina não é organizada por tópicos isolados que se sucedem em aulas expositivas. Ela é organizada em torno de um único Projeto Integrador semestral — o Kit Modular de Ambiente — que atravessa as 17 semanas e absorve cada conteúdo técnico como uma ferramenta a mais para sua construção. Isso significa que, para o professor que assume esta disciplina, a pergunta orientadora de cada semana nunca é "o que eu preciso ensinar hoje?", mas "do que o projeto dos estudantes precisa nesta etapa, e que conteúdo resolve essa necessidade?".

### 1.2 O papel da texturização na formação do aluno de Jogos Digitais

A texturização é, com frequência, a etapa do pipeline de produção em que um modelo 3D deixa de ser uma forma genérica e passa a comunicar história, material, escala e uso. Um estudante de Jogos Digitais que domina modelagem mas não domina texturização entrega ativos "cinzentos": tecnicamente corretos, mas sem vida visual, sem leitura de material e sem lugar plausível dentro de um jogo. A disciplina de Texturização é, portanto, o elo entre a competência técnica de modelagem (adquirida em disciplinas anteriores) e a competência de comunicação visual que o mercado de jogos exige de um artista 3D.

Além disso, a texturização é a etapa do pipeline mais diretamente ligada à performance em tempo real. Decisões de UV, resolução de textura, compressão e empacotamento de canais têm impacto direto no desempenho do jogo — e é nesta disciplina que o estudante aprende, pela primeira vez de forma sistemática, a pensar simultaneamente como artista e como engenheiro de performance. Essa dupla competência — estética e técnica — é o núcleo da formação que a disciplina busca consolidar.

### 1.3 Relação com Arte Conceitual e Pintura Digital

A Texturização não é uma disciplina isolada no currículo. Ela pressupõe e recicla competências desenvolvidas em Arte Conceitual (leitura de referência visual, composição, linguagem de materiais, moodboarding) e em Pintura Digital (manejo de camadas, pincéis, valores tonais, textura pictórica). O professor de Texturização deve tratar essas disciplinas como fornecedoras de matéria-prima para o Projeto Integrador, não como pré-requisitos abstratos já superados.

Na prática, isso significa duas coisas. Primeiro, sempre que possível, os moodboards, estudos de material e exercícios de pintura produzidos em Arte Conceitual e Pintura Digital devem ser reaproveitados como ponto de partida do Kit Modular — o estudante não recomeça do zero, mas estende um repertório visual que já construiu. Segundo, o vocabulário técnico de Texturização (roughness, metallic, desgaste, narrativa de uso) deve ser apresentado como uma tradução, em termos de motor de jogo, de conceitos que o estudante já manipula em linguagem pictórica (luz, sombra, textura de pincel, saturação). A Seção 9 deste guia detalha estratégias concretas de integração.

### 1.4 Justificativa para o uso de Studio-Based Learning

A escolha do SBL como metodologia central não é uma preferência estilística — ela responde a uma característica própria da competência que a disciplina busca desenvolver. Texturização é uma habilidade de julgamento aplicado: não existe uma resposta única correta para "qual roughness essa pedra deveria ter" ou "onde esse seam deveria ficar". A competência se constrói pela prática repetida, pela exposição a feedback estruturado e pela necessidade de justificar decisões — não pela memorização de procedimentos.

Uma aula expositiva tradicional ensina o estudante a executar um comando. O SBL ensina o estudante a decidir quando e por que executar esse comando, e a defender essa decisão diante de pares e do professor. É esse deslocamento — de executor de instruções para tomador de decisões justificadas — que prepara o estudante para o ambiente de trabalho real de um estúdio de jogos, onde diretores de arte e colegas de equipe cobram justificativa, não apenas execução técnica.

O SBL também distribui a responsabilidade pela aprendizagem: o professor deixa de ser a única fonte de correção e passa a ser mediador de um processo em que os próprios estudantes, através das críticas coletivas, desenvolvem a capacidade de avaliar trabalho — a sua e a dos colegas. Essa capacidade de autoavaliação crítica é, em si, um objetivo de aprendizagem da disciplina (Critério 1 e Critério 10 da Rubrica Mestre), não apenas um meio para atingir outros objetivos.

---

## 2. Papel do Professor

O professor de uma disciplina SBL exerce três papéis distintos, que se alternam ao longo de uma mesma sessão de estúdio. Confundir esses papéis — ou permanecer preso a apenas um deles — é o erro mais comum de quem assume a disciplina pela primeira vez.

### 2.1 Mentor

Como mentor, o professor acompanha a trajetória individual de cada estudante, reconhece seu ponto de partida e ajusta a exigência e o tipo de pergunta ao momento de desenvolvimento em que aquele estudante se encontra. O mentor não compara o estudante a um padrão abstrato de "aluno ideal" — compara o estudante à sua própria versão da semana anterior.

**Exemplo prático:** dois estudantes entregam UVs com distorção residual. Para o estudante que já demonstrou domínio de seams em assets anteriores, o mentor pergunta: *"Você sabe qual seam está causando essa distorção. O que te impediu de resolver isso antes da entrega?"* — uma pergunta que cobra autonomia. Para o estudante que está tendo sua primeira experiência com unwrap manual, o mentor pergunta: *"Onde no checker você vê o quadriculado esticado? Vamos olhar juntos essa área."* — uma pergunta que constrói percepção visual antes de cobrar autonomia.

### 2.2 Diretor de Arte

Como diretor de arte, o professor avalia a coerência estética do trabalho em relação ao próprio projeto do estudante e ao padrão de qualidade esperado da indústria — não em relação ao gosto pessoal do professor. O diretor de arte faz perguntas sobre intenção ("o que você quer que o jogador sinta ao ver esse asset?") e sobre coerência ("esse nível de desgaste está de acordo com o resto do seu kit?"), e reserva a opinião pessoal sobre estilo para os momentos em que é explicitamente solicitada.

**Exemplo prático:** um estudante apresenta um material com roughness muito uniforme. Em vez de dizer "eu prefiro mais variação", o professor, no papel de diretor de arte, pergunta: *"Esse material representa uma pedra que ficou anos exposta ao tempo, certo? Onde nessa pedra a água escorreria e deixaria ela mais polida? Onde ficaria mais fosca?"* — a crítica é ancorada na lógica interna do próprio projeto do estudante, não em preferência subjetiva do avaliador.

### 2.3 Supervisor Técnico

Como supervisor técnico, o professor garante que os fundamentos técnicos (UV sem sobreposição, valores PBR fisicamente plausíveis, bake sem artefatos, otimização adequada) sejam cumpridos, porque decisões técnicas incorretas comprometem o funcionamento do asset no motor de jogo independentemente de quão boa seja a intenção artística. O supervisor técnico intervém de forma mais direta e prescritiva do que o mentor ou o diretor de arte, porque alguns erros técnicos (UV sobreposta, metallic mal configurado) não têm "níveis" de certo — são binariamente funcionais ou não funcionais.

**Exemplo prático:** um estudante configura um material metálico com metallic = 0,4. Como supervisor técnico, o professor intervém diretamente: *"Metais na vida real são metallic = 1 ou muito próximos disso. Um valor de 0,4 confunde o motor de renderização sobre se essa superfície é dielétrica ou condutora, e o resultado nunca vai ficar fisicamente crível. Ajuste para 1 e me mostre a diferença no viewport."* Aqui a intervenção é corretiva e imediata, porque o erro é técnico e objetivo, não uma questão de interpretação artística.

### 2.4 Como evitar assumir o papel de solucionador dos problemas dos estudantes

O erro mais comum de professores que migram de metodologias expositivas para o SBL é resolver o problema do estudante em vez de guiá-lo até a solução. Quando o professor senta no computador do estudante e corrige o seam, o UV fica correto — mas o estudante não aprendeu por que estava errado, e vai repetir o mesmo erro no próximo asset.

**Regras práticas para o professor:**

Nunca tocar no mouse ou teclado do computador do estudante, exceto em demonstrações públicas planejadas para toda a turma. Toda correção técnica individual deve ser verbalizada, apontada com o dedo ou o cursor, mas executada pelo próprio estudante.

Substituir afirmações por perguntas sempre que a resposta puder ser descoberta pelo estudante com uma pista razoável. Em vez de "esse seam está errado, mova para a aresta de baixo", perguntar "o que aconteceria com a textura se essa aresta virasse um seam em vez dessa?".

Tolerar o silêncio depois da pergunta. É comum que o professor, desconfortável com a pausa, responda a própria pergunta antes que o estudante processe. Contar mentalmente até cinco antes de complementar.

Reservar a correção direta e não-socrática apenas para: (1) erros técnicos objetivos que impedem qualquer progresso posterior (ex.: UV completamente ausente, arquivo corrompido); (2) situações em que o tempo de estúdio está se esgotando e a demonstração direta é pedagogicamente mais eficiente do que insistir na descoberta guiada; (3) risco de o estudante consolidar um hábito tecnicamente incorreto que será mais custoso desfazer depois do que corrigir agora.

**Exemplo do erro a evitar:** estudante chama o professor porque o normal map "não está funcionando" na Unity. O professor abre o Inspector, marca a flag "Normal Map" na textura, e diz "pronto, agora funciona". O estudante aprendeu que "quando o normal map não funciona, eu chamo o professor" — não aprendeu por que a flag existe. A abordagem correta: *"Vamos olhar o tipo de textura que a Unity está lendo. Clica na textura no Project e olha o campo 'Texture Type' no Inspector. O que está selecionado? O que você acha que precisa estar selecionado para um mapa de normais?"*

---

## 3. Papel dos Estudantes

O SBL exige do estudante uma postura ativa que é, em si, um objetivo de aprendizagem. O professor deve comunicar essas expectativas explicitamente nas primeiras semanas, porque estudantes vindos de metodologias mais passivas frequentemente não sabem o que se espera deles em um estúdio.

### 3.1 Responsabilidade pelo próprio aprendizado

O estudante é responsável por chegar às sessões de estúdio com o trabalho da semana anterior em mãos, por buscar referências visuais de forma autônoma, por experimentar soluções antes de pedir ajuda, e por registrar suas próprias dúvidas para trazê-las de forma específica ao professor. A disciplina não pune a tentativa malsucedida — ela pune a ausência de tentativa. Um estudante que erra um bake mas consegue descrever o que tentou e por que não funcionou está mais avançado, do ponto de vista do Critério 1 da Rubrica Mestre, do que um estudante que espera passivamente pela instrução do professor.

### 3.2 Participação nas críticas

O estudante participa das críticas coletivas em dois papéis: como apresentador do próprio trabalho e como avaliador do trabalho dos colegas. Ambos os papéis são avaliados (Critério 10). Espera-se que, como apresentador, o estudante justifique decisões técnicas e artísticas com vocabulário da rubrica, não apenas descreva o que fez. Espera-se que, como avaliador, o estudante ofereça feedback específico e observável, evitando comentários vagos como "ficou bom" ou "acho que precisa melhorar".

### 3.3 Registro de decisões

O estudante mantém um registro mínimo de processo: pasta de referências organizada, arquivos versionados com nomenclatura consistente, e anotações sobre decisões tomadas e feedback recebido. Este registro não é burocracia — é a evidência que sustenta o Critério 1 da rubrica e é o material que o próprio estudante usa para preparar sua autoavaliação antes de cada crítica formal. O Instrumento 4 da Rubrica Mestre (Checklist Semanal) é a ferramenta recomendada para isso.

### 3.4 Iteração contínua

Nenhuma entrega na disciplina é definitiva até a Semana 17. O estudante deve entender que uma nota baixa em uma crítica formal intermediária não é uma punição terminal, mas um ponto de dados para a próxima iteração — daí a estrutura de pesos crescentes do Portfolio de Artefatos (CF1 = 10%, até CF5 = 30%), que recompensa explicitamente a trajetória de melhoria. Cabe ao professor reforçar, em linguagem simples e recorrente, que "essa nota de hoje não é sobre você — é sobre o asset de hoje, e o asset de amanhã pode ser diferente".

---

## 4. Como Conduzir uma Sessão de Estúdio

A sessão de estúdio (os 50 minutos do primeiro encontro e os 60 minutos do segundo) é o núcleo da disciplina. É nela que a aprendizagem efetivamente acontece — a mini aula e a demonstração são preparação; a crítica é reflexão; o estúdio é onde o estudante produz e o professor observa, medeia e intervém.

### 4.1 O que observar durante a produção

O professor circula continuamente pelo estúdio — nunca senta atrás de uma mesa esperando ser chamado. Durante essa circulação, observa quatro dimensões simultaneamente:

**Progresso técnico:** o estudante está avançando na tarefa da semana, ou está parado no mesmo ponto há muito tempo? Um estudante travado por 15 minutos na mesma operação, sem sinais de progresso, provavelmente está bloqueado (ver 4.2) e precisa de intervenção.

**Qualidade das decisões:** mesmo quando o estudante avança tecnicamente, o professor observa se as decisões tomadas ao longo do caminho são coerentes com os critérios da rubrica ativos naquela semana. Um estudante pode terminar um UV rapidamente e ainda assim ter tomado decisões de seam ruins que só aparecerão como problema depois.

**Estado emocional e engajamento:** frustração, tédio ou ansiedade visíveis são sinais de que a tarefa está descalibrada para aquele estudante (fácil demais, difícil demais, ou pouco clara). Um estudante silenciosamente frustrado raramente pede ajuda por iniciativa própria — cabe ao professor perceber e se aproximar.

**Padrões coletivos:** se três ou mais estudantes cometem o mesmo erro de forma independente, o problema provavelmente não é individual — é uma lacuna na mini aula ou demonstração daquele dia. Isso deve ser registrado e considerado uma pausa coletiva de dois minutos para reesclarecer o ponto, em vez de repetir a mesma explicação individualmente para cada estudante.

### 4.2 Como identificar bloqueios

Um bloqueio se manifesta de formas específicas e reconhecíveis: o estudante realiza a mesma operação repetidamente sem alterar o resultado (por exemplo, desfazer e refazer um unwrap várias vezes sem mudar a estratégia de seam); o estudante navega em menus sem objetivo aparente, procurando uma ferramenta que não sabe nomear; o estudante para de trabalhar e começa a mexer no celular ou conversar sobre assuntos não relacionados ao projeto — frequentemente um sinal de desistência temporária diante de um obstáculo não verbalizado; o estudante pergunta a mesma dúvida a colegas diferentes sem incorporar as respostas.

Diante de qualquer um desses sinais, a abordagem recomendada é a pergunta diagnóstica aberta, não a pergunta fechada: *"Me conta o que você está tentando fazer agora"* revela mais do que *"Você está com dúvida?"* (que geralmente recebe um "não" defensivo mesmo quando há bloqueio).

### 4.3 Quando intervir

A intervenção deve ser calibrada pelo custo do bloqueio, não pela duração da luta do estudante. Alguns bloqueios são produtivos — o estudante está processando um conceito genuinamente difícil e vai chegar à solução com mais alguns minutos de tentativa. Outros bloqueios são estéreis — o estudante está preso por falta de uma informação factual que nenhuma quantidade de tentativa vai revelar (por exemplo, não saber que existe um atalho de teclado específico, ou desconhecer que uma flag precisa ser ativada).

Regra prática: se o bloqueio é conceitual (o estudante está decidindo entre abordagens, testando hipóteses, comparando resultados), dar mais tempo e intervir apenas com perguntas. Se o bloqueio é factual (falta uma informação que a exploração sozinha não vai revelar em tempo razoável), intervir mais cedo com uma dica direta e pontual, preservando o restante da tarefa para a autonomia do estudante.

### 4.4 Quando permitir experimentação

A experimentação deve ser ativamente protegida, mesmo quando o professor já sabe, de antemão, que a abordagem do estudante provavelmente não vai funcionar — desde que o custo do erro seja baixo e o tempo de estúdio comporte a tentativa. Um estudante que tenta empacotar UV islands de uma forma pouco eficiente, mas plausível, deve ter espaço para descobrir sozinho que a abordagem não funcionou bem, porque essa descoberta consolida o aprendizado de forma mais duradoura do que a advertência prévia do professor.

A exceção é quando o erro é caro de desfazer (por exemplo, um bake mal configurado que vai consumir 20 minutos de processamento) ou quando o tempo de estúdio remanescente não comporta a tentativa e a correção subsequente. Nesses casos, a intervenção preventiva é justificada — mas deve vir acompanhada da explicação do motivo, não apenas do impedimento.

### 4.5 Como promover colaboração entre estudantes

O SBL se beneficia de estudantes que aprendem uns com os outros, não apenas com o professor — isso reduz a dependência do professor como única fonte de correção e constrói a cultura de crítica entre pares que sustenta os Critérios 1 e 10 da rubrica. Estratégias práticas: quando um estudante resolve um problema técnico que outros também enfrentam, pedir explicitamente que ele mostre a solução para os colegas ("Marina, você acabou de resolver isso — vai lá mostrar pro Lucas como você fez"); organizar a disposição física do estúdio (quando possível) de forma que estudantes trabalhando em problemas semelhantes fiquem próximos; ao final do estúdio, perguntar publicamente "alguém encontrou uma solução interessante hoje que vale a pena compartilhar com a turma?"; evitar responder perguntas que já foram respondidas para outro estudante na mesma sessão — em vez disso, direcionar: "essa mesma dúvida a Beatriz teve há uns 10 minutos, vai perguntar pra ela como resolveu".

---

## 5. Como Conduzir uma Critique

### 5.1 Objetivos pedagógicos da crítica

A crítica coletiva, seja informal ou formal, persegue quatro objetivos simultâneos: desenvolver a capacidade de autoavaliação do estudante que apresenta; desenvolver a capacidade de comunicação visual e verbal (o estudante precisa justificar decisões, não apenas mostrá-las); desenvolver a capacidade de dar e receber feedback de forma construtiva; e consolidar, coletivamente, o vocabulário técnico e os critérios de qualidade da disciplina, usando o trabalho real da turma como material de estudo.

A crítica não é uma correção de tarefa. O professor que conduz a crítica como se estivesse apenas "dando a nota em voz alta" perde a maior parte do valor pedagógico do formato. A crítica é bem-sucedida quando, ao final, tanto quem apresentou quanto quem assistiu saíram com uma compreensão mais precisa dos critérios de qualidade — não apenas quando o apresentador recebeu uma avaliação.

### 5.2 Estrutura recomendada

Toda crítica, informal ou formal, segue a mesma lógica de três movimentos, ajustando apenas a duração e o grau de formalidade: (1) apresentação com justificativa — o estudante mostra o trabalho e responde a uma pergunta orientadora sobre uma decisão específica, não descreve tudo o que fez; (2) feedback estruturado — colegas e/ou professor respondem com observações específicas ancoradas em critérios observáveis, seguindo a lógica "eu vejo [observação concreta]; para avançar, seria necessário [ação específica]"; (3) síntese e conexão com a rubrica — o professor nomeia o padrão que emergiu (o que a maioria fez bem, o que a maioria ainda precisa desenvolver) e conecta explicitamente à linguagem da Rubrica Mestre.

### 5.3 Perguntas abertas para estimular reflexão

Uma crítica de qualidade é sustentada por perguntas, não por afirmações. Banco de perguntas reutilizáveis, organizadas por finalidade:

Para abrir a apresentação: *"Qual foi a decisão mais difícil que você tomou nesta etapa?"*; *"Se você tivesse que escolher uma coisa desse trabalho para eu olhar com atenção, qual seria?"*; *"O que você ainda não está satisfeito nesse resultado?"*

Para investigar justificativa técnica: *"Por que você escolheu esse valor de roughness aqui?"*; *"O que te fez posicionar o seam nesse lugar e não em outro?"*; *"Que problema esse trim sheet resolve que texturas individuais não resolveriam?"*

Para investigar justificativa artística: *"O que essa textura está tentando comunicar sobre a história desse objeto?"*; *"Como esse asset conversa com os outros do seu kit?"*; *"Se um jogador visse isso por dois segundos, o que ele entenderia sobre esse material?"*

Para provocar autoavaliação: *"Olhando pra rubrica, em que nível você diria que está esse critério agora? Por quê?"*; *"O que separaria esse trabalho do nível seguinte da rubrica?"*; *"Se você tivesse mais uma semana só para isso, o que você faria primeiro?"*

Para orientar o feedback dos colegas: *"O que você vê no trabalho da/do colega que se destaca?"*; *"Que critério da rubrica você usaria para descrever o que você está observando?"*; *"Que sugestão específica e acionável você daria?"*

### 5.4 Como evitar críticas destrutivas

Três regras protegem a crítica de se tornar destrutiva sem perder o rigor técnico: toda observação negativa deve vir acompanhada de uma direção de melhoria concreta — "isso está ruim" nunca é uma crítica completa; a crítica avalia o trabalho, nunca a pessoa — "essa textura ficou repetitiva" é diferente de "você não presta atenção em detalhes"; a crítica deve equilibrar reconhecimento do que funciona com indicação do que precisa evoluir, mesmo quando o trabalho está claramente aquém do esperado — sempre existe algo, por menor que seja, que pode ser nomeado como acerto real (não um elogio genérico e vazio).

O professor deve modelar essas regras ativamente nas primeiras críticas da disciplina, porque os estudantes vão replicar o padrão de comunicação que observam do professor quando derem feedback aos colegas.

### 5.5 Como estimular argumentação técnica

A disciplina espera que o estudante progrida de "descrever o que fez" para "justificar por que fez". Isso não acontece automaticamente — precisa ser cobrado de forma consistente desde a primeira crítica. Técnicas: nunca aceitar uma resposta puramente descritiva sem uma pergunta de acompanhamento ("e por que você fez dessa forma?"); recusar respostas vagas como "porque ficou melhor assim" pedindo especificidade ("melhor em que sentido? o que mudou visualmente?"); quando o estudante não consegue justificar, não fornecer a justificativa no lugar dele — perguntar "o que você acha que eu diria se perguntasse por quê?" força o estudante a antecipar o raciocínio, mesmo sem ter articulado antes.

### 5.6 Roteiros completos de crítica

#### Roteiro A — Crítica Informal (semanas sem CF)

**Duração:** 20 minutos, no início do segundo encontro da semana.
**Formato:** circulante ou coletiva rápida, sem preenchimento de ficha formal.

| Tempo | Etapa | Condução |
|---|---|---|
| 0–2 min | Abertura | Professor relembra o objetivo da semana e comunica o formato: "hoje vamos olhar rapidamente 3 ou 4 trabalhos, sem ficha formal, só pra alinhar onde a turma está." |
| 2–15 min | Apresentações rápidas | 3 a 4 estudantes (escolhidos por amostragem, rotativos semana a semana) mostram o trabalho por 1–2 minutos cada, respondendo a uma única pergunta do professor. Um colega complementa com uma observação. |
| 15–18 min | Síntese de padrões | Professor nomeia o erro mais comum e o acerto mais notável observados nos casos mostrados, sem individualizar quem errou. |
| 18–20 min | Direcionamento | Professor conecta a síntese ao que a turma vai fazer no restante do estúdio: "então, quem ainda não resolveu [x], é nisso que vocês vão focar agora." |

Este roteiro pode também ocorrer de forma inteiramente circulante — o professor caminha entre as estações e faz uma crítica breve e individual a cada estudante, sem reunir a turma. A escolha entre formato coletivo e circulante depende do tempo disponível e de quão homogêneo é o estágio de progresso da turma naquela semana.

#### Roteiro B — Crítica Formal Intermediária (CF1–CF5)

**Duração:** 20 minutos, no início do segundo encontro das semanas 3, 5, 8, 11 e 14.
**Pré-requisito:** autoavaliação (Instrumento 2 da Rubrica Mestre) entregue antes do encontro; professor já revisou os trabalhos e selecionou 3–4 casos representativos.

| Tempo | Etapa | Condução |
|---|---|---|
| 0–2 min | Abertura e protocolo | Professor comunica o protocolo do dia: quantos casos serão vistos, tempo por caso, papel da turma. |
| 2–14 min | Apresentação dos casos selecionados | Para cada caso (3–4 min): estudante apresenta com justificativa de uma decisão específica → colega designado oferece feedback usando linguagem da rubrica → professor complementa em até 30 segundos. |
| 14–17 min | Síntese de padrões | Professor nomeia o erro mais comum, a decisão mais acertada observada, e o que distingue os níveis da rubrica nos trabalhos vistos. |
| 17–19 min | Leitura da rubrica em voz alta | Professor lê o descritor do nível atual predominante e do nível seguinte para o(s) critério(s) foco da semana, tornando concreta a distância entre eles. |
| 19–20 min | Fechamento e registro | Professor anuncia que vai recolher/comparar autoavaliações com sua própria avaliação (Ficha de Crítica Formal — Instrumento 1) e devolver feedback escrito. |

Estudantes não selecionados para apresentação nesta CF específica ainda entregam a autoavaliação e recebem a Ficha de Crítica Formal preenchida pelo professor com base na avaliação direta do trabalho entregue (não é necessário que todos apresentem oralmente em toda CF — a amostragem rotativa garante que, ao longo do semestre, todos apresentem repetidamente).

#### Roteiro C — Crítica Final (CF6, Semana 17)

**Duração:** parte central da Semana 17, com defesa oral individual de no mínimo 10–15 minutos por estudante (ajustar conforme tamanho da turma e tempo disponível — pode ocupar os dois encontros da semana).
**Formato:** apresentação e defesa formal do Kit Modular de Ambiente completo, com banca (ver Seção 10).

| Etapa | Duração sugerida | Condução |
|---|---|---|
| Apresentação do kit | 5–7 min | Estudante apresenta o Kit Modular completo: tema, moodboard original, os 5–10 assets finalizados, e a montagem em cena na Unity. |
| Defesa técnica e artística | 5–6 min | Professor(es) da banca fazem perguntas dirigidas sobre decisões específicas, usando os 10 critérios da Rubrica Mestre como roteiro (ex.: "me mostra o texel density mais crítico do seu kit"; "qual asset você mais retrabalhou e por quê?"). |
| Feedback da banca | 2–3 min | Banca oferece uma síntese verbal: ponto mais forte do projeto e uma prioridade de melhoria, caso o estudante continue desenvolvendo o kit além da disciplina. |
| Registro | — | Preenchimento da Ficha de Crítica Formal (Instrumento 1) com todos os 10 critérios ativos, conforme os pesos da Avaliação Final descritos na Rubrica Mestre. |

A Crítica Final se diferencia das intermediárias por avaliar o projeto como um todo integrado (não mais uma etapa isolada) e por incluir explicitamente a integração na Unity (C8), que só se torna avaliável nesta etapa.

---

## 6. Estratégias de Feedback

O feedback eficaz na disciplina se distribui em quatro registros, que frequentemente precisam ser combinados na mesma intervenção. Confundir os registros — dar feedback técnico quando o estudante precisa de feedback motivacional, por exemplo — é uma causa comum de frustração em ambos os lados.

### 6.1 Feedback técnico

Refere-se à correção ou plausibilidade de parâmetros, valores e processos (UV, PBR, bake, otimização, Unity). É objetivo, ancorado em critérios verificáveis, e deve vir acompanhado de uma explicação do princípio subjacente, não apenas da correção pontual.

**Adequado:** *"Seu metallic está em 0.3 para essa superfície de ferro. Na vida real, metais são condutores elétricos e refletem luz de forma quase total nas frequências específicas da sua cor — por isso, no workflow metallic/roughness, metais ficam próximos de 1. Um valor intermediário como 0.3 faz o motor de renderização misturar comportamento dielétrico e condutor, e o resultado nunca fica plausível em nenhuma condição de luz. Ajusta para 0.9–1 e compara o resultado no viewport."*

**Inadequado:** *"Seu metallic está errado."* (não diz o quê, por quê, nem como corrigir.)

### 6.2 Feedback artístico

Refere-se à leitura visual, composição, narrativa de material e coerência estética. É mais subjetivo do que o feedback técnico, mas deve ser ancorado em referências concretas ou em critérios observáveis da rubrica, nunca apenas em gosto pessoal do professor.

**Adequado:** *"Comparando com a referência de metal enferrujado que você trouxe no moodboard, a ferrugem no seu asset está distribuída de forma muito uniforme. Na referência, ela se concentra nas frestas e nas áreas onde a água escorre e fica parada. Isso é o que dá credibilidade ao desgaste — não é a quantidade de ferrugem, é a lógica de onde ela aparece."*

**Inadequado:** *"Eu não gostei muito dessa textura, acho que ficou meio sem graça."* (não referencia critério nem oferece direção.)

### 6.3 Feedback conceitual

Refere-se à coerência entre o asset e a proposta geral do projeto (tema do kit, narrativa do ambiente, função do objeto dentro do espaço de jogo). Esse tipo de feedback frequentemente exige que o professor faça perguntas antes de opinar, porque a intenção conceitual pertence ao estudante.

**Adequado:** *"Seu kit é pós-apocalíptico e esse barril está impecavelmente limpo — parece que acabou de sair da fábrica. Isso é intencional? Existe alguma razão narrativa pra esse objeto específico estar conservado num ambiente onde tudo o mais está deteriorado? Se não houver, talvez esse seja um ponto de ruptura com a coerência do kit."*

**Inadequado:** *"Isso não parece pós-apocalíptico."* (aponta o sintoma sem investigar a intenção nem abrir espaço para justificativa.)

### 6.4 Feedback motivacional

Refere-se ao estado emocional e ao engajamento do estudante com o processo, não ao produto em si. É especialmente necessário em momentos de frustração, bloqueio prolongado ou quando o estudante recebe uma sequência de feedbacks técnicos e artísticos negativos e precisa de reconhecimento de esforço e progresso para manter engajamento.

**Adequado:** *"Compara o UV que você fez hoje com o da Semana 2. Naquele, você tinha ilhas sobrepostas e nem sabia usar o checker. Hoje você identificou sozinho onde estava a distorção antes mesmo de eu falar qualquer coisa. Isso é progresso real, mesmo que esse UV específico ainda não esteja perfeito."*

**Inadequado:** *"Não desanima, tá ótimo!"* (vago, não ancorado em evidência, soa como consolo genérico e perde credibilidade.)

**Regra geral de combinação:** ao dar feedback técnico ou artístico corretivo, especialmente em momentos de maior fragilidade emocional percebida (início do semestre, primeira crítica formal, período de maior carga de outras disciplinas), o professor deve intercalar reconhecimento específico de progresso — não para suavizar a crítica de forma artificial, mas porque o reconhecimento preciso de progresso é, em si, informação útil que ajuda o estudante a calibrar o próprio julgamento.

---

## 7. Estudantes com Diferentes Ritmos

Uma turma nunca progride de forma homogênea. O professor deve ter estratégias prontas para os quatro perfis mais recorrentes, evitando tanto a negligência de quem avança rápido quanto o abandono de quem está com dificuldade.

### 7.1 Estudantes avançados

Estudantes que terminam a tarefa da semana com folga de tempo não devem ser deixados ociosos nem avançados mecanicamente para a tarefa da semana seguinte sem critério. Estratégias: aprofundar o mesmo critério da semana com um desafio de refinamento (ex.: "seu UV está funcional — agora tenta chegar em ocupação de espaço acima de 85% sem perder a organização das ilhas"); atribuir o papel de mentor de pares temporário, pedindo que ajude um colega travado no mesmo tipo de problema (benefício mútuo: reforça o próprio domínio do estudante avançado ao explicar, e libera tempo do professor); oferecer uma extensão opcional relacionada a um tópico futuro do cronograma, sinalizando claramente que é opcional e não altera a rubrica da semana atual; aumentar a exigência de justificativa ("você resolveu isso rápido — me explica três razões técnicas pelas quais você fez dessa forma e não de outra").

### 7.2 Estudantes com dificuldades técnicas

Dificuldade técnica (não conseguir operar a ferramenta, esquecer atalhos, errar sequências de passos) exige quebra da tarefa em passos menores e verificáveis, e repetição deliberada. Estratégias: reduzir o escopo da entrega da semana para esse estudante especificamente, comunicando isso de forma discreta e sem estigmatizar ("essa semana, foca só em terminar o unwrap com seams corretos — a organização de ilhas a gente resolve juntos na próxima"); criar ou indicar um guia de referência rápida (atalhos, sequência de passos) que o estudante possa consultar de forma autônoma sem precisar chamar o professor a cada passo; priorizar esse estudante na circulação do estúdio, verificando o progresso a cada 10–15 minutos em vez de esperar ser chamado; identificar se a dificuldade é de retenção (esquece o que já foi mostrado) ou de compreensão (nunca entendeu o princípio) — a estratégia de intervenção é diferente em cada caso: retenção pede repetição e registro escrito pelo próprio estudante; compreensão pede reformulação da explicação com outra analogia.

### 7.3 Estudantes com dificuldades artísticas

Dificuldade artística (composição fraca, paleta inconsistente, falta de repertório visual) costuma ter raiz em pobreza de referência, não em falta de habilidade manual. Estratégias: antes de qualquer correção técnica de pincel ou camada, verificar o moodboard do estudante — frequentemente o problema é que a referência é insuficiente ou genérica, e nenhuma técnica de pintura compensa isso; propor exercícios de comparação direta lado a lado (referência real ao lado do trabalho do estudante) para desenvolver a percepção de diferença antes de pedir correção; conectar explicitamente com o repertório que o estudante já construiu em Arte Conceitual e Pintura Digital — perguntar "como você resolveria isso se fosse uma pintura?" costuma destravar mais do que instrução técnica nova; para estudantes com dificuldade persistente de composição, sugerir um limite deliberado de paleta (3–4 cores dominantes) como andaime temporário — restringir opções costuma facilitar decisões para quem ainda não desenvolveu critério próprio.

### 7.4 Estudantes que não participam das críticas

A não participação pode ter causas distintas — timidez, insegurança sobre o próprio trabalho, desengajamento geral com a disciplina, ou dificuldade de expressão verbal — e a estratégia deve variar conforme a causa aparente. Estratégias gerais: atribuir papéis estruturados e específicos na crítica (ex.: "hoje você é o observador do critério C3 — sua tarefa é anotar uma observação sobre UV em cada apresentação") reduz a ansiedade de falar "sobre qualquer coisa" e dá um roteiro concreto; para estudantes tímidos, iniciar com perguntas de resposta mais curta e factual antes de pedir opiniões elaboradas, construindo confiança gradual; conversar individualmente, fora da crítica pública, para entender a causa da não participação antes de insistir publicamente; nunca forçar apresentação pública de um estudante visivelmente inseguro sem preparação prévia — isso tende a reforçar a esquiva em vez de superá-la; registrar a não participação como dado relevante para o Critério 10, mas comunicar isso ao estudante de forma direta e com antecedência, nunca como surpresa na nota final.

---

## 8. Problemas Comuns da Disciplina

Para cada área do pipeline, seguem os problemas mais frequentes observados em turmas de Texturização, com sintomas, causas prováveis e estratégias de orientação socrática (evitando a correção direta sempre que pedagogicamente viável).

### 8.1 UV Mapping

| Problema | Sintomas | Causas Prováveis | Estratégia de Orientação |
|---|---|---|---|
| Distorção visível no checker | Quadriculado esticado ou comprimido de forma irregular em superfícies planas ou curvas | Seams insuficientes; unwrap aplicado sobre geometria com poucos cortes estratégicos; uso de Smart UV Project em asset de produção | "Essa distorção está numa superfície plana ou curva? Se é plana e ainda distorce, o que isso te diz sobre onde falta um seam?" |
| Ilhas sobrepostas | Duas ou mais regiões do modelo compartilham o mesmo espaço UV, causando textura duplicada/incorreta | Falha ao separar seams entre partes distintas do objeto; movimentação acidental de ilha no UV Editor | "Seleciona cada ilha com L e olha se alguma delas está por cima da outra. O que você precisa fazer pra elas não se sobreporem?" |
| Texel density inconsistente | Alguns assets do kit parecem "borrados" e outros "nítidos demais" quando texturizados com a mesma resolução | Ilhas de tamanhos desproporcionais ao tamanho real do objeto; ausência de normalização de escala UV entre assets | "Se você aplicar o mesmo checker nos dois assets, os quadrados ficam do mesmo tamanho? O que isso te diz sobre a escala relativa das UVs?" |
| Aproveitamento de espaço baixo | Grande área vazia no quadrado UV 0–1, resolução de textura desperdiçada | Ilhas não rotacionadas nem escaladas para preencher o espaço; ausência de empacotamento (packing) | "Quanto do quadrado UV está realmente ocupado por ilha? O que aconteceria se você rotacionasse essa ilha 45 graus?" |
| Seams visíveis no resultado final | Linha ou descontinuidade visível na textura aplicada, mesmo com UV tecnicamente correto | Seams posicionados em arestas frontais ou muito visíveis; padding insuficiente entre ilhas | "Imagina esse asset no jogo, visto de frente. O jogador vai olhar direto pra essa aresta onde está o seam?" |

### 8.2 Materiais PBR

| Problema | Sintomas | Causas Prováveis | Estratégia de Orientação |
|---|---|---|---|
| Metallic mal calibrado | Metais parecem plásticos foscos; superfícies não-metálicas parecem metalizadas | Uso de valores intermediários de metallic (0.3–0.7) para materiais que deveriam ser puramente dielétricos ou condutores | "Esse material conduz eletricidade na vida real? O que isso te diz sobre onde o metallic dele deveria estar — perto de 0 ou perto de 1?" |
| Roughness uniforme | Material parece "plástico" ou artificial, sem variação de brilho em nenhuma área | Ausência de mapa de roughness com variação; uso de valor único constante sem lógica de uso do objeto | "Onde nesse objeto a mão de alguém tocaria com frequência? O que costuma acontecer com o brilho de uma superfície de tanto ser tocada?" |
| Albedo com iluminação "assada" | Sombras e realces de luz pintados diretamente no mapa de cor base, gerando iluminação duplicada e incorreta no motor | Uso de referências fotográficas sem correção de iluminação; hábito trazido de pintura tradicional (chiaroscuro) sem adaptação ao workflow PBR | "Esse mapa de cor base tem uma sombra pintada aqui embaixo. O motor de jogo também vai calcular uma sombra nessa área quando a luz da cena bater. O que acontece quando as duas se somam?" |
| Normal map com aparência "invertida" ou incorreta | Relevo aparece afundado onde deveria ser saliente, ou vice-versa; iluminação do detalhe parece errada | Convenção de espaço de normal (tangent/object, OpenGL/DirectX) incompatível entre ferramenta de geração e motor de destino | "Repara se o canal verde do seu normal map está invertido entre o 3D Coat e a Unity. Qual convenção cada ferramenta espera?" |
| Falta de plausibilidade física geral | Material "não convence" mesmo com valores tecnicamente corretos | Ausência de referência real consultada durante a criação; falta de teste sob diferentes condições de luz | "Você comparou esse material com uma foto real desse tipo de superfície sob luz direta e sob luz difusa? O que muda?" |

### 8.3 Bake

| Problema | Sintomas | Causas Prováveis | Estratégia de Orientação |
|---|---|---|---|
| Artefatos ("manchas") no normal map | Manchas escuras ou claras inesperadas em superfícies que deveriam ser lisas | Cage muito próxima ou muito distante da high-poly; sobreposição de projeção entre partes próximas do modelo | "A cage está capturando só a parte da high-poly que pertence a essa região, ou está pegando geometria de outra parte também?" |
| Seams visíveis após bake | Linha nítida no resultado do bake mesmo com UV tecnicamente correto | Padding insuficiente na textura; ausência de "exploded bake" em partes muito próximas | "Se você afastar as partes do modelo antes de assar (exploded bake), será que essas manchas desaparecem?" |
| AO com "bleeding" entre ilhas | Sombreamento de oclusão vazando de uma ilha UV para outra vizinha no espaço da textura | Padding insuficiente entre ilhas UV; resolução de bake baixa em relação ao tamanho das ilhas | "Olhando o layout UV, essas duas ilhas estão próximas demais no espaço da textura? O que o padding resolveria aqui?" |
| Detalhe da high-poly não aparece no bake | Normal map resultante fica "liso", sem capturar esculturas ou detalhes finos da high-poly | Nomenclatura ou agrupamento incorreto entre objetos high-poly e low-poly; high-poly não posicionada corretamente sobre a low-poly | "O nome do grupo de bake da sua high-poly bate com o da low-poly correspondente? O software sabe qual high-poly pertence a qual low-poly?" |
| Bake consome tempo excessivo ou trava | Processo de bake demora muito além do esperado ou o software não responde | Resolução de bake desnecessariamente alta para o teste; excesso de geometria não otimizada na high-poly de teste | "Pra esse teste, você precisa mesmo de 4K? Que tal testar em 512 primeiro pra confirmar que o setup está correto antes de assar em resolução final?" |

### 8.4 Pintura (Texturização Artística)

| Problema | Sintomas | Causas Prováveis | Estratégia de Orientação |
|---|---|---|---|
| Textura repetitiva/genérica | Superfície parece um padrão copiado, sem variação orgânica | Uso de textura procedural ou stencil sem camadas adicionais de variação manual | "Se você olhar essa superfície de perto, ela parece feita por um carimbo. O que você poderia adicionar em cima pra quebrar essa repetição?" |
| Desgaste sem narrativa | Sujeira e desgaste aplicados uniformemente, sem lógica de uso do objeto | Ausência de reflexão sobre como o objeto seria usado no mundo do jogo; aplicação de máscara procedural sem ajuste manual | "Pensa na vida desse objeto: quem usa, como usa, há quanto tempo existe. Onde nele o desgaste faria mais sentido?" |
| Perda de leitura à distância | Detalhes finos ficam ilegíveis quando o asset é visto de longe (distância típica de uso no jogo) | Excesso de detalhamento em close-up sem verificação em escala reduzida; contraste de valor insuficiente entre camadas | "Reduz o zoom até a distância que o jogador realmente vai ver esse objeto. O detalhe que você fez ainda se lê?" |
| Inconsistência entre assets do mesmo kit | Um asset parece "mais pintado" ou "mais estilizado" que os outros do mesmo kit | Ausência de referência cruzada entre assets durante a produção; moodboard não consultado de forma consistente | "Coloca esse asset lado a lado com os outros dois que você já terminou. Eles parecem pertencer ao mesmo lugar?" |
| Uso de stencil sem integração | Detalhes de stencil parecem "colados" sobre a superfície, sem se misturar ao restante da textura | Camada de stencil aplicada sem ajuste de opacidade, blend mode ou desgaste sobreposto | "Esse detalhe do stencil está exatamente na mesma cor e nitidez do restante? O que aconteceria se você passasse uma camada de sujeira por cima dele também?" |

### 8.5 Otimização

| Problema | Sintomas | Causas Prováveis | Estratégia de Orientação |
|---|---|---|---|
| Resolução de textura desproporcional ao asset | Objeto pequeno ou de fundo usa textura de resolução igual à de um asset em destaque | Ausência de critério de resolução baseado em importância visual e proximidade de câmera | "Esse objeto vai ficar a que distância da câmera no jogo? Ele precisa da mesma resolução que o asset principal do seu kit?" |
| Múltiplas texturas únicas para elementos repetitivos | Molduras, painéis e bordas semelhantes usam texturas distintas em vez de uma trim sheet compartilhada | Falta de identificação de padrões repetitivos antes de iniciar a texturização de cada peça | "Esses três elementos têm a mesma lógica de borda e material. O que aconteceria se eles compartilhassem uma única trim sheet?" |
| Channel packing ausente ou incorreto | Mapas de roughness, AO e metallic salvos como três arquivos RGB separados, ocupando memória desnecessária | Desconhecimento da técnica de empacotamento de canais (ex.: ORM); exportação sem configuração de canais únicos | "Cada um desses mapas usa só um canal de cor, certo? O que aconteceria se você colocasse os três dentro dos canais R, G e B de uma única imagem?" |
| Ausência de justificativa quantificada | Estudante não sabe dizer quanta memória cada decisão de otimização economizou | Falta de hábito de registrar e comparar tamanhos de arquivo antes/depois das otimizações | "Qual era o tamanho total das texturas desse asset antes do atlas, e qual é agora? Você consegue calcular a economia?" |
| UDIMs/multi-tile mal organizados | Tiles numerados incorretamente ou aplicados a assets que não justificam a complexidade de múltiplos tiles | Uso de UDIM em assets pequenos que se beneficiariam mais de um atlas simples; confusão na numeração de tiles | "Esse asset realmente precisa de mais resolução do que um único tile de 4K oferece? Um atlas simples resolveria com menos complexidade?" |

### 8.6 Unity

| Problema | Sintomas | Causas Prováveis | Estratégia de Orientação |
|---|---|---|---|
| Normal map "achatado" ou com aparência incorreta | Relevo do normal map não aparece ou aparece invertido dentro da Unity | Textura importada sem a flag "Texture Type: Normal Map" ativada no Inspector | "Clica na textura no Project e olha o campo Texture Type no Inspector. O que está selecionado ali, e o que precisaria estar?" |
| Cor base "lavada" ou muito clara/escura | Albedo aparece com valores incorretos de exposição comparado ao 3D Coat | Espaço de cor incorreto (linear vs. sRGB) na importação da textura; configuração de color space não corresponde ao tipo de mapa | "Esse mapa é uma textura de cor (albedo) ou uma textura de dado (roughness, normal)? Isso muda o color space que a Unity deveria usar pra ler ele." |
| Material não aparece como no 3D Coat | Diferença visual significativa entre o preview no software de texturização e o resultado na Unity | Slots de textura conectados incorretamente no shader; pipeline de renderização (Built-in/URP/HDRP) diferente do esperado; ausência de iluminação equivalente na cena de teste | "Compara slot por slot: o que está conectado no Albedo, no Metallic, no Normal? Bate com o que você exportou do 3D Coat?" |
| Escala incorreta do asset importado | Objeto aparece gigante ou minúsculo em relação à cena | Unidades de escala divergentes entre Blender e Unity na exportação/importação (metros vs. outras unidades) | "Qual era o tamanho real desse objeto no Blender? Que tamanho ele tem agora na cena da Unity? O que isso te diz sobre a escala de exportação?" |
| Iluminação/lightmap não bakeia corretamente | Sombras ausentes, manchas pretas ou artefatos após o bake de lightmap na Unity | Ausência de segundo canal de UV (lightmap UV) no asset importado; sobreposição de UVs no canal de lightmap | "Esse asset tem um segundo mapa de UV dedicado ao lightmap, separado do UV de textura? Eles podem ter sobreposição, ao contrário do UV principal — mas você conferiu isso?" |

---

## 9. Integração com Outras Disciplinas

### 9.1 Reaproveitamento de Arte Conceitual

Os estudantes chegam à disciplina de Texturização com moodboards, estudos de material e definições de linguagem visual já produzidos em Arte Conceitual. O professor de Texturização deve tratar esse material como ponto de partida obrigatório do Kit Modular, não como referência opcional. Estratégias concretas: na Semana 1, ao invés de pedir um moodboard inteiramente novo, orientar os estudantes a revisitarem e curarem o material de Arte Conceitual já produzido, selecionando o que é diretamente aplicável ao tema do kit; quando o feedback artístico em critique referenciar decisões de cor ou composição, perguntar explicitamente "isso está de acordo com o que você definiu na Arte Conceitual?", reforçando a continuidade entre disciplinas em vez de tratá-las como compartimentos isolados; sempre que possível, dialogar com o professor de Arte Conceitual sobre quais temas e vocabulário visual a turma já domina, para calibrar a profundidade das explicações conceituais em Texturização (ex.: se a turma já trabalhou linguagem de materiais em Arte Conceitual, a mini aula de PBR pode partir desse vocabulário em vez de reconstruí-lo do zero).

### 9.2 Reaproveitamento de Pintura Digital

As competências técnicas de Pintura Digital (manejo de camadas, blend modes, pincéis customizados, controle de valor tonal) são diretamente transferíveis para a Unidade III da disciplina (pintura digital e bake, Semanas 9–12). O professor deve nomear explicitamente essa transferência para o estudante, em vez de assumir que ele fará a ponte sozinho. Estratégias: ao introduzir a pintura de desgaste e sujeira no 3D Coat, comparar diretamente com técnicas equivalentes já praticadas em Pintura Digital (ex.: "isso é exatamente a mesma lógica de camada de sombra que vocês usaram em Pintura Digital, só que agora aplicada sobre um modelo 3D em vez de uma superfície plana"); para estudantes com dificuldade artística (Seção 7.3), a Pintura Digital costuma ser a disciplina onde já demonstraram mais domínio — usar esse repertório como ponto de apoio explícito ("como você resolveria essa sombra numa pintura 2D? Agora aplica esse mesmo raciocínio aqui"); considerar, quando pedagogicamente viável, que exercícios de textura seamless (Semana 6) sejam produzidos em Krita, reforçando a ferramenta e o fluxo já familiares de Pintura Digital antes de migrar para o ambiente 3D do 3D Coat.

---

## 10. Encerramento da Disciplina

### 10.1 Bancas finais

A Crítica Formal 6 (Semana 17) funciona como banca de defesa do Projeto Integrador. Recomenda-se, sempre que a estrutura do curso permitir, a composição de banca com mais de um avaliador — o professor titular da disciplina e, idealmente, um segundo professor da área (por exemplo, de Arte Conceitual, Modelagem 3D ou Desenvolvimento de Jogos), o que traz uma perspectiva externa à rotina do estúdio e reforça, para o estudante, que a competência desenvolvida é avaliável por qualquer profissional da área, não apenas pelo professor que o acompanhou. A banca segue o Roteiro C descrito na Seção 5.6, com tempo individual de defesa de no mínimo 10–15 minutos por estudante.

### 10.2 Exposição dos trabalhos

Recomenda-se organizar, ao final do semestre, uma exposição (física, em telão, ou digital via galeria online) dos Kits Modulares completos de toda a turma. Esse momento cumpre função pedagógica além da avaliação: reforça a cultura de crítica coletiva ao expor o trabalho de cada estudante ao olhar de toda a turma e, quando possível, de outras turmas e professores do curso; valida socialmente o esforço do semestre, funcionando como fechamento simbólico do processo; e serve de referência viva para a próxima turma que cursar a disciplina — o professor pode, com autorização dos estudantes, manter um arquivo de kits exemplares para usar como referência nas demonstrações de anos seguintes.

### 10.3 Portfólio dos estudantes

Cada estudante deve encerrar a disciplina com material de portfólio profissional, não apenas com a nota final. O Critério 9 da Rubrica Mestre (Apresentação) já orienta essa exigência ao longo do semestre — o encerramento formaliza isso como entrega explícita. Orientar os estudantes a produzirem: breakdown visual de pelo menos 2–3 assets do kit (wireframe, UV, mapas individuais isolados, comparativo antes/depois); renders de apresentação do kit completo, com iluminação cuidada, em pelo menos duas condições de luz distintas; um documento curto (uma página) descrevendo o processo, as decisões técnicas e artísticas centrais, e o que o estudante mudaria se continuasse o projeto; recomendação explícita, quando pertinente, de publicação em plataformas profissionais como ArtStation, já referenciada na bibliografia da disciplina como padrão de portfólio da indústria.

### 10.4 Autoavaliação final

Além da autoavaliação de cada crítica formal (Instrumento 2 da Rubrica Mestre), a Semana 17 pede uma autoavaliação de caráter distinto: retrospectiva sobre o semestre inteiro, não apenas sobre a última entrega. Perguntas recomendadas para essa autoavaliação final: "Compare seu primeiro asset (Semana 3) com o kit final. O que mudou na sua forma de tomar decisões técnicas e artísticas, não apenas no resultado visual?"; "Qual foi o feedback mais difícil de receber ao longo do semestre, e o que você fez com ele?"; "Se você tivesse que ensinar UV mapping, PBR ou bake para um colega de outra turma, o que você diria que é mais importante entender — não fazer, entender?"; "O que no seu processo de trabalho você pretende manter e o que pretende mudar em projetos futuros?". Essa autoavaliação final deve ser lida pelo professor antes da defesa (CF6) sempre que o cronograma permitir, para que a banca possa referenciar diretamente a trajetória do estudante durante a própria defesa — reforçando, no último momento formal da disciplina, o mesmo princípio que orientou o semestre inteiro: a avaliação da texturização não é sobre um resultado isolado, mas sobre um processo de julgamento que o estudante desenvolveu e agora consegue articular por conta própria.

---

## Referências

Este guia deriva diretamente dos seguintes documentos-fonte do projeto, que permanecem a referência primária e devem ser consultados em conjunto com este manual:

- Plano de Ensino da Disciplina de Texturização (IFMS Campus Dourados, 2026)
- Rubrica Mestre do Projeto Integrador de Texturização, versão 2.0
- Cronograma Detalhado — Disciplina de Texturização (17 semanas)
- Planos de Aula — Semanas 1 a 17
- Apostila de Texturização — DEVIGO, Rodrigo. IFMS Campus Dourados, 2026. Disponível em: <https://rsdevigo.github.io/apostila_texturizacao>
- Projeto Pedagógico do Curso Superior de Tecnologia em Jogos Digitais — IFMS Campus Dourados, 2025

*Guia do Professor — Texturização — Jogos Digitais | Versão 1.0 | 2026*
