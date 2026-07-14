# Plano de Aula — Semana 5
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** II — Materiais PBR e Workflow  
**Tema:** Fundamentos do Physically Based Rendering (PBR)  
**Apostila:** Parte III, Cap. 8 — Fundamentos do Physically Based Rendering; Parte III, Cap. 9 — Os Mapas que Compõem um Material PBR (Diffuse/Albedo, Metallic e Roughness). Leitura de apoio para esta CF2: Parte VI, Cap. 23 — Controle de Qualidade de Materiais  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔴 FORMAL — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 com UV otimizado: Stretch Overlay azul/verde, texel density normalizada, empacotado (Semana 4)
- Asset 02 com UV aberto: seams, Unwrap e checkerboard verificado (Semana 4)
- Familiaridade consolidada com: seams manuais, Unwrap, Average Islands Scale, Pack Islands, Stretch Overlay
- A Semana 5 inaugura a Unidade II. Pela primeira vez, os estudantes sairão do UV Editor e entrarão no Shader Editor para configurar materiais. O UV que fizeram nas Semanas 3–4 passa a ser o endereço onde os mapas PBR vão morar.

> **Contexto da Crítica Formal:** Esta é a segunda crítica formal do semestre. Ela encerra a Unidade I — o UV é avaliado de forma conclusiva aqui. Ao mesmo tempo, é a estreia do C4 (Materiais PBR) na avaliação: os estudantes vão criar materiais de teste simples ainda nesta semana, que serão avaliados na crítica.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é PBR e por que o modelo Metallic/Roughness é o padrão para jogos em tempo real.
2. Descrever a função de cada canal do Principled BSDF: Albedo (Base Color), Metallic e Roughness.
3. Atribuir valores fisicamente plausíveis de Metallic (0 ou 1) e Roughness para materiais distintos (metal, plástico, pedra, madeira).
4. Criar 4 materiais PBR simples no Blender com o Principled BSDF e verificar o resultado em render.
5. Apresentar e defender o UV do Asset 01 na crítica formal, usando vocabulário técnico correto e autoavaliação prévia preenchida.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Autoavaliação entregue antes da crítica; versionamento correto dos materiais de teste |
| C2 — Direção Artística | Coerência entre o tema do kit e os materiais escolhidos para os 4 testes de PBR |
| C3 — UV Mapping | **Encerramento da Unidade I** — avaliação definitiva do UV do Asset 01 na crítica formal |
| C4 — Materiais PBR | **Estreia na avaliação** — 4 materiais com valores de Metallic e Roughness fisicamente plausíveis |
| C10 — Participação | Qualidade da autoavaliação, da apresentação oral e do feedback oferecido na crítica formal |

> **CF2 — Crítica Formal (Portfolio de Artefatos):** Esta é a segunda crítica formal do semestre. C1, C2, C3 e C4 são avaliados — C3 pela última vez como critério principal (a partir da CF3, entra em modo de observação). O professor deve calibrar o nível atribuído com base no progresso observado nas semanas 1–4. A nota desta CF contribui com 15% para o PA.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Asset 01 e Asset 02 dos estudantes (Semana 4)
- Arquivo de demonstração: cena com 4 esferas ou cubos sem material, preparada pelo professor para aplicação ao vivo durante a demo
- HDRI de iluminação neutra para o Viewport (ex: studio_small_09 do Poly Haven — fazer download com antecedência se não estiver no laboratório)
- Projetor para demonstração e para a crítica formal
- Fichas de Crítica Formal (Instrumento 1 da Rubrica Mestre) — imprimir ou disponibilizar digitalmente
- Formulário de Autoavaliação (Instrumento 2) — enviado aos estudantes com pelo menos 48h de antecedência para preenchimento antes da aula
- Apostila — Parte III, Cap. 8 e Cap. 9 — disponibilizadas antes da aula. Parte VI, Cap. 23 (Controle de Qualidade de Materiais) recomendado como leitura de apoio para a autoavaliação desta CF2
- Referências visuais de materiais reais preparadas pelo professor: foto de metal polido, metal fosco, plástico, pedra, madeira (5 imagens)

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**PBR: por que a física da luz mudou o workflow de texturização**

Objetivo: criar o entendimento de que PBR não é um estilo visual — é um modelo matemático que simula como a luz realmente se comporta ao tocar superfícies. A consequência prática é que os materiais respondem corretamente à iluminação em qualquer cenário, sem precisar de ajustes manuais de brilho.

**Desenvolvimento:**

Abrir com uma pergunta: *"Antes do PBR, como vocês acham que os artistas faziam um material brilhante parecer brilhante em qualquer condição de luz?"*

Aguardar 2–3 respostas. Em geral vão citar: pintar highlights diretamente na textura, usar mapa especular, ajustar o material no motor. Confirmar que todas essas respostas estavam certas — e mostrar o problema: um material pintado com highlight embutido só parece bom com a luz no ângulo certo. Em qualquer outro ângulo, o brilho aparece no lugar errado.

---

**Conteúdo a cobrir:**

**1. O problema que o PBR resolve**

Antes do PBR (pré-2013), artistas adicionavam highlights, sombras e reflexos diretamente na textura difusa. Isso funcionava com uma câmera e uma iluminação fixas — como em jogos de câmera estática. Em qualquer outro ângulo ou condição de luz, os materiais quebravam.

O PBR transfere a responsabilidade da aparência do artista para a física. O artista define *o que o material é* (rugoso? metálico?), e o motor calcula *como ele parece* em cada condição de luz. O resultado é consistente em qualquer ângulo, qualquer iluminação.

**2. Dois workflows PBR — por que usamos Metallic/Roughness**

Existem dois workflows PBR principais:

- **Specular/Glossiness:** mais antigo, mais intuitivo para artistas vindos de fluxos tradicionais. Permite controle direto do reflectance. Usado em alguns pipelines legados.
- **Metallic/Roughness:** adotado pela Unity, Unreal, Blender (Principled BSDF) e pela maioria dos motores modernos. Mais simples de calibrar e menos sujeito a erros físicos.

Nesta disciplina, o workflow será **exclusivamente Metallic/Roughness**. Quando o estudante exportar para a Unity nas semanas finais, os mapas já estarão no formato esperado.

**3. Os três canais que definem qualquer material**

**Albedo (Base Color):**  
A cor pura do material, sem sombra, sem luz, sem reflexo. O Albedo deve ser uma cor "achatada" — apenas pigmento. Erros comuns: albedo com highlight pintado (material fica estranho com luz vinda do lado oposto), albedo muito escuro ou muito claro fora dos valores físicos.

Faixa física: valores entre 30–240 em 8 bits (evitar preto puro e branco puro, que não existem em materiais reais).

**Metallic:**  
Define se o material é condutor (metal) ou dielétrico (tudo o mais). Na natureza, não existe "meio metal" — um material é um ou outro. Os valores corretos são:
- 0 = dielétrico (plástico, pedra, madeira, tecido, pele)
- 1 = condutor (aço, ouro, cobre, alumínio)

Materiais mistos (ferrugem sobre metal, metal pintado) podem ter valores intermediários *apenas* nas regiões de transição.

**Roughness:**  
Define a microgranularidade da superfície — o quanto os raios de luz são espalhados ao refletir. Ao contrário do Metallic, o Roughness é genuinamente contínuo:
- 0 = espelho perfeito (reflexo nítido)
- 1 = fosco total (luz difusa, sem reflexo direcional)

O Roughness é o canal onde o artista tem mais liberdade criativa dentro do PBR. A variação de roughness é o que dá profundidade e história a um material.

**4. Calibração rápida com referências**

Mostrar as 5 referências visuais preparadas e pedir à turma que estime os valores de Metallic e Roughness de cada uma antes de revelar os valores:
- Metal polido: Metallic 1 / Roughness 0.05–0.15
- Metal fosco (anodizado): Metallic 1 / Roughness 0.4–0.6
- Plástico brilhante: Metallic 0 / Roughness 0.1–0.3
- Pedra calcária: Metallic 0 / Roughness 0.7–0.9
- Madeira natural: Metallic 0 / Roughness 0.6–0.8

> **Nota do professor:** O exercício de estimativa é mais importante do que os valores finais. O objetivo é construir intuição sobre o que o Roughness "sente" na escala 0–1. Os valores reais variam por subtipos do material (pedra polida vs. pedra bruta têm Roughness bem diferentes) — deixar isso claro para evitar memorização mecânica de valores.

---

### Demonstração — 20 minutos

**Criação de 4 materiais PBR simples no Principled BSDF**

**Setup (2 min):**  
Abrir o arquivo de demonstração com 4 objetos (esferas ou cubos). Configurar o Viewport em Rendered Mode com HDRI de iluminação neutra. Ativar o Shader Editor ao lado do Viewport (layout dividido). Mostrar o Principled BSDF já conectado à saída Material Output num dos objetos.

**Percurso da demonstração:**

**Objeto 1 — Metal polido (3 min):**
1. Selecionar o primeiro objeto. No Principled BSDF, ajustar:
   - Base Color: cinza claro neutro (R: 0.7, G: 0.7, B: 0.7) — a cor do reflexo de metais é a cor base
   - Metallic: 1.0
   - Roughness: 0.05
2. Mostrar no Viewport renderizado: superfície com reflexo nítido, quase espelho.
3. Arrastar o Roughness para 0.3 e mostrar como o reflexo fica difuso — *"Isso seria um metal escovado. Mesmo Metallic, Roughness diferente."*
4. Voltar para 0.05.

**Objeto 2 — Plástico brilhante (3 min):**
1. Selecionar o segundo objeto. Ajustar:
   - Base Color: vermelho saturado (ex: R: 0.8, G: 0.1, B: 0.1)
   - Metallic: 0.0
   - Roughness: 0.15
2. Mostrar no Viewport: reflexo difuso com cor do material visível — comportamento de dielétrico.
3. Perguntar: *"O que muda se eu colocar Metallic 0.5 aqui?"* — mostrar o resultado e explicar que o valor intermediário cria um material fisicamente incorreto para a maioria dos casos.

**Objeto 3 — Pedra áspera (3 min):**
1. Selecionar o terceiro objeto. Ajustar:
   - Base Color: cinza bege (R: 0.45, G: 0.4, B: 0.35)
   - Metallic: 0.0
   - Roughness: 0.85
2. Mostrar no Viewport: superfície completamente fosca, sem reflexo direcional, luz difusa uniforme.
3. Diminuir Roughness para 0.2: *"Isso seria uma pedra polida — mármore. O Albedo é o mesmo, só a superfície mudou."*

**Objeto 4 — Madeira (3 min):**
1. Selecionar o quarto objeto. Ajustar:
   - Base Color: marrom médio (R: 0.35, G: 0.18, B: 0.08)
   - Metallic: 0.0
   - Roughness: 0.7
2. Mostrar no Viewport: aspecto de madeira natural não tratada.

**Comparação final (6 min):**
1. Mostrar os 4 objetos lado a lado no Viewport.
2. Mover a HDRI (rotacionar a iluminação): mostrar como os materiais respondem corretamente à mudança de luz sem nenhum ajuste.
3. Perguntar à turma: *"No mundo do kit de vocês, que materiais vocês vão precisar criar? Qual é o Roughness aproximado desse material?"* — coletar 3–4 respostas.
4. Fechar com: *"No estúdio hoje, vocês vão criar 4 materiais para o tema do seu kit. Não precisam ser perfeitos — precisam ser fisicamente plausíveis. A pergunta que vai guiar cada material é: esse material é um condutor ou um dielétrico? Qual é sua microtextura?"*

> **Nota do professor:** Manter o arquivo de demonstração aberto durante o estúdio. Se algum estudante travar nos valores do Principled BSDF, referencie os 4 objetos da demo como âncora.

---

### Produção em Estúdio — 50 minutos

**Criação de 4 materiais PBR de referência temática**

**Consigna entregue verbalmente:**

> *"O objetivo deste estúdio é criar 4 materiais PBR no Blender que reflitam o universo visual do seu kit. Cada material deve ter valores de Albedo, Metallic e Roughness coerentes com um material real do seu tema. Não estamos pintando textura ainda — estamos definindo as propriedades físicas da superfície. Pense nos 4 materiais mais importantes do seu kit: provavelmente você vai precisar de uma pedra ou concreto, uma madeira ou metal, e mais dois materiais característicos do seu tema. Comecem pelo mais simples e usem as referências do moodboard."*

**Atividade estruturada:**

1. Criar um arquivo `.blend` novo com 4 primitivos (esferas recomendadas — respondem melhor ao reflexo especular).
2. Configurar o Viewport em Rendered Mode e adicionar uma HDRI neutra no World.
3. Para cada objeto, criar um material novo e nomear com o nome do material real (ex: `pedra_calcaria`, `aco_enferrujado`, `madeira_carvalho`, `couro_curtido`).
4. Configurar Albedo, Metallic e Roughness com valores de referência real.
5. Fazer screenshots do Viewport renderizado com os 4 materiais visíveis simultaneamente.
6. Salvar: `[Nome]_MaterialesPBR_Semana05.blend`.

**Papel do professor:**

Circular com foco em verificação de plausibilidade física:

- *"Qual é esse material? Ele é condutor ou dielétrico? Então seu Metallic deveria ser 0 ou 1."*
- *"Esse Roughness de 0.02 significa que a superfície é quase um espelho. A madeira do seu kit é assim polida? Olha a referência do moodboard."*
- *"O Albedo está muito claro — quase branco. Pedra real não reflete 95% da luz. Vai para algo entre 0.35 e 0.6 no valor de brilho."*
- *"Você tem dois materiais com o mesmo Roughness. São o mesmo tipo de superfície? Se não forem, a diferença tem que aparecer nos valores."*

Identificar estudantes que estão usando Metallic 0.5 como padrão — é o erro mais comum da primeira semana de PBR. Corrigir individualmente e reforçar a lógica binária do canal.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva FORMAL — 20 minutos

**Formato: apresentação individual com autoavaliação, foco em C3 (conclusivo) e C4 (estreia)**

Esta é uma crítica formal. A autoavaliação deve ter sido entregue antes da aula. O professor já a leu e marcou divergências entre a autoavaliação do estudante e sua própria observação — essas divergências são o material mais rico da conversa.

**Protocolo da crítica formal:**

**Abertura (2 min):**  
Professor enuncia os dois focos da crítica: *"Hoje fecha a avaliação de UV (C3) — é a última vez que o UV do Asset 01 está em avaliação. Ao mesmo tempo, começa a avaliação de PBR (C4). Vamos olhar para as duas coisas."*

Lembrar à turma o protocolo de crítica: o apresentador fala primeiro, a turma observa, depois a conversa abre. Não interromper durante a apresentação.

**Apresentações (14 min — 3 a 4 estudantes, ≈3–4 min cada):**

Para cada apresentador, o roteiro é:

1. **(30 seg)** Apresentar o tema do kit e os materiais escolhidos para os 4 testes.
2. **(1 min)** Mostrar o UV do Asset 01 com Stretch Overlay ativo e checkerboard. Descrever: onde há distorção residual, por quê os seams foram posicionados assim, qual o aproveitamento estimado do espaço.
3. **(1 min)** Mostrar os 4 materiais PBR em Rendered Mode. Justificar os valores de Metallic e Roughness de pelo menos dois materiais com referência a um material real.
4. **(30 seg)** Citar o nível da autoavaliação em C3 e C4 e a justificativa principal.

Após cada apresentação, o professor faz 1–2 perguntas diretas à turma:
- *"O Roughness desse metal parece coerente com o que você esperaria de um metal do universo [tema do kit]?"*
- *"O UV tem alguma área que vocês identificam como problema? Por quê?"*

**Fechamento da crítica (4 min):**  
Professor enuncia os padrões observados:
- Qual é o erro de PBR mais comum na turma (tipicamente: Metallic 0.5, Albedo muito claro, Roughness uniforme em todos os materiais).
- Qual é a qualidade geral dos UVs entregues — comparada com a Semana 3.
- Uma orientação coletiva para o estúdio: *"No estúdio de hoje, o foco é corrigir o que a crítica apontou nos materiais PBR. O UV pode ser ajustado se houver tempo, mas não é a prioridade."*

> **Nota do professor:** Não é necessário que todos os estudantes apresentem formalmente. Selecionar 3–4 trabalhos que cubram o espectro: um UV forte com PBR iniciante, um UV com problemas e um PBR bem resolvido, e um caso intermediário. Os demais estudantes entregam a Ficha de Crítica Formal preenchida pelo professor individualmente ao final do encontro. A autoavaliação de todos é registrada independentemente de quem apresenta.

---

### Produção em Estúdio — 60 minutos

**Refinamento dos materiais PBR + início da aplicação ao Asset 01**

**Consigna:**

> *"Sessenta minutos com dois objetivos. Primeiro: incorporar o que a crítica apontou nos 4 materiais — ajustar valores de Roughness, corrigir Metallic indevido, calibrar Albedo. Segundo, para quem terminar: criar um material PBR para o Asset 01 do kit, usando os valores que você definiu no arquivo de materiais de teste. Esse é o primeiro passo real do pipeline: UV como mapa, material como intenção."*

**Atividade:**

**Parte 1 — Refinamento dos materiais de teste (≈25 min):**
1. Abrir o arquivo `_MaterialesPBR_Semana05.blend`.
2. Ajustar os valores apontados na crítica formal — anotar o que foi mudado e por quê (para a entrega de C1).
3. Capturar novo screenshot com os 4 materiais revisados.
4. Salvar: `[Nome]_MaterialesPBR_Semana05_v2.blend`.

**Parte 2 — Aplicação do material ao Asset 01 (≈35 min):**
1. Abrir o arquivo do Asset 01 com UV otimizado (Semana 4).
2. Criar um novo material para o Asset 01 no Principled BSDF — apenas valores de cor plana, sem mapa ainda.
3. Configurar Albedo, Metallic e Roughness com base no material real que o Asset 01 representa no kit.
4. Verificar no Viewport Rendered com HDRI: o material responde coerentemente à luz?
5. Comparar com a referência do moodboard: a cor e a "sensação de superfície" são próximas?
6. Salvar: `[Nome]_Asset01_PBR_Semana05.blend`.

**Papel do professor:**

- *"Você ajustou o Metallic para 0 depois da crítica. O que mudou visualmente? Você acha que ficou mais próximo da referência?"* — reforçar a ligação entre o ajuste técnico e a percepção visual.
- *"Esse Asset 01 tem só um material? Ou partes dele são feitas de materiais diferentes?"* — alguns assets têm múltiplos materiais (ex.: uma lanterna tem vidro, metal e couro). Orientar o estudante a identificar e separar os slots.
- Para estudantes rápidos: *"Aplica o mesmo material no Asset 02 — como os dois ficam lado a lado? A leitura visual do kit começa a aparecer?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese técnica)**  
*"Hoje vocês deixaram de trabalhar só com geometria e UV e começaram a definir o que os materiais são fisicamente. A pergunta que vai guiar todo o resto do semestre é: esse valor corresponde a algo real? Se a resposta for não, o material vai parecer falso, independentemente de quanto detalhe você pintar por cima."*

2. **(3 min — Reflexão de processo)**  
Pergunta para 2–3 voluntários: *"Qual dos 4 materiais foi mais difícil de calibrar? Por quê? O que você usou de referência para decidir o Roughness?"* O objetivo é verbalizar a lógica de decisão — que é o núcleo do C4.

3. **(3 min — Antecipação da Semana 6)**  
*"Na semana que vem, vocês vão sair dos valores planos e começar a trabalhar com texturas seamless — imagens reais de superfície que vão para o canal de Albedo. O material que vocês definiram hoje vai ganhar variação, micro-detalhe e a identidade visual do tema. Guardem os arquivos com versionamento correto — vamos importar os valores de Roughness e Metallic que vocês escolheram hoje para dentro das texturas."*

4. **(2 min — Confirmação das entregas)**  
Recapitular as entregas da semana com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Confundir Roughness com Glossiness**  
Estudantes que trabalharam em outros softwares ou viram tutoriais mais antigos podem ter a intuição invertida: achar que "mais Roughness = mais brilho". No Blender (e no Metallic/Roughness workflow), Roughness 0 = superfície lisa e reflexiva; Roughness 1 = fosco. Estratégia: escrever no quadro durante toda a aula: `Roughness 0 = espelho | Roughness 1 = fosco`. Referenciar os 4 objetos da demo como âncora visual sempre que o erro aparecer.

**2. Usar Metallic 0.5 como padrão**  
É o erro mais frequente. O estudante acha que "deixar no meio" é mais seguro. O resultado é um material que não é metal nem plástico — visualmente parece "emborrachado" e perde a identidade. Estratégia: mostrar ao vivo no Viewport a diferença entre Metallic 0, 0.5 e 1 com o mesmo Roughness. Perguntar: *"Você já viu um material assim na vida real? Se não, não deve existir no jogo."*

**3. Albedo com valores extremos (muito claro ou muito escuro)**  
Albedo branco puro (valor 1.0) e preto puro (valor 0.0) não existem em materiais físicos reais. Branco puro reflete 100% da luz — nenhum material real faz isso. Preto puro absorve 100% — só materiais como Vantablack chegam perto. Estratégia: pedir que o estudante olhe a referência do moodboard e diga em percentual quão claro o material parece. Usar isso como âncora para ajustar o valor do Albedo.

**4. Dificuldade de relacionar os materiais de teste com o tema do kit**  
Alguns estudantes criam os 4 materiais de forma genérica (pedra, madeira, metal, plástico) sem pensar na identidade visual do kit. O material de "pedra" de um kit Medieval tem textura e cor bem diferentes do de um kit Sci-Fi. Estratégia: pedir que o estudante abra o moodboard ao lado do Blender e escolha um material específico visível em alguma das referências — não um material genérico, mas *aquela* superfície específica.

**5. UV não está pronto para receber material**  
Alguns estudantes podem chegar com UV do Asset 01 ainda problemático (distorção severa ou espaço UV mal aproveitado). A aplicação do material ao Asset 01 vai revelar esses problemas de forma visual — quadros da textura checkerboard aparecem esticados. Estratégia: usar esse momento como oportunidade de diagnóstico, não de pressão. *"O material está mostrando que o UV precisa de ajuste aqui. Você quer corrigir isso agora ou terminar o material e registrar como ponto de melhoria?"* — deixar a decisão com o estudante.

**6. HDRI não disponível no laboratório**  
Sem HDRI, o Rendered Mode mostra iluminação de mundo padrão (cinza uniforme) que não permite avaliar corretamente a plausibilidade dos materiais PBR. Estratégia: preparar com antecedência um arquivo `.blend` com a HDRI embutida nos dados do arquivo (opção "Pack into .blend" no World). Ou usar a iluminação padrão do Studio com 3 luzes de area light posicionadas para criar ambiente de avaliação mínimo.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante com Roughness igual em todos os 4 materiais | Perguntar: *"Você fecharia os olhos e diria que está tocando madeira vs. pedra só pelo tato? O Roughness é o equivalente visual do tato. Se os valores são iguais, a sensação é a mesma."* |
| Estudante inseguro sobre os valores "certos" | Redirecionar para a referência: *"Não existe valor certo sem referência. Abre o moodboard, escolhe uma foto desse material e descreve pra mim: reflexo difuso, nítido, ou sem reflexo? Isso é o Roughness."* |
| Estudante satisfeito com material claramente incorreto fisicamente (ex: pedra metálica) | Perguntar: *"Pedra conduz eletricidade? Não. Então ela é um dielétrico — Metallic tem que ser 0. O que o Metallic 0.8 está adicionando aqui que um Roughness baixo não resolveria?"* |
| Estudante resistente à crítica da autoavaliação | Não confrontar diretamente. Mostrar a referência ao lado do material no Viewport: *"Você avaliou C4 como nível 4. Esse material da sua referência e esse do Blender parecem o mesmo para você? O que você vê de diferente?"* |
| Estudante que termina os 4 materiais rapidamente e quer avançar | Propor que aplique todos os 4 materiais nos assets do kit em um único arquivo `.blend`, configurando múltiplos slots de material por objeto onde for pertinente — antecipando a Semana 6. |
| Turma com dificuldade geral de calibrar Albedo | Usar analogia fotográfica: *"Albedo é como você fotografaria o material num dia nublado, com iluminação difusa e neutra. Sem sombra, sem reflexo. Se a foto ficaria escura, o Albedo é escuro. Se ficaria clara, é clara. Sem extremos."* |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Autoavaliação entregue antes da crítica com justificativas por escrito | C1 — Processo de Projeto | Existência, completude e qualidade reflexiva das respostas |
| 4 materiais PBR com Metallic 0 ou 1 (exceto em casos justificados), Roughness diferenciado entre materiais | C4 — Materiais PBR | Análise dos valores no Principled BSDF; comparação visual com referências reais do tema |
| Screenshot do Viewport Rendered com 4 materiais em iluminação de estúdio | C4 — Materiais PBR | Plausibilidade física visual: materiais metálicos com reflexo direcional, foscos com difusão uniforme |
| UV do Asset 01 com Stretch Overlay ativo apresentado e justificado na crítica | C3 — UV Mapping | Qualidade final do UV conforme critério C3 da Rubrica Mestre — avaliação conclusiva de Unidade I |
| Material aplicado ao Asset 01 com Principled BSDF | C4 — Materiais PBR | Coerência entre o material atribuído e o objeto real que o asset representa no tema do kit |
| Justificativa oral dos valores de Roughness e Metallic durante a crítica | C10 — Participação | Uso de vocabulário técnico correto (condutor/dielétrico, microgranularidade), argumentação baseada em referência real |
| Arquivo nomeado e versionado corretamente (incluindo v2 pós-crítica) | C1 — Processo de Projeto | Existência dos arquivos com sufixo `_Semana05` e distinção entre v1 e v2 |

---

## Entrega da Semana 5

| Entrega | Formato | Prazo |
|---|---|---|
| Autoavaliação preenchida (Instrumento 2 da Rubrica) | Documento físico ou digital | **Antes da crítica formal** (início do segundo encontro) |
| 4 materiais PBR temáticos configurados no Principled BSDF (v1 e v2 pós-crítica) | `.blend` com sufixo `_MaterialesPBR_Semana05` | Até o fim do segundo encontro |
| Asset 01 com material PBR aplicado | `.blend` com sufixo `_Asset01_PBR_Semana05` | Até o fim do segundo encontro |
| Screenshots: Viewport Rendered com 4 materiais + Asset 01 com material aplicado | PNG ou JPG (2 imagens no mínimo) | Até o fim do segundo encontro |

> **Nota:** Esta semana encerra a CF2. O professor deve registrar as notas de C1, C2, C3 e C4 na Ficha de Crítica Formal e consolidar o registro de C10 (observação) antes da próxima aula.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 5 | 2026*
