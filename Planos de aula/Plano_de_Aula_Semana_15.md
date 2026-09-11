# Plano de Aula — Semana 15
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização, Trim Sheets e Integração na Unity
**Tema:** UDIMs, otimização e integração completa na Unity
**Apostila:** Parte V, Cap. 19 — UDIMs, Texture Arrays e Multi-Tile Texturing; Parte V, Cap. 20 — Compressão, Mipmaps e Packing de Canais; Parte VI, Cap. 21 — Lightmaps e Iluminação em Motores; Parte VI, Cap. 22 — Integração com Unreal Engine e Unity
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — Crítica circulante em estúdio ou comentário coletivo rápido ao final do segundo encontro

---

## Pré-requisito da semana

Os estudantes chegam com:

- Trim Sheet funcional, avaliada formalmente na CF4 — Semana 14, com feedback escrito já recebido
- Texture Atlas (Semana 13) e Trim Sheet (Semana 14) consolidados como as duas ferramentas de otimização por organização espacial do UV
- Materiais PBR completos (Albedo, Metallic, Roughness, Normal) em todos os assets do kit, com bake integrado desde as Semanas 11–12

> **Nota de transição:** As Semanas 13 e 14 resolveram otimização do lado da **organização espacial** do UV — menos texturas distintas, por meio de agrupamento (atlas) ou reutilização por tiling (trim). Esta é a última semana de produção da disciplina antes do Projeto Final: ela fecha a Unidade IV combinando dois assuntos que, juntos, levam o kit inteiro até dentro do motor. Primeiro, o **peso e a estrutura de arquivo** de cada textura já produzida — resolução, compressão, mipmaps e channel packing (mapa ORM). Segundo, a **integração completa na Unity**: um segundo canal de UV dedicado à luz (UV2), a importação de todos os assets do kit, a montagem da fase caminhável e o lightmap bake da cena inteira. É uma semana carregada — o objetivo não é perfeição em cada etapa, mas ter, ao final do segundo encontro, o kit inteiro funcionando como uma cena única, otimizada e iluminada, pronta para a defesa da Semana 16.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que são UDIMs, diferenciando-os do espaço UV único 0–1 e do conceito de Texture Array, e identificar (ou descartar, com justificativa) a necessidade de UDIM no próprio kit.
2. Diferenciar os formatos de compressão de textura para tempo real (BC1, BC3, BC7) e relacionar cada um ao mapa PBR mais adequado.
3. Executar channel packing, combinando Roughness, Metallic e AO em um único mapa ORM (canais R, G, B).
4. Justificar a resolução de cada asset do kit com base em importância visual e distância de câmera esperada, e quantificar a economia de memória obtida com a otimização da Unidade IV.
5. Diferenciar UV1 (textura) de UV2 (lightmap) e gerar um UV2 sem sobreposição para os assets do kit.
6. Importar todos os assets otimizados do kit na Unity, montar a fase caminhável (colisão de piso e limites de percurso) e executar o lightmap bake da cena completa.
7. Capturar evidência visual (renders e um teste de caminhada) do kit modular funcionando como uma cena única e coerente com o tema.

---

## Critérios observados nesta semana

> 🔵 **Crítica Informal.** Não há nota formal nesta semana. C7 (Otimização) segue em observação, com peso crescente de evidência acumulada para o Projeto Final. C8 (Integração na Unity) aparece pela primeira vez na disciplina — ainda em observação, não em nota — preparando o terreno para a CF5 (Projeto Final, Semana 16), quando C8 recebe sua primeira nota formal.

| Critério | Status | O que observar |
|---|---|---|
| C1 — Processo de Projeto | obs. | Tabela de memória antes/depois registrada; processo de importação documentado |
| C4 — Materiais PBR | obs. — revisitado | O mapa ORM reconstituído no motor preserva a leitura física correta de cada canal? |
| C7 — Otimização | obs. — evidência acumulada | Resolução justificada por asset; compressão coerente por tipo de mapa; channel packing sem perda perceptível |
| C8 — Integração na Unity | obs. — primeiro contato | Materiais com texturas nos slots corretos; UV2 sem sobreposição; cena montada e lightmap baked sem vazamento de luz perceptível |
| C10 — Participação (CC) | obs. | Qualidade do feedback dado na crítica circulante |

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x) e Unity (versão LTS mais recente, com pipeline URP configurado previamente pelo professor ou técnico de laboratório)
- Projeto Unity vazio ou com cena base já criada, disponibilizado com antecedência para evitar perda de tempo com setup inicial
- Editor de imagem com suporte a edição por canal (Krita, Photoshop ou equivalente) para o channel packing manual
- Todos os assets do kit de cada estudante, com mapas PBR completos já produzidos nas semanas anteriores
- Arquivo de demonstração do professor: um asset simples já com Roughness/Metallic/AO separados (para o ORM) e com UV1 validado (para gerar UV2 ao vivo)
- Luz direcional (Directional Light) configurada na cena base, para uso imediato no lightmap bake
- Projetor para demonstração
- Apostila — Parte V, Cap. 19 e 20; Parte VI, Cap. 21 e 22 — disponibilizados antes da aula
- Planilha ou tabela simples para o registro da comparação de memória antes/depois

> **Preparação do laboratório:** confirmar com antecedência que a Unity está instalada e o pipeline URP funcional em todas as máquinas — problemas de instalação nesta etapa custam tempo que não pode ser recuperado antes da defesa final. Esta é a semana do evento institucional Pantanal Game Show — sem relação direta com a entrega, mas vale observar a agenda do campus ao planejar o ritmo de estúdio.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Fechando o peso da textura e abrindo a porta para o motor**

Objetivo: cobrir, de forma compacta, os dois assuntos da semana — otimização de peso de arquivo e a diferença entre UV1 e UV2 — o suficiente para o estudante agir com autonomia no estúdio.

**Bloco 1 (≈12 min) — UDIMs, compressão, mipmaps e channel packing**

- **UDIMs:** até aqui todo UV coube em um único espaço 0–1, mesmo compartilhado via atlas (Semana 13). UDIM estende esse espaço para múltiplos tiles numerados, usado apenas quando um asset — tipicamente o hero do kit — precisa de mais resolução do que um tile único comporta. *"É exceção, não regra: a maioria dos kits não precisa de UDIM."* Diferença rápida de Texture Array: UDIM é um recurso de **autoria** (Blender/3D Coat); Texture Array é uma estrutura de **tempo real** do motor, fora do escopo prático desta disciplina.
- **Compressão:** BC1 (Albedo sem alpha, Metallic), BC3 (com transparência), BC7 (Normal Maps e Albedo hero — maior qualidade). *"A pergunta é: qual erro esse mapa específico pode tolerar sem que o olho perceba?"*
- **Mipmaps:** versões pré-calculadas em resolução decrescente, trocadas automaticamente pela distância à câmera — argumento contra superdimensionar resolução de asset pequeno ou distante.
- **Channel packing (mapa ORM):** Roughness, Metallic e AO são grayscale (1 canal útil cada) — combiná-los em R, G, B de uma única imagem elimina dois arquivos sem perda de informação. *"Mesma lógica do atlas da Semana 13, mas combinando mapas em vez de objetos."*

**Bloco 2 (≈8 min) — UV1 vs. UV2: por que a luz baked precisa de um mapa próprio**

O UV1 (desde a Semana 2) foi otimizado para textura — pode ter ilhas sobrepostas (atlas) ou repetidas (trim), porque a mesma região de textura serve a várias partes do objeto. Um lightmap registra a luz incidente sobre **cada ponto físico** da superfície: se duas regiões compartilham o mesmo espaço de UV, elas "vazam" luz uma para a outra no bake. Por isso todo asset que vai para a fase caminhável precisa de um segundo canal de UV (UV2), sem nenhuma sobreposição — o Blender gera isso automaticamente na maioria dos casos, sem substituir o UV1.

*"UV1 responde 'que pixel de textura aparece aqui?'. UV2 responde 'quanta luz chega exatamente neste ponto?'. Por isso UV2 não pode ter sobreposição."*

> **Nota do professor:** Esta é uma mini aula densa — o objetivo não é profundidade teórica, é dar munição suficiente para o estúdio. Cada bloco será retomado na prática, na demonstração e na circulação.

---

### Demonstração — 20 minutos

**Channel packing, UV2 e primeira montagem na Unity**

**Passo 1 — Mapa ORM (6 min):**
1. Combinar Roughness (R), Metallic (G) e AO (B) do asset de demonstração em um único PNG, usando o editor de canais.
2. Reconfigurar o material no Blender: nó `Separate Color` alimentando Roughness, Metallic e (multiplicando) AO. Comparar o render antes/depois — resultado idêntico, um arquivo a menos.

**Passo 2 — UV2 de lightmap (5 min):**
1. No mesmo asset (já com UV1 validado), gerar o UV2 com a ferramenta de lightmap do Blender.
2. Mostrar no UV Editor a diferença: UV1 pode ter sobreposição; UV2 não tem nenhuma, com padding entre ilhas.

**Passo 3 — Exportação e importação completa na Unity (6 min):**
1. Reexportar o asset em FBX confirmando que ambos os canais de UV (UV1 e UV2) são incluídos.
2. Na Unity: criar material URP/Lit, conectar Albedo, Normal (flag "Normal Map" ativada) e o mapa ORM nos slots de Metallic/Smoothness e Occlusion.
3. Marcar o objeto como Static (Contribute GI) e rodar um lightmap bake rápido — mostrar o resultado antes/depois.

**Passo 4 — Cálculo de economia (3 min):**
Comparar o peso em disco dos mapas separados versus o ORM comprimido, como exemplo do dado que os estudantes vão registrar para o próprio kit.

> **Nota do professor:** Se o bake demorar mais que o tempo disponível, preparar uma cena com o bake já concluído e usar o tempo ao vivo para ORM e UV2 — as partes mais transferíveis para o estúdio. Este é o único momento da disciplina em que ORM, UV2 e importação completa aparecem juntos: reforçar que no estúdio esse fluxo se repete para o kit inteiro.

---

### Produção em Estúdio — 50 minutos

**Channel packing, UV2 e primeira leva de importação na Unity**

**Consigna entregue verbalmente:**

> *"Cinquenta minutos, três frentes: criar mapas ORM para os assets do seu kit, gerar UV2 de lightmap para os que ainda não têm, e começar a importar tudo na Unity. Não precisa terminar o kit inteiro hoje — o objetivo é ter o processo rodando em pelo menos dois ou três assets antes de expandir para o resto no segundo encontro."*

**Atividade estruturada:**

**Etapa 1 — Channel packing (≈15 min):**
1. Combinar Roughness/Metallic/AO em ORM para ao menos dois assets do kit.
2. Reconfigurar os materiais no Blender e validar visualmente.

**Etapa 2 — UV2 de lightmap (≈15 min):**
1. Gerar UV2 para os assets do kit que ainda não têm, sem alterar o UV1.
2. Verificar no UV Editor: ausência de sobreposição, padding adequado.

**Etapa 3 — Primeira importação na Unity (≈15 min):**
1. Exportar em FBX os assets já com ORM e UV2 prontos, preservando ambos os canais de UV.
2. Importar na Unity, criar os materiais (Albedo, Normal com flag ativada, ORM em Metallic/Smoothness e Occlusion) e posicionar na cena.

**Etapa 4 — Registro (≈5 min):**
Preencher a tabela de memória (peso antes/depois) para os assets trabalhados. Salvar: `[Nome]_Otimizacao_Integracao_S15.blend`.

**Papel do professor:**

Circular verificando: inversão de canal no ORM (erro mais custoso, verificar canal por canal isolado); UV2 realmente sem sobreposição antes de exportar; resolução justificada por importância visual, não por hábito. Perguntas: *"Esse asset vai aparecer perto da câmera no seu kit, ou é fundo repetido? Isso muda a resolução?"* / *"Se eu isolasse o canal R do seu ORM, eu veria o Roughness?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva — 20 minutos

**Formato: circulante, sem nota formal**

**Abertura (2 min):** *"Hoje é crítica circulante — quero ver o ORM com canais corretos, o UV2 sem sobreposição e o que já está rodando na Unity."*

**Dinâmica (16 min):** Circulação livre. Em cada estação: *"Mostra o canal R isolado do ORM."* / *"Essa ilha do UV2 sobrepõe alguma outra?"* / *"O que você percebeu de diferente entre o render do Blender e o resultado na Unity?"* Encorajar comparação entre colegas sobre a lógica de resolução hero/secundário/fundo.

**Síntese (2 min):** *"A maioria já tem o processo rodando em alguns assets. O estúdio de hoje é expandir para o kit inteiro, montar a fase caminhável completa e rodar o lightmap bake final — essa é a cena que vai direto para a defesa da Semana 16."*

---

### Produção em Estúdio — 60 minutos

**Montagem completa da fase caminhável e lightmap bake final**

**Consigna:**

> *"Sessenta minutos para fechar a semana: primeiro, expandir ORM e UV2 para os assets restantes do kit e importar tudo na Unity. Segundo, montar a fase caminhável — todos os assets posicionados de forma coerente, com colisão de piso e limites de percurso, sem gameplay adicional. Terceiro, rodar o lightmap bake da cena completa e capturar renders e um teste de caminhada."*

**Atividade estruturada:**

**Bloco 1 — Expansão do ORM/UV2 e importação restante (≈20 min):**
1. Repetir o processo de channel packing e UV2 para os assets do kit ainda não trabalhados.
2. Importar todos os assets restantes na Unity, configurando os materiais.

**Bloco 2 — Montagem da fase caminhável (≈20 min):**
1. Posicionar todos os assets do kit na cena, formando uma composição coerente com o tema regional definido desde a Semana 1.
2. Configurar colisão de piso e limites de percurso simples (paredes ou barreiras invisíveis), permitindo que a cena seja percorrida a pé — sem gameplay além da locomoção.
3. Marcar os objetos relevantes como Static (Contribute GI) e ajustar a luz direcional (intensidade, ângulo, cor) coerente com o tema.

**Bloco 3 — Lightmap bake e captura de evidência (≈15 min):**
1. Executar o lightmap bake da cena completa (Generate Lighting).
2. Revisar vazamento de luz: se houver, verificar primeiro o UV2 (sobreposição) antes de ajustar parâmetros de luz.
3. Capturar screenshots de pelo menos 4 ângulos e um vídeo curto ou gif de teste de caminhada pela fase.

**Bloco 4 — Fechamento da tabela de memória e registro (≈5 min):**
1. Consolidar a tabela de memória do kit completo (antes da Unidade IV × depois de atlas, trim, ORM e compressão).
2. Salvar o projeto Unity: `[Nome]_Kit_Unity_S15`.

**Papel do professor:**

Priorizar apoio a vazamento de luz no bake (sintoma de UV2 mal gerado ou objetos sobrepostos na cena) e a inversão de canal no ORM. Para quem termina rápido: testar variações de iluminação (cor, intensidade, ângulo) e observar o impacto no clima da cena, antecipando a discussão de direção artística da defesa. Perguntas de mediação: *"A cena já comunica o tema do seu kit mesmo sem legenda? O que ajudaria a comunicar melhor até a Semana 16?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(3 min — Síntese técnica)** *"Hoje vocês fecharam a Unidade IV e viram o kit inteiro, pela primeira vez, montado como uma cena única dentro de um motor de jogo — com otimização de arquivo e iluminação baked. É a integração final de tudo que foi produzido desde a Semana 1."*

2. **(3 min — Reflexão de fechamento de unidade)** Pergunta aberta: *"Das quatro ferramentas de otimização desta unidade — atlas, trim, ORM e UDIM — qual vocês acham que vão usar mais no futuro, fora da disciplina? E o que foi mais diferente entre trabalhar no Blender/3D Coat e montar a cena na Unity?"* Deixar 2–3 respostas.

3. **(2 min — Antecipação da Semana 16)** *"Semana que vem é a última com crítica coletiva: apresentação e defesa do Kit Modular e da fase caminhável que vocês acabaram de montar. A cena de hoje, os renders e o vídeo de caminhada vão compor essa apresentação."*

4. **(2 min — Confirmação das entregas)** Recapitular nomenclatura de entrega. Lembrar que a tabela de memória e a cena montada hoje compõem evidência de C7 e o primeiro contato de C8 para a CF5 da Semana 16.

---

## Possíveis Dificuldades

**1. Inversão de canais no channel packing**
Colocar Metallic no canal errado produz um material fisicamente incoerente, só percebido quando o shader lê o canal certo. Estratégia: inspecionar cada canal do ORM isoladamente e comparar com o mapa de origem.

**2. Vazamento de luz (light bleeding) no lightmap por sobreposição no UV2**
Erro técnico mais comum na primeira tentativa de UV2. Estratégia: inspecionar visualmente o UV2 antes de qualquer bake — prevenir no UV é mais rápido que diagnosticar depois do bake pronto.

**3. Normal Map sem a flag de importação ativada na Unity**
Erro silencioso: relevo invertido ou achatado. Estratégia: verificar sistematicamente a opção "Normal Map" no Inspector antes de conectar ao material.

**4. Tempo insuficiente para o kit inteiro**
A semana cobre muito conteúdo em pouco tempo. Estratégia: priorizar o asset hero e dois ou três secundários no primeiro encontro; tratar a expansão completa e a montagem da cena como o foco do segundo encontro, aceitando que o kit chegue "quase completo" ao final, com o restante ajustável na Semana 16.

**5. Escala incorreta dos assets ao importar na Unity**
Diferenças de unidade entre Blender e Unity podem distorcer o tamanho. Estratégia: comparar com um objeto de escala conhecida (cubo de 1 metro) e ajustar a escala de importação.

**6. Aplicar UDIM sem necessidade real**
Estratégia: reforçar que UDIM é solução de exceção — perguntar se o asset realmente perde detalhe perceptível em um único tile antes de justificar seu uso.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante inseguro se inverteu canal no ORM | Isolar visualmente cada canal (R, G, B) e comparar com o mapa de origem correspondente. |
| Estudante com vazamento de luz no bake | Voltar ao Blender e inspecionar o UV2 ilha por ilha antes de mexer nos parâmetros de luz. |
| Estudante com Normal Map de aparência estranha | Verificar a flag "Normal Map" no Inspector da Unity antes de qualquer outro diagnóstico. |
| Estudante mantendo a mesma resolução em todos os assets por hábito | Pedir classificação hero/secundário/fundo antes de qualquer decisão de resolução. |
| Estudante com assets em escala incorreta na cena | Posicionar um cubo de 1 metro ao lado do asset importado e comparar visualmente. |
| Estudante terminando rápido e com qualidade | Propor testar variações de iluminação e revisar compressão mapa a mapa, calculando a economia acumulada desde a Semana 13. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Mapa(s) ORM com canais R/G/B correspondendo corretamente a Roughness, Metallic e AO | C7 — Otimização / C4 — Materiais PBR | Verificação por canal isolado confirma ausência de inversão |
| UV2 de lightmap gerado sem sobreposição entre ilhas | C8 — Integração na Unity (obs.) | Inspeção visual confirma ausência de sobreposição e padding adequado |
| Tabela comparativa de memória (antes/depois da Unidade IV) | C1 — Processo de Projeto / C7 — Otimização | Economia quantificada com números concretos |
| Fase caminhável montada na Unity com todos os assets do kit, materiais ORM e lightmap baked sem vazamento de luz perceptível | C8 — Integração na Unity (obs.) | Cena funcional, iluminação coerente, sem manchas de luz incoerentes |
| Renders (4 ângulos) e teste de caminhada (vídeo ou gif) | C9 — Apresentação (obs.) | Os ângulos e o percurso comunicam o kit modular como um conjunto coeso |
| Participação na crítica circulante com observação técnica específica | C10 — Participação (obs.) | O feedback referencia canal, UV2, resolução ou bake, ou é genérico? |

---

## Entrega da Semana 15

| Entrega | Formato | Prazo |
|---|---|---|
| Mapas ORM de todos os assets do kit | `.png`, pasta `_ORM_S15` | Até o fim do segundo encontro |
| Assets com UV2 de lightmap gerado, sem sobreposição | `.blend` atualizado | Até o fim do segundo encontro |
| Tabela comparativa de memória (antes/depois) | Documento digital ou planilha | Até o fim do segundo encontro |
| Fase caminhável montada na Unity com todos os assets do kit importados, materiais otimizados (ORM) e lightmap baked | Pasta de projeto Unity `[Nome]_Kit_Unity_S15` | Até o fim do segundo encontro |
| Renders da cena (4 ângulos) + teste de caminhada (vídeo curto ou gif) | `.png`/`.jpg` + `.mp4`/`.gif`, pasta `_Renders_S15` | Até o fim do segundo encontro |

> **Nota:** Não há nota formal nesta semana (crítica informal). A tabela de memória, o ORM e a fase caminhável montada compõem o conjunto de evidências acumuladas de C7 e o primeiro contato de C8, que serão formalmente avaliados na CF5 — Projeto Final, na Semana 16.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 15 | 2026*
