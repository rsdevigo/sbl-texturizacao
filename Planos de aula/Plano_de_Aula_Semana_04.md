# Plano de Aula — Semana 4
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** I — Fundamentos e Mapeamento UV  
**Tema:** Otimização de layout UV: distorção, aproveitamento e densidade de texel  
**Apostila:** Parte II, Cap. 6 — Texel Density e Organização de UVs (análise de distorção; otimização de layout e empacotamento de UV islands)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔵 Informal — circulante em estúdio e comentário coletivo ao final do segundo encontro

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 do Kit Modular com UV aberto via seams manuais e Unwrap (Semana 3)
- Arquivo versionado `_v2` revisado após a crítica formal da Semana 3
- Formulário de Autoavaliação da Semana 3 já entregue e comentado
- Familiaridade com: marcação de seams, Unwrap, checkerboard, organização manual de islands no UV Editor
- Feedback escrito do professor sobre o C3 da Semana 3 disponível para consulta durante o estúdio

Esta semana é a continuação direta da Semana 3. O UV já foi aberto — agora o foco é qualificar esse UV: detectar e corrigir distorção, normalizar texel density e empacotar o layout com eficiência. É também a semana em que o Asset 02 começa a ter UV.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Usar o Stretch Overlay do Blender para identificar regiões com distorção de UV e nomear a causa (estiramento, compressão, island mal orientada).
2. Explicar o conceito de texel density e por que islands de tamanhos diferentes resultam em resolução de textura inconsistente.
3. Normalizar o tamanho relativo das UV islands de um asset usando o comando Average Islands Scale.
4. Usar Pack Islands para empacotar o layout UV de forma eficiente sem sobreposição.
5. Abrir o UV do Asset 02 aplicando desde o início os critérios da Semana 3, sem precisar de uma rodada de correção.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Arquivo versionado corretamente (`_Semana04`), pasta organizada, entrega nos dois assets |
| C2 — Direção Artística | Asset 02 escolhido de forma coerente com o tema do kit e com o Asset 01 (conjunto visual consistente) |
| C3 — UV Mapping | **Foco principal:** texel density normalizada, aproveitamento eficiente do espaço UV, ausência de distorção vermelha no Stretch Overlay |
| C10 — Participação | Qualidade do feedback oferecido na crítica informal; engajamento durante o estúdio |

> Esta é a **última semana da Unidade I**. A Semana 5 inicia PBR com os UVs já prontos. Um UV com problemas nesta semana vai gerar retrabalho nas próximas três unidades — comunicar isso aos estudantes com clareza.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Asset 01 com UV da Semana 3 (cada estudante traz o próprio arquivo)
- Arquivo de demonstração preparado pelo professor: um UV com problemas reais — islands de tamanhos desproporcionais, desperdício de espaço, distorção visível no Stretch Overlay. Pode ser o mesmo prop da Semana 3, propositalmente mal otimizado, ou um arquivo novo
- Pack Islands nativo do Blender (ferramenta usada nesta semana). O add-on UVPackmaster (versão gratuita), se disponível no laboratório, é retomado como recapitulação de 5 minutos na Semana 6 — não é necessário para esta aula
- Textura de checkerboard (mesma usada nas Semanas 2 e 3)
- Projetor para demonstração e para a crítica informal
- Apostila — Parte II, Cap. 6 — disponibilizada antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Otimizar UV não é estética — é resolução de textura**

Objetivo: criar o entendimento de que a qualidade do layout UV tem impacto direto e mensurável na qualidade final da textura pintada.

**Desenvolvimento:**

Abrir com uma comparação visual: dois screenshots do mesmo asset texturizado — um com UV bem otimizado e outro com UV com texel density inconsistente. Perguntar à turma: *"Vocês conseguem ver a diferença? Por que uma parte do objeto parece borrada e outra parece nítida, se a textura é a mesma?"*

Deixar 2–3 respostas antes de apresentar a causa.

---

**Conteúdo a cobrir:**

**1. Stretch Overlay: ver o que o olho não vê**

O Blender tem um modo de visualização no UV Editor chamado Stretch Overlay (ativado pelo ícone de gradiente na barra do UV Editor). Ele coloriza as faces de acordo com o grau de distorção do UV:

- **Azul** = sem distorção (a face no UV tem a mesma proporção que a face na malha 3D)
- **Verde** = distorção leve, geralmente aceitável
- **Vermelho** = distorção severa — a textura vai aparecer esticada ou amassada nessa região

A causa mais comum de distorção em áreas já com seams é a island mal orientada ou escalonada incorretamente após o Unwrap. Adicionar um seam resolve parte do problema; orientar e escalonar a island corretamente resolve o resto.

**2. Texel density: todos os assets merecem a mesma atenção**

Texel density é a quantidade de pixels de textura por unidade de área do modelo 3D. Uma island grande no UV recebe mais pixels; uma island pequena recebe menos. Se dois assets do mesmo kit tiverem texel density muito diferente, um vai parecer com o dobro da resolução do outro — e o resultado é incoerente visualmente.

O objetivo em um kit modular é que todos os assets que serão vistos à mesma distância no jogo tenham texel density similar.

Como verificar: com checkerboard aplicado, o padrão quadriculado deve ter quadrados de tamanho visual similar em todos os assets quando vistos na mesma escala no Viewport.

**3. Average Islands Scale: normalização em um clique**

No UV Editor, com todas as islands selecionadas, o comando `UV > Average Islands Scale` redimensiona todas as islands para que tenham a mesma densidade de pixels por unidade de superfície. É o ponto de partida de qualquer otimização — normalizar antes de empacotar.

> Importante: Average Islands Scale é calculado em relação à área da face na malha 3D, não ao tamanho aparente no Viewport. Um objeto pequeno vai ter islands menores; um objeto grande vai ter islands maiores — mas a *densidade* será igual.

**4. Pack Islands: aproveitamento automático do espaço UV**

Depois de normalizar, as islands vão estar espalhadas fora do quadrado UV. Pack Islands reorganiza automaticamente todas as islands dentro do quadrado UV (0–1), maximizando o aproveitamento do espaço e respeitando um padding mínimo configurável.

Usar: `UV > Pack Islands` com Margin de 0.003–0.008 dependendo da resolução da textura final (valores maiores para texturas menores). Isso é suficiente para o Asset 01 e o Asset 02 desta semana.

> **Nota:** ferramentas de empacotamento mais sofisticadas, como o add-on UVPackmaster (rotação de islands, formas irregulares, útil para assets com muitas islands orgânicas), não são vistas hoje para não sobrecarregar a mini-aula — elas voltam como recapitulação rápida no início da Semana 6, quando o Asset 01 já estará pronto para receber textura.

**5. O que Pack Islands não resolve**

Pack Islands não corrige distorção — ele apenas reposiciona islands existentes. Se uma island está distorcida, ela vai ser empacotada distorcida. A ordem correta é sempre: corrigir distorção → normalizar → empacotar.

> **Nota do professor:** Esta mini aula é densamente técnica. Se a turma estiver confusa após o ponto 3, pausar e confirmar o entendimento antes de seguir para o 4 e 5. A demonstração vai reforçar os conceitos com visualização ao vivo — não é necessário que tudo seja compreendido apenas com a mini aula.

---

### Demonstração — 20 minutos

**Otimização ao vivo de um UV com problemas reais**

**Setup (2 min):**  
Abrir o arquivo de demonstração com UV propositalmente mal otimizado. Configurar o layout dividido: Viewport 3D à esquerda com checkerboard em Material Preview, UV Editor à direita. Ativar o Stretch Overlay no UV Editor.

**Parte 1 — Diagnóstico com Stretch Overlay (4 min):**

1. Mostrar o Viewport com checkerboard: apontar onde os quadrados estão esticados ou amassados.
2. Mostrar o UV Editor com Stretch Overlay ativo: identificar as áreas vermelhas e correlacionar com as regiões problemáticas no Viewport.
3. Perguntar à turma: *"Antes de qualquer ferramenta de otimização, o que vocês fariam para reduzir esse vermelho?"* — Resposta esperada: adicionar um seam na região distorcida ou reorientar a island.
4. Corrigir uma distorção ao vivo: selecionar a island problemática, reposicioná-la e re-escalonar. Verificar no Stretch Overlay.

**Parte 2 — Average Islands Scale (5 min):**

1. Mostrar o problema de texel density: islands de tamanhos muito diferentes no UV Editor, e no checkerboard o padrão de quadrados com tamanhos visuais diferentes entre partes do objeto.
2. Selecionar todas as islands (`A` no UV Editor).
3. Executar `UV > Average Islands Scale`. Mostrar como as islands se redimensionam.
4. Voltar ao Viewport com checkerboard: os quadrados agora têm tamanho similar em todo o objeto.

**Parte 3 — Pack Islands (5 min):**

1. Com todas as islands selecionadas após o Average Islands Scale, executar `UV > Pack Islands`.
2. Ajustar o Margin (mostrar a diferença entre 0.002 e 0.01 — padding mais largo reduz aproveitamento de espaço mas evita bleeding em mipmaps).
3. Mostrar o resultado: islands compactadas no quadrado UV sem sobreposição.
4. Verificar no Stretch Overlay: a distorção que existia ainda existe — Pack Islands não criou nem eliminou distorção.

**Comparação antes/depois (4 min):**

Usar Ctrl+Z repetidamente para desfazer e refazer o processo, mostrando o UV Editor antes e depois. Perguntar: *"Que porcentagem do espaço UV vocês estimam que estava desperdiçada antes?"* Mostrar no painel de propriedades do UV Editor a métrica de coverage (se disponível no add-on ou visualmente).

> **Nota do professor:** Mantenha o arquivo de demonstração aberto durante o estúdio para referência. Não é necessário demonstrar o UVPackmaster nesta semana — ele será mostrado na recapitulação da Semana 6.

---

### Produção em Estúdio — 50 minutos

**Otimização do UV do Asset 01 + Abertura do UV do Asset 02**

**Consigna entregue verbalmente:**

> *"Vocês receberam feedback na crítica formal da Semana 3. Agora têm dois objetivos neste estúdio: primeiro, otimizar o UV do Asset 01 com as ferramentas que acabamos de ver — corrigir distorção residual, normalizar texel density e empacotar. Segundo, iniciar a abertura do UV do Asset 02, aplicando desde o início o que já sabem sobre seams. O Asset 02 não precisa estar finalizado hoje — mas precisa estar começado."*

**Atividade estruturada:**

**Asset 01 — Otimização (≈30 minutos):**

1. Abrir o arquivo `_v2` da Semana 3.
2. Ativar Stretch Overlay no UV Editor — identificar regiões vermelhas ou laranjas.
3. Corrigir distorções residuais: reposicionar seams se necessário, re-executar Unwrap, reorientar islands problemáticas.
4. Selecionar todas as islands e executar Average Islands Scale.
5. Executar Pack Islands com Margin de 0.004 (para textura final de 1024px) ou 0.008 (para 512px).
6. Verificar resultado final: Stretch Overlay predominantemente azul/verde, quadrados do checkerboard de tamanho uniforme, aproveitamento do espaço UV acima de 70%.
7. Salvar: `[Nome]_Asset01_UV_Semana04.blend`.

**Asset 02 — Abertura inicial (≈20 minutos):**

1. Abrir o arquivo `.blend` do Asset 02 (segundo prop do kit — decidido com antecedência com o professor ou escolhido neste momento se ainda não definido).
2. Em Edit Mode, analisar a geometria e identificar candidatos a seam com os critérios da Semana 3.
3. Marcar seams e executar Unwrap.
4. Aplicar checkerboard e verificar a distorção — corrigir os problemas mais evidentes ainda neste estúdio.
5. Salvar: `[Nome]_Asset02_UV_Semana04_v1.blend`.

**Papel do professor:**

Circular com foco em diagnóstico visual — não corrigir diretamente, mas orientar o olhar:

- *"Você viu o Stretch Overlay? Onde está o vermelho mais intenso? O que acha que está causando isso?"*
- *"Seu checkerboard está com quadrados de tamanho diferente aqui e aqui. Antes de empacotar, você precisa normalizar. Onde está o Average Islands Scale?"*
- *"O Pack Islands foi executado antes do Average Islands Scale? Se sim, o aproveitamento vai parecer bom, mas a density vai estar errada. Desfaz e refaz na ordem certa."*
- *"Para o Asset 02: você já sabe onde colocar o seam antes de começar. Onde você vai esconder a costura nesse objeto?"*

Identificar estudantes cujo Asset 01 ainda tem distorção severa e priorizar atenção neles — o UV do Asset 01 é a base das Semanas 5 e 6.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: comparação entre pares com foco em Stretch Overlay**

Esta é uma crítica informal. O objetivo não é avaliação — é calibrar o olhar da turma e criar consciência coletiva sobre os critérios de qualidade de UV.

**Roteiro:**

1. **(2 min de abertura)** Professor pede que todos abram o Stretch Overlay no UV Editor e o checkerboard no Viewport. *"Hoje a crítica vai ser sobre o que vocês conseguem ver — não sobre o que está escrito no arquivo."*

2. **(12 min — 3 casos comparados)** Professor seleciona 3 UVs para comparação lado a lado (usando projetor ou compartilhamento de tela): um com otimização completa, um com distorção residual, e um com texel density inconsistente.

   Para cada caso, o professor faz uma rodada rápida:
   - *"O que vocês veem no Stretch Overlay?"*
   - *"O padrão do checkerboard está uniforme?"*
   - *"Quanto do espaço UV está sendo aproveitado? Estimem visualmente."*
   
   Sem julgamento ao estudante — o foco é no UV, não na pessoa.

3. **(4 min de padrão coletivo)** Professor aponta o padrão que apareceu na turma e estabelece a meta para o estúdio:
   - *"A maioria dos UVs ainda tem islands pequenas demais em relação ao espaço disponível. Isso é o que vamos resolver nos próximos 60 minutos."*
   - *"Quem já chegou no Stretch Overlay predominantemente azul, avança para o Asset 02 com foco."*

4. **(2 min de conexão com o semestre)** Professor retoma: *"Na Semana 5 vocês vão pintar Material PBR nos UVs que tiverem prontos. Um UV ruim vai aparecer na textura. Um UV bom vai ser invisível — vai ser só o material que o jogador vai ver. Essa é a última semana para corrigir a base."*

---

### Produção em Estúdio — 60 minutos

**Finalização do Asset 01 + Avanço no Asset 02**

**Consigna:**

> *"Sessenta minutos. Dois objetivos: Asset 01 com UV finalizado e otimizado — Stretch Overlay azul/verde, texel density normalizada, empacotado. Asset 02 com seams marcados, Unwrap executado e checkerboard verificado. Entreguem o que tiverem no final deste encontro."*

**Atividade:**

**Asset 01 — Finalização:**

1. Incorporar ajustes identificados na crítica informal.
2. Verificar com Stretch Overlay e checkerboard: Stretch predominantemente azul/verde; quadrados de tamanho uniforme em todo o objeto.
3. Verificar aproveitamento de espaço: estimativa visual acima de 70% do quadrado UV ocupado por islands.
4. Capturar screenshot do UV Editor com Stretch Overlay ativo e do Viewport com checkerboard.
5. Salvar versão final: `[Nome]_Asset01_UV_Semana04_final.blend`.

**Asset 02 — Desenvolvimento:**

1. Retomar o arquivo da v1 do primeiro estúdio.
2. Refinar seams se necessário com base no checkerboard.
3. Executar Average Islands Scale e Pack Islands após corrigir distorção.
4. Capturar screenshot do UV Editor e do Viewport com checkerboard.
5. Salvar: `[Nome]_Asset02_UV_Semana04.blend`.

**Papel do professor:**

- Para estudantes que finalizaram o Asset 01 e avançam bem no Asset 02: *"Seu Asset 02 tem texel density comparável ao Asset 01? Coloca os dois no mesmo arquivo e aplica o checkerboard em ambos ao mesmo tempo — você vai conseguir ver a diferença de tamanho dos quadrados."*
- Para estudantes ainda presos no Asset 01: focar exclusivamente na distorção mais severa (áreas vermelhas) — não tentar resolver tudo, mas chegar em um UV funcional para Semana 5.
- Para quem terminar tudo: *"Escolha um terceiro asset e pense nos seams antes de marcar qualquer um. Me explica sua estratégia de corte antes de começar."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese técnica)** *"Hoje vocês saíram do 'UV que funciona' para o 'UV que está pronto para receber textura'. A diferença não é estética — é técnica: texel density consistente significa que a resolução da textura vai aparecer igual em todos os assets do kit. Isso é o que vai fazer o conjunto parecer profissional."*

2. **(3 min — Reflexão de processo)** Pergunta para 2–3 voluntários: *"Em qual momento do processo de hoje você teve que tomar uma decisão que não era apenas seguir os passos da demonstração?"* O objetivo é identificar os momentos de agência técnica — quando o estudante deixou de executar e começou a decidir.

3. **(3 min — Antecipação da Semana 5)** *"Na semana que vem começa a Unidade II: Physically Based Rendering. Vocês vão aprender o que significa criar um material que simula a física da luz. O UV que vocês entregam hoje é o mapa onde toda essa informação vai morar. Guardem os arquivos com os nomes corretos — vamos continuar com esses mesmos assets."*

4. **(2 min — Confirmação das entregas)** Recapitular as entregas da semana com o arquivo e nomenclatura esperados.

---

## Possíveis Dificuldades

**1. Executar Pack Islands antes de Average Islands Scale**  
É o erro de ordem mais comum desta semana. O Pack Islands vai empacotar com as islands nos tamanhos errados, gerando aproveitamento aparentemente bom mas com texel density inconsistente. O problema só aparece quando o estudante aplica a textura e percebe que uma parte do objeto está com muito mais resolução que outra. Estratégia: reforçar verbalmente a ordem — *"Distorção → Normalização → Empacotamento"* — e escrever no quadro ou projetar durante o estúdio.

**2. Confundir Stretch Overlay com problema de UV vs. problema de geometria**  
Em alguns casos, o vermelho no Stretch Overlay é resultado de geometria ngon (face com mais de 4 vértices) ou face não-planar, não de um problema de seam. O estudante vai tentar adicionar seams sem resultado. Estratégia: pedir que ative a opção de visualização de ngons no Viewport (`Overlay > Geometry > Face Orientation` ou buscar ngons com `Select > All by Trait > Faces by Sides`). Se for geometria, o problema está antes do UV.

**3. Pack Islands não respeitando a orientação das islands**  
O Pack Islands nativo do Blender pode rotacionar islands em ângulos que não correspondem à orientação natural do objeto (ex.: topo de uma caixa rotacionado 45°). Isso não gera distorção, mas pode dificultar a leitura do UV na hora de pintar. Estratégia: na versão nativa, usar a opção "Rotate" desativada se disponível; ou com UVPackmaster, configurar restrição de rotação por múltiplos de 90°. Se nenhuma das opções estiver disponível, orientar a ilha manualmente após o empacotamento.

**4. Asset 02 muito diferente em complexidade do Asset 01**  
Alguns estudantes podem ter escolhido um Asset 02 muito mais complexo, o que pode impedir a conclusão do UV no tempo disponível. Estratégia: na segunda parte do estúdio, orientar o estudante a priorizar seams e Unwrap funcional — a otimização do Asset 02 pode ser concluída no início da Semana 5 como aquecimento, antes de iniciar PBR.

**5. Estudantes que chegam sem o arquivo da Semana 3**  
Pode acontecer esquecimento de salvar ou upload em local errado. Estratégia: preparar um arquivo de fallback com o mesmo prop da demonstração já com UV aberto (Semana 3-nível), para que o estudante não perca o estúdio inteiro. Registrar a ausência do arquivo para C1.

**6. Dificuldade em estimar "70% de aproveitamento" visualmente**  
Muitos estudantes não têm referência intuitiva de quanto espaço está sendo aproveitado. Estratégia: mostrar na demonstração três exemplos visuais — UV com ~40% de aproveitamento, ~70% e ~90% — e nomear qualitativamente: "desperdício", "funcional", "otimizado". Criar âncoras visuais concretas em vez de trabalhar só com percentual.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe o que fazer com o Stretch Overlay vermelho | Pedir que identifique a face vermelha no UV Editor e a correspondente na malha 3D. Perguntar: *"Essa face é curva ou plana? Se for plana e ainda estiver vermelha, o seam provavelmente está impedindo ela de abrir bem. Se for curva, um seam adicional nessa área pode ajudar."* |
| Islands de tamanhos muito diferentes após Average Islands Scale | Verificar se o Average Islands Scale foi feito com todas as islands selecionadas. Se sim, explicar que objetos com faces muito diferentes em área de superfície vão ter islands de tamanhos diferentes — isso é correto. O que o Average garante é *densidade*, não *tamanho absoluto*. |
| Estudante satisfeito com UV com distorção evidente | Pedir que aproxime a câmera no Viewport e observe o checkerboard de perto: *"Esses quadrados estão esticados. Quando você pintar uma madeira com veio horizontal aqui, o veio vai aparecer inclinado. Você está satisfeito com isso para o seu projeto?"* |
| Asset 02 com seams mal posicionados desde o início | Pedir que desfaça tudo (Clear Seams) e faça uma análise em voz alta: *"Diz pra mim qual é a frente desse objeto, qual é o fundo, e onde o jogador nunca vai olhar. Vamos marcar seams só nessas arestas primeiro."* |
| Estudante rápido com ambos os UVs otimizados | Propor desafio: combinar os dois assets em um único arquivo `.blend`, selecionar todas as islands de ambos e fazer um Pack Islands conjunto — simulando o início de um Texture Atlas (tema da Semana 13). |
| Turma confusa sobre a diferença entre padding e margin | Usar analogia física: *"Margin é a calçada entre duas casas. Se a calçada for muito larga, você desperdiça terreno. Se for muito estreita, na hora da chuva (mipmap) a água escorre de uma casa para outra (bleeding). Para texturas de 1024px, 4px de calçada já é suficiente."* |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Stretch Overlay do Asset 01 predominantemente azul/verde | C3 — UV Mapping | Screenshot do UV Editor com Stretch Overlay ativo — avaliar proporção de vermelho/laranja residual |
| Padrão de checkerboard uniforme em todo o Asset 01 | C3 — UV Mapping | Quadrados de tamanho similar em toda a superfície do objeto no Viewport com Material Preview |
| Aproveitamento do espaço UV acima de 70% | C3 — UV Mapping | Análise visual do screenshot do UV Editor: proporção do quadrado UV ocupada por islands |
| Asset 02 com Unwrap funcional iniciado | C3 — UV Mapping | Arquivo `.blend` com UV aberto, islands dentro do espaço UV, sem sobreposição evidente |
| Arquivo nomeado corretamente e versionado | C1 — Processo de Projeto | Existência dos arquivos com nomenclatura `_Semana04` e distinção entre Asset 01 e Asset 02 |
| Feedback oferecido na crítica informal com observação técnica concreta | C10 — Participação | Qualidade do comentário: usa vocabulário técnico (distorção, texel density, island) e identifica algo específico, não genérico |

---

## Entrega da Semana 4

| Entrega | Formato | Prazo |
|---|---|---|
| Asset 01 do Kit Modular com UV otimizado (Stretch Overlay e texel density normalizados, empacotado) | `.blend` com sufixo `_Semana04_final` | Até o fim do segundo encontro |
| Asset 02 com UV aberto (seams, Unwrap e checkerboard verificado) | `.blend` com sufixo `_Semana04` | Até o fim do segundo encontro |
| Screenshots de ambos os assets: UV Editor com Stretch Overlay ativo + Viewport com checkerboard | PNG ou JPG (4 imagens no total — 2 por asset) | Até o fim do segundo encontro |

> **Nota:** A crítica desta semana é informal. Não há Ficha de Crítica Formal nem Autoavaliação obrigatória. O registro avaliativo de C3 para a Semana 4 se dará via análise dos arquivos entregues. O professor pode fazer observações qualitativas no diário de classe para subsidiar o feedback da próxima crítica formal (Semana 5).

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 4 | 2026*
