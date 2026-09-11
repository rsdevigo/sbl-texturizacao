# Plano de Aula — Semana 5
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** I/II — Transição: Revisão de UV e Fundamentos do PBR  
**Tema:** Revisão de UV com base no feedback da CF1 e fundamentos de PBR (Principled BSDF)  
**Apostila:** Parte II, Cap. 6 — Texel Density e Organização de UVs (revisão rápida); Parte III, Cap. 8 — Fundamentos do Physically Based Rendering; Parte III, Cap. 9 — Os Mapas que Compõem um Material PBR (Diffuse/Albedo, Metallic e Roughness)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro (sem instrumento formal; a próxima crítica formal é a CF2, na Semana 8)

---

## Pré-requisito da semana

Os estudantes chegam com:

- Hero Asset Referência com UV aberto (seams manuais, Unwrap) e feedback escrito recebido na crítica formal da Semana 4 (CF1)
- Familiaridade consolidada com: seams manuais, Unwrap, Average Islands Scale, Pack Islands, Stretch Overlay
- A Semana 5 fecha a Unidade I revisando o UV a partir do feedback da CF1, e abre a Unidade II com a primeira aproximação a materiais PBR. Pela primeira vez, os estudantes sairão do UV Editor e entrarão no Shader Editor para configurar materiais. O UV revisado nesta semana é o endereço onde os mapas PBR das próximas semanas vão morar.

> **Nota de transição:** Não há crítica formal nesta semana — a Semana 5 é um encontro de ajuste e abertura, não de avaliação conclusiva. A CF1 (Semana 4) já avaliou C3 (UV Mapping) formalmente; esta semana serve para incorporar esse feedback antes de seguir adiante, sem nova cobrança de rubrica. A próxima crítica formal, a CF2, acontece somente na Semana 8, ao final da Unidade II — ela avaliará o resultado acumulado de UV, material PBR e textura, já dentro do 3D Coat.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Corrigir distorção e aproveitamento de espaço UV do Hero Asset Referência com base no feedback recebido na CF1.
2. Explicar o que é PBR e por que o modelo Metallic/Roughness é o padrão para jogos em tempo real.
3. Descrever a função de cada canal do Principled BSDF: Albedo (Base Color), Metallic e Roughness.
4. Atribuir valores fisicamente plausíveis de Metallic (0 ou 1) e Roughness para materiais distintos (metal, plástico, pedra, madeira).
5. Criar materiais PBR de teste no Blender com o Principled BSDF e aplicar um deles, com valores planos, ao Hero Asset Referência.

---

## Critérios da Rubrica Mestre observados nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Registro do que foi ajustado no UV a partir do feedback da CF1; nomenclatura de arquivo consistente |
| C3 — UV Mapping | Observado (não avaliado formalmente) — incorporação do feedback da CF1 antes da CF2 |
| C4 — Materiais PBR | Observado (não avaliado formalmente) — primeira aproximação: valores de Metallic e Roughness fisicamente plausíveis |

> **Sem crítica formal:** Esta semana não atribui nota. O professor observa e orienta, mas o registro formal de C3 e C4 só volta a acontecer na CF2 (Semana 8), quando o material PBR já estiver acompanhado de textura real e migrado para o 3D Coat.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Hero Asset Referência de cada estudante, com UV aberto e feedback escrito da CF1 em mãos
- Arquivo de demonstração: cena com 4 esferas ou cubos sem material, preparada pelo professor para aplicação ao vivo durante a demo
- HDRI de iluminação neutra para o Viewport (ex: studio_small_09 do Poly Haven — fazer download com antecedência se não estiver no laboratório)
- Projetor para demonstração e para a crítica circulante
- Apostila — Parte II, Cap. 6 (revisão), Parte III, Cap. 8 e Cap. 9 — disponibilizadas antes da aula
- Referências visuais de materiais reais preparadas pelo professor: foto de metal polido, metal fosco, plástico, pedra, madeira (5 imagens)

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Parte 1 (≈8 min) — Fechando o UV: revisão rápida de distorção e aproveitamento**

Objetivo: relembrar Stretch Overlay, texel density e Pack Islands o suficiente para que os estudantes consigam agir sobre o feedback da CF1 sem precisar de uma aula nova sobre o assunto.

Revisão rápida no quadro/projetor:
- Stretch Overlay: azul = compressão, vermelho = esticamento. Meta: predominância de verde/azul-claro neutro.
- Texel density: todas as islands do mesmo objeto devem ter densidade equivalente (Average Islands Scale resolve a maior parte dos casos).
- Pack Islands: aproveitamento do espaço 0–1, padding consistente entre islands.

*"Vocês já viram tudo isso na Semana 4. Hoje não é aula nova de UV — é a correção do que a crítica formal apontou. Abram o feedback que receberam e localizem, no próprio arquivo, onde está o problema."*

**Parte 2 (≈12 min) — PBR: por que a física da luz mudou o workflow de texturização**

Objetivo: criar o entendimento de que PBR não é um estilo visual — é um modelo matemático que simula como a luz realmente se comporta ao tocar superfícies. A consequência prática é que os materiais respondem corretamente à iluminação em qualquer cenário, sem precisar de ajustes manuais de brilho.

Abrir com uma pergunta: *"Antes do PBR, como vocês acham que os artistas faziam um material brilhante parecer brilhante em qualquer condição de luz?"*

Aguardar 2–3 respostas. Em geral vão citar: pintar highlights diretamente na textura, usar mapa especular, ajustar o material no motor. Confirmar que todas essas respostas estavam certas — e mostrar o problema: um material pintado com highlight embutido só parece bom com a luz no ângulo certo. Em qualquer outro ângulo, o brilho aparece no lugar errado.

**Conteúdo a cobrir:**

**1. O problema que o PBR resolve**

Antes do PBR (pré-2013), artistas adicionavam highlights, sombras e reflexos diretamente na textura difusa. Isso funcionava com uma câmera e uma iluminação fixas — como em jogos de câmera estática. Em qualquer outro ângulo ou condição de luz, os materiais quebravam.

O PBR transfere a responsabilidade da aparência do artista para a física. O artista define *o que o material é* (rugoso? metálico?), e o motor calcula *como ele parece* em cada condição de luz. O resultado é consistente em qualquer ângulo, qualquer iluminação.

**2. Dois workflows PBR — por que usamos Metallic/Roughness**

- **Specular/Glossiness:** mais antigo, mais intuitivo para artistas vindos de fluxos tradicionais. Permite controle direto do reflectance. Usado em alguns pipelines legados.
- **Metallic/Roughness:** adotado pela Unity, Unreal, Blender (Principled BSDF), 3D Coat e pela maioria dos motores modernos. Mais simples de calibrar e menos sujeito a erros físicos.

Nesta disciplina, o workflow será **exclusivamente Metallic/Roughness**. Quando o estudante exportar para a Unity nas semanas finais, os mapas já estarão no formato esperado.

**3. Os três canais que definem qualquer material**

**Albedo (Base Color):** A cor pura do material, sem sombra, sem luz, sem reflexo. Erros comuns: albedo com highlight pintado, albedo muito escuro ou muito claro fora dos valores físicos (evitar preto puro e branco puro).

**Metallic:** Define se o material é condutor (metal) ou dielétrico (tudo o mais). Na natureza, não existe "meio metal":
- 0 = dielétrico (plástico, pedra, madeira, tecido, pele)
- 1 = condutor (aço, ouro, cobre, alumínio)

**Roughness:** Define a microgranularidade da superfície. Ao contrário do Metallic, é genuinamente contínuo:
- 0 = espelho perfeito (reflexo nítido)
- 1 = fosco total (luz difusa, sem reflexo direcional)

O Roughness é o canal onde o artista tem mais liberdade criativa dentro do PBR.

**4. Calibração rápida com referências**

Mostrar as 5 referências visuais preparadas e pedir à turma que estime os valores de Metallic e Roughness de cada uma antes de revelar os valores:
- Metal polido: Metallic 1 / Roughness 0.05–0.15
- Metal fosco (anodizado): Metallic 1 / Roughness 0.4–0.6
- Plástico brilhante: Metallic 0 / Roughness 0.1–0.3
- Pedra calcária: Metallic 0 / Roughness 0.7–0.9
- Madeira natural: Metallic 0 / Roughness 0.6–0.8

> **Nota do professor:** O exercício de estimativa é mais importante do que os valores finais. Os valores reais variam por subtipos do material — deixar isso claro para evitar memorização mecânica de valores.

---

### Demonstração — 20 minutos

**Parte 1 (≈5 min) — Correção ao vivo de um UV com distorção residual**

Abrir um arquivo de prática com distorção evidente (esticamento visível no Stretch Overlay). Aplicar Average Islands Scale e Pack Islands, comparando o resultado antes/depois. *"Isso é exatamente o que vocês vão fazer com o feedback da própria CF1 daqui a pouco."*

**Parte 2 (≈15 min) — Criação de materiais PBR simples no Principled BSDF**

**Setup (1 min):** Abrir o arquivo de demonstração com 4 objetos (esferas ou cubos). Viewport em Rendered Mode com HDRI neutra. Shader Editor ao lado do Viewport.

**Objeto 1 — Metal polido (3 min):**
1. Base Color: cinza claro neutro (R: 0.7, G: 0.7, B: 0.7); Metallic: 1.0; Roughness: 0.05.
2. Mostrar reflexo nítido no Viewport renderizado. Arrastar Roughness para 0.3: *"Isso seria um metal escovado. Mesmo Metallic, Roughness diferente."* Voltar para 0.05.

**Objeto 2 — Plástico brilhante (3 min):**
1. Base Color vermelho saturado (R: 0.8, G: 0.1, B: 0.1); Metallic: 0.0; Roughness: 0.15.
2. Perguntar: *"O que muda se eu colocar Metallic 0.5 aqui?"* — mostrar o resultado fisicamente incorreto.

**Objeto 3 — Pedra áspera (3 min):**
1. Base Color cinza bege (R: 0.45, G: 0.4, B: 0.35); Metallic: 0.0; Roughness: 0.85.
2. Diminuir Roughness para 0.2: *"Isso seria mármore polido. O Albedo é o mesmo, só a superfície mudou."*

**Objeto 4 — Madeira (2 min):**
1. Base Color marrom médio (R: 0.35, G: 0.18, B: 0.08); Metallic: 0.0; Roughness: 0.7.

**Fechamento (3 min):** Mostrar os 4 objetos lado a lado, rotacionar a HDRI e mostrar como os materiais respondem corretamente sem nenhum ajuste manual. *"No estúdio hoje, vocês vão primeiro corrigir o UV com o feedback da CF1 e depois criar materiais de teste para o tema do seu kit. A pergunta que vai guiar cada material é: esse material é condutor ou dielétrico? Qual é sua microtextura?"*

> **Nota do professor:** Manter os dois arquivos de demonstração abertos durante o estúdio, como âncora para dúvidas de UV e de PBR.

---

### Produção em Estúdio — 50 minutos

**Revisão de UV + primeiros materiais PBR do tema**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com dois blocos. No primeiro, corrijam o UV do Hero Asset Referência com base no feedback escrito que vocês receberam na semana passada — foco em distorção e aproveitamento de espaço. No segundo, criem de 2 a 4 materiais PBR de teste que reflitam o universo visual do seu kit: valores de Albedo, Metallic e Roughness, sem textura ainda. Estamos definindo as propriedades físicas da superfície, não pintando nada."*

**Atividade estruturada:**

**Etapa 1 — Revisão do UV (≈20 min):**
1. Reabrir o Hero Asset Referência com o feedback da CF1 em mãos.
2. Reativar Stretch Overlay e identificar as islands apontadas como problemáticas.
3. Aplicar Average Islands Scale e/ou Pack Islands para corrigir distorção e aproveitamento.
4. Screenshot do UV revisado com checkerboard, para comparação com o estado da CF1.
5. Salvar: `[Nome]_HeroAsset_UV_Semana05.blend`.

**Etapa 2 — Materiais PBR de teste (≈25 min):**
1. Criar de 2 a 4 materiais novos no Principled BSDF, nomeados com o nome do material real (ex: `pedra_calcaria`, `aco_enferrujado`, `madeira_carvalho`).
2. Configurar Albedo, Metallic e Roughness com valores de referência real, usando o moodboard como base.
3. Aplicar um dos materiais, com valores planos, ao próprio Hero Asset Referência com UV já revisado.
4. Screenshot do Viewport renderizado com os materiais de teste e o Hero Asset com material aplicado.

**Etapa 3 — Registro (≈5 min):**
1. Salvar: `[Nome]_MateriaisPBR_Semana05.blend`.

**Papel do professor:**

Circular com foco duplo — verificação de UV corrigido e plausibilidade física dos materiais:

- *"O que a CF1 apontou como problema nesse UV? Mostra onde você corrigiu."*
- *"Qual é esse material? Ele é condutor ou dielétrico? Então seu Metallic deveria ser 0 ou 1."*
- *"Esse Roughness de 0.02 significa que a superfície é quase um espelho. A madeira do seu kit é assim polida? Olha a referência do moodboard."*
- *"O Albedo está muito claro — quase branco. Pedra real não reflete 95% da luz."*

Identificar estudantes usando Metallic 0.5 como padrão — erro mais comum da primeira semana de PBR. Corrigir individualmente e reforçar a lógica binária do canal.

---

## ENCONTRO 2 (1h30)

### Crítica Circulante Informal — 15 minutos

**Formato: comentário coletivo rápido, sem apresentação individual estruturada**

Sem Ficha de Crítica Formal e sem autoavaliação obrigatória. O professor circula durante os primeiros minutos do encontro observando os arquivos salvos no dia anterior e reúne a turma para um comentário coletivo breve.

**Roteiro:**

1. **(5 min)** Mostrar 2–3 exemplos de UV revisado com sucesso (antes/depois) e 1–2 exemplos de material PBR bem calibrado, projetados para a turma.
2. **(5 min)** Nomear o erro mais comum observado na circulação (tipicamente: Metallic 0.5, Albedo muito claro, Roughness igual em materiais diferentes).
3. **(5 min)** Pergunta aberta para 2–3 voluntários: *"Qual desses dois blocos foi mais difícil hoje, o UV ou o PBR? Por quê?"* — sem registro formal, apenas para aquecer a reflexão que será cobrada na CF2.

> **Nota do professor:** Esta não é uma crítica formal — não há nota nem Ficha de Crítica Formal. O objetivo é dar visibilidade coletiva rápida e recalibrar antes do estúdio, mantendo o ritmo de estúdio sem o peso de uma apresentação individual.

---

### Produção em Estúdio — 65 minutos

**Refinamento dos materiais PBR + consolidação do Hero Asset Referência**

**Consigna:**

> *"Sessenta e cinco minutos com dois objetivos. Primeiro: incorporar o que foi observado na circulação — ajustar valores de Roughness, corrigir Metallic indevido, calibrar Albedo. Segundo, para quem terminar: criar mais um material de teste, cobrindo um material do tema que ainda não foi representado. Guardem os arquivos com versionamento — a partir da Semana 6, esses valores de Metallic e Roughness vão receber textura real no canal Albedo."*

**Atividade:**

**Parte 1 — Refinamento dos materiais de teste (≈30 min):**
1. Abrir o arquivo `_MateriaisPBR_Semana05.blend`.
2. Ajustar os valores observados na circulação — anotar o que foi mudado e por quê (para o registro de C1).
3. Capturar novo screenshot com os materiais revisados.
4. Salvar: `[Nome]_MateriaisPBR_Semana05_v2.blend`.

**Parte 2 — Consolidação do Hero Asset Referência (≈30 min):**
1. Conferir que o Hero Asset Referência está com UV revisado e material PBR de valores planos aplicado, coerente com o material real que representa no kit.
2. Verificar no Viewport Rendered com HDRI: o material responde coerentemente à luz?
3. Comparar com a referência do moodboard: a cor e a "sensação de superfície" são próximas?
4. Salvar: `[Nome]_HeroAsset_PBR_Semana05.blend`.

**Papel do professor:**

- *"Você ajustou o Metallic para 0 depois da circulação. O que mudou visualmente?"* — reforçar a ligação entre ajuste técnico e percepção visual.
- *"Esse Hero Asset tem só um material? Ou partes dele são feitas de materiais diferentes?"* — orientar sobre múltiplos slots de material quando pertinente.
- Para estudantes rápidos: *"Pensem em qual outro asset do kit já poderia receber um material de teste hoje, antecipando a Semana 6."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese técnica)**
*"Hoje vocês fecharam o ciclo de UV da CF1 e começaram a definir o que os materiais do kit são fisicamente. A pergunta que vai guiar todo o resto do semestre é: esse valor corresponde a algo real? Se a resposta for não, o material vai parecer falso, independentemente de quanto detalhe você pintar por cima."*

2. **(3 min — Reflexão de processo)**
Pergunta para 2–3 voluntários: *"Qual dos materiais foi mais difícil de calibrar? Por quê? O que você usou de referência para decidir o Roughness?"*

3. **(3 min — Antecipação da Semana 6)**
*"Na semana que vem, vocês vão sair dos valores planos e começar a trabalhar com texturas seamless — imagens reais ou pintadas de superfície que vão para o canal de Albedo. O material que vocês definiram hoje vai ganhar variação, micro-detalhe e a identidade visual do tema. Guardem os arquivos com versionamento correto — vamos importar os valores de Roughness e Metallic que vocês escolheram hoje para dentro das texturas."*

4. **(2 min — Confirmação das entregas)**
Recapitular as entregas da semana com nomenclatura esperada. Lembrar que a próxima crítica formal, a CF2, é só na Semana 8 — esta e a próxima semana (6 e 7) são de produção livre, sem nota.

---

## Possíveis Dificuldades

**1. Estudante trata a revisão de UV como opcional por não haver nota nesta semana**
Sem crítica formal, alguns estudantes podem relaxar a correção do UV. Estratégia: reforçar que o UV desta semana é o que vai receber textura definitiva já na Semana 6 — um UV mal corrigido agora se torna um problema de textura visível duas semanas depois, quando for mais custoso corrigir.

**2. Confundir Roughness com Glossiness**
Estudantes que trabalharam em outros softwares podem ter a intuição invertida. Estratégia: escrever no quadro durante toda a aula: `Roughness 0 = espelho | Roughness 1 = fosco`. Referenciar os 4 objetos da demo como âncora visual.

**3. Usar Metallic 0.5 como padrão**
Erro mais frequente — o estudante acha que "deixar no meio" é mais seguro. Estratégia: mostrar ao vivo a diferença entre Metallic 0, 0.5 e 1 com o mesmo Roughness. Perguntar: *"Você já viu um material assim na vida real? Se não, não deve existir no jogo."*

**4. Albedo com valores extremos (muito claro ou muito escuro)**
Albedo branco puro e preto puro não existem em materiais físicos reais. Estratégia: pedir que o estudante olhe a referência do moodboard e diga em percentual quão claro o material parece.

**5. Dificuldade de relacionar os materiais de teste com o tema do kit**
Alguns estudantes criam materiais de forma genérica (pedra, madeira, metal) sem pensar na identidade visual do kit. Estratégia: pedir que o estudante abra o moodboard ao lado do Blender e escolha uma superfície específica de alguma referência, não um material genérico.

**6. HDRI não disponível no laboratório**
Sem HDRI, o Rendered Mode não permite avaliar corretamente a plausibilidade dos materiais PBR. Estratégia: preparar com antecedência um `.blend` com a HDRI embutida ("Pack into .blend"), ou usar 3 luzes de area light posicionadas como ambiente mínimo.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe por onde começar a corrigir o UV | Reabrir o feedback escrito da CF1 junto com o estudante e apontar, no Stretch Overlay, exatamente a island mencionada no feedback. |
| Estudante com Roughness igual em todos os materiais | Perguntar: *"Você fecharia os olhos e diria que está tocando madeira vs. pedra só pelo tato? O Roughness é o equivalente visual do tato."* |
| Estudante inseguro sobre os valores "certos" | Redirecionar para a referência: *"Não existe valor certo sem referência. Abre o moodboard, escolhe uma foto desse material e descreve: reflexo difuso, nítido, ou sem reflexo?"* |
| Estudante satisfeito com material claramente incorreto fisicamente (ex: pedra metálica) | Perguntar: *"Pedra conduz eletricidade? Não. Então ela é um dielétrico — Metallic tem que ser 0."* |
| Estudante que termina rápido e quer avançar | Propor que crie um material adicional para outro elemento do tema do kit, antecipando a Semana 6. |
| Turma com dificuldade geral de calibrar Albedo | Usar analogia fotográfica: *"Albedo é como você fotografaria o material num dia nublado, com iluminação difusa e neutra. Sem sombra, sem reflexo."* |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar (observação, sem nota formal) |
|---|---|---|
| UV do Hero Asset Referência revisado, com distorção e aproveitamento corrigidos conforme feedback da CF1 | C3 — UV Mapping (observado) | Comparação visual do Stretch Overlay antes (CF1) e depois (Semana 5) |
| Materiais PBR de teste com Metallic 0 ou 1 (exceto casos justificados), Roughness diferenciado entre materiais | C4 — Materiais PBR (observado) | Análise dos valores no Principled BSDF; comparação visual com referências reais do tema |
| Hero Asset Referência com material PBR de valores planos aplicado | C4 — Materiais PBR (observado) | Coerência entre o material atribuído e o objeto real que representa no tema do kit |
| Arquivo nomeado e versionado corretamente (incluindo v2 pós-circulação) | C1 — Processo de Projeto | Existência dos arquivos com sufixo `_Semana05` e distinção entre v1 e v2 |

---

## Entrega da Semana 5

| Entrega | Formato | Prazo |
|---|---|---|
| Hero Asset Referência com UV revisado | `.blend` com sufixo `_HeroAsset_UV_Semana05` | Até o fim do primeiro encontro |
| Materiais PBR de teste (v1 e v2 pós-circulação) | `.blend` com sufixo `_MateriaisPBR_Semana05` | Até o fim do segundo encontro |
| Hero Asset Referência com material PBR de valores planos aplicado | `.blend` com sufixo `_HeroAsset_PBR_Semana05` | Até o fim do segundo encontro |
| Screenshots: UV revisado + Viewport Rendered com materiais de teste | PNG ou JPG (2 imagens no mínimo) | Até o fim do segundo encontro |

> **Nota:** Esta semana não tem crítica formal nem nota. As observações do professor sobre C1, C3 e C4 alimentam o acompanhamento informal do progresso, servindo de base para a CF2, na Semana 8.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 5 | 2026*
