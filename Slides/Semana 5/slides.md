---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 05"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Texturização

## Do feedback da CF1 aos primeiros materiais PBR

**Semana 5** — Revisão de UV pós-CF1 e fundamentos de PBR (Principled BSDF)

<!--
Notas: Marcar a dupla função da semana: fechar a Unidade I (revisão de UV com base no feedback da CF1) e abrir a Unidade II (primeira aproximação a materiais PBR). Não há crítica formal hoje — deixar isso claro logo na abertura para calibrar a expectativa da turma.
-->

---

## Onde vocês estão

Semana 4: primeira Crítica Formal do semestre — UV do Hero Asset avaliado (CF1).

Hoje: incorporar o feedback da CF1 e dar o primeiro passo em materiais PBR.

Próxima crítica formal: só na **Semana 8** (CF2).

<!--
Notas: Recapitular em uma frase, sem reabrir o conteúdo técnico de seams/unwrap da Semana 4 — isso já foi ensinado. Só situar o fluxo e a ausência de nota formal hoje.
-->

---

<div class="objectives">

Ao final da semana você será capaz de:

- Corrigir distorção e aproveitamento de espaço UV com base no feedback da CF1
- Explicar o que é PBR e por que o modelo Metallic/Roughness é o padrão em jogos
- Descrever a função de Albedo, Metallic e Roughness no Principled BSDF
- Atribuir valores fisicamente plausíveis de Metallic e Roughness a materiais reais
- Criar materiais PBR de teste e aplicar um deles ao Hero Asset Referência

</div>

<!--
Notas: Os dois primeiros objetivos fecham a Unidade I (revisão técnica de UV); os três últimos abrem a Unidade II (PBR) e são o foco do restante do semestre.
-->

---

## Fechando o UV: revisão rápida

**Stretch Overlay** — azul = compressão, vermelho = esticamento. Meta: verde/azul-claro predominante.

**Texel density** — todas as islands do mesmo objeto devem ter densidade equivalente (Average Islands Scale resolve a maior parte dos casos).

**Pack Islands** — aproveitamento do espaço 0–1, padding consistente entre islands.

<!--
Notas: "Vocês já viram tudo isso na Semana 4. Hoje não é aula nova de UV — é a correção do que a crítica formal apontou. Abram o feedback que receberam e localizem, no próprio arquivo, onde está o problema." Revisão rápida (~8 min), não uma aula nova.
-->

---

<!-- _class: question -->

# Como um material "sabe" que é metal?

<!--
Notas: Deixar 2-3 respostas antes de nomear o conceito. Respostas típicas: "não sabe, o artista pinta assim" — é exatamente a ponte para o problema que o PBR resolve.
-->

---

## Antes do PBR: pintar a luz na textura

Artistas pintavam highlights, sombras e reflexos direto na textura difusa.

Funcionava com câmera e iluminação fixas — quebrava em qualquer outro ângulo ou luz.

<!--
Notas: Perguntar: "Antes do PBR, como os artistas faziam um material brilhante parecer brilhante em qualquer luz?" Aguardar 2-3 respostas antes de revelar o problema.
-->

---

<div class="tip">

O PBR transfere a responsabilidade da aparência do artista para a física.

</div>

O artista define **o que o material é**. O motor calcula **como ele parece** em qualquer luz.

<!--
Notas: Esse é o ponto central da mini aula — reforçar antes de entrar nos dois workflows.
-->

---

## Dois workflows PBR

**Specular/Glossiness** — mais antigo, controle direto do reflectance.

**Metallic/Roughness** — Unity, Unreal, Blender, 3D Coat. Mais simples de calibrar.

Nesta disciplina, o workflow é **exclusivamente Metallic/Roughness**.

<!--
Notas: Não aprofundar Specular/Glossiness — é só contexto histórico. O que importa é fixar que todo o pipeline da disciplina (até a Unity) usa Metallic/Roughness.
-->

---

## Albedo (Base Color)

A cor pura do material — sem sombra, sem luz, sem reflexo.

<div class="error">

Erro comum: Albedo com highlight pintado, ou valores extremos (preto puro, branco puro).

</div>

<!--
Notas: Analogia útil: "Albedo é como você fotografaria o material num dia nublado, com luz difusa e neutra."
-->

---

## Metallic — binário na natureza

**0** = dielétrico (plástico, pedra, madeira, tecido, pele)

**1** = condutor (aço, ouro, cobre, alumínio)

<div class="warning">

Não existe "meio metal". Metallic 0.5 é o erro mais comum da primeira semana de PBR.

</div>

<!--
Notas: Perguntar: "Você já viu um material assim na vida real? Se não, não deve existir no jogo." Identificar esse erro é prioridade na circulação de hoje.
-->

---

## Roughness — o canal contínuo

**0** = espelho perfeito (reflexo nítido)

**1** = fosco total (luz difusa, sem reflexo direcional)

É o canal onde o artista tem mais liberdade criativa dentro do PBR.

<!--
Notas: Escrever no quadro durante toda a aula: "Roughness 0 = espelho | Roughness 1 = fosco" — âncora para quem confunde Roughness com Glossiness (lógica invertida).
-->

---

## Calibrando com referências reais

| Material | Metallic | Roughness |
|---|---|---|
| Metal polido | 1 | 0.05–0.15 |
| Metal fosco | 1 | 0.4–0.6 |
| Plástico brilhante | 0 | 0.1–0.3 |
| Pedra calcária | 0 | 0.7–0.9 |
| Madeira natural | 0 | 0.6–0.8 |

<!--
Notas: Mostrar as 5 referências e pedir que a turma estime os valores antes de revelar. O exercício de estimativa importa mais que os valores exatos — evitar memorização mecânica.
-->

---

<!-- _class: invert -->

## Na indústria

Um material PBR bem calibrado responde certo à luz em **qualquer** cenário, sem ajuste manual.

Um valor "no meio" (Metallic 0.5) nunca corresponde a um material real.

<!--
Notas: Amarrar ao C4 (Materiais PBR) da Rubrica Mestre, observado (não formal) nesta semana.
-->

---

<!-- _class: summary-slide -->

# Resumo

- **PBR** simula fisicamente como a luz responde à superfície — não é estilo, é física
- **Metallic** é binário: 0 (dielétrico) ou 1 (condutor) — nunca "no meio"
- **Roughness** é contínuo: 0 (espelho) a 1 (fosco total)
- Hoje é **observação**, não crítica formal — a CF2 é só na Semana 8

<!--
Notas: Fechar a mini aula amarrando os conceitos antes da demonstração.
-->

---

## Agora: demonstração

Correção ao vivo de um UV com distorção residual — antes/depois.

Quatro materiais PBR no Principled BSDF: metal polido, plástico, pedra, madeira.

![diagram](assets/pbr_quatro_materiais.webp)

<!--
Notas: Transição para os 20 min de demonstração.

[!FIGURA]
Objetivo didático — Mostrar os quatro materiais de referência (metal polido, plástico brilhante, pedra áspera, madeira) lado a lado no Viewport renderizado, com a mesma HDRI neutra, evidenciando como Metallic e Roughness sozinhos definem a resposta à luz.
Arquivo sugerido — assets/pbr_quatro_materiais.webp
Descrição — Render do Viewport do Blender em modo Rendered, quatro esferas ou cubos lado a lado, cada um com um dos materiais de referência aplicado (metal polido, plástico brilhante, pedra áspera, madeira), sob a mesma HDRI de estúdio neutra.
Como produzir — Capturar no Blender usando o arquivo de demonstração do professor (4 objetos, HDRI neutra tipo studio_small_09), um único enquadramento com os quatro objetos visíveis.
-->

---

<!-- _class: chapter -->

<span class="chapter-number">05</span>

# Produção em estúdio

Do feedback da CF1 aos primeiros materiais PBR do tema

<!--
Notas: Divisória entre a mini aula e o estúdio. Os slides a seguir ficam projetados durante a produção — servem de consigna e timebox visíveis, apresentados um a um conforme a etapa correspondente começa.
-->

---

<!-- _class: exercise -->

## Etapa 1 — Revisão do UV com feedback da CF1

**20 minutos.**

Reabram o Hero Asset Referência com o feedback escrito da CF1 em mãos.

Reativem o Stretch Overlay e corrijam as islands apontadas com Average Islands Scale / Pack Islands.

<!--
Notas: Encontro 1. Circular perguntando: "O que a CF1 apontou como problema nesse UV? Mostra onde você corrigiu." Salvar como [Nome]_HeroAsset_UV_Semana05.blend.
-->

---

<!-- _class: exercise -->

## Etapa 2 — Materiais PBR de teste

**25 minutos.**

Criem de 2 a 4 materiais no Principled BSDF (Albedo, Metallic, Roughness), nomeados pelo material real.

Apliquem um deles, com valores planos, ao Hero Asset Referência.

<div class="warning">

Pergunta-guia: esse material é condutor ou dielétrico? Metallic é 0 ou 1 — nunca 0.5.

</div>

<!--
Notas: Circular com foco duplo: UV corrigido e plausibilidade física. Identificar quem usa Metallic 0.5 como padrão — corrigir individualmente.
-->

---

<!-- _class: exercise -->

## Etapa 3 — Registro

**5 minutos.**

Screenshot do UV revisado e do Viewport com os materiais de teste.

Salvem: `[Nome]_MateriaisPBR_Semana05.blend`.

<!--
Notas: Fechamento do Encontro 1. Garantir que todos saem com os dois arquivos salvos e nomeados corretamente antes do intervalo.
-->

---

<!-- _class: exercise -->

## Crítica circulante — 15 minutos

**Sem Ficha de Crítica Formal, sem autoavaliação obrigatória.**

2–3 exemplos de UV revisado e material bem calibrado, projetados para a turma.

Nomear o erro mais comum observado (tipicamente: Metallic 0.5, Albedo muito claro).

<!--
Notas: Abertura do Encontro 2. Pergunta aberta para 2-3 voluntários: "Qual bloco foi mais difícil hoje, o UV ou o PBR? Por quê?" Sem registro formal — apenas aquece a reflexão para a CF2.
-->

---

<!-- _class: exercise -->

## Refinamento dos materiais — 30 minutos

Incorporem o que foi observado na circulação: ajustem Roughness, corrijam Metallic indevido, calibrem Albedo.

Anotem o que foi mudado e por quê — vira registro de C1.

Salvem: `[Nome]_MateriaisPBR_Semana05_v2.blend`.

<!--
Notas: Perguntar: "Você ajustou o Metallic para 0 depois da circulação. O que mudou visualmente?" Reforçar a ligação entre ajuste técnico e percepção visual.
-->

---

<!-- _class: exercise -->

## Consolidação do Hero Asset — 30 minutos

Confirmem: UV revisado + material PBR de valores planos aplicado, coerente com o tema.

Verifiquem no Viewport Rendered com HDRI: o material responde bem à luz?

Comparem com o moodboard: a cor e a "sensação de superfície" batem?

<!--
Notas: Para quem terminar rápido: "Pensem em qual outro asset do kit já poderia receber um material de teste hoje, antecipando a Semana 6." Salvar como [Nome]_HeroAsset_PBR_Semana05.blend.
-->

---

<!-- _class: exercise -->

## Antes de sair

Confirmem as três entregas de hoje:

- Hero Asset Referência com **UV revisado** (`_HeroAsset_UV_Semana05`)
- Materiais PBR de teste, **v1 e v2 pós-circulação** (`_MateriaisPBR_Semana05`)
- Hero Asset Referência com **material PBR aplicado** (`_HeroAsset_PBR_Semana05`)

<div class="warning">

Sem crítica formal hoje. A próxima é a CF2, na Semana 8 — Semanas 6 e 7 são de produção livre.

</div>

<!--
Notas: Fechamento (10 min): "A pergunta que vai guiar todo o resto do semestre é: esse valor corresponde a algo real? Se não, o material vai parecer falso, não importa quanto detalhe você pinte por cima." Ponte: na Semana 6 esses valores de Metallic/Roughness recebem textura real no canal Albedo.
-->
