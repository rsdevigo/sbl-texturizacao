# Plano de Aula — Semana 9
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** II — Materiais PBR e Workflow no 3D Coat (Semanas 6–9)
**Tema da semana:** Texturização artística por pintura digital no 3D Coat
**Apostila:** Parte IV, Cap. 14 — Pintura Digital para Jogos (aplicada a texturas; ferramentas de pintura no 3D Coat)
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — circulante em estúdio e comentário coletivo ao final do segundo encontro

---

## O que já foi ministrado (Semana 8 — não repetir)

Na **Semana 8**, os estudantes refinaram Color e Metallic combinando base, máscara e pintura manual, exportaram os quatro mapas PBR e reconfiguraram o material no Blender — avaliado na **CF2**, encerrando o ciclo básico de texturização PBR do Hero Asset.

**Esta é a última semana da Unidade II e do trabalho dedicado ao Hero Asset antes do Kit Modular começar (Semana 10).** O foco agora é aprofundar a camada artística que a CF2 já começou a avaliar (C5), sem alterar a base PBR já aprovada. **Esta é a semana da SCT (Semana de Ciência e Tecnologia)** — o ritmo de estúdio pode precisar de ajuste conforme a agenda do evento institucional.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Diferenciar texturização fotorrealista de estilizada na aplicação prática de desgaste e sujeira, mantendo a trilha escolhida desde a Semana 6.
2. Pintar desgaste de borda (edge wear), sujeira acumulada (dirt) e riscos (scratches) usando pincéis e alphas apropriados no 3D Coat.
3. Organizar camadas de pintura por tipo de detalhe (base, desgaste, sujeira, riscos), mantendo o material editável e não destrutivo.
4. Avaliar o resultado tanto em close-up quanto à distância de uso, priorizando legibilidade de silhueta e material sobre detalhe microscópico isolado.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Organização de camadas por tipo de detalhe; registro de decisões de desgaste |
| C2 — Direção Artística | Consistência do desgaste com a narrativa do tema (um artefato ritual desgasta diferente de uma peça industrial) |
| C5 — Texturização | **Foco principal:** profundidade de detalhe além do que foi avaliado na CF2 — a próxima nota de C5 é a CF3 (Semana 11) |

---

## Recursos necessários

- Computadores com 3D Coat instalado
- Hero Asset texturizado da Semana 8 (pós-CF2)
- Alphas de desgaste, sujeira e riscos (biblioteca padrão do 3D Coat ou pacote customizado)
- Referências visuais de objetos reais com desgaste similar ao material do Hero Asset
- Apostila — Parte IV, Cap. 14 — disponibilizada antes da aula
- **Atenção à agenda da SCT nesta semana** — confirmar com antecedência se o horário de aula sofre alguma alteração institucional

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **Fotorrealista vs. estilizado na prática do desgaste:** a trilha fotorrealista busca reproduzir com fidelidade como a luz e o desgaste se comportam em referências reais; a trilha estilizada exagera ou simplifica esses padrões para reforçar leitura e intenção artística — mas ambas seguem a mesma lógica de onde o desgaste acontece (contato, fricção, exposição).
2. **Organização de camadas por tipo de detalhe:** separar em camadas distintas base, edge wear, dirt e scratches permite ajustar a intensidade de cada um independentemente, sem repintar do zero.
3. **Técnicas de edge wear, dirt e scratches:** pincéis com alphas específicos para cada efeito; uso de máscara de Curvature (já gerada na Semana 7) para guiar onde o desgaste de borda se concentra automaticamente.

---

### Demonstração — 20 minutos

1. **(10 min) Pintura de desgaste em um material metálico de referência:** aplicar edge wear guiado por Curvature, ajustando opacidade da camada.
2. **(10 min) Variação de cor e sujeira:** adicionar sutil variação de tom na base e sujeira acumulada em reentrâncias usando a máscara de AO já existente.

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Adicionem desgaste, sujeira e variação de cor ao Hero Asset, em camadas separadas por tipo de detalhe. Testem a leitura tanto de perto quanto à distância simulada de uso no jogo."*

**Atividade estruturada:**

1. **(30 min) Pintura de detalhe** em camadas separadas (edge wear, dirt, scratches).
2. **(20 min) Teste de leitura à distância** — afastar a câmera no viewport do 3D Coat e verificar se o detalhe ainda comunica a narrativa pretendida.

**Papel do professor:** perguntar *"Esse desgaste conta uma história de uso, ou está espalhado aleatoriamente?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

Circulante em estúdio; comentário coletivo rápido ao final, com foco em leitura de silhueta e legibilidade do material à distância.

> **Nota do professor:** ajustar a duração desta crítica conforme a agenda da SCT, se necessário — o essencial é garantir que cada estudante receba pelo menos um comentário direcionado antes do fim da semana.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Finalizem as camadas de detalhe. Exportem os mapas atualizados e capturem o render comparativo antes/depois."*

**Atividade:**

1. Finalizar pintura de detalhe.
2. Exportar mapas atualizados (Albedo/Color com o novo detalhamento).
3. Capturar render comparativo antes (Semana 8) / depois (Semana 9).
4. Salvar: `[Nome]_HeroAsset_Semana09`.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"O Hero Asset agora está no nível de acabamento que ele vai manter até o fim do semestre — a partir da Semana 10, a atenção se volta para o Kit Modular, que não vai receber o mesmo tempo individual de pintura."*
2. **(3 min)** Reflexão: *"Que decisão de desgaste você tomou que conta uma história específica do seu tema, e não seria genérica em qualquer outro projeto?"*
3. **(2 min)** Ponte para a Semana 10: *"Na próxima semana começa a Unidade III — Kit Modular, com os primeiros assets de Modelagem 3D e Level Design chegando, e a técnica de stencils."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. Desgaste uniforme sem narrativa de uso**
Estratégia: perguntar de onde vem o desgaste na história do objeto (impacto? fricção de manuseio? exposição ao tempo?) antes de pintar.

**2. Detalhe que só funciona em close-up e desaparece à distância**
Estratégia: sempre testar em duas distâncias de câmera antes de considerar finalizado.

**3. Cronograma comprimido pela SCT**
Estratégia: priorizar a entrega mínima viável (pelo menos uma camada de desgaste completa) e permitir finalização assíncrona se a agenda do evento comprometer o tempo de estúdio.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Sujeira aplicada sem lógica gravitacional | Perguntar onde a poeira/sujeira realmente se acumula em um objeto parado (partes baixas, reentrâncias) |
| Estudante satisfeito com resultado genérico | Comparar com a referência cultural específica do tema (Semana 1/3) e perguntar se o desgaste reforça ou dilui essa especificidade |
| Falta de tempo por causa da SCT | Focar em uma única camada de detalhe bem executada em vez de três incompletas |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Camadas de desgaste organizadas por tipo | C1 — Processo de Projeto | Inspeção da pilha de camadas no 3D Coat |
| Desgaste com lógica de uso perceptível | C5 — Texturização | Render comparativo antes/depois; justificativa verbal do estudante |
| Consistência com a narrativa temática | C2 — Direção Artística | Comparação com moodboard e justificativa da Semana 3 |
| Leitura mantida à distância de uso | C5 — Texturização | Teste de câmera afastada no 3D Coat |

---

## Entrega da Semana 9

| Entrega | Formato | Prazo |
|---|---|---|
| Hero Asset com camadas de detalhe pintadas | Arquivo nativo do 3D Coat | Até o fim do segundo encontro |
| Mapas exportados atualizados | PNG | Até o fim do segundo encontro |
| Render comparativo antes/depois | PNG ou JPG | Até o fim do segundo encontro |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 9 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
