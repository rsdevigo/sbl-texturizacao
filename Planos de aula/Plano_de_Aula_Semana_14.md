# Plano de Aula — Semana 14
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização e Integração ao Motor
**Tema:** Trim Sheets: criação e aplicação para assets modulares
**Apostila:** Cap. 9 — Trim Sheets: conceito e workflow; Aplicação em arquitetura modular
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF5** (peso de 30% no Portfolio de Artefatos — o maior peso entre as cinco críticas formais realizadas até agora)

---

## Pré-requisito da semana

Os estudantes chegam com:

- Texture Atlas funcional, combinando ao menos três assets do kit em um único UV 2048×2048, com justificativa escrita de agrupamento e render comparativo antes/depois — Semana 13
- Pacote completo de bake (Normal, AO, Curvature, ID Map) integrado a pelo menos um asset do kit — Semana 12
- Dois assets consolidados (Asset 01 e Asset 02) com UV, material PBR, desgaste pintado e bake — Semanas 1 a 12
- Ficha de Autoavaliação da Rubrica Mestre preenchida **antes** desta aula (disponibilizada ao final da Semana 13)

> **Nota de transição:** A Semana 13 resolveu o problema de agrupar **objetos completos** em uma única textura compartilhada — o Texture Atlas parte do princípio de que cada objeto ocupa uma região fixa e exclusiva do espaço UV. Isso funciona bem para peças distintas, mas falha para um problema diferente, típico de kits modulares de ambiente: elementos arquitetônicos que se **repetem em grande quantidade com pequenas variações** — paredes, molduras, vigas, trilhos, bordas de encaixe. Repetir esses elementos no atlas, um do lado do outro, desperdiçaria espaço e criaria dezenas de UVs quase idênticas. A Trim Sheet resolve isso de outra forma: uma faixa estreita e longa de textura, projetada para ser **reutilizada via tiling** ao longo de qualquer comprimento de UV, permitindo que uma única textura sirva para paredes de 1 metro e paredes de 10 metros sem nunca precisar de uma textura nova. É uma ferramenta de otimização com lógica diferente da do atlas — não menos texturas por objeto, mas uma textura que se **estica e repete** para servir a qualquer quantidade de geometria modular.

> **Atenção — Crítica Formal (CF5):** Esta é a 5ª das 6 críticas formais da disciplina e a primeira em que o Critério 7 (Otimização) entra em nota formal — até aqui ele era apenas observado (Semana 13). C1, C2, C5, C6 e C9 seguem em nota; C4 (Materiais PBR) passa a ser apenas observado nesta CF; C3 (UV Mapping) e C8 (Integração na Unity) não se aplicam ainda. A CF5 corresponde a 30% do Portfolio de Artefatos — o maior peso das cinco, refletindo que o estudante já deve demonstrar domínio consolidado antes da reta final do semestre.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Diferenciar Trim Sheet de Texture Atlas quanto ao propósito: reutilização por tiling de elementos repetitivos versus agrupamento de objetos distintos em um único espaço fixo.
2. Planejar uma Trim Sheet temática, organizando faixas horizontais ou verticais por tipo de detalhe (madeira trabalhada, metal, pedra, sujeira, ornamento), coerente com a identidade visual do kit.
3. Mapear o UV de um asset arquitetônico modular (parede, viga, moldura) para uma faixa da Trim Sheet, aplicando UV elongado e tiling ao longo do comprimento da peça.
4. Validar o resultado do tiling no Blender e antecipar seu comportamento na Unity, verificando repetição sem costura visível (seam) e sem distorção de escala.
5. Aplicar a mesma Trim Sheet a mais de uma variação do asset modular, demonstrando o ganho de reutilização como evidência concreta de otimização (C7).
6. Apresentar formalmente, na CF5, a Trim Sheet produzida e o(s) asset(s) mapeado(s), justificando as decisões técnicas de otimização tomadas desde a Semana 13.

---

## Critérios avaliados nesta semana — CF5 (peso 30% no PA)

> 🔴 **Crítica Formal.** Esta semana atribui nota. Consultar a tabela **Critérios Ativos por Crítica Formal** da Rubrica Mestre antes de preencher a Ficha de Crítica Formal (Instrumento 1).

| Critério | Status na CF5 | O que observar |
|---|---|---|
| C1 — Processo de Projeto | ✓ Nota | Registro de processo desde a CF4: versões nomeadas, justificativa do atlas da Semana 13 incorporada, anotações de decisões da trim sheet |
| C2 — Direção Artística | ✓ Nota | A trim sheet mantém a paleta e a linguagem visual já estabelecidas no kit, ou introduz um estilo dissonante? |
| C3 — UV Mapping | — Não aplicável nesta CF | — |
| C4 — Materiais PBR | obs. — passa de nota para observação nesta CF | Os canais PBR da trim (roughness, metallic) seguem coerentes ao serem esticados/repetidos ao longo do tiling? |
| C5 — Texturização | ✓ Nota | O detalhe pintado na trim (desgaste, junções, ornamento) se sustenta visualmente quando repetido várias vezes lado a lado? |
| C6 — Bake | ✓ Nota | Trim sheets frequentemente usam Normal Map bakeado para reforçar profundidade de talha/entalhe ao longo da faixa — qualidade do bake aplicado à trim |
| C7 — Otimização | ✓ **Nota — primeira vez avaliado formalmente** | Redução do número de texturas únicas obtida com a trim; coerência de tiling; reutilização em mais de uma variação de asset |
| C8 — Integração na Unity | — Não aplicável nesta CF | — |
| C9 — Apresentação | ✓ Nota | Clareza da apresentação individual; capacidade de explicar o trade-off entre atlas (S13) e trim sheet (S14) |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado aos colegas durante a apresentação formal |

> **Lembrete de peso:** A CF5 corresponde a 30% da nota do Portfolio de Artefatos (PA), o maior peso entre as cinco críticas formais realizadas até o momento — reflexo de que a trajetória de aprendizagem já deveria estar consolidada às vésperas da reta final do semestre (Semanas 15 a 17).

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Computadores com 3D Coat instalado (versão 2023 ou superior)
- Arquivos `.blend`/projeto 3D Coat do kit de cada estudante, incluindo o Texture Atlas da Semana 13 e ao menos um asset arquitetônico modular (parede, viga, moldura) ainda com UV individual
- Arquivo de demonstração do professor: uma Trim Sheet temática já preparada de antemão (ex.: faixa de madeira trabalhada com talha, metal com rebites, pedra com fiada de tijolos) e um asset de parede modular pronto para ser mapeado nela ao vivo
- Projetor para demonstração e para a Crítica Formal
- Ficha de Crítica Formal (Instrumento 1 da Rubrica Mestre), uma por estudante
- Ficha de Autoavaliação (Instrumento 2), preenchida por cada estudante e trazida para a aula
- Apostila Cap. 9 — trecho de Trim Sheets, disponibilizado antes da aula

> **Preparação da Trim Sheet de demonstração:** É essencial que a trim já exista pronta antes da aula — pintá-la do zero consumiria o tempo da demonstração. A trim de referência deve ter ao menos três faixas distintas (ex.: madeira, metal, ornamento) para que a lógica de divisão por tipo de detalhe fique visualmente clara.

> **Preparação da Crítica Formal:** Definir previamente a ordem de apresentação (lista visível, ordem alfabética ou sorteio). Como na CF4, calcular o tempo com cuidado: 20 minutos para toda a turma é justo — para turmas grandes, considerar duplas simultâneas com o professor circulando, ou reservar parte do estúdio do Encontro 2 para completar apresentações que não couberam no bloco formal.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**De um UV por objeto para uma faixa que se repete: o que é uma Trim Sheet**

Objetivo: fazer o estudante entender a Trim Sheet como resposta a um problema que o Texture Atlas da Semana 13 não resolve — elementos modulares que se repetem em quantidade variável, não em conjuntos fixos.

**Abertura:**

Exibir no projetor uma parede modular composta por várias peças repetidas ao longo de um corredor do kit de referência. Perguntar: *"Se cada segmento dessa parede tivesse sua própria textura única, quantas texturas diferentes vocês estimam que esse corredor inteiro exigiria? E se essa parede tivesse que crescer em uma nova versão da cena, adicionando mais dez metros — quantas texturas novas seriam necessárias?"*

Deixar 2–3 respostas. Direcionar para a ideia central: o Texture Atlas resolve bem quando o número de objetos é conhecido e fixo (três assets específicos, Semana 13). Mas elementos arquitetônicos modulares — paredes, vigas, molduras, trilhos — se repetem em quantidade que muda conforme o design da cena. Uma Trim Sheet resolve isso com uma faixa de textura que se **estica e repete (tiling)** ao longo de qualquer comprimento de UV, sem nunca precisar de uma textura nova por segmento adicional.

---

**Conteúdo a cobrir:**

**1. Trim Sheet: definição e diferença em relação ao Texture Atlas**

Uma Trim Sheet é uma textura organizada em **faixas horizontais ou verticais**, cada uma representando um tipo de detalhe reutilizável (uma faixa de madeira trabalhada, uma faixa de metal com rebites, uma faixa de borda ornamentada). O UV de um asset modular é mapeado como uma tira estreita e longa sobre uma dessas faixas, com **tiling repetido** ao longo do comprimento da peça — diferente do Texture Atlas, em que cada objeto ocupa uma região fixa e única, sem repetição.

*"O atlas da semana passada é como uma folha de contato: cada foto aparece uma vez, num lugar fixo. A trim sheet de hoje é como um rolo de fita adesiva decorada: o padrão se repete quantas vezes for necessário, ao longo de qualquer comprimento que vocês precisarem cortar."*

**2. Tiling horizontal vs. vertical**

Faixas horizontais tendem a servir elementos que se repetem ao longo do comprimento (uma parede que se estende horizontalmente); faixas verticais servem elementos que se repetem em altura (uma coluna, um trilho vertical, uma moldura de porta). A escolha depende de como o asset modular realmente se repete na cena — não é uma decisão arbitrária de layout da textura.

**3. Planejamento de uma trim: divisão de faixas por tipo de detalhe**

Antes de pintar qualquer coisa, planejar quais faixas a trim vai conter, com base nos tipos de superfície mais recorrentes no kit do estudante:

- Uma faixa para o material estrutural dominante (madeira, pedra, metal — conforme o tema).
- Uma faixa para elementos de junção ou reforço (rebites, encaixes, vigas transversais).
- Uma faixa para detalhe ornamental ou de desgaste específico do tema (talha, ferrugem, musgo).

*"Pensem nas faixas da trim como um alfabeto visual do seu kit: em vez de escrever a mesma palavra várias vezes com tinta nova a cada vez, vocês criam as letras uma vez e as combinam quantas vezes precisarem."*

**4. Mapeamento do UV elongado e tiling**

O UV de um asset modular mapeado numa trim ocupa uma tira estreita (ex.: toda a largura da faixa, mas repetida várias vezes ao longo do eixo do comprimento). O texel density precisa ser calibrado para que o padrão se repita de forma consistente sem parecer "esticado" em peças mais longas nem "compactado demais" em peças mais curtas — o mesmo cuidado com texel density já dominado desde a Semana 4, aplicado agora sob a lógica de repetição.

> **Nota do professor:** O erro mais comum nesta etapa é o estudante tratar a trim como um atlas — mapeando o UV do asset uma única vez, sem tiling, perdendo toda a vantagem de reutilização da ferramenta. Reforçar que a trim só cumpre seu propósito se o UV realmente repetir o padrão ao longo do comprimento da peça.

**5. Onde a costura do tiling pode falhar**

Se as bordas esquerda e direita (ou superior e inferior) da faixa não forem desenhadas para se encontrarem sem descontinuidade, o tiling produz uma costura visível (seam) toda vez que o padrão se repete — o mesmo princípio de textura seamless da Semana 6, agora aplicado a uma faixa estreita em vez de uma textura quadrada completa.

---

### Demonstração — 20 minutos

**Criação e aplicação de uma Trim Sheet temática no 3D Coat**

**Setup (1 min):**
Abrir o 3D Coat com a Trim Sheet de demonstração já pintada (três faixas: madeira, metal, ornamento) e o asset de parede modular de referência, ainda com UV individual, carregado ao lado.

**Percurso da demonstração:**

**Passo 1 — Apresentação da trim já pronta (4 min):**
1. Mostrar a Trim Sheet completa (ex.: 1024×2048) e apontar as três faixas: *"Esta faixa de madeira serve para qualquer parede de madeira do kit, não importa o comprimento. Esta faixa de metal serve para reforços e dobradiças. Esta última é puramente ornamental, para bordas e detalhes de acabamento."*
2. Destacar que as bordas de cada faixa foram desenhadas para se encontrarem sem descontinuidade — mostrar a faixa duplicada lado a lado no Krita ou em um preview de tiling para provar que a costura é invisível.

**Passo 2 — Mapeamento do UV da parede na trim (8 min):**
1. No Blender (ou no UV Room do 3D Coat), abrir o UV do asset de parede — ainda com seu UV individual da fase anterior.
2. Remapear o UV para ocupar uma tira estreita sobre a faixa de madeira da trim, com o eixo do comprimento da parede alinhado ao eixo de tiling da faixa.
3. Configurar a repetição (tiling) do UV ao longo do comprimento da parede — mostrar como aumentar o número de repetições do UV faz o padrão se repetir mais vezes sem perda de nitidez.
4. Aplicar o material com a trim carregada e mostrar o resultado no viewport: a parede exibindo o padrão de madeira repetido de forma contínua.

**Passo 3 — Validação do tiling (4 min):**
1. Rotacionar e afastar a câmera do viewport para verificar se há costura visível nas junções do padrão repetido.
2. Verificar a escala: o padrão de madeira parece do mesmo tamanho em toda a extensão da parede, ou distorce em algum trecho?
3. *"Validar tiling é como validar uma textura seamless da Semana 6 — só que agora em uma dimensão só, ao longo do comprimento da peça, não nas quatro bordas de uma textura quadrada."*

**Passo 4 — Reaplicação em uma segunda variação (3 min):**
1. Mostrar rapidamente a mesma trim aplicada a uma segunda peça modular de tamanho diferente (uma parede mais curta ou uma viga) sem precisar pintar nada novo.
2. *"Essa é a prova concreta de otimização: a mesma textura, sem nenhuma pintura adicional, serve a duas peças de tamanhos diferentes do kit."*

> **Nota do professor:** Se o tempo apertar, é aceitável mostrar a trim de demonstração já mapeada em ambas as peças de antemão, dedicando o tempo restante a explicar o processo de mapeamento em vez de executá-lo do zero ao vivo. O ponto central é a lógica de tiling e reutilização, não a velocidade de execução.

---

### Produção em Estúdio — 50 minutos

**Planejamento e criação da Trim Sheet do próprio kit**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com dois objetivos: primeiro, planejar as faixas da trim sheet do seu kit — que tipos de detalhe modular se repetem no seu tema e merecem uma faixa própria. Segundo, começar a pintar ou construir a primeira faixa no 3D Coat ou no Krita. Vocês não precisam terminar a trim inteira hoje — o objetivo do primeiro encontro é ter o planejamento definido e a primeira faixa iniciada."*

**Atividade estruturada:**

**Etapa 1 — Planejamento das faixas (≈10 min):**
1. Revisar os assets arquitetônicos modulares do próprio kit (paredes, vigas, molduras, trilhos) e identificar quais se repetem com frequência na composição do ambiente.
2. Definir de 2 a 4 faixas para a trim, cada uma associada a um tipo de detalhe (estrutural, junção/reforço, ornamental), coerentes com o tema e a paleta já estabelecidos desde a Semana 1.
3. Escrever uma justificativa breve (2–3 frases) sobre por que essas faixas foram escolhidas — esse registro alimenta C1 (Processo) e C7 (Otimização).

**Etapa 2 — Criação da primeira faixa (≈30 min):**
1. Criar a imagem de destino da trim (ex.: 1024×2048 ou proporção equivalente, coerente com a resolução de trabalho do kit).
2. Pintar ou construir a primeira faixa (a de maior uso — geralmente o material estrutural dominante) no 3D Coat ou Krita, garantindo que as bordas se encontrem sem descontinuidade quando repetidas.
3. Testar o tiling da faixa isoladamente antes de avançar: duplicar a faixa lado a lado em um preview e verificar a costura.

**Etapa 3 — Registro de processo (≈10 min):**
1. Salvar o arquivo: `[Nome]_TrimSheet_S14.blend` / projeto 3D Coat correspondente.
2. Screenshot da trim em construção com preview de tiling da primeira faixa, para levar à Crítica Formal do segundo encontro.

**Papel do professor:**

Circular verificando:

- **A escolha das faixas reflete elementos que realmente se repetem no kit, ou faixas genéricas sem relação com os assets modulares do estudante?** Perguntar: "Que peça do seu kit você vai construir com essa faixa, especificamente?"
- **A faixa está sendo desenhada pensando em repetição desde o início, ou o estudante está pintando como se fosse uma textura única?** Erro comum vindo diretamente da Semana 13 — tratar a trim como um atlas.
- **As bordas da faixa se encontram sem costura visível no teste de tiling?** Verificar com o preview de repetição lado a lado, não apenas visualmente na textura isolada.

Perguntas de mediação circulante:
- *"Se essa faixa tivesse que servir a uma parede duas vezes mais longa do que a peça que você está pensando agora, ela ainda funcionaria sem parecer repetitiva ou quebrada?"*
- *"Compare com o atlas da semana passada: por que essa faixa não caberia como um objeto fixo no atlas? O que ela precisa fazer que o atlas não faz?"*

---

## ENCONTRO 2 (1h30)

### Crítica Formal (CF5) — 20 minutos

**Formato: Apresentação individual estruturada**

Esta é uma crítica 🔴 **FORMAL**, com apresentação individual, preenchimento da Ficha de Crítica Formal (Instrumento 1) comparada à autoavaliação do estudante (Instrumento 2), e nota que compõe 30% do PA — o maior peso entre as críticas formais realizadas até agora.

**Protocolo:**

**Preparação (antes do início):**
- Confirmar que todos trouxeram a Ficha de Autoavaliação preenchida.
- Ordem de apresentação definida previamente e visível para a turma.
- Cada estudante prepara: Trim Sheet aberta com preview de tiling, asset(s) modular(es) mapeado(s) e aplicados no viewport, e — se possível — comparação lado a lado com o Texture Atlas da Semana 13.

**Abertura (1 min):**
*"Cada apresentação tem cerca de 2 minutos: mostrem a trim sheet, o asset modular mapeado nela e, se tiver mais de uma peça usando a mesma trim, mostrem as duas. Expliquem a diferença de propósito entre o atlas da semana passada e a trim de hoje, no contexto do próprio kit. Depois, uma pergunta rápida da turma ou minha."*

**Apresentações (≈16 min para a turma, ajustar tempo por estudante conforme o tamanho da turma):**

Roteiro sugerido para cada estudante (⏱ ~2 min):
1. Mostrar a Trim Sheet: faixas escolhidas e por quê.
2. Mostrar o asset modular mapeado na trim, com tiling validado (sem costura visível).
3. Se aplicável, mostrar uma segunda peça reaproveitando a mesma trim, sem textura nova.
4. Uma frase de autoavaliação: *"O que eu acho que está no nível mais alto no meu trabalho esta semana é [X], e o que eu sei que ainda precisa de trabalho é [Y]."*
5. Uma pergunta do professor ou de um colega, registrada como parte de C10 do colega que perguntou.

O professor preenche a Ficha de Crítica Formal (Instrumento 1) para C1, C2, C5, C6, C7 e C9 durante cada apresentação, comparando mentalmente com a autoavaliação entregue. C4 é apenas observado (obs.) nesta CF. Diferenças relevantes entre a autopercepção do estudante e a avaliação do professor são material valioso para o feedback escrito.

**Síntese coletiva (3 min):**
*"A maioria de vocês conseguiu mostrar reutilização real — a mesma trim servindo a mais de uma peça. Onde eu vi mais dificuldade foi na costura do tiling, o que é esperado numa primeira trim sheet. É exatamente isso que vamos resolver no estúdio de hoje."*

> **Nota sobre o feedback escrito:** A Ficha de Crítica Formal exige um "ponto mais forte" e uma "prioridade de melhoria" por estudante. Preencher esses campos imediatamente após cada apresentação, enquanto o contexto está fresco.

---

### Produção em Estúdio — 60 minutos

**Correção de tiling, expansão da trim e aplicação em mais assets**

**Consigna:**

> *"Sessenta minutos com foco na prioridade de melhoria recebida na crítica formal de hoje. Se o problema foi costura visível no tiling, corrijam as bordas da faixa. Se a trim já está sólida, expandam para uma segunda ou terceira faixa, ou apliquem a trim existente em mais uma peça modular do kit."*

**Atividade estruturada:**

**Bloco 1 — Correção de costura de tiling identificada na CF5 (≈20 min):**

Para estudantes com problemas de costura apontados na apresentação:
1. Reabrir a faixa problemática no Krita ou 3D Coat e ajustar as bordas para que padrão e cor se encontrem sem descontinuidade (offset + patch, mesma técnica da Semana 6, aplicada apenas ao eixo de repetição).
2. Testar novamente com o preview de tiling lado a lado antes de reaplicar ao asset.
3. Reaplicar a faixa corrigida ao material do asset e validar no viewport, rotacionando a câmera.

**Bloco 2 — Expansão da Trim Sheet (≈20 min):**

Para estudantes com a primeira faixa já validada:
1. Criar uma segunda faixa (ex.: metal com rebites, ou detalhe ornamental) seguindo o mesmo cuidado de bordas sem costura.
2. Mapear um segundo asset modular do kit (viga, moldura, trilho) nessa nova faixa.
3. Se possível, integrar Normal Map de bake (Semanas 11–12) à faixa, reforçando profundidade de entalhe ou talha ao longo do tiling.

**Bloco 3 — Aplicação em mais variações, se houver tempo (≈15 min):**

Para estudantes com trim sólida e já expandida:
1. Aplicar a trim existente a uma terceira peça modular de tamanho ou proporção diferente, sem criar textura nova.
2. Calcular e registrar: quantas peças do kit agora compartilham essa única trim sheet, e quantas texturas únicas seriam necessárias sem ela.

**Bloco 4 — Exportação e registro final (≈5 min):**
1. Exportar a Trim Sheet final (`.png`, resolução definida no planejamento).
2. Salvar arquivo Blender/3D Coat com sufixo `_TrimSheet_S14_Final`.
3. Render comparativo: as peças modulares mapeadas com a trim, lado a lado, demonstrando reutilização sem perda de qualidade visual.

**Papel do professor:**

- Para estudantes que corrigiram a costura rapidamente: direcionar para o Bloco 2 ou 3 em vez de deixá-los ociosos.
- Para estudantes com dificuldade persistente de tiling: verificar primeiro se o problema é de textura (bordas mal casadas) ou de UV (repetição mal configurada) antes de insistir na repintura.
- Perguntas de mediação: *"Quantas texturas separadas essas peças do seu kit exigiriam se você não tivesse feito essa trim? Essa conta já é evidência concreta de C7 para o seu portfólio."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese da CF5)**
*"Hoje foi a quinta crítica formal do semestre e a primeira que avaliou Otimização como nota. Entre o atlas da semana passada e a trim de hoje, vocês agora têm duas ferramentas complementares de otimização — uma para agrupar objetos distintos, outra para reutilizar padrões repetitivos. Um kit modular de produção real usa as duas ao mesmo tempo, escolhendo a ferramenta certa para cada tipo de asset."*

2. **(3 min — Reflexão de trade-off)**
Pergunta aberta: *"Existe algum elemento do seu kit que você hesitou entre colocar no atlas da semana passada ou numa faixa da trim de hoje? O que te fez decidir de um jeito ou de outro?"*
Deixar 2–3 respostas. O objetivo é consolidar que a escolha entre atlas e trim é uma decisão técnica com critério, não uma questão de preferência.

3. **(2 min — Antecipação da Semana 15)**
*"Semana que vem: UDIMs e otimização de compressão, mipmaps e channel packing — o fechamento da Unidade IV antes de irmos para a integração na Unity. Antes de chegar: pensem em qual dos mapas PBR dos seus assets (roughness, metallic, AO) poderia ser combinado em um único mapa de canais para economizar memória."*

4. **(2 min — Confirmação das entregas e devolução da nota)**
Informar prazo para devolução da Ficha de Crítica Formal preenchida (feedback escrito) e recapitular nomenclatura de entrega.

---

## Possíveis Dificuldades

**1. Confundir Trim Sheet com Texture Atlas — UV mapeado sem tiling**
O erro mais recorrente vindo diretamente da Semana 13: o estudante mapeia o UV do asset modular uma única vez sobre a faixa, sem configurar repetição, perdendo toda a vantagem de reutilização da trim. Estratégia: pedir para o estudante explicar em voz alta o que aconteceria se a peça precisasse ser duas vezes mais longa — se a resposta envolver "eu precisaria redesenhar a textura", o UV não está configurado como trim.

**2. Costura visível no tiling (seam de repetição)**
Bordas da faixa que não se encontram sem descontinuidade produzem uma linha ou mudança de tom visível a cada repetição do padrão. Estratégia: aplicar a mesma técnica de offset e patch de bordas da Semana 6, mas restrita ao eixo de tiling da faixa (geralmente apenas horizontal ou apenas vertical, não nos quatro lados como uma textura seamless completa).

**3. Faixas planejadas sem relação com os assets reais do kit**
Alguns estudantes criam faixas "genéricas" (madeira, metal, pedra) sem verificar se o kit realmente possui peças modulares que se beneficiariam de cada uma. Estratégia: exigir que cada faixa planejada seja associada a uma peça específica e nomeada do kit antes de começar a pintar — se o estudante não conseguir nomear a peça, a faixa provavelmente não é prioritária ainda.

**4. Distorção de escala do padrão ao longo de peças de tamanhos diferentes**
Quando a mesma trim é aplicada a peças de comprimentos muito diferentes sem recalibrar o número de repetições do UV, o padrão pode parecer esticado numa peça e comprimido demais em outra. Estratégia: ensinar o estudante a ajustar o número de repetições (tiling count) proporcionalmente ao comprimento de cada peça, mantendo o tamanho do "motivo" visual constante, exatamente como se calibra texel density entre assets desde a Semana 4.

**5. Tempo insuficiente para produzir mais de uma faixa até a Crítica Formal**
Planejar múltiplas faixas é rápido; pintar cada uma com qualidade e testar tiling consome tempo. Estratégia: reforçar na consigna do primeiro encontro que apenas a primeira faixa (a de maior uso) precisa estar pronta e validada para a CF5 — as demais podem ser produzidas no Bloco 2 do segundo encontro, após o feedback formal.

**6. Ansiedade de apresentação elevada por ser a CF de maior peso até agora**
Sabendo que a CF5 vale 30% do PA — o maior peso das cinco — alguns estudantes podem chegar mais tensos que nas críticas anteriores. Estratégia: abrir a crítica reforçando que o peso maior reflete confiança no progresso já demonstrado nas CFs anteriores, não uma régua mais rígida, e que o objetivo continua sendo registrar o estado atual do processo, não julgar um resultado fechado.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe quais faixas a trim deveria ter | Pedir que aponte, no kit já construído, os três elementos arquitetônicos que mais se repetem na composição da cena. A resposta geralmente revela as faixas prioritárias sem necessidade de instrução técnica adicional. |
| Estudante mapeou o UV sem tiling, tratando a trim como um atlas | Perguntar diretamente: "Se essa parede precisasse ser o dobro do tamanho amanhã, o que você faria com essa textura?" Se a resposta envolver redesenhar, reforçar a diferença de propósito entre as duas ferramentas antes de seguir adiante. |
| Estudante com costura visível no tiling e frustrado após tentativas | Isolar o problema em uma faixa de teste simplificada (apenas cor sólida com uma borda colorida diferente) para que o estudante veja claramente onde a borda não casa, antes de voltar à faixa real com o problema mais sutil. |
| Estudante inseguro sobre a diferença entre atlas (S13) e trim (S14) na hora de apresentar | Sugerir uma frase-ponte: "Uso o atlas quando tenho um número fixo de objetos diferentes para agrupar; uso a trim quando tenho um elemento que se repete em quantidade que eu não sei de antemão." Praticar essa frase antes da apresentação reduz a insegurança verbal. |
| Estudante terminando rápido e com qualidade | Propor expandir para uma segunda ou terceira faixa, ou aplicar a trim existente a uma variação de asset ainda não testada — e calcular a economia total de texturas do kit até aqui, acumulando evidência concreta de C7 para a reta final do semestre. |
| Estudante questionando se vale a pena usar trim em um elemento que aparece poucas vezes no kit | Validar a pergunta como legítima — trim sheets compensam mais quanto maior a repetição do elemento. Propor que o estudante registre esse critério por escrito: a partir de quantas repetições a trim se justifica em vez de uma textura única. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Trim Sheet com ao menos uma faixa validada, sem costura visível de tiling | C7 — Otimização | O padrão se repete sem linha ou mudança de tom perceptível na junção? |
| Justificativa escrita da escolha das faixas, associada a peças específicas e nomeadas do kit | C1 — Processo de Projeto / C7 — Otimização | A justificativa referencia elementos reais do kit que se repetem, ou é genérica? |
| UV de ao menos um asset modular mapeado com tiling configurado sobre a trim, escala consistente ao longo do comprimento da peça | C7 — Otimização | O número de repetições foi calibrado proporcionalmente ao tamanho da peça, evitando distorção? |
| Reaplicação da mesma trim em uma segunda variação de asset, sem textura nova | C7 — Otimização | Há prova concreta de reutilização — a mesma textura servindo a mais de uma peça? |
| Coerência visual da trim com a paleta e linguagem já estabelecidas no kit desde a Semana 1 | C2 — Direção Artística | A faixa dialoga com os materiais já produzidos, ou introduz um estilo dissonante? |
| Integração de bake (Normal Map) à trim, reforçando profundidade de entalhe/talha ao longo do tiling, quando aplicável | C6 — Bake | O bake se comporta corretamente ao ser repetido, sem artefato na costura? |
| Apresentação individual na CF5: clareza da fala, capacidade de diferenciar verbalmente atlas (S13) de trim (S14), organização dos arquivos exibidos | C9 — Apresentação | O estudante consegue explicar por que escolheu trim em vez de atlas para aquele elemento específico? |
| Ficha de Autoavaliação preenchida com evidência específica por critério, entregue antes da apresentação | C1 — Processo de Projeto | A autoavaliação aponta evidência concreta, ou é genérica? |
| Feedback dado a colegas durante a Crítica Formal com observação técnica específica | C10 — Participação (obs.) | O comentário referencia critério técnico observável (tiling, escolha de faixa, reutilização), ou é genérico? |

---

## Entrega da Semana 14

| Entrega | Formato | Prazo |
|---|---|---|
| Trim Sheet finalizada (ao menos uma faixa validada, idealmente mais de uma) | `.png`, resolução definida no planejamento (ex.: 1024×2048), pasta `_TrimSheet_S14` | Até o fim do segundo encontro |
| Arquivo Blender/3D Coat com ao menos um asset modular mapeado na trim, com tiling configurado | `.blend`/projeto com sufixo `_TrimSheet_S14_Final` | Até o fim do segundo encontro |
| Justificativa escrita da escolha das faixas e das peças associadas | Documento digital ou anotação junto ao arquivo de entrega | Até o fim do segundo encontro |
| Render comparativo: peças modulares mapeadas com a trim, demonstrando reutilização | `.png` com sufixo `_Comparativo_TrimSheet_S14` | Até o fim do segundo encontro |
| Ficha de Autoavaliação (Instrumento 2) preenchida | Documento digital ou impresso, entregue antes da apresentação | Início do segundo encontro |
| Ficha de Crítica Formal (Instrumento 1), preenchida pelo professor | Devolução com feedback escrito | Conforme cronograma de devolução da disciplina |

> **Nota sobre a nota da CF5:** A nota atribuída nesta semana corresponde a 30% do Portfolio de Artefatos (PA), o maior peso entre as cinco críticas formais realizadas até agora. O feedback escrito deve destacar claramente o ponto mais forte e a prioridade de melhoria de cada estudante, servindo de guia direto para as Semanas 15 e 16, que fecham a Unidade IV antes da apresentação final na Semana 17.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 14 | 2026*
