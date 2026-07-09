# Plano de Aula — Semana 12
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** III — Pintura Digital e Bake
**Tema:** Bake avançado: ID Map, Curvature e integração ao workflow PBR
**Apostila:** Cap. 8 — ID Map e Curvature Map; Uso de bakes como base de mascaramento no 3D Coat
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 **Informal** — circulante, sem nota formal nesta semana

---

## Pré-requisito da semana

Os estudantes chegam com:

- Fluxo completo de bake de **Normal Map** e **Ambient Occlusion** dominado: high-poly/low-poly, cage, ray distance/extrusion, resolução e margin — Semana 11
- Pelo menos uma área de um dos assets já com bake de Normal + AO integrado ao material no 3D Coat, convivendo com desgaste pintado (S09) e stencil (S10) — Semana 11
- Feedback escrito da Crítica Formal 4 (CF4), com ponto forte e prioridade de melhoria identificados por estudante — Semana 11
- Ficha de Autoavaliação da CF4 já devolvida com anotações do professor

> **Nota de transição:** A Semana 11 resolveu o problema de transferir **geometria real** (chanfros, entalhes) do high-poly para o low-poly via Normal Map e AO. Esta semana não introduz um novo processo de bake — o fluxo de seleção de objetos, cage e execução já foi aprendido. O que muda é o **uso** do bake: ID Map e Curvature Map não existem para adicionar detalhe visual diretamente, mas para gerar **máscaras automáticas** que aceleram a texturização no 3D Coat. É a primeira vez na disciplina em que o bake deixa de ser apenas "captura de aparência" e passa a ser "captura de informação para seleção". Esse é o ponto central da aula: o estudante já sabe bakear — agora aprende a bakear *para outro propósito*.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar a diferença de propósito entre os bakes já dominados (Normal, AO — geram aparência) e os bakes desta semana (ID Map, Curvature — geram máscara de seleção).
2. Configurar um bake de **ID Map** atribuindo cores distintas por material ou grupo de faces no high-poly ou no próprio low-poly.
3. Configurar um bake de **Curvature Map**, identificando regiões convexas (arestas, cantos salientes) e côncavas (sulcos, frestas) do asset.
4. Importar o pacote completo de bakes (Normal, AO, Curvature, ID Map) no 3D Coat e utilizá-lo como base de **mascaramento automático** — Curvature para edge highlight e cavity dirt, ID Map para seleção rápida por material.
5. Comparar o resultado de uma máscara gerada automaticamente por bake com o desgaste pintado manualmente nas Semanas 9 e 10, avaliando onde a automação economiza tempo sem comprometer a intenção artística.
6. Justificar, em crítica circulante, a escolha de quais áreas do kit se beneficiam de mascaramento automático versus pintura livre.

---

## Critérios observados nesta semana

> 🔵 **Crítica Informal.** Não há nota formal nesta semana. C6 (Bake) e C5 (Texturização) seguem em observação contínua — a evidência de hoje será insumo direto para a CF5 (Semana 14, Trim Sheets), quando o kit inteiro precisa estar coerente.

| Critério | Status | O que observar |
|---|---|---|
| C1 — Processo de Projeto | obs. | Registro do pacote de bakes gerado, nomenclatura consistente com a S11 |
| C5 — Texturização | obs. | O detalhe gerado por máscara automática (curvature/ID) dialoga com o desgaste já pintado, ou parece mecânico e descolado? |
| C6 — Bake | obs. — aprofundamento | Domínio de dois novos tipos de bake (ID Map, Curvature); qualidade técnica (sem artefatos, cores de ID separadas corretamente) |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado na crítica circulante |

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Computadores com 3D Coat instalado (versão 2023 ou superior)
- Arquivos `.blend` do Asset 01 e Asset 02 de cada estudante, já com pacote de bake de Normal + AO da Semana 11
- Arquivo de demonstração do professor: asset com pelo menos dois materiais distintos (ex: madeira + reforço metálico) preparado para bake de ID Map, e mesmo asset com detalhe de aresta/sulco suficiente para um Curvature Map ilustrativo
- Projetor para demonstração
- Apostila Cap. 8 — trecho de ID Map e Curvature Map, disponibilizado antes da aula

> **Preparação do asset de demonstração:** É necessário que o asset já tenha **grupos de material ou seleções de face nomeadas** antes da aula (ex: `Mat_Madeira`, `Mat_Metal`) — atribuir isso ao vivo consumiria tempo da demonstração. O ID Map depende inteiramente dessa organização prévia.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**De captura de aparência para captura de informação: ID Map e Curvature como máscara**

Objetivo: deslocar o entendimento do estudante de "bake gera uma textura que se vê" (Normal, AO) para "bake pode gerar uma textura que se usa para selecionar" (ID Map, Curvature).

**Abertura:**

Exibir no projetor um asset com dois materiais visualmente distintos (madeira + metal) já texturizado manualmente na Semana 10, ao lado do mesmo asset com um ID Map colorido (uma cor sólida por material). Perguntar: *"Se eu quisesse selecionar só a área de metal deste objeto para aplicar um desgaste diferente, sem usar o mouse para clicar peça por peça, como essa segunda imagem me ajudaria?"*

Deixar 2–3 respostas. Direcionar para a ideia central: cada cor sólida no ID Map corresponde a um material ou grupo de faces — o 3D Coat pode usar essa imagem para gerar uma **máscara de seleção instantânea**, sem depender de seams ou cliques manuais.

---

**Conteúdo a cobrir:**

**1. ID Map (Material ID): mapa de seleção por cor**

O ID Map atribui uma cor sólida e única a cada material ou grupo de faces do asset — não representa luz, sombra ou textura, apenas identidade. No Blender, isso é configurado atribuindo materiais simples com cores diferentes (ou usando o node `Object Info → Random` para variações automáticas por objeto) e bakeando com `Bake Type: Diffuse` (apenas contribuição de cor, sem luz) ou o node dedicado a ID, dependendo da versão.

*"O ID Map não tenta parecer bonito. Ele existe para ser lido por um programa, não por um olho humano — a única regra é que cada área que você quer selecionar depois precisa ter uma cor exclusiva e sem gradiente."*

**2. Curvature Map: leitura automática de arestas e sulcos**

O Curvature Map compara a normal de cada ponto da superfície com a de seus vizinhos: onde a superfície se curva "para fora" (convexo — arestas, cantos, relevos salientes), o mapa registra um tom claro; onde se curva "para dentro" (côncavo — sulcos, frestas, reentrâncias), um tom escuro. Diferente do AO — que mede oclusão de luz — a Curvature mede **geometria pura**, independente de iluminação.

*"Lembrem da Semana 9: vocês pintaram EdgeWear nas arestas à mão, decidindo região por região onde o desgaste faz sentido. O Curvature Map faz uma primeira passada automática disso — ele já sabe, geometricamente, onde estão as arestas e os sulcos do modelo. Vocês continuam no controle da decisão artística, mas não partem mais do zero."*

**3. Por que essas máscaras aceleram o 3D Coat sem substituir a pintura**

No 3D Coat, o Curvature Map importado pode alimentar diretamente os geradores de **Edge Highlight** (realce de aresta) e **Cavity Dirt** (sujeira de cavidade) — efeitos que, nas Semanas 9 e 10, foram construídos manualmente com pincéis e alphas. O ID Map alimenta seleções rápidas por material, permitindo isolar "só o metal" ou "só a madeira" com um clique para aplicar um ajuste de cor, roughness ou desgaste específico daquele material.

*"O objetivo de hoje não é abandonar o pincel — é usar as duas primeiras camadas de decisão (onde há aresta, onde há material X) automaticamente, para que o tempo de pintura livre de vocês seja gasto em refinamento artístico, não em selecionar região por região manualmente."*

**4. Relação com os parâmetros já dominados na Semana 11**

Cage, ray distance, resolução e margin funcionam exatamente como na semana passada — não há parâmetro novo de configuração de bake em si. A única diferença real está na preparação **antes** do bake: para ID Map, é preciso ter materiais ou grupos de face organizados; para Curvature, nenhuma preparação especial é necessária além de já ter o high-poly (ou o próprio low-poly, se o detalhe de aresta já existir na malha de produção).

> **Nota do professor:** Reforçar que o Curvature pode ser gerado a partir do **low-poly puro**, sem depender de um high-poly — diferente do Normal e AO da S11, que exigiam o par high/low. Isso costuma gerar confusão: alguns estudantes vão tentar duplicar um high-poly desnecessariamente para o Curvature. Esclarecer isso já na mini aula evita retrabalho no estúdio.

---

### Demonstração — 20 minutos

**Bake de ID Map e Curvature Map, e importação do pacote completo no 3D Coat**

**Setup (1 min):**
Abrir o Blender com o asset de demonstração já preparado: dois materiais nomeados e coloridos (`Mat_Madeira`, `Mat_Metal`) e o par high-poly/low-poly reaproveitado da Semana 11.

**Percurso da demonstração:**

**Passo 1 — Bake de ID Map (7 min):**
1. Mostrar os dois materiais já atribuídos por seleção de face no low-poly, cada um com uma cor base sólida e distinta (ex: vermelho puro para madeira, verde puro para metal — cores saturadas, fáceis de distinguir sem ambiguidade).
2. Criar um novo `Image Texture Node`, `Asset_IDMap_2048`, Color Space **sRGB** (diferente de Normal e AO, que usam Non-Color — o ID Map representa cor pura de identidade, não dado técnico).
3. Em `Bake Type`, selecionar **Diffuse** com apenas o contribuidor **Color** ativo (desligar Direct e Indirect) — isso captura só a cor base de cada material, sem influência de luz ou sombra.
4. Executar o bake. Mostrar o resultado: um mapa com blocos de cor sólida correspondendo exatamente às áreas de cada material.
5. *"Reparem que não há gradiente nenhum entre as cores — se aparecer um degradê na borda, geralmente é sinal de anti-aliasing na configuração de bake, e isso precisa ser desligado para ID Map funcionar como máscara limpa no 3D Coat."*

**Passo 2 — Bake de Curvature Map (6 min):**
1. Criar novo `Image Texture Node`: `Asset_CurvatureBake_2048`, Non-Color.
2. Mostrar que, para este bake, **não é necessário** selecionar high-poly e low-poly juntos — pode-se bakear a curvatura do próprio low-poly diretamente (ou usar o high-poly se houver detalhe fino que só existe nele).
3. Em `Bake Type`, usar o método disponível na versão do Blender (nó `Pointiness` no Color Attribute, ou addon/shader de curvature, conforme a apostila Cap. 8 detalha o procedimento passo a passo da versão em uso).
4. Executar o bake. Mostrar o resultado: tons claros nas arestas do baú/objeto, tons escuros nos sulcos e reentrâncias.
5. *"Comparem mentalmente com o AO da semana passada: a AO escurece onde falta luz ambiente; a Curvature escurece onde a geometria é côncava, independente de luz nenhuma. São informações diferentes, mesmo que visualmente pareçam parecidas à primeira vista."*

**Passo 3 — Importação do pacote completo no 3D Coat (5 min):**
1. Alternar para o 3D Coat com o asset já texturizado (base + desgaste da S09/S10 + Normal/AO da S11).
2. Importar o Curvature Map recém-gerado como fonte para o gerador **Cavity Dirt**: mostrar o painel onde essa opção aceita uma textura externa em vez de calcular a curvatura internamente a partir da malha.
3. Importar o ID Map como base de uma **seleção por cor** (ferramenta de seleção/máscara do 3D Coat que lê blocos de cor): isolar a área "metal" com um clique e aplicar um ajuste rápido de roughness só naquela região, como exemplo.
4. Mostrar o resultado combinado: Cavity Dirt automático (via Curvature) por cima do desgaste já pintado manualmente, sem sobrepor de forma destrutiva — como uma camada adicional com opacidade ajustável.

**Passo 4 — Antes/depois (1 min):**
Alternar rapidamente entre o material sem as máscaras automáticas e com elas aplicadas, destacando o ganho de detalhe em frestas e a facilidade da seleção por material.

> **Nota do professor:** Se a versão do 3D Coat disponível no laboratório não tiver um gerador de Cavity Dirt que aceite textura externa diretamente, adaptar a demonstração usando a Curvature como **camada de máscara de opacidade** (Layer Mask) sobre uma camada de sujeira já pintada — o princípio pedagógico (curvature acelera decisão de onde aplicar sujeira) se mantém mesmo que o caminho técnico exato varie por versão.

---

### Produção em Estúdio — 50 minutos

**Bake de ID Map e Curvature em um asset do kit**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com dois objetivos: primeiro, gerar o ID Map de um asset do kit que tenha pelo menos dois materiais distintos — se nenhum dos seus assets tiver isso ainda, aproveitem para separar rapidamente uma área que deveria ser de material diferente (ex: reforço metálico numa peça de madeira). Segundo, gerar o Curvature Map do mesmo asset. No fim, vocês terão o pacote completo de quatro bakes: Normal e AO da semana passada, mais ID Map e Curvature de hoje."*

**Atividade estruturada:**

**Etapa 1 — Organização de materiais para ID Map (≈12 min):**
1. Escolher o asset com maior potencial de separação de material (ex: madeira + metal, pedra + musgo, painel + reforço).
2. Se os materiais ainda não estiverem separados por seleção de face: usar `Edit Mode → Face Select` para isolar a região e atribuir um novo material simples com cor sólida distinta (cores saturadas e bem diferentes entre si — evitar tons próximos que dificultem a leitura da máscara).
3. Nomear os materiais de forma clara (`ID_Madeira`, `ID_Metal`, etc.) para facilitar o registro de processo.

**Etapa 2 — Bake de ID Map (≈13 min):**
1. Criar o Image Texture Node de destino (`Asset_IDMap_2048`, sRGB).
2. Configurar `Bake Type: Diffuse`, apenas contribuidor Color ativo.
3. Executar o bake. Verificar se as cores aparecem em blocos sólidos, sem gradiente nas bordas.
4. Se houver problema de anti-aliasing entre ilhas: revisar a configuração de amostragem do bake (reduzir samples ou desligar filtro, conforme a apostila).

**Etapa 3 — Bake de Curvature Map (≈15 min):**
1. Sem necessidade de recriar o par high/low: bakear diretamente a partir do low-poly (ou do high-poly da S11, se o detalhe relevante estiver só nele).
2. Criar o Image Texture Node de destino (`Asset_CurvatureBake_2048`, Non-Color).
3. Executar o bake conforme o método demonstrado (Pointiness/Curvature).
4. Verificar visualmente: arestas devem aparecer claras, sulcos escuros, sem ruído excessivo em superfícies planas.

**Etapa 4 — Registro de processo (≈10 min):**
1. Salvar o arquivo: `[Nome]_Asset0X_BakeCompleto_S12.blend`.
2. Exportar os quatro mapas (Normal, AO, ID Map, Curvature) para a pasta do asset.
3. Screenshot do ID Map e do Curvature Map lado a lado com o asset renderizado, para levar à crítica circulante do segundo encontro.

**Papel do professor:**

Circular verificando:

- **As cores do ID Map estão suficientemente distintas?** Cores próximas (ex: dois tons de marrom) dificultam a seleção por cor no 3D Coat depois. Sugerir substituição por cores saturadas e opostas na roda cromática.
- **O estudante está tentando duplicar um high-poly desnecessário para o Curvature?** Reforçar o ponto da mini aula: Curvature funciona direto no low-poly na maioria dos casos.
- **O objetivo é o pacote completo de quatro mapas, não um asset perfeito.** Reforçar que hoje é sobre dominar a geração dos dois mapas novos — a aplicação refinada acontece no encontro 2.

Perguntas de mediação circulante:
- *"Se você entregasse esse ID Map para outra pessoa sem explicação nenhuma, ela conseguiria adivinhar quantos materiais esse objeto tem só olhando o mapa?"*
- *"Olhando o Curvature Map, você concorda com onde ele marcou as arestas mais claras? Faz sentido com onde você já pintou desgaste nas Semanas 9 e 10, ou aponta um lugar que você ainda não tinha notado?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva — 20 minutos

**Formato: circulante, sem nota formal**

**Abertura (2 min):**
*"Hoje é crítica circulante — vou passar de estação em estação. Tenham o ID Map e o Curvature Map abertos lado a lado com o render do asset. Quero ver se a máscara automática que vocês geraram faz sentido com o que vocês já sabem sobre o próprio trabalho."*

**Dinâmica (16 min):**
Circulação livre pelas estações. Em cada uma, o professor observa os dois novos mapas e faz 1–2 perguntas direcionadas:
- *"Essa cor no ID Map corresponde exatamente à área que deveria ser metal? Tem algum pixel isolado de cor errada?"*
- *"Onde o Curvature marcou mais claro, é onde você acha que a luz bateria mais numa aresta real?"*

Encorajar comentários entre colegas próximos — *"Passem para o vizinho: vocês concordam com a separação de material que ele fez?"* — sem formalizar como avaliação por pares registrada (isso é reservado às críticas formais).

**Síntese (2 min):**
*"A maior parte de vocês já tem o pacote completo de quatro bakes. O trabalho de hoje no estúdio é usar essas duas novas máscaras dentro do 3D Coat para acelerar a texturização — não é para substituir o que vocês pintaram, é para dar um empurrão automático antes de refinar à mão."*

---

### Produção em Estúdio — 60 minutos

**Integração de ID Map e Curvature ao workflow do 3D Coat**

**Consigna:**

> *"Sessenta minutos para levar os dois mapas novos até dentro do 3D Coat e usá-los de verdade: Curvature para acelerar desgaste em arestas e sujeira em cavidades, ID Map para selecionar rapidamente uma região de material e ajustar algo nela — cor, roughness, ou um detalhe pintado só naquela área."*

**Atividade estruturada:**

**Bloco 1 — Importação e configuração no 3D Coat (≈15 min):**
1. Importar Normal, AO (já existentes da S11), ID Map e Curvature (novos) no 3D Coat, cada um no canal ou uso correspondente.
2. Configurar o Curvature como fonte de Cavity Dirt/Edge Highlight (ou como máscara de opacidade sobre uma camada de sujeira, conforme o caminho técnico disponível na versão instalada).
3. Configurar o ID Map como referência de seleção por cor.

**Bloco 2 — Aplicação de Curvature em desgaste (≈20 min):**
1. Usar a máscara gerada pelo Curvature para aplicar Cavity Dirt automaticamente nas reentrâncias do asset.
2. Comparar com o Dirt pintado manualmente nas Semanas 9–10: ajustar a opacidade da camada automática para que ela **reforce**, e não duplique ou contradiga, o que já foi pintado à mão.
3. Ajustar manualmente qualquer área onde a máscara automática exagerou ou ficou fraca demais — o objetivo é combinação, não substituição total.

**Bloco 3 — Aplicação de seleção por ID Map (≈15 min):**
1. Usar a ferramenta de seleção por cor do 3D Coat lendo o ID Map para isolar uma das regiões de material (ex: só o metal).
2. Aplicar um ajuste específico àquela região isolada: variação de roughness, cor ligeiramente diferente, ou um detalhe de desgaste característico daquele material (ex: ferrugem só no metal, não na madeira).
3. Verificar que a seleção automática não vazou para a região errada — se vazou, revisar a separação de material feita no Blender no primeiro encontro.

**Bloco 4 — Registro final (≈10 min):**
1. Exportar os mapas atualizados e salvar o projeto do 3D Coat.
2. Renders comparativos: sem máscaras automáticas vs. com Curvature e ID Map aplicados.
3. Salvar arquivo Blender/3D Coat com sufixo `_BakeCompleto_S12_Final`.

**Papel do professor:**

- Priorizar apoio individual aos estudantes cuja separação de material no ID Map ficou com vazamento de cor (geralmente exige voltar ao Blender e revisar a seleção de faces).
- Para estudantes que terminam rápido: sugerir aplicar o mesmo fluxo (Curvature + ID Map) no segundo asset do kit, mantendo coerência entre Asset 01 e Asset 02.
- Perguntas de mediação: *"Se você tivesse feito esse desgaste todo à mão, quanto tempo acha que teria levado comparado a usar a máscara automática como ponto de partida? Onde a automação te economizou trabalho, e onde ela ainda precisou da sua decisão artística?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese técnica)**
*"Hoje vocês fecharam o pacote completo de bake da disciplina: Normal, AO, Curvature e ID Map. A partir de agora, qualquer asset novo que vocês criarem pode passar por esse fluxo completo desde o início, em vez de aprender cada mapa separadamente."*

2. **(3 min — Reflexão sobre automação vs. decisão artística)**
Pergunta aberta: *"Em que momento, hoje, vocês sentiram que a máscara automática (Curvature ou ID Map) tomou uma decisão que vocês não teriam tomado sozinhos — para melhor ou para pior?"*
Deixar 2–3 respostas. O objetivo é consolidar que ferramentas automáticas em produção de jogos aceleram, mas não substituem, o julgamento artístico — um tema que volta a aparecer nas Semanas 13–15 com Atlas, Trim Sheets e otimização.

3. **(2 min — Antecipação da Semana 13)**
*"Semana que vem começamos a Unidade IV: otimização e integração ao motor. A primeira parada é Texture Atlas — vamos unificar vários assets do kit em uma única textura para reduzir draw calls. Antes de chegar: pensem em quais três assets do seu kit poderiam, plausivelmente, compartilhar a mesma textura sem perder qualidade visual."*

4. **(2 min — Confirmação das entregas)**
Recapitular nomenclatura de entrega e prazo. Lembrar que o pacote de quatro bakes será referência de qualidade técnica (C6) na CF5 da Semana 14.

---

## Possíveis Dificuldades

**1. Cores do ID Map muito próximas entre si**
Quando dois materiais recebem cores similares (ex: dois tons de cinza ou de marrom), a seleção por cor no 3D Coat pode capturar as duas áreas juntas ou nenhuma corretamente. Estratégia: antes do bake, revisar as cores atribuídas no Blender e substituir por cores saturadas e opostas na roda cromática — vermelho puro, verde puro, azul puro, magenta — mesmo que essas cores nunca apareçam no material final; o ID Map não representa aparência, só identidade.

**2. Vazamento de seleção entre materiais na borda das faces**
Mesmo com cores bem distintas, pode haver um contorno de mistura entre as duas cores na borda da seleção de face, causado por anti-aliasing do bake. Estratégia: desligar qualquer suavização/anti-aliasing na configuração do bake de Diffuse/ID Map — a nitidez da borda é mais importante que a suavidade visual neste caso específico.

**3. Estudante tenta recriar o par high-poly/low-poly para Curvature sem necessidade**
Hábito reforçado pela Semana 11, em que high/low era sempre necessário. Estratégia: lembrar diretamente que Curvature funciona a partir da geometria existente do próprio low-poly (ou do high-poly da S11, se já existir e tiver detalhe relevante) — não é necessário duplicar objetos novamente.

**4. Curvature Map com ruído excessivo em superfícies que deveriam ser lisas**
Ocorre quando a malha tem N-gons (faces com mais de 4 lados) ou triangulação irregular, que geram variações de normal não intencionais. Estratégia: verificar a topologia da área problemática; se necessário, aplicar `Mesh → Clean Up → Fill Holes` ou retopologizar rapidamente a região antes de bakear novamente.

**5. Máscara automática de Curvature contradiz o desgaste já pintado manualmente**
O Cavity Dirt gerado automaticamente pode aparecer em uma área onde o estudante já havia decidido, artisticamente, que não deveria haver sujeira (ex: uma superfície polida por uso constante, que deveria ficar limpa mesmo sendo uma cavidade geométrica). Estratégia: reforçar que a opacidade da camada automática é sempre ajustável e que o estudante tem autoridade para reduzir ou apagar localmente onde a leitura automática não corresponde à narrativa de uso pretendida — a automação é ponto de partida, não veredito final.

**6. Tempo insuficiente para completar os quatro mapas em um único asset**
Alguns estudantes, especialmente os que tiveram mais dificuldade na Semana 11, podem não terminar o pacote completo dentro do primeiro encontro. Estratégia: priorizar a conclusão do ID Map (mais rápido e com maior valor pedagógico imediato) sobre o Curvature caso o tempo se esgote — o Curvature pode ser finalizado no início do estúdio do segundo encontro, antes do Bloco 1 de integração.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe como separar materiais para o ID Map | Perguntar: "Se você pegasse este objeto na vida real, quantos materiais fisicamente diferentes ele teria — não cores, materiais?" A resposta geralmente revela a separação correta (madeira vs. metal, tecido vs. couro) sem precisar de instrução técnica adicional. |
| Estudante com ID Map "vazando" cor entre regiões | Voltar ao Blender e mostrar a seleção de faces em Edit Mode antes do bake — o problema quase sempre está na seleção de face incompleta ou sobreposta, não no bake em si. Resolver na origem antes de tentar ajustar o bake. |
| Estudante inseguro sobre onde aplicar Cavity Dirt automático | Pedir para comparar com o Dirt pintado manualmente na Semana 9: "Essas duas leituras concordam? Se sim, você pode confiar na automática como ponto de partida. Se não, qual delas está mais de acordo com a história de uso do seu objeto?" |
| Estudante terminando rápido e com qualidade | Propor aplicar o pacote completo de quatro bakes no segundo asset do kit, mantendo a mesma lógica de nomenclatura de material usada no primeiro — reforça consistência entre Asset 01 e Asset 02 (C2). |
| Estudante confuso sobre a diferença entre AO e Curvature | Usar a analogia: "A AO pergunta: quanta luz ambiente chega aqui? A Curvature pergunta: essa superfície se dobra para dentro ou para fora? Uma depende de luz, a outra só de forma. Às vezes concordam visualmente, mas medem coisas diferentes — por isso às vezes vale usar as duas juntas." |
| Estudante que resiste a usar a automação, preferindo pintar tudo manualmente | Validar a preferência artística, mas propor um teste controlado: aplicar a máscara automática em uma cópia da camada, comparar lado a lado com a versão pintada à mão, e decidir com base no resultado — não é obrigatório usar automação, mas vale experimentar antes de descartar. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| ID Map com cores sólidas e distintas por material, sem vazamento nas bordas de seleção | C6 — Bake | As cores são suficientemente distintas para seleção automática? Há gradiente ou mistura indevida entre regiões? |
| Curvature Map gerado a partir da geometria correta (low-poly ou high-poly conforme o caso), com arestas claras e sulcos escuros de forma coerente com a forma real do objeto | C6 — Bake | O mapa corresponde à geometria real? Há ruído excessivo em superfícies que deveriam ser lisas? |
| Pacote completo de quatro bakes (Normal, AO, Curvature, ID Map) organizado com nomenclatura consistente | C1 — Processo de Projeto | Os arquivos estão nomeados de forma que qualquer pessoa entenda o que cada mapa representa sem abrir o arquivo? |
| Cavity Dirt ou Edge Highlight gerado via Curvature, integrado como camada adicional (não substitutiva) sobre o desgaste pintado nas Semanas 9–10 | C5 — Texturização | O resultado automático reforça a narrativa de uso já construída, ou contradiz decisões artísticas anteriores sem ajuste? |
| Seleção por cor via ID Map usada para aplicar ao menos um ajuste específico de material (roughness, cor ou desgaste diferenciado) | C6 — Bake / C4 — Materiais PBR | A seleção automática isolou corretamente a região pretendida? O ajuste aplicado é fisicamente plausível para aquele material? |
| Comparativo visual (sem máscaras automáticas vs. com Curvature e ID Map aplicados) documentado com renders | C1 — Processo de Projeto | A evolução é compreensível sem explicação verbal? |
| Participação na crítica circulante: comentários referenciando os mapas específicos gerados (não observações genéricas) | C10 — Participação (obs.) | O feedback dado a colegas menciona critério técnico observável (separação de cor, coerência de curvature), ou é vago? |

---

## Entrega da Semana 12

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo Blender/3D Coat com pacote completo de bake (Normal, AO, Curvature, ID Map) integrado ao material do asset trabalhado | `.blend` e projeto 3D Coat com sufixo `_BakeCompleto_S12_Final` | Até o fim do segundo encontro |
| ID Map e Curvature Map exportados | `.png` na resolução de trabalho do asset (1024 ou 2048), pasta `_Bake_S12` | Até o fim do segundo encontro |
| Screenshot comparativo: sem máscaras automáticas vs. com Curvature e ID Map aplicados | `.png` com sufixo `_Comparativo_Bake_S12` | Até o fim do segundo encontro |

> **Nota:** Não há nota formal nesta semana (crítica informal). A qualidade do pacote de quatro bakes gerado hoje será avaliada como evidência de C6 na CF5 da Semana 14 (Trim Sheets), quando o kit precisa demonstrar coerência técnica completa entre todos os assets.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 12 | 2026*
