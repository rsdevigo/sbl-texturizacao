# Plano de Aula — Semana 2
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** I — Fundamentos e Mapeamento UV  
**Tema:** Fundamentos de mapeamento UV: conceitos e projeção de textura  
**Apostila:** Parte II, Cap. 4 — Coordenadas UV e Projeções de Textura; Parte II, Cap. 6 — Texel Density e Organização de UVs  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** Informal — circulante em estúdio e comentário coletivo ao final do segundo encontro

---

## Pré-requisito da semana

Os estudantes chegam com:
- Tema do Kit Modular definido e aprovado (Semana 1)
- Moodboard finalizado e Documento de Definição de Tema entregues
- Blender instalado e com orientação espacial básica dos workspaces (Semana 1)

Nenhum conteúdo de UV foi apresentado anteriormente. Esta é a primeira vez que os estudantes abrem o UV Editor com intenção de trabalho.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é um mapa UV e por que ele é necessário para aplicar texturas em objetos 3D.
2. Descrever o espaço UV (coordenadas 0–1) e identificar distorção, sobreposição e desperdício de espaço em um layout.
3. Aplicar os quatro tipos de projeção (planar, cilíndrica, esférica, cúbica) em objetos simples e identificar qual é mais adequado a cada forma geométrica.
4. Usar a textura de checkerboard para diagnosticar distorção em UVs.
5. Relacionar texel density com a resolução perceptível de textura em diferentes partes do objeto.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Organização dos arquivos de prática (.blend), nomenclatura e screenshots entregues |
| C2 — Direção Artística | Consciência de que o UV é a base para toda texturização futura do kit |
| C3 — UV Mapping | Foco principal: distorção aceitável, ausência de sobreposição, aproveitamento básico do espaço |
| C10 — Participação | Engajamento na crítica informal, qualidade das observações sobre o trabalho dos colegas |

> **C4 a C9** ainda não são exigidos. O único resultado técnico esperado é o UV funcional sem sobreposição e com checkerboard aplicado.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Arquivo de prática preparado pelo professor: cena .blend com cubo, cilindro, esfera e um prop simples temático (ex.: barril, caixa ou pedra) — **distribuir antes do primeiro encontro ou no início da aula**
- Textura de checkerboard (incluída no Blender por padrão ou PNG externo de 1024×1024 com grid de cores)
- Projetor para demonstração
- Apostila — Parte II, Cap. 4 e Cap. 6 — disponibilizadas antes da aula

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

**1. O espaço UV (0–1)**  
O UV editor representa um quadrado de 0 a 1 nos dois eixos. A textura ocupa exatamente esse quadrado. Cada vértice do objeto 3D tem uma coordenada UV que diz "esse ponto do objeto corresponde a esse ponto da textura". Mostrar com uma imagem simples: um cubo aberto em UVs ao lado da textura que o cobre.

**2. O problema da distorção**  
Não é possível desdobrar uma esfera sem distorção — assim como não é possível desenhar um mapa-mundi perfeitamente plano. O objetivo do UV mapping não é eliminar distorção, mas controlá-la: manter a distorção em locais onde ela não é perceptível.

**3. Tipos de projeção**  
- **Planar:** projeta do mesmo ângulo que uma câmera. Funciona bem para superfícies planas. Distorce nas bordas laterais.
- **Cilíndrica:** enrola a textura ao redor do objeto. Adequada para colunas, árvores, pernas, tubos.
- **Esférica:** enrola em todas as direções. Adequada para esferas e cabeças, mas distorce nos polos.
- **Cúbica (Box):** aplica seis projeções planares nas faces do cubo imaginário ao redor do objeto. Funciona bem para formas com faces reconhecíveis.

**4. Texel density — intuição inicial**  
Texel = pixel de textura. Density = quantos texels cobrem um centímetro do objeto. Se uma parede tem o dobro do tamanho de uma pedra decorativa, ela deveria ter o dobro de espaço UV — caso contrário, a pedra vai parecer nítida e a parede vai parecer embaçada (ou vice-versa).

> **Nota do professor:** Não entre em fórmulas de texel density agora. A intuição ("islands maiores = mais nítidas") é suficiente para esta semana. O cálculo numérico vem na Semana 4. Se algum estudante perguntar os valores exatos, responda: *"Vamos medir isso na Semana 4 — por enquanto, use o checker para ver se parece uniforme."*

---

### Demonstração — 20 minutos

**Projeção UV no Blender: cubo e esfera com checkerboard**

**Setup inicial (2 min):**  
Abrir o arquivo de prática com o cubo e a esfera já na cena. Configurar o layout de tela com o Viewport 3D à esquerda e o UV Editor à direita. Explicar que trabalharemos sempre com esse layout dividido nesta semana.

**Parte 1 — Cubo (8 min):**

1. Selecionar o cubo. Entrar em Edit Mode (`Tab`).
2. Selecionar todas as faces (`A`).
3. Abrir o menu UV (`U`) e mostrar as opções disponíveis.
4. Aplicar **Cube Projection** e observar o layout gerado no UV Editor.
5. Aplicar uma textura de checkerboard via Material Preview (`Z` → Material Preview) e mostrar como o grid aparece no objeto.
6. Apontar o que está bom e o que está distorcido.

**Parte 2 — Esfera (8 min):**

1. Selecionar a esfera. Entrar em Edit Mode.
2. Testar **Sphere Projection** — mostrar a distorção nos polos.
3. Testar **Cylinder Projection** — mostrar o seam vertical e a distorção aceitável no corpo.
4. Testar **Smart UV Project** — mostrar o resultado automático, sem edição humana.
5. Comentar: *"Smart UV Project é rápido mas não é inteligente. Ele não sabe o que é importante no objeto. Para o nosso kit, vamos sempre revisar o resultado."*

**Fechamento da demo (2 min):**  
Mostrar brevemente como verificar sobreposição de UV islands (Overlay → UV Stretch no UV Editor). Indicar o que é vermelho (estiramento) e o que é azul (compressão).

> **Nota do professor:** Não execute seams manuais ainda — isso é Semana 3. Se os estudantes perguntarem "como cortar para abrir melhor?", responda que é o próximo passo: *"Agora estamos entendendo o problema. Na semana que vem, aprendemos a controlar onde cortar."*

---

### Produção em Estúdio — 50 minutos

**Praticar projeções UV em objetos geométricos simples**

**Consigna entregue verbalmente:**

> *"Vocês vão trabalhar nos três objetos do arquivo de prática — cubo, cilindro e esfera. Para cada um, testem pelo menos dois tipos de projeção, apliquem o checkerboard e identifiquem qual projeção gera menos distorção. Não tem resposta errada — tem observação certa ou errada. O que eu quero ver é vocês olhando para o checker e conseguindo descrever o que está acontecendo."*

**Atividade estruturada:**

1. Abrir o arquivo de prática (.blend com cubo, cilindro, esfera).
2. Para cada objeto:
   - Testar pelo menos 2 tipos de projeção UV (`U` no Edit Mode).
   - Aplicar textura de checkerboard e ativar Material Preview.
   - Fazer screenshot do resultado no UV Editor + Viewport com o checker.
   - Anotar no próprio arquivo (ou em um documento de texto): "qual projeção escolhi e por quê".
3. Se terminar antes, começar a explorar o prop temático incluído no arquivo (barril, caixa ou pedra) e tentar aplicar Cube ou Smart UV Project nele.

**Papel do professor:**

Circular pelo estúdio fazendo perguntas diagnósticas:
- *"O que esse vermelho no checker está dizendo?"*
- *"Se a textura fosse uma imagem de tijolo, que parte do objeto ficaria esticada?"*
- *"Por que você escolheu essa projeção para o cilindro?"*

Identificar quem avançou rápido (será desafiado a explorar o prop temático) e quem está travado na navegação do Blender (atenção extra no próximo encontro).

> **Nota do professor:** Não interrompa o estúdio para corrigir erros de forma. Deixe os estudantes experimentarem e errarem. Os erros serão o material da crítica do próximo encontro.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: Diagnóstico visual compartilhado**

Não é apresentação formal. Cada estudante mostra na tela o seu resultado mais interessante (ou mais problemático) dos três objetos.

**Roteiro:**

1. **(5 min)** Professor seleciona 3–4 trabalhos com problemas distintos e visíveis (sobreposição, estiramento forte, escolha de projeção inadequada). Projetar na tela.
2. **(10 min)** Para cada trabalho projetado, a turma responde:
   - *"O que vocês veem de errado aqui?"*
   - *"Que tipo de projeção foi usada? Faz sentido para essa forma?"*
   - *"Se fosse a textura final do kit de vocês, onde isso apareceria como problema?"*
3. **(5 min)** Professor sistematiza: reforça os três diagnósticos mais comuns que apareceram (distorção, sobreposição, espaço desperdiçado) e antecipa como eles serão resolvidos nas próximas semanas com seams manuais.

> **Nota do professor:** Escolha trabalhos que mostrem erros comuns e instrutivos, não os piores da turma. O objetivo não é expor o estudante, mas usar o erro como material didático. Sempre peça autorização antes de projetar: *"Posso usar o seu para mostrar esse caso?"* Nunca projete sem permissão.

**Conectar à rubrica:**  
Ao final, mencionar explicitamente: *"Na crítica formal da Semana 3, vamos olhar para o C3 — UV Mapping. O que vimos hoje é exatamente o que o Nível 2 da rubrica descreve. Vejam o Nível 3 e entendam o que falta para chegar lá."*

---

### Produção em Estúdio — 60 minutos

**Aplicar UV no prop temático e preparar entrega**

**Consigna:**

> *"Agora o objetivo muda. Vocês já praticaram nos objetos simples. Agora apliquem o que aprenderam no prop temático do arquivo. Escolham a melhor projeção que encontrarem, apliquem o checker e organizem o UV Editor de forma que as islands não se sobreponham. Esse arquivo vai ser a entrega da semana."*

**Atividade:**

1. Abrir o prop temático do arquivo de prática (ou usar o mesmo arquivo com os três objetos — todos devem ter checker aplicado).
2. Aplicar projeção UV no prop usando o método que fizer mais sentido para a forma.
3. Verificar distorção com o checkerboard e ativar UV Stretch Overlay.
4. Organizar as islands no UV Editor para evitar sobreposição.
5. Salvar o arquivo com nomenclatura `[Nome]_UV_Semana02.blend`.
6. Capturar screenshot do UV Editor e do Viewport com checker ativo.
7. Quem terminar com tempo: explorar o UV do primeiro asset do seu próprio kit modular (modelagem trazida de disciplinas anteriores, se houver).

**Papel do professor:**

Priorizar atenção individual para:
- Estudantes que na crítica mostraram confusão conceitual sobre sobreposição de UVs.
- Estudantes que não conseguiram concluir os três objetos no primeiro encontro.

Para quem avança rápido:
- *"Agora aplica no modelo do seu kit. Não precisa ser perfeito — o objetivo é você ver os problemas que vão aparecer com uma forma real."*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min)** Síntese rápida: *"Hoje vocês aprenderam a linguagem básica do UV mapping. Sabem o que é distorção, sabem o que o checker está dizendo, sabem que a projeção depende da forma. Essa consciência vai com vocês até o final do semestre."*

2. **(3 min)** Reflexão individual registrada (em papel, post-it digital ou comentário no arquivo):  
   *"Complete a frase: 'O maior problema que encontrei nos meus UVs hoje foi ____. Acho que aconteceu porque ____.'*  
   Quem quiser compartilhar, pode. Não é obrigatório.

3. **(3 min)** Antecipação da Semana 3: *"Na próxima semana, vocês vão aprender a controlar onde o Blender corta a malha antes de desdobrar — isso se chama seam. Com seams bem posicionados, a distorção que vocês viram hoje desaparece. E na Semana 3 tem crítica formal: usem a rubrica para fazer a autoavaliação antes de chegar aqui."*

4. **(2 min)** Confirmação das entregas:
   - Arquivo `.blend` com os 3 objetos UV mapeados e checkerboard aplicado
   - Screenshot do UV Editor de cada objeto (pode ser dentro do próprio arquivo como referência, ou imagens separadas)
   - Anotação de qual projeção foi usada em cada objeto e por quê (pode ser um comentário de texto dentro do Blender ou documento separado)

---

## Possíveis Dificuldades

**1. Confusão entre o UV Editor e o Viewport**  
Estudantes podem editar UVs sem perceber que estão em modo errado, ou não entender que o UV Editor mostra a "planificação" do objeto selecionado. Estratégia: sempre pedir que o estudante olhe para os dois painéis ao mesmo tempo e relacione o que vê em cada um: *"Seleciona essa face aqui no Viewport. Agora olha no UV Editor — que parte apareceu destacada?"*

**2. Não saber distinguir distorção de sobreposição**  
São dois problemas diferentes com aparências similares no checker. Distorção = o grid está deformado. Sobreposição = duas partes diferentes do objeto ocupando o mesmo espaço UV. Estratégia: no UV Editor, ativar o Overlay de UV Stretch (distorção) e mostrar que a sobreposição aparece como área mais escura ou com bordas duplicadas.

**3. Expectativa de "deixar perfeito" na primeira semana**  
Alguns estudantes ficam presos tentando eliminar toda distorção usando só projeção automática. Estratégia: reforçar que o objetivo esta semana é observar e nomear os problemas, não resolvê-los. A solução (seams) vem na Semana 3.

**4. Dificuldade com a navegação do Blender**  
Estudantes que não usaram o Blender nas semanas anteriores podem travar em operações básicas (entrar em Edit Mode, alternar viewports). Estratégia: ter um "cartão de atalhos" mínimo impresso ou compartilhado digitalmente: `Tab` (Edit/Object), `A` (selecionar tudo), `U` (UV menu), `Z` (modos de shading). Não interromper a aula para tutorial de interface.

**5. Checkerboard não aparecendo no Viewport**  
É um problema frequente: o estudante aplica a textura no UV Editor mas esquece de ativar Material Preview no Viewport. Ou o material não tem a textura conectada ao Principled BSDF. Estratégia: durante a demo, mostrar exatamente as etapas de conexão e fixar o passo de ativar `Z → Material Preview` como verificação obrigatória.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não entende o checker e o que ele indica | Perguntar: *"Se essa grade fosse de tijolos reais, como eles estariam aparecendo nesse objeto?"* Usar analogia concreta antes de retornar ao conceito técnico. |
| Estudante aplica projeção mas não vê diferença entre as opções | Pedir que aplique com o checker ativo e mude de projeção em tempo real sem sair do modo de visualização. O contraste imediato ajuda a perceber a diferença. |
| Estudante avança rápido e termina cedo | Desafiar a aplicar UV no próprio asset do kit modular (modelagem trazida de disciplina anterior) e identificar os problemas que aparecerão. |
| Turma dispersa na crítica informal | Reformular como votação: *"Qual dessas duas projeções no cilindro vocês escolheriam? Levanta a mão."* Força posicionamento e mantém atenção. |
| Estudante frustrado com erros nos UVs | Recontextualizar: *"Erros em UV são muito mais fáceis de corrigir agora do que depois de texturizar. Você está economizando horas de trabalho futuro ao perceber isso aqui."* |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Arquivo .blend com 3 objetos UV mapeados e checker aplicado | C3 — UV Mapping | Ausência de sobreposição, distorção aceitável para o tipo de projeção, checker visível no render |
| Escolha documentada de projeção (anotação textual) | C1 — Processo de Projeto | Existência do registro; qualidade da justificativa (mesmo que mínima) |
| Participação na crítica diagnóstica | C10 — Participação | Capacidade de nomear um problema visual no trabalho próprio ou do colega |
| Screenshot do UV Editor com a island organizada | C3 — UV Mapping | Islands sem sobreposição, ocupação básica do espaço UV |

> **Nota:** Esta semana não gera nota. O professor registra observações qualitativas individuais, especialmente sobre quem demonstrou compreensão conceitual (distinção distorção vs. sobreposição) e quem precisará de acompanhamento extra na Semana 3 (primeira crítica formal).

---

## Entrega da Semana 2

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo .blend com cubo, cilindro e esfera UV mapeados (checkerboard aplicado) | .blend | Até o fim do segundo encontro |
| Screenshot do UV Editor de cada objeto com checker ativo no Viewport | PNG ou JPG (pode estar dentro do .blend como referência de imagem) | Até o fim do segundo encontro |
| Anotação de qual projeção foi usada em cada objeto e justificativa mínima | Texto (comentário no .blend, .txt ou .docx) | Até o fim do segundo encontro |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 2 | 2026*
