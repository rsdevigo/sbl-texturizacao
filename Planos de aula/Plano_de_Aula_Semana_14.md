# Plano de Aula — Semana 14
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização, Trim Sheets e Integração na Unity (Semanas 14–15)
**Tema da semana:** Trim Sheets: criação e aplicação para assets modulares
**Apostila:** Parte V, Cap. 18 — Texture Atlas e Trim Sheets (conceito e workflow de trim sheets; aplicação em arquitetura modular). Leitura de apoio: Parte VI, Cap. 23 — Controle de Qualidade de Materiais
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF4** (30% do Portfolio de Artefatos)

---

## O que já foi ministrado (Semana 13 — não repetir)

Na **Semana 13**, os estudantes criaram um Texture Atlas combinando pelo menos três assets do Kit Modular e formalizaram o inventário do kit (asset / camada / status), atingindo o piso mínimo de 5 assets entre Hero Asset Referência, Secundários e de Repetição.

**Esta semana abre a Unidade IV e produz, especificamente, os Assets de Repetição do kit** (ver Plano de Ensino, Seção 8.1): uma única Trim Sheet aplicada a múltiplas variações do mesmo elemento modular — a técnica que sustenta a modularidade da fase caminhável que será montada na Semana 15. É a quarta Crítica Formal do semestre, a última antes do Projeto Final.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Diferenciar Trim Sheet de Texture Atlas: o atlas combina objetos inteiros e distintos em uma textura; a trim sheet é uma faixa de padrões (molduras, bordas, painéis) pensada para ser reutilizada, via tiling, em múltiplas peças modulares diferentes.
2. Planejar uma trim dividindo-a em faixas por tipo de detalhe (moldura, junta, painel liso, ornamento), decidindo tiling horizontal vs. vertical conforme a geometria do asset arquitetônico.
3. Criar uma Trim Sheet temática no 3D Coat coerente com a linguagem visual já estabelecida no kit.
4. Mapear um asset arquitetônico modular (UV elongado ao longo da trim) e validar o resultado no Blender e na Unity.
5. Aplicar a mesma trim em ao menos uma variação do elemento modular, demonstrando o ganho de reutilização.

---

## Critérios da Rubrica Mestre ativos nesta semana — CF4

| Critério | Peso na CF4 | Foco desta semana |
|---|---|---|
| C1 — Processo de Projeto | parte da nota | Inventário do kit atualizado; documentação da trim e de onde ela é aplicada |
| C2 — Direção Artística | parte da nota | Coerência da trim com a linguagem visual do Hero Asset e dos demais assets |
| C4 — Materiais PBR | observado (não pontua) | Verificação de que a trim mantém plausibilidade física ao ser aplicada |
| C5 — Texturização | parte da nota | Qualidade artística da trim sheet em si |
| C6 — Bake | parte da nota | Reaproveitamento de bakes anteriores (Curvature, AO) na produção da trim, quando aplicável |
| C7 — Otimização | **foco principal** | Eficiência de reutilização: quantas peças diferentes a trim sustenta sem multiplicar texturas únicas |
| C9 — Apresentação | parte da nota | Clareza ao apresentar a trim e suas variações aplicadas |

> Esta é a **CF4**, com peso de 30% no Portfolio de Artefatos — o maior peso entre as quatro críticas intermediárias, reconhecendo a trajetória de aprendizado acumulada. Gera Ficha de Crítica Formal e Autoavaliação obrigatória.

---

## Recursos necessários

- Computadores com Blender e 3D Coat instalados
- Ao menos um asset arquitetônico modular recebido de Modelagem 3D e Level Design, com geometria adequada a UV elongado
- Referências de trim sheets de projetos publicados (ArtStation)
- Ficha de Crítica Formal e formulário de Autoavaliação
- Apostila — Parte V, Cap. 18, e Parte VI, Cap. 23 — disponibilizadas antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **O que é uma Trim Sheet e quando usar:** uma faixa estreita de textura com múltiplos padrões (bordas, molduras, painéis) organizados lado a lado, pensada para ser mapeada repetidamente (tiling) ao longo de peças modulares diferentes — típica de arquitetura em jogos (paredes, vigas, molduras de porta).
2. **Diferença entre Trim Sheet e Texture Atlas:** o atlas reserva um espaço fixo para cada objeto inteiro; a trim é projetada para repetição via tiling, sustentando um número teoricamente ilimitado de peças com uma única textura estreita.
3. **Planejamento de uma trim:** dividir a faixa em seções por tipo de detalhe (por exemplo, um terço para moldura ornamentada, um terço para painel liso, um terço para junta/borda) — cada estudante escolhe a divisão conforme os elementos modulares do próprio kit.
4. **Tiling horizontal vs. vertical:** a orientação da trim deve seguir a direção predominante de repetição do asset modular (uma parede alta se beneficia de tiling vertical; uma cornija longa, de tiling horizontal).

---

### Demonstração — 20 minutos

1. **(10 min) Criação de uma Trim Sheet temática no 3D Coat**, dividindo a faixa em seções coerentes com um tema de referência.
2. **(6 min) Mapeamento de um asset arquitetônico modular na trim** (UV elongado ao longo da faixa).
3. **(4 min) Validação no Blender e na Unity:** verificar que o tiling se comporta corretamente ao repetir a peça.

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Criem uma Trim Sheet condizente com o tema do kit e apliquem em ao menos um asset arquitetônico modular."*

**Atividade estruturada:**

1. **(15 min) Planejamento da divisão da trim** por tipo de detalhe.
2. **(35 min) Criação da trim no 3D Coat e mapeamento** do primeiro asset modular.

**Papel do professor:** perguntar *"Essa divisão de faixas realmente cobre os tipos de detalhe que aparecem no seu kit, ou falta alguma categoria?"*

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Formal — 20 minutos

**Formato: CF4**

1. Cada estudante apresenta a Trim Sheet e o asset mapeado, com render mostrando ao menos uma variação usando a mesma trim.
2. Perguntas guiadas: *"Quantas peças diferentes essa trim sustenta? O que aconteceria se vocês precisassem de uma quarta variação amanhã?"*
3. Ficha de Crítica Formal preenchida; Autoavaliações recolhidas.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Apliquem a trim em pelo menos uma segunda variação do elemento modular, completando os Assets de Repetição do inventário do kit."*

**Atividade:**

1. Aplicar a trim a variações adicionais do elemento modular.
2. Atualizar o inventário do kit com os novos Assets de Repetição.
3. Capturar render com comparação de variações usando a mesma trim.
4. Salvar: `[Nome]_TrimSheet_Semana14_final`.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"A trim sheet é a técnica que permite ao Kit Modular crescer em número de peças sem crescer proporcionalmente em número de texturas — é otimização pensada desde a raiz do design, não corrigida depois."*
2. **(3 min)** Reflexão: *"Se vocês tivessem que adicionar mais três peças ao kit amanhã, essa trim já daria conta, ou precisaria de uma nova faixa?"*
3. **(2 min)** Ponte para a Semana 15: *"Na próxima semana, fechamos a otimização com channel packing e UDIMs, e montamos a fase caminhável completa na Unity."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. Trim com poucas seções, limitando a variedade visual possível**
Estratégia: revisar o kit e perguntar quais tipos de detalhe (moldura, junta, painel) ainda não têm seção dedicada na trim.

**2. UV elongado mapeado incorretamente, gerando distorção no tiling**
Estratégia: verificar se a proporção do UV corresponde à proporção real da faixa da trim, não apenas ao comprimento do objeto.

**3. Trim sheet visualmente destoante do restante do kit**
Estratégia: comparar diretamente com a paleta e o tipo de desgaste já estabelecidos no Hero Asset e nos Assets Secundários.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante sem clareza de quais elementos modulares precisam de trim | Revisar com o professor de Modelagem 3D e Level Design quais peças arquitetônicas do kit se repetem na fase caminhável |
| Tiling incorreto na Unity apesar de correto no Blender | Verificar configurações de Wrap Mode da textura na importação (Repeat vs. Clamp) |
| Estudante com apenas uma variação, sem tempo para uma segunda | Priorizar a entrega mínima (uma trim + uma aplicação bem executada) e completar a segunda variação como tarefa de acompanhamento até a Semana 15 |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Trim Sheet com seções organizadas por tipo de detalhe | C7 — Otimização | Inspeção da textura e da divisão de faixas |
| Asset mapeado corretamente na trim, sem distorção de tiling | C5, C7 — Texturização / Otimização | Render com tiling ativo |
| Ao menos uma variação usando a mesma trim | C7 — Otimização | Comparação visual das variações |
| Coerência com a linguagem visual do kit | C2 — Direção Artística | Comparação com Hero Asset e Assets Secundários |

---

## Entrega da Semana 14 (CF4)

| Entrega | Formato | Prazo |
|---|---|---|
| Trim Sheet temática | PNG 1024×2048 ou equivalente | Até o fim do segundo encontro |
| Asset mapeado na trim + ao menos uma variação | Render com comparação | Até o fim do segundo encontro |
| Inventário do kit atualizado | Planilha ou documento | Até o fim do segundo encontro |
| Autoavaliação (Instrumento 2) | Preenchida antes da crítica formal | Início do Encontro 2 |
| Ficha de Crítica Formal preenchida pelo professor | Devolução com feedback escrito | Até a Semana 15 |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 14 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
