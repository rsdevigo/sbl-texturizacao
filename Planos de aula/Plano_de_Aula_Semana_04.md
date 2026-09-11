# Plano de Aula — Semana 4
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** I — Fundamentos, Mapeamento UV e Definição do Hero Asset (Semanas 1–5)
**Tema da semana:** Abertura de UV do Hero Asset Referência — Smart UV Project e seams manuais
**Apostila:** Parte II, Cap. 5 — UV Unwrapping (Smart UV Project, Seams e Unwrap manual)
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF1** (20% do Portfolio de Artefatos)

---

## O que já foi ministrado (Semana 3 — não repetir)

Os estudantes chegam com:

- Tema definido e Hero Asset Referência escolhido e justificado por escrito na Semana 3, com briefing já compartilhado com Modelagem 3D e Level Design
- Familiaridade técnica com o conceito de espaço UV (0–1), distorção, sobreposição e os quatro tipos de projeção (planar, cilíndrica, esférica, cúbica), praticada em objetos geométricos neutros na Semana 2
- **Nesta semana, cada estudante recebe pela primeira vez o Hero Asset Referência modelado por Modelagem 3D e Level Design** — é o primeiro contato com a malha real que vai acompanhar o estudante até a Semana 9. Abrir o UV dessa peça é a primeira operação técnica real do semestre sobre um asset que vale nota.

> **Nota de transição:** Esta é a primeira Crítica Formal do semestre (CF1) e a primeira vez que a Rubrica Mestre é aplicada com instrumento formal (Ficha de Crítica Formal + autoavaliação). O Critério avaliado é C3 — UV Mapping. Não há ainda material, textura ou pintura — apenas UV. O padrão de exigência é o Nível 3 da rubrica (não o nível máximo): islands organizadas, distorção controlada, seams com lógica, aproveitamento razoável de espaço.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar quando usar Smart UV Project e quais são suas limitações em relação ao unwrap manual guiado por seams.
2. Aplicar a lógica de corte de seams para reduzir distorção, escolhendo posições de corte que sejam tecnicamente eficientes e, sempre que possível, esteticamente discretas na peça final.
3. Abrir o UV completo do Hero Asset Referência combinando Smart UV Project (como ponto de partida ou comparação) e seams manuais com Unwrap, chegando a um layout de islands organizado.
4. Avaliar a qualidade do próprio layout UV usando o Stretch Overlay e o checkerboard, identificando distorção e desperdício de espaço antes da entrega.
5. Apresentar o UV do Hero Asset Referência na primeira Crítica Formal do semestre, com autoavaliação escrita segundo a Rubrica Mestre.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana | Nível esperado |
|---|---|---|
| C3 — UV Mapping | **Avaliado formalmente (CF1).** Seams com lógica de corte, islands organizadas, distorção controlada (Stretch Overlay predominantemente verde/azul-claro), aproveitamento de espaço no layout 0–1 | Nível 3 da rubrica |
| C1 — Processo de Projeto | Nomenclatura de arquivo consistente; registro do processo de decisão de seams | Observado |
| C10 — Participação nas Critiques | Clareza na apresentação da CF1; qualidade da autoavaliação escrita | Observado |

> Esta é a primeira vez que C3 recebe nota formal. C2 (Direção Artística) e C4 em diante ainda não são exigidos — não há material nem textura aplicados até aqui.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Hero Asset Referência de cada estudante, já modelado e entregue por Modelagem 3D e Level Design (arquivo `.blend`, `.fbx` ou `.obj`, conforme fluxo combinado entre as disciplinas)
- Textura checkerboard 1024×1024 para verificação visual de distorção
- Arquivo de demonstração: prop temático simples (barril, caixote ou pedra) sem UV aberto, preparado pelo professor
- Add-on de empacotamento de UV (UVPackmaster) ou uso do Pack Islands nativo do Blender como alternativa
- Ficha de Crítica Formal — Instrumento 1 da Rubrica Mestre (impressa ou digital)
- Ficha de Autoavaliação — Instrumento 2 da Rubrica Mestre (impressa ou digital), a ser preenchida antes da apresentação
- Projetor para demonstração e para a Crítica Formal
- Apostila — Parte II, Cap. 5 (disponibilizada antes da aula)

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Smart UV Project, seams e os princípios de um bom layout UV**

Objetivo: dar aos estudantes o vocabulário técnico e o critério de decisão necessários antes de abrirem o UV do próprio Hero Asset Referência.

**Conteúdo a cobrir:**

**1. Smart UV Project: quando usar e limitações (≈7 min)**

O Smart UV Project analisa a geometria e corta automaticamente onde detecta ângulos abruptos, gerando islands sem intervenção manual. É rápido e útil como ponto de partida ou para objetos secundários de baixa importância visual, mas tem limitações relevantes: os cortes nem sempre ficam em posições esteticamente discretas, a distribuição de islands raramely é eficiente no espaço 0–1, e a densidade de texel entre islands costuma ficar desigual. Para um Hero Asset — a peça que carrega a maior responsabilidade visual do semestre — o Smart UV Project não é suficiente sozinho.

**2. Seams: lógica de corte para reduzir distorção (≈8 min)**

Cortar um seam é decidir onde a "casca" do objeto vai se abrir para virar um plano. Uma boa lógica de corte busca:
- Cortar em arestas que naturalmente escondem a costura (cantos internos, embaixo da peça, junções entre partes distintas do modelo).
- Cortar em número suficiente para permitir que cada island fique relativamente plana (evitando distorção), mas sem fragmentar demais (o que multiplica costuras visíveis e desperdiça padding).
- Priorizar cortes ao longo de mudanças reais de superfície (uma borda, uma quina, uma junção de material) em vez de cortes arbitrários no meio de uma face contínua.

**3. Princípios de um bom layout UV (≈5 min)**

- **Islands organizadas:** agrupadas por lógica de superfície, não espalhadas aleatoriamente no espaço 0–1.
- **Padding consistente:** espaço suficiente entre islands para evitar sangramento de textura entre elas (referência prática: 4–8 px de padding em uma textura de 1024px).
- **Aproveitamento de espaço:** o objetivo é preencher o quadrado 0–1 da forma mais eficiente possível — cada pixel de textura não utilizado é resolução desperdiçada.

> **Nota do professor:** reforçar que hoje o critério técnico (Stretch Overlay, densidade de texel) já foi visto na Semana 2 em objetos neutros — a novidade desta semana é aplicar esse critério a uma decisão real de corte de seams em uma peça que vale nota.

---

### Demonstração — 20 minutos

**Abertura de UV de um prop simples com seams manuais**

**Parte 1 (≈12 min) — Do Smart UV Project ao unwrap manual:**

1. Abrir o arquivo de demonstração (prop temático sem UV) e aplicar Smart UV Project primeiro, mostrando o resultado: islands funcionais, mas com cortes em posições pouco discretas e aproveitamento de espaço mediano.
2. Desfazer e refazer o processo manualmente: marcar seams nas arestas estrategicamente escolhidas (cantos, junções), aplicar Unwrap e comparar o resultado lado a lado com o Smart UV Project.
3. Perguntar à turma: *"Qual dos dois layouts vocês escolheriam para o Hero Asset de vocês? Por quê?"*

**Parte 2 (≈8 min) — Organização de UV islands no UV Editor:**

1. Ativar o checkerboard e o Stretch Overlay para avaliar visualmente a distorção do unwrap manual.
2. Reorganizar as islands no espaço 0–1 usando Average Islands Scale (para igualar densidade de texel) e Pack Islands (para otimizar aproveitamento de espaço e padding).
3. Fechar comparando o resultado final com o Smart UV Project inicial, reforçando: *"O Smart UV Project foi útil como primeira leitura da geometria, mas o resultado final que vai para a Crítica Formal precisa do julgamento manual de vocês."*

> **Nota do professor:** manter o arquivo de demonstração aberto durante o estúdio como referência visual para dúvidas de seams e organização de islands.

---

### Produção em Estúdio — 50 minutos

**Abertura de UV do Hero Asset Referência**

**Consigna entregue verbalmente:**

> *"Vocês receberam o Hero Asset Referência modelado por Modelagem 3D e Level Design. A tarefa de hoje é abrir o UV completo dessa peça: comecem testando o Smart UV Project para ter uma primeira leitura da geometria, depois marquem seams manualmente nos pontos estratégicos e apliquem Unwrap. O objetivo final é um layout de islands organizado, com distorção controlada e bom aproveitamento de espaço — é esse UV que vai para a Crítica Formal no próximo encontro."*

**Atividade estruturada:**

1. **(10 min) Importação e primeira leitura da geometria.** Importar o Hero Asset Referência recebido de Modelagem 3D e Level Design. Aplicar Smart UV Project como primeira leitura, identificando visualmente onde a malha tem mais complexidade de forma.
2. **(25 min) Marcação de seams e unwrap manual.** Marcar seams nos pontos estrategicamente escolhidos (cantos, junções, mudanças reais de superfície). Aplicar Unwrap e avaliar o resultado com o Stretch Overlay.
3. **(15 min) Organização do layout.** Aplicar Average Islands Scale e Pack Islands. Ativar o checkerboard para verificação visual final. Ajustar manualmente islands que ainda estejam mal posicionadas ou sobrepostas.

**Papel do professor:**

Circular pelo estúdio perguntando:
- *"Por que você cortou o seam aqui e não ali? Essa costura vai aparecer na peça final?"*
- *"O Stretch Overlay está mostrando vermelho nessa island — o que isso significa e como você resolve?"*
- *"Esse espaço vazio no canto do layout 0–1 é resolução desperdiçada — dá para reorganizar?"*

Identificar estudantes com seams excessivamente fragmentados ou distorção não resolvida — eles vão precisar de atenção prioritária no Encontro 2, antes da apresentação da CF1.

> **Nota do professor:** garantir que todo estudante termine o Encontro 1 com um UV pelo menos funcional (sem sobreposição, sem distorção extrema), mesmo que ainda não refinado — o refinamento final acontece no início do Encontro 2, antes da Crítica Formal.

---

## ENCONTRO 2 (1h30)

### Produção em Estúdio — 30 minutos

**Refinamento final e preparação para a Crítica Formal**

**Consigna:**

> *"Trinta minutos para fechar o UV antes da Crítica Formal. Revisem o Stretch Overlay uma última vez, confirmem o aproveitamento de espaço com Pack Islands, e capturem o screenshot do UV layout com checkerboard que vocês vão apresentar. Depois, preencham a Ficha de Autoavaliação — ela é obrigatória e entra antes da apresentação, não depois."*

**Atividade:**

1. Revisão final do Stretch Overlay e correção de qualquer distorção residual.
2. Confirmação do aproveitamento de espaço e padding com Pack Islands.
3. Captura do screenshot do UV layout com checkerboard aplicado (evidência principal da CF1).
4. Preenchimento da Ficha de Autoavaliação (Instrumento 2 da Rubrica Mestre), com base no Nível 3 do Critério C3.
5. Salvar: `[Nome]_HeroAsset_UV_Semana04.blend`.

**Papel do professor:**

Últimos ajustes individuais antes da CF1; verificar que todos os estudantes têm a Ficha de Autoavaliação preenchida antes do início das apresentações.

---

### Crítica Formal 1 (CF1) — 50 minutos

**Formato: apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito**

**Roteiro:**

1. **(≈3 min por estudante, ajustar conforme tamanho da turma)** Cada estudante apresenta o UV do Hero Asset Referência: mostra o layout com checkerboard, explica a lógica de corte dos seams escolhidos e lê brevemente sua autoavaliação (Nível atribuído a si mesmo no Critério C3 e justificativa).
2. **(feedback do professor e da turma, 1–2 comentários por apresentação)** Perguntas focadas no Critério C3: *"Essa distorção aqui compromete a textura futura?"*, *"Esse aproveitamento de espaço está adequado para a resolução que vocês vão usar?"*
3. **(fechamento, 5 min no total)** Professor sistematiza padrões observados na turma (erros recorrentes de seams, exemplos de bom aproveitamento de espaço) e anuncia que o feedback escrito individual (Ficha de Crítica Formal) será entregue até o fim da aula ou no início da Semana 5.

**Papel do professor:**

Preencher a Ficha de Crítica Formal (Instrumento 1) para cada estudante durante ou imediatamente após a apresentação, atribuindo nível ao Critério C3 e registrando ao menos um ponto forte e um ponto de melhoria específico e acionável — esse feedback é o que orienta a revisão de UV da Semana 5.

> **Nota do professor:** manter o ritmo — é preferível um feedback objetivo e acionável para todos do que um aprofundamento longo em poucos estudantes. O feedback escrito completo pode ser finalizado fora do horário de aula, desde que entregue a tempo de orientar a revisão da Semana 5.

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min) Síntese técnica pelo professor:** *"Vocês acabaram de passar pela primeira Crítica Formal do semestre. O UV que vocês abriram hoje é o endereço onde toda textura, todo material e toda pintura das próximas semanas vai morar — um UV mal resolvido agora se paga caro depois, quando for muito mais difícil de corrigir."*

2. **(3 min) Reflexão individual registrada** (post-it físico, digital ou comentário no arquivo):
   *"Complete a frase: 'O feedback que mais me surpreendeu na CF1 foi ____. Na Semana 5, vou corrigir ____ primeiro.'"*

3. **(2 min) Ponte para a Semana 5:** *"Na próxima semana, vocês corrigem o UV com base no feedback de hoje e começam a trabalhar com PBR — a primeira vez que vamos sair do UV Editor e entrar no Shader Editor. Não há crítica formal na Semana 5; é uma semana de ajuste e abertura para a próxima etapa."*

4. **(2 min) Confirmação das entregas:**
   - Hero Asset Referência com UV aberto (arquivo `.blend`)
   - Screenshot do UV layout com checkerboard
   - Ficha de Autoavaliação preenchida (entregue antes da apresentação)

---

## Possíveis Dificuldades

**1. Seams excessivamente fragmentados**
Estudante corta seams em excesso, "por segurança", gerando muitas islands pequenas e desperdiçando padding. Estratégia: perguntar *"Cada corte que você fez resolve um problema real de distorção, ou é só precaução? Menos cortes bem escolhidos costumam valer mais do que muitos cortes arbitrários."*

**2. Confiar demais no Smart UV Project e não refinar manualmente**
Estudante aceita o resultado automático sem ajuste, mesmo com islands em posições pouco discretas ou aproveitamento de espaço ruim. Estratégia: comparar lado a lado com a Demonstração e perguntar *"Essa costura vai aparecer na parte mais visível da peça? Dá para reposicionar o seam?"*

**3. Distorção não identificada antes da entrega**
Estudante não ativa o Stretch Overlay e entrega um UV com distorção evidente sem perceber. Estratégia: tornar a verificação do Stretch Overlay um passo obrigatório da consigna, não opcional — reforçar antes da CF1.

**4. Densidade de texel desigual entre islands**
Islands de partes grandes da peça ficam proporcionalmente menores que islands de detalhes pequenos. Estratégia: aplicar Average Islands Scale antes do Pack Islands, e mostrar visualmente a diferença de densidade com o checkerboard.

**5. Ansiedade em torno da primeira Crítica Formal**
Por ser a primeira avaliação com nota do semestre, alguns estudantes ficam inseguros sobre o que "vale nota" de fato. Estratégia: relembrar explicitamente que o padrão esperado é o Nível 3 da rubrica, não o nível máximo — e que a CF1 avalia clareza de processo e domínio técnico do UV, não perfeição estética.

**6. Autoavaliação genérica ou não crítica**
Estudante preenche a Ficha de Autoavaliação atribuindo a si mesmo o nível máximo sem justificativa específica. Estratégia: exigir que a justificativa cite um ponto concreto do próprio UV (uma island específica, uma decisão de seam), não uma afirmação genérica de qualidade.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Seams fragmentados demais | Perguntar se cada corte resolve um problema real de distorção; consolidar islands quando possível. |
| Confiança excessiva no Smart UV Project sem refinamento manual | Comparar lado a lado com o resultado manual da Demonstração; perguntar sobre visibilidade da costura na peça final. |
| Distorção não verificada | Tornar a checagem do Stretch Overlay etapa obrigatória antes de qualquer entrega. |
| Densidade de texel desigual | Aplicar Average Islands Scale antes do Pack Islands; usar o checkerboard como evidência visual. |
| Insegurança sobre o padrão de avaliação da CF1 | Relembrar que o nível esperado é o Nível 3 da rubrica, com foco em processo e domínio técnico, não perfeição estética. |
| Autoavaliação superficial | Exigir justificativa com referência a um elemento concreto do próprio UV. |

---

## Evidências de Aprendizagem

| Evidência | Objetivo(s) relacionado(s) | Critério da Rubrica | Como avaliar |
|---|---|---|---|
| UV do Hero Asset Referência aberto (seams manuais + Unwrap, organizado com Pack Islands) | Objetivos 1, 2, 3 | C3 — UV Mapping | Análise do Stretch Overlay (distorção), organização e aproveitamento de espaço do layout 0–1, lógica de corte dos seams |
| Screenshot do UV layout com checkerboard | Objetivo 4 | C3 — UV Mapping | Clareza visual do layout apresentado; ausência de sobreposição de islands |
| Ficha de Autoavaliação preenchida antes da apresentação | Objetivo 5 | C10 — Participação nas Critiques | Especificidade e honestidade da autoavaliação frente ao Nível 3 da rubrica |
| Apresentação na Crítica Formal 1 (CF1) | Objetivo 5 | C3, C10 | Clareza da explicação da lógica de seams; qualidade das respostas ao feedback |

---

## Entrega da Semana 4

| Entrega | Formato | Escopo | Prazo |
|---|---|---|---|
| Hero Asset Referência com UV aberto | `.blend` com sufixo `_HeroAsset_UV_Semana04` | Individual | Até o início da Crítica Formal (Encontro 2) |
| Screenshot do UV layout com checkerboard | PNG ou JPG | Individual | Até o início da Crítica Formal (Encontro 2) |
| Ficha de Autoavaliação (Instrumento 2) | PDF ou digital | Individual | Antes da apresentação na CF1 |
| Ficha de Crítica Formal (Instrumento 1) com feedback escrito | PDF ou digital | Preenchida pelo professor | Até o fim da aula ou início da Semana 5 |

> Esta é a primeira Crítica Formal do semestre (CF1, 20% da nota). A próxima Crítica Formal só acontece na Semana 8 (CF2) — a Semana 5 é de ajuste e abertura, sem nova cobrança de rubrica.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 4 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
