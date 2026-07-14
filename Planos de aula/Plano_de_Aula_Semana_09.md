# Plano de Aula — Semana 9
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** III — Pintura Digital e Bake  
**Tema:** Texturização artística: desgaste, sujeira e detalhes hand-painted no 3D Coat  
**Apostila:** Parte IV, Cap. 14 — Pintura Digital para Jogos (aplicada a texturas; ferramentas de pintura no 3D Coat)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔵 Informal — Crítica circulante no segundo encontro

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 texturizado no 3D Coat (arquivo `.3b` salvo): canais Color, Roughness e Metallic com pelo menos uma camada base e uma camada de variação em cada — Semana 8
- Mapas PBR exportados (Albedo, Roughness, Metallic em PNG 1024×1024 ou superior) e conectados corretamente no Blender — Semana 8
- Material no Blender com Color Space Non-Color aplicado nos mapas de dados — Semana 8
- Moodboard atualizado com referências do tema do kit — Semana 1 (atualização contínua)

> **Nota de transição:** A Semana 8 introduziu o 3D Coat e estabeleceu o fluxo básico: importar, pintar por canal, exportar, conectar. Os estudantes já têm os três canais fundamentais com camadas base. Esta semana move o foco do **estrutural** para o **narrativo**: o que diferencia uma textura funcional de uma textura com caráter? A resposta é desgaste intencional, sujeira com lógica e variação de cor que conta a história do objeto. O conteúdo novo não é uma nova ferramenta — é uma forma diferente de usar o 3D Coat, agora com propósito artístico claro.

> **Atenção ao moodboard:** Antes da aula, lembrar os estudantes de revisitar o moodboard do kit. A pergunta central da semana — *"qual é a história desse objeto?"* — só pode ser respondida se o estudante souber o contexto do universo do kit. Um objeto medieval envelhecido tem um tipo de desgaste. Um objeto sci-fi em uso ativo tem outro. A referência visual é a bússola da pintura.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Distinguir texturização fotorrealista de texturização estilizada e identificar qual abordagem é mais coerente com o tema do seu kit.
2. Identificar e aplicar os três tipos canônicos de detalhe de superfície: **edge wear** (desgaste em arestas), **dirt/grime** (sujeira acumulada em cavidades) e **scratches** (riscos e arranhões por fricção).
3. Organizar camadas no 3D Coat por tipo de detalhe, mantendo separação entre a base e cada camada de informação adicional.
4. Aplicar a lógica de uso para determinar **onde** pintar desgaste: arestas expostas ao contato, superfícies inferiores e côncavas que acumulam sujeira, faces superiores sujeitas a impacto.
5. Avaliar a leitura do material à distância de uso (não apenas em close-up), verificando se o desgaste contribui para a silhueta e legibilidade do asset.
6. Exportar e atualizar os mapas no Blender com os novos detalhes pintados, e capturar um render comparativo antes/depois.

---

## Critérios observados nesta semana

> ⚠️ **Semana sem crítica formal — nenhuma nota é atribuída.** O professor observa e registra evidências nos critérios abaixo para calibrar a avaliação da CF4 (sem 11). O estudante recebe feedback oral durante o estúdio.

| Critério | O que observar |
|---|---|
| C1 — Processo de Projeto | Registro do processo: screenshots comparativos antes/depois, nomenclatura das camadas no 3D Coat, versão salva com sufixo `_S09` |
| C2 — Direção Artística | O desgaste é coerente com o tema do kit? A história do objeto está alinhada com a proposta estética do moodboard? |
| C5 — Texturização | Qualidade e intenção das camadas de detalhe: edge wear nas arestas corretas, sujeira com lógica gravitacional e de uso, scratches com direção e intensidade plausíveis |
| C10 — Participação (CC) | Qualidade do feedback oferecido na crítica informal: é observável e específico? Conecta desgaste à lógica de uso do objeto? |

> **Progressão do PA — entre CF3 e CF4:** Esta semana fica entre a CF3 (sem 8) e a CF4 (sem 11). C5 (Texturização) é o critério central — é onde o trabalho desta semana mais impacta a próxima avaliação formal. A distinção entre nível 2 ("desgaste uniforme e irreal") e nível 4 ("camadas com narrativa de uso perceptível") é exatamente o que esta aula ensina. O professor deve manter registro de observação de C5 durante o estúdio para calibrar a CF4.

---

## Recursos necessários

- Computadores com 3D Coat instalado (versão 2023 ou superior)
- Computadores com Blender instalado (3.x ou 4.x)
- Arquivos `.3b` do Asset 01 de cada estudante (3D Coat — Semana 8)
- Arquivo de demonstração do professor: asset com textura base já pintada (Color + Roughness + Metallic com Fill simples), pronto para receber detalhes
- Projetor para demonstração e para a crítica informal
- Coleção de referências visuais de desgaste organizadas por tema (Medieval, Sci-Fi, Pós-apocalíptico, etc.) — exibir no projetor durante o estúdio como apoio visual
- Apostila — Parte IV, Cap. 14 — disponibilizada antes da aula

> **Preparação do arquivo de demonstração:** O asset usado na demonstração deve ter as três camadas base já pintadas (sem detalhes), exatamente no estado em que os estudantes chegam com o Asset 01. Isso garante que a demonstração parte do mesmo ponto de partida que o estúdio — e que o antes/depois seja imediatamente comparável.

> **Sobre coleção de referências:** Preparar uma pasta com 10–15 imagens de superfícies desgastadas coerentes com os temas dos kits da turma. Exibir como slideshow no projetor durante os momentos de produção — funciona como referência visual passiva que inspira sem interromper o fluxo de trabalho.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Da textura funcional à textura com história**

Objetivo: apresentar a distinção entre texturização fotorrealista e estilizada, e introduzir a lógica de desgaste como ferramenta narrativa — não como decoração. A mini aula não ensina ferramentas novas: ensina intenção. As ferramentas já foram apresentadas na Semana 8.

**Abertura:**

Exibir no projetor dois renders lado a lado do mesmo asset: um com apenas as três camadas base da Semana 8 (cor flat, roughness uniforme), outro com desgaste, sujeira e scratches aplicados. Perguntar à turma: *"Esses dois assets têm a mesma malha, o mesmo UV, o mesmo número de polígonos. O que é diferente? O que conta de diferente sobre eles?"*

Deixar 2–3 respostas. Direcionar para a ideia central: a textura com desgaste narra o tempo de uso do objeto. Ela responde à pergunta: *"O que aconteceu com esse objeto antes de ele aparecer no frame?"*

---

**Conteúdo a cobrir:**

**1. Fotorrealista vs. estilizado — não é uma escolha de qualidade, é uma escolha de intenção**

Texturização fotorrealista busca a aparência de materiais reais sob condições de luz física. Texturização estilizada amplifica certas qualidades visuais para criar impacto à distância ou identidade artística reconhecível.

Ambas usam as mesmas ferramentas e os mesmos canais PBR. A diferença está na intensidade, na exageração e na prioridade de informação.

Perguntar à turma: *"O tema do seu kit pede realismo ou estilo? Um kit Medieval pode ser ambos — depende da decisão artística que você tomou na Semana 1. Olhem o moodboard de vocês. As referências são fotográficas ou artísticas?"*

Não há resposta certa — mas a escolha deve ser deliberada e consistente em todo o kit.

**2. Os três tipos de detalhe de superfície**

Apresentar como uma taxonomia simples que organiza o processo de pintura:

**Edge Wear (desgaste de aresta):** acontece onde o material é exposto ao contato físico — bordas, projeções, pontos de manipulação. É o lugar onde tinta descasca, metal polido aparece sob ferrugem, pedra lascada expõe material interno. No 3D Coat: canal Roughness (arestas ficam mais polidas = roughness menor) e canal Color (cor interna exposta é diferente da cor de superfície). *Regra de ouro: quanto mais projetado e exposto, mais desgastado.*

**Dirt / Grime (sujeira e acúmulo):** acontece onde gravitação e abrigo convergem — cantos inferiores, encaixes entre peças, fendas, reentrâncias. Pó, fuligem, musgo, óleo acumulam em lugares protegidos onde o vento não chega e a água fica parada. No 3D Coat: canal Color (tom mais escuro ou acinzentado), canal Roughness (sujeira = muito rugosa). *Regra de ouro: quanto mais baixo e protegido, mais sujo.*

**Scratches (riscos e arranhões):** acontecem pela direção de uso — arrastar, esvaziar, empurrar. Têm direção e comprimento que revelam como o objeto foi usado. No 3D Coat: canal Color (exposição de material base) + canal Roughness (risco = alteração de micro-superfície). *Regra de ouro: os riscos seguem a direção do movimento do usuário.*

**3. Organização de camadas por tipo de detalhe**

Cada tipo de detalhe deve ter sua própria camada (ou grupo de camadas) no 3D Coat. Isso permite:
- Ajustar a intensidade de cada detalhe sem retrabalhar os outros
- Comparar o antes/depois desativando camadas individualmente
- Manter o arquivo legível para revisão futura

Nomenclatura recomendada para esta semana:
```
Base_Color         ← Fill com cor base
Variacao_Cor       ← variação de tom da Semana 8
EdgeWear_Color     ← cor interna exposta nas arestas
Dirt_Color         ← acúmulo de sujeira em cavidades

Base_Roughness     ← Fill base
EdgeWear_Rough     ← arestas mais polidas
Dirt_Rough         ← cavidades mais rugosas
Scratches_Rough    ← micro-rugosidade dos riscos
```

*"Quem tem as camadas assim nomeadas consegue ir direto em qualquer detalhe para ajustar. Quem tem tudo numa camada só vai retrabalhar o asset do zero na próxima crítica."*

**4. A leitura à distância de uso**

Desgaste deve funcionar na distância em que o jogador vê o asset — não apenas em close-up de render de portfólio. Em jogos, assets de ambiente são vistos a 3–10 metros. Micro-detalhes que só aparecem a 30cm no 3D Coat Render Room são invisíveis no jogo.

Regra prática: se o edge wear não aparece no viewport do Blender com câmera a 5 metros de distância, está fraco demais. Se o asset parece "coberto de arranhões" a essa distância, está forte demais. O objetivo é que o desgaste **leia à distância** sem ser caricato.

> **Nota do professor:** Esta mini aula é mais uma aula de visão e intenção do que de procedimento técnico. Resistir à tentação de explicar ferramentas — as ferramentas serão mostradas na demonstração. O objetivo aqui é que o estudante chegue no estúdio com uma pergunta clara em mente: *"Qual é a história do meu objeto?"*

---

### Demonstração — 20 minutos

**Pintura de edge wear, dirt e scratches no 3D Coat**

**Setup (1 min):**  
Abrir o 3D Coat com o asset de demonstração já preparado: malha com UV, três canais base pintados (Color, Roughness, Metallic com Fill uniforme). Ter o Render Room disponível para comparações rápidas ao longo da demonstração.

**Percurso da demonstração:**

**Passo 1 — Edge Wear no canal Color (5 min):**
1. No painel Layers, criar nova camada acima da `Variacao_Cor`: nomear `EdgeWear_Color`.
2. Modo de mistura: **Normal**. Opacidade: 70%.
3. Ferramenta: **Brush**. Tamanho: pequeno (3–5% do tamanho da malha). Opacidade: 80–100%.
4. Cor escolhida: a cor "interna" do material — para pedra: tom mais claro e amarelado (material sem oxidação superficial); para metal: tom de metal limpo sob ferrugem.
5. Pintar as arestas superiores e projeções do asset com traços curtos, concentrados, não uniformes. Variar a espessura do traço para evitar aparência mecânica.
6. Abrir o Render Room: mostrar como as arestas agora "brilham" com cor diferente — o objeto começa a ter profundidade.

**Passo 2 — Edge Wear no canal Roughness (3 min):**
1. Mudar canal ativo para **Roughness**.
2. Nova camada: `EdgeWear_Rough`. Modo: Normal. Opacidade: 90%.
3. Com brush das mesmas arestas: pintar com **cor mais escura** (valor de roughness menor = mais polido = mais reflexivo).
4. Percurso de pintura coincide com o `EdgeWear_Color` — as duas camadas constroem juntas a leitura de "material exposto pelo uso".
5. Mostrar no Render Room: as arestas agora têm brilho sutil diferente do corpo principal. *"É o que acontece com metal enferrujado quando você bate — aparece o metal limpo embaixo, que é mais reflexivo do que a ferrugem."*

**Passo 3 — Dirt no canal Color (5 min):**
1. Canal ativo: **Color**.
2. Nova camada: `Dirt_Color`. Modo: **Multiply**. Opacidade: 60–70%.
3. Brush de tamanho maior (15–25% da malha), opacidade muito baixa (15–25%).
4. Cor: cinza escuro acastanhado (pó + terra).
5. Pintar nas **áreas côncavas e inferiores**: cantos, encaixes entre peças, face inferior, reentrâncias. Construir a sujeira em passadas suaves e acumulativas — não em uma pincelada única.
6. *"Repara que o brush de opacidade baixa me deixa construir o acúmulo de forma gradual. A sujeira não é um evento — é um processo. A pintura também deve ser."*

**Passo 4 — Dirt no canal Roughness (3 min):**
1. Canal ativo: **Roughness**.
2. Nova camada: `Dirt_Rough`. Modo: **Multiply**. Opacidade: 70%.
3. Brush de tamanho médio, opacidade 30–40%.
4. Pintar nas mesmas áreas do `Dirt_Color` com **cor mais clara** (roughness maior = mais rugoso = sujeira e pó).
5. Mostrar no Render Room: as áreas sujas agora são mais matte do que a superfície principal. *"Sujeira real absorve luz — ela é quase sempre mais rugosa do que o material de base."*

**Passo 5 — Verificação à distância (2 min):**
1. No Render Room: afastar a câmera para simular a distância de jogo.
2. Perguntar para a turma: *"Vocês conseguem ler o edge wear daqui? E a sujeira?"*
3. Mostrar que se a resposta for "não" para o edge wear: aumentar a opacidade da camada ou o contraste da cor. Se a resposta for "não" para a sujeira em cavidades: verificar se o modo Multiply está ativo.
4. *"A demonstração não termina quando você acha bonito no Render Room de perto. Termina quando você aprova a distância de uso."*

> **Nota do professor:** Não é necessário demonstrar scratches nesta sessão — deixar para o estúdio como desafio para estudantes avançados. O foco da demonstração são edge wear e dirt, que são os dois tipos de detalhe mais difíceis de acertar a lógica. Scratches têm lógica mais simples de inferir.

---

### Produção em Estúdio — 50 minutos

**Adição de camadas de detalhe ao Asset 01**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com um objetivo: adicionar desgaste com história ao Asset 01. Antes de abrir o 3D Coat, olhem o moodboard e respondam mentalmente: 'O que aconteceu com esse objeto? Ele foi muito usado? Abandonado? Ainda está em uso ativo?' A resposta vai ditar onde vocês pintam. Quando terminar, tirem um screenshot do Render Room com a câmera longe — se o desgaste aparecer, está no caminho certo. Se não aparecer, está fraco demais. Não façam desgaste bonito: façam desgaste verdadeiro."*

**Atividade estruturada:**

**Etapa 1 — Revisão do arquivo da Semana 8 (≈5 min):**
1. Abrir o arquivo `.3b` do Asset 01 salvo na Semana 8.
2. Verificar as camadas existentes: Color (base + variação), Roughness (base + desgaste inicial), Metallic (base).
3. Abrir o Render Room por 1 minuto: avaliar o estado atual do asset. Identificar mentalmente: *onde o uso deixaria marcas?*
4. Renomear ou reorganizar as camadas existentes para seguir a nomenclatura da mini aula (se necessário).

**Etapa 2 — Edge Wear (≈20 min):**

No canal **Color**:
1. Nova camada `EdgeWear_Color` acima da `Variacao_Cor`. Modo: Normal. Opacidade: 70%.
2. Brush pequeno, opacidade alta. Cor interna do material (ver referência no moodboard).
3. Pintar arestas superiores, projeções, pontos de contato e manipulação. Não pintar toda aresta — concentrar nas mais expostas.
4. Verificar no Render Room: as arestas têm leitura visual diferente do corpo principal?

No canal **Roughness**:
1. Nova camada `EdgeWear_Rough`. Modo: Normal. Opacidade: 90%.
2. Brush nas mesmas arestas com cor mais escura (roughness menor).
3. Verificar: arestas refletem levemente mais luz do que o corpo principal?

**Etapa 3 — Dirt / Grime (≈20 min):**

No canal **Color**:
1. Nova camada `Dirt_Color`. Modo: Multiply. Opacidade: 60%.
2. Brush grande, opacidade baixa (15–20%). Pintar em passadas acumulativas.
3. Focar em: face inferior, cantos, encaixes, reentrâncias, fendas.
4. Cor de sujeira coerente com o tema: pó terroso para Medieval/Fantasia, graxa/fuligem para Sci-Fi/Industrial, ferrugem+terra para Pós-apocalíptico.

No canal **Roughness**:
1. Nova camada `Dirt_Rough`. Modo: Multiply. Opacidade: 70%.
2. Pintar nas mesmas áreas com valor de roughness maior (cor mais clara).

**Etapa 4 — Verificação e registro (≈5 min):**
1. Render Room: câmera afastada para distância de uso. Avaliar a leitura.
2. Screenshot do Render Room com câmera próxima (close-up de detalhe).
3. Screenshot do Render Room com câmera afastada (distância de uso).
4. Salvar: `[Nome]_Asset01_S09.3b`.

**Papel do professor:**

Circular verificando três pontos em cada estação:

- **A lógica de uso está presente?** Se o estudante está pintando desgaste nas mesmas quantidades em todas as arestas e superfícies, o desgaste é decorativo, não narrativo. Perguntar: *"Qual parte desse objeto o usuário toca? Qual parte bate em outra superfície quando é posta no chão?"*
- **O modo de mistura do Dirt está correto?** O erro mais comum é usar modo Normal para o Dirt_Color, o que cria manchas opacas em vez de acúmulo sutil. Verificar que o modo é Multiply.
- **A leitura à distância funciona?** Pedir ao estudante que afaste a câmera no Render Room antes de avançar. Se o edge wear desaparece completamente, precisar reforçar.

Perguntas de mediação circulante:
- *"Se você tivesse que dar um nome para a história desse objeto — 'foi usado por anos e nunca lavado', 'foi deixado ao relento por décadas', 'ainda está em uso ativo' — qual seria? A textura está narrando essa história?"*
- *"Olha o desgaste de um colega que tem um kit parecido com o seu. O que ele fez que você ainda não fez? O que você fez que ele ainda não fez?"*
- *"A sujeira está só nas arestas ou também nos cantos e partes inferiores? Sujeira real não sobe — ela cai e acumula."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: Walk-around + crítica direcionada**

Esta é uma crítica 🔵 Informal. Não há ficha formal, não há apresentação estruturada individual. O objetivo é expor o trabalho em progresso, receber feedback externo e ajustar antes do segundo bloco de estúdio.

**Protocolo:**

**Preparação (2 min antes do início):**
- Cada estudante exibe o Asset 01 no Render Room do 3D Coat ou no viewport do Blender com os mapas conectados.
- Preparar dois screenshots visíveis: o estado do asset ao final da Semana 8 (antes) e o estado atual (depois).

**Abertura (2 min):**
*"Vamos fazer um walk-around rápido. Cada um tem 30 segundos para me dizer: qual tipo de desgaste você adicionou? Edge wear, dirt, scratches — ou os três? E qual é a história do objeto? Não me mostre a técnica — me conta a história."*

**Walk-around (15 min):**

O professor circula junto com a turma (ou conduz a turma de monitor em monitor). Para cada asset, a turma observa por 30–45 segundos e um ou dois colegas oferecem feedback verbal. O professor complementa com uma pergunta direcionada.

Perguntas-modelo do professor durante o walk-around:
- *"Olhando de longe: o edge wear aparece? Se não aparece, o que vocês fariam para reforçar?"*
- *"A sujeira está onde a gravidade depositaria ela? Ou está distribuída uniformemente?"*
- *"Compara o antes e o depois. O que mudou de mais significativo? O que ainda está igual?"*
- *"O desgaste desse asset combina com o desgaste dos outros assets do kit? Ou esse parece de uma época diferente?"*

Identificar e destacar para a turma: um ou dois exemplos de edge wear com lógica de uso clara, e um ou dois exemplos de Dirt com modo de mistura e lógica gravitacional bem aplicados. Tornar visíveis os bons exemplos — não para criar ranking, mas para materializar o que "nível 4" parece na prática.

**Síntese (3 min):**
*"O que a turma está acertando: [X]. O que ainda precisa de atenção: [Y]. Nos próximos 60 minutos, quero que cada um refine ao menos uma coisa que os colegas apontaram. Não é hora de adicionar mais coisa — é hora de intensificar o que já existe ou corrigir o que está errado na lógica."*

---

### Produção em Estúdio — 60 minutos

**Refinamento, scratches e exportação**

**Consigna:**

> *"Sessenta minutos divididos assim: 30 minutos para refinamento e adição de scratches; 15 minutos para exportação e atualização do Blender; 15 minutos livres para iniciar o Asset 02 com a mesma lógica. Quem tiver refinado o Asset 01 e exportado com qualidade, avança para o Asset 02. Quem ainda está construindo a lógica de desgaste fica no Asset 01."*

**Atividade estruturada:**

**Bloco 1 — Refinamento com base no feedback da crítica (≈15 min):**

Para cada ponto levantado na crítica informal:
1. Identificar a camada responsável pelo problema.
2. Ajustar: aumentar opacidade, corrigir modo de mistura, reforçar ou suavizar a pintura.
3. Verificar no Render Room à distância de uso após cada ajuste.

Prioridade de refinamento (por ordem de impacto visual):
- Reforço do edge wear se não aparece à distância
- Correção do Dirt se não está nos locais corretos (gravitacional e protegido)
- Ajuste de Roughness se não há diferenciação visual entre zonas

**Bloco 2 — Adição de scratches (≈15 min):**

Para estudantes que completaram edge wear e dirt com lógica clara:

No canal **Roughness**:
1. Nova camada: `Scratches_Rough`. Modo: Normal. Opacidade: 80%.
2. Brush muito pequeno e comprido, opacidade alta.
3. Pintar traços **com direção coerente com o uso**: horizontal se o objeto é deslizado em superfícies, vertical se é apoiado contra paredes, diagonal se é carregado.
4. Não cobrir toda a superfície — concentrar em 20–30% das faces expostas.

No canal **Color** (opcional):
1. Nova camada: `Scratches_Color`. Modo: Normal. Opacidade: 40–50%.
2. Cor levemente diferente da base: o material abaixo da superfície exposto pelo risco.
3. Pintar apenas nos riscos maiores — micro-riscos podem ficar só no Roughness.

**Bloco 3 — Exportação e atualização no Blender (≈15 min):**
1. No 3D Coat: `File → Export Textures`.
2. Exportar Albedo (Color), Roughness, Metallic.
3. Pasta de destino: `[Nome]_Asset01_Mapas_S09/` (nova pasta — preservar a da Semana 8 para comparação).
4. Abrir o Blender com o material da Semana 8.
5. Nos nós `Image Texture`: substituir os PNGs da S08 pelos da S09 (`Reload` ou relinkar os arquivos).
6. No viewport Rendered: verificar que as atualizações aparecem.
7. Capturar render comparativo: viewport com material S08 e viewport com material S09, lado a lado (screenshot ou render estático).
8. Salvar: `[Nome]_Asset01_3DCoat_S09.blend`.

**Bloco 4 — Início do Asset 02 no 3D Coat (≈15 min, se houver tempo):**

Para estudantes que completaram o fluxo do Asset 01:
1. Exportar Asset 02 do Blender (ou usar o exportado na S08 se já existe).
2. Importar no 3D Coat: `File → Import for Per-Pixel Painting`. Resolução: 1024×1024.
3. Pintar ao menos as camadas base dos três canais (Color, Roughness, Metallic — Fill).
4. Se houver tempo adicional: iniciar edge wear.
5. Salvar: `[Nome]_Asset02_3DCoat_S09.3b`.

**Papel do professor:**

- Para estudantes com edge wear muito uniforme (todas as arestas com mesmo valor): *"Qual aresta desse objeto bate no chão quando ele é largado? Essa é a que tem mais desgaste. Qual fica no topo e raramente toca em nada? Essa tem pouco ou nenhum desgaste. A intensidade de edge wear não é uniforme — é proporcional à exposição ao contato."*
- Para estudantes com Dirt no lugar errado (superfícies superiores, faces mais expostas): *"Sujeira sobe? Ou cai? Onde você acumularia pó e terra numa mesa de verdade? Agora pensa no seu objeto. Mesmo princípio."*
- Para estudantes avançados com tempo sobrando: *"Você pode criar uma variação de cor no canal Color que simula umidade — uma segunda camada de Dirt com cor levemente azulada nas partes mais côncavas e protegidas, modo Overlay, opacidade 20%. Isso dá a impressão de umidade acumulada. Testa e vê se faz sentido para o seu tema."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese da semana)**
*"Hoje vocês passaram de 'textura com canais corretos' para 'textura com história'. Essa é a diferença entre um asset funcional e um asset que comunica algo. Edge wear, dirt, scratches — esses não são detalhes decorativos. São respostas às perguntas: 'Quem usou esse objeto? Como? Por quanto tempo?' Quando vocês sabem responder isso, o desgaste aparece nos lugares certos automaticamente."*

2. **(3 min — Reflexão de processo)**
Pergunta aberta para a turma: *"Qual foi o momento em que vocês mais hesitaram hoje? Quando não sabiam onde pintar? Quando o desgaste não aparecia como esperado? O que vocês fizeram para resolver?"*

Deixar 2–3 respostas. O objetivo não é validar as soluções — é tornar visível o processo de decisão. Em SBL, o obstáculo e a resposta ao obstáculo são tão pedagógicos quanto o resultado.

3. **(3 min — Antecipação da Semana 10)**
*"Na semana que vem: stencils. Vocês vão aprender a usar máscaras para aplicar padrões específicos com precisão — rachaduras em pedra, símbolos entalhados, corrosão química, grafites. Stencils permitem detalhe que pintura livre não consegue com facilidade. Para chegar preparado: pensem em que tipo de detalhe específico o tema do kit pede que não dá para pintar à mão com naturalidade. Esse é o candidato perfeito para stencil."*

4. **(2 min — Confirmação das entregas)**
Recapitular as entregas com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Edge wear aplicado em todas as arestas igualmente — desgaste sem lógica de uso**
O estudante pinta todas as arestas com a mesma intensidade, criando um efeito "contorno" uniforme que parece gerado por filtro, não por uso real. O resultado tem aparência cartoon involuntária. Estratégia: pedir ao estudante que identifique verbalmente as duas ou três arestas mais expostas do asset *antes* de começar a pintar. Pintar primeiro essas arestas com intensidade alta, depois as demais com intensidade progressivamente menor. A assimetria é o que torna o edge wear crível.

**2. Sujeira pintada com modo Normal em vez de Multiply — manchas opacas em vez de acúmulo**
Acontece quando o estudante não verifica o modo de mistura da camada de Dirt. O resultado é uma camada de cor uniforme e opaca que cobre a textura base em vez de escurecê-la sutilmente. O Render Room mostra o asset com manchas de cor plana desconectadas da textura de base. Estratégia: verificar o modo da camada antes de pintar qualquer detalhe. O Multiply escurece o que está abaixo sem apagar — é o comportamento correto para sujeira acumulada.

**3. Desgaste invisível à distância de uso**
Detalhes pintados com opacidade muito baixa ou tamanho de brush muito pequeno desaparecem quando a câmera se afasta. O close-up no Render Room parece rico; a distância de jogo parece igual à Semana 8. Estratégia: estabelecer o hábito de verificar a distância no Render Room antes de declarar a camada "pronta". Se o detalhe não aparece a 5 metros de distância simulada, aumentar contraste ou opacidade antes de avançar.

**4. Direção dos scratches sem lógica de uso**
Riscos pintados em todas as direções simultaneamente criam ruído visual sem narrativa. Estratégia: perguntar *"Como esse objeto é movimentado? Em que direção ele desliza ou bate?"* Os riscos devem ser consistentes em direção em cada face do asset — faces horizontais têm riscos de deslizamento, faces verticais têm riscos de impacto ou fricção de passagem.

**5. Comparativo antes/depois sem diferença visível**
Se o estudante trabalhou com opacidades muito baixas em todas as camadas, o render da S09 parece idêntico ao da S08. O asset não evoluiu visivelmente. Estratégia: o professor deve identificar isso durante a crítica informal e redirecionar antes do segundo estúdio. Pedir que o estudante desative todas as camadas novas e compare: *"Você vê diferença? Não? Então as camadas não têm intensidade suficiente."* Intensificar primeiro o edge wear (aumento de opacidade) antes de avançar para outros detalhes.

**6. Asset 01 não está disponível ou foi perdido**
Estudante que não salvou corretamente o arquivo `.3b` na Semana 8 ou não tem acesso ao computador em que trabalhou. Estratégia: usar o arquivo exportado de Blender (`.obj` ou `.fbx`) para reimportar no 3D Coat e iniciar novamente. O estudante perde o trabalho das camadas base da S08, mas pode refazê-las em 10–15 minutos com o fluxo já aprendido, e então avançar para os detalhes desta semana. Usar o tempo do primeiro estúdio para reconstruir o base.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não sabe onde pintar o desgaste | Pedir que descreva verbalmente a "vida" do objeto: *"Conta a história de como esse objeto chegou até aqui. Quem o usou? Como? Durante quanto tempo?"* A narrativa verbal antecede e orienta a pintura. Só depois de ter a história em palavras, o estudante abre o brush. |
| Estudante com edge wear cartoon (muito forte, uniforme) | *"Desativa a camada de EdgeWear_Color por 10 segundos. Olha o asset sem ela. Agora reativa. A diferença é muito drástica? Se for, diminui a opacidade da camada — não refaz do zero."* Ensinar a controlar via opacidade de camada, não via retrabalho de pintura. |
| Estudante satisfeito com o resultado mas que não cresceu visualmente desde a S08 | Exibir o antes (S08) e o depois (S09) lado a lado no projetor: *"Qual informação nova a textura tem agora? Se eu mostrar para alguém sem dizer qual é a S08 e qual é a S09, eles conseguem identificar? Se não conseguirem, a semana não adicionou nada."* |
| Estudante tentando adicionar muitos tipos de detalhe ao mesmo tempo | *"Para. Termina o edge wear antes de abrir qualquer outra camada. Um detalhe de cada vez, com lógica, é melhor do que quatro detalhes ao mesmo tempo sem lógica. Quando o edge wear estiver aprovado no Render Room a distância, aí você abre o Dirt."* |
| Estudante com dificuldade de dar feedback na crítica informal | Fornecer estrutura: *"Para dar feedback, usa essa frase: 'Eu vejo [descrição do que está acontecendo na textura]. O que eu me pergunto é [pergunta sobre a lógica de uso]. Uma possibilidade seria [sugestão concreta]'."* O modelo de frase reduz o bloqueio de quem não sabe por onde começar. |
| Estudante avançado que terminou o Asset 01 com qualidade | Propor exploração de variação de cor com umidade: segunda camada de Dirt com azul-acinzentado frio, modo Overlay, opacidade 15–20% em cavidades profundas. Ou: iniciar o Asset 02 com a mesma lógica, aplicando edge wear e dirt desde o começo, sem fazer a base "limpa" da S08 primeiro. |
| Estudante com kits de estilo mais artístico (cartoon/estilizado) que questiona se o edge wear "realista" faz sentido | Validar a dúvida: *"Para um kit estilizado, o edge wear pode ser mais exagerado, mais colorido e mais uniforme em intensidade — porque a leitura à distância é ainda mais importante. Um kit cartoon com arestas highlights brancos é edge wear estilizado. A lógica de onde pintar é a mesma; o quanto você exagera é uma decisão artística que vem do moodboard."* |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Camadas de EdgeWear_Color e EdgeWear_Rough presentes no arquivo `.3b` com intensidade visível à distância de uso no Render Room | C5 — Texturização | As camadas existem e têm impacto visual verificável? O edge wear está nas arestas mais expostas, não em todas igualmente? |
| Camadas de Dirt_Color e Dirt_Rough com modo Multiply e lógica gravitacional (partes inferiores e côncavas) | C5 — Texturização | O Dirt está nos locais corretos (partes baixas, côncavas, protegidas)? O modo Multiply está ativo? A cor de sujeira é coerente com o tema do kit? |
| Render comparativo antes/depois (S08 vs. S09) mostrando evolução visível | C1 — Processo de Projeto | Os dois renders mostram diferença visível? A evolução é documentada e identificável sem legenda? |
| Nomenclatura de camadas organizada por tipo de detalhe (não genérica como "Layer 1") | C1 — Processo de Projeto | As camadas estão nomeadas de forma que qualquer pessoa possa entender o que cada uma faz sem abrir o Paint Room? |
| Tipo de desgaste coerente com o tema do kit (ex: ferrugem+pó para Medieval, fuligem+graxa para Sci-Fi) | C2 — Direção Artística | A escolha de cor e tipo de sujeira reflete o universo visual do moodboard do kit? |
| Feedback oferecido na crítica informal: ao menos uma observação específica sobre a lógica de desgaste de um colega | C10 — Participação | O feedback cita localização e lógica ("a sujeira está nas arestas superiores — ela deveria estar nas partes baixas") ou é genérico ("ficou bom / ficou ruim")? |
| Mapas atualizados exportados e conectados no Blender com render do material S09 | C4 — Materiais PBR | Os três PNGs foram exportados com a nomenclatura `_S09`? O material no Blender reflete os detalhes pintados? |

---

## Entrega da Semana 9

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo do 3D Coat com Asset 01 com camadas de detalhe (EdgeWear, Dirt e, se houver tempo, Scratches) | `.3b` ou `.3dc` com sufixo `_Asset01_3DCoat_S09` | Até o fim do segundo encontro |
| Mapas PBR exportados com detalhes: Albedo, Roughness, Metallic | `.png` 1024×1024 (ou 2048) na pasta `_Mapas_S09` | Até o fim do segundo encontro |
| Arquivo Blender atualizado com mapas da S09 conectados | `.blend` com sufixo `_Asset01_3DCoat_S09` | Até o fim do segundo encontro |
| Render comparativo antes/depois (S08 vs. S09) | `.png` com sufixo `_Comparativo_S08_S09` | Até o fim do segundo encontro |
| Screenshot do Paint Room com painel de camadas visível | `.png` com sufixo `_Camadas_S09` | Até o fim do segundo encontro |

> **Nota:** O início do Asset 02 no 3D Coat é opcional nesta semana e não compõe a nota. Estudantes que iniciaram devem salvar o arquivo `.3b` mesmo que incompleto — o Asset 02 será o foco da Semana 10 (stencils).

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 9 | 2026*
