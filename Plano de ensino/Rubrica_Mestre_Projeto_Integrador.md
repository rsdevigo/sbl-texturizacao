# Rubrica Mestre do Projeto Integrador de Texturização

**Disciplina:** Texturização — Curso Superior de Tecnologia em Jogos Digitais  
**Metodologia:** Studio-Based Learning (SBL)  
**Projeto:** Kit Modular de Ambiente (tema definido pelos estudantes)  
**Pipeline:** Blender → 3D Coat → Unity  

---

## Sobre este documento

Esta rubrica é o instrumento avaliativo central da disciplina. Ela acompanha o estudante durante todo o semestre e serve de base para:

- **Críticas formais** periódicas (CF1–CF5, semanas 3, 5, 8, 11, 14) — compõem o Portfolio de Artefatos (PA)
- **Autoavaliação** (antes de cada crítica formal)
- **Avaliação por pares** (críticas coletivas formais e informais) — compõe as Críticas Coletivas (CC)
- **Avaliação final** (CF6, semana 17) — Projeto Final (PF)

Todos os critérios são **observáveis e verificáveis**. O avaliador deve conseguir justificar o nível atribuído apontando evidências concretas no trabalho do estudante.

---

## Escala de Desempenho

| Nível | Nome | Descrição Geral |
|---|---|---|
| 1 | **Insuficiente** | O estudante não atendeu ao critério. Há ausência de evidências ou o trabalho está incompleto a ponto de impossibilitar a avaliação. |
| 2 | **Em Desenvolvimento** | O estudante demonstra tentativa de atender ao critério, mas com erros significativos, inconsistências ou incompreensão parcial do conceito. |
| 3 | **Adequado** | O estudante atende ao critério de forma funcional. O trabalho cumpre o mínimo esperado sem erros graves, mas sem refinamento. |
| 4 | **Bom** | O estudante atende ao critério com qualidade acima do esperado. Há evidências de compreensão aprofundada e atenção ao detalhe. |
| 5 | **Excelente** | O estudante supera as expectativas do critério. O trabalho demonstra domínio técnico, intenção artística clara e pode servir de referência para a turma. |

---

## Critérios de Avaliação

---

### Critério 1 — Processo de Projeto

> Avalia a qualidade do processo de trabalho ao longo do semestre: como o estudante planeja, organiza, registra decisões e evolui a partir do feedback recebido.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Não há registro de processo. O estudante não apresenta rascunhos, referências organizadas ou histórico de versões. Não é possível identificar evolução entre sessões. |
| 2 — Em Desenvolvimento | Existe algum registro, mas fragmentado e sem organização. O estudante demonstra dificuldade em retomar o trabalho de onde parou. Feedback recebido raramente aparece incorporado nas versões seguintes. |
| 3 — Adequado | O estudante mantém um registro básico de processo (pasta de referências, versões numeradas, anotações de crítica). Incorpora parte dos feedbacks recebidos nas iterações seguintes. |
| 4 — Bom | O processo é bem documentado: referências organizadas por categoria, versões com identificação de data, anotações sobre decisões tomadas e justificativas. O feedback é incorporado de forma consistente e o estudante consegue explicar o que mudou entre versões. |
| 5 — Excelente | O estudante mantém um registro de processo exemplar. Há moodboard atualizado, breakdown de decisões técnicas e artísticas, histórico de iterações com comparativos visuais. O feedback não apenas é incorporado — o estudante demonstra reflexão sobre por que aceitou ou recusou cada sugestão. |

**Evidências esperadas:** pasta de projeto organizada, moodboard, versões salvas, anotações de critique, comparativos before/after.

---

### Critério 2 — Direção Artística

> Avalia a coerência visual do projeto, a consistência entre os elementos do kit e a clareza da proposta estética.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | O kit não apresenta identidade visual reconhecível. Os elementos não possuem relação estética entre si. O estudante não consegue descrever a proposta visual do projeto. |
| 2 — Em Desenvolvimento | Existe uma intenção visual, mas ela não se sustenta ao longo dos assets. Elementos do kit apresentam estilos visuais distintos que não dialogam entre si. |
| 3 — Adequado | O kit apresenta uma paleta de cores e estilo visual definidos. Os elementos principais compartilham linguagem visual reconhecível, mesmo que com variações pontuais. |
| 4 — Bom | O projeto possui direção artística clara e documentada. Paleta, linguagem de materiais e nível de detalhe são consistentes em todos os assets. O estudante consegue descrever e justificar as escolhas estéticas. |
| 5 — Excelente | O projeto demonstra direção artística madura e coesa. A proposta visual é comunicada com precisão (moodboard, referências, descrição verbal) e se reflete fielmente em todos os assets. O kit tem identidade própria e reconhecível. |

**Evidências esperadas:** moodboard, paleta de cores, consistência visual entre assets, capacidade de verbalizar a proposta.

---

### Critério 3 — UV Mapping

> Avalia a qualidade do layout de UV: organização, eficiência de espaço, ausência de distorção e preparação para produção.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | UVs sobrepostas, invertidas ou ausentes. O mapa de textura não pode ser aplicado de forma funcional. |
| 2 — Em Desenvolvimento | UVs desdobradas mas com problemas graves: distorção visível em superfícies planas ou curvas, escala inconsistente entre peças do mesmo kit, espaço UV mal aproveitado (menos de 50% de ocupação). |
| 3 — Adequado | UVs funcionais sem sobreposição. Escala razoavelmente consistente. Distorção aceitável em superfícies secundárias. Ocupação do espaço entre 50% e 70%. |
| 4 — Bom | UVs organizadas com ilhas alinhadas, escala consistente entre todos os assets do kit, distorção mínima ou ausente. Ocupação do espaço acima de 70%. Seams posicionados em locais onde não aparecem em renders. |
| 5 — Excelente | UV layout otimizado: texel density uniforme e verificado, seams invisíveis, ocupação acima de 85%, ilhas rotacionadas e empacotadas para máxima eficiência. O layout está pronto para produção sem retrabalho. |

**Evidências esperadas:** visualização do UV editor com checker map aplicado, texel density consistente, ausência de estiramento.

---

### Critério 4 — Materiais PBR

> Avalia o uso correto do fluxo PBR: plausibilidade física, qualidade dos mapas e coerência com propriedades reais dos materiais representados.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Materiais sem configuração PBR. Uso de valores de cor plana sem mapas ou com configuração incorreta dos canais (ex: metal com roughness 0, superfícies matte com valor de metallic > 0). |
| 2 — Em Desenvolvimento | Existe configuração PBR básica, mas com erros que comprometem a plausibilidade física: roughness uniforme sem variação, metallic mal calibrado, albedo com iluminação "baked" desnecessária. |
| 3 — Adequado | Os materiais seguem o fluxo PBR correto. Albedo sem iluminação, roughness com variação funcional, metallic dentro dos valores corretos (0 para dielétricos, 1 para metais). A aparência é crível mesmo sem refinamento artístico. |
| 4 — Bom | Materiais bem configurados com variação de roughness informada por lógica de uso (áreas de desgaste mais polidas, áreas protegidas mais matte). Mapas com resolução adequada e sem artefatos. Leitura visual clara à distância de uso. |
| 5 — Excelente | Materiais com plausibilidade física impecável e refinamento artístico. Variação de roughness e metallic baseada em referência real. Micro-variações de albedo que evitam a aparência de "plástico". O material responde corretamente à iluminação em diferentes condições de luz. |

**Evidências esperadas:** render com e sem iluminação, visualização dos mapas individuais (albedo, roughness, metallic, normal), valores dentro do range correto de PBR.

---

### Critério 5 — Texturização

> Avalia a qualidade artística da texturização: detalhamento, variação visual, narrativa de uso e desgaste.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Textura ausente ou com apenas cor plana. O asset não apresenta nenhum detalhe de superfície. |
| 2 — Em Desenvolvimento | Textura presente mas repetitiva, sem variação. Desgaste ou sujeira aplicados de forma uniforme e irreal. O asset parece "novo demais" ou "sujo demais" sem narrativa. |
| 3 — Adequado | Textura com detalhamento básico (variação de cor, micro-rugosidade). Algum uso de desgaste em arestas ou áreas de contato. A superfície é crível e evita aparência completamente uniforme. |
| 4 — Bom | Texturização com camadas de detalhe: base, variação de cor, desgaste em arestas, sujeira acumulada em áreas protegidas e baixas. Narrativa de uso perceptível. A textura comunica a história do objeto. |
| 5 — Excelente | Texturização com profundidade narrativa e artística. Desgaste diferenciado por tipo de uso (impacto, fricção, oxidação). Sujeira acumulada com lógica gravitacional e de uso. Micro-detalhes (poros, riscos finos, variação de material) visíveis em close-up sem comprometer a leitura à distância de uso. |

**Evidências esperadas:** renders em close-up e à distância de uso, comparativo com referência visual, isolamento dos mapas de detalhe.

---

### Critério 6 — Bake

> Avalia a qualidade do processo de bake: transferência de detalhes do high poly para o low poly, ausência de artefatos e organização do workflow.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Bake não realizado ou com falha completa (erros de projeção, artefatos que cobrem mais de 50% do asset). Os mapas gerados não podem ser utilizados. |
| 2 — Em Desenvolvimento | Bake realizado mas com artefatos visíveis: normal map com "manchas" em superfícies planas, ambient occlusion com bleeding entre ilhas, seams visíveis no resultado final. |
| 3 — Adequado | Bake funcional com artefatos mínimos. Normal map transfere os detalhes principais do high poly. Ambient occlusion sem bleeding significativo. Seams aceitáveis à distância de uso. |
| 4 — Bom | Bake de alta qualidade: normal map com transferência fiel de detalhes, AO limpa e consistente, curvature map utilizável para mascaramento. Seams invisíveis. O workflow de bake está documentado (cage, ray distance, grupos de bake). |
| 5 — Excelente | Bake exemplar com todos os mapas necessários gerados corretamente (normal, AO, curvature, thickness, position). Normal map sem artefatos mesmo em ângulos críticos. O estudante demonstra compreensão dos parâmetros de bake e consegue explicar cada decisão tomada no processo. |

**Evidências esperadas:** visualização do normal map no viewport, comparativo high poly / low poly com normal aplicado, ausência de seams visíveis.

---

### Critério 7 — Otimização

> Avalia as decisões de otimização: resolução de textura, uso de atlas, trim sheets e eficiência geral do asset para uso em tempo real.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Nenhuma consideração de otimização. Texturas em resoluções inconsistentes ou desnecessariamente altas. Assets com UVs que impossibilitam o uso compartilhado de texturas. |
| 2 — Em Desenvolvimento | Existe alguma tentativa de otimização, mas sem critério claro: resoluções mistas sem lógica de LOD, atlas criado mas mal organizado, trim sheets tentados mas com erros de tiling. |
| 3 — Adequado | Resoluções de textura adequadas ao tamanho e importância do asset. Uso funcional de atlas para assets menores. Trim sheets aplicados em pelo menos um elemento do kit. |
| 4 — Bom | Estratégia de otimização clara e aplicada consistentemente: atlas organizados por categoria de asset, trim sheets utilizados para elementos repetitivos (molduras, painéis, bordas), channel packing implementado (ex: roughness no canal R, AO no G, metallic no B). |
| 5 — Excelente | Otimização exemplar com justificativa técnica para cada decisão. O estudante consegue quantificar o ganho de memória de cada escolha. Uso inteligente de trim sheets reduz o número de texturas únicas sem comprometer a variedade visual. Channel packing correto e documentado. O kit completo utiliza o mínimo necessário de texturas únicas. |

**Evidências esperadas:** documentação das resoluções utilizadas, visualização do atlas UV, exemplo de trim sheet aplicado, número total de texturas do kit.

---

### Critério 8 — Integração na Unity

> Avalia a configuração correta dos materiais na Unity e a aparência final do asset no motor de jogo.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Assets não importados ou com configuração incorreta (texturas não conectadas, normais invertidas, materiais ausentes). O asset não aparece corretamente no motor. |
| 2 — Em Desenvolvimento | Assets importados mas com problemas de configuração: normal map sem a flag "Normal Map" ativada, roughness/metallic em slots incorretos, escala incorreta no scene. |
| 3 — Adequado | Assets importados e configurados corretamente. Materiais com texturas nos slots corretos (Albedo, Normal, Metallic/Smoothness). O asset aparece como esperado sob iluminação padrão. |
| 4 — Bom | Configuração cuidadosa: normal maps com intensidade calibrada, valores de smoothness/metallic ajustados para o motor, assets em escala correta. O kit montado em cena demonstra coerência visual sob diferentes condições de iluminação. |
| 5 — Excelente | Integração exemplar: assets configurados para o pipeline de renderização correto (URP/HDRP), iluminação de apresentação preparada, prefabs organizados com nomenclatura clara. O estudante demonstra que o kit funciona como um produto utilizável por outro artista ou desenvolvedor sem retrabalho. |

**Evidências esperadas:** screenshot da Unity com o asset montado, configuração dos materiais no Inspector, renders com diferentes condições de luz.

---

### Critério 9 — Apresentação

> Avalia a organização dos arquivos entregues, a qualidade da documentação e a capacidade de apresentar e defender o trabalho.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | Entrega incompleta ou desorganizada. Arquivos sem nomenclatura padronizada, ausência de documentação. O estudante não consegue apresentar o trabalho de forma compreensível. |
| 2 — Em Desenvolvimento | Entrega com estrutura parcial. Alguns arquivos nomeados corretamente, documentação mínima ou ausente. A apresentação oral é confusa ou depende de explicações longas para compensar a falta de organização visual. |
| 3 — Adequado | Entrega organizada com nomenclatura consistente. Há documentação básica (nome do projeto, lista de assets, texturas utilizadas). A apresentação é clara o suficiente para que o avaliador compreenda o trabalho sem auxílio extra. |
| 4 — Bom | Entrega bem organizada com pasta estruturada, nomenclatura padronizada e documentação que inclui decisões de projeto, referências visuais e lista de otimizações aplicadas. A apresentação é fluente e o estudante consegue responder perguntas técnicas sobre o processo. |
| 5 — Excelente | A entrega é um portfólio de projeto. Inclui breakdown visual (wireframe, UVs, mapas individuais, comparativo antes/depois), documentação completa e apresentação que comunica tanto o processo quanto o resultado. O estudante antecipa perguntas e demonstra domínio sobre cada decisão tomada. |

**Evidências esperadas:** estrutura de pasta da entrega, documento de apresentação, qualidade do breakdown visual.

---

### Critério 10 — Participação nas Critiques

> Avalia o engajamento do estudante nas críticas coletivas: qualidade do feedback oferecido, recepção de críticas e justificativa de decisões.

| Nível | Descrição Observável |
|---|---|
| 1 — Insuficiente | O estudante não participa das críticas ou participa de forma passiva (não fala, não responde). Feedback oferecido é vago ou ausente ("tá bom", "não sei"). |
| 2 — Em Desenvolvimento | O estudante participa mas com dificuldade. Feedback oferecido é genérico ("poderia melhorar a textura"). Quando recebe crítica, demonstra resistência ou aceita sem reflexão. Tem dificuldade de justificar suas escolhas. |
| 3 — Adequado | O estudante participa regularmente. Oferece feedback observável ("o roughness dessa área parece uniforme demais, sem variação"). Recebe críticas sem resistência e registra o que foi discutido. Consegue descrever as decisões tomadas, mesmo que sem justificativa aprofundada. |
| 4 — Bom | O estudante contribui ativamente. Feedback é específico e construtivo, referenciando critérios técnicos e/ou referências visuais. Quando recebe crítica, questiona, negocia e explica seu ponto de vista com argumentos técnicos ou artísticos. |
| 5 — Excelente | O estudante é um participante exemplar das críticas. Oferece feedback que ajuda o colega a enxergar o próprio trabalho de forma nova. Quando apresenta seu trabalho, antecipa críticas e demonstra que já realizou autoavaliação. É capaz de discordar de feedback com argumentação técnica respeitosa e fundamentada. |

**Evidências esperadas:** observação direta durante as críticas, registros de anotações pós-critique, qualidade das autoavaliações entregues.

---

## Pesos por Momento Avaliativo

### Conexão com os Instrumentos do Plano de Ensino

Os 6 momentos de crítica formal conectam-se diretamente aos três instrumentos avaliativos definidos no Plano de Ensino:

| Instrumento | Corresponde a | Peso na Nota Final |
|---|---|---|
| **Portfolio de Artefatos (PA)** | CF1 a CF5 — semanas 3, 5, 8, 11 e 14 | 40% |
| **Críticas Coletivas (CC)** | C10 — Participação, registrado em todas as CF | 20% |
| **Projeto Final (PF)** | CF6 — Apresentação e defesa (semana 17) | 40% |

```
NF = (PA × 0,40) + (CC × 0,20) + (PF × 0,40)
```

A nota do **PA** é calculada com **pesos crescentes** entre CF1 e CF5, valorizando a trajetória de aprendizado — um aluno que melhora consistentemente é recompensado pelo estado avançado do trabalho, não penalizado pelas notas iniciais quando ainda estava formando o conhecimento:

| Crítica Formal | Semana | Peso no PA |
|---|---|---|
| CF1 | 3 | 10% |
| CF2 | 5 | 15% |
| CF3 | 8 | 20% |
| CF4 | 11 | 25% |
| CF5 | 14 | 30% |
| **Total** | | **100%** |

A nota de **CC** é consolidada pelo professor a partir dos registros de C10 ao longo de todas as CF. O **PF** é a avaliação da CF6.

---

### Critérios Ativos por Crítica Formal

A tabela indica quais critérios são formalmente avaliados em cada CF. Critérios marcados como *obs.* são observados e registrados, mas não compõem a nota daquela CF.

| Critério | CF1 (Sem. 3) | CF2 (Sem. 5) | CF3 (Sem. 8) | CF4 (Sem. 11) | CF5 (Sem. 14) | CF6 (Sem. 17) |
|---|---|---|---|---|---|---|
| C1 — Processo de Projeto | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| C2 — Direção Artística | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| C3 — UV Mapping | ✓ | ✓ | obs. | — | — | ✓ |
| C4 — Materiais PBR | — | ✓ | ✓ | ✓ | obs. | ✓ |
| C5 — Texturização | — | — | ✓ | ✓ | ✓ | ✓ |
| C6 — Bake | — | — | — | ✓ | ✓ | ✓ |
| C7 — Otimização | — | — | — | — | ✓ | ✓ |
| C8 — Integração na Unity | — | — | — | — | — | ✓ |
| C9 — Apresentação | — | — | — | — | ✓ | ✓ |
| C10 — Participação (CC) | obs. | obs. | obs. | obs. | obs. | ✓ |

> **Legenda:** ✓ = critério avaliado e registrado nesta CF | obs. = observado e anotado, não compõe nota | — = não aplicável ainda

---

#### Avaliação Final (Semana 17 — CF6 / Projeto Final)

> Avalia o projeto completo integrado na apresentação e defesa final. Todos os critérios são considerados.

| Critério | Peso |
|---|---|
| C1 — Processo de Projeto | 10% |
| C2 — Direção Artística | 12% |
| C3 — UV Mapping | 8% |
| C4 — Materiais PBR | 12% |
| C5 — Texturização | 14% |
| C6 — Bake | 8% |
| C7 — Otimização | 8% |
| C8 — Integração na Unity | 12% |
| C9 — Apresentação | 8% |
| C10 — Participação nas Critiques | 8% |
| **Total** | **100%** |

---

### Justificativa Pedagógica dos Pesos

**C5 — Texturização (14%)** recebe o maior peso na avaliação final por ser o núcleo da disciplina e o critério que mais diretamente reflete o domínio da competência central: transformar superfícies 3D em materiais críveis e com narrativa visual.

**C2 — Direção Artística, C4 — Materiais PBR e C8 — Integração na Unity (12% cada)** compartilham peso elevado porque representam os três pilares do resultado: a proposta visual, a qualidade técnica dos materiais e a entrega funcional no motor.

**C1 — Processo de Projeto (10%)** mantém peso relevante mesmo na avaliação final porque a metodologia SBL valoriza o processo como aprendizagem, não apenas o produto.

**C10 — Participação nas Critiques (8%)** é incluído na nota final para institucionalizar a cultura de critique como prática profissional. Artistas de jogos trabalham em equipe e a capacidade de dar e receber feedback é competência técnica, não comportamental.

**C3 — UV Mapping, C6 — Bake e C7 — Otimização (8% cada)** são competências técnicas fundamentais avaliadas principalmente nas fases intermediárias. Na avaliação final, elas são verificadas como requisito de qualidade, não como foco principal.

---

## Instrumentos Derivados

---

### Instrumento 1 — Ficha de Crítica Formal

> Para uso nas 6 críticas formais (CF1–CF6). Antes de preencher, consulte a tabela **Critérios Ativos por Crítica Formal** e deixe em branco os critérios marcados como "—" para a CF atual. Critérios marcados como "obs." recebem anotação mas não nota.

**Estudante:** _____________________________ **CF:** _______ **Semana:** _______ **Data:** _______

| Critério | Status nesta CF | 1 | 2 | 3 | 4 | 5 | Observação |
|---|---|---|---|---|---|---|---|
| C1 — Processo | ✓ em todas | ○ | ○ | ○ | ○ | ○ | |
| C2 — Dir. Artística | ✓ em todas | ○ | ○ | ○ | ○ | ○ | |
| C3 — UV Mapping | ✓ CF1–CF2 / obs. CF3 | ○ | ○ | ○ | ○ | ○ | |
| C4 — Materiais PBR | ✓ CF2–CF4 / obs. CF5 | ○ | ○ | ○ | ○ | ○ | |
| C5 — Texturização | ✓ CF3–CF6 | ○ | ○ | ○ | ○ | ○ | |
| C6 — Bake | ✓ CF4–CF6 | ○ | ○ | ○ | ○ | ○ | |
| C7 — Otimização | ✓ CF5–CF6 | ○ | ○ | ○ | ○ | ○ | |
| C8 — Unity | ✓ CF6 apenas | ○ | ○ | ○ | ○ | ○ | |
| C9 — Apresentação | ✓ CF5–CF6 | ○ | ○ | ○ | ○ | ○ | |
| C10 — Critiques (CC) | obs. CF1–CF5 / ✓ CF6 | ○ | ○ | ○ | ○ | ○ | |

**Ponto mais forte desta crítica:**  
_____________________________________________________________

**Prioridade de melhoria para a próxima entrega:**  
_____________________________________________________________

---

### Instrumento 2 — Autoavaliação do Estudante

> Para ser preenchida pelo estudante **antes** de cada crítica formal. O professor compara com sua própria avaliação durante a critique.

**Nome:** _____________________________ **CF:** _______ **Semana:** _______ **Data:** _______

Para cada critério aplicável nesta CF, responda:

1. Em qual nível você acredita que está? (1 a 5)
2. Qual evidência no seu trabalho justifica esse nível?
3. O que você faria diferente se tivesse mais uma semana?

---

**C1 — Processo de Projeto**  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C2 — Direção Artística**  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C3 — UV Mapping** *(CF1, CF2 e CF6)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C4 — Materiais PBR** *(CF2, CF3, CF4 e CF6)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C5 — Texturização** *(CF3 em diante)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C6 — Bake** *(CF4 em diante)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C7 — Otimização** *(CF5 e CF6)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C8 — Integração na Unity** *(CF6 apenas)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C9 — Apresentação** *(CF5 e CF6)*  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

**C10 — Participação nas Critiques**  
Nível: _____ | Evidência: ____________________________________________  
O que mudaria: _________________________________________________

---

**Pergunta de reflexão:**  
*Qual foi a decisão técnica ou artística mais difícil que você tomou esta semana? O que te fez decidir dessa forma?*

_______________________________________________________________
_______________________________________________________________
_______________________________________________________________

---

### Instrumento 3 — Avaliação por Pares

> Para uso nas críticas coletivas. O estudante avalia o trabalho de um colega.

**Avaliador:** _____________________________ **Avaliado:** _____________________________ **Data:** _______

**Instruções:** Avalie o trabalho do seu colega com honestidade e respeito. O objetivo não é julgar, mas ajudar. Para cada critério, indique o nível que você observa e escreva uma observação específica e construtiva. Evite comentários vagos como "ficou bom" ou "precisa melhorar".

| Critério | Nível (1–5) | Observação específica |
|---|---|---|
| C1 — Processo de Projeto | | *Ex: "Vi que você incorporou o feedback de curvatura da semana passada — o desgaste ficou mais crível."* |
| C2 — Direção Artística | | *Ex: "A paleta do kit é coerente, mas o barril destoa dos outros assets em saturação."* |
| C3 — UV Mapping | | *Ex: "As UVs do tronco da coluna têm estiramento visível no checker. As demais estão bem."* |
| C4 — Materiais PBR | | *Ex: "O roughness da pedra está muito uniforme. Pedra real tem variação de polimento nas arestas."* |
| C5 — Texturização | | *Ex: "O desgaste está só nas arestas. Faltou sujeira acumulada nos cantos e partes baixas."* |
| C6 — Bake | | *Ex: "O normal map do arco tem um seam visível na parte de cima. O restante está limpo."* |
| C7 — Otimização | | *Ex: "Não consegui identificar uso de trim sheet. Há assets que poderiam compartilhar textura."* |
| C8 — Integração na Unity | | *Ex: "O asset ficou bem na Unity, mas o normal map parece fraco comparado ao 3D Coat."* |
| C9 — Apresentação | | *Ex: "Os renders de apresentação estão bem iluminados. Sentiu falta de um wireframe."* |
| C10 — Critiques | | *Ex: "Você deu um feedback muito específico para a Maria sobre o roughness. Foi útil."* |

**O ponto mais forte do projeto do seu colega:**  
_______________________________________________________________

**A única coisa que você priorizaria melhorar se fosse você:**  
_______________________________________________________________

---

### Instrumento 4 — Checklist Semanal de Acompanhamento

> Para uso pelo estudante ao final de cada sessão de estúdio. Permite acompanhar o progresso incremental.

**Nome:** _____________________________ **Semana:** _______ **Data:** _______

Marque o que foi concluído nesta semana:

#### Processo
- [ ] Atualizei minha pasta de referências com novas imagens relevantes
- [ ] Salvei versão numerada do arquivo de trabalho desta sessão
- [ ] Anotei as decisões que tomei e por quê
- [ ] Registrei o feedback recebido na última crítica
- [ ] Incorporei pelo menos um ponto de feedback nas iterações desta semana

#### Direção Artística
- [ ] Todos os assets desta semana seguem a paleta definida no moodboard
- [ ] O nível de detalhe está consistente com os outros assets do kit

#### UV Mapping (quando aplicável)
- [ ] Apliquei checker map para verificar distorção
- [ ] Verifiquei texel density entre os assets
- [ ] Posicionei seams em locais não visíveis
- [ ] Ocupação do espaço UV acima de 70%

#### Materiais PBR (quando aplicável)
- [ ] Albedo sem iluminação "baked"
- [ ] Roughness com variação (não uniforme)
- [ ] Metallic dentro dos valores corretos (0 ou 1, com transições apenas para materiais mistos)
- [ ] Normal map aplicado e intensidade calibrada

#### Texturização (quando aplicável)
- [ ] Há pelo menos 3 camadas de detalhe (base, variação, desgaste)
- [ ] Desgaste em arestas com lógica de uso
- [ ] Sujeira acumulada em áreas protegidas e inferiores
- [ ] Testei a leitura à distância de uso (não apenas em close-up)

#### Bake (quando aplicável)
- [ ] Bake realizado sem artefatos visíveis
- [ ] Normal map testado no viewport
- [ ] AO sem bleeding entre ilhas
- [ ] Seams invisíveis à distância de uso

#### Otimização (quando aplicável)
- [ ] Resoluções de textura definidas e justificadas
- [ ] Verificado se o asset pode compartilhar textura com outro do kit
- [ ] Trim sheet aplicado onde cabível

#### Unity (quando aplicável)
- [ ] Asset importado e na escala correta
- [ ] Materiais configurados com texturas nos slots corretos
- [ ] Normal map com flag "Normal Map" ativada
- [ ] Asset testado sob diferentes condições de iluminação

---

**Reflexão rápida (2 minutos):**

O que eu **finalizei** esta semana: ________________________________

O que ficou **pendente** para a próxima: ____________________________

O que eu **aprendi** que não estava no plano: ________________________

---

*Rubrica Mestre — Texturização — Jogos Digitais | Versão 2.0 | 2026*
