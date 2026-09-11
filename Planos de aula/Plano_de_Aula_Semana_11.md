# Plano de Aula — Semana 11
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** III — Produção do Kit Modular: Bake e Detalhamento (Semanas 10–13)
**Tema da semana:** Bake de texturas: Normal Map, AO e Curvature
**Apostila:** Parte V, Cap. 15 — Bake de Texturas (no Blender: Normal Map e Ambient Occlusion). Leitura de apoio: Parte VI, Cap. 23 — Controle de Qualidade de Materiais
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF3** (25% do Portfolio de Artefatos)

---

## O que já foi ministrado (Semana 10 — não repetir)

Na **Semana 10**, os estudantes usaram stencils para refinar o Hero Asset (símbolos, rachaduras, corrosão) e, para quem já tinha recebido os primeiros Assets Secundários de Modelagem 3D e Level Design, começaram a estender a mesma linguagem visual a eles.

**Esta semana introduz o bake formal high-poly → low-poly**, distinto dos mesh maps gerados direto da malha na Semana 7 (que não exigiam par high/low). Agora, pela primeira vez no semestre, o estudante trabalha com dois níveis de densidade de malha do mesmo asset do Kit Modular, transferindo detalhe de um para o outro. É a terceira Crítica Formal do semestre.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar por que o bake existe: permitir que um asset de baixa contagem de polígonos (low-poly, adequado para tempo real) exiba detalhe visual equivalente a uma versão de alta densidade (high-poly), sem o custo de performance.
2. Configurar corretamente um par high-poly/low-poly no Blender para bake, incluindo cage e ray distance.
3. Executar o bake de Normal Map e Ambient Occlusion, verificando e corrigindo artefatos comuns (seams visíveis, ray distance incorreta).
4. Integrar o resultado do bake ao material já existente no 3D Coat de um asset do Kit Modular.
5. Apresentar o comparativo visual high-poly vs. low-poly com bake na terceira Crítica Formal.

---

## Critérios da Rubrica Mestre ativos nesta semana — CF3

| Critério | Peso na CF3 | Foco desta semana |
|---|---|---|
| C1 — Processo de Projeto | parte da nota | Organização do par high/low poly; documentação dos parâmetros de bake usados |
| C2 — Direção Artística | parte da nota | Continuidade da linguagem visual do kit no asset baked |
| C4 — Materiais PBR | parte da nota | Integração do resultado do bake ao material PBR já existente |
| C5 — Texturização | parte da nota | Qualidade visual do resultado final após integração do bake |
| C6 — Bake | **foco principal** | Ausência de artefatos, fidelidade de transferência de detalhe, workflow documentado |
| C9 — Apresentação | parte da nota | Clareza do comparativo visual apresentado na crítica |

> Esta é a **CF3**, com peso de 25% no Portfolio de Artefatos. Gera Ficha de Crítica Formal e Autoavaliação obrigatória.

---

## Recursos necessários

- Computadores com Blender e 3D Coat instalados
- Um asset do Kit Modular com par preparado em Modelagem 3D e Level Design (versão high-poly e low-poly do mesmo objeto)
- Arquivo de demonstração com um par high/low já configurado para bake
- Ficha de Crítica Formal e formulário de Autoavaliação
- Apostila — Parte V, Cap. 15, e Parte VI, Cap. 23 — disponibilizadas antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **O que é bake e por que usar:** transferir informação visual de uma malha de alta densidade (detalhes esculpidos ou modelados finamente) para o Normal Map de uma malha de baixa densidade, permitindo que o objeto pareça detalhado sem o custo de milhares de polígonos extras em tempo real.
2. **High-poly vs. low-poly:** o high-poly existe apenas para gerar o bake — não vai para o motor de jogo. O low-poly é o asset final, otimizado, que recebe o resultado.
3. **Foco de hoje: Normal Map e Ambient Occlusion.** (Curvature, ID Map e Thickness são apresentados na Semana 12 — não antecipar.)
4. **Cage e ray distance:** a cage é uma malha auxiliar que envolve o low-poly, definindo até onde o raio de bake procura informação do high-poly; a ray distance mal configurada gera artefatos (informação "vazando" de partes erradas do high-poly).

---

### Demonstração — 20 minutos

1. **(10 min) Setup completo de bake de Normal Map** no Blender: posicionar high-poly e low-poly, configurar cage, ajustar ray distance.
2. **(6 min) Execução do bake** e inspeção do resultado no material do low-poly.
3. **(4 min) Verificação de artefatos:** identificar visualmente uma distorção comum (seam visível ou "vazamento") e corrigir ajustando a cage.

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Executem o bake de Normal Map e AO no asset do kit que vocês receberam com par high-poly/low-poly. Integrem o resultado ao material já existente no 3D Coat."*

**Atividade estruturada:**

1. **(30 min) Setup e execução do bake** de Normal Map e AO.
2. **(20 min) Integração ao material** no 3D Coat, verificando compatibilidade visual com a linguagem já estabelecida no kit.

**Papel do professor:** verificar configuração de cage e ray distance antes da execução — evita retrabalho de bakes com artefatos grosseiros.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Formal — 20 minutos

**Formato: CF3**

1. Cada estudante apresenta o comparativo visual high-poly vs. low-poly com bake integrado.
2. Perguntas guiadas: *"Onde você ajustou a cage e por quê? Esse Normal Map transfere fielmente o detalhe do high-poly?"*
3. Ficha de Crítica Formal preenchida; Autoavaliações recolhidas.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Corrijam artefatos identificados na crítica. Finalizem a integração do bake ao material."*

**Atividade:**

1. Corrigir artefatos residuais.
2. Finalizar integração ao material PBR do asset.
3. Capturar comparação visual final high-poly vs. low-poly com bake.
4. Salvar: `[Nome]_Asset_Bake_Semana11_final.blend` + mapas exportados.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"O bake é a técnica que torna o Kit Modular viável em tempo real — sem ele, vocês precisariam escolher entre detalhe visual e performance."*
2. **(3 min)** Reflexão: *"Que artefato vocês encontraram e como resolveram?"*
3. **(2 min)** Ponte para a Semana 12: *"Na próxima semana, expandimos o bake com Curvature e ID Map, completando o pacote de mapas para um segundo asset do kit."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. Ray distance mal configurada gerando "vazamento" de detalhe**
Estratégia: reduzir a ray distance gradualmente até o artefato desaparecer, ajustando a cage se necessário.

**2. Seams visíveis no Normal Map resultante**
Estratégia: verificar se o UV do low-poly (produzido nas Semanas 4–5) tem seams em posições compatíveis com o bake — nem sempre a mesma posição de seam que funcionava para textura funciona igualmente bem para bake.

**3. High-poly e low-poly desalinhados no espaço**
Estratégia: confirmar que ambas as malhas compartilham a mesma origem e escala antes de iniciar o bake.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante sem entender por que precisa de duas versões da mesma malha | Comparar contagem de polígonos das duas versões e relacionar ao custo de performance em tempo real |
| Bake com resultado "borrado" ou sem detalhe perceptível | Verificar se o high-poly realmente tem o detalhe esculpido/modelado que se espera transferir |
| Integração ao material do 3D Coat com aparência destoante | Comparar lado a lado com o Hero Asset e ajustar intensidade do Normal Map |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Normal Map e AO baked sem artefatos graves | C6 — Bake | Inspeção visual do resultado e do workflow documentado (cage, ray distance) |
| Comparação visual high-poly vs. low-poly | C6, C9 — Bake / Apresentação | Clareza do comparativo apresentado na CF3 |
| Integração coerente ao material existente | C4, C5 — Materiais PBR / Texturização | Comparação com a linguagem visual já estabelecida no kit |

---

## Entrega da Semana 11 (CF3)

| Entrega | Formato | Prazo |
|---|---|---|
| Normal Map e AO baked de um asset do kit | PNG | Até o fim do segundo encontro |
| Material atualizado com o bake integrado | Arquivo nativo do 3D Coat / `.blend` | Até o fim do segundo encontro |
| Comparação visual high-poly vs. low-poly com bake | PNG ou JPG | Até o fim do segundo encontro |
| Autoavaliação (Instrumento 2) | Preenchida antes da crítica formal | Início do Encontro 2 |
| Ficha de Crítica Formal preenchida pelo professor | Devolução com feedback escrito | Até a Semana 12 |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 11 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
