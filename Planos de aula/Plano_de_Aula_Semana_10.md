# Plano de Aula — Semana 10
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** III — Pintura Digital e Bake  
**Tema:** Uso de Stencils em texturização  
**Apostila:** Parte V, Cap. 17 — Máscaras, Stencils e Decals (uso de stencils no 3D Coat; criação e importação de alphas)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔵 Informal — Crítica circulante no segundo encontro

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 finalizado com camadas de desgaste: EdgeWear, Dirt e Scratches pintados no 3D Coat, mapas PBR exportados e conectados no Blender — Semana 9
- Render comparativo antes/depois do Asset 01 (S08 vs. S09) salvo — Semana 9
- Asset 02 importado no 3D Coat com ao menos as camadas base dos três canais (Color, Roughness, Metallic) pintadas — iniciado na Semana 9 (bloco final do estúdio) ou pendente para esta semana
- Moodboard atualizado com referências do tema do kit — Semana 1 (atualização contínua)

> **Nota de transição:** A Semana 9 desenvolveu a linguagem do desgaste por pintura livre — edge wear, dirt, scratches. Essa semana introduz uma nova forma de adicionar detalhe: o stencil. Se a pintura livre é como desenhar à mão, o stencil é como usar um carimbo com controle total de posição, escala e ângulo. Não são técnicas concorrentes — são complementares. Esta semana o foco migra do Asset 01 (desgaste orgânico) para o Asset 02 (detalhe específico e temático via stencil).

> **Atenção à Semana 11 (Crítica FORMAL):** Esta é a última semana antes da crítica formal da Unidade III. O estudante deve sair do segundo encontro desta semana com o Asset 02 suficientemente avançado para apresentação na semana seguinte. O fechamento desta aula deve deixar isso explícito.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Distinguir **stencil** de **alpha/brush**: compreender que o stencil é uma máscara estática projetada no espaço 3D, enquanto o alpha é uma textura aplicada junto com o brush.
2. Identificar e selecionar **fontes de stencils** apropriadas ao tema do kit (ArtStation, Poly Haven, TextureHaven) ou criar um stencil personalizado no Krita a partir de referência fotográfica.
3. Aplicar um stencil no 3D Coat com controle de **posição, escala, rotação e opacidade**, combinando múltiplos stencils para criar detalhe complexo.
4. Decidir **onde e como** o stencil contribui para a narrativa visual do asset: o stencil deve responder a uma necessidade do tema (rachadura, símbolo, corrosão, padrão de uso) — não ser aplicado aleatoriamente.
5. Combinar stencil com pintura livre para **integrar** o detalhe estampado ao contexto do material (evitando o efeito "colado sobre a superfície").
6. Exportar os mapas atualizados do Asset 02 e conectar no Blender para verificação visual.

---

## Critérios observados nesta semana

> ⚠️ **Semana sem crítica formal — nenhuma nota é atribuída.** O professor observa e registra evidências nos critérios abaixo para calibrar a avaliação da CF4 (sem 11). O estudante recebe feedback oral durante o estúdio.

| Critério | O que observar |
|---|---|
| C1 — Processo de Projeto | Screenshot do processo: stencil configurado no 3D Coat, camadas nomeadas, versão salva com sufixo `_S10` |
| C2 — Direção Artística | O tipo de stencil escolhido é coerente com o tema do kit? (Rachaduras para pedra medieval; corrosão para sci-fi; grafites para pós-apocalíptico) |
| C5 — Texturização | O stencil adicionou detalhe com narrativa temática? O detalhe está integrado ao material ou parece "colado"? A combinação de stencil + pintura livre é coerente? |
| C10 — Participação (CC) | Qualidade do feedback oferecido na crítica informal: o estudante consegue identificar se o stencil parece integrado ou sobreposto, e por quê? |

> **Progressão do PA — semana anterior à CF4:** Esta é a última semana antes da CF4 (sem 11). C5 (Texturização) é o critério que mais cresce neste momento — a distinção entre nível 3 ("detalhe presente mas desconexo do material") e nível 4 ("detalhe integrado com contexto de uso") é o que esta aula trabalha. O professor deve atualizar o registro de observação de C5 e C2 durante o estúdio, pois serão a base da avaliação formal da próxima semana. A nota da CF4 contribuirá com 25% para o PA.

---

## Recursos necessários

- Computadores com 3D Coat instalado (versão 2023 ou superior)
- Computadores com Krita instalado (versão 5.x — gratuito)
- Computadores com Blender instalado (3.x ou 4.x)
- Arquivos do Asset 02 de cada estudante no 3D Coat (`.3b` com camadas base ou em branco, a depender do progresso na S09)
- Arquivo de demonstração do professor: asset de pedra com UV e camadas base pintadas (Color, Roughness, Metallic — Fill), pronto para receber stencils
- Coleção de stencils organizada por categoria temática: **rachaduras** (pedra, concreto), **corrosão e oxidação** (metal, enferrujado), **padrões e símbolos** (runas, marcas industriais, grafites) — disponível como pasta .zip no servidor da disciplina ou pen drive
- Projetor para demonstração e crítica informal
- Apostila — Parte V, Cap. 17 — disponibilizada antes da aula

> **Preparação da coleção de stencils:** Organizar entre 15–20 stencils em escala de cinza (PNG fundo preto, detalhes brancos) divididos por categoria. Stencils com fundo preto funcionam diretamente no 3D Coat em modo de blend "Multiply". Fontes: [Poly Haven](https://polyhaven.com), [ArtStation Marketplace](https://www.artstation.com/marketplace) (muitos gratuitos), ou criados em aula no Krita como parte da demonstração.

> **Preparação do arquivo de demonstração:** O asset de demonstração deve ser de pedra (ou material genérico que permita rachaduras) com as três camadas base já pintadas. Não adicionar desgaste da S09 — o estudante precisa ver que o stencil pode trabalhar tanto sobre uma base limpa quanto sobre um material já desgastado. Usar o mesmo asset da S09 se possível, para que a turma perceba a continuidade.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Stencil como ferramenta de detalhe intencional**

Objetivo: apresentar o conceito de stencil, sua distinção de alpha/brush, e — mais importante — a lógica de quando e por que usar stencil em vez de pintura livre. A mini aula não é um tutorial de menu. É uma aula sobre decisão projetual.

**Abertura:**

Exibir no projetor duas imagens lado a lado: a primeira, uma superfície de pedra com rachaduras pintadas à mão com brush (imperfeitas, orgânicas, imprecisas); a segunda, a mesma superfície com rachaduras aplicadas por stencil (precisas, definidas, reproduzíveis). Perguntar à turma: *"Qual parece mais natural? Em que contexto cada uma faz mais sentido?"*

Deixar 2–3 respostas. Direcionar para a ideia central: stencil não é melhor nem pior que pintura livre — é uma ferramenta diferente para uma necessidade diferente. Quando você precisa de um padrão específico, reproduzível e controlado, o stencil é mais eficiente. Quando você precisa de orgânico, único e irregular, a pintura livre é mais adequada. O objetivo desta semana é aprender a usar as duas juntas.

---

**Conteúdo a cobrir:**

**1. Stencil vs. Alpha: a distinção fundamental**

**Alpha** é uma textura aplicada na ponta do brush. Quando você pinta, o brush "carimba" o alpha repetidamente ao longo do traço. O resultado depende do tamanho do brush, da pressão e do caminho percorrido. Útil para scratches e texturas de pincelada.

**Stencil** é uma máscara estática projetada sobre o asset. Não importa onde você pinta — o stencil permanece fixo no espaço 3D, funcionando como um gabarito. Você controla a posição, escala e rotação do gabarito, e então pinta sobre ele. O resultado é preciso e reproduzível em qualquer área do asset.

*"Pense assim: o alpha é o carimbo. O stencil é o molde que fica parado enquanto você passa a tinta por cima."*

No 3D Coat: o stencil fica no painel **Stencils** (aba lateral). Pode ser ativado e desativado com a tecla **S**. Com o stencil ativo, qualquer brush que você usar vai obedecer ao gabarito.

**2. Fontes de stencils**

**Fontes externas (gratuitas):**
- Poly Haven: texturas PBR com mapas de alpha utilizáveis como stencil
- ArtStation Marketplace: coleções gratuitas de stencils por categoria
- Fichiers de alpha do ZBrush (compatíveis com 3D Coat): muitas disponíveis no Reddit e Discord de ZBrush

**Criação manual no Krita:**
Qualquer imagem em escala de cinza pode virar stencil. Processo rápido:
1. Foto ou imagem de referência (ex: fotografia de parede rachada)
2. Filtro de contraste alto: `Filters → Adjust → Brightness/Contrast` (aumentar contraste para >80)
3. Opcional: `Filters → Edge Detection` para extrair só as bordas
4. Exportar como PNG 1024×1024 em escala de cinza

O stencil deve ter **fundo preto** (área que não pinta) e **detalhes em branco** (área que pinta). No 3D Coat, o modo de blend "Multiply" respeita essa convenção automaticamente.

**3. Quando usar stencil: a decisão projetual**

Stencil é a ferramenta certa quando o detalhe que você precisa:

- Tem uma **forma específica e reconhecível** que pintura livre dificilmente reproduz com precisão (rachadura ramificada, símbolo entalhado, padrão de corrosão química)
- Precisa ser **reproduzido em múltiplas faces** do mesmo asset ou em assets diferentes do kit (padrão de tijolos, marca de fabricante, grade metálica)
- Tem **escala e posição intencionais** na composição do asset (um símbolo centralizado em um escudo, uma rachadura que começa na aresta e avança para o centro)

Stencil *não* é a ferramenta certa para variação orgânica de cor, sujeira acumulada progressiva ou edge wear — esses pedem pintura livre.

*"A pergunta que você faz antes de abrir o stencil: 'Esse detalhe precisa ser específico e controlado, ou pode ser orgânico e irregular?' Se a resposta for específico: stencil. Se for orgânico: brush."*

**4. Integração: stencil + pintura livre**

O erro mais comum com stencil é aplicá-lo e deixar por aí — o resultado parece "estampado", flutuando sobre o material sem relação com o contexto. A integração acontece em duas etapas depois de aplicar o stencil:

- **Suavização de bordas:** com um brush de opacidade muito baixa (10–15%), pintar na borda do stencil para fundir com o material base. O detalhe não deve ter bordas perfeitamente definidas em um material orgânico.
- **Resposta do material ao detalhe:** uma rachadura real muda a roughness ao longo de sua extensão (mais rugosa nos bordos, mais lisa no interior se for fratura de rocha). Aplicar o stencil no canal Color não é suficiente — o detalhe deve ressoar nos outros canais.

> **Nota do professor:** Resistir à tentação de mostrar todas as opções do painel de Stencils na mini aula — o 3D Coat tem muitas. Cobrir apenas o essencial: como carregar, como posicionar (drag para mover, Ctrl+drag para escalar, Shift+drag para rotacionar), como ativar/desativar (tecla S). O restante o estudante descobre durante a demonstração e o estúdio.

---

### Demonstração — 20 minutos

**Aplicação de stencil no 3D Coat e criação de stencil no Krita**

**Setup (1 min):**  
Abrir o 3D Coat com o asset de demonstração pronto: mesh de pedra com UV, três canais base (Color, Roughness, Metallic — Fill). Ter o Krita aberto em segundo plano com uma fotografia de parede rachada já carregada.

**Percurso da demonstração:**

**Passo 1 — Carregar e posicionar um stencil existente (5 min):**
1. No painel lateral **Stencils**, clicar em `Import Stencil` e carregar o PNG de rachadura da coleção fornecida.
2. Ativar o stencil com a tecla **S** — o overlay aparece sobre o asset no viewport.
3. Mostrar os controles de posição:
   - **Drag** no centro: mover o stencil
   - **Ctrl + Drag**: escalar
   - **Shift + Drag**: rotacionar
4. Posicionar o stencil sobre a face principal do asset, com a rachadura saindo de uma aresta em direção ao centro: *"Rachaduras não começam no meio. Elas começam em pontos de tensão — arestas, furos, transições de material."*
5. Mostrar que o stencil permanece fixo enquanto você muda de face: *"Se eu pintar aqui e mudar de câmera para outra face, o stencil não se move. Ele é um gabarito no espaço — não segue o brush."*

**Passo 2 — Aplicar o stencil no canal Color (5 min):**
1. Canal ativo: **Color**. Nova camada: `Stencil_Rachadura_Color`. Modo: Normal. Opacidade: 85%.
2. Brush de tamanho médio, opacidade alta (80–90%). Cor: levemente mais clara que a pedra base (interior da rachadura expõe material mais claro, menos oxidado).
3. Pintar sobre o stencil com traços suaves. Mostrar que o brush só afeta onde o stencil é branco.
4. Verificar no Render Room: a rachadura aparece em cor diferente da superfície.

**Passo 3 — Aplicar o stencil no canal Roughness (4 min):**
1. Canal ativo: **Roughness**. Nova camada: `Stencil_Rachadura_Rough`. Modo: Normal. Opacidade: 90%.
2. Com o mesmo stencil ativo, pintar na rachadura com valor de roughness alto (cor clara = muito rugoso = fratura exposta de pedra).
3. Adicionar uma segunda passada mais fina e longa saindo da rachadura principal — as micro-trincas ao redor. *"Uma rachadura real não é um traço limpo. Ela tem micro-fissuras que irradiam. Isso é o que o Roughness captura, mesmo invisível em Color."*
4. Mostrar no Render Room: a rachadura agora muda o comportamento de luz — a fratura absorve mais luz do que a superfície polida ao redor.

**Passo 4 — Criação de stencil personalizado no Krita (4 min):**
1. Abrir o Krita com a fotografia de parede rachada.
2. Aplicar `Filters → Adjust → Brightness/Contrast` (Contrast ao máximo). Mostrar como o contraste alto isola as rachaduras.
3. Converter para escala de cinza: `Image → Convert Image Color Space → Grayscale`.
4. Exportar como PNG: `File → Export → PNG → 1024×1024`.
5. Voltar ao 3D Coat: importar o stencil criado e mostrar que ele funciona imediatamente. *"Em menos de 2 minutos, qualquer foto com contraste vira stencil. A internet inteira de referências de superfície é uma biblioteca de stencils esperando para ser convertida."*

**Passo 5 — Integração: suavizar bordas do stencil (2 min):**
1. No canal Color, desativar o stencil (tecla S) para trabalhar com brush livre.
2. Brush grande, opacidade muito baixa (10%). Cor intermediária entre o stencil e o fundo.
3. Pintar nas bordas da rachadura com traços suaves. *"Estou fundindo a borda do stencil com o material. O detalhe não deve parecer colado — deve parecer que a rachadura pertence à pedra."*
4. Resultado no Render Room: comparar com e sem a suavização. A diferença é sutil mas elimina o efeito "estampado".

> **Nota do professor:** Não é necessário demonstrar stencil em múltiplos canais além de Color e Roughness — o estudante pode explorar o canal Metallic no estúdio se quiser. O foco da demonstração é o workflow completo: carregar → posicionar → aplicar em ao menos dois canais → integrar. A criação no Krita é rápida (4 min) mas de alto valor pedagógico — mostra que qualquer referência fotográfica pode se tornar ferramenta de trabalho.

---

### Produção em Estúdio — 50 minutos

**Aplicação de stencils temáticos no Asset 02**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com o Asset 02. Antes de abrir qualquer stencil, olhem o moodboard e respondam: 'Que tipo de detalhe específico esse asset precisa que pintura livre não entregaria com precisão?' Isso é o que você vai fazer com stencil. Se a resposta for 'nenhum', talvez seu asset não precise de stencil — use pintura livre. Mas se houver um padrão, um símbolo, uma rachadura com forma definida, ou uma textura de corrosão com estrutura — esse é o stencil. Antes de sair desta sessão: ao menos um stencil aplicado em dois canais (Color e Roughness), com as bordas integradas. Screenshot do processo com o painel de Stencils visível."*

**Atividade estruturada:**

**Etapa 1 — Verificação do estado do Asset 02 (≈5 min):**
1. Abrir o arquivo `.3b` do Asset 02 no 3D Coat (ou iniciar a importação se o asset ainda não foi trazido para o 3D Coat na S09).
2. Se as camadas base ainda não existem: criar Fill de Color, Roughness e Metallic antes de prosseguir (≈5 min de trabalho rápido — o estudante já fez isso na S09 com o Asset 01).
3. Abrir o Render Room por 1 minuto: avaliar o estado atual. Identificar: *que detalhe específico o tema pede que este asset tenha?*

> **Opção de recuperação:** Estudantes que não iniciaram o Asset 02 na S09 devem dedicar os primeiros 10 min ao setup base (importar mesh com UV do Blender, pintar Fill nos três canais). O stencil pode ser aplicado nos 40 min restantes — é tempo suficiente.

**Etapa 2 — Seleção e carregamento do stencil (≈5 min):**
1. Acessar a coleção de stencils fornecida pelo professor ou criar um no Krita com referência do moodboard.
2. Critério de seleção: o stencil deve responder a uma necessidade do tema. Exemplos por tema:
   - Medieval/Fantasia: rachaduras de pedra, runas entalhadas, marca de ferreiro, desgaste de pele/couro
   - Sci-Fi: corrosão química com padrão hexagonal, marca de laser, grade de ventilação, grafismo de painel
   - Pós-apocalíptico: grafite de spray, ferrugem com padrão de escorrimento, vidro quebrado, fuligem localizada
   - Cyberpunk: circuito impresso, néon derramado, marca de solda, código QR desgastado
3. Importar no 3D Coat e posicionar: *a rachadura deve começar em ponto de tensão, o símbolo deve ter posição intencional na composição do asset.*

**Etapa 3 — Aplicação do stencil em múltiplos canais (≈25 min):**

No canal **Color**:
1. Nova camada: `Stencil_[Nome]_Color`. Modo: Normal. Opacidade: 80–90%.
2. Brush de tamanho adequado ao detalhe. Cor coerente com o tipo de detalhe (interior da rachadura, cor do símbolo, cor de corrosão).
3. Pintar sobre o stencil. Verificar no Render Room.

No canal **Roughness**:
1. Nova camada: `Stencil_[Nome]_Rough`. Modo: Normal. Opacidade: 90%.
2. Valor de roughness coerente: fratura de pedra → rugosa (cor clara); símbolo entalhado → pode ser polido nas bordas; corrosão → muito rugosa.
3. Verificar: o detalhe muda a leitura de luz no Render Room?

**Integração com pintura livre (mesmo bloco):**
1. Desativar stencil (tecla S).
2. Brush grande, opacidade muito baixa (10–15%). Cor intermediária.
3. Suavizar bordas do stencil no canal Color e, se necessário, no Roughness.
4. Adicionar uma ou duas pinceladas de Dirt ao redor do detalhe (sujeira acumulada dentro da rachadura ou ao redor do símbolo — o detalhe "atrai" sujeira).

**Etapa 4 — Segundo stencil ou variação (≈10 min, se houver tempo):**

Para estudantes que completaram o primeiro stencil com integração:
1. Aplicar um segundo stencil menor em outra face do asset: micro-rachaduras secundárias, marca adicional, padrão de textura.
2. Ou variar a escala e rotação do mesmo stencil e aplicar em outra posição — criando duas ocorrências do mesmo tipo de detalhe com leituras diferentes.

**Etapa 5 — Registro de processo (≈5 min):**
1. Screenshot do Paint Room com o painel de Stencils visível e as camadas nomeadas.
2. Render Room: screenshot close-up do detalhe aplicado.
3. Render Room: screenshot da câmera afastada (distância de uso).
4. Salvar: `[Nome]_Asset02_S10.3b`.

**Papel do professor:**

Circular verificando três pontos em cada estação:

- **O stencil tem justificativa temática?** Se o estudante está usando o primeiro stencil que encontrou sem relação com o tema, redirecionar: *"O que esse objeto sofreu que deixaria essa marca específica? Rachaduras fazem sentido para madeira? Para metal? Para o contexto do seu kit?"*
- **O stencil está posicionado com intenção ou aleatoriamente?** Verificar se a posição do stencil faz sentido compositivo e narrativo: *"Por que a rachadura começa aqui? O que causou isso neste ponto específico do objeto?"*
- **A integração aconteceu?** O erro mais comum é deixar o stencil sem suavização de bordas. Se o detalhe parece "colado sobre" o material, pedir que o estudante faça a etapa de suavização antes de avançar.

Perguntas de mediação circulante:
- *"Se eu cobrir o stencil com minha mão e olhar só o material base, e depois revelar — a diferença parece que pertence ao material ou parece que foi adicionada por fora?"*
- *"Você aplicou o stencil só no Color. O que acontece com o Roughness nessa região? Material com rachadura fica mais rugoso ou mais liso do que o entorno?"*
- *"Esse símbolo foi entalhado, pintado ou fundido no metal? Cada resposta pede um tipo diferente de variação de roughness ao redor."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: Walk-around com foco em integração**

Esta é uma crítica 🔵 Informal. Não há ficha formal nem apresentação individual estruturada. O objetivo é identificar coletivamente a diferença entre stencil integrado e stencil sobreposto — e definir o que cada estudante deve trabalhar no segundo estúdio.

**Protocolo:**

**Preparação (2 min antes do início):**
- Cada estudante exibe o Asset 02 no Render Room com o detalhe de stencil aplicado.
- Preparar dois screenshots visíveis: o asset antes do stencil (base da S09) e o estado atual.

**Abertura (2 min):**
*"Vamos olhar os assets com uma pergunta única: o stencil pertence ao material ou está por cima do material? 'Pertencer' significa que o detalhe faz sentido com o tipo de superfície, com a posição no asset, e que as bordas estão integradas. 'Por cima' significa que o detalhe parece colado — as bordas são muito definidas, a cor não dialoga com o material base, ou a posição não tem narrativa. Cada um tem 20 segundos para me dizer: pertence ou está por cima? E por que?"*

**Walk-around (15 min):**

O professor circula com a turma. Para cada asset, 30–45 segundos de observação coletiva. Perguntas-modelo:

- *"Olhando de longe: o detalhe aparece? Se aparecer, é porque tem contraste suficiente. Se não aparecer, pode ser que esteja fraco demais ou integrado demais — são problemas diferentes."*
- *"O tipo de stencil escolhido é coerente com o material? Esse padrão de corrosão acontece em pedra? Essa rachadura aparece em metal?"*
- *"Compara com o asset do colega que tem o mesmo tipo de superfície. O detalhe de stencil tem a mesma 'linguagem' ou cada um tem um stencil de uma categoria visual diferente?"*
- *"O roughness ao redor do stencil mudou? Ou o detalhe existe só no Color?"*

Identificar e destacar: um ou dois casos de stencil bem integrado (bordas suavizadas, roughness correspondente, narrativa clara) e um ou dois casos que precisam de integração ainda. Não como crítica negativa — como materialização do próximo passo de cada estudante.

**Síntese (3 min):**
*"O que estou vendo em geral: [X — o que está bem]. O que falta ainda: [Y — o que precisa de atenção]. Nos próximos 60 minutos, quero que cada um resolva pelo menos uma dessas coisas: (1) integrar as bordas do stencil se ainda parecem coladas; (2) aplicar o stencil no canal Roughness se ainda está só no Color; ou (3) avançar para um segundo detalhe se o primeiro já está resolvido. Saiam desta aula com o Asset 02 em estado de apresentação — semana que vem é Crítica Formal."*

---

### Produção em Estúdio — 60 minutos

**Integração, refinamento e preparação para a Crítica Formal da Semana 11**

**Consigna:**

> *"Sessenta minutos com foco em qualidade, não em quantidade. Não adicionem stencil novo só para ter mais — refinem o que já existe. Ao final desta sessão, o Asset 02 precisa estar em estado de apresentação: pelo menos um stencil integrado em Color e Roughness, bordas suavizadas, e os mapas exportados para o Blender. Quem terminar isso com tempo sobrando: aplique os detalhes de edge wear e dirt aprendidos na S09 ao Asset 02 — o stencil não substitui o desgaste, ele adiciona um nível a mais."*

**Atividade estruturada:**

**Bloco 1 — Refinamento de integração com base no feedback da crítica (≈20 min):**

Para cada ponto levantado na crítica informal, identificar e resolver:

1. **Bordas ainda muito definidas:** Desativar stencil (S). Brush grande, opacidade 10–15%. Pintar nas bordas em Color e em Roughness. Comparar antes/depois desativando a camada de integração.
2. **Stencil só no Color:** Criar `Stencil_[Nome]_Rough` e aplicar o mesmo gabarito no canal Roughness. Verificar resposta no Render Room.
3. **Posição do stencil sem narrativa:** Mover o stencil para posição mais intencional (ponto de tensão, centro compositivo, ponto de uso). Redesenhar as camadas. Se o stencil foi destruído, reconstruir na nova posição — é aprendizado legítimo.
4. **Tipo de stencil incongruente com o material:** Trocar por um stencil da coleção mais adequado ao material. O retrabalho aqui é pedagógico — a decisão errada de stencil é conteúdo da crítica.

**Bloco 2 — Complementar com edge wear e dirt da S09 (≈20 min):**

Para estudantes com o stencil integrado e resolvido:
1. No canal Color: camada `EdgeWear_Color` com as arestas mais expostas do Asset 02. Lógica de uso da S09.
2. No canal Roughness: `EdgeWear_Rough` correspondente.
3. No canal Color: camada `Dirt_Color` (Multiply, baixa opacidade) nas partes inferiores e côncavas.
4. Verificar coerência entre o desgaste pintado livremente e o detalhe do stencil: *o objeto tem rachaduras E sujeira? As rachaduras estão em locais coerentes com o acúmulo de sujeira?*

> **Nota de continuidade:** Estudantes que chegaram mais avançados podem ter um Asset 02 com stencil + desgaste completo ao final desta semana. Isso coloca esses estudantes em posição confortável para a Crítica Formal da S11, onde o foco será bake — eles chegam com dois assets texturizados com qualidade.

**Bloco 3 — Exportação e verificação no Blender (≈15 min):**
1. No 3D Coat: `File → Export Textures`.
2. Exportar Albedo (Color), Roughness, Metallic.
3. Pasta de destino: `[Nome]_Asset02_Mapas_S10/`.
4. Abrir o Blender com o material do Asset 02.
5. Conectar os mapas exportados no Principled BSDF. Verificar: **Color Space** dos mapas de dados (Roughness, Metallic) deve ser **Non-Color**.
6. Viewport Rendered: verificar que o stencil aparece corretamente. Se o detalhe desapareceu ou parece diferente do 3D Coat, comparar os nós — o erro mais comum é mapa conectado no slot errado.
7. Capturar render do Asset 02 com material S10 conectado.
8. Salvar: `[Nome]_Asset02_Blender_S10.blend`.

**Bloco 4 — Documentação visual para a S11 (≈5 min):**
1. Screenshot do Paint Room com painel de camadas e painel de Stencils visível.
2. Screenshot do Render Room: close-up do detalhe do stencil.
3. Screenshot do Render Room: câmera afastada (distância de uso).
4. Organizar na pasta de entrega com nomenclatura padronizada.

**Papel do professor:**

- Para estudantes com stencil ainda "flutuando" sobre o material sem integração: *"Desativa a camada do stencil por 5 segundos. Agora reativa. A transição parece suave ou abrupta? Se abrupta, é porque a borda não foi trabalhada. A suavização de borda não é opcional — é o que transforma o stencil de elemento decorativo em propriedade do material."*
- Para estudantes com dificuldade de decidir o tipo de stencil: *"Abre o moodboard. Qual textura de superfície tem nessas referências que você ainda não colocou no asset? Tem padrão de madeira serrada? Marca de entalhe? Isso é o que você busca como stencil."*
- Para estudantes avançados com tempo sobrando: *"Tente um channel packing visual: use o stencil de rachadura no canal Metallic com valor 0 na rachadura e entorno com valor maior. Em alguns materiais metálicos, a fratura expõe o metal bruto abaixo da oxidação — isso é um detalhe de Metallic, não só de Color e Roughness."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese da semana)**
*"Hoje vocês aprenderam que o stencil é uma ferramenta de precisão — não de conveniência. Um stencil mal posicionado, sem justificativa, e sem integração de bordas, prejudica o material em vez de enriquecer. Um stencil bem colocado conta a história de um evento específico: a rachadura que surgiu de um impacto, a corrosão que se instalou em um ponto de umidade, o símbolo gravado por uma mão. A técnica é simples. A decisão é o que importa."*

2. **(3 min — Reflexão de processo)**
Pergunta aberta: *"Qual foi o momento de maior dúvida de hoje? Quando vocês não sabiam se o detalhe estava integrado ou não? Como vocês resolveram?"*

Deixar 2–3 respostas. Direcionar para a percepção de que o critério de avaliação do próprio trabalho — "pertence ou está por cima?" — é uma habilidade de autoleitura que se desenvolve com prática. Quanto mais se nomeia o problema em palavras, mais rápido o olho aprende a identificar.

3. **(3 min — Preparação para a Semana 11 — CRÍTICA FORMAL)**
*"Semana que vem é a Crítica Formal 4 — CF4. O tema técnico será Bake: vocês vão aprender a transferir detalhe de um mesh de alta resolução para o low poly. Mas antes de entrar nesse conteúdo, a crítica vai exigir que o Asset 02 esteja apresentável — com stencils integrados e desgaste. Isso é o que vocês têm desta sessão para amanhã. Quem chegar na S11 com o Asset 02 em estado incompleto vai entrar na parte mais técnica da disciplina com um passivo. Priorizem a exportação e o Blender antes de encerrar."*

*"Para a crítica formal da S11, trazer: Asset 01 (completo, S09), Asset 02 (stencils + desgaste, S10), renders de ambos, pasta de camadas organizada e autoavaliação da rubrica preenchida. A ficha de autoavaliação estará disponível no servidor antes da próxima aula."*

4. **(2 min — Confirmação das entregas)**
Recapitular com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Stencil aplicado sem justificativa temática — detalhe incongruente com o material**
O estudante escolhe o primeiro stencil disponível (ex: rachadura de concreto aplicada em metal polido) sem verificar coerência. O resultado é um detalhe que não "pertence" ao material. Estratégia: antes de carregar o stencil, o estudante deve responder em voz alta: *"Esse tipo de detalhe acontece nesse tipo de material, nesse universo do kit?"* Se a resposta não for clara, trocar o stencil antes de pintar qualquer coisa.

**2. Bordas do stencil muito definidas — efeito "colado sobre"**
O detalhe aparece com borda perfeitamente recortada, sem transição com o material de base. Estratégia: a etapa de suavização de bordas com brush de baixa opacidade não é opcional — ensinar como parte do fluxo, não como etapa de finalização opcional. No estúdio, verificar ativamente se a suavização foi feita antes de liberar o estudante para avançar.

**3. Stencil aplicado apenas no canal Color — falta de resposta física do material**
O estudante aplica o stencil no Color e considera o trabalho concluído. O detalhe existe visualmente mas não tem profundidade física — não muda a roughness, não responde diferente à luz. Estratégia: o protocolo do estúdio exige explicitamente a aplicação em dois canais (Color e Roughness). O professor deve verificar o painel de camadas: se só existir `Stencil_Color` e não `Stencil_Rough`, o trabalho está incompleto.

**4. Asset 02 ainda não importado para o 3D Coat — atraso de progresso**
Estudantes que não iniciaram o Asset 02 na S09 chegam sem arquivo `.3b` para trabalhar. Estratégia: os primeiros 10 min do estúdio são de setup (importar mesh, Fill nos três canais). O professor deve identificar esses estudantes antes da mini aula e avisá-los para iniciar o setup imediatamente ao início do estúdio, sem esperar a demonstração terminar.

**5. Stencil posicionado aleatoriamente — sem intenção compositiva**
O estudante posiciona o stencil onde "coube" sem pensar na lógica narrativa do detalhe. Rachaduras no centro de uma superfície plana sem fissuras ao redor, símbolos em áreas não visíveis ou mal proporcionados em relação ao asset. Estratégia: antes de pintar qualquer coisa com o stencil, pedir ao estudante que explique a posição: *"Por que aqui? O que causou esse detalhe nesse ponto?"* A incapacidade de responder é sinal de posicionamento aleatório.

**6. Confusão entre stencil e alpha durante o estúdio**
Alguns estudantes tentam usar o painel de Alphas do brush em vez do painel de Stencils, obtendo resultados diferentes do esperado. O brush com alpha se repete ao longo do traço; o stencil permanece fixo. O resultado parece errado e o estudante não entende por quê. Estratégia: verificar qual painel está ativo durante a circulação — Alpha em vez de Stencil é o erro mais comum de identificação de interface.

**7. Detalhe de stencil desaparece ou distorce no Blender após exportação**
O mapa exportado parece correto no 3D Coat mas no Blender o detalhe tem cor estranha ou a roughness parece invertida. Causa mais comum: mapa de Roughness conectado com Color Space sRGB em vez de Non-Color. Estratégia: checklist de verificação na etapa de exportação: *"Roughness e Metallic: Color Space = Non-Color. Albedo: Color Space = sRGB. Se o detalhe sumiu, começa por aí."*

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não consegue decidir qual stencil usar | Pedir que abra o moodboard e aponte três superfícies nas referências que têm um detalhe específico e reconhecível que ainda não está no asset. Esse detalhe é o candidato ao stencil. A decisão vem das referências, não da coleção de stencils disponível. |
| Estudante que posiciona o stencil com medo de "estragar" | *"O stencil não é destrutivo enquanto estiver em camada separada. Se você não gostar da posição, apaga a camada e refaz. O único erro aqui é não tentar."* Confirmar que as camadas estão separadas antes de iniciar. |
| Stencil parece "flutuando" sobre o material (sem integração) | Perguntar: *"Se esse objeto existisse no mundo real, alguém conseguiria descascar esse detalhe com a mão? Se conseguisse, está colado. Se não conseguisse — se fosse parte do material — as bordas precisam desaparecer no entorno."* Depois: suavização de bordas com brush 10% opacidade. |
| Estudante avançado que dominou o stencil rapidamente | Propor desafio: criar um stencil personalizado do zero no Krita com um elemento específico do tema (ex: uma runa medieval, um símbolo de facção sci-fi, um logotipo industrial). O stencil criado pelo estudante é mais valioso como portfólio do que um stencil de biblioteca. |
| Estudante com Asset 02 em estado muito incompleto (sem camadas base) | Reduzir o escopo para a semana: uma camada base de Color + um stencil simples integrado + exportação. Melhor um detalhe bem resolvido do que três detalhes fragmentados. A Crítica Formal da S11 avalia processo e qualidade, não quantidade. |
| Estudante que aplica vários stencils diferentes sem integrar nenhum | *"Para. Escolhe o melhor dos stencils que você aplicou — o que mais faz sentido com o material. Apaga os outros. Resolve esse um com integração completa. Depois, se sobrar tempo, você adiciona o segundo. Três stencils mediocres valem menos que um stencil exemplar."* |
| Estudante que questiona se precisa de stencil para o tema do seu kit | Validar a dúvida genuína: *"Para alguns kits — especialmente os mais orgânicos ou estilizados — pintura livre entrega o mesmo resultado com mais naturalidade. Se você olhar o moodboard e não encontrar nenhum detalhe que seja específico e controlado o suficiente para precisar de stencil, tudo bem. Mas preciso ouvir de você por que o detalhe pode ser pintado livre com o mesmo resultado — não que você não quer aprender a ferramenta."* |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Camada `Stencil_[Nome]_Color` no arquivo `.3b` do Asset 02 com detalhe visível e posicionado com intenção narrativa | C5 — Texturização | O detalhe existe? A posição tem justificativa de uso (ponto de tensão, elemento temático)? |
| Camada `Stencil_[Nome]_Rough` correspondente com valor de roughness coerente ao tipo de detalhe (fratura, símbolo, corrosão) | C5 — Texturização | O detalhe muda a resposta de luz no Render Room? A variação de roughness é plausível para o tipo de evento representado? |
| Bordas do stencil suavizadas com brush de baixa opacidade — detalhe integrado ao material (não "colado sobre") | C5 — Texturização | A transição entre o detalhe e o material base é suave? Ou há uma borda perfeitamente recortada que denuncia o stencil? |
| Tipo de stencil coerente com o tema e o material do kit | C2 — Direção Artística | A escolha do stencil reforça a proposta estética do moodboard? Ou é um stencil genérico sem relação com o universo visual do kit? |
| Screenshot do Paint Room com painel de Stencils visível e camadas nomeadas | C1 — Processo de Projeto | As camadas de stencil estão nomeadas de forma descritiva? O painel de Stencils mostra o stencil carregado? |
| Mapas do Asset 02 exportados e conectados corretamente no Blender com Color Space correto | C4 — Materiais PBR | Os três mapas foram exportados? O Roughness tem Color Space = Non-Color? O detalhe do stencil aparece no viewport do Blender? |
| Feedback oferecido na crítica informal distinguindo stencil integrado de stencil sobreposto, com observação específica | C10 — Participação | O feedback usa os critérios de integração ("as bordas estão ainda muito definidas", "o roughness não corresponde ao tipo de fratura") ou é genérico ("ficou bom/ruim")? |

---

## Entrega da Semana 10

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo do 3D Coat com Asset 02 com ao menos um stencil integrado em dois canais | `.3b` ou `.3dc` com sufixo `_Asset02_S10` | Até o fim do segundo encontro |
| Mapas PBR exportados do Asset 02: Albedo, Roughness, Metallic | `.png` 1024×1024 (ou 2048) na pasta `_Asset02_Mapas_S10` | Até o fim do segundo encontro |
| Arquivo Blender do Asset 02 com mapas da S10 conectados | `.blend` com sufixo `_Asset02_Blender_S10` | Até o fim do segundo encontro |
| Screenshot do Paint Room com painel de Stencils e camadas visíveis | `.png` com sufixo `_StencilProcess_S10` | Até o fim do segundo encontro |
| Screenshot do Render Room: close-up do stencil aplicado | `.png` com sufixo `_StencilCloseup_S10` | Até o fim do segundo encontro |
| Screenshot do Render Room: câmera afastada (distância de uso) | `.png` com sufixo `_DistanciaUso_S10` | Até o fim do segundo encontro |

> **Nota sobre a Crítica Formal da Semana 11:** O Asset 02 da S10 será apresentado na Crítica Formal da S11 junto com o Asset 01 (finalizado na S09). Estudantes devem chegar na S11 com o Asset 02 em estado de apresentação. A ficha de autoavaliação da rubrica mestre deve ser preenchida antes da S11 — ela estará disponível no ambiente virtual antes da próxima aula.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 10 | 2026*
