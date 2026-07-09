# Plano de Aula — Semana 16
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização e Integração ao Motor
**Tema:** Integração na Unity: materiais, lightmap UV e renderização
**Apostila:** Cap. 11 — Abertura de malha para lightmap; Cap. 12 — Importação e configuração na Unity; Renderização de modelos texturizados
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 **Informal** — circulante, sem nota formal nesta semana

---

## Pré-requisito da semana

Os estudantes chegam com:

- Kit modular com UV principal (UV1) validado desde as Semanas 2–4, materiais PBR completos (Albedo, Metallic, Roughness, Normal) desde as Semanas 5–8, texturas com detalhe pintado e bake integrado desde as Semanas 9–12
- Otimização de textura consolidada na Unidade IV: Texture Atlas (Semana 13), Trim Sheet validada formalmente na CF5 (Semana 14), e mapa ORM / decisões de resolução e compressão fechados na Semana 15
- Tabela comparativa de memória (antes/depois da otimização) já preenchida, cobrindo todos os assets trabalhados até aqui
- Nenhuma experiência prévia na disciplina com a Unity como motor de destino — até aqui, todo o trabalho de visualização e validação ocorreu inteiramente no Blender e no 3D Coat

> **Nota de transição:** As Semanas 13 a 15 resolveram a Unidade IV do lado da **produção de conteúdo**: menos texturas (atlas, trim) e texturas mais leves (channel packing, compressão, resolução justificada). Esta semana fecha a unidade transportando esse conteúdo, pela primeira vez, para dentro de um motor de jogo real. Isso exige um UV que ainda não foi trabalhado na disciplina — o **UV2 de lightmap**, distinto do UV1 usado desde a Semana 2 para aplicar textura — e a reconfiguração dos mapas PBR já produzidos dentro do sistema de materiais da Unity (URP/HDRP), que lê e interpreta canais de forma diferente do Principled BSDF do Blender. O resultado esperado é a primeira visão do kit modular inteiro, montado como cena, sob iluminação baked — o ensaio geral antes da apresentação final da Semana 17.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Diferenciar UV1 (mapa de textura, trabalhado desde a Semana 2) de UV2 (mapa de lightmap), explicando por que a iluminação baked exige um layout de UV com regras próprias — sem sobreposição entre ilhas, mesmo que isso já exista intencionalmente no UV1.
2. Gerar um UV2 de lightmap no Blender para os assets do kit, distinto do UV1 já validado, respeitando padding suficiente para evitar vazamento de luz (light bleeding) entre ilhas adjacentes.
3. Exportar os assets do kit em FBX preservando ambos os canais de UV (UV1 e UV2) e importá-los corretamente na Unity.
4. Configurar materiais PBR na Unity (Standard/URP/HDRP, conforme o pipeline do laboratório), conectando corretamente os mapas já produzidos (Albedo, mapa ORM ou Metallic/Roughness separados, Normal Map) aos slots equivalentes do shader da Unity.
5. Executar um lightmap bake simples da cena com todos os assets do kit montados, ajustando parâmetros básicos de iluminação (luz direcional, intensidade, resolução de lightmap) para uma primeira leitura coerente do ambiente.
6. Capturar renders finais da cena montada na Unity sob a iluminação baked, a partir de múltiplos ângulos, como primeira evidência visual do kit modular funcionando como um todo integrado.

---

## Critérios observados nesta semana

> 🔵 **Crítica Informal.** Não há nota formal nesta semana. C8 (Integração na Unity) aparece pela primeira vez na disciplina — ele só passa a valer nota formal na CF6 (Semana 17), então nesta semana ele é praticado e observado, não avaliado. C7 (Otimização) retorna em observação, pois é na Unity que as decisões de resolução, compressão e channel packing da Semana 15 são finalmente verificadas em contexto de motor real.

| Critério | Status | O que observar |
|---|---|---|
| C1 — Processo de Projeto | obs. | Registro do processo de importação (o que funcionou de primeira, o que precisou de retrabalho) e decisões de configuração de material anotadas |
| C7 — Otimização | obs. — verificação em contexto real | As resoluções e compressões definidas na Semana 15 se comportam bem dentro da Unity, ou houve necessidade de ajuste ao ver o resultado no motor? |
| C8 — Integração na Unity | obs. — primeira prática, sem nota | Materiais com texturas nos slots corretos; normal map com a flag correta ativada; UV2 sem sobreposição; asset em escala coerente na cena |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado na crítica circulante sobre a configuração de materiais e o resultado do lightmap dos colegas |

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Computadores com Unity instalado (versão LTS mais recente disponível no laboratório, com o pipeline URP configurado previamente pelo professor ou técnico de laboratório)
- Projeto Unity vazio ou com cena base já criada para o kit modular, disponibilizado com antecedência pelo professor, para evitar perda de tempo com configuração inicial de projeto
- Todos os assets do kit de cada estudante, já otimizados (atlas, trim, ORM) ao final da Semana 15, com arquivos `.blend` e mapas de textura exportados
- Arquivo de demonstração do professor: um asset simples já com UV1 validado, pronto para receber UV2 ao vivo
- Projetor para demonstração
- Apostila Cap. 11 e Cap. 12 — trechos de lightmap UV e importação/configuração na Unity, disponibilizados antes da aula
- Luz direcional (Directional Light) configurada na cena base, para uso imediato no lightmap bake

> **Preparação do laboratório:** É necessário confirmar, antes da aula, que a Unity está instalada e o pipeline URP funcional em todas as máquinas — problemas de instalação nesta etapa final da disciplina custam tempo de estúdio que não pode ser recuperado nas duas últimas semanas.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Do arquivo de produção à cena no motor: UV2, lightmap e materiais na Unity**

Objetivo: fazer o estudante entender que integrar ao motor não é apenas "importar o arquivo" — é preparar o asset com uma camada de informação nova (UV2) e reconfigurar os mapas PBR dentro de um sistema de material diferente do usado até aqui.

**Abertura:**

Exibir no projetor o mesmo asset do kit em duas situações: o material completo aberto no Blender (Principled BSDF, todos os nós conectados) e o mesmo asset ainda sem material, cinza, recém-importado na Unity. Perguntar: *"Tudo que vocês fizeram nas últimas 15 semanas está guardado nesses mapas de textura. Por que será que, ao importar para a Unity, o objeto aparece cinza, sem nenhum material aplicado automaticamente?"*

Deixar 2–3 respostas. Direcionar para a ideia central: a Unity não lê o node setup do Blender — ela só recebe a geometria, o UV e os arquivos de textura brutos. O trabalho de hoje é reconstruir, dentro do sistema de material da Unity, a mesma lógica de leitura de mapas que já existe no Blender, mais uma camada de UV nova que nunca foi necessária até agora: o lightmap.

---

**Conteúdo a cobrir:**

**1. UV2: por que a iluminação baked precisa de um mapa próprio**

O UV1, usado desde a Semana 2, foi otimizado para textura: pode ter ilhas sobrepostas (Semana 13, atlas) ou repetidas por tiling (Semana 14, trim sheet) — sobreposição aí é desejável, porque a mesma região de textura é reaproveitada em várias partes do objeto. Um lightmap, ao contrário, registra a luz **incidente sobre cada ponto da superfície** — se duas regiões da malha compartilham o mesmo espaço de UV, elas vão "vazar" luz uma para a outra no resultado baked, mesmo que sejam partes fisicamente distintas do objeto. Por isso, todo asset que vai receber lightmap precisa de um segundo canal de UV (UV2), exclusivo para essa finalidade, sem nenhuma sobreposição entre ilhas — mesmo que o UV1 do mesmo objeto tenha sobreposição intencional.

*"UV1 responde a pergunta 'que pixel de textura aparece aqui?'. UV2 responde a uma pergunta diferente: 'quanta luz chega exatamente neste ponto da superfície?'. Como a resposta da segunda pergunta é única para cada ponto físico do objeto, o UV2 não pode ter sobreposição — cada centímetro da malha precisa do seu próprio espaço exclusivo no lightmap."*

**2. Gerando UV2 no Blender**

O Blender oferece uma opção de geração automática de um segundo canal de UV, com regras de empacotamento adequadas para lightmap (sem sobreposição, com padding entre ilhas). Esse UV2 é gerado independentemente do UV1 já existente e não o substitui — ambos convivem no mesmo objeto e são exportados juntos.

*"Vocês não vão reabrir o UV1 que já está pronto e validado desde as primeiras semanas. UV2 é um mapa adicional, gerado de forma automática na maioria dos casos, que existe só para a luz — o UV1 continua sendo o responsável pela aparência da textura."*

**3. Materiais na Unity: reconstruindo o fluxo PBR em outro shader**

O shader padrão da Unity (Lit, no URP) espera os mapas PBR em slots próprios: Base Map (Albedo), Normal Map, e um slot combinado de Metallic/Smoothness (ou Mask Map, dependendo do pipeline). Isso exige atenção a duas diferenças em relação ao que foi produzido no Blender: primeiro, o slot de "Smoothness" da Unity é o inverso do Roughness usado até aqui (superfície mais lisa = valor mais alto), o que pode exigir inverter o canal correspondente do mapa ORM produzido na Semana 15. Segundo, o Normal Map importado precisa ter a flag de importação "Normal Map" ativada no Inspector da Unity — sem isso, a textura é lida como cor comum e o resultado fica visualmente incorreto.

*"Os mapas que vocês já produziram estão certos — o trabalho técnico e artístico das últimas 15 semanas não muda. O que muda é o container que lê esses mapas. É como levar a mesma receita de um forno para outro: os ingredientes são os mesmos, mas o forno tem os próprios botões e você precisa saber onde cada um fica."*

**4. Lightmap bake: da malha estática à iluminação calculada**

Para que um objeto receba lightmap bake na Unity, ele precisa estar marcado como estático (Static, ou especificamente Contribute GI). O processo de bake calcula a iluminação indireta da cena (luz que rebate entre superfícies) e a grava como textura no UV2 de cada objeto — sendo por isso que o UV2 sem sobreposição é pré-requisito, não detalhe técnico secundário.

*"O bake de lightmap da Unity é conceitualmente parecido com o bake de Normal Map e AO que vocês já fizeram no Blender nas Semanas 11 e 12: em ambos os casos, uma informação complexa (luz, ou detalhe de superfície) é calculada uma vez e gravada como textura, para não precisar ser recalculada em tempo real."*

> **Nota do professor:** Reforçar que esta é a primeira vez na disciplina que o estudante trabalha com um sistema de UV e material fora do par Blender/3D Coat. É esperado e normal que a primeira importação de cada estudante tenha pelo menos um problema (normal map incorreto, smoothness invertido, ou lightmap com vazamento) — o objetivo da semana é o primeiro ciclo completo de diagnóstico e correção nesse ambiente novo, não a perfeição na primeira tentativa.

---

### Demonstração — 20 minutos

**Do Blender à cena Unity: UV2, exportação, material e primeiro lightmap bake**

**Setup (1 min):**
Abrir o asset de demonstração no Blender, já com UV1 validado, e a Unity aberta em uma segunda janela ou monitor, com a cena base já criada.

**Percurso da demonstração:**

**Passo 1 — Geração de UV2 no Blender (4 min):**
1. No asset de demonstração, gerar o segundo canal de UV com a ferramenta de lightmap do Blender.
2. Mostrar no UV Editor a diferença entre o layout do UV1 (com ilhas possivelmente sobrepostas ou repetidas) e o layout do UV2 gerado (sem sobreposição, com padding entre ilhas).

**Passo 2 — Exportação e importação (4 min):**
1. Exportar o asset como FBX, confirmando nas opções de exportação que ambos os canais de UV serão incluídos.
2. Importar o FBX na Unity, arrastando o asset para a cena base.
3. Mostrar o objeto aparecendo cinza (sem material), retomando o gancho da abertura da mini aula.

**Passo 3 — Configuração do material no shader da Unity (8 min):**
1. Criar um novo material no shader Lit (URP) da Unity.
2. Conectar o Albedo ao Base Map, o Normal Map ao slot correspondente (ativando a flag "Normal Map" no Inspector da textura antes de conectar) e o mapa Metallic/Smoothness (ajustando ou invertendo o canal de Roughness/Smoothness conforme necessário).
3. Aplicar o material ao objeto e comparar visualmente com o render de referência do mesmo asset no Blender.

**Passo 4 — Lightmap bake simples (3 min):**
1. Marcar o objeto como Static (Contribute GI).
2. Configurar uma luz direcional simples na cena, se ainda não configurada.
3. Executar o bake de lightmap (Generate Lighting) e mostrar o resultado antes/depois na viewport da Unity.

> **Nota do professor:** Se o tempo de bake for muito longo para caber nos 20 minutos, preparar antecipadamente uma cena já com o bake concluído para mostrar o resultado final, e usar o tempo ao vivo para a parte mais transferível: a configuração do material e o entendimento do UV2.

---

### Produção em Estúdio — 50 minutos

**Geração de UV2, exportação e primeira importação de assets do kit na Unity**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos com três objetivos, na ordem: gerar UV2 de lightmap para os assets do seu kit, exportar em FBX preservando os dois canais de UV, e importar na Unity configurando o material de pelo menos dois assets. Não é necessário ter o kit inteiro montado até o fim deste encontro — o objetivo é validar o processo completo em uma amostra do kit antes de expandir no segundo encontro."*

**Atividade estruturada:**

**Etapa 1 — Geração de UV2 (≈15 min):**
1. Para cada asset do kit, gerar o segundo canal de UV (lightmap) no Blender, sem alterar o UV1 já validado.
2. Verificar visualmente no UV Editor que o UV2 não tem ilhas sobrepostas e possui padding suficiente entre elas.

**Etapa 2 — Exportação em FBX (≈10 min):**
1. Exportar os assets trabalhados em FBX, conferindo que ambos os canais de UV estão incluídos na exportação.
2. Organizar os arquivos exportados em uma pasta clara para importação na Unity.

**Etapa 3 — Importação e primeira configuração de material (≈25 min):**
1. Importar os assets exportados no projeto Unity.
2. Criar e configurar o material de pelo menos dois assets do kit, conectando Albedo, Normal Map (com a flag correta ativada) e o mapa de Metallic/Smoothness.
3. Posicionar os assets configurados na cena base, comparando visualmente o resultado com o render de referência produzido no Blender.

**Papel do professor:**

Circular verificando:

- **O UV2 realmente não tem sobreposição?** Erro mais comum e mais custoso de diagnosticar depois: verificar visualmente o layout do UV2 no UV Editor antes de exportar, não depois do bake já ter apresentado vazamento de luz.
- **A flag "Normal Map" foi ativada na importação da textura?** Verificar diretamente no Inspector da Unity — um Normal Map sem essa flag produz um resultado visualmente estranho, mas nem sempre óbvio para quem está vendo pela primeira vez.
- **O Smoothness está coerente, ou foi conectado como se fosse Roughness sem inverter?** Perguntar: "Essa superfície deveria ser mais lisa ou mais áspera aqui? O valor que você está vendo bate com isso?"

Perguntas de mediação circulante:
- *"Se você girar essa ilha do UV2 no editor, ela toca ou sobrepõe alguma outra ilha? Vamos conferir com o zoom."*
- *"Compare o material na Unity com o render do Blender: alguma coisa parece mais brilhante ou mais opaca do que deveria? Isso costuma ser o Smoothness invertido."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva — 20 minutos

**Formato: circulante, sem nota formal**

**Abertura (2 min):**
*"Hoje é crítica circulante — vou passar de estação em estação vendo os assets já importados e configurados na Unity. Tenham a cena aberta com pelo menos dois assets configurados, e o comparativo com o render do Blender à mão."*

**Dinâmica (16 min):**
Circulação livre pelas estações. Em cada uma, o professor observa o material configurado na Unity e faz perguntas diretas:
- *"Esse Normal Map está com a flag certa? Mostra o Inspector da textura."*
- *"O que você percebeu de diferente entre o render do Blender e o resultado na Unity? O que precisou ajustar?"*
- *"Já testou marcar esse objeto como Static e rodar um bake rápido? O que apareceu?"*

Encorajar comparação entre colegas — *"Troquem de estação com o vizinho por um minuto: o material dele está lendo os mapas do jeito que você esperaria?"* — sem formalizar como avaliação por pares registrada.

**Síntese (2 min):**
*"A maior parte de vocês já tem pelo menos dois assets funcionando corretamente na Unity. O trabalho de hoje no estúdio é expandir isso para o kit inteiro, montar a cena completa e rodar o lightmap bake final — essa cena montada é a primeira vez que o kit inteiro aparece junto, e vai direto para a apresentação da Semana 17."*

---

### Produção em Estúdio — 60 minutos

**Montagem completa da cena, lightmap bake final e captura de renders**

**Consigna:**

> *"Sessenta minutos para três blocos: primeiro, importar e configurar o material de todos os assets restantes do kit. Segundo, montar a cena completa com todos os assets posicionados de forma coerente com o tema do kit modular. Terceiro, rodar o lightmap bake da cena completa e capturar renders finais de pelo menos quatro ângulos."*

**Atividade estruturada:**

**Bloco 1 — Configuração dos assets restantes (≈20 min):**
1. Repetir o processo de importação e configuração de material para os assets do kit ainda não trabalhados no primeiro encontro.
2. Verificar cada um quanto a UV2 sem sobreposição, flag de Normal Map ativada e Smoothness coerente.

**Bloco 2 — Montagem da cena completa (≈20 min):**
1. Posicionar todos os assets do kit na cena, formando uma composição coerente com o tema definido na Semana 1 (ex.: um ambiente modular montado, não apenas objetos soltos lado a lado).
2. Marcar todos os objetos relevantes como Static (Contribute GI) para participarem do bake.
3. Ajustar a luz direcional da cena (intensidade, ângulo) para uma primeira leitura de iluminação coerente com o tema (ex.: luz mais quente para ambientes desérticos, mais fria para cenários sci-fi).

**Bloco 3 — Lightmap bake e captura de renders (≈20 min):**
1. Executar o lightmap bake da cena completa (Generate Lighting).
2. Revisar o resultado: há vazamento de luz visível entre objetos ou dentro de um mesmo asset? Se sim, identificar se o problema está no UV2 (sobreposição) ou no posicionamento dos objetos (muito próximos entre si).
3. Capturar screenshots da cena renderizada a partir de pelo menos 4 ângulos diferentes, documentando o kit modular montado.
4. Salvar o projeto Unity com nomenclatura clara (`[Nome]_Kit_Unity_S16`).

**Papel do professor:**

- Priorizar apoio aos estudantes com vazamento de luz visível no bake (geralmente sintoma de UV2 mal gerado ou objetos sobrepostos na cena) — direcionar para verificação do UV2 antes de tentar ajustar apenas os parâmetros de luz.
- Para estudantes que terminam rápido: sugerir testar variações simples de iluminação (cor, intensidade, ângulo da luz direcional) e comparar o efeito no clima geral da cena, antecipando a discussão de direção artística da apresentação final.
- Perguntas de mediação: *"Olhando a cena montada agora, ela já comunica o tema do seu kit modular mesmo sem nenhuma legenda? O que ajudaria a comunicar isso melhor até a Semana 17?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese técnica)**
*"Hoje o kit modular de vocês apareceu montado, pela primeira vez, dentro de um motor de jogo de verdade — com UV2 de lightmap, materiais reconfigurados no shader da Unity e uma primeira iluminação baked. Essa é a integração final de tudo que foi produzido desde a Semana 1."*

2. **(3 min — Reflexão de fechamento de unidade)**
Pergunta aberta: *"O que foi mais diferente entre trabalhar no Blender/3D Coat e configurar o mesmo material na Unity? O que essa diferença te ensina sobre como um pipeline de produção real funciona entre ferramentas diferentes?"*
Deixar 2–3 respostas. O objetivo é consolidar que a interoperabilidade entre ferramentas é parte central do trabalho de um artista técnico de jogos, não um obstáculo acidental.

3. **(2 min — Antecipação da Semana 17)**
*"Semana que vem é a última: apresentação e defesa do Kit Modular de Ambiente completo. A cena que vocês montaram hoje na Unity, os renders capturados e toda a documentação de processo das últimas 16 semanas vão compor essa apresentação final."*

4. **(2 min — Confirmação das entregas)**
Recapitular nomenclatura de entrega e prazo. Lembrar que os renders de hoje já podem começar a compor a documentação visual (breakdown) exigida na apresentação final, especialmente para o Critério 9 (Apresentação).

---

## Possíveis Dificuldades

**1. Vazamento de luz (light bleeding) no lightmap por sobreposição no UV2**
O erro técnico mais comum e mais confuso para quem faz isso pela primeira vez: se duas ilhas do UV2 se sobrepõem, o bake mistura a iluminação de regiões fisicamente distintas do objeto, produzindo manchas de luz incoerentes. Estratégia: antes de qualquer bake, inspecionar visualmente o UV2 no Blender e confirmar ausência de sobreposição — o problema é muito mais rápido de prevenir no UV do que de diagnosticar depois do bake pronto.

**2. Normal Map sem a flag de importação ativada na Unity**
Um erro silencioso: a textura é importada como imagem comum, o material aceita a conexão sem erro, mas o resultado visual fica sutilmente errado (relevo invertido ou achatado). Estratégia: verificar sistematicamente, para cada Normal Map importado, se a opção "Normal Map" está marcada no Inspector antes de conectar ao material.

**3. Smoothness invertido em relação ao Roughness já produzido**
Como o conceito de Roughness (usado desde a Semana 5) é o inverso do conceito de Smoothness (usado no shader Lit da Unity), estudantes frequentemente conectam o canal sem inverter, produzindo superfícies que parecem mais ásperas ou mais lisas do que o material realmente é. Estratégia: comparar visualmente a superfície na Unity com o render de referência do Blender e perguntar diretamente se a leitura de "brilho" bate com a intenção original do material.

**4. Confusão entre UV1 e UV2 durante a exportação**
Alguns estudantes podem gerar o UV2, mas esquecer de conferir se a exportação FBX está de fato incluindo os dois canais, resultando em um lightmap gerado automaticamente pela Unity (de baixa qualidade) em vez do UV2 planejado manualmente. Estratégia: verificar nas configurações de importação da Unity se o canal de lightmap UV está de fato vindo do FBX, e não sendo gerado automaticamente pelo motor como solução de contingência.

**5. Escala incorreta dos assets ao importar na Unity**
Diferenças de unidade entre Blender e Unity podem fazer os assets aparecerem desproporcionalmente grandes ou pequenos na cena. Estratégia: comparar a escala de um asset com um objeto de referência conhecido na cena (ex.: um cubo de 1 metro) e ajustar a escala de importação, se necessário, antes de prosseguir com a montagem da cena completa.

**6. Tempo insuficiente para configurar o kit inteiro na Unity**
Como em outras semanas de introdução a uma ferramenta nova, o primeiro asset consome mais tempo por exigir diagnóstico de todo o processo; os seguintes tendem a ser mais rápidos, pois os problemas já foram identificados e corrigidos uma vez. Estratégia: priorizar a configuração cuidadosa de dois ou três assets representativos no primeiro encontro e tratar a expansão para o kit completo como o foco do segundo encontro, aceitando que a montagem final da cena aconteça majoritariamente no Bloco 2 do segundo encontro.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante com vazamento de luz visível no bake | Voltar ao Blender e inspecionar visualmente o UV2 no UV Editor, ilha por ilha, procurando sobreposição — resolver na origem (UV) em vez de tentar compensar apenas ajustando parâmetros de luz na Unity. |
| Estudante com Normal Map com aparência estranha (achatado ou invertido) | Verificar diretamente no Inspector da Unity se a flag "Normal Map" está ativada na importação da textura — esse é o primeiro ponto de verificação antes de qualquer outro diagnóstico. |
| Estudante com material parecendo mais brilhante ou mais opaco do que deveria | Comparar lado a lado com o render de referência do Blender e perguntar se o canal de Smoothness foi conectado direto ou precisa de inversão em relação ao Roughness original. |
| Estudante confuso sobre se o lightmap UV vindo é o UV2 planejado ou um gerado automaticamente pela Unity | Checar as configurações de importação do modelo no Inspector da Unity, conferindo se a opção de gerar lightmap UV automaticamente está desativada e se o canal correto do FBX está sendo lido. |
| Estudante com assets em escala visivelmente incorreta na cena | Posicionar um objeto de escala conhecida (cubo de 1 metro) ao lado do asset importado e comparar visualmente, ajustando a escala de importação conforme necessário. |
| Estudante terminando rápido e com qualidade | Propor testar variações de iluminação (cor, intensidade, ângulo) e observar o impacto no clima da cena, ou revisar se algum asset se beneficiaria de ajuste fino adicional de Smoothness/Metallic para leitura mais correta sob a luz baked. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| UV2 de lightmap gerado para os assets do kit, sem sobreposição entre ilhas, visível no UV Editor do Blender | C8 — Integração na Unity (obs.) | A inspeção visual do UV2 confirma ausência de sobreposição e padding adequado entre ilhas? |
| Assets exportados em FBX e importados na Unity preservando UV1 e UV2 | C8 — Integração na Unity (obs.) | A configuração de importação confirma que ambos os canais de UV vieram do arquivo, sem substituição por lightmap UV gerado automaticamente? |
| Materiais configurados no shader da Unity com Albedo, Normal Map (flag correta) e Metallic/Smoothness coerentes com os mapas produzidos | C7 — Otimização (obs.) / C8 — Integração na Unity (obs.) | O resultado visual na Unity é comparável ao render de referência produzido no Blender, sem inversões de canal perceptíveis? |
| Cena completa montada com todos os assets do kit posicionados de forma coerente com o tema | C2 — Direção Artística (obs., revisitado) | A composição da cena comunica o tema do kit modular sem explicação adicional? |
| Lightmap bake da cena executado, sem vazamento de luz perceptível entre objetos ou dentro de um mesmo asset | C8 — Integração na Unity (obs.) | O resultado do bake apresenta manchas de luz incoerentes, ou a iluminação lê corretamente a geometria de cada objeto? |
| Renders finais da cena capturados em ao menos 4 ângulos diferentes | C9 — Apresentação (obs., revisitado) | Os ângulos escolhidos comunicam bem o kit modular como um conjunto coeso, e não apenas objetos isolados? |
| Participação na crítica circulante: comentários referenciando configuração de material, UV2 ou resultado do bake, não apenas impressão visual geral | C10 — Participação (obs.) | O feedback dado menciona um ponto técnico específico (flag de normal map, sobreposição de UV2, escala) ou é genérico? |

---

## Entrega da Semana 16

| Entrega | Formato | Prazo |
|---|---|---|
| Assets do kit com UV2 de lightmap gerado, sem sobreposição | `.blend` atualizado | Até o fim do segundo encontro |
| Projeto Unity com todos os assets do kit importados, materiais configurados e lightmap baked | Pasta de projeto Unity, nomeada `[Nome]_Kit_Unity_S16` | Até o fim do segundo encontro |
| Renders finais da cena renderizada na Unity, em pelo menos 4 ângulos | `.png` ou `.jpg`, pasta `_Renders_S16` | Até o fim do segundo encontro |

> **Nota:** Não há nota formal nesta semana (crítica informal). O material produzido — cena Unity montada, lightmap baked e renders finais — compõe a evidência central de C8 (Integração na Unity) que será formalmente avaliada pela primeira vez na CF6 da Semana 17 (Projeto Final), junto com todos os demais critérios da rubrica.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 16 | 2026*
