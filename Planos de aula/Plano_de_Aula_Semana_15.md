# Plano de Aula — Semana 15
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização e Integração ao Motor
**Tema:** UDIMs e otimização: compressão, mipmaps e empacotamento de canais
**Apostila:** Parte V, Cap. 19 — UDIMs, Texture Arrays e Multi-Tile Texturing; Parte V, Cap. 20 — Compressão, Mipmaps e Packing de Canais
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 **Informal** — circulante, sem nota formal nesta semana

---

## Pré-requisito da semana

Os estudantes chegam com:

- Trim Sheet funcional, com ao menos uma faixa validada e reaplicada em uma segunda variação de asset, avaliada formalmente na CF5 — Semana 14
- Feedback escrito da CF5 já recebido, com ponto mais forte e prioridade de melhoria identificados
- Texture Atlas da Semana 13 e Trim Sheet da Semana 14 consolidados como as duas ferramentas de otimização por textura já dominadas
- Materiais PBR completos (Albedo, Metallic, Roughness, Normal) em pelo menos dois assets do kit, com bake integrado desde as Semanas 11–12

> **Nota de transição:** As Semanas 13 e 14 resolveram otimização do lado da **organização espacial** do UV — menos texturas distintas, por meio de agrupamento (atlas) ou reutilização por tiling (trim). Esta semana fecha a Unidade IV abordando um tipo diferente de otimização: o **peso e a estrutura de arquivo** de cada textura já produzida, independentemente de quantas existem. Um asset pode já ter o número mínimo de texturas graças ao atlas e à trim, e ainda assim consumir memória de vídeo desnecessária se cada textura for maior que o preciso, não tiver mipmaps configurados corretamente, ou usar três mapas em escala de cinza (Roughness, Metallic, AO) quando poderiam ocupar os três canais de um único arquivo (channel packing — mapa ORM). Além disso, para o caso raro de um asset que **precisa** de mais espaço de textura do que um único UV 0–1 comporta — um objeto hero do kit com muito detalhe — apresentamos os UDIMs, que estendem esse espaço para múltiplos tiles. Esta é a última semana de conteúdo novo antes da integração ao motor (Semana 16) e da apresentação final (Semana 17): o objetivo é que cada estudante feche o semestre sabendo justificar, com números, por que suas texturas pesam o que pesam.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que são UDIMs (Multi Tile Texture), diferenciando-os do espaço UV único 0–1 usado até aqui, e identificar em que situação um asset do próprio kit justificaria seu uso.
2. Diferenciar os principais formatos de compressão de textura para tempo real (BC1, BC3, BC7), relacionando cada um ao tipo de mapa PBR mais adequado (ex.: BC1 para Albedo sem alpha, BC7 para Normal Map de alta fidelidade).
3. Explicar o que são mipmaps, por que são gerados automaticamente pelo motor e como isso impacta a escolha de resolução e de compressão da textura.
4. Executar channel packing, combinando três mapas em escala de cinza (Roughness, Metallic, AO) nos canais R, G e B de uma única imagem (mapa ORM), reduzindo o número de texturas carregadas por material.
5. Justificar a resolução de textura escolhida para cada asset do kit com base em sua importância visual e distância de câmera esperada em cena, em vez de aplicar a mesma resolução a todos os assets por padrão.
6. Quantificar, em uma tabela comparativa, a economia de memória obtida entre o estado anterior (texturas separadas, sem compressão otimizada) e o estado após a otimização desta semana.
7. Importar um asset otimizado do kit na Unity e configurar um material PBR básico (Albedo, Normal, Metallic/Smoothness), sem lightmap, preparando o terreno técnico para a integração completa da Semana 16.

---

## Critérios observados nesta semana

> 🔵 **Crítica Informal.** Não há nota formal nesta semana. C7 (Otimização) já está em sua segunda semana de nota formal desde a CF5 (Semana 14) — aqui ele volta a ser apenas observado, mas com peso crescente de evidência acumulada para a reta final. C4 (Materiais PBR) retorna em observação, pois o channel packing reorganiza fisicamente os mapas PBR já validados nas Semanas 5–8.

| Critério | Status | O que observar |
|---|---|---|
| C1 — Processo de Projeto | obs. | Tabela de memória antes/depois registrada; justificativa de resolução por asset documentada |
| C4 — Materiais PBR | obs. — revisitado | O mapa ORM reconstituído no motor/shader preserva a leitura física correta de cada canal (Roughness, Metallic, AO)? |
| C7 — Otimização | obs. — evidência acumulada para a reta final | Escolha de resolução justificada por asset; uso correto de compressão por tipo de mapa; channel packing sem perda perceptível de qualidade |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado na crítica circulante sobre as escolhas de resolução e compressão dos colegas |

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Computadores com 3D Coat instalado (versão 2023 ou superior), com suporte a exportação de mapas separados por canal
- Arquivos `.blend`/projeto 3D Coat de todos os assets do kit de cada estudante, com mapas PBR completos (Albedo, Roughness, Metallic, AO, Normal) já produzidos nas semanas anteriores
- Editor de imagem com suporte a edição por canal (Krita, Photoshop ou equivalente) para o channel packing manual, caso o 3D Coat do laboratório não exporte ORM nativamente
- Arquivo de demonstração do professor: um asset simples já com Roughness, Metallic e AO separados, pronto para ser combinado ao vivo em um mapa ORM
- Projetor para demonstração
- Apostila — Parte V, Cap. 19 e Cap. 20 — trechos de UDIMs e otimização, disponibilizados antes da aula
- Planilha ou tabela simples (impressa ou digital) para o registro da comparação de memória antes/depois

> **Preparação do conjunto de demonstração:** É necessário que os três mapas em escala de cinza (Roughness, Metallic, AO) do objeto de referência já existam antes da aula, para que o tempo da demonstração seja dedicado à combinação dos canais e não à geração dos mapas em si.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**O peso da textura: UDIMs, compressão, mipmaps e channel packing**

Objetivo: fazer o estudante entender que otimização não termina em "quantas texturas eu tenho" (Semanas 13–14) — ela continua em "quanto cada textura pesa e como ela é lida pelo motor em tempo real".

**Abertura:**

Exibir no projetor dois arquivos de textura do mesmo asset lado a lado: um Albedo 4096×4096 sem compressão e o mesmo Albedo 1024×1024 com compressão BC7, ambos aplicados ao asset em um render comparativo. Perguntar: *"Visualmente, essas duas imagens no viewport parecem quase idênticas de perto e idênticas à distância normal de uso. Qual delas vocês acham que pesa mais em memória de vídeo — e por quanto?"*

Deixar 2–3 respostas (geralmente subestimadas). Revelar a proporção real (arquivo maior pode pesar dezenas de vezes mais). Direcionar para a ideia central: até aqui, a disciplina otimizou a **quantidade** de texturas (atlas, trim). Hoje o foco é o **peso individual** de cada textura que sobrou depois dessa otimização — resolução, compressão, mipmaps e o número de mapas carregados por material.

---

**Conteúdo a cobrir:**

**1. UDIMs (Multi Tile Texture): quando um único espaço 0–1 não é suficiente**

Este conceito já foi apresentado de forma breve na Semana 13, ao final da mini-aula de Texture Atlas — hoje é a aplicação prática dele. Até aqui, todo UV foi mapeado dentro de um único espaço 0–1 (Semanas 2–4), mesmo quando múltiplos objetos compartilhavam esse espaço via atlas (Semana 13). UDIMs estendem esse conceito: em vez de um único tile, o UV pode ocupar múltiplos tiles numerados (1001, 1002, 1003...), cada um funcionando como um espaço 0–1 independente com sua própria textura de alta resolução. Isso é usado quando um único asset — tipicamente um objeto *hero* do kit, com muito mais detalhe que os demais — precisa de mais resolução do que um único tile comportaria sem ficar borrado.

*"Pensem no espaço UV 0–1 como uma folha de papel. Até agora, tudo o que vocês fizeram coube em uma folha — mesmo quando vários objetos dividiram a mesma folha no atlas. UDIM é usar mais de uma folha para o mesmo objeto, quando ele é grande ou detalhado demais para uma folha só."*

*"Isso é exceção, não regra: a maioria dos assets de um kit modular de ambiente não precisa de UDIM — atlas e trim sheet já resolvem a maior parte dos casos das Semanas 13 e 14. UDIM se justifica para o objeto mais importante e mais próximo da câmera do seu kit, se houver um."*

**2. Compressão de textura: BC1, BC3, BC7**

Motores de jogo não armazenam texturas na GPU como PNG — eles usam formatos de compressão específicos para hardware gráfico, decodificados em tempo real com custo mínimo de performance:

- **BC1 (DXT1):** compressão mais agressiva, sem canal alpha (ou alpha de 1 bit). Adequado para Albedo sem transparência e para mapas simples como Metallic (que geralmente só precisa de poucos valores distintos).
- **BC3 (DXT5):** inclui canal alpha completo. Adequado quando a textura precisa de transparência real (ex.: folhagem, grades).
- **BC7:** compressão de maior qualidade, com custo de arquivo maior que BC1/BC3, mas muito mais fiel. Recomendado para Normal Maps (onde artefatos de compressão agressiva ficam visíveis como distorção de superfície) e para Albedo de assets hero.

*"A pergunta não é 'qual formato é melhor', é 'qual erro esse mapa específico pode tolerar sem que o olho perceba'. Um Normal Map errado quebra a leitura de profundidade da superfície inteira — por isso ele merece a compressão de maior qualidade, mesmo custando mais."*

**3. Mipmaps: por que existem e como influenciam a escolha de resolução**

Mipmaps são versões pré-calculadas de cada textura em resoluções decrescentes (metade do tamanho a cada nível), geradas automaticamente pelo motor e trocadas dinamicamente conforme a distância do objeto à câmera. Isso evita aliasing (ruído visual) em superfícies distantes e economiza banda de memória durante a renderização. A existência de mipmaps é um argumento a favor de **não superdimensionar** a resolução de textura de um asset pequeno ou distante: o detalhe extra de uma textura maior que o necessário nunca é visto de perto o suficiente para justificar o peso adicional, e ainda gera mais níveis de mipmap para armazenar.

*"Mipmap é a razão pela qual textura grande demais não é 'mais seguro', é só mais pesado. O motor já vai trocar automaticamente para uma versão menor quando o objeto estiver longe — o trabalho de vocês é escolher bem o tamanho da versão original, não empurrar essa decisão para depois."*

**4. Channel packing: o mapa ORM**

Roughness, Metallic e Ambient Occlusion são, cada um, mapas em escala de cinza — tecnicamente, cada um usa apenas 1 canal de cor, mas ocupa um arquivo de imagem inteiro com 3 canais (RGB) se exportado normalmente. Channel packing combina esses três mapas em um único arquivo: Roughness no canal R, Metallic no canal G, AO no canal B — o chamado **mapa ORM** (Occlusion-Roughness-Metallic). O resultado: três texturas separadas viram uma, sem perda de informação, porque cada mapa já usava só um canal.

*"É a mesma lógica do atlas da Semana 13, mas em vez de combinar objetos diferentes no espaço UV, vocês estão combinando mapas diferentes nos canais de cor de uma única imagem. Nada muda visualmente no resultado final — só o número de arquivos que o motor precisa carregar."*

> **Nota do professor:** Reforçar que channel packing só funciona porque os três mapas de origem já eram grayscale — combinar um mapa que realmente precisa de cor (Albedo) nesse esquema não faz sentido e quebra a técnica. Este é o erro conceitual mais comum desta semana.

---

### Demonstração — 20 minutos

**Criação de um mapa ORM (channel packing) e configuração de compressão/mipmaps**

**Setup (1 min):**
Abrir o editor de imagem com os três mapas em escala de cinza do objeto de demonstração (Roughness, Metallic, AO) já carregados lado a lado.

**Percurso da demonstração:**

**Passo 1 — Combinação dos canais (8 min):**
1. Criar uma nova imagem do mesmo tamanho dos três mapas de origem.
2. Copiar o mapa de Roughness para o canal R da nova imagem, o mapa de Metallic para o canal G, e o mapa de AO para o canal B (usando a ferramenta de canais do editor de imagem — Krita ou equivalente).
3. Exportar o resultado como um único PNG (`_ORM.png`).
4. Mostrar visualmente a imagem combinada: uma textura colorida e aparentemente sem sentido isolada, mas que representa três informações distintas simultaneamente.

**Passo 2 — Reconfiguração do material no Blender (6 min):**
1. No node editor do Blender (ou no shader equivalente), conectar a textura ORM ao material.
2. Separar os canais com um nó `Separate Color` (ou equivalente): canal R alimenta o input de Roughness, canal G o input de Metallic, canal B multiplica a cor final (AO).
3. Comparar o render antes (três texturas separadas) e depois (uma textura ORM) — confirmar que a aparência final é idêntica.

**Passo 3 — Compressão e mipmaps (4 min):**
1. Mostrar as configurações de exportação/importação de textura relevantes: escolha de formato de compressão por tipo de mapa (BC7 para Normal, BC1 para Albedo e ORM).
2. Mostrar a opção de geração automática de mipmaps habilitada, e explicar rapidamente onde essa configuração aparecerá na Unity na Semana 16.

**Passo 4 — Cálculo de economia (2 min):**
1. Comparar o peso em disco (proxy para memória de vídeo) dos três arquivos separados versus o único arquivo ORM comprimido.
2. Registrar a economia percentual como exemplo do tipo de dado que os estudantes vão calcular para o próprio kit.

**Passo 5 — Importação básica de um asset na Unity, sem lightmap (5 min):**
1. Abrir a Unity com um projeto já criado (URP configurado previamente pelo professor, para não consumir tempo de aula com setup de projeto).
2. Arrastar o arquivo `.fbx` do asset de demonstração (já com o ORM e os demais mapas otimizados) para a pasta de Assets.
3. Criar um novo material URP/Lit e conectar Albedo, Normal Map (marcando a textura como "Normal Map" no Inspector) e o mapa ORM nos slots de Metallic/Smoothness e Occlusion.
4. Arrastar o material para o asset na cena e mostrar o resultado sob a iluminação padrão da Unity — sem qualquer configuração de lightmap.
5. *"Isso é só a ponta do fluxo. Na Semana 16 vocês vão abrir um segundo canal de UV para a luz e rodar um lightmap bake da cena inteira — hoje o objetivo é só ver que o material que vocês otimizaram funciona igual dentro do motor."*

> **Nota do professor:** Se o laboratório não tiver um editor de imagem com edição por canal disponível, é aceitável demonstrar o Passo 1 conceitualmente com um arquivo ORM já preparado de antemão, focando o tempo na reconfiguração do material no Blender e na importação na Unity, que são as partes mais transferíveis para o projeto dos estudantes.

---

### Produção em Estúdio — 50 minutos

**Channel packing e planejamento de resolução dos assets do próprio kit**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com dois objetivos: primeiro, criar o mapa ORM de pelo menos um asset do seu kit, combinando Roughness, Metallic e AO em uma única textura. Segundo, revisar a resolução de todas as texturas do seu kit até agora e decidir, com justificativa, quais podem ser reduzidas sem perda perceptível. Vocês não precisam otimizar o kit inteiro hoje — o objetivo é ter pelo menos um asset com ORM funcional e a tabela de resoluções revisada."*

**Atividade estruturada:**

**Etapa 1 — Channel packing de um asset (≈25 min):**
1. Selecionar um asset do kit com Roughness, Metallic e AO já produzidos separadamente.
2. Combinar os três mapas em um único arquivo ORM, seguindo o processo da demonstração.
3. Reconfigurar o material do asset no Blender para ler o ORM combinado, separando os canais no node editor.
4. Validar visualmente: o render do asset com ORM deve ser indistinguível do render com os três mapas separados.

**Etapa 2 — Revisão de resolução por asset (≈15 min):**
1. Listar todos os assets do kit e suas texturas atuais (Albedo, Normal, ORM ou mapas separados).
2. Para cada asset, classificar sua importância visual esperada em cena: hero (grande, próximo da câmera, foco da composição), secundário (médio, presença regular) ou de fundo (pequeno, repetido, distante).
3. Decidir e justificar a resolução final de cada categoria (ex.: hero em 2048, secundário em 1024, fundo em 512), evitando aplicar a mesma resolução a todos por padrão.

**Etapa 3 — Registro de processo (≈10 min):**
1. Salvar o arquivo: `[Nome]_ORM_S15.blend`.
2. Preencher a tabela de memória: peso das texturas separadas (antes) versus peso do ORM comprimido (depois), para o asset trabalhado nesta etapa.
3. Screenshot do node setup com a separação de canais, para levar à crítica circulante do segundo encontro.

> Estudantes que concluírem as Etapas 1–3 com tempo sobrando já podem iniciar a importação do asset otimizado na Unity (ver Bloco 3 do segundo encontro) — não é obrigatório nesta etapa, mas adianta o trabalho do Encontro 2.

**Papel do professor:**

Circular verificando:

- **O channel packing preserva a leitura física correta de cada mapa?** Erro comum: inverter canais (ex.: Metallic no lugar de Roughness), o que produz um material fisicamente incoerente mesmo com o arquivo tecnicamente correto.
- **A justificativa de resolução é baseada em importância visual em cena, ou em conveniência ("deixei tudo em 2048 porque já estava assim")?** Perguntar diretamente: "Esse asset vai aparecer perto da câmera no seu kit, ou é um elemento de fundo repetido várias vezes?"
- **O estudante está confundindo channel packing com compressão?** São otimizações complementares, mas distintas — channel packing reduz o número de arquivos; compressão reduz o peso de cada arquivo individual.

Perguntas de mediação circulante:
- *"Se eu abrisse só o canal vermelho dessa textura ORM, eu deveria ver o mapa de Roughness dela. Vamos conferir?"*
- *"Esse asset é do tipo que a câmera vai chegar perto dele no seu kit final, ou ele aparece sempre de longe, repetido? Isso muda a resolução que ele precisa?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva — 20 minutos

**Formato: circulante, sem nota formal**

**Abertura (2 min):**
*"Hoje é crítica circulante — vou passar de estação em estação. Tenham o mapa ORM aberto com a separação de canais no node editor e a tabela de resolução por asset preenchida. Quero ouvir a justificativa de resolução antes de olhar os números."*

**Dinâmica (16 min):**
Circulação livre pelas estações. Em cada uma, o professor pede primeiro a justificativa de resolução, depois observa o ORM:
- *"Por que esse asset ficou em [resolução X] e não em [resolução Y]?"*
- *"Mostra o canal R isolado do seu ORM — é mesmo o Roughness que eu deveria estar vendo?"*
- *"Quanto essa textura pesava antes do channel packing, e quanto pesa agora?"*

Encorajar comparação entre colegas — *"Compare a lógica de resolução do seu kit com a do seu vizinho: vocês classificaram os assets hero/secundário/fundo de forma parecida?"* — sem formalizar como avaliação por pares registrada.

**Síntese (2 min):**
*"A maior parte de vocês já tem pelo menos um ORM funcional. O trabalho de hoje no estúdio é expandir isso para mais assets do kit e fechar a tabela comparativa de memória — essa tabela é uma das evidências mais concretas de otimização que vocês vão levar para a apresentação final."*

---

### Produção em Estúdio — 60 minutos

**Expansão do channel packing e fechamento da tabela de otimização do kit**

**Consigna:**

> *"Sessenta minutos para expandir o channel packing para mais assets do seu kit e fechar a tabela comparativa de memória: quantas texturas o kit usava antes de hoje, quantas usa agora, e qual o peso total estimado em cada cenário."*

**Atividade estruturada:**

**Bloco 1 — Channel packing de assets adicionais (≈25 min):**
1. Repetir o processo de combinação de canais (ORM) para os demais assets do kit que ainda têm Roughness, Metallic e AO separados.
2. Reconfigurar os materiais correspondentes no Blender.
3. Validar visualmente cada asset após a mudança.

**Bloco 2 — Ajuste de resolução conforme a tabela de importância (≈15 min):**
1. Redimensionar as texturas de assets classificados como secundários ou de fundo para a resolução decidida no primeiro encontro.
2. Reexportar e reaplicar as texturas redimensionadas, verificando que não há perda perceptível de qualidade na distância de uso esperada.

**Bloco 3 — Avaliação de necessidade de UDIM (≈10 min):**
1. Revisar se algum asset do kit — tipicamente o mais elaborado, hero da composição — se beneficiaria de UDIM por exigir mais detalhe do que um único tile 0–1 comporta.
2. Para a maioria dos kits, a conclusão esperada é que UDIM não é necessário — registrar essa conclusão como decisão justificada, não como tarefa pendente.

**Bloco 4 — Fechamento da tabela de memória e registro final (≈10 min):**
1. Consolidar a tabela: número de texturas do kit antes da Unidade IV (Semana 12) versus depois de atlas, trim e channel packing (hoje); peso estimado total em cada momento.
2. Exportar todos os mapas ORM finalizados.
3. Salvar arquivo Blender com sufixo `_Otimizacao_S15_Final`.

**Bloco 5 — Importação básica de um asset na Unity, sem lightmap (≈15 min, dentro do tempo do Bloco 3 de quem já concluiu a avaliação de UDIM):**
1. Exportar do Blender, como `.fbx`, um asset do kit já com o ORM e os demais mapas otimizados.
2. Na Unity: importar o `.fbx`, criar um material URP/Lit e conectar Albedo, Normal (com a flag "Normal Map" ativada no Inspector) e o mapa ORM nos slots de Metallic/Smoothness e Occlusion.
3. Aplicar o material ao asset na cena e verificar sob a iluminação padrão da Unity que a aparência é coerente com o resultado no Blender/3D Coat.
4. Salvar a cena da Unity — ela será reaproveitada diretamente na Semana 16, quando o foco passa a ser exclusivamente o UV2 e o lightmap bake.
5. Não é necessário importar mais de um asset nem configurar iluminação além do padrão — o objetivo desta semana é apenas validar que o material otimizado funciona no motor.

**Papel do professor:**

- Priorizar apoio aos estudantes com inversão de canais no ORM (erro mais custoso de diagnosticar sem verificação sistemática por canal).
- Para estudantes que terminam rápido: sugerir revisar se a compressão configurada em cada mapa (BC1/BC3/BC7) está de fato coerente com o tipo de conteúdo, não apenas com um padrão aplicado a todos.
- Perguntas de mediação: *"Olhando a tabela que vocês fecharam agora, qual foi a otimização que trouxe mais economia sozinha: o atlas, a trim sheet ou o channel packing de hoje? Essa resposta já é um argumento pronto para a apresentação final."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese técnica)**
*"Hoje fechamos a Unidade IV de otimização. Vocês agora têm quatro ferramentas complementares: atlas para agrupar objetos fixos, trim sheet para elementos repetitivos, channel packing para reduzir o número de arquivos por material, e o entendimento de UDIM para o caso raro de um asset que precisa de mais espaço do que isso tudo comporta. Semana que vem, a virada final: tudo isso vai para dentro da Unity."*

2. **(3 min — Reflexão de fechamento de unidade)**
Pergunta aberta: *"Olhando as quatro semanas da Unidade IV — atlas, trim, otimização — qual dessas técnicas vocês acham que vão usar mais no futuro, fora da disciplina, e por quê?"*
Deixar 2–3 respostas. O objetivo é consolidar que essas técnicas são práticas de produção real, não exercícios isolados da disciplina.

3. **(2 min — Antecipação da Semana 16)**
*"Vocês já importaram um asset na Unity hoje e viram o material funcionando. Semana que vem é a integração completa: todos os assets do kit na cena, um segundo canal de UV dedicado à luz (UV2) e um lightmap bake da cena inteira. Como a parte de importação e material vocês já dominam, a Semana 16 vai poder focar inteiramente nisso — UV2 e luz."*

4. **(2 min — Confirmação das entregas)**
Recapitular nomenclatura de entrega e prazo. Lembrar que a tabela de memória fechada hoje será parte da evidência de C7 na apresentação final da Semana 17.

---

## Possíveis Dificuldades

**1. Inversão de canais no channel packing**
O erro mais grave e menos perceptível visualmente: colocar Metallic no canal errado (ex.: R em vez de G) produz um material fisicamente incoerente que só é percebido quando o shader é configurado para ler o canal certo e o resultado não bate. Estratégia: verificar sistematicamente cada canal isolado do ORM (visualizar R, G e B separadamente) e comparar com o mapa de origem correspondente, em vez de confiar apenas no resultado visual final combinado.

**2. Confundir channel packing com Albedo**
Alguns estudantes tentam incluir um mapa de cor (Albedo) no esquema ORM, sem perceber que a técnica só funciona para mapas grayscale de canal único. Estratégia: reforçar que a pergunta-chave é "esse mapa usa cor real ou é uma escala de cinza representando um valor único?" — se a resposta for cor real, ele não entra no channel packing.

**3. Resolução de textura escolhida por hábito, não por critério**
Tendência de manter a mesma resolução usada desde as primeiras semanas (ex.: sempre 2048) sem reavaliar se o asset realmente precisa disso. Estratégia: exigir a classificação explícita hero/secundário/fundo antes de decidir a resolução — a decisão deve vir da importância em cena, não da resolução "padrão" que o estudante já está acostumado a usar.

**4. Aplicar UDIM sem necessidade real**
Empolgados com o conceito novo, alguns estudantes podem querer aplicar UDIM a um asset comum do kit, que já é bem servido por um único tile 0–1. Estratégia: reforçar que UDIM é solução de exceção — perguntar diretamente se o asset em questão realmente sofre perda de detalhe perceptível em um único tile antes de justificar o uso da técnica.

**5. Compressão genérica aplicada a todos os mapas igualmente**
Configurar todos os mapas (Albedo, Normal, ORM) com o mesmo formato de compressão, sem considerar que Normal Maps toleram muito menos erro de compressão que Albedo. Estratégia: retomar a tabela de formatos (BC1/BC3/BC7) e pedir que o estudante justifique a escolha de formato mapa por mapa, não texture set por texture set.

**6. Tempo insuficiente para expandir o channel packing a todos os assets**
Como nas semanas anteriores da Unidade IV, o primeiro asset consome mais tempo por ser a primeira vez executando o processo; os seguintes tendem a ser mais rápidos. Estratégia: priorizar o asset hero do kit no primeiro encontro (maior peso na apresentação final) e tratar os demais como expansão no segundo encontro, aceitando que nem todo o kit precise estar com ORM até o fim da semana.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante inseguro se inverteu algum canal no ORM | Isolar visualmente cada canal (R, G, B) da textura combinada e comparar lado a lado com o mapa de origem correspondente — a inspeção sistemática por canal resolve a dúvida mais rápido que tentar adivinhar pelo resultado final combinado. |
| Estudante tentando incluir Albedo no channel packing | Perguntar: "Esse mapa representa uma cor real que varia em RGB, ou um valor único em escala de cinza?" Se for cor real, mostrar que ele não se encaixa na lógica de canais únicos que torna o ORM possível. |
| Estudante mantendo a mesma resolução em todos os assets por hábito | Pedir que classifique cada asset como hero, secundário ou de fundo antes de qualquer decisão de resolução — a classificação costuma revelar sozinha onde a resolução está sendo desperdiçada. |
| Estudante querendo aplicar UDIM sem necessidade clara | Perguntar diretamente: "Esse asset específico já perde detalhe perceptível com um único tile, ou você só achou o recurso interessante?" Validar a curiosidade, mas redirecionar o tempo para os quatro assets que realmente precisam de otimização hoje. |
| Estudante aplicando a mesma compressão a Normal Map e Albedo | Mostrar lado a lado o mesmo Normal Map comprimido em BC1 (agressivo) e BC7 (alta qualidade) — a diferença de artefato na superfície costuma ser visível o suficiente para justificar a escolha sem explicação teórica adicional. |
| Estudante terminando rápido e com qualidade | Propor revisar a compressão de cada mapa individualmente (não por conjunto) e calcular a economia total acumulada do kit desde a Semana 13 (atlas + trim + channel packing) — essa métrica consolidada já antecipa parte do discurso da apresentação final. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Mapa ORM (channel packing) de ao menos um asset, com canais R/G/B correspondendo corretamente a Roughness, Metallic e AO | C7 — Otimização / C4 — Materiais PBR | A verificação por canal isolado confirma que cada canal contém o mapa correto, sem inversão? |
| Material reconfigurado no Blender lendo o ORM combinado, com render indistinguível da versão com mapas separados | C4 — Materiais PBR | O resultado visual final se manteve idêntico após a mudança de estrutura de arquivo? |
| Tabela de classificação hero/secundário/fundo dos assets do kit, com resolução justificada para cada categoria | C7 — Otimização | A resolução escolhida decorre da importância visual em cena, ou foi aplicada por hábito/conveniência? |
| Tabela comparativa de memória: peso das texturas antes (separadas, sem compressão otimizada) e depois (ORM, compressão adequada) | C1 — Processo de Projeto / C7 — Otimização | A economia está quantificada com números concretos, não apenas descrita qualitativamente? |
| Decisão registrada sobre a necessidade (ou não) de UDIM no kit, com justificativa | C7 — Otimização | A decisão está fundamentada na real exigência de detalhe do asset mais elaborado do kit? |
| Escolha de formato de compressão (BC1/BC3/BC7) coerente com o tipo de cada mapa | C7 — Otimização | O Normal Map recebeu compressão de maior qualidade que o Albedo, refletindo a menor tolerância a erro desse mapa? |
| Participação na crítica circulante: comentários referenciando critério técnico de resolução ou canal, não apenas impressão visual geral | C10 — Participação (obs.) | O feedback dado menciona classificação de importância, canal específico ou peso de arquivo, ou é genérico? |

---

## Entrega da Semana 15

| Entrega | Formato | Prazo |
|---|---|---|
| Mapa(s) ORM (channel packing) de pelo menos um asset do kit | `.png`, pasta `_ORM_S15` | Até o fim do segundo encontro |
| Arquivo Blender com materiais reconfigurados para leitura de ORM | `.blend` com sufixo `_Otimizacao_S15_Final` | Até o fim do segundo encontro |
| Tabela de classificação hero/secundário/fundo com resolução justificada por asset | Documento digital ou planilha | Até o fim do segundo encontro |
| Tabela comparativa de memória estimada (antes vs. depois da otimização) | Documento digital ou planilha, anexado ao arquivo de entrega | Até o fim do segundo encontro |
| Um asset do kit importado na Unity com material PBR básico configurado (sem lightmap) | Cena da Unity salva + screenshot | Até o fim do segundo encontro |

> **Nota:** Não há nota formal nesta semana (crítica informal). A tabela de memória e o(s) mapa(s) ORM produzidos hoje compõem o conjunto de evidências acumuladas de C7 (Otimização) que será apresentado de forma consolidada na CF6 da Semana 17 (Projeto Final).

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 15 | 2026*
