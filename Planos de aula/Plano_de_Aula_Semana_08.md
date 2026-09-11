# Plano de Aula — Semana 8
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** II — Materiais PBR e Workflow no 3D Coat (Semanas 6–9)
**Tema da semana:** Refinamento no 3D Coat e exportação PBR unificada (Albedo, Metallic, Roughness, Normal)
**Apostila:** Parte III, Cap. 10 — Construção e Análise de Materiais Reais (workflow de texturização PBR: camadas e exportação). Leitura de apoio para esta CF2: Parte VI, Cap. 23 — Controle de Qualidade de Materiais
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF2** (25% do Portfolio de Artefatos) — Apresentação estruturada com rubrica, autoavaliação obrigatória e feedback escrito do professor

---

## O que já foi ministrado (Semana 7 — não repetir)

Os estudantes chegam com:

- Hero Asset Referência no 3D Coat com material PBR iniciado: Color (base fotográfica ou estilizada da Semana 6), Roughness e Normal (via Depth) ativos, com máscaras de AO/Curvature aplicadas — Semana 7
- Trilha visual definida e consistente no Hero Asset Referência (fotorrealista ou estilizada)
- UV layout do Hero Asset Referência já otimizado e validado com checkerboard (Semana 4, revisado na Semana 5)
- Autoavaliação da Semana 8 **preenchida e entregue antes do segundo encontro** — requisito da crítica formal

> **Nota de transição:** A Semana 7 já fez a migração completa para o 3D Coat e já deu ao Hero Asset Referência profundidade real — via bake de AO/Curvature e via Normal pintado no canal Depth. Esta semana não reintroduz a ferramenta: ela aprofunda o que já está em andamento. Como existe apenas uma peça em jogo — o Hero Asset Referência — todo o tempo de estúdio desta semana se converte em profundidade de trabalho sobre ela: mais refinamento de camada (mais controle, mais intenção), exportação mais cuidada e uma exploração mais completa do Subsurface Scattering para quem tiver elementos orgânicos no kit. O foco passa a ser refinamento de camada e o fechamento técnico do semestre até aqui — exportar os **quatro** mapas PBR (Albedo, Metallic, Roughness e Normal, todos vindos do 3D Coat) e reconectá-los no Blender, substituindo de vez qualquer material provisório anterior. Isso vale igualmente para as duas trilhas: o critério de avaliação é a plausibilidade física e a comunicação visual do material, não a técnica usada para chegar lá.

> **Orientação sobre autoavaliação:** A autoavaliação deve ser distribuída digitalmente ou em papel **ao final do primeiro encontro**, para que os estudantes possam preenchê-la antes do segundo encontro. O professor deve comunicar claramente que a autoavaliação é pré-requisito de participação na crítica formal — quem chegar sem ela preenche no lugar antes de apresentar, perdendo tempo de produção.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Refinar camadas de Color, Roughness e Metallic no 3D Coat com detalhe intencional, combinando base (foto ou Smart Material), máscara de AO/Curvature e pintura manual.
2. Descrever quando o Subsurface Scattering (SSS) é fisicamente adequado e localizar o canal correspondente no sistema de camadas do 3D Coat.
3. Pintar o canal Metallic com lógica física correta (binária na maioria dos casos) e ajustar transições coerentes em materiais mistos.
4. Exportar os quatro mapas PBR do 3D Coat — Albedo, Metallic, Roughness e Normal (bakeado na Semana 7 a partir das camadas de Depth) — em resolução e formato adequados, de forma unificada para as duas trilhas visuais.
5. Configurar o material no Blender utilizando os quatro mapas exportados do 3D Coat, sem depender de nenhum nó procedural remanescente.
6. (Crítica formal) Apresentar e defender oralmente as decisões de material tomadas durante as Semanas 6–7 no Hero Asset Referência, utilizando vocabulário técnico correto e a autoavaliação como ponto de partida, justificando a trilha visual escolhida.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Qualidade da documentação entregue à crítica: organização de pasta, versões salvas, registro visual do processo das Semanas 6–7; incorporação de feedbacks anteriores visível nas iterações |
| C2 — Direção Artística | Coerência da paleta e proposta estética no Hero Asset Referência; capacidade de verbalizar as escolhas visuais durante a crítica, incluindo a justificativa da trilha (fotorrealista/estilizada) |
| C4 — Materiais PBR | Material PBR completo e unificado exportado do 3D Coat (Albedo, Metallic, Roughness, Normal), avaliado por plausibilidade física — independentemente da trilha visual |
| C5 — Texturização | Consolidação e refinamento dos mapas pintados/bakeados no 3D Coat: qualidade da cor base, coerência do Roughness, distinção visual entre áreas do material, credibilidade do Normal Map |
| C9 — Apresentação | Qualidade e organização da apresentação na crítica formal: breakdown visual, clareza da defesa oral, uso da autoavaliação |
| C10 — Participação | Qualidade das perguntas e feedbacks oferecidos durante a crítica dos colegas; postura de recepção e negociação de feedback sobre o próprio trabalho |

> **CF2 — Crítica Formal (Portfolio de Artefatos):** Esta é a segunda crítica formal do semestre (após a Semana 4). C5 (Texturização) entra formalmente na avaliação nesta CF — os mapas pintados e bakeados no 3D Coat, refinados e exportados nesta semana, são a evidência central, nas duas trilhas visuais. C9 (Apresentação) é avaliado formalmente pela primeira vez nesta CF — o estudante deve demonstrar não apenas o que produziu, mas como articula suas decisões. A nota desta CF contribui com 25% para o PA.

---

## Recursos necessários

- Computadores com 3D Coat instalado (versão 2023 ou superior recomendada)
- Computadores com Blender instalado (3.x ou 4.x) — para configurar o material final ao término do estúdio
- Arquivo `.3b`/`.3dc` do Hero Asset Referência de cada estudante, com o material iniciado na Semana 7
- Arquivo `.blend` do Hero Asset Referência de cada estudante, com UV das semanas anteriores
- Projetor para demonstração e para a crítica formal
- Fichas de Crítica Formal impressas (Instrumento 1 da Rubrica Mestre) — uma por estudante apresentado
- Fichas de Autoavaliação preenchidas pelos estudantes (Instrumento 2 da Rubrica Mestre)
- Apostila — Parte III, Cap. 10 — disponibilizada antes da aula. Parte VI, Cap. 23 (Controle de Qualidade de Materiais) recomendado como leitura de apoio para a autoavaliação desta CF2
- Pasta de exportação criada previamente no computador de demonstração do professor: `[DEMO]_3DCoat_Exportacao/`

> **Nota sobre versões do 3D Coat:** a interface passou por reorganizações entre versões — verificar a versão instalada no laboratório antes da aula e adaptar nomes de menu conforme necessário. O princípio de fluxo (refinar por canal → exportar → reconectar no Blender) é estável entre versões.

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

**Do refinamento por camada à exportação unificada: Subsurface, combinação de máscaras e o pacote de quatro mapas**

Objetivo: a turma já domina a mecânica básica do 3D Coat desde a Semana 7 — esta mini-aula não reapresenta a ferramenta, ela aprofunda duas coisas que ainda faltam: o canal Subsurface (para quem tiver elementos orgânicos no Hero Asset Referência) e a lógica de **combinar** camadas de fontes diferentes (base fotográfica/Smart Material + máscara de AO/Curvature + pintura manual de detalhe) em um resultado final coerente, fechando com o pacote completo de exportação.

**Desenvolvimento:**

Abrir com a seguinte pergunta para a turma: *"Vocês já têm Color, Roughness e Normal ativos desde a semana passada, no Hero Asset Referência. O que ainda falta para esse material estar pronto para ir para a Unity?"* Conduzir a turma a perceber que falta: (1) o Metallic, ainda não trabalhado a fundo; (2) mais uma camada de detalhe intencional sobre o que já existe; (3) a exportação de tudo isso como imagem real.

---

**Conteúdo a cobrir:**

**1. Por que os mapas do 3D Coat são portáveis e os nós do Blender não são**

Recapitulação rápida (1 min): os mapas que saem do 3D Coat são imagens reais — PNG ou TGA — que podem ser abertas em qualquer software e conectadas em qualquer motor, diferente de um material feito só de nós dentro do Blender. É por isso que o pipeline da disciplina fecha com essa exportação: Blender (modelagem + UV) → **3D Coat (texturização)** → Unity (motor).

**2. Subsurface Scattering (SSS) como canal do 3D Coat**

O Subsurface Scattering simula materiais que permitem que a luz penetre levemente antes de ser dispersa internamente — como pele, cera, mármore, folhas e tecidos finos. O resultado visual é uma suavidade característica nas transições de luz/sombra e um leve "brilho interno" nas bordas. No 3D Coat, assim como no Principled BSDF do Blender, o canal Subsurface aceita valores de 0 (sem efeito) a 1 (máximo). Se o Hero Asset Referência do estudante tiver algum elemento orgânico ou translúcido — flores, folhas, tecido, cera, cristal —, hoje é o momento de localizar esse canal na interface e testar valores baixos (0.05–0.15 costuma ser suficiente para o efeito ser perceptível sem "derreter" a leitura de material sólido). Para a maioria dos Hero Assets do kit (pedra, metal, madeira, concreto), o SSS não se aplica — e não pintar nada nesse canal é a decisão fisicamente correta, não uma omissão.

**3. Combinando fontes numa mesma camada de material**

O material do Hero Asset Referência de cada estudante, a esta altura, já tem no mínimo três origens de informação empilhadas: a base (foto ou Smart Material), a máscara gerada da geometria (AO/Curvature) e a pintura manual (Depth, variações de cor). O refinamento desta semana consiste em ajustar o peso relativo dessas três camadas — nenhuma delas sozinha deveria contar toda a história do material. *"Se alguém desligar só a camada de máscara de vocês, o material ainda deveria parecer razoável — só mais 'novo', menos usado. Se desligar e o material sumir ou virar outra coisa, a camada de máscara está fazendo trabalho demais sozinha."* Como esta semana concentra todo o tempo de refinamento em uma única peça, vale a pena ir além do mínimo: testar uma segunda camada de detalhe focal, revisar a intensidade de cada camada isoladamente no Render Room, e comparar o resultado com referências reais do material antes de considerar o Color pronto para exportação.

**4. O pacote de exportação: quatro mapas, uma vez só**

1. **Refinar** as camadas de Color, Roughness e Metallic com detalhe adicional.
2. **Exportar** os quatro mapas: Albedo (Color), Roughness, Metallic e Normal — este último já bakeado a partir do Depth pintado na Semana 7, exportado junto com os demais pela primeira vez.
3. **Conectar** os quatro mapas no material do Blender, com o Color Space correto em cada nó.

> **Nota do professor:** Manter o ritmo desta mini-aula curto — o conteúdo novo real é o SSS e a lógica de combinação de camadas; o resto é consolidação. Priorizar tempo de demonstração e estúdio.

---

### Demonstração — 20 minutos

**Refinamento de camadas, Metallic, e exportação dos quatro mapas PBR**

**Setup (1 min):**
Abrir o 3D Coat com o arquivo de demonstração da Semana 7 (asset já com Color, Roughness e Normal iniciados). Ter o Blender aberto em outra janela.

**Percurso da demonstração:**

**Passo 1 — Refinamento da camada de Color (4 min):**
1. Adicionar uma camada de detalhe focal: `Detalhe_Cor`, modo Multiply ou Overlay, opacidade 20–30%.
2. Pintar detalhes específicos do tema sobre a base já existente — sombras de fissuras, manchas de umidade, concentração de cor em áreas de desgaste, reforçando (não substituindo) o que a máscara de AO/Curvature já indicava.
3. Avaliar no Render Room: a cor tem história? Parece que o objeto foi usado?

**Passo 2 — Canal Metallic (4 min):**
1. Canal ativo: **Metallic**.
2. Para o asset de demonstração (pedra): Fill com preto puro (Metallic = 0). Explicar: *"Pedra, madeira e concreto ficam em preto — sem exceção, sem meio-termo."*
3. Rapidamente, mostrar em um segundo arquivo de referência preparado (caixa metálica): Fill com branco puro (Metallic = 1), com preto pintado nas áreas de ferrugem/tinta exposta usando a mesma lógica de máscara por Curvature — apenas para ilustrar o caso metálico, sem que os estudantes precisem replicar esse segundo arquivo.
4. *"Note que a transição de metal para ferrugem não é um gradiente suave de Metallic — é uma borda nítida, porque fisicamente ou é metal exposto ou não é."*

**Passo 3 — Revisão final do Roughness com a máscara combinada (3 min):**
1. Mostrar as camadas empilhadas no painel Layers: base + desgaste (Curvature) + sujeira (AO).
2. No Render Room: alternar ligando/desligando cada camada para mostrar a contribuição individual de cada uma.

**Passo 4 — Exportação dos quatro mapas (5 min):**
1. `File → Export Textures` (ou exportação individual por canal, dependendo da versão).
2. Selecionar: Albedo (Color), Roughness, Metallic **e Normal**.
3. Formato: **PNG**, resolução: **1024×1024** (mesma da importação).
4. Destinar para a pasta `[DEMO]_3DCoat_Exportacao/`. Confirmar exportação.
5. Abrir a pasta no explorador: mostrar os quatro arquivos PNG gerados — `HeroAsset_Albedo.png`, `HeroAsset_Roughness.png`, `HeroAsset_Metallic.png`, `HeroAsset_Normal.png`.

**Passo 5 — Conexão no Blender (3 min):**
1. Mudar para o Blender.
2. No Shader Editor, criar um material novo e limpo (sem nós procedurais remanescentes): `[Nome]_HeroAsset_3DCoat_Final`.
3. Adicionar quatro nós `Image Texture`:
   - `HeroAsset_Albedo.png` → `Base Color` (Color Space: **sRGB**, padrão)
   - `HeroAsset_Roughness.png` → `Roughness` (Color Space: **Non-Color**)
   - `HeroAsset_Metallic.png` → `Metallic` (Color Space: **Non-Color**)
   - `HeroAsset_Normal.png` → através de um nó `Normal Map` (`Shift+A → Vector → Normal Map`) → entrada `Normal` do Principled BSDF (Color Space do Image Texture: **Non-Color**)
4. Mostrar o viewport Rendered: *"Os quatro canais agora vêm de imagens reais, exportadas do 3D Coat. Esse material está pronto para ir para a Unity exatamente como está aqui."*

> **Nota do professor:** O nó `Normal Map` entre o Image Texture do Normal e o Principled BSDF é obrigatório — conectar a saída Color do Image Texture diretamente ao Normal do Principled produz resultado incorreto. Reforçar isso explicitamente, é um erro recorrente.

---

### Produção em Estúdio — 50 minutos

**Refinamento do Hero Asset Referência, canal Metallic e primeira exportação de teste**

**Consigna entregue verbalmente:**

> *"O objetivo deste estúdio é ter o Hero Asset Referência com os quatro canais refinados — Color com uma camada de detalhe adicional, Roughness revisado, Metallic corretamente preenchido — e uma primeira exportação de teste dos quatro mapas. Não precisa ser a versão final: o segundo encontro tem mais 60 minutos de estúdio, incluindo a reconexão completa no Blender. Antes de sair daqui, quero ver o Metallic preenchido com lógica física e pelo menos uma exportação de teste na pasta do projeto. Quem terminar tudo isso com sobra de tempo: aprofunda — uma segunda camada de detalhe, um teste de SSS se fizer sentido para o material, ou uma comparação mais cuidadosa com as referências do moodboard."*

**Atividade estruturada:**

**Etapa 1 — Refinamento do Color (≈15 min):**
1. Abrir o arquivo `.3b`/`.3dc` do Hero Asset Referência da Semana 7.
2. Adicionar camada de detalhe focal sobre a base já existente, reforçando a leitura de uso/desgaste com pincel de opacidade baixa.
3. Revisar no Render Room: a variação de cor conta uma história, sem apagar a base?
4. Se houver tempo: testar uma segunda camada de detalhe em outra área do asset, comparando o peso relativo das duas camadas.

**Etapa 2 — Canal Metallic (≈15 min):**
1. Canal ativo: **Metallic**.
2. Para materiais não-metálicos (pedra, madeira, concreto): Fill com preto puro. Não pintar nada adicional.
3. Para materiais metálicos (ferro, aço): Fill com branco puro. Pintar com preto as áreas de ferrugem ou tinta onde o metal ficaria exposto, usando a máscara de Curvature como guia de onde o desgaste concentraria essa exposição.
4. Para materiais mistos: preencher as zonas corretas sem gradientes suaves — Metallic em PBR é quase binário.
5. Para quem tiver elemento orgânico/translúcido no Hero Asset Referência: localizar o canal Subsurface e testar um valor baixo (0.05–0.15), avaliando o resultado no Render Room antes de decidir se mantém.

**Etapa 3 — Revisão do Roughness (≈10 min):**
1. Conferir se as camadas de base + desgaste + sujeira (Semana 7) ainda produzem contraste perceptível.
2. Ajustar opacidade se necessário.

**Etapa 4 — Exportação de teste (≈5 min):**
1. `File → Export Textures`.
2. Selecionar Albedo, Roughness, Metallic e Normal.
3. Formato PNG, 1024×1024.
4. Pasta: `[Nome]_HeroAsset_Mapas_S08/`.
5. Verificar no explorador de arquivos que os quatro PNGs foram gerados com tamanho esperado.

**Etapa 5 — Salvar e documentar (≈5 min):**
1. Salvar o arquivo do 3D Coat: `[Nome]_HeroAsset_S08.3b`.
2. Tirar screenshot do painel de Layers com todas as camadas visíveis.
3. Tirar screenshot do Render Room mostrando o resultado combinado.

**Papel do professor:**

Circular verificando três pontos em cada estação:

- **O Metallic está correto para o material?** Para kits Medieval, Fantasia ou pós-apocalíptico, a maioria dos Hero Assets de pedra e madeira deve ter Metallic = 0. Estudantes que colocam Metallic em valores intermediários em pedra ou madeira devem ser orientados.
- **A camada de detalhe do Color está reforçando ou competindo com a máscara de AO/Curvature já existente?** Se as duas contarem histórias diferentes (uma diz "desgastado aqui", a outra diz "desgastado ali"), o material perde coerência.
- **Os quatro mapas foram exportados de fato?** Confirmar no explorador de arquivos, não só na confirmação do 3D Coat — exportações vazias por erro de seleção de canal acontecem.

Perguntas de mediação circulante:

- *"Esse Fill do Metallic está em que valor? Mostra o painel — preto puro ou branco puro, sem meio-termo, a menos que você tenha uma razão física específica para uma transição."*
- *"Você exportou os quatro mapas ou só três? Confere na pasta — o Normal também precisa estar lá esta semana."*
- *"A camada de detalhe que você acabou de pintar concorda com a máscara de Curvature de baixo? Ou está competindo com ela?"*
- *"Você já terminou o mínimo — quer aproveitar o tempo restante para testar uma segunda camada de detalhe ou revisar o Roughness com mais cuidado, já que é só uma peça este semestre?"*

> **Orientação ao final do Estúdio 1:** Comunicar que a autoavaliação deve ser preenchida antes do segundo encontro. Distribuir o Instrumento 2 (Autoavaliação) neste momento se ainda não foi distribuído. Lembrar que a crítica formal começa o segundo encontro — quem chegar sem autoavaliação perde tempo de estúdio para preenchê-la.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva FORMAL — 20 minutos

**Formato: Crítica formal com rubrica, autoavaliação e feedback escrito do professor**

Esta é a segunda crítica formal do semestre (após a Semana 4). O objeto da crítica é o trabalho das Semanas 6–7 no Hero Asset Referência: a textura seamless de origem, a trilha visual escolhida, e o material construído no 3D Coat com máscaras de AO/Curvature e Normal via Depth. O refinamento feito no início deste encontro (Estúdio 1) pode ser incluído como contexto, mas o foco avaliativo é o estado consolidado do material.

**Protocolo:**

**Preparação (antes do início — 2 min antes):**
- Professor confere se todos têm a autoavaliação preenchida. Quem não tem: preenche agora, em 5 minutos, antes de qualquer outra atividade.
- Fichas de Crítica Formal (Instrumento 1) separadas por estudante.
- Projetor ligado e pronto para receber o arquivo do estudante (3D Coat ou Blender, conforme o que o estudante preferir apresentar).

**Abertura (2 min):**
Professor define o contexto e os critérios em foco:
*"Esta é a crítica formal da Unidade II. Vocês vão apresentar o material que construíram no 3D Coat, no Hero Asset Referência, nas últimas duas semanas. Quero ouvir de cada um: qual é a trilha visual do seu kit — fotorrealista ou estilizada —, quais canais estão ativos, e uma escolha que vocês fizeram — de máscara, de Roughness, de Normal — e por que fizeram essa escolha. Depois a turma comenta. Cada apresentação tem dois minutos."*

Os critérios observados hoje: C1 (processo e documentação), C2 (coerência artística), C4 (materiais PBR), C5 (texturização), C9 (apresentação oral).

**Rodada de apresentações (15 min — ≈3–4 estudantes, 2 min cada + 1–2 min de feedback):**

Para cada apresentação:

1. **O estudante apresenta** (2 min):
   - Projeta o Hero Asset Referência com o material no Render Room do 3D Coat ou no viewport Rendered do Blender.
   - Descreve: o material, a trilha visual, os canais ativos, e uma decisão técnica ou artística que tomou.
   - Lê a própria autoavaliação: o critério em que se avaliou mais alto e o critério em que se avaliou mais baixo, com justificativa.

2. **Feedback da turma** (1 min):
   - Uma pergunta ou observação específica de qualquer colega.
   - O professor pode complementar ou direcionar: *"Alguém vê algo no Roughness ou na máscara de desgaste que poderia ser diferente?"*

3. **Feedback escrito do professor** (preenchido durante a apresentação na ficha):
   - C4 — O material tem plausibilidade física? Os valores dos canais fazem sentido para o material representado, independentemente da trilha?
   - C5 — Há variação visual real, não apenas uma base colada? O Normal adiciona credibilidade?
   - C9 — A apresentação foi clara e estruturada? O estudante conseguiu justificar as decisões, inclusive a escolha de trilha?
   - Ponto forte + prioridade de melhoria.

> **Nota sobre o tempo:** Com turmas grandes (mais de 12 estudantes), não é possível apresentar todos na crítica formal de 20 minutos. Neste caso: sortear 3–4 estudantes para apresentar formalmente e usar a avaliação das Fichas de Crítica como registro para todos os demais. Alternativa: semanas com crítica formal podem ter a crítica expandida para 30 min retirando 10 min do estúdio 2.

**Fechamento da crítica (2 min):**
Sintetizar os padrões observados:
- Qual o critério em que a turma está mais forte? (tipicamente C4 — os materiais PBR estão funcionalmente corretos nas duas trilhas)
- Qual o critério com maior gap entre autoavaliação e avaliação do professor? (tipicamente C9 — estudantes subavaliam a própria capacidade de apresentação, ou C2 — autoavaliam acima no artístico)
- Uma orientação para o estúdio: *"O que ficou mais claro na crítica é [X]. Levem isso para o refinamento final agora — o que vocês vão exportar deve responder a esse ponto."*

---

### Produção em Estúdio — 60 minutos

**Refinamento final, exportação unificada dos quatro mapas e configuração no Blender**

**Consigna:**

> *"Sessenta minutos para três objetivos, todos no Hero Asset Referência: (1) refinamento final das camadas no 3D Coat, incorporando o que saiu na crítica; (2) exportação final dos quatro mapas PBR — Albedo, Metallic, Roughness e Normal; (3) reconexão completa no Blender, sem nenhum nó procedural remanescente. Como é uma peça só este semestre, quem terminar os três blocos com tempo de sobra usa o restante para aprofundar: mais uma camada de detalhe, um teste comparativo de Roughness, ou revisão fina do Normal — não para começar outra coisa."*

**Atividade estruturada:**

**Bloco 1 — Refinamento final das camadas no 3D Coat (≈20 min):**

Incorporar o feedback recebido na crítica formal. Focos típicos:
1. Reforçar ou reduzir a intensidade da máscara de AO/Curvature conforme apontado.
2. Adicionar uma camada de sujeira/acúmulo se ainda não existir: `Roughness_Sujeira`, pintada em áreas côncavas com valor mais alto (mais rugoso), modo Multiply, opacidade 40–50%.
3. Revisar o Metallic nas transições, se aplicável.
4. Revisar o Normal/Depth se a crítica apontou relevo fraco ou exagerado.
5. Se sobrar tempo dentro do bloco: revisar o canal Subsurface (quando aplicável) e comparar o resultado com as referências do moodboard uma última vez.

**Bloco 2 — Exportação final dos quatro mapas PBR (≈10 min):**
1. `File → Export Textures`.
2. Mapas a exportar: **Albedo**, **Roughness**, **Metallic** e **Normal**.
3. Formato: PNG.
4. Resolução: mesma da importação (1024×1024).
5. Pasta de destino: `[Nome]_HeroAsset_Mapas_S08/`.
6. Confirmar exportação. Verificar no explorador de arquivos que os quatro PNGs foram gerados com tamanho esperado.

**Bloco 3 — Configuração final do material no Blender (≈25 min):**
1. Abrir o `.blend` do Hero Asset Referência.
2. Criar um material novo e limpo: `[Nome]_HeroAsset_3DCoat_Final`.
3. Adicionar quatro nós `Image Texture`:
   - `HeroAsset_Albedo.png` → `Base Color` (sRGB)
   - `HeroAsset_Roughness.png` → `Roughness` (Non-Color)
   - `HeroAsset_Metallic.png` → `Metallic` (Non-Color)
   - `HeroAsset_Normal.png` → nó `Normal Map` → `Normal` do Principled BSDF (Image Texture em Non-Color)
4. No Viewport Rendered: conferir o resultado final. Comparar com o estado do material no fechamento da Semana 7, se ainda houver um material anterior salvo, para ver a evolução.
5. Salvar: `[Nome]_HeroAsset_3DCoat_S08.blend`.
6. Capturar screenshot do material final e do node tree simplificado (quatro Image Texture + Normal Map + Principled BSDF, sem mais nada).

**Bloco 4 — Aprofundamento (se houver tempo — ≈5 min):**
Para estudantes que terminaram o fluxo completo dos três blocos:
1. Revisar comparativamente o Roughness em zonas de alto e baixo desgaste, ajustando contraste se a diferença ainda for sutil demais no Render Room.
2. Ou: testar um valor alternativo de Subsurface (quando aplicável) e decidir qual versão comunica melhor o material, documentando a escolha para citar na próxima crítica.
3. Reexportar apenas os mapas alterados e reconferir a conexão no Blender.

**Papel do professor:**

- Para estudantes com mapa de Roughness muito uniforme: *"Abre o Render Room. Onde tem diferença de brilho na superfície? Se não tem diferença visível, volta para o Paint Room e intensifica o contraste entre as camadas de Roughness."*
- Para estudantes com Color Space errado no Blender: *"O material parece excessivamente reflexivo ou matte demais, ou o relevo do Normal está invertido/estranho? Verifica o Color Space de cada nó Image Texture — só o Albedo fica em sRGB, todos os outros (Roughness, Metallic, Normal) em Non-Color."*
- Para estudantes que esqueceram o nó Normal Map: *"O Normal está conectado direto do Image Texture ao Principled BSDF, ou passa pelo nó Normal Map antes? Sem esse nó intermediário, o relevo sai incorreto."*
- Para estudantes avançados que já terminaram os três blocos: *"Compara o material de agora com o que você tinha no fechamento da Semana 6, só com a textura no Albedo. O que as camadas de máscara, o Metallic e o Normal adicionaram que a textura sozinha não tinha? Onde ainda dá para intensificar isso sem exagerar?"*

---

### Fechamento — 10 minutos

**Roteiro:**

1. **(2 min — Síntese da semana)**
*"Hoje vocês fecharam a Unidade II: um material PBR completo, com quatro mapas reais exportados do 3D Coat, funcionando igualmente bem seja a trilha fotorrealista ou estilizada. Esse fluxo — refinar por camada, exportar, reconectar — é a base de tudo que vem pela frente: desgaste mais elaborado, stencils, bake de assets do kit inteiro."*

2. **(3 min — Reflexão comparativa)**
Pergunta para 2–3 voluntários: *"Compara o material que vocês tinham no final da Semana 6 — só uma textura no Albedo — com o material de agora, com os quatro mapas do 3D Coat. O que mudou? O que a máscara de AO/Curvature e o Normal pintado adicionaram que a textura sozinha não tinha?"*

3. **(3 min — Antecipação da Semana 9)**
*"Na semana que vem: texturização artística no Hero Asset Referência — desgaste, sujeira e variação de cor pintados com ainda mais intenção, para além do que a máscara automática já faz. Vocês vão aprender edge wear, dirt e a lógica de leitura de silhueta. Antes de chegar na Semana 9, olhem o moodboard de vocês — o tema do kit pede um material envelhecido? Destruído? Novo? Essa decisão vai guiar onde vocês pintam o desgaste, nas duas trilhas."*

4. **(2 min — Confirmação das entregas)**
Recapitular as entregas com nomenclatura esperada.

---

## Possíveis Dificuldades

**1. Mapa de Roughness exportado uniforme (sem variação visível)**
Se as camadas de variação foram pintadas com opacidade muito baixa ou com o modo de mistura errado, o mapa exportado pode ser praticamente um Fill uniforme. Estratégia: antes de exportar, abrir o mapa no Render Room e ampliar a vista de Roughness isolado para verificar se há gradação. Se não houver, aumentar a opacidade das camadas de variação ou reforçar a intensidade da pintura antes de exportar.

**2. Color Space incorreto no Blender ao conectar os mapas**
Mapas de Roughness, Metallic e Normal conectados com Color Space em "sRGB" (padrão) em vez de "Non-Color" produzem valores incorretos — o material fica excessivamente reflexivo ou completamente matte sem controle, e o Normal pode ficar com relevo errado. Estratégia: lembrar a regra: somente o mapa Albedo fica em sRGB. Todos os outros mapas de dados devem ter Color Space em **Non-Color**.

**3. Normal Map conectado sem o nó intermediário**
Conectar o Image Texture do Normal diretamente à entrada Normal do Principled BSDF, sem passar pelo nó `Normal Map`, produz um resultado fisicamente incorreto (o motor interpreta a imagem como cor, não como vetor). Estratégia: verificar visualmente a presença do nó `Normal Map` entre os dois — é um erro silencioso, o material roda sem erro mas com aparência errada, então vale conferir ativamente em cada estação.

**4. 3D Coat lento ou travando no laboratório**
Sintomas: viewport lento ao rodar o asset, pintura com delay, travamento ao trocar de canal. Estratégia: usar resolução 512×512 em vez de 1024 nos computadores mais lentos — o fluxo é idêntico, apenas com menos detalhe. Orientar o estudante a trabalhar em 512 em aula e re-importar em 1024 em casa ou em computador mais potente para a entrega final.

**5. Estudante não traz autoavaliação para a crítica formal**
Sem a autoavaliação preenchida, a crítica formal perde a dimensão de metacognição que é central no SBL. Estratégia: reservar 5 minutos no início do Encontro 2 para preenchimento emergencial. Criar o hábito de comunicar a importância da autoavaliação no fechamento do Encontro 1 — e repetir no início do segundo encontro.

**6. Trilha estilizada avaliada com régua de fotorrealismo (ou vice-versa)**
Ao circular ou ao preencher a Ficha de Crítica, existe o risco de o professor (ou um colega, na crítica) cobrar de um material estilizado o mesmo grau de detalhe fotográfico de um material realista, ou cobrar de um material fotorrealista uma "personalidade" pictórica que não é o objetivo daquela trilha. Estratégia: ancorar toda avaliação de C4/C5 na pergunta "esse material é fisicamente plausível e comunica bem o que pretende ser dentro do próprio universo visual escolhido?" — nunca em "isso parece uma foto?" para quem optou por estilizado, nem em "isso parece uma pintura?" para quem optou por fotorrealismo.

**7. Estudante termina cedo e não sabe o que fazer com o tempo restante**
Como há apenas um asset em jogo este semestre, alguns estudantes podem terminar os blocos mínimos rapidamente e ficar ociosos. Estratégia: ter sempre pronta uma lista curta de aprofundamentos válidos (segunda camada de detalhe, teste de SSS, comparação de Roughness em zonas específicas, revisão fina do Normal) para direcionar esse tempo, evitando tanto a ociosidade quanto o risco de o estudante começar a mexer em algo fora do escopo da semana.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante com material muito parecido com o final da Semana 6 (sem ganho visível na Semana 7–8) | *"Compara o antes e o depois no Render Room. Se o material parece igual à textura sozinha, as camadas de máscara e o Normal não adicionaram informação nova. Volta e reforça a camada de desgaste ou o Depth com algo que a textura de base não tinha."* |
| Estudante nervoso ou travado na crítica formal | Redirecionar para a autoavaliação: *"O que você escreveu na sua autoavaliação como ponto forte? Começa mostrando isso."* O documento é um apoio — quem preencheu com honestidade tem um roteiro de apresentação pronto. |
| Estudante com dificuldade de justificar decisões na crítica | *"Não precisa ter sido a decisão certa — precisa ter sido uma decisão consciente. Por que você escolheu essa trilha, esse tom de roughness, essa intensidade de desgaste? Você olhou referências? Isso é suficiente para justificar."* Reforçar que justificar ≠ acertar. |
| Turma geral com dificuldade de organizar a exportação em lote dos quatro mapas | Fazer uma pausa de 5 minutos para revisar juntos, no projetor, a janela de exportação do 3D Coat, conferindo explicitamente a checklist dos quatro canais marcados antes de confirmar. |
| Estudante que terminou cedo e quer ir além | Propor: *"Tenta pintar uma camada adicional de Depth com brush de tamanho pequeno e opacidade alta, simulando desgaste concentrado em um ponto específico do asset — um canto que seria mais batido no universo do kit. Refaz a exportação e compara o Normal Map novo com o antigo."* |
| Diferença de ritmo entre trilha fotorrealista e estilizada no mesmo estúdio | Como as duas trilhas usam o mesmo fluxo de ferramenta, a circulação do professor não precisa se dividir por grupo — as perguntas de mediação são as mesmas, só a referência visual muda (foto de material real vs. moodboard/concept art). |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Hero Asset Referência no 3D Coat com Color refinado (base + máscara + camada de detalhe) | C5 — Texturização | Verificar no painel de Layers/Render Room: há pelo menos três camadas contribuindo para o Color, com variação visível |
| Canal Roughness com contraste perceptível entre regiões (base, arestas, cavidades) no mapa exportado | C4 — Materiais PBR | Abrir o PNG exportado do Roughness: há gradação de tons entre arestas e reentrâncias? |
| Canal Metallic preenchido corretamente para o tipo de material (0 para dielétricos, 1 para metais, transições nítidas quando mistos) | C4 — Materiais PBR | Verificar no mapa exportado: o preenchimento é coerente com as propriedades físicas do material? |
| Quatro mapas PBR exportados do 3D Coat (Albedo, Roughness, Metallic, Normal) | C4 — Materiais PBR | Conferir a pasta de exportação: quatro arquivos PNG presentes, com conteúdo (não uniformes/vazios) |
| Material no Blender configurado com os quatro mapas conectados nos slots corretos (Color Space e nó Normal Map corretos) | C4 — Materiais PBR | Verificar o Shader Editor: Albedo em sRGB; Roughness, Metallic e Normal (Image Texture) em Non-Color; nó Normal Map presente entre o Image Texture do Normal e o Principled BSDF |
| Apresentação oral na crítica formal: descrição do material, trilha visual, canais ativos, e justificativa de ao menos uma decisão técnica ou artística | C9 — Apresentação | Qualidade da justificativa oral: é específica e técnica ("escolhi roughness 0.7 para pedra porque...") ou vaga ("ficou bom")? |
| Autoavaliação preenchida com evidência concreta para cada critério avaliado | C1 — Processo de Projeto | Verificar se a autoavaliação cita evidências observáveis no trabalho (ex: "tenho quatro mapas exportados e conectados" — não apenas "acho que está bom") |
| Participação na crítica dos colegas: ao menos uma observação específica e construtiva sobre o trabalho apresentado | C10 — Participação | Qualidade do feedback: é observável ("o roughness parece muito uniforme, sem variação de desgaste") ou genérico ("ficou bonito")? |
| Screenshot do painel de Layers com camadas visíveis e screenshot do Render Room mostrando o material com os canais combinados | C1 — Processo de Projeto | Presença dos dois registros com nomenclatura `_S08` e identificação do asset. |

---

## Entrega da Semana 8

| Entrega | Formato | Prazo |
|---|---|---|
| Arquivo do 3D Coat com o Hero Asset Referência refinado (Color, Roughness, Metallic, Normal) | `.3b`/`.3dc` com sufixo `_HeroAsset_3DCoat_S08` | Até o fim do segundo encontro |
| Mapas PBR exportados do 3D Coat: Albedo, Roughness, Metallic **e Normal** | `.png` 1024×1024 (ou 2048) com sufixos `_Albedo`, `_Roughness`, `_Metallic`, `_Normal` na pasta `_Mapas_S08` | Até o fim do segundo encontro |
| Arquivo Blender com material final configurado usando os quatro mapas do 3D Coat, sem nós procedurais remanescentes | `.blend` com sufixo `_HeroAsset_3DCoat_S08` | Até o fim do segundo encontro |
| Autoavaliação preenchida com evidências | Instrumento 2 da Rubrica Mestre (físico ou digital) | Até o início do segundo encontro |
| Screenshot do painel de Layers (camadas visíveis) e do Render Room | `.png` com sufixos `_Layers_S08` e `_RenderRoom_S08` | Até o fim do segundo encontro |

> **Nota:** Como o modelo pedagógico da disciplina trabalha uma única peça — o Hero Asset Referência — até a Semana 9, não há entrega paralela de um segundo asset nesta semana. A Semana 9 continua sobre o mesmo Hero Asset Referência, aprofundando a texturização artística por pintura digital (desgaste, sujeira, variação de cor).

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 8 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
