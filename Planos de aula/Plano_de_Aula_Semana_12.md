# Plano de Aula — Semana 12
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** III — Produção do Kit Modular: Bake e Detalhamento (Semanas 10–13)
**Tema da semana:** Bake avançado: ID Map, Curvature e integração ao workflow PBR
**Apostila:** Parte V, Cap. 15 — Bake de Texturas (ID Map e Curvature Map); Parte V, Cap. 17 — Máscaras, Stencils e Decals (uso de bakes como base de mascaramento no 3D Coat)
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — circulante em estúdio e comentário coletivo ao final do segundo encontro

---

## O que já foi ministrado (Semana 11 — não repetir)

Na **Semana 11**, os estudantes executaram o bake formal de Normal Map e Ambient Occlusion em um asset do Kit Modular, configurando cage e ray distance — avaliado na **CF3**. O par high-poly/low-poly e o fluxo básico de bake já estão dominados.

**Esta semana completa o panorama de bake** com dois mapas que não foram vistos na Semana 11: ID Map e Curvature Map. Diferente da Semana 11, aqui o objetivo não é qualificação técnica isolada, mas usar esses bakes como **base de mascaramento automático** no 3D Coat — conectando bake e texturização de forma mais eficiente do que a pintura manual usada no Hero Asset.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Situar Normal, AO, Curvature, ID Map e Thickness no panorama geral de tipos de bake, entendendo a função específica de cada um.
2. Configurar um bake de ID Map atribuindo materiais coloridos distintos a diferentes partes de um asset no Blender.
3. Explicar como a Curvature Map detecta arestas convexas e côncavas, e como isso orienta automação de máscara.
4. Importar um pacote completo de bakes no 3D Coat e usar Curvature Map para gerar edge highlight e cavity dirt automáticos, reduzindo a necessidade de pintura manual de máscara.
5. Executar o bake completo (Normal, AO, Curvature, ID Map) de um segundo asset do Kit Modular.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Documentação do pacote de bake de um segundo asset; progressão do inventário do kit |
| C2 — Direção Artística | Consistência do resultado mascarado automaticamente com a linguagem visual já estabelecida |
| C6 — Bake | Ampliação do domínio técnico com ID Map e Curvature, sem gerar nova nota formal (a próxima nota de C6 é a CF4, Semana 14) |
| C7 — Otimização | Primeiro contato com a lógica de mascaramento automático como ganho de eficiência de produção — antecipa a Unidade IV |

---

## Recursos necessários

- Computadores com Blender e 3D Coat instalados
- Um segundo asset do Kit Modular com par high-poly/low-poly (ou geometria suficiente para bake de Curvature/ID direto da malha)
- Arquivo de demonstração com bake de ID Map já configurado
- Apostila — Parte V, Cap. 15 e Cap. 17 — disponibilizadas antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **Panorama dos tipos de bake:** Normal (relevo), AO (oclusão ambiente — sombra de contato), Curvature (arestas convexas/côncavas), ID Map (identifica materiais/regiões por cor), Thickness (espessura da geometria, útil para SSS). Cada um responde a uma pergunta diferente sobre a superfície.
2. **ID Map: criação e uso.** Atribuir um material colorido distinto a cada parte lógica do asset no Blender (por exemplo, metal em vermelho, madeira em verde, pedra em azul) e assar essas cores em uma textura — no 3D Coat, essa textura vira máscara de seleção rápida por região.
3. **Curvature Map: detecção de arestas e cavidades.** Áreas convexas (bordas, quinas) aparecem destacadas de um lado do espectro; áreas côncavas (frestas, sulcos), do outro — usado para automatizar exatamente a lógica de desgaste/sujeira que foi pintada manualmente no Hero Asset (Semanas 7–9).

---

### Demonstração — 20 minutos

1. **(8 min) Configuração de bake de ID Map** com materiais coloridos no Blender.
2. **(12 min) Importação do pacote de bakes no 3D Coat** e uso do Curvature Map para gerar edge highlight e cavity dirt automáticos, comparando com o tempo que a pintura manual da Semana 9 exigiu para efeito semelhante.

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Executem o bake completo (Normal, AO, Curvature, ID Map) de um segundo asset do kit. Usem os bakes de Curvature e ID para gerar máscaras automáticas no 3D Coat."*

**Atividade estruturada:**

1. **(25 min) Bake completo** dos quatro mapas no asset escolhido.
2. **(25 min) Configuração do pacote no 3D Coat**, usando máscaras geradas por bake para distribuir materiais automaticamente.

**Papel do professor:** comparar com a Semana 9: *"Veja quanto tempo você economizou usando Curvature automático em vez de pintar manualmente cada aresta."*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

Circulante em estúdio; comentário coletivo rápido, com foco em quanto do resultado foi automatizado por bake versus ajustado manualmente.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Finalizem o pacote de bake e a configuração de material no 3D Coat usando as máscaras geradas."*

**Atividade:**

1. Finalizar configuração de material com máscaras automáticas.
2. Ajustar manualmente apenas onde a automação não for suficiente.
3. Salvar: `[Nome]_Asset02_Bake_Semana12`.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"Vocês agora têm duas formas de gerar o mesmo tipo de resultado — pintura manual guiada (Hero Asset) e mascaramento automático via bake (Kit Modular). Nenhuma é superior; são ferramentas para momentos diferentes de produção."*
2. **(3 min)** Reflexão: *"Em que situação vocês ainda prefeririam pintura manual, mesmo tendo a opção automática?"*
3. **(2 min)** Ponte para a Semana 13: *"Na próxima semana, começamos a unificar múltiplos assets em um único Texture Atlas — o primeiro passo formal de otimização do kit."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. ID Map com cores muito próximas entre regiões diferentes**
Estratégia: usar cores fortemente saturadas e distintas (vermelho puro, verde puro, azul puro) para evitar ambiguidade na máscara.

**2. Curvature Map gerando ruído excessivo em superfícies com muitos detalhes pequenos**
Estratégia: ajustar a resolução do bake ou suavizar a malha high-poly antes de assar.

**3. Estudante depende só da automação e ignora ajuste artístico fino**
Estratégia: reforçar que a máscara automática é ponto de partida, não resultado final — pequenos ajustes manuais ainda diferenciam um resultado genérico de um específico ao tema.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Confusão entre Curvature e AO | Comparar lado a lado: AO reage a oclusão de luz ambiente; Curvature reage apenas à geometria (convexidade/concavidade), independente de iluminação |
| ID Map não gerando seleção limpa no 3D Coat | Verificar se as cores no Blender foram atribuídas por material (não por vértice) antes do bake |
| Estudante sem segundo asset disponível de Modelagem 3D e Level Design | Praticar o fluxo completo no Hero Asset como exercício, documentando a técnica para aplicar assim que o asset chegar |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Pacote completo de bake (4 mapas) sem artefatos graves | C6 — Bake (observado) | Inspeção visual dos mapas gerados |
| Uso de máscara por Curvature/ID para distribuir materiais | C7 — Otimização (nível inicial) | Verificação da configuração de camadas no 3D Coat |
| Resultado coerente com a linguagem visual do kit | C2 — Direção Artística | Comparação com o Hero Asset e demais assets |

---

## Entrega da Semana 12

| Entrega | Formato | Prazo |
|---|---|---|
| Pacote completo de bake (Normal, AO, Curvature, ID Map) de um asset do kit | PNG | Até o fim do segundo encontro |
| Configuração de material no 3D Coat com uso de máscara por curvature e ID | Arquivo nativo do 3D Coat | Até o fim do segundo encontro |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 12 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
