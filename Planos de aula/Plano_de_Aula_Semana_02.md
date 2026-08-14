# Plano de Aula — Semana 2
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** I — Fundamentos, Mapeamento UV e Definição do Hero Asset (Semanas 1–5)
**Tema da semana:** Fundamentos de mapeamento UV: conceitos e projeção de textura
**Apostila:** Parte II, Cap. 4 — Coordenadas UV e Projeções de Textura
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — Diagnóstico visual compartilhado, circulante em estúdio e ao final do segundo encontro

---

## O que já foi ministrado (Semana 1 — não repetir)

Na Semana 1 os estudantes já foram apresentados a: textura vs. material, raster vs. procedural, o pipeline da disciplina (Blender → 3D Coat → Unity), o trabalho interdisciplinar do semestre (Pintura Digital e Arte Conceitual, Texturização, Modelagem 3D e Level Design; entregável final = fase caminhável na Unity; tema = mundo fantástico a partir de elementos regionais de MS ou do estado de origem) e um tour de orientação espacial pelo Blender (Shading Workspace, UV Editor, Viewport Shading — sem operar). Também já realizaram, em grupo, a dinâmica de ideação cultural (props de MS → jigsaw → matriz morfológica/SCAMPER/conexões forçadas) e cada estudante saiu com 1–2 ideias individuais de recorte temático, ainda não fechadas.

**Importante:** o recorte temático e o Hero Asset Referência só são definidos formalmente na Semana 3. Nesta semana, portanto, os estudantes **ainda não têm** um Kit Modular, tema ou Hero Asset oficiais — apenas as ideias em amadurecimento da Semana 1. Esta semana é a primeira operação técnica real no Blender: ninguém abriu o UV Editor com intenção de trabalho ainda.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é um mapa UV e por que ele é necessário para aplicar texturas em um objeto 3D.
2. Descrever o espaço UV (coordenadas 0–1) e identificar distorção e sobreposição em um layout, usando a textura de checkerboard como ferramenta de diagnóstico.
3. Aplicar os quatro tipos de projeção UV (planar, cilíndrica, esférica, cúbica) em objetos geométricos simples e justificar qual é mais adequada a cada forma.
4. Reconhecer, de forma intuitiva (sem cálculo numérico), que islands maiores no espaço UV correspondem a mais nitidez de textura — antecipando o conceito de texel density, que será formalizado na Semana 5.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Organização dos arquivos de prática (.blend), nomenclatura e registro da justificativa de escolha de projeção |
| C3 — UV Mapping | Foco principal: distorção aceitável, ausência de sobreposição — correspondente ao Nível 2–3 da rubrica (ver Rubrica Mestre) |
| C10 — Participação nas Critiques | Engajamento na crítica diagnóstica e qualidade das observações sobre o próprio trabalho e o dos colegas |

> C2 (Direção Artística) e C4–C9 ainda não são exigidos — não há tema nem Hero Asset definidos. O único resultado técnico esperado é um UV funcional, sem sobreposição, com checkerboard aplicado. Esta semana não gera nota; serve de linha de base para a crítica formal da Semana 4 (C3).

---

## Recursos necessários

- Computadores com Blender instalado (versão 3.x ou 4.x)
- Arquivo de prática preparado pelo professor: cena `.blend` com cubo, cilindro, esfera e um prop simples neutro (ex.: barril, caixa ou pedra — genérico, sem amarração a nenhum tema específico, já que o recorte temático ainda não foi fechado) — distribuir antes do primeiro encontro ou no início da aula
- Textura de checkerboard (padrão do Blender ou PNG externo de 1024×1024 com grid de cores)
- Projetor para demonstração
- Apostila — Parte II, Cap. 4 (disponibilizada antes da aula)

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**O que é um mapa UV e por que ele existe?**

Objetivo: construir a intuição conceitual antes de qualquer operação técnica.

**Desenvolvimento:**

Abrir com uma pergunta concreta para a turma: *"Se você tem uma esfera 3D e quer pintar ela, como você diz ao computador onde cada pixel da textura vai parar?"*

Deixar 2–3 respostas antes de apresentar a analogia central:

> *"UV mapping é o processo de 'desdobrar' um objeto 3D como se fosse uma caixa de papelão. Você corta as dobras (seams) e abre tudo em um plano 2D. É nesse plano que a textura será pintada."*

**Conteúdo a cobrir:**

1. **O espaço UV (0–1).** O UV Editor representa um quadrado de 0 a 1 nos dois eixos. A textura ocupa exatamente esse quadrado. Cada vértice do objeto 3D tem uma coordenada UV que diz "esse ponto do objeto corresponde a esse ponto da textura". Mostrar com uma imagem simples: um cubo aberto em UVs ao lado da textura que o cobre.

2. **O problema da distorção.** Não é possível desdobrar uma esfera sem distorção — assim como não é possível desenhar um mapa-múndi perfeitamente plano sem deformar algo. O objetivo do UV mapping não é eliminar distorção, mas controlá-la: manter a distorção em locais onde ela não é perceptível.

3. **Tipos de projeção.**
   - **Planar:** projeta do mesmo ângulo que uma câmera. Funciona bem para superfícies planas. Distorce nas bordas laterais.
   - **Cilíndrica:** enrola a textura ao redor do objeto. Adequada para colunas, troncos, tubos.
   - **Esférica:** enrola em todas as direções. Adequada para esferas, mas distorce nos polos.
   - **Cúbica (Box):** aplica seis projeções planares nas faces de um cubo imaginário ao redor do objeto. Funciona bem para formas com faces reconhecíveis.

4. **Antecipação de texel density (intuição, sem fórmula).** Texel = pixel de textura. Se uma island ocupa mais espaço no quadrado UV, ela recebe mais texels e fica mais nítida; uma island pequena fica borrada. Basta a intuição "island maior = mais nítida" — o cálculo numérico e o nome formal "texel density" ficam para a Semana 5, quando a otimização de layout for o foco da aula.

> **Nota do professor:** não avance para seams manuais nem para cálculo de texel density agora. Se surgir a pergunta "como cortar para abrir melhor?", responda: *"Isso é a Semana 4, quando vocês abrirem o UV do Hero Asset Referência. Hoje é só entender o problema e testar as projeções automáticas."* Se perguntarem valores exatos de texel density, responda: *"Vamos medir isso na Semana 5 — por enquanto, use o olho e o checker."*

---

### Demonstração — 20 minutos

**Projeção UV no Blender: cubo e esfera com checkerboard**

**Setup inicial (2 min):** abrir o arquivo de prática com o cubo e a esfera já na cena. Configurar o layout de tela com o Viewport 3D à esquerda e o UV Editor à direita — esse será o layout de trabalho padrão da disciplina a partir de agora.

**Parte 1 — Cubo (8 min):**

1. Selecionar o cubo. Entrar em Edit Mode (`Tab`).
2. Selecionar todas as faces (`A`).
3. Abrir o menu UV (`U`) e mostrar as opções disponíveis.
4. Aplicar **Cube Projection** e observar o layout gerado no UV Editor.
5. Aplicar a textura de checkerboard via Material Preview (`Z` → Material Preview) e mostrar como o grid aparece no objeto.
6. Apontar o que está bom e o que está distorcido.

**Parte 2 — Esfera (8 min):**

1. Selecionar a esfera. Entrar em Edit Mode.
2. Testar **Sphere Projection** — mostrar a distorção nos polos.
3. Testar **Cylinder Projection** — mostrar o seam vertical e a distorção aceitável no corpo.
4. Testar **Smart UV Project** — mostrar o resultado automático, sem edição humana.
5. Comentar: *"Smart UV Project é rápido, mas não é inteligente. Ele não sabe o que é importante no objeto. A partir da Semana 4, quando vocês tiverem um asset real para trabalhar, vamos sempre revisar o resultado com seams manuais."*

**Fechamento da demo (2 min):** mostrar brevemente como verificar distorção com o Overlay UV Stretch no UV Editor. Indicar o que é vermelho (estiramento) e o que é azul (compressão).

> **Nota do professor:** não execute seams manuais nesta demonstração — isso é conteúdo da Semana 4 (abertura de UV do Hero Asset Referência). O objetivo aqui é reconhecimento do problema via projeções automáticas, não a solução completa.

---

### Produção em Estúdio — 50 minutos

**Praticar projeções UV em objetos geométricos simples**

**Consigna entregue verbalmente:**

> *"Vocês vão trabalhar nos três objetos do arquivo de prática — cubo, cilindro e esfera. Para cada um, testem pelo menos dois tipos de projeção, apliquem o checkerboard e identifiquem qual projeção gera menos distorção. Não tem resposta errada — tem observação certa ou errada. O que eu quero ver é vocês olhando para o checker e conseguindo descrever o que está acontecendo."*

**Atividade estruturada:**

1. Abrir o arquivo de prática (`.blend` com cubo, cilindro, esfera).
2. Para cada objeto:
   - Testar pelo menos 2 tipos de projeção UV (`U` no Edit Mode).
   - Aplicar textura de checkerboard e ativar Material Preview.
   - Fazer screenshot do resultado no UV Editor + Viewport com o checker.
   - Anotar (no próprio arquivo ou em um documento de texto): "qual projeção escolhi e por quê".
3. Quem terminar antes: explorar o prop neutro incluído no arquivo (barril, caixa ou pedra) e tentar aplicar Cube ou Smart UV Project nele — sem amarração temática ainda.

**Papel do professor:**

Circular pelo estúdio fazendo perguntas diagnósticas:
- *"O que esse vermelho no checker está dizendo?"*
- *"Se a textura fosse uma imagem de tijolo, que parte do objeto ficaria esticada?"*
- *"Por que você escolheu essa projeção para o cilindro?"*

Identificar quem avançou rápido (será desafiado a explorar o prop neutro) e quem está travado na navegação do Blender — essa lista alimenta o acompanhamento individual da Semana 3, quando o Moodboard e o Hero Asset Referência começam a exigir mais autonomia técnica.

> **Nota do professor:** não interrompa o estúdio para corrigir erros de forma. Deixe os estudantes experimentarem e errarem — os erros são o material da crítica do próximo encontro.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: Diagnóstico visual compartilhado**

Não é apresentação formal. Cada estudante mostra na tela o seu resultado mais interessante (ou mais problemático) dos três objetos.

**Roteiro:**

1. **(5 min)** Professor seleciona 3–4 trabalhos com problemas distintos e visíveis (sobreposição, estiramento forte, escolha de projeção inadequada). Projetar na tela — sempre pedindo autorização antes: *"Posso usar o seu para mostrar esse caso?"*
2. **(10 min)** Para cada trabalho projetado, a turma responde:
   - *"O que vocês veem de errado aqui?"*
   - *"Que tipo de projeção foi usada? Faz sentido para essa forma?"*
   - *"Se essa distorção aparecesse na textura final de um asset do kit de vocês, onde ela incomodaria mais?"*
3. **(5 min)** Professor sistematiza: reforça os dois diagnósticos mais comuns que apareceram (distorção, sobreposição) e antecipa como serão resolvidos com seams manuais na Semana 4.

> **Nota do professor:** escolha trabalhos que mostrem erros comuns e instrutivos, não os piores da turma. O objetivo é usar o erro como material didático, não expor o estudante.

**Conectar à rubrica:** ao final, mencionar explicitamente: *"Na crítica formal da Semana 4, vamos olhar para o C3 — UV Mapping, aplicado ao Hero Asset Referência de vocês. O que vimos hoje nos objetos simples é exatamente o tipo de problema que o Nível 2 da rubrica descreve. Deem uma olhada no Nível 3 e pensem no que falta para chegar lá com um asset real."*

---

### Produção em Estúdio — 60 minutos

**Consolidar a prática nos três objetos e explorar o prop neutro**

**Consigna:**

> *"Agora o objetivo é consolidar. Revisem os três objetos com base no que discutimos na crítica — corrijam sobreposições, testem a projeção que vocês não tinham experimentado ainda. Depois, quem quiser, explora o prop neutro do arquivo aplicando o que aprenderam. Esse arquivo é a entrega de hoje."*

**Atividade:**

1. Revisar os três objetos (cubo, cilindro, esfera) incorporando os diagnósticos da crítica: corrigir sobreposições, testar a(s) projeção(ões) ainda não exploradas no Encontro 1.
2. Verificar distorção com o checkerboard e o Overlay UV Stretch.
3. Organizar as islands no UV Editor evitando sobreposição.
4. Salvar o arquivo com nomenclatura `[Nome]_UV_Semana02.blend`.
5. Capturar screenshot do UV Editor e do Viewport com checker ativo, para cada objeto.
6. Quem terminar com tempo: aplicar projeção UV no prop neutro (barril, caixa ou pedra) usando o método que fizer mais sentido para a forma — sem se preocupar em amarrar ao tema pessoal ainda, isso só começa a valer a partir da Semana 3.

**Papel do professor:**

Priorizar atenção individual para:
- Estudantes que na crítica mostraram confusão conceitual entre distorção e sobreposição.
- Estudantes que não conseguiram concluir os três objetos no primeiro encontro.

Para quem avança rápido: *"Testem o prop neutro e me digam: qual dos quatro tipos de projeção vocês tentariam primeiro, e por quê, antes mesmo de testar?"* — essa previsão qualitativa é um bom indicador de compreensão conceitual.

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min)** Síntese rápida pelo professor: *"Hoje vocês aprenderam a linguagem básica do UV mapping: sabem o que é distorção, sabem o que o checker está dizendo, sabem que a projeção depende da forma do objeto. Essa consciência vai com vocês até o final do semestre — e vai ser posta à prova de verdade na Semana 4, com o Hero Asset Referência que vocês vão receber de Modelagem 3D e Level Design."*

2. **(3 min) Reflexão individual registrada** (post-it físico, digital ou comentário no arquivo):
   *"Complete a frase: 'O maior problema que encontrei nos meus UVs hoje foi ____. Acho que aconteceu porque ____.'"*
   Quem quiser compartilhar, pode — não é obrigatório.

3. **(3 min) Ponte para a Semana 3:** *"Na próxima semana, vocês vão consolidar o Moodboard temático a partir das ideias da Semana 1 e definir, em diálogo com Modelagem 3D e Level Design, qual vai ser o Hero Asset Referência de vocês — a peça que abre UV de verdade na Semana 4. Tragam pelo menos 10 referências visuais organizadas."*

4. **(2 min) Confirmação das entregas:**
   - Arquivo `.blend` com os 3 objetos UV mapeados e checkerboard aplicado
   - Screenshot do UV Editor de cada objeto com checker ativo no Viewport
   - Anotação de qual projeção foi usada em cada objeto e por quê

---

## Possíveis Dificuldades

**1. Confusão entre o UV Editor e o Viewport**
Estudantes podem editar UVs sem perceber que estão no modo errado, ou não entender que o UV Editor mostra a "planificação" do objeto selecionado. Estratégia: pedir que o estudante olhe para os dois painéis ao mesmo tempo e relacione o que vê em cada um: *"Seleciona essa face aqui no Viewport. Agora olha no UV Editor — que parte apareceu destacada?"*

**2. Não saber distinguir distorção de sobreposição**
São dois problemas diferentes com aparências similares no checker. Distorção = o grid está deformado. Sobreposição = duas partes diferentes do objeto ocupando o mesmo espaço UV. Estratégia: ativar o Overlay de UV Stretch (distorção) no UV Editor e mostrar que a sobreposição aparece como área mais escura ou com bordas duplicadas.

**3. Expectativa de "deixar perfeito" na primeira semana técnica**
Alguns estudantes ficam presos tentando eliminar toda distorção usando só projeção automática. Estratégia: reforçar que o objetivo desta semana é observar e nomear os problemas, não resolvê-los — a solução (seams manuais) vem na Semana 4, aplicada a um asset real.

**4. Dificuldade com a navegação do Blender**
Estudantes que ainda não operaram o software (a Semana 1 foi só orientação espacial, sem prática) podem travar em operações básicas (entrar em Edit Mode, alternar viewports). Estratégia: ter um "cartão de atalhos" mínimo impresso ou compartilhado digitalmente: `Tab` (Edit/Object), `A` (selecionar tudo), `U` (menu UV), `Z` (modos de shading). Não interromper a aula para tutorial de interface.

**5. Checkerboard não aparecendo no Viewport**
Problema frequente: o estudante aplica a textura no UV Editor mas esquece de ativar Material Preview no Viewport, ou o material não tem a textura conectada ao Principled BSDF. Estratégia: durante a demo, mostrar exatamente as etapas de conexão e fixar `Z → Material Preview` como passo de verificação obrigatório.

**6. Estudante tenta amarrar o prop neutro ao próprio tema antes da hora**
Como a Semana 1 já plantou ideias individuais, alguns estudantes podem querer forçar o prop neutro a "virar" o objeto do seu tema. Estratégia: não desencorajar o entusiasmo, mas lembrar que o objetivo técnico da semana é praticar projeção, não representar o tema — a amarração formal começa na Semana 3.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não entende o checker e o que ele indica | Perguntar: *"Se essa grade fosse de tijolos reais, como eles estariam aparecendo nesse objeto?"* Usar analogia concreta antes de retornar ao conceito técnico. |
| Estudante aplica projeção mas não vê diferença entre as opções | Pedir que aplique com o checker ativo e alterne a projeção em tempo real, sem sair do modo de visualização. O contraste imediato ajuda a perceber a diferença. |
| Estudante avança rápido e termina cedo | Desafiar a prever, antes de testar, qual projeção funcionará melhor no prop neutro, e depois verificar se acertou. |
| Turma dispersa na crítica informal | Reformular como votação: *"Qual dessas duas projeções no cilindro vocês escolheriam? Levanta a mão."* Força posicionamento e mantém atenção. |
| Estudante frustrado com erros nos UVs | Recontextualizar: *"Erros em UV são muito mais fáceis de corrigir agora, em um objeto simples, do que depois em um asset real e texturizado. Vocês estão economizando horas de trabalho futuro ao perceber isso aqui."* |
| Estudante ansioso por já saber o tema/Hero Asset | Reafirmar com clareza o cronograma: *"A definição fecha na Semana 3, com calma e com o feedback de Arte Conceitual e Modelagem 3D. Hoje o foco é a ferramenta, não o tema."* |

---

## Evidências de Aprendizagem

| Evidência | Objetivo(s) relacionado(s) | Critério da Rubrica | Como avaliar |
|---|---|---|---|
| Arquivo `.blend` com 3 objetos UV mapeados e checker aplicado | Objetivos 1, 2, 3 | C3 — UV Mapping | Ausência de sobreposição, distorção aceitável para o tipo de projeção usada, checker visível no render |
| Escolha documentada de projeção (anotação textual) para cada objeto | Objetivo 3 | C1 — Processo de Projeto | Existência do registro; qualidade da justificativa, mesmo que mínima |
| Participação na crítica diagnóstica | Objetivos 2, 3 | C10 — Participação nas Critiques | Capacidade de nomear um problema visual no trabalho próprio ou do colega |
| Reflexão individual do fechamento ("maior problema encontrado") | Objetivos 1, 2 | — (qualitativa, sem nota) | Registro informal do professor sobre compreensão conceitual e necessidade de acompanhamento extra na Semana 3–4 |

> **Nota:** esta semana não gera nota. O professor registra observações qualitativas individuais, especialmente sobre quem demonstrou compreensão conceitual (distinção distorção vs. sobreposição) e quem precisará de acompanhamento extra a partir da Semana 4 (primeira crítica formal).

---

## Entrega da Semana 2

| Entrega | Formato | Escopo | Prazo |
|---|---|---|---|
| Arquivo `.blend` com cubo, cilindro e esfera UV mapeados (checkerboard aplicado) | `.blend` | Individual | Até o fim do segundo encontro |
| Screenshot do UV Editor de cada objeto com checker ativo no Viewport | PNG/JPG (pode estar dentro do `.blend` como referência de imagem) | Individual | Até o fim do segundo encontro |
| Anotação de qual projeção foi usada em cada objeto e justificativa mínima | Texto (comentário no `.blend`, `.txt` ou `.docx`) | Individual | Até o fim do segundo encontro |

> Não há entrega relacionada ao tema ou ao Hero Asset Referência nesta semana — essas entregas começam formalmente na Semana 3 (Moodboard temático + definição do Hero Asset Referência).

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 2 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
