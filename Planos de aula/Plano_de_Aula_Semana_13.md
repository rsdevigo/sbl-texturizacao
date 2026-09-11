# Plano de Aula — Semana 13
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** III — Produção do Kit Modular: Bake e Detalhamento (Semanas 10–13)
**Tema da semana:** Texture Atlas: unificação de assets em uma única textura
**Apostila:** Parte V, Cap. 18 — Texture Atlas e Trim Sheets (conceito e criação de atlas; otimização de draw calls)
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — circulante em estúdio e comentário coletivo ao final do segundo encontro

---

## O que já foi ministrado (Semana 12 — não repetir)

Na **Semana 12**, os estudantes completaram o panorama de bake (Normal, AO, Curvature, ID Map) em um segundo asset do Kit Modular, usando máscaras automáticas para acelerar a distribuição de materiais no 3D Coat.

**Esta é a última semana da Unidade III e o primeiro passo formal de otimização do semestre.** Até aqui, cada asset do kit teve sua própria textura individual. A partir de hoje, múltiplos assets passam a compartilhar uma única textura (atlas), reduzindo draw calls — um conceito que só faz sentido porque, a esta altura, o estudante já tem pelo menos dois ou três assets texturizados para combinar.

**Esta semana também formaliza o inventário do kit** (asset / camada — Hero Asset Referência, Secundário ou Repetição / status), exigido no Plano de Ensino, Seção 8.1, como evidência de C1 e C7 e piso mínimo de 5 assets.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é um Texture Atlas e por que ele reduz draw calls em comparação a texturas individuais por asset.
2. Planejar um atlas identificando quais assets do kit compartilham características suficientes (escala de detalhe, resolução necessária) para dividir a mesma textura.
3. Reorganizar UV islands de múltiplos objetos em um único espaço UV, com padding adequado para evitar bleeding entre assets.
4. Validar texel density consistente entre os assets combinados no atlas.
5. Registrar o inventário do Kit Modular (asset / camada / status), atingindo o piso mínimo de 5 assets entre Hero Asset Referência, Secundários e de Repetição.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | **Inventário do kit** formalizado (asset / camada / status) — evidência central desta semana |
| C2 — Direção Artística | Coerência visual entre os assets combinados no mesmo atlas |
| C5 — Texturização | Preservação da qualidade de cada asset individual após a combinação em atlas |
| C7 — Otimização | **Foco principal:** planejamento de atlas, organização de UV islands, texel density consistente entre assets |

---

## Recursos necessários

- Computadores com Blender instalado
- Ao menos três assets do Kit Modular já texturizados (incluindo o Hero Asset Referência) — cada estudante organiza os próprios arquivos
- Template de inventário do kit (planilha ou tabela simples: asset / camada / status)
- Apostila — Parte V, Cap. 18 — disponibilizada antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **O que é Texture Atlas e por que reduz draw calls:** ao combinar as UVs de múltiplos objetos em uma única textura, o motor de jogo pode renderizá-los com uma única chamada de material, em vez de uma por asset — ganho relevante de performance em cenas com muitos objetos, como a fase caminhável da Semana 15.
2. **Planejamento de atlas:** nem todos os assets do kit precisam estar no mesmo atlas — a decisão depende de escala de detalhe (um objeto pequeno e um grande podem competir por espaço de textura de forma ineficiente) e de quais assets aparecem juntos com frequência na cena.
3. **Organização de UV islands de múltiplos objetos:** cada asset ocupa uma região distinta do mesmo espaço UV (0–1), com padding suficiente entre eles para evitar bleeding (vazamento de cor entre islands vizinhas nos mipmaps).
4. **Texel density consistente:** assim como dentro de um único asset (Semana 5), a densidade de pixel por área deve ser comparável entre os diferentes assets do atlas — senão um objeto parece nítido e outro borrado lado a lado na cena.

---

### Demonstração — 20 minutos

1. **(10 min) Criação de um Texture Atlas** combinando 3 assets de referência em um único UV 2048×2048 no Blender.
2. **(10 min) Reorganização de UV islands e validação de texel density:** mostrar como usar Average Islands Scale entre múltiplos objetos selecionados simultaneamente, seguido de Pack Islands para o conjunto.

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Planejem e comecem a executar um Texture Atlas com pelo menos 3 assets do seu kit, incluindo o Hero Asset Referência. Em paralelo, preencham o inventário do kit."*

**Atividade estruturada:**

1. **(15 min) Planejamento do atlas** — decidir quais assets combinar e por quê.
2. **(25 min) Execução:** combinar UVs no mesmo espaço, normalizar texel density, empacotar.
3. **(10 min) Preenchimento do inventário do kit** (asset / camada / status).

**Papel do professor:** verificar se o inventário já soma ao menos 5 assets projetados (mesmo que nem todos estejam finalizados) entre as três camadas do Plano de Ensino, Seção 8.1.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

Circulante em estúdio; comentário coletivo rápido sobre a validação de texel density entre os assets combinados.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Finalizem o Texture Atlas e o mapa de textura único. Fechem o inventário do kit."*

**Atividade:**

1. Finalizar UV combinado e textura única do atlas.
2. Renderizar os objetos com o atlas aplicado, verificando ausência de bleeding.
3. Finalizar o inventário do kit, garantindo o piso mínimo de 5 assets (1 Hero Asset Referência + 2–3 Secundários + 2–4 de Repetição, conforme Plano de Ensino, Seção 8.1).
4. Salvar: `[Nome]_TextureAtlas_Semana13`.

**Papel do professor:** priorizar estudantes cujo inventário ainda está abaixo do piso de 5 assets — identificar cedo é o objetivo explícito desta entrega, conforme o Plano de Ensino.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"O atlas de hoje é a primeira vez que vocês pensam no kit como um conjunto, não como peças isoladas. Essa mentalidade de otimização de conjunto continua nas próximas duas semanas."*
2. **(3 min)** Reflexão: *"Olhando o inventário, que camada do kit (Hero Asset, Secundário, Repetição) ainda está mais fraca?"*
3. **(2 min)** Ponte para a Semana 14: *"Na próxima semana é a quarta Crítica Formal — Trim Sheets, a técnica que sustenta os Assets de Repetição do kit."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. Bleeding entre islands de assets diferentes**
Estratégia: aumentar o padding entre as regiões do atlas e verificar em mipmaps reduzidos (zoom out no Viewport).

**2. Assets com escalas de detalhe muito diferentes combinados no mesmo atlas**
Estratégia: reconsiderar o agrupamento — um objeto pequeno com muito detalhe pode justificar um atlas separado dos objetos grandes e simples.

**3. Inventário do kit abaixo do piso de 5 assets nesta altura do semestre**
Estratégia: mapear com o estudante, nesta própria aula, quais Assets de Repetição (mais rápidos de produzir via Trim Sheet, Semana 14) podem completar o piso a tempo.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante sem saber quais assets combinar no atlas | Perguntar quais assets aparecem juntos com mais frequência na fase caminhável planejada |
| Texel density inconsistente entre assets do atlas | Aplicar Average Islands Scale com todos os objetos do atlas selecionados simultaneamente, não um de cada vez |
| Inventário incompleto | Usar a tabela de camadas do Plano de Ensino (Seção 8.1) como checklist direto com o estudante |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Texture Atlas com 3+ assets, UV combinado sem bleeding | C7 — Otimização | Inspeção do UV Editor e render final |
| Texel density consistente entre assets do atlas | C7 — Otimização | Comparação visual com checkerboard |
| Inventário do kit com piso mínimo de 5 assets | C1 — Processo de Projeto | Verificação da tabela de inventário |
| Coerência visual entre assets combinados | C2 — Direção Artística | Comparação visual no render final |

---

## Entrega da Semana 13

| Entrega | Formato | Prazo |
|---|---|---|
| Texture Atlas com 3+ assets do kit | UV combinado + mapa de textura único (PNG) | Até o fim do segundo encontro |
| Render dos objetos com o atlas aplicado | PNG ou JPG | Até o fim do segundo encontro |
| Inventário do kit (asset / camada / status) | Planilha ou documento | Até o fim do segundo encontro |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 13 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
