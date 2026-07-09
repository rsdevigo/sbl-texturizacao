# Plano de Aula — Semana 13
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização e Integração ao Motor
**Tema:** Texture Atlas: unificação de assets em uma única textura
**Apostila:** Cap. 9 — Texture Atlas: conceito e criação; Otimização de draw calls
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 **Informal** — circulante, sem nota formal nesta semana

---

## Pré-requisito da semana

Os estudantes chegam com:

- Pacote completo de bake (Normal, AO, Curvature, ID Map) dominado e aplicado em pelo menos um asset do kit — Semana 12
- Dois assets consolidados (Asset 01 e Asset 02) com UV finalizado, material PBR completo, desgaste pintado e bake integrado — Semanas 1 a 12
- Feedback da CF4 (Semana 11) incorporado, com prioridade de melhoria já trabalhada
- Kit modular com identidade visual e paleta já estabelecidas (moodboard atualizado desde a Semana 1)

> **Nota de transição:** Até aqui, cada asset do kit recebeu sua própria textura dedicada — um UV, um conjunto de mapas, um material. Essa abordagem foi correta para aprender UV mapping, PBR, pintura e bake em profundidade, mas não é como um kit modular é entregue em produção real. Esta semana inicia a **Unidade IV**, que desloca o foco de "como texturizar bem um objeto" para "como texturizar um kit inteiro de forma eficiente para o motor de jogo". O primeiro problema desse novo bloco é o **Texture Atlas**: em vez de cada asset carregar sua própria textura (o que gera múltiplos draw calls quando vários objetos aparecem juntos em cena), vários assets passam a compartilhar uma única textura, reorganizando seus UVs dentro do mesmo espaço 0–1. Isso não é um recurso novo de pintura ou bake — é uma decisão de **arquitetura de produção**, e exige revisitar o UV mapping aprendido nas Semanas 2 a 4 sob uma lente nova: eficiência para tempo real, não apenas ausência de distorção.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é um Texture Atlas e por que ele reduz draw calls, relacionando o conceito à performance de um kit modular em tempo real (Unity).
2. Avaliar quais assets do próprio kit são bons candidatos a compartilhar textura, com base em critério técnico (tamanho relativo, complexidade de material, frequência de uso em cena) e não apenas em conveniência.
3. Reorganizar UV islands de múltiplos objetos dentro de um único espaço UV 0–1, aplicando os princípios de padding, texel density e aproveitamento de espaço já dominados nas Semanas 2 a 4.
4. Executar o processo de re-bake e re-texturização necessário quando os UVs de um asset já finalizado são remapeados para caber no atlas combinado.
5. Verificar a integridade do atlas resultante: ausência de sobreposição indevida entre ilhas de objetos diferentes, texel density comparável entre os assets combinados, bleeding contido pelo padding.
6. Justificar, em crítica circulante, a escolha dos três (ou mais) assets combinados no atlas e o trade-off entre economia de textura e perda de resolução individual.

---

## Critérios observados nesta semana

> 🔵 **Crítica Informal.** Não há nota formal nesta semana. C7 (Otimização) é observado pela **primeira vez** na disciplina — é a semana em que esse critério começa a ser construído como evidência, embora só entre em nota formal na CF5 (Semana 14). C3 (UV Mapping) retorna em observação, revisitado sob a ótica de otimização.

| Critério | Status | O que observar |
|---|---|---|
| C1 — Processo de Projeto | obs. | Justificativa registrada da escolha dos assets combinados no atlas; comparação antes/depois documentada |
| C3 — UV Mapping | obs. — revisitado | O remapeamento de UV para o atlas mantém os princípios de texel density e padding já dominados, ou os sacrifica em nome da economia? |
| C7 — Otimização | obs. — **primeira aparição** | Critério de escolha dos assets combinados; ocupação eficiente do espaço do atlas; ausência de sobreposição indevida |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado na crítica circulante, especialmente sobre a lógica de agrupamento escolhida pelos colegas |

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Computadores com 3D Coat instalado (versão 2023 ou superior)
- Arquivos `.blend` de todos os assets do kit de cada estudante (mínimo 3, já com UV, material e bake das semanas anteriores)
- Arquivo de demonstração do professor: 3 assets simples do kit de referência do professor (ex.: barril, caixote, tocha), cada um ainda com UV individual, prontos para serem combinados ao vivo
- Projetor para demonstração
- Apostila Cap. 9 — trecho de Texture Atlas, disponibilizado antes da aula

> **Preparação do conjunto de demonstração:** É necessário que os três objetos de referência já existam com UV individual e textura aplicada antes da aula — modelá-los ou texturizá-los do zero consumiria o tempo da demonstração. O importante é que sejam objetos de tamanho e complexidade visivelmente diferentes entre si (um grande, um médio, um pequeno), para que a decisão de proporção de espaço no atlas fique clara para a turma.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**De um UV por objeto para um UV por grupo: o que é e por que existe o Texture Atlas**

Objetivo: fazer o estudante entender o Texture Atlas não como uma técnica isolada, mas como resposta a um problema de performance que só aparece quando o kit é visto como um todo, não asset por asset.

**Abertura:**

Exibir no projetor uma cena simples com 5 objetos do mesmo kit modular, cada um com sua própria textura — 5 materiais distintos carregados simultaneamente. Ao lado, a mesma cena com os 5 objetos compartilhando uma única textura combinada — 1 material carregado. Perguntar: *"Visualmente, as duas cenas parecem idênticas. Mas para o motor de jogo, elas custam coisas muito diferentes. O que vocês acham que mudou por trás da cena, mesmo sem mudança visível?"*

Deixar 2–3 respostas. Direcionar para a ideia central: cada material/textura distinta que a GPU precisa carregar para renderizar um frame gera um **draw call** adicional. Um kit modular de ambiente pode ter dezenas de instâncias do mesmo conjunto de assets em cena (paredes, barris, caixas repetidos) — se cada peça carrega textura própria, o custo de renderização cresce rapidamente. O Texture Atlas resolve isso agrupando várias texturas em uma só, para que múltiplos objetos usem o mesmo material.

---

**Conteúdo a cobrir:**

**1. O que é um draw call e por que ele importa**

Um draw call é uma instrução da CPU para a GPU desenhar um conjunto de geometria com um material específico. Trocar de material entre objetos custa tempo de processamento. Em uma cena com muitos objetos pequenos e repetidos — exatamente o perfil de um kit modular de ambiente — reduzir o número de materiais distintos é uma das otimizações mais diretas disponíveis ao artista de texturas, antes mesmo de qualquer otimização de código.

*"Vocês não vão escrever nenhuma linha de código hoje. A otimização de hoje acontece inteiramente na forma como vocês organizam o UV e a textura — é trabalho de artista, não de programador, e ainda assim tem impacto direto em performance."*

**2. Texture Atlas: definição e o que muda em relação ao UV individual**

Um Texture Atlas é uma única textura (ex.: 2048×2048) que contém, dentro do mesmo espaço de imagem, os mapas de vários objetos diferentes — cada um ocupando uma região exclusiva. Isso exige que o UV de cada objeto combinado seja remapeado: em vez de ocupar sozinho o espaço 0–1 inteiro, cada objeto passa a ocupar apenas uma fração desse espaço, dividindo-o com os demais.

*"Pensem no atlas como uma folha de contato de fotos: em vez de uma foto por página, várias fotos organizadas numa única folha — cada uma ainda reconhecível e separada, mas compartilhando o mesmo papel."*

**3. Planejamento do atlas: quais assets combinar**

Nem todo conjunto de assets é um bom candidato para atlas conjunto. Critérios de decisão:

- **Assets que aparecem juntos com frequência em cena** (ex.: elementos de uma mesma parede modular) se beneficiam mais do que assets isolados e raramente vistos ao mesmo tempo.
- **Assets de complexidade de material semelhante** combinam melhor — misturar um objeto com material simples (cor sólida) e outro com detalhe fino de pintura pode desperdiçar espaço do atlas se não for bem proporcionado.
- **Tamanho relativo em cena** deve informar a proporção de espaço no atlas: um objeto grande (parede) precisa de mais área de textura do que um pequeno (moeda), mesmo dentro do mesmo atlas.

*"A pergunta não é 'quais três assets eu escolho por serem mais fáceis de combinar', é 'quais três assets do meu kit realmente aparecem juntos, na mesma cena, com frequência suficiente para justificar compartilhar textura'."*

**4. Reorganização de UV islands: revisitando a Semana 4 com um objetivo novo**

Os princípios já dominados — padding entre ilhas, texel density consistente, aproveitamento de espaço — continuam valendo integralmente, mas agora aplicados entre **objetos diferentes**, não apenas entre ilhas do mesmo objeto. A texel density precisa ser mantida coerente entre os assets combinados: se um objeto pequeno ocupa proporcionalmente mais espaço no atlas do que sua importância visual justifica, ele está "roubando" resolução dos demais.

> **Nota do professor:** Este é o ponto onde mais erros conceituais aparecem. Reforçar que texel density consistente entre objetos diferentes no mesmo atlas é tão importante quanto era entre ilhas do mesmo objeto na Semana 4 — a diferença é que agora o "objeto" de referência é o kit inteiro, não uma peça isolada.

---

### Demonstração — 20 minutos

**Criação de um Texture Atlas combinando 3 assets em um único UV 2048×2048**

**Setup (1 min):**
Abrir o Blender com os três objetos de demonstração já carregados, cada um com seu material e UV individual visíveis lado a lado no viewport.

**Percurso da demonstração:**

**Passo 1 — Avaliação e decisão de proporção (4 min):**
1. Mostrar os três objetos e discutir em voz alta o critério de escolha: *"Estes três aparecem juntos na minha cena de referência — fazem parte do mesmo conjunto de mobiliário do kit."*
2. Estimar visualmente a proporção de espaço que cada um deveria ocupar no atlas combinado, com base no tamanho relativo em cena (não no tamanho do UV individual anterior).

**Passo 2 — Criação do UV combinado (8 min):**
1. Selecionar os três objetos e entrar em modo de edição conjunta (`Edit Mode` com múltiplos objetos selecionados, ou unir temporariamente para fins de UV).
2. Abrir o UV Editor e mostrar as três ilhas de UV originais sobrepostas no mesmo espaço 0–1 (problema a ser resolvido).
3. Reposicionar e redimensionar cada conjunto de ilhas proporcionalmente ao tamanho relativo definido no Passo 1, usando `Pack Islands` com a opção de manter proporção relativa entre grupos, quando disponível na versão do Blender em uso.
4. Aplicar padding entre os grupos de ilhas de objetos diferentes — reforçar que esse padding precisa ser generoso o suficiente para evitar bleeding entre os *objetos*, não só entre ilhas do mesmo objeto.

**Passo 3 — Criação da textura combinada 2048×2048 (5 min):**
1. Criar uma nova imagem 2048×2048 no Blender ou levar o UV remapeado ao 3D Coat para repintura.
2. Demonstrar rapidamente como uma textura já existente de um dos objetos pode ser reposicionada e redimensionada dentro da nova textura combinada, respeitando a nova área do UV.
3. Mostrar o resultado: os três objetos, agora com uma única textura carregada, exibindo suas aparências originais preservadas.

**Passo 4 — Validação (2 min):**
1. Aplicar checkerboard temporariamente sobre o atlas combinado para verificar distorção introduzida pelo redimensionamento.
2. Verificar visualmente se a texel density entre os três objetos permanece comparável — nenhum deles deve parecer "borrado" em relação aos outros.

> **Nota do professor:** Se o tempo apertar, é aceitável não repintar a textura combinada ao vivo — mostrar o UV remapeado e uma textura combinada já preparada de antemão é suficiente para transmitir o processo. O ponto central da demonstração é a reorganização do UV, não a repintura em si.

---

### Produção em Estúdio — 50 minutos

**Planejamento e início da execução do Texture Atlas do próprio kit**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com dois objetivos: primeiro, escolher três assets do seu kit que fazem sentido compartilhar uma única textura — usem o critério da mini aula, não conveniência. Segundo, começar a reorganizar os UVs desses três assets dentro de um único espaço 2048×2048. Vocês não precisam terminar a repintura hoje — o objetivo do primeiro encontro é ter os UVs remapeados e organizados corretamente."*

**Atividade estruturada:**

**Etapa 1 — Seleção e justificativa dos assets (≈10 min):**
1. Revisar os assets do kit já produzidos e escolher três que aparecem juntos com frequência na composição do ambiente.
2. Escrever uma justificativa breve (2–3 frases) de por que esses três foram escolhidos — esse registro alimenta C1 (Processo) e C7 (Otimização).

**Etapa 2 — Reorganização do UV combinado (≈25 min):**
1. Selecionar os três objetos no Blender e abrir o UV Editor em modo conjunto.
2. Definir a proporção de espaço de cada objeto no atlas com base no tamanho relativo em cena.
3. Reposicionar e redimensionar as ilhas de UV de cada objeto dentro do espaço 0–1 combinado, aplicando padding entre grupos.
4. Verificar sobreposição: nenhuma ilha de um objeto pode se sobrepor à ilha de outro.

**Etapa 3 — Início da textura combinada (≈10 min):**
1. Criar a imagem de destino 2048×2048.
2. Se o tempo permitir, iniciar o reposicionamento das texturas já existentes dentro do novo espaço do atlas (no Blender ou já preparando a exportação para o 3D Coat).

**Etapa 4 — Registro de processo (≈5 min):**
1. Salvar o arquivo: `[Nome]_Atlas_S13.blend`.
2. Screenshot do UV combinado com checkerboard aplicado, para levar à crítica circulante do segundo encontro.

**Papel do professor:**

Circular verificando:

- **A justificativa de agrupamento é técnica ou apenas por conveniência?** Perguntar diretamente: "Esses três objetos aparecem juntos na sua cena, ou você só escolheu os que já estavam prontos?"
- **A proporção de espaço no atlas reflete o tamanho relativo real dos objetos em cena?** Erro comum: dividir o espaço igualmente entre os três objetos, independentemente do tamanho — isso desperdiça resolução no objeto pequeno e sacrifica o grande.
- **Há sobreposição de ilhas entre objetos diferentes?** Esse é o erro mais grave possível nesta etapa — verificar com atenção redobrada, pois sobreposição entre objetos diferentes (ao contrário de ilhas do mesmo objeto) é mais fácil de passar despercebida.

Perguntas de mediação circulante:
- *"Se você tivesse que explicar para alguém de fora da disciplina por que esses três objetos específicos compartilham textura, o que você diria?"*
- *"Olhando a proporção de espaço que você deu a cada objeto no atlas, ela corresponde a quanto espaço eles realmente ocupam quando você olha sua cena de referência?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva — 20 minutos

**Formato: circulante, sem nota formal**

**Abertura (2 min):**
*"Hoje é crítica circulante — vou passar de estação em estação. Tenham o UV combinado aberto com checkerboard e a justificativa escrita de por que vocês escolheram esses três assets. Quero ouvir a lógica de agrupamento antes de olhar o resultado técnico."*

**Dinâmica (16 min):**
Circulação livre pelas estações. Em cada uma, o professor pede primeiro a justificativa verbal, depois observa o UV combinado:
- *"Por que esses três e não outros três do seu kit?"*
- *"A proporção de espaço que cada objeto recebeu no atlas faz sentido com o tamanho dele na cena?"*
- *"Onde está o padding entre os objetos? Se eu aumentar o zoom nessa fronteira, vou ver bleeding?"*

Encorajar comparação entre colegas — *"Vejam o critério de agrupamento do seu vizinho: vocês concordam com a lógica dele, ou agrupariam diferente?"* — sem formalizar como avaliação por pares registrada.

**Síntese (2 min):**
*"A maior parte de vocês já tem o UV combinado organizado. O trabalho de hoje no estúdio é fechar a textura do atlas — trazer as texturas individuais para dentro do espaço combinado e garantir que a qualidade visual não caiu em nenhum dos três objetos."*

---

### Produção em Estúdio — 60 minutos

**Finalização da textura combinada e validação do Texture Atlas**

**Consigna:**

> *"Sessenta minutos para transformar o UV combinado de vocês em um atlas de fato funcional: a textura final 2048×2048 com os três objetos representados, prontos para serem exportados e aplicados de volta aos assets do kit."*

**Atividade estruturada:**

**Bloco 1 — Transferência das texturas para o atlas combinado (≈25 min):**
1. Para cada um dos três objetos: reposicionar ou repintar a textura existente (Albedo, e demais canais PBR relevantes) dentro da nova área do UV combinado.
2. Se o fluxo do estudante usar o 3D Coat: reimportar o mesh com o novo UV combinado e reconstruir as camadas de detalhe já pintadas (desgaste, stencil, bake) na nova posição do UV — este é o ponto de maior atenção, pois o remapeamento de UV invalida a posição original das camadas pintadas.
3. Verificar que cada objeto mantém sua identidade visual original mesmo dentro do espaço compartilhado.

**Bloco 2 — Re-bake, se necessário (≈15 min):**
1. Para objetos cujo Normal Map ou AO da Semana 11/12 dependiam da posição original do UV: executar novo bake com o UV remapeado.
2. Verificar ausência de artefatos após o re-bake, seguindo o mesmo protocolo de checagem da Semana 11 (rotacionar o viewport, checar superfícies planas).

**Bloco 3 — Validação final do atlas (≈15 min):**
1. Aplicar os três objetos na cena de teste com a textura combinada carregada uma única vez.
2. Confirmar visualmente: um material, três objetos, aparência preservada.
3. Verificar texel density comparativa entre os três objetos — nenhum deve parecer nitidamente mais nítido ou mais borrado que os outros.

**Bloco 4 — Registro final (≈5 min):**
1. Exportar a textura do atlas (`.png`, 2048×2048).
2. Salvar arquivo Blender/3D Coat com sufixo `_Atlas_S13_Final`.
3. Render comparativo: os três objetos com textura individual (antes) vs. com atlas combinado (depois).

**Papel do professor:**

- Priorizar apoio aos estudantes que perderam camadas de detalhe pintado ao remapear o UV — esse é o problema técnico mais provável e mais custoso em tempo desta semana.
- Para estudantes que terminam rápido: sugerir avaliar se um quarto asset do kit poderia entrar no mesmo atlas sem comprometer a qualidade dos outros três.
- Perguntas de mediação: *"Quantas texturas seu kit inteiro usava antes de hoje, e quantas usa agora depois desses três assets combinados? Essa conta já é uma evidência concreta de otimização que você pode apresentar na CF5."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese técnica)**
*"Hoje vocês deram o primeiro passo da Unidade IV: transformar texturas individuais em uma estratégia de kit. O Texture Atlas resolve bem casos de objetos de tamanho parecido e uso conjunto. Semana que vem vocês vão conhecer uma ferramenta complementar para um problema diferente: elementos arquitetônicos repetitivos, como paredes e molduras — aí entra a Trim Sheet."*

2. **(3 min — Reflexão sobre trade-offs)**
Pergunta aberta: *"Vocês sentiram que algum dos três objetos perdeu qualidade visual por causa da divisão de espaço no atlas? Se sim, o que vocês fariam diferente da próxima vez — talvez combinar objetos diferentes, ou usar um atlas maior?"*
Deixar 2–3 respostas. O objetivo é consolidar que otimização sempre envolve trade-off, e que reconhecer esse trade-off é parte da competência técnica — não existe atlas "perfeito", existe atlas bem justificado para o caso de uso.

3. **(2 min — Antecipação da Semana 14)**
*"Semana que vem é Crítica Formal — CF5, a quinta do semestre. O tema é Trim Sheets: faixas de textura reutilizáveis para elementos modulares repetitivos. É a primeira vez que Otimização (C7) entra em nota. Antes de chegar: pensem em qual elemento do seu kit se repete várias vezes com pequenas variações — esse é o candidato ideal para trim sheet."*

4. **(2 min — Confirmação das entregas)**
Recapitular nomenclatura de entrega e prazo. Lembrar que a justificativa escrita de agrupamento do atlas será parte da evidência de C7 na CF5.

---

## Possíveis Dificuldades

**1. Escolha de assets por conveniência, não por critério de uso conjunto**
Alguns estudantes tendem a escolher os três assets "mais prontos" ou "mais fáceis de mexer", em vez de avaliar se realmente aparecem juntos na cena. Estratégia: exigir a justificativa escrita antes de começar a reorganização do UV — o ato de verbalizar por escrito frequentemente expõe a fragilidade do critério e leva à reconsideração antes de investir tempo no remapeamento.

**2. Divisão de espaço igual entre objetos de tamanhos diferentes**
Erro comum: dividir o atlas em três áreas iguais, independentemente do tamanho relativo dos objetos em cena, resultando em resolução desproporcional (o objeto grande fica com pouca definição, o pequeno com definição desnecessária). Estratégia: pedir para o estudante comparar visualmente os três objetos lado a lado na escala real da cena antes de decidir a proporção do UV — a decisão de espaço deve vir da cena, não da conveniência de organização no editor.

**3. Perda de camadas de detalhe pintado ao remapear o UV**
Quando um asset já tinha desgaste, stencil ou bake associados ao UV original (Semanas 9 a 12), o remapeamento para o atlas invalida a posição espacial dessas camadas, exigindo reconstrução. Estratégia: alertar sobre isso antes de começar a reorganização — sugerir manter o arquivo original intacto (salvar como novo arquivo, não sobrescrever) e tratar a reconstrução do detalhe pintado como parte esperada do processo, não como erro.

**4. Sobreposição de ilhas entre objetos diferentes**
Diferente da sobreposição entre ilhas do mesmo objeto (erro já familiar desde a Semana 3), a sobreposição entre objetos diferentes no atlas é mais difícil de perceber visualmente no UV Editor, especialmente com muitas ilhas na tela. Estratégia: usar a ferramenta de detecção de sobreposição do Blender (`UV → Select Overlap` ou equivalente) para verificação sistemática, em vez de depender apenas da inspeção visual.

**5. Padding insuficiente entre grupos de objetos diferentes**
Mesmo com padding adequado entre ilhas do mesmo objeto, pode faltar espaço de segurança entre o "bloco" de um objeto e o "bloco" de outro, causando bleeding visível na fronteira quando a textura é comprimida ou tem mipmap gerado. Estratégia: tratar cada grupo de objeto como uma unidade e aplicar padding extra nas bordas externas do grupo, não apenas internamente entre suas próprias ilhas.

**6. Tempo insuficiente para repintar a textura combinada completa**
Reorganizar UV é mais rápido que reconstruir texturas pintadas à mão nas novas posições — alguns estudantes podem terminar o primeiro encontro com o UV pronto mas gastar todo o segundo encontro só na repintura de um dos três objetos. Estratégia: priorizar a reconstrução de camadas nos objetos com maior detalhe pintado primeiro (geralmente o Asset 01, mais trabalhado desde a Semana 9); objetos mais simples podem ser resolvidos rapidamente ao final, mesmo que com menos refinamento.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe quais assets combinar | Perguntar: "Se você fosse montar uma cena de demonstração do seu kit agora, quais objetos apareceriam juntos, no mesmo enquadramento, com mais frequência?" A resposta geralmente revela o agrupamento natural sem precisar de instrução técnica adicional. |
| Estudante divide o espaço do atlas igualmente entre objetos de tamanhos diferentes | Colocar os três objetos lado a lado no viewport na escala real e perguntar: "Olhando assim, qual deles claramente precisa de mais pixels para não ficar borrado?" A comparação visual direta corrige a decisão mais rápido que a explicação teórica. |
| Estudante perdeu camadas de detalhe pintado ao remapear UV | Normalizar a situação como parte esperada do processo, não como erro: "Isso acontece sempre que se remapeia um UV já texturizado — a boa notícia é que vocês já sabem pintar desgaste e stencil desde as Semanas 9 e 10, então essa parte vai mais rápido da segunda vez." |
| Estudante inseguro se há sobreposição de UV entre objetos | Ensinar o uso da ferramenta de detecção automática de sobreposição do Blender, em vez de depender só da inspeção visual — reforçar que esse é um problema que vale a pena verificar com ferramenta, não só com o olho. |
| Estudante terminando rápido e com qualidade | Propor avaliar se um quarto asset do kit cabe no mesmo atlas sem comprometer a qualidade dos outros três, ou calcular quantas texturas o kit inteiro usava antes e depois da otimização de hoje — essa métrica concreta já antecipa parte do que será cobrado na CF5. |
| Estudante questionando se vale a pena reduzir resolução individual em troca de menos draw calls | Validar a pergunta como legítima — não há resposta única. Propor que o estudante registre esse trade-off por escrito como parte da justificativa: em que situações a economia de draw calls compensa a perda de resolução, e em que situações não compensaria (ex.: um asset em primeiro plano na cena, muito próximo da câmera). |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Justificativa escrita da escolha dos três assets combinados no atlas, baseada em uso conjunto em cena | C7 — Otimização | A justificativa é técnica (frequência de uso conjunto, tamanho relativo) ou apenas conveniência ("eram os que já estavam prontos")? |
| UV combinado de três ou mais assets em um único espaço 0–1, sem sobreposição indevida entre objetos | C3 — UV Mapping / C7 — Otimização | Há sobreposição verificada com a ferramenta de detecção do Blender? O padding entre grupos de objetos é suficiente? |
| Proporção de espaço no atlas coerente com o tamanho relativo dos objetos em cena | C7 — Otimização | O objeto maior recebeu proporcionalmente mais área de textura que o menor? A escolha foi justificada, não arbitrária? |
| Textura combinada 2048×2048 com os três objetos representados, preservando identidade visual individual de cada um | C5 — Texturização / C7 — Otimização | A qualidade visual de cada objeto se manteve após a compressão no espaço compartilhado, comparada ao estado anterior? |
| Camadas de detalhe (desgaste, stencil, bake) reconstruídas corretamente na nova posição do UV, quando aplicável | C5 — Texturização / C6 — Bake | O detalhe reconstruído mantém a mesma qualidade e coerência narrativa do original, ou houve perda perceptível? |
| Render comparativo documentando o número de texturas do kit antes e depois da criação do atlas | C1 — Processo de Projeto | A evolução é compreensível sem explicação verbal? Há uma métrica concreta (número de texturas, resolução total) registrada? |
| Participação na crítica circulante: comentários referenciando a lógica de agrupamento específica dos colegas | C10 — Participação (obs.) | O feedback dado menciona critério técnico observável (proporção, padding, uso conjunto em cena), ou é genérico? |

---

## Entrega da Semana 13

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo Blender/3D Coat com os três (ou mais) assets combinados, UV remapeado e textura de atlas aplicada | `.blend` e projeto 3D Coat com sufixo `_Atlas_S13_Final` | Até o fim do segundo encontro |
| Textura do Texture Atlas exportada | `.png`, 2048×2048, pasta `_Atlas_S13` | Até o fim do segundo encontro |
| Justificativa escrita da escolha dos assets combinados (2–3 frases) | Documento digital ou anotação junto ao arquivo de entrega | Até o fim do segundo encontro |
| Render comparativo: assets com textura individual (antes) vs. com atlas combinado (depois) | `.png` com sufixo `_Comparativo_Atlas_S13` | Até o fim do segundo encontro |

> **Nota:** Não há nota formal nesta semana (crítica informal). A qualidade do atlas produzido hoje, junto com a justificativa de agrupamento, será avaliada como evidência de C7 na CF5 da Semana 14 (Trim Sheets), quando Otimização entra em nota formal pela primeira vez.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 13 | 2026*
