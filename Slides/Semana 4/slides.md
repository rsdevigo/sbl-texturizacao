---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 04"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Texturização

## Do moodboard ao UV real

**Semana 4** — Abertura de UV do Hero Asset Referência — Smart UV Project e seams manuais

<!--
Notas: Abrir marcando a virada: até aqui (Semana 3) o Hero Asset era decisão e justificativa escrita. Hoje ele chega modelado, pela primeira vez, e a turma abre o UV dele de verdade. É também a primeira Crítica Formal do semestre — dizer isso já na abertura, sem alarmismo.
-->

---

## Onde vocês estão

Semana 2: primeiro contato técnico com UV, **sem tema**.

Semana 3: tema e Hero Asset Referência **definidos e justificados**.

Hoje: o Hero Asset chega modelado — e o UV dele vale nota.

<!--
Notas: Recapitular em uma frase cada semana, sem reabrir conteúdo técnico de projeção UV (Semana 2) nem a lógica dos três critérios de escolha (Semana 3) — isso já foi ensinado. Só situar o fluxo.
-->

---

<div class="objectives">

Ao final da semana você será capaz de:

- Explicar quando usar **Smart UV Project** e suas limitações
- Aplicar a **lógica de corte de seams** para reduzir distorção
- Abrir o UV completo do Hero Asset com islands organizadas
- Avaliar o próprio layout com **Stretch Overlay** e checkerboard
- Apresentar o UV na **primeira Crítica Formal** do semestre

</div>

<!--
Notas: Os três primeiros objetivos são cobertos na mini aula e na demonstração; os dois últimos são o trabalho do estúdio de hoje, fechado na Crítica Formal do Encontro 2.
-->

---

<!-- _class: question -->

# O Smart UV Project resolveria isso sozinho?

<!--
Notas: Deixar 2-3 respostas antes de nomear o conceito. A resposta certa é "depende" — ponte direta para a próxima seção.
-->

---

## Smart UV Project: quando usar

Analisa a geometria e corta automaticamente por ângulo de face.

Rápido, útil como **ponto de partida** ou para objetos secundários de baixa importância visual.

<!--
Notas: Não é uma ferramenta ruim — é uma ferramenta para um problema diferente do de hoje. O Hero Asset é a peça mais observada do semestre.
-->

---

<div class="error">

Cortes nem sempre ficam em posições esteticamente discretas.

</div>

<div class="error">

Distribuição de islands raramente é eficiente no espaço 0–1.

</div>

<div class="error">

Densidade de texel entre islands costuma ficar desigual.

</div>

<!--
Notas: Três limitações do Smart UV Project isoladamente. Para um Hero Asset, não é suficiente sozinho — precisa de seams manuais por cima.
-->

---

## Seams: lógica de corte

1. Cortar em arestas que **já escondem** a costura (cantos, junções)
2. Cortar o **suficiente** para reduzir distorção, sem fragmentar demais
3. Priorizar mudanças **reais** de superfície — não cortes arbitrários

<!--
Notas: Ligar ao critério 3 da Semana 3 (reaproveitamento) — um bom seam pensa também em onde a textura vai ser pintada depois.
-->

---

## Princípios de um bom layout UV

**Islands organizadas** — agrupadas por lógica de superfície.

**Padding consistente** — 4 a 8 px em textura de 1024px.

**Aproveitamento de espaço** — todo pixel não usado é resolução desperdiçada.

<!--
Notas: Reforçar que o critério técnico (Stretch Overlay, densidade de texel) já foi visto na Semana 2 em objetos neutros — a novidade de hoje é aplicar isso a uma peça real que vale nota.
-->

---

<div class="tip">

**Esse UV está sem sobreposição, com seams justificáveis, aproveitando o espaço?**

</div>

O padrão esperado hoje é o **Nível 3** da Rubrica Mestre — não o nível máximo.

<!--
Notas: Pergunta de checagem para repetir circulando no estúdio. Reforçar que a CF1 avalia domínio técnico do processo, não perfeição estética.
-->

---

<!-- _class: invert -->

## Na indústria

Um bom UV é **invisível** — ninguém nota o layout, só a textura final.

Um UV mal resolvido aparece semanas depois, quando é caro corrigir.

<!--
Notas: Amarrar ao C3 (UV Mapping) da Rubrica Mestre, foco principal da CF1 de hoje.
-->

---

<!-- _class: summary-slide -->

# Resumo

- **Smart UV Project** é ponto de partida, não solução final para o Hero Asset
- **Seams manuais** reduzem distorção e escondem costura
- Layout bom = **islands organizadas + padding + aproveitamento de espaço**
- Hoje é a **CF1** — primeira nota formal do semestre, foco em C3

<!--
Notas: Fechar a mini aula amarrando os conceitos antes da demonstração.
-->

---

## Agora: demonstração

Do Smart UV Project ao unwrap manual — comparação lado a lado.

Organização de islands com Average Islands Scale e Pack Islands.

![diagram](assets/uv_comparacao_smart_manual.webp)

<!--
Notas: Transição para os 20 min de demonstração.

[!FIGURA]
Objetivo didático — Mostrar visualmente a diferença de qualidade entre um UV resolvido só por Smart UV Project e o mesmo objeto com seams manuais, islands organizadas e Pack Islands aplicado.
Arquivo sugerido — assets/uv_comparacao_smart_manual.webp
Descrição — Duas capturas de tela lado a lado do mesmo prop no UV Editor do Blender: à esquerda, resultado do Smart UV Project (islands fragmentadas, aproveitamento mediano); à direita, resultado após seams manuais + Pack Islands (islands organizadas, aproveitamento alto), ambas com checkerboard aplicado no Viewport ao fundo.
Como produzir — Capturar no Blender com o prop de demonstração do professor, exportando as duas telas no mesmo enquadramento para comparação direta.
-->

---

<!-- _class: chapter -->

<span class="chapter-number">04</span>

# Produção em estúdio

Do Hero Asset modelado ao UV pronto para a Crítica Formal

<!--
Notas: Divisória entre a mini aula e o estúdio. Os slides a seguir ficam projetados durante a produção — servem de consigna e timebox visíveis, apresentados um a um conforme a etapa correspondente começa.
-->

---

<!-- _class: exercise -->

## Etapa 1 — Primeira leitura da geometria

**10 minutos.**

Importem o Hero Asset Referência recebido de Modelagem 3D e Level Design.

Apliquem Smart UV Project como primeira leitura — onde a malha é mais complexa?

<!--
Notas: Encontro 1. Circular perguntando onde a malha concentra mais complexidade de forma, antes de qualquer corte manual.
-->

---

<!-- _class: exercise -->

## Etapa 2 — Seams e unwrap manual

**25 minutos.**

Marquem seams nos pontos estratégicos (cantos, junções, mudanças reais de superfície).

Apliquem Unwrap e avaliem com o **Stretch Overlay**.

<!--
Notas: Perguntar: "Por que você cortou o seam aqui e não ali? Essa costura vai aparecer na peça final?" Identificar seams excessivamente fragmentados.
-->

---

<!-- _class: exercise -->

## Etapa 3 — Organização do layout

**15 minutos.**

Average Islands Scale + Pack Islands.

Checkerboard ativo — ajustem manualmente islands mal posicionadas ou sobrepostas.

<div class="warning">

Todo estudante deve sair do Encontro 1 com um UV pelo menos funcional.

</div>

<!--
Notas: O refinamento final acontece no início do Encontro 2, antes da Crítica Formal. Identificar quem ainda tem distorção não resolvida — atenção prioritária amanhã.
-->

---

<!-- _class: exercise -->

## Refinamento final — 30 minutos

Revisem o Stretch Overlay uma última vez.

Capturem o screenshot do UV com checkerboard — é a evidência da CF1.

Preencham a **Autoavaliação** antes de apresentar — não depois.

<!--
Notas: Abertura do Encontro 2. Verificar que todos têm a Ficha de Autoavaliação preenchida antes do início das apresentações.
-->

---

<!-- _class: exercise -->

## Crítica Formal 1 (CF1) — 50 minutos

Apresentem o UV: layout, checkerboard, lógica dos seams.

Leiam brevemente sua autoavaliação.

<div class="tip">

Padrão esperado: **Nível 3** da Rubrica Mestre no Critério C3.

</div>

<!--
Notas: Cerca de 3 min por estudante, ajustar ao tamanho da turma. Perguntas focadas em C3: "Essa distorção compromete a textura futura?", "Esse aproveitamento de espaço está adequado?" Ficha de Crítica Formal preenchida durante ou logo após cada apresentação.
-->

---

<!-- _class: exercise -->

## Antes de sair

Confirmem as três entregas de hoje:

- Hero Asset com **UV aberto** (`.blend`)
- **Screenshot** do UV layout com checkerboard
- **Autoavaliação** preenchida

<div class="warning">

Próxima Crítica Formal só na Semana 8 (CF2). A Semana 5 é de ajuste e abertura — sem nova cobrança de rubrica.

</div>

<!--
Notas: Fechamento (10 min): "O UV que vocês abriram hoje é o endereço onde toda textura, todo material e toda pintura das próximas semanas vai morar." Reflexão individual: "O feedback que mais me surpreendeu na CF1 foi ___. Na Semana 5, vou corrigir ___ primeiro." Ponte: na Semana 5 corrigem o UV com base no feedback e entram no Shader Editor pela primeira vez.
-->
