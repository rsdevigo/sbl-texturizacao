# Plano de Aula — Semana 7
**Disciplina:** Texturização | **Metodologia:** Studio-Based Learning  
**Unidade:** II — Materiais PBR e Workflow  
**Tema:** Mapas PBR avançados: Normal Map e geração procedural  
**Apostila:** Parte V, Cap. 16 — Normal Maps e Transferência de Detalhes; Parte IV, Cap. 13 — Texturização Procedural (geração procedural no Blender)  
**Carga horária:** 3h (2 encontros de 1h30)  
**Crítica:** 🔵 Informal — Crítica circulante com ênfase em leitura de profundidade e coerência do material

---

## Pré-requisito da semana

Os estudantes chegam com:

- Asset 01 com UV otimizado + textura seamless aplicada no canal Albedo (Principled BSDF com Metallic e Roughness preservados da Semana 5) — Semana 6
- Asset 02 com UV aberto + textura seamless (completo ou em estágio avançado) — Semana 6
- Arquivo `.kra` do Krita com camadas preservadas para cada textura seamless criada
- Compreensão consolidada de: projeção UV, plausibilidade PBR, criação de textura seamless, Krita, fontes livres (Poly Haven, AmbientCG)

> **Nota de transição:** Alguns estudantes podem chegar com o Asset 02 ainda sem textura seamless aplicada — a entrega da Semana 6 previa esse caso. O início do Estúdio 1 reserva tempo para que esses estudantes concluam o Albedo antes de avançar para os novos mapas. Não prosseguir para Normal Map sem Albedo funcional conectado.

> **Transição pedagógica desta semana:** nas Semanas 5 e 6, o material PBR ganhou forma progressivamente — primeiro com valores planos (Semana 5), depois com uma imagem real no Albedo (Semana 6). A Semana 7 é o momento em que o material deixa de ser **plano** e passa a ter **profundidade**. O Normal Map simula relevos e micro-geometria sem adicionar polígonos; o Roughness Map faz o brilho variar dentro da mesma superfície. O conteúdo procedural com nós introduz o Blender como motor de geração de textura — não apenas receptor de imagens externas. A saída desta semana é o primeiro material PBR **completo**: todos os canais principais conectados (Albedo + Metallic + Roughness + Normal).

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar como um Normal Map simula relevo de superfície sem alterar a geometria, diferenciando espaço tangente de espaço objeto.
2. Distinguir Normal Map de Bump Map e justificar quando usar cada um no contexto de um asset de jogo.
3. Gerar um Normal Map procedural no Blender usando os nós Noise Texture → Bump → Normal Map e conectá-lo ao Principled BSDF.
4. Criar variação de Roughness dentro de um material usando os nós Noise Texture e ColorRamp.
5. Montar um material PBR completo no Blender com os quatro canais principais conectados: Albedo (Image Texture), Metallic (valor), Roughness (nó procedural) e Normal (nó procedural ou mapa).

> O Subsurface Scattering (SSS) não é abordado nesta semana — ele é apresentado na Semana 8, junto ao sistema de canais do 3D Coat, para não sobrecarregar esta mini-aula com um quinto conceito novo.

---

## Critérios observados nesta semana

> ⚠️ **Semana sem crítica formal — nenhuma nota é atribuída.** O professor observa e registra evidências nos critérios abaixo para calibrar a avaliação da CF3 (sem 8). O estudante recebe feedback oral durante o estúdio.

| Critério | O que observar |
|---|---|
| C1 — Processo de Projeto | Organização do node tree (nomenclatura dos nós, uso de frames); registro visual do material antes e depois do Normal Map |
| C2 — Direção Artística | Coerência do relevo simulado pelo Normal Map com o universo do kit; variação de roughness que conta a história do material |
| C4 — Materiais PBR | Construção do material completo: todos os quatro canais conectados com lógica física correta |
| C5 — Texturização | Primeiro contato observável: a profundidade visual adicionada pelo Normal Map + variação de Roughness será avaliada formalmente na CF3 |
| C10 — Participação (CC) | Qualidade da leitura crítica na critique informal: capacidade de identificar onde o Normal Map adiciona ou não credibilidade visual |

> **Progressão do PA — entre CF2 e CF3:** Esta é a segunda semana antes da CF3 (sem 8). C4 e C5 estão em desenvolvimento ativo. C5 começa a ser observado de forma substantiva esta semana — a profundidade visual adicionada pelo Normal Map + variação de Roughness é a evidência central. O professor registra observações para calibrar a avaliação de C4 e C5 na CF3.

---

## Recursos necessários

- Computadores com Blender instalado (3.x ou 4.x)
- Krita instalado (para eventuais ajustes nas texturas seamless)
- Arquivos `.blend` do Asset 01 e Asset 02 de cada estudante (Semanas 4–6)
- Arquivo `.kra` do Krita com as texturas seamless preservadas em camadas
- Arquivo de demonstração do professor: Asset simples (cubo ou parede) com textura seamless já conectada ao Albedo
- Acesso à internet (Poly Haven como fonte de Normal Maps para referência de qualidade)
- Projetor para demonstração
- Apostila — Parte V, Cap. 16 e Parte IV, Cap. 13 — disponibilizadas antes da aula
- HDRI de iluminação neutra no Blender para visualização correta do Normal Map (arquivos dos estudantes já devem ter HDRI das semanas anteriores)

> **Nota sobre Blender 4.x:** O nó Musgrave Texture foi incorporado ao nó Noise Texture no Blender 4.0 (parâmetro *Detail* e *Roughness* expandidos cobrem os casos de uso do Musgrave). Na demonstração, verificar a versão instalada no laboratório e adaptar a nomenclatura dos nós conforme necessário. Em Blender 3.x, o Musgrave Texture ainda existe como nó separado.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Normal Map e geração procedural: adicionando profundidade sem adicionar geometria**

Objetivo: mostrar que os mapas de textura não são apenas "imagens sobre a superfície" — alguns mapas alteram a forma como a luz interage com o objeto, simulando geometria que não existe. Esse princípio é central na produção de assets para jogos em tempo real, onde o custo de polígonos é limitado.

**Desenvolvimento:**

Abrir com uma comparação visual no projetor (imagens estáticas):

Mostrar três versões do mesmo asset de parede de pedra:
1. Material com apenas Albedo conectado (resultado da Semana 6).
2. O mesmo asset com Normal Map aplicado — a superfície parece ter blocos de pedra com volume, rachaduras e relevos.
3. O mesmo asset com Normal Map + Roughness Map — partes da pedra têm brilho diferente, como se houvesse variação de polimento entre as superfícies planas e as arestas desgastadas.

Perguntar: *"O que mudou entre a imagem 1 e a imagem 2? A geometria do asset é a mesma nos três casos — nenhum polígono foi adicionado."*

---

**Conteúdo a cobrir:**

**1. O que é um Normal Map e como ele funciona**

Um Normal Map é uma imagem RGB onde cada pixel armazena um vetor de direção — a "normal" da superfície naquele ponto. Quando o motor de renderização calcula como a luz incide sobre o asset, ele usa os vetores do Normal Map em vez dos vetores reais da geometria. O resultado é que superfícies planas parecem ter relevo e volume.

A codificação de cores do Normal Map em espaço tangente segue uma convenção: o canal R armazena a direção X (esquerda/direita), o canal G armazena a direção Y (cima/baixo), e o canal B armazena a direção Z (profundidade — perpendicular à superfície). Por isso mapas de espaço tangente têm sempre aquele tom azulado predominante: a maioria dos vetores aponta "para fora" da superfície (Z alto = B alto).

**Espaço tangente vs. espaço objeto:**

- **Espaço tangente** (mais comum): os vetores são relativos à superfície local de cada polígono. O mapa pode ser aplicado a qualquer objeto, independentemente de sua orientação no mundo. A maioria dos Normal Maps de jogos é espaço tangente.
- **Espaço objeto**: os vetores são absolutos (relativos ao centro do objeto). Só funciona corretamente se o objeto não for rotacionado. Raramente usado em produção, exceto em casos específicos de bake.

**Normal Map vs. Bump Map:**

Um Bump Map é uma imagem em escala de cinza onde os valores representam altura relativa (branco = alto, preto = baixo). O motor calcula a normal a partir do gradiente dessa imagem. É mais simples, mas produz resultados menos precisos e não pode ser exportado para uso em outros motores sem recálculo. O Normal Map armazena os vetores diretamente — é mais preciso e portável.

No Blender, é possível converter um Bump Map em contribuição de Normal Map usando os nós **Bump** → conectando à entrada *Normal* do Principled BSDF. É um atalho funcional quando não há um Normal Map baked disponível.

**2. Geração procedural de Normal Maps e Roughness no Blender**

O Blender possui um sistema de nós (Shader Editor) que permite gerar texturas matematicamente, sem precisar de imagens externas. Para esta semana, os nós mais relevantes são:

- **Noise Texture:** gera um padrão de ruído orgânico, configurável por escala, detalhe e rugosidade. Usado como base para simular variações de superfície (micro-relevo, variação de brilho).
- **Musgrave Texture** (Blender 3.x) / **Noise Texture com Detail alto** (Blender 4.x): ruído com mais controle sobre a frequência e estrutura. Gera superfícies com aspecto mais "rochoso" ou "nublado".
- **Bump node:** recebe um valor escalar (de qualquer textura ou math node) e o interpreta como mapa de altura, gerando uma contribuição normal que pode ser conectada à entrada *Normal* do Principled BSDF.
- **ColorRamp:** converte valores contínuos em faixas de cor/valor discretas. Usado para transformar o ruído em um Roughness Map com contraste controlado (ex: áreas altas do relevo ficam mais polidas, áreas baixas ficam mais matte).

**Workflow simplificado para esta semana:**

```
Noise Texture → Bump → Normal (entrada do Principled BSDF)
Noise Texture → ColorRamp → Roughness (entrada do Principled BSDF)
```

Ou, com mais controle:

```
Noise Texture A (escala pequena, micro-detalhe) → Bump
Noise Texture B (escala grande, macro-relevo) → MixRGB/Math → Bump
→ Normal (entrada do Principled BSDF)
```

> **Nota do professor:** O Subsurface Scattering (SSS) não é tratado nesta mini-aula — ele será apresentado na Semana 8, como um canal adicional do sistema de camadas do 3D Coat. Isso mantém o foco de hoje inteiramente no Normal Map e na variação procedural de Roughness.

---

### Demonstração — 20 minutos

**Criação de um material PBR completo com Normal Map e Roughness procedurais no Blender**

**Setup (1 min):**  
Abrir o Blender com o asset de demonstração já carregado — uma parede simples (ou cubo subdividido) com a textura seamless de pedra da Semana 6 já conectada ao Albedo. O Shader Editor deve estar visível ao lado do Viewport (layout horizontal).

**Percurso da demonstração:**

**Passo 1 — Adicionar o Noise Texture para o Normal Map (4 min):**
1. No Shader Editor: `Shift+A → Texture → Noise Texture`.
2. Ajustar parâmetros ao vivo:
   - **Scale:** 8.0 (escala de repetição do ruído — explicar: valores maiores = micro-detalhe mais fino)
   - **Detail:** 6.0 (camadas de frequência sobrepostas — mais detalhe orgânico)
   - **Roughness:** 0.6
3. `Shift+A → Vector → Bump`.
4. Conectar a saída `Fac` do Noise Texture à entrada `Height` do nó Bump.
5. Conectar a saída `Normal` do Bump à entrada `Normal` do Principled BSDF.
6. No Viewport Rendered: mostrar o resultado — a superfície plana agora tem micro-relevo visível.
7. Ajustar o parâmetro `Strength` do Bump node de 1.0 para 0.3: *"O Normal Map procedural tende a ser muito forte com os valores padrão. Calibrar o Strength é a forma de controlar a intensidade sem refazer o nó."*

**Passo 2 — Adicionar variação de Roughness (5 min):**
1. `Shift+A → Texture → Noise Texture` (um segundo nó separado).
2. Ajustar Scale para 4.0 (escala maior = variação mais ampla, menos "pixelada").
3. `Shift+A → Converter → ColorRamp`.
4. Conectar `Fac` do segundo Noise Texture à entrada do ColorRamp.
5. Ajustar o ColorRamp para criar contraste:
   - Marcador esquerdo (preto): posição 0.3, cor cinza escuro (Roughness alto = mais matte)
   - Marcador direito (branco): posição 0.7, cor cinza claro (Roughness baixo = mais polido)
6. Conectar a saída `Color` do ColorRamp à entrada `Roughness` do Principled BSDF.
7. No Viewport Rendered: mostrar como partes da pedra agora têm brilho diferente — *"Parece que algumas faces da pedra foram polidas pelo desgaste e outras permanecem matte. Essa variação é o que faz o material parecer usado, não fabricado."*

**Passo 3 — Organizar o node tree (3 min):**
1. Selecionar os nós do Normal Map: `Ctrl+J` para agrupar em um Frame.
2. Selecionar os nós do Roughness: `Ctrl+J` para outro Frame.
3. Nomear os frames clicando no label: `Normal_Procedural` e `Roughness_Variacao`.
4. Comentar: *"Organizar o node tree em frames é equivalente a organizar camadas no Krita — em projetos reais, o Shader Editor pode ter 30, 40 nós. Sem estrutura, fica impossível de manter."*

**Passo 4 — Verificação final (5 min):**
1. Rodar a câmera ao redor do asset no Viewport Rendered.
2. Comparar com e sem os nós de Normal e Roughness (desabilitar os frames temporariamente com `M`).
3. Mostrar o antes/depois: *"O asset é idêntico geometricamente. O que mudou foi a informação que chegou para o cálculo de luz. Isso é o princípio central de PBR: simular física, não falsificar aparência."*

> **Nota do professor:** Manter o arquivo de demonstração salvo para referência durante o estúdio. Se um estudante travar em algum nó, apontar para a tela do professor: *"Olha como está montado aqui — qual nó está diferente no seu?"*

---

### Produção em Estúdio — 50 minutos

**Conclusão do Albedo do Asset 02 (se necessário) + início do Normal Map e Roughness no Asset 01**

**Consigna entregue verbalmente:**

> *"Este estúdio tem dois blocos. Quem chegou com o Albedo do Asset 02 ainda sem textura seamless conectada: os primeiros 15 minutos são para isso. Abre o Krita, faz o seamless, conecta ao Albedo do Asset 02 — o mesmo processo da semana passada. Para quem o Asset 02 já está com Albedo: começa agora no Asset 01 ou 02, adicionando os dois nós que a demonstração mostrou — Noise Texture para Normal Map via Bump, e Noise Texture + ColorRamp para Roughness. O objetivo do estúdio é ter um dos seus assets com o material PBR tendo pelo menos três canais conectados: Albedo + Normal + Roughness."*

**Atividade estruturada:**

**Bloco A — Para quem ainda não concluiu o Albedo do Asset 02 (≈15 min):**
1. Abrir o Krita com o arquivo `.kra` da textura seamless do Asset 02.
2. Se necessário, ajustar o patch de bordas e re-exportar o PNG.
3. Abrir o `.blend` do Asset 02, criar material no Principled BSDF.
4. Conectar a textura seamless ao `Base Color`.
5. Salvar como `[Nome]_Asset02_Textura_S07_base.blend`.

**Bloco B — Para toda a turma (≈35 min):**
1. Abrir o arquivo `.blend` do Asset 01 com a textura seamless já conectada (Semana 6).
2. No Shader Editor, adicionar `Noise Texture` → `Bump` → conectar ao `Normal` do Principled BSDF.
3. Calibrar Scale e Strength do Bump para que o relevo seja perceptível mas não exagerado.
4. Adicionar segundo `Noise Texture` → `ColorRamp` → conectar ao `Roughness` do Principled BSDF.
5. Ajustar o ColorRamp para criar contraste coerente com o material do kit (pedra tende a ter roughness alto 0.6–0.9; metal tratado pode ter range 0.2–0.7).
6. Organizar o node tree em frames nomeados.
7. Capturar screenshot do node tree + render no Viewport para comparação.
8. Salvar: `[Nome]_Asset01_PBR_S07.blend`.

**Papel do professor:**

Circular e verificar três pontos em cada estação:

- **O Normal Map está conectado corretamente?** Confirmar que a saída do Bump node está chegando à entrada *Normal* do Principled BSDF — não à entrada *Base Color* por engano.
- **O Roughness tem variação visível?** Um ColorRamp com faixa muito estreita ou sem contraste não produz variação perceptível. Pedir para o estudante mostrar o material com e sem o ColorRamp habilitado: a diferença deve ser visível.
- **A escala dos nós procedurais é coerente com o asset?** Um Scale muito baixo (1–2) no Noise Texture produz um relevo com "ondas" grandes que não parecem com o material real. Orientar Scale entre 5–15 para micro-texturas.

Perguntas de mediação circulante:

- *"Esse Bump está com Strength 1.0 — o relevo está muito agressivo. O que acontece se você baixa para 0.2? O Strength controla a intensidade sem alterar a estrutura do nó."*
- *"O ColorRamp está com as duas paradas muito próximas — a variação de Roughness é quase zero. Arrasta as paradas para aumentar o contraste: uma mais escura, outra mais clara."*
- *"A escala do Noise do Normal e a escala do Noise do Roughness precisam ser iguais? Experimenta colocar valores diferentes — um micro, outro macro — e vê o que acontece visualmente."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

**Formato: crítica circulante com ênfase em leitura de profundidade e calibração do Normal Map**

Esta é uma crítica informal. O professor conduz a turma por 4–5 estações, com foco em verificar se o Normal Map adiciona credibilidade ao material ou se está mal calibrado (exagerado, fraco, ou com escala errada).

**Protocolo:**

**Abertura (2 min):**  
Professor define o foco: *"Hoje vamos olhar para profundidade. Pergunta central: o Normal Map desse material faz você acreditar que a superfície tem textura real, ou ele parece artificial? Vamos olhar para três coisas: (1) o relevo tem escala compatível com o material — as pedras têm tamanho físico crível? (2) a variação de Roughness conta alguma história — parece que algo aconteceu com esse material? (3) o node tree está organizado — consigo entender o que cada bloco faz?"*

**Rodada circulante (15 min — 4–5 estações):**

Para cada trabalho, conduzir com perguntas:

- *"Fecha os olhos e abre. Esse material parece ser de pedra [ou madeira, metal, etc.]? Se a resposta imediata for 'parece plástico', o Normal Map provavelmente está fraco ou na escala errada."*
- *"Qual é a história desse material? Onde ele foi mais polido? Onde acumulou sujeira? O ColorRamp de Roughness está respondendo a alguma lógica de uso, ou é só ruído aleatório?"*
- *"Mostra o node tree. Consigo identificar qual parte faz o Normal e qual faz o Roughness sem você me explicar? Se sim, a organização está boa."*

**Fechamento da crítica (3 min):**  
Sintetizar os padrões observados:
- Qual o erro mais comum na calibração do Bump (tipicamente: Strength muito alto ou Scale muito baixo gerando ondas visíveis ao invés de micro-textura)?
- Estado geral da variação de Roughness — os materiais estão ganhando historia ou ainda parecem uniformes?
- Orientação para o estúdio: *"Quem tem o Normal Map com escala errada: ajusta o Scale do Noise Texture primeiro. Quem está satisfeito com Asset 01: avança para o Asset 02 — o objetivo é ter os dois com material PBR completo ao final deste encontro."*

---

### Produção em Estúdio — 60 minutos

**Conclusão do material PBR completo do Asset 02 (todos os quatro canais conectados)**

**Consigna:**

> *"Sessenta minutos para fechar a semana. O objetivo é ter os dois assets com material PBR completo: Albedo conectado (textura seamless), Metallic com valor calibrado, Roughness com variação procedural via ColorRamp, e Normal Map via Bump procedural. Quem terminar os dois assets antes do fechamento: avança para testar variações — troca a escala do Noise, experimenta dois Noise Textures misturados para o Normal, ou testa um valor baixo de SSS em um material orgânico se o kit tiver um elemento assim."*

**Atividade:**

**Parte 1 — Material PBR completo do Asset 02 (≈40 min):**
1. Abrir o `.blend` do Asset 02 com textura seamless no Albedo.
2. Verificar e calibrar o valor de Metallic conforme o material (0 para pedra/madeira/concreto; 1 para metal puro; intermediário apenas para materiais mistos ou enferrujados com cuidado).
3. Adicionar `Noise Texture` → `Bump` → conectar ao `Normal` do Principled BSDF.
4. Calibrar Scale e Strength coerentes com o material do Asset 02 (não necessariamente os mesmos valores do Asset 01 — dois materiais diferentes têm micro-relevo diferente).
5. Adicionar segundo `Noise Texture` → `ColorRamp` → conectar ao `Roughness`.
6. Calibrar o range do ColorRamp para o material específico (referência: pedra 0.65–0.90; madeira 0.55–0.80; metal tratado 0.20–0.60; metal enferrujado 0.50–0.85).
7. Organizar o node tree em frames nomeados.
8. Capturar screenshot do node tree + render Viewport.
9. Salvar: `[Nome]_Asset02_PBR_S07.blend`.

**Parte 2 — Refinamento do Asset 01 se necessário + variações avançadas (≈20 min):**

Para estudantes que concluíram os dois assets:
1. Experimentar adicionar um terceiro nó ao Normal Map: dois Noise Textures com escalas diferentes (micro e macro) combinados via nó `Math → Add` antes do Bump. O resultado simula materiais com detalhe em múltiplas escalas (ex: pedra com micro-rugosidade E rachados maiores).
2. Ou: exportar o material do Asset 01 como `.blend` de material reutilizável para usar como ponto de partida nos próximos assets do kit.
3. Ou: começar a mapear a textura seamless também ao canal `Normal` diretamente — conectar o PNG do Poly Haven que inclui Normal Map e comparar com o Normal Map procedural.
4. Ou: se o kit tiver um elemento orgânico (planta, vela, tecido), adiantar a leitura do trecho de Subsurface Scattering na Apostila (Semana 8) e testar informalmente o parâmetro `Subsurface` do Principled BSDF — sem cobrança de entrega, apenas exploração.

**Papel do professor:**

- Para estudantes calibrando o Asset 02: *"O Roughness do Asset 02 usa o mesmo range do Asset 01? Esses dois materiais no seu kit têm a mesma rugosidade base? Se um é madeira e outro é pedra, o range no ColorRamp deve ser diferente."*
- Para estudantes com Metallic incorreto: *"Esse valor de Metallic 0.5 — o que seria um material com Metallic no meio? Em PBR físico, quase nenhum material real fica no meio. Ou é metal (1) ou não é (0). Ferrugem, por exemplo, é tratada como dielétrico (0) com a cor do ferrugem no Albedo, não como Metallic intermediário."*
- Para estudantes avançados: *"Conecta os dois Noise Textures com escalas diferentes — um no 5 e outro no 15 — no mesmo Bump. Precisa de um nó Math entre eles. O que muda no resultado visual comparado com um único Noise?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese técnica)**  
*"Hoje vocês montaram um material PBR completo pela primeira vez — com quatro canais trabalhando juntos. O Normal Map dá profundidade, o Roughness Map dá variação de brilho, o Albedo dá cor e identidade. Esse é o conjunto mínimo de um material de jogo profissional. Na Semana 8 vocês vão fazer exatamente isso, mas dentro do 3D Coat — que é uma ferramenta projetada especificamente para esse fluxo, com mais controle artístico."*

2. **(3 min — Reflexão de processo)**  
Pergunta para 2–3 voluntários: *"O Normal Map procedural que vocês criaram hoje — ele representa bem o material do kit? Se alguém olhar para o asset, vai conseguir dizer o que é o material só pelo relevo? O que o Normal Map está simulando que não existia antes?"* O objetivo é conectar a decisão técnica (parâmetros do Noise) com a intenção artística (micro-textura coerente com o universo visual do kit).

3. **(3 min — Antecipação da Semana 8)**  
*"Na semana que vem: Crítica FORMAL. Isso significa que vocês vão apresentar o trabalho para a turma usando a rubrica — inclusive a autoavaliação que entregam antes da apresentação. O tema da Semana 8 é o 3D Coat, que vai permitir que vocês pintem os mapas PBR diretamente sobre o asset em 3D — muito mais intuitivo do que montar nós. Para a crítica formal, o material que vocês têm hoje é o ponto de partida — não precisam refazer tudo, mas precisam conseguir justificar cada canal conectado. Preparem screenshots dos node trees e renders comparativos antes/depois para a apresentação."*

4. **(2 min — Confirmação das entregas)**  
Recapitular entregas com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Normal Map conectado ao canal errado (Base Color ao invés de Normal)**  
É o erro mais frequente ao montar o node tree pela primeira vez. O resultado é que o Albedo se torna azulado (cor do Normal Map) e o relevo não aparece. Estratégia: verificar visualmente se o Principled BSDF tem um fio roxo chegando à entrada *Normal* (abaixo de Roughness) — esse fio deve vir do nó Bump, não diretamente do Noise Texture. Se o fio amarelo do Noise Texture for conectado diretamente à entrada Normal, também não funciona corretamente.

**2. Bump com Strength muito alto — relevo exagerado e irreal**  
O parâmetro padrão `Strength = 1.0` do nó Bump tende a ser excessivo para micro-texturas orgânicas. Superfícies de pedra ou madeira com Strength alto parecem cráteres lunares. Estratégia: orientar o estudante a comparar com referência visual (foto do Poly Haven do mesmo material) e baixar o Strength progressivamente até o relevo parecer fisicamente crível. Range típico: pedra 0.2–0.4, madeira 0.1–0.3, metal 0.05–0.15.

**3. Scale do Noise Texture inadequado para o tamanho do asset**  
Um Scale de 1–2 gera ondulações muito grandes no asset — parece um terreno, não uma textura. Um Scale de 50+ gera ruído tão fino que some no render. A escala correta depende do tamanho físico do asset no mundo. Estratégia: pedir para o estudante ligar o Texture Coordinate com *Object* (em vez de *Generated*) para que o Scale corresponda ao tamanho real do objeto. Depois calibrar visualmente a partir de 8–12 como ponto de partida.

**4. ColorRamp com variação de Roughness invisível**  
Se os dois marcadores do ColorRamp ficarem muito próximos em valor (ex: 0.6 e 0.65), a variação de Roughness é imperceptível. Estratégia: pedir para o estudante mover os marcadores para extremos mais distantes (0.4 e 0.85) e observar o viewport. A diferença deve ser visível na comparação de brilho entre áreas. Se ainda invisível, verificar se o fio está chegando corretamente à entrada *Roughness* do Principled BSDF.

**5. Estudante conecta o Normal Map procedural E uma textura de imagem ao mesmo canal**  
Ao experimentar conectar um Normal Map de imagem (do Poly Haven) ao canal Normal, o estudante pode sobrescrever acidentalmente o nó Bump procedural sem perceber. O Principled BSDF aceita apenas uma entrada por canal. Estratégia: explicar que para combinar dois Normals (procedural + baked/imagem) é necessário um nó `Mix Shader` não — mas um nó específico para normais: `Vector → Mix` com modo *Overlay* ou *Add*. Para esta semana, orientar a usar apenas um dos dois — o procedural — e deixar a combinação para semanas posteriores.

**6. Estudante ainda sem Albedo no Asset 02 no início do Encontro 2**  
Se o tempo do Bloco A do Estúdio 1 não foi suficiente para concluir o Albedo do Asset 02, o estudante chega ao Encontro 2 sem base para o material completo. Estratégia: priorizar a conclusão do Albedo no início do Estúdio 2. O material PBR completo do Asset 02 é a entrega principal — é preferível ter um material completo em um asset do que dois assets com material incompleto.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante não consegue identificar visualmente o efeito do Normal Map | *"Desabilita o nó Bump com 'M' para ver o antes, habilita para ver o depois. Se a diferença for mínima, o Strength está baixo demais. Se parecer irreal, está alto demais. Vai ajustando o Strength com os dois estados mentalmente comparados."* |
| Node tree desorganizado, sem frames, fios cruzando | *"Para um momento. Seleciona todos os nós de Normal, pressiona Ctrl+J para criar um frame, nomeia como 'Normal'. Repete para Roughness. Agora o tree está legível. Em projeto real, você vai precisar editar esse material daqui a 2 semanas — se não entender o próprio node tree, vai refazer tudo do zero."* |
| Roughness calibrado sem lógica de material | Abrir referência no Poly Haven ou Google Imagens do mesmo material. *"Onde essa pedra [ou madeira, metal] seria mais polida na vida real? Onde acumularia mais rugosidade? O ColorRamp precisa representar isso — não só ser ruído bonito."* |
| Metallic em valor intermediário incorreto (ex: 0.3 ou 0.5) | *"Em PBR físico, Metallic é quase binário: 0 para não-metais, 1 para metais puros. Intermediários só existem em transições de material muito específicas — como borda de metal enferrujado onde a tinta está descascando. Qual é o caso do seu material? Provavelmente 0 ou 1."* |
| Estudante que terminou cedo e quer explorar mais | Propor o desafio de combinar dois Noise Textures de escalas diferentes no mesmo Bump para criar Normal Map em duas frequências (macro + micro). Ou: usar o `Texture Coordinate → UV` em vez de `Generated` para que a textura procedural respeite o UV mapeado do asset. |
| Turma geral com dificuldade no node tree (primeira experiência com nós) | Fazer pausa de 5 minutos para mostrar a anatomia de um nó no projetor: entrada (esquerda), saída (direita), parâmetros (corpo do nó). Mostrar que nós se conectam de saída para entrada — nunca ao contrário. A cor do fio indica o tipo de dado: amarelo = escalar, roxo = vetor, verde = shader. |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Asset 01 com quatro canais PBR conectados: Albedo (Image Texture), Metallic (valor), Roughness (Noise + ColorRamp), Normal (Noise + Bump) | C4 — Materiais PBR | Verificar no Shader Editor: quatro entradas do Principled BSDF conectadas. Metallic com valor físico correto (0 ou 1). Roughness com variação perceptível no viewport. Normal com fio roxo vindo do Bump. |
| Normal Map com micro-relevo visível e escala coerente com o material do kit | C5 — Texturização | Comparar o render com e sem o Bump habilitado: a diferença deve ser perceptível sem ser exagerada. A escala do relevo deve ser compatível com o material representado. |
| Variação de Roughness com lógica visual (contraste entre regiões mais polidas e mais matte) | C4 — Materiais PBR | Verificar no Viewport Rendered sob HDRI: o brilho varia dentro do mesmo material? A variação tem relação com a estrutura da superfície (ex: áreas altas mais polidas, reentrâncias mais matte)? |
| Node tree organizado em frames nomeados | C1 — Processo de Projeto | Verificar presença de frames com labels descritivos. Fios sem cruzamentos desnecessários. Distinção visual clara entre blocos de Normal, Roughness e Albedo. |
| Asset 02 com pelo menos Albedo + Normal + Roughness conectados | C4 — Materiais PBR | Mesma verificação do Asset 01. Aceitar entrega parcial se o estudante concluiu o Asset 01 com qualidade. |
| Participação na crítica: identificar calibração incorreta de Normal Map ou Roughness no trabalho de colega | C10 — Participação | Qualidade da observação — especificidade técnica (Scale errado, Strength exagerado, Roughness sem variação) em vez de comentário genérico. |
| Screenshot do node tree e render comparativo antes/depois do Normal Map | C1 — Processo de Projeto | Presença dos dois registros visuais com nomenclatura correta e sufixo `_S07`. |

---

## Entrega da Semana 7

| Entrega | Formato | Prazo |
|---|---|---|
| Asset 01 com material PBR completo (Albedo + Metallic + Roughness + Normal) | `.blend` com sufixo `_Asset01_PBR_S07` | Até o fim do segundo encontro |
| Asset 02 com material PBR completo ou avançado (mínimo: Albedo + Normal + Roughness) | `.blend` com sufixo `_Asset02_PBR_S07` | Até o fim do segundo encontro |
| Screenshot do node tree do Asset 01 (com frames visíveis) | `.png` com sufixo `_NodeTree_S07` | Até o fim do segundo encontro |
| Screenshot de render comparativo do Asset 01: antes/depois do Normal Map | `.png` com sufixos `_semNormal_S07` e `_comNormal_S07` | Até o fim do segundo encontro |

> **Nota:** A entrega do Asset 02 com todos os quatro canais é desejável mas progressiva — estudantes que chegaram ao segundo encontro concluindo o Albedo do Asset 02 podem entregar com Albedo + um canal adicional. O estado do Asset 02 será consolidado no início da Semana 8 antes da crítica formal.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 7 | 2026*
