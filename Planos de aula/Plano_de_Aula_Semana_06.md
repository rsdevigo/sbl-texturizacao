# Plano de Aula — Semana 6
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** II — Materiais PBR e Workflow  
**Tema:** Criação de texturas seamless e tileable  
**Apostila:** Parte IV, Cap. 12 — Texturas Seamless e Tileables (fontes de texturas e técnicas de criação)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔵 Informal — Crítica circulante em estúdio e comentário coletivo ao final do segundo encontro

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 com UV otimizado + material PBR aplicado (Principled BSDF com valores planos de Albedo, Metallic e Roughness) — Semana 5
- Asset 02 com UV aberto — Semana 4
- 4 materiais PBR temáticos calibrados (v2 pós-crítica formal) — Semana 5
- Compreensão consolidada de: Albedo, Metallic, Roughness, plausibilidade física, Principled BSDF

> **Transição pedagógica desta semana:** nas Semanas anteriores, os estudantes definiram *o que o material é* usando valores planos (cor sólida, Metallic 0 ou 1, Roughness fixo). A Semana 6 é o primeiro momento em que uma **imagem real** entra no pipeline — o Albedo deixa de ser uma cor e passa a ser uma textura com variação, micro-detalhe e identidade visual do tema. O conceito central a introduzir é que uma textura de jogo precisa ser **seamless** (sem costura visível quando repetida) para funcionar em superfícies maiores do que um único UV tile.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é uma textura seamless e por que ela é necessária em jogos com superfícies amplas.
2. Diferenciar uma textura seamless criada por offset+patch de uma simples repetição direta de foto.
3. Criar ou adaptar uma textura seamless a partir de uma fotografia usando o Krita (ou editor equivalente), aplicando o método de offset e patch de bordas.
4. Importar a textura seamless no Blender e conectá-la ao canal Albedo do Principled BSDF do Asset 01.
5. Localizar e baixar texturas PBR de fontes livres (Poly Haven, AmbientCG) e identificar os mapas disponíveis em cada pacote.

---

## Critérios observados nesta semana

> ⚠️ **Semana sem crítica formal — nenhuma nota é atribuída.** O professor observa e registra evidências nos critérios abaixo para calibrar a avaliação da próxima CF. O estudante não recebe nota, mas recebe feedback oral durante o estúdio.

| Critério | O que observar |
|---|---|
| C1 — Processo de Projeto | Nomenclatura e organização dos arquivos de textura; registro visual da textura antes e depois do patch |
| C2 — Direção Artística | Coerência entre a textura escolhida/criada e o universo visual do kit; paleta respeitada |
| C4 — Materiais PBR | Integração correta da textura ao canal Albedo; manutenção dos valores de Metallic e Roughness já calibrados |
| C10 — Participação (CC) | Qualidade das observações na crítica circulante; capacidade de identificar costuras visíveis no trabalho dos colegas |

> **Progressão do PA — entre CF2 e CF3:** Esta semana fica entre a CF2 (sem 5) e a CF3 (sem 8). C4 (Materiais PBR) continua em desenvolvimento — aqui passa de valores planos para textura real. C5 (Texturização) começa a ser observado pelo professor, mas só será formalmente avaliado a partir da CF3. O professor registra observações de C4 e C5 no campo de anotações da Ficha de Crítica Formal da semana seguinte.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x) e Krita instalado
- Asset 01 de cada estudante (arquivo `.blend` da Semana 5 com UV + material PBR)
- Arquivo de demonstração do professor: fotografia de pedra ou tijolos (resolução mínima 1024×1024, iluminação difusa e neutra — sem sombras duras)
- Krita aberto e configurado para uso (confirmar instalação no laboratório com antecedência)
- Acesso à internet para acessar Poly Haven (polyhaven.com) e AmbientCG (ambientcg.com)
- Projetor para a demonstração
- Apostila — Parte IV, Cap. 12 — disponibilizada antes da aula
- Checkerboard texture para verificação de UV (já presente nos arquivos dos estudantes da Semana 2)
- Add-on UVPackmaster (versão gratuita), se disponível no laboratório, para a recapitulação de empacotamento avançado de UV no início da mini-aula (retomando a Semana 4). Não é essencial — se indisponível, mencionar apenas verbalmente

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Recapitulação rápida (5 min): empacotamento avançado de UV**

Antes de começar o conteúdo novo, retomar em 5 minutos o que ficou pendente da Semana 4: o add-on UVPackmaster (quando disponível no laboratório) permite empacotamento de UV islands com rotação livre e aproveitamento de formas irregulares — um resultado mais eficiente que o Pack Islands nativo do Blender, especialmente para islands orgânicas. Mostrar rapidamente (ou, se o add-on não estiver instalado, descrever com uma imagem) a diferença de aproveitamento de espaço entre um Pack Islands nativo e um empacotamento via UVPackmaster no mesmo asset. Fechar com a pergunta: *"Vale a pena reabrir o Pack Islands do Asset 01 ou do Asset 02 com essa ferramenta antes de aplicar a textura de hoje? Se sim, façam isso nos primeiros minutos do estúdio."*

**Texturas seamless: por que repetição sem costuras é uma exigência de produção**

Objetivo (15 min restantes): mostrar que o problema da costura não é estético — é funcional. Uma textura não-seamless aplicada em uma parede de jogo cria linhas visíveis que quebram a ilusão de realidade independentemente da qualidade artística do resto do material.

**Desenvolvimento:**

Abrir com uma demonstração visual rápida (sem abrir nenhum software ainda — usar imagens estáticas no projetor):

Mostrar dois exemplos lado a lado:
1. Uma parede de pedra com uma textura de 512×512 repetida sem tratamento seamless — as linhas de corte são visíveis.
2. A mesma parede com a textura tornada seamless — a repetição não é perceptível.

Perguntar: *"O que está diferente entre essas duas imagens? Onde está o problema na primeira?"* — aguardar 2–3 respostas. O objetivo é que os estudantes identifiquem a **costura** antes de nomear o conceito.

---

**Conteúdo a cobrir:**

**1. O que é uma textura seamless**

Uma textura seamless (ou tileable) é uma imagem cujas bordas esquerda/direita e superior/inferior são matematicamente contínuas: quando repetida lado a lado, o olho não detecta a transição entre os tiles.

Em jogos, superfícies como paredes, pisos, tetos e terrenos são frequentemente maiores do que uma única tile de textura. A solução mais eficiente em termos de memória é usar uma textura pequena repetida muitas vezes — mas ela só funciona se for seamless.

A alternativa (textura única cobrindo toda a superfície) existe e tem usos específicos, mas exige resoluções altíssimas e não é escalável para um kit modular.

**2. Por que fotos brutas não são seamless**

Uma fotografia comum captura variações de iluminação, sombras e perspectiva que tornam as bordas diferentes entre si. Mesmo se o conteúdo visual fosse idêntico nos quatro lados, a iluminação ambiente cria gradientes que vazam pelas bordas.

O método clássico para corrigir isso é o **offset**:
- Deslocar a imagem em 50% nos dois eixos (horizontal e vertical).
- As bordas originais — que eram invisíveis por estarem no centro — agora ficam explícitas no centro da imagem.
- O artista pinta sobre essas costuras usando ferramentas de clone stamp, healing brush ou pintura direta.
- Resultado: bordas seamless, centro com conteúdo variado.

**3. Krita como ferramenta de criação de texturas seamless**

O Krita possui o filtro **Wrap Around** (atalho: `W` no canvas) que ativa uma pré-visualização de repetição em tempo real — o artista vê como a textura ficará quando tileada *enquanto pinta*. Isso elimina a necessidade de exportar e testar a cada ajuste.

Ferramentas do Krita úteis para este fluxo:
- **Clone Stamp** (S): copia pixels de outra região para cobrir as costuras.
- **Healing Brush** (não presente no Krita nativo): usar o Clone Stamp com blending mode Normal é equivalente para patches de textura.
- **Smudge Tool**: suavizar transições entre áreas patcheadas e o entorno.
- **Wrap Around** (W): visualizar a repetição a qualquer momento.

**4. Fontes de texturas PBR gratuitas**

Quando criar uma textura do zero não for necessário ou viável, existem fontes de alta qualidade com licença livre:

- **Poly Haven** (polyhaven.com): texturas fotografadas em condições controladas, disponíveis com todos os mapas PBR (Albedo, Normal, Roughness, AO, Displacement). Licença CC0.
- **AmbientCG** (ambientcg.com): grande variedade de materiais, organização por categoria, mapas PBR completos. Licença CC0.

Para esta semana, os estudantes podem *criar* uma textura a partir de uma foto (processo de aprendizagem mais rico) ou *baixar* uma de uma das fontes acima e adaptar ao tema do kit se necessário. O professor deve deixar claro que baixar uma textura pronta **não isenta o estudante de entender o processo de seamless** — a entrega inclui evidência do processo, não apenas o arquivo final.

> **Nota do professor:** Manter as imagens de exemplo abertas no projetor durante o estúdio para referência. Se o laboratório tiver conexão instável, preparar com antecedência um pacote de 5–6 texturas do Poly Haven e AmbientCG em pen drive (temas cobertos: pedra, madeira, metal, concreto, tijolos).

---

### Demonstração — 20 minutos

**Criação de uma textura seamless de pedra a partir de uma fotografia no Krita**

**Setup (2 min):**  
Abrir o Krita com a fotografia de pedra preparada (resolução 1024×1024 ou superior, iluminação difusa). Ter o Blender aberto minimizado com o Asset 01 de demonstração já carregado para uso na segunda parte.

**Percurso da demonstração:**

**Passo 1 — Observar o problema (2 min):**
1. Importar a foto bruta no Krita.
2. Ativar o modo Wrap Around (`W`): mostrar ao vivo as costuras que aparecem na visualização de repetição.
3. Apontar as linhas: *"Essas costuras existem porque as bordas da foto têm valores de cor e textura diferentes entre si. O offset vai trazê-las para o centro onde podemos consertá-las."*

**Passo 2 — Aplicar o offset (3 min):**
1. Menu `Filter → Transform → Offset...`
2. Definir offset de 50% em X e 50% em Y (equivalente a metade da largura e altura da imagem).
3. Confirmar. As costuras agora aparecem como linhas cruzadas no centro da imagem.
4. Mostrar no Wrap Around: as bordas agora são contínuas — o problema se moveu para o centro.

**Passo 3 — Patch das costuras (8 min):**
1. Selecionar o Clone Stamp (`S`). Ajustar tamanho e dureza (hardness ~60–70%).
2. Amostrar (`Ctrl+clique`) uma região de pedra próxima à costura com textura similar.
3. Cobrir a linha de costura com clones de regiões adjacentes, trabalhando de forma irregular (não linear) para evitar padrões repetitivos.
4. Alternar entre Clone Stamp e Smudge para suavizar transições abruptas.
5. Verificar constantemente no Wrap Around se novas costuras estão sendo criadas.

**Passo 4 — Verificação final e exportação (3 min):**
1. Desativar o Wrap Around e verificar a textura plana — ela deve parecer uma pedra natural sem costuras óbvias.
2. Reativar o Wrap Around com zoom out para ver a repetição em grid — confirmar ausência de costuras.
3. Exportar: `File → Export As...` → formato PNG, 1024×1024, nome `pedra_seamless_demo.png`.

**Passo 5 — Importação no Blender (2 min):**
1. Abrir o Blender com o Asset 01 de demonstração.
2. No Shader Editor, adicionar um nó `Image Texture` (`Shift+A → Texture → Image Texture`).
3. Abrir a textura exportada no nó.
4. Conectar a saída `Color` do Image Texture à entrada `Base Color` do Principled BSDF.
5. No Viewport Rendered: mostrar a textura aplicada sobre o asset — comparar com o Albedo plano da semana anterior.

> **Nota do professor:** Não precisa ser perfeito — uma costura residual durante a demo é didaticamente valiosa. Mostrar: *"Tem ainda uma costura aqui. O que eu faria agora? Volto ao Krita, re-exporto e recarrego o nó. Esse ciclo Krita → Blender vai se repetir várias vezes durante o estúdio — é normal."*

---

### Produção em Estúdio — 50 minutos

**Criação da textura seamless temática e aplicação ao Asset 01**

**Consigna entregue verbalmente:**

> *"O objetivo deste estúdio é criar uma textura seamless que represente o material principal do Asset 01 do seu kit — a superfície que ele mais mostra. Se o Asset 01 é uma parede de pedra medieval, a textura é pedra. Se é uma caixa de metal enferrujado Sci-Fi, a textura é metal com ferrugem. Vocês têm três caminhos: criar a partir de uma foto própria ou da internet, criar a partir de uma foto do Poly Haven ou AmbientCG (que já são quase seamless), ou baixar uma textura pronta dessas fontes se o tempo for curto. Qualquer caminho vale — o que importa é que ao final vocês tenham uma textura PNG seamless aplicada ao canal Albedo do Asset 01 no Blender."*

**Atividade estruturada:**

1. Abrir o Krita e preparar a imagem de origem (foto ou download).
2. Aplicar o processo de offset + patch conforme demonstração.
3. Verificar continuidade no Wrap Around (`W`).
4. Exportar a textura: `[Nome]_[material]_seamless_S06.png` (ex: `joao_pedra_seamless_S06.png`).
5. No Blender, abrir o arquivo do Asset 01 da Semana 5.
6. No Shader Editor, adicionar o nó `Image Texture`, carregar a textura exportada e conectar ao `Base Color` do Principled BSDF.
7. Verificar no Viewport Rendered com HDRI: a textura tile sem costuras visíveis? O Albedo anterior (cor plana) foi substituído pela textura, mas Metallic e Roughness devem permanecer com os valores calibrados na Semana 5.
8. Salvar: `[Nome]_Asset01_Textura_S06.blend`.

**Papel do professor:**

Circular e verificar três pontos em cada estação:

- **A textura está seamless?** Pedir para o estudante ampliar a visualização em Wrap Around — costuras visíveis indicam patch incompleto.
- **Os valores de Metallic e Roughness foram preservados?** Erro comum: ao adicionar o nó Image Texture, o estudante desconecta por acidente outros inputs. Verificar que o Metallic e Roughness ainda estão configurados.
- **A escala da textura está coerente com o asset?** Uma textura de pedra com tiles muito grandes (pedras enormes em relação ao objeto) ou muito pequenos (pedras minúsculas) quebra a crença. Orientar o ajuste pelo nó `Mapping` + `Texture Coordinate`.

Perguntas de mediação circulante:

- *"Essa costura está aparecendo porque o patch aqui foi linear — você pintou em linha reta. Tenta trabalhar de forma mais irregular, seguindo as formas naturais da pedra."*
- *"A textura está muito grande em relação ao asset. Adiciona um nó Mapping entre o Texture Coordinate e o Image Texture e aumenta o Scale."*
- *"Esse Roughness de 0.85 que você calibrou na Semana 5 — ele ainda está lá? Confere no Principled BSDF."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: crítica circulante com ênfase em leitura de costura e coerência temática**

Esta é uma crítica informal. Não há apresentação individual obrigatória — o professor conduz uma rodada circulante pelos monitores da turma, parando em 4–5 trabalhos para comentário coletivo.

**Protocolo:**

**Abertura (2 min):**  
Professor define o foco da crítica: *"Hoje vamos olhar para duas coisas: (1) a textura está seamless? — olho de 2 metros de distância do monitor, textura no Asset em Viewport Rendered; (2) essa textura poderia existir no universo do kit? — o material, a cor, o nível de detalhe combinam com o moodboard?"*

**Rodada circulante (15 min — 4–5 estações):**

Para cada trabalho observado, o professor faz a turma se posicionar diante do monitor e conduz com perguntas:

- *"Alguém consegue ver onde começa um tile e termina outro nessa parede? Apontem se virem."* — Se a costura for invisível: reforçar positivamente o processo. Se for visível: identificar coletivamente onde está e por que ocorreu (patch insuficiente, offset incorreto, região muito regular).
- *"Essa textura de [material] combina com o universo [tema do kit]? Parece medieval suficiente? Sci-Fi o bastante? O que está certo e o que destoa?"*
- *"O material está preservado — Roughness e Metallic configurados corretamente? Ou só o Albedo foi conectado?"*

**Fechamento da crítica (3 min):**  
Professor sintetiza os padrões observados na turma:
- Qual o erro de seamless mais comum (tipicamente: patch em linha reta criando novo padrão repetitivo, ou patch insuficiente nas extremidades).
- Qual é o estado geral de coerência temática — os kits estão ganhando identidade visual?
- Orientação para o estúdio: *"Quem ainda tem costura visível: foco em voltar ao Krita e refinar o patch. Quem já está satisfeito com a textura: começa a criar a textura seamless para o Asset 02."*

---

### Produção em Estúdio — 60 minutos

**Refinamento da textura do Asset 01 + início da textura do Asset 02**

**Consigna:**

> *"Sessenta minutos, duas prioridades em ordem. Primeiro: se a crítica apontou costura ou incoerência temática no Asset 01, corrija agora — volte ao Krita, refine o patch, re-exporte e recarregue no Blender. Segundo, para quem estiver satisfeito com o Asset 01: repita o processo para o Asset 02. Não precisa terminar — o objetivo é ter o fluxo completo (Krita → export PNG → Blender → conectar ao Albedo) rodando de forma autônoma para ambos os assets."*

**Atividade:**

**Parte 1 — Refinamento do Asset 01 (≈20 min para quem precisar, pular para Parte 2 se já resolvido):**
1. Reabrir a textura no Krita.
2. Ativar Wrap Around, identificar costuras residuais e refinar o patch com Clone Stamp.
3. Re-exportar com o mesmo nome (sobrescrever) ou com sufixo `_v2`.
4. No Blender: no nó Image Texture do Asset 01, clicar em `Reload` para atualizar a textura sem precisar reimportar.
5. Verificar no Viewport Rendered.
6. Salvar: `[Nome]_Asset01_Textura_S06_v2.blend`.

**Parte 2 — Textura seamless para o Asset 02 (≈40 min):**
1. Identificar o material principal do Asset 02 no kit.
2. Buscar ou capturar imagem de origem coerente com o tema.
3. Aplicar o processo de offset + patch no Krita.
4. Verificar no Wrap Around.
5. Exportar: `[Nome]_[material]_seamless_Asset02_S06.png`.
6. Abrir o arquivo do Asset 02 no Blender (Semana 4 — UV aberto, sem material ainda).
7. Criar material no Principled BSDF com os valores de Metallic e Roughness coerentes com o material do Asset 02 (referenciar os 4 materiais de teste da Semana 5).
8. Conectar a textura seamless ao `Base Color`.
9. Salvar: `[Nome]_Asset02_Textura_S06.blend`.

**Papel do professor:**

- Para estudantes refinando o Asset 01: *"O que mudou com o patch que você fez? Consegue mostrar no Wrap Around antes e depois?"* — estimular a verbalização do processo para C1.
- Para estudantes avançando para o Asset 02: *"O Roughness do Asset 02 é o mesmo do Asset 01? Os dois objetos no seu kit têm a mesma superfície? Se não, os valores têm que ser diferentes."*
- Para estudantes rápidos que terminam os dois assets: *"Você tem um terceiro asset em mente para o kit? Se tiver, começa o UV dele — semana que vem você vai precisar."* Ou: *"Experimenta ajustar o Scale da textura do Asset 01 para ver o impacto na leitura visual do objeto."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese técnica)**  
*"Hoje vocês fizeram a primeira conexão entre uma imagem real e o pipeline de texturização. O Albedo do Asset 01 não é mais uma cor — é uma superfície com história. Isso parece simples, mas é a base de tudo que vem na Semana 7 em diante: Normal Map, Roughness mapeado, desgaste pintado. Tudo começa aqui."*

2. **(3 min — Reflexão de processo)**  
Pergunta para 2–3 voluntários: *"Qual foi a parte mais difícil do processo de seamless? O patch em si, ou saber quando a costura estava boa o suficiente? Como você decidiu parar?"* O objetivo é problematizar o critério de "bom o suficiente" — que é uma decisão artística, não técnica.

3. **(3 min — Antecipação da Semana 7)**  
*"Na semana que vem, vocês vão adicionar profundidade a esses materiais com o Normal Map — que simula relevos e detalhes 3D sem adicionar geometria. Vamos também criar o Roughness Map, que faz partes do mesmo material terem brilho diferente. Para isso, vocês vão precisar das texturas seamless que criaram hoje — mantenham os arquivos de origem do Krita (não só o PNG exportado). O arquivo `.kra` nativo do Krita com as camadas preservadas vai poupar trabalho."*

4. **(2 min — Confirmação das entregas)**  
Recapitular as entregas da semana com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Patch em linha reta cria um novo padrão repetitivo**  
O erro mais comum ao usar o Clone Stamp é cobrir a costura com pinceladas horizontais ou verticais regulares. O resultado substitui uma costura reta por um padrão de linhas paralelas igualmente visível. Estratégia: orientar pinceladas *diagonais e irregulares*, seguindo as formas naturais do material (veios da madeira, juntas da pedra). Mostrar ao vivo no Krita com o Wrap Around ativo.

**2. Costura visível apenas em repetição, invisível no arquivo isolado**  
O estudante olha para o PNG exportado e não vê costura — só percebe o problema depois de aplicar no Blender, quando a textura tilea. Estratégia: insistir no uso do Wrap Around (`W`) no Krita *durante* o processo. Ele é o único feedback em tempo real confiável. Se o estudante chegou ao Blender e viu costura: *"Volte ao Krita, abra o arquivo .kra (não o PNG), ative o Wrap Around e corrija lá — re-exporte e dê Reload no nó do Blender."*

**3. Imagem de origem com iluminação direcional forte (sombras duras)**  
Fotos com sombras duras criam gradientes que não podem ser corrigidos com offset+patch simples — as sombras seguem a direção da luz e criam costuras que "giram" conforme o tile. Estratégia: orientar os estudantes a usar imagens capturadas em dia nublado ou iluminação difusa. Se a foto tiver sombras leves, o Krita permite suavizá-las com Dodge/Burn ou ajuste de níveis por camada antes do offset.

**4. Krita não instalado ou com problemas no laboratório**  
O Krita é um software gratuito mas precisa estar instalado com antecedência. Estratégia: confirmar a instalação antes da aula. Como alternativa imediata, o próprio Blender possui um Image Editor integrado com ferramentas básicas de pintura (`Texture Paint` workspace) que permite fazer um patch rudimentar. Para esta semana, essa alternativa é funcional embora menos confortável.

**5. Escala da textura incorreta após aplicação no Blender**  
A textura aparece muito grande (poucos tiles visíveis) ou muito pequena (tiles microscópicos) em relação ao objeto. Isso não é problema do seamless — é de escala de mapeamento. Estratégia: adicionar um nó `Mapping` (Shift+A → Vector → Mapping) entre o `Texture Coordinate` e o `Image Texture`. Ajustar os valores de `Scale` em X e Y até a proporção parecer fisicamente coerente. Referenciar: uma pedra de parede medieval típica tem entre 20–40 cm — quanto isso representa em relação ao Asset 01?

**6. Estudante baixa textura do Poly Haven/AmbientCG e não entende o processo**  
Texturas do Poly Haven já são seamless, então o estudante que as baixa pula todo o aprendizado prático da semana. Estratégia: não proibir o uso das fontes — elas são parte do fluxo profissional. Mas exigir que o estudante **documente** por que a textura é seamless (identificar o Wrap Around, apontar a continuidade de bordas) e que adapte a cor ou o detalhe ao tema do kit se necessário. *"Baixar é válido. Entregar sem entender não é."*

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não consegue eliminar a costura após múltiplos patches | *"Para um pouco. Ativa o Wrap Around, faz zoom out e me mostra a costura mais importante — aquela que vai ser mais visível na parede final. Trabalha só nela por 5 minutos. As menores a gente resolve depois."* Priorizar o problema mais impactante, não tentar corrigir tudo de uma vez. |
| Estudante inseguro sobre se a textura está "boa o suficiente" | *"Recua 2 passos do monitor e olha para a parede tileada. Se você precisar se concentrar para achar a costura, ela já não vai incomodar o jogador. Essa é a régua."* |
| Textura coerente tecnicamente mas desconectada do tema | Abrir o moodboard ao lado do Blender. *"Olha para essas referências. Essa pedra que você usou — ela existe nesse universo? A cor está certa? O nível de desgaste está certo?"* Redirecionar para busca de nova referência se necessário. |
| Metallic ou Roughness perdidos ao adicionar o nó Image Texture | *"Esses inputs no Principled BSDF — o que está conectado agora? Metallic e Roughness ainda têm valor? Se o campo está branco e sem nó, o valor voltou para o padrão. Recoloca os valores que você tinha na Semana 5."* |
| Estudante avançado que termina cedo os dois assets | Propor desafio de variação: *"Cria uma segunda versão da mesma textura com cor ligeiramente diferente — como se fosse o mesmo material em partes mais novas e partes mais antigas. Dois arquivos PNG do mesmo material com variação de temperatura de cor. Isso vai ser útil para dar vida ao kit mais pra frente."* |
| Turma com dificuldade geral no Krita (interface desconhecida) | Fazer uma pausa de 5 minutos para um micro-tour: mostrar Clone Stamp (`S`), Smudge, Wrap Around (`W`) e Export. Não mais do que isso — o Krita é suficientemente intuitivo para o nível necessário esta semana. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| PNG da textura seamless com ausência de costura visível a zoom normal | C4 — Materiais PBR | Ativar Wrap Around no Krita ou observar a repetição no Viewport do Blender com escala real — costura não deve ser identificável sem esforço |
| Arquivo `.kra` do Krita com camadas preservadas (ou registro do processo de offset+patch) | C1 — Processo de Projeto | Presença do arquivo de origem nomeado corretamente; camadas distinguindo a foto original do trabalho de patch |
| Asset 01 com textura seamless conectada ao Albedo e Metallic/Roughness preservados da Semana 5 | C4 — Materiais PBR | Verificar no Principled BSDF: Base Color conectado ao Image Texture, Metallic e Roughness com valores não-padrão coerentes com o material |
| Coerência temática da textura com o universo do kit (cor, desgaste, escala) | C2 — Direção Artística | Comparação direta com o moodboard: a textura poderia existir naquele universo visual? |
| Participação na crítica circulante: identificar costura ou incoerência temática no trabalho de outro estudante | C10 — Participação | Qualidade e especificidade da observação — não apenas "está bom" ou "está ruim", mas apontamento técnico ou artístico fundamentado |
| Arquivo nomeado e versionado corretamente (PNG + .blend + .kra) | C1 — Processo de Projeto | Existência dos três tipos de arquivo com sufixo `_S06` e distinção de versões onde aplicável |

---

## Entrega da Semana 6

| Entrega | Formato | Prazo |
|---|---|---|
| Textura seamless do Asset 01 (material principal do kit) | PNG 1024×1024 ou superior, com sufixo `_seamless_S06` | Até o fim do segundo encontro |
| Arquivo de origem do Krita (processo de patch preservado) | `.kra` nativo do Krita | Até o fim do segundo encontro |
| Asset 01 com textura seamless aplicada no Albedo | `.blend` com sufixo `_Asset01_Textura_S06` | Até o fim do segundo encontro |
| Asset 02 com textura seamless aplicada (se concluído) | PNG + `.blend` com sufixo `_Asset02_Textura_S06` | Até o fim do segundo encontro (entrega parcial aceita) |

> **Nota:** A entrega do Asset 02 com textura é progressiva — o objetivo é que todos completem o Asset 01. O Asset 02 será concluído no início da Semana 7 se necessário, antes da introdução do Normal Map.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 6 | 2026*
