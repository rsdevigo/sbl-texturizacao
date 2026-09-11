---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 16"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Apresentação e defesa do Projeto Final

## Kit Modular de Ambiente e fase caminhável na Unity

**Semana 16** — CF5 / Projeto Final, 40% da nota final

<!--
Notas: Unidade V — Projeto Final e Apresentação. Crítica 🔴 FORMAL — CF5 / Projeto Final (PF) — todos os 10 critérios da rubrica avaliados com nota simultaneamente pela primeira e única vez no semestre. Apostila: Parte VI, Cap. 24 — Apresentação Profissional de Assets (breakdown visual, portfólio, padrão ArtStation), disponibilizada ao final da Semana 15. Não há conteúdo técnico novo nesta semana: é o encerramento do projeto integrador. Os estudantes chegam com o Kit Modular completo — UV1 validado (S2–4), materiais PBR (S5–8), texturização e bake (S9–12), otimização em atlas/trim (S14) e a fase caminhável montada na Unity com materiais ORM e lightmap baked (S15). A defesa de hoje é o primeiro momento formal em que C8 (Integração na Unity) recebe nota. Autoavaliação (Instrumento 2) já entregue antes da aula, cobrindo os 10 critérios.
-->

---

<!-- _class: objectives -->

## Objetivos de hoje

Ao final da semana você será capaz de:

- **Apresentar** oralmente o Kit Modular completo em formato estruturado (10 min de apresentação + 5 min de perguntas)
- **Justificar** tecnicamente as decisões do semestre — UV, materiais, textura, bake, otimização e integração na Unity
- **Comparar** a própria autoavaliação com o feedback recebido na defesa
- **Oferecer** feedback específico aos colegas, referenciando critérios da rubrica
- **Refletir** sobre a trajetória de aprendizagem desde a Semana 1
- **Entregar** a documentação final organizada: Kit Modular, cena Unity, renders e autoavaliação

<!--
Notas: Os seis objetivos vêm direto do plano de aula (itens 1 a 6). Reforçar: nada aqui é técnica nova — é a integração e a comunicação oral de tudo o que já foi produzido. O objetivo 6 (entrega organizada) já é, em si, evidência de C9.
-->

---

<!-- _class: question -->

# Se vocês tivessem só 10 minutos para convencer alguém de que esse kit modular é bom, o que mostrariam primeiro?

<!--
Notas: Pergunta de abertura da mini aula (do plano de aula). Deixar 2–3 respostas da turma. Usar as respostas para introduzir a ideia central: uma boa defesa não é mostrar tudo — é uma curadoria do próprio processo. Depois de 16 semanas produzindo, hoje e no próximo encontro os estudantes vão contar a história desse projeto para quem não acompanhou o processo de perto.
-->

---

## Nota de transição: o encerramento do projeto integrador

Todas as 15 semanas anteriores produziram **peças isoladas** de um mesmo projeto — UV, material, textura, bake, otimização, integração no motor.

- A Semana 16 **não ensina nada tecnicamente novo**
- Ela pede que você monte essas peças em uma **narrativa coerente**
- E as **defenda oralmente** diante da turma e do professor

<div class="tip">

É, ao mesmo tempo, o encerramento pedagógico da disciplina e a avaliação de maior peso do semestre — CF5, 40% da nota final.

</div>

<!--
Notas: Nota de transição do plano de aula, citada quase literalmente. Fundamental para reduzir ansiedade: nenhuma novidade técnica hoje, apenas a integração e a comunicação do que já existe.
-->

---

## O que chega pronto hoje

O Kit Modular de Ambiente completo, produzido ao longo de 15 semanas:

- **UV1 validado** (Semanas 2–4)
- **Materiais PBR completos** (Semanas 5–8)
- **Texturização artística** com detalhe pintado e bake integrado (Semanas 9–12)
- **Otimização consolidada** em atlas/trim (Semana 14)
- **Fase caminhável completa**, montada na Unity, com materiais ORM otimizados e **lightmap baked** (Semana 15)

<div class="best">

Nenhuma entrega técnica nova a produzir esta semana. A fase caminhável e o kit inteiro já existem — hoje é sobre apresentá-los.

</div>

<!--
Notas: Pré-requisito da semana, listado no plano. Reforçar a ligação direta com a Semana 15: é lá que a fase caminhável foi montada na Unity com lightmap baked — é esse mesmo material que sobe ao "palco" hoje. Também chegam prontos: autoavaliação (Instrumento 2), documento de processo acumulado (moodboard, versões, anotações, checklists — Instrumento 4) e a leitura do Cap. 24 sobre apresentação profissional de assets.
-->

---

<!-- _class: chapter -->

## CF5 — Projeto Final

### Todos os 10 critérios, uma única vez

<!--
Notas: Slide de transição de capítulo antes da tabela de pesos. Hoje, pela primeira vez, todos os 10 critérios da rubrica recebem nota formal simultaneamente, incluindo C10 (Participação nas Critiques), que nas CFs anteriores era apenas observado.
-->

---

## A tabela de pesos do Projeto Final (CF5)

A ponderação segue a **Rubrica Mestre** — não é média simples, e não é a mesma ponderação do Portfolio de Artefatos (PA).

| Critério | Peso | Critério | Peso |
|---|---|---|---|
| C1 — Processo de Projeto | 10% | C6 — Bake | 8% |
| C2 — Direção Artística | 12% | C7 — Otimização | 8% |
| C3 — UV Mapping | 8% | C8 — Integração na Unity | 12% |
| C4 — Materiais PBR | 12% | C9 — Apresentação | 8% |
| **C5 — Texturização** | **14%** | C10 — Participação nas Critiques | 8% |

<!--
Notas: Tabela central da CF5, do plano de aula. C5 (Texturização) tem o maior peso — coerente com ser o núcleo da disciplina. Destacar que C8 (Integração na Unity) recebe nota formal pela primeira vez hoje, e que C10 também recebe nota formal pela primeira e única vez, consolidando o engajamento do estudante em todas as críticas do semestre. Vocês já foram avaliados nesses critérios separadamente ao longo do semestre — hoje é a primeira e única vez em que todos aparecem juntos.
-->

---

## Como a nota de hoje se conecta às notas anteriores

<div class="tip">

**NF = (PA × 0,40) + (CC × 0,20) + (PF × 0,40)**

</div>

- A nota de hoje corresponde ao componente **PF** (Projeto Final)
- **C10** avaliado hoje também alimenta o fechamento da nota de **CC** (Críticas Coletivas)
- Esta é a **última entrega avaliativa formal** da disciplina

<!--
Notas: Fórmula de referência do plano de aula. Importante deixar claro que a defesa de hoje tem peso duplo — compõe diretamente o PF (40% da nota final) e fecha o cômputo de CC (20% da nota final) através de C10.
-->

---

<!-- _class: timeline -->

## Os 10 minutos de apresentação

1. **Tema e referência visual** (1–2 min)
2. **Breakdown de processo** — o que mudou da primeira à última versão, com exemplo de feedback incorporado (2–3 min)
3. **Destaque técnico** — 2 ou 3 decisões técnicas de maior orgulho (UV, material, bake, otimização ou Unity) (3–4 min)
4. **A cena final na Unity**, com os renders (2 min)

<!--
Notas: Estrutura recomendada dos 10 minutos, do plano de aula — sugestão de sequência, não um roteiro rígido. Frase-chave: "Vocês não precisam explicar cada uma das 16 semanas. Escolham o que for mais representativo do trabalho de vocês — a apresentação é uma escolha editorial, não um relatório completo."
-->

---

## Os 5 minutos de perguntas: defesa, não interrogatório

As perguntas do professor e dos colegas têm o mesmo espírito das críticas já vividas no semestre: **entender a decisão**, não expor uma falha.

<div class="best">

"Não sei" seguido de uma tentativa de raciocínio vale mais, na avaliação de C10, do que silêncio ou defensividade.

</div>

<!--
Notas: Tópico 2 da mini aula. "As perguntas de hoje são as mesmas que vocês já responderam nas cinco críticas formais anteriores — só que agora sobre o projeto inteiro. Vocês já treinaram isso a cada duas ou três semanas desde a CF1." Aceitar "não sei, mas acho que..." como resposta válida e observável para C10.
-->

---

## Autoavaliação × avaliação do professor

<div class="columns">
<div class="col positive">

### Concordância
Autoavaliação e nota do professor apontam para o mesmo nível → confirma percepção madura do próprio processo.

</div>
<div class="col negative">

### Divergência
Não é punida — é **material de conversa** durante os 5 minutos de perguntas.

</div>
</div>

<div class="tip">

"Se vocês se avaliaram em 4 e eu observar um 3, isso vira uma pergunta: 'me mostra a evidência que te fez pensar em nível 4 aqui.'"

</div>

<!--
Notas: Tópico 4 da mini aula. A autoavaliação (Instrumento 2) já foi entregue antes da aula e será comparada com a avaliação do professor durante a defesa. É a mesma lógica de justificar decisões praticada desde a Semana 3. A autoavaliação em si já é evidência de C1, independentemente de bater exatamente com a nota final.
-->

---

<!-- _class: industry -->

## Demonstração: o padrão esperado

Não há demonstração técnica nova esta semana. Em vez disso, o professor apresenta um **Kit Modular de referência** — de uma coorte anterior ou preparado antecipadamente — como parâmetro de padrão esperado nível 4–5.

Percurso: moodboard e direção artística (C2) → UV, material, textura e bake (C3–C6) → cena montada na Unity e renders (C7–C8) → estrutura da própria apresentação (C9).

<!--
Notas: Demonstração de 20 min do plano de aula. "Este é um exemplo de projeto que atingiu nível 4–5 em praticamente todos os critérios da rubrica. Vou passar pelos mesmos pontos que vocês vão apresentar hoje." Se não houver kit de coorte anterior, usar kit de referência próprio ou prints de portfólio profissional (com créditos). Objetivo: calibrar expectativas de forma concreta, não intimidar com padrão inatingível.

[!FIGURA]
Objetivo didático: dar à turma um exemplo concreto de nível 4–5 em todos os critérios antes da própria defesa.
Descrição sugerida: montagem em grade do kit de referência do professor — moodboard, UV layout, material PBR, textura com desgaste, cena Unity final — não há imagem disponível nos assets desta semana; usar material próprio do professor no dia.
-->

---

<!-- _class: chapter -->

## Encontro 1

### Preparação final e primeiro bloco de defesas

<!--
Notas: Transição para o bloco de Produção em Estúdio do Encontro 1 (50 min).
-->

---

## Encontro 1 — Produção em Estúdio (50 min)

**Etapa 1 — Preparação final (≈15 min)**
- Teste de abertura do projeto Unity, `.blend` e renders na máquina da apresentação
- Revisão da autoavaliação e do roteiro (o que mostrar primeiro)
- Organização do material de apoio (documento de processo, breakdown visual)

**Etapa 2 — Primeiro bloco de defesas (≈35 min)**
- Cada estudante: 10 min de apresentação + 5 min de perguntas
- Professor preenche a Ficha de Crítica Formal (Instrumento 1) — 10 critérios
- Colegas preenchem a Ficha de Avaliação por Pares (Instrumento 3)

<!--
Notas: Atividade estruturada do Encontro 1. Cronômetro visível durante toda a etapa 2. Consigna verbal: "Os primeiros 15 minutos são para ajustes finais... Cada apresentação tem 10 minutos de fala mais 5 minutos de perguntas — o cronômetro vai estar visível para todos."
-->

---

<!-- _class: quote -->

## Perguntas de mediação da defesa

*"Você me mostrou o resultado final desse asset — me conta uma decisão que você tomou no meio do processo e depois mudou. O que te fez mudar?"*

*"Olhando sua autoavaliação, você se deu nível X em Materiais PBR. Me mostra a evidência que sustenta esse nível."*

*"Se você tivesse mais uma semana de produção, o que você priorizaria ajustar?"*

<!--
Notas: Papel do professor durante os 5 minutos de perguntas — priorizar perguntas que peçam justificativa técnica ("por que esse valor de roughness aqui?", "o que te fez escolher trim sheet nesse elemento e atlas nesse outro?") em vez de perguntas de sim/não. Manter o cronômetro visível e respeitado — parte da avaliação de C9 é a capacidade de organizar a fala dentro do tempo dado.
-->

---

<!-- _class: chapter -->

## Encontro 2

### Defesas finais e fechamento do semestre

<!--
Notas: Transição para o Encontro 2 (1h30) — Crítica Coletiva de 20 min (continuação das defesas) e Produção em Estúdio de 60 min.
-->

---

## Encontro 2 — continuação e consolidação

**Crítica Coletiva (20 min)** — continuação das defesas na mesma dinâmica: 10 min de apresentação + 5 de perguntas, mesmo rigor de cronômetro e ficha.

**Produção em Estúdio (60 min)**
- **Bloco 1** (≈45–50 min): apresentações restantes, mesmo formato do Encontro 1
- **Bloco 2** (≈10–15 min): confirmação da entrega final — Kit Modular, projeto Unity e autoavaliação — e recolhimento das fichas de avaliação por pares

<div class="warning">

Turma grande e tempo apertado: priorizar garantir os 15 minutos completos de cada estudante — é preferível reduzir discussão em outros momentos do que comprimir uma defesa individual.

</div>

<!--
Notas: Estrutura do Encontro 2. "Estamos na reta final das apresentações. Nos próximos 60 minutos, terminamos as defesas restantes e fechamos oficialmente o semestre." Perguntas de mediação recorrentes: "Esse é o mesmo asset que eu vi na Semana 3 com o UV recém-aberto. O que mudou entre aquela versão e essa?" e "Qual desses 10 critérios você sente que foi seu ponto mais forte no semestre? E qual foi o mais desafiador?"
-->

---

## Entrega da Semana 16

| Entrega | Formato | Prazo |
|---|---|---|
| Kit Modular completo (assets, `.blend`, mapas) | Pasta `[Nome]_Kit_Final` | Início da apresentação |
| Projeto Unity — cena, materiais, lightmap (S15) | Pasta `[Nome]_Kit_Unity_Final` | Início da apresentação |
| Renders finais, mínimo 4 ângulos | `.png`/`.jpg` em `_Renders_Final` | Início da apresentação |
| Autoavaliação reflexiva (Instrumento 2) | `.pdf` ou `.docx` | Antes da aula |
| Ficha de Avaliação por Pares | Física ou digital | Final de cada encontro |

<!--
Notas: Tabela de entregas do plano de aula. Preparação prévia: confirmar na Semana 15 (ou por comunicado) que cada estudante testou a abertura do próprio projeto Unity e da pasta de entrega — problemas técnicos de última hora não devem consumir tempo da defesa formal.
-->

---

## Possíveis dificuldades

<div class="warning">

**Ansiedade elevada** — é a avaliação de maior peso do semestre. Reforçar: nada é novo, são os mesmos critérios já praticados desde a CF1, agora juntos.

</div>

<div class="warning">

**Apresentações que estouram o tempo** — cronômetro visível; interromper com gentileza ao final dos 10 min, direcionando o resto para as perguntas.

</div>

<div class="warning">

**Problema técnico de última hora** — exigir teste prévio de abertura; ter plano B com renders/screenshots exportados.

</div>

<!--
Notas: Três das seis dificuldades do plano de aula, priorizadas por frequência esperada. As demais: divergência entre autoavaliação e nota do professor (tratar como diálogo técnico, não confronto); engajamento desigual dos colegas (a Ficha de Pares também compõe C10 de quem a preenche); tempo insuficiente em turmas maiores (planejar a ordem com antecedência a partir do número real de matriculados).
-->

---

## Estratégias de mediação

| Situação | Estratégia |
|---|---|
| Estudante ansioso antes de apresentar | Os critérios de hoje já são praticados desde a CF1 — só a integração é nova |
| Apresentação ultrapassando o tempo | Cronômetro como referência compartilhada, não surpresa |
| Divergência autoavaliação × professor | Pedir a evidência concreta, tratar como diálogo técnico |
| Problema técnico na abertura do projeto | Plano B com renders/screenshots já exportados |
| Atenção decrescente na turma | Ficha de Pares também compõe C10 de quem a preenche |
| Estudante sem resposta imediata | "Não sei, mas acho que..." é resposta válida para C10 |

<!--
Notas: Tabela de Estratégias de Mediação do plano de aula, para consulta rápida do professor durante as duas aulas de defesa.
-->

---

<!-- _class: question -->

# Pensando nas 16 semanas, qual foi a maior mudança na forma como vocês tomam decisões técnicas ou artísticas — do início ao fim do semestre?

<!--
Notas: Pergunta de reflexão semestral do Fechamento (3 min). 2–3 respostas voluntárias. Objetivo: consolidar a metacognição sobre o próprio processo de aprendizagem, não apenas sobre o produto entregue.
-->

---

## Fechamento das defesas e da participação

- Encerramos as defesas do Projeto Final — cada um contou a história de um semestre inteiro de decisões, da Semana 1 à cena montada na Unity na semana passada
- **C10 (Participação)** hoje também consolida o engajamento em todas as críticas anteriores do semestre — não só na defesa de hoje
- A **Ficha de Avaliação por Pares** preenchida hoje ainda será considerada

<!--
Notas: Roteiro do Fechamento (10 min) — itens 1 e 3. Encerramento institucional (item 4): informar prazos administrativos remanescentes (lançamento de notas, prazo de recurso, feedback escrito individual, se houver).
-->

---

<!-- _class: curiosity -->

## Sobre a Semana 17

A Semana 17 existe como semana de **Recuperação** — atendimento individual, sem crítica coletiva, para quem tiver entregas formais pendentes de qualquer semana do semestre.

<!--
Notas: Encerramento institucional do plano de aula. Não é uma nova defesa nem uma repetição da CF5 — é atendimento pontual para pendências específicas. Deixar claro que não altera o caráter de "última entrega avaliativa formal" da CF5 de hoje.
-->

---

<!-- _class: summary-slide -->

# Resumo

- Hoje é a **CF5 / Projeto Final** — todos os 10 critérios avaliados juntos, pela primeira vez
- Estrutura da apresentação: **10 min** (tema, breakdown, destaque técnico, cena Unity) + **5 min** de perguntas
- **C5 (Texturização)** tem o maior peso (14%); **C8 (Unity)** e **C10 (Participação)** recebem nota formal pela primeira vez
- Autoavaliação e avaliação do professor são **comparadas**, não confrontadas
- Fórmula: **NF = (PA × 0,40) + (CC × 0,20) + (PF × 0,40)**
- Última entrega avaliativa formal da disciplina

<!--
Notas: Amarrar a mini aula antes da demonstração e da defesa propriamente dita. Todos os pontos retornam ao longo dos dois encontros de defesa.
-->

---

<!-- _class: industry -->

## Fechamento do semestre

O portfólio produzido — Kit Modular completo, documentado e funcional na Unity — é, a partir de hoje, **material de portfólio profissional** do estudante.

<!--
Notas: Última fala do plano de aula (Encerramento institucional). Agradecer o semestre de trabalho e reforçar o valor profissional do que foi produzido, conectando com a leitura obrigatória da semana (Cap. 24 — Apresentação Profissional de Assets, padrão ArtStation).
-->
