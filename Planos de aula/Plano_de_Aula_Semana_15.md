# Plano de Aula — Semana 15
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** IV — Otimização, Trim Sheets e Integração na Unity (Semanas 14–15)
**Tema da semana:** UDIMs, otimização e integração completa na Unity
**Apostila:** Parte V, Cap. 19 — UDIMs, Texture Arrays e Multi-Tile Texturing; Parte V, Cap. 20 — Compressão, Mipmaps e Packing de Canais; Parte VI, Cap. 21 — Lightmaps e Iluminação em Motores; Parte VI, Cap. 22 — Integração com Unreal Engine e Unity
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔵 Informal — circulante em estúdio e comentário coletivo ao final do segundo encontro. Esta é a semana do evento institucional Pantanal Game Show — sem relação direta com a entrega, mas vale observar a agenda do campus ao planejar o ritmo de estúdio.

---

## O que já foi ministrado (Semana 14 — não repetir)

Na **Semana 14**, os estudantes criaram uma Trim Sheet temática e a aplicaram a variações de um asset arquitetônico modular, completando os Assets de Repetição do kit — avaliado na **CF4**, a última crítica intermediária do semestre.

**Esta é a última semana antes do Projeto Final.** O Kit Modular já está tecnicamente pronto em suas peças individuais (Hero Asset, Secundários, Repetição); o trabalho de hoje é o que transforma um conjunto de assets texturizados em uma **cena funcional na Unity** — a fase caminhável que será apresentada e defendida na Semana 16. Não há mais crítica formal antes disso: esta é a única semana para identificar e corrigir problemas de integração antes da apresentação final.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar quando UDIMs são necessários (assets de alta resolução que excedem a praticidade de um único espaço UV 0–1) em contraste com o Texture Atlas e a Trim Sheet já dominados.
2. Executar channel packing, combinando Roughness, Metallic e AO em um único mapa ORM (Roughness no canal R, Metallic no G, AO no B), reduzindo o número de texturas carregadas pelo motor.
3. Explicar a diferença entre UV1 (textura) e UV2 (lightmap) e abrir um UV2 dedicado para os assets que ainda não o têm.
4. Importar todos os assets do Kit Modular na Unity, configurar os materiais com os mapas otimizados e montar a fase caminhável (colisão de piso e limites de percurso, sem gameplay adicional).
5. Executar o lightmap bake da cena completa e validar a fase caminhável de ponta a ponta.

---

## Critérios da Rubrica Mestre ativos nesta semana

| Critério | Foco desta semana |
|---|---|
| C1 — Processo de Projeto | Organização final de todos os arquivos do kit antes da apresentação da Semana 16 |
| C2 — Direção Artística | Coerência visual do conjunto completo sob iluminação real da Unity (diferente da iluminação de estúdio do Blender/3D Coat) |
| C7 — Otimização | Channel packing (ORM) e UV2 aplicados corretamente |
| C8 — Integração na Unity | **Foco principal — mas sem nota formal ainda.** Montagem completa da fase caminhável, com feedback do professor. A primeira e única nota formal de C8 é atribuída na CF5 (Semana 16), conforme Rubrica Mestre |

> Esta semana não tem crítica formal, mas é **decisiva** para a CF5: qualquer problema de integração não resolvido aqui aparece como falha na apresentação final. O professor deve dar feedback direcionado mesmo sem atribuir nota.

---

## Recursos necessários

- Computadores com Blender e Unity instalados (projeto Unity do trabalho interdisciplinar já configurado, conforme combinado entre as três disciplinas)
- Todos os assets do Kit Modular texturizados até a Semana 14
- Apostila — Parte V, Cap. 19 e 20, e Parte VI, Cap. 21 e 22 — disponibilizadas antes da aula
- **Atenção à agenda do Pantanal Game Show nesta semana** — evento institucional do campus, sem relação direta com a entrega, mas que pode afetar a disponibilidade de horário/laboratório

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **UDIMs para assets de alta resolução:** quando um único espaço UV 0–1 não comporta a resolução necessária para um asset (tipicamente o Hero Asset, se ele exigir detalhe muito alto), UDIMs permitem múltiplos "tiles" UV, cada um com sua própria textura de alta resolução — não é a técnica padrão para o Kit Modular inteiro, mas pode se aplicar pontualmente ao Hero Asset.
2. **Compressão de texturas e mipmaps:** formatos como BC1, BC3 e BC7 reduzem o tamanho em memória das texturas sem perda perceptível na maioria dos casos; mipmaps geram versões reduzidas automaticamente para objetos distantes, evitando aliasing.
3. **Channel packing (mapa ORM):** combinar Roughness (R), Metallic (G) e AO (B) em uma única textura reduz o número de texturas carregadas por material — de três arquivos para um.
4. **Lightmap UV: UV1 vs. UV2.** UV1 é o mapa usado para a textura visual do objeto (já produzido desde a Semana 4); UV2 é um mapa separado, sem sobreposição entre islands, dedicado ao lightmap bake da Unity — a fase caminhável precisa dele para receber iluminação estática de forma correta.

---

### Demonstração — 20 minutos

1. **(8 min) Channel packing** de Roughness, Metallic e AO em um mapa ORM, usando compositing no Blender ou uma ferramenta equivalente.
2. **(6 min) Abertura de UV2 (lightmap)** no Blender e reexportação do FBX com os dois canais de UV.
3. **(6 min) Importação na Unity, montagem básica da fase e lightmap bake da cena.**

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Criem mapas ORM para os assets do kit que ainda não têm. Abram UV2 nos assets que ainda não têm. Comecem a importar os assets na Unity."*

**Atividade estruturada:**

1. **(20 min) Channel packing** dos assets pendentes.
2. **(15 min) Abertura de UV2** nos assets pendentes.
3. **(15 min) Início da importação na Unity.**

**Papel do professor:** verificar se a exportação do FBX está preservando os dois canais de UV corretamente — erro comum é exportar apenas UV1.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Informal — 20 minutos

Circulante em estúdio; comentário coletivo rápido sobre o estado de montagem da fase caminhável de cada estudante — foco em identificar problemas de integração antes da Semana 16.

> **Nota do professor:** ajustar a duração conforme a agenda do Pantanal Game Show, se necessário.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Montem a fase caminhável completa: todos os assets do kit importados, colisão de piso e limites de percurso configurados, sem gameplay adicional. Executem o lightmap bake da cena inteira."*

**Atividade:**

1. Importar todos os assets restantes do Kit Modular.
2. Configurar colisão de piso e limites de percurso.
3. Executar o lightmap bake da cena completa.
4. Testar a caminhada de ponta a ponta, verificando ausência de falhas de colisão.
5. Capturar screenshots da cena (4 ângulos) e um teste de caminhada (vídeo curto ou gif).

**Papel do professor:** priorizar estudantes com falhas de colisão ou lightmap não gerado — são os riscos mais graves para a apresentação da Semana 16. Dar feedback direto e específico, mesmo sem nota formal.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"A partir de hoje, o kit deixou de ser uma coleção de arquivos separados e virou uma cena única e funcional. É essa cena, não os arquivos individuais, que vocês vão apresentar na Semana 16."*
2. **(3 min)** Reflexão: *"Que problema de integração surpreendeu vocês ao levar o kit para a Unity, que não aparecia no Blender ou no 3D Coat?"*
3. **(2 min)** Ponte para a Semana 16: *"Na próxima semana é a apresentação e defesa do Projeto Final — a CF5, com todos os dez critérios da rubrica em jogo, incluindo a primeira e única nota de C8."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. UV2 sobreposto (herdado do UV1), impedindo lightmap bake correto**
Estratégia: usar a função de lightmap unwrap automático do Blender como ponto de partida, ajustando manualmente apenas onde necessário.

**2. Materiais aparecendo "achatados" ou sem brilho na Unity, diferente do 3D Coat**
Estratégia: verificar se o Roughness/Metallic foi corretamente conectado nos slots do shader da Unity (Standard ou URP/HDRP, conforme o pipeline do projeto) — não apenas visualmente semelhante no Blender.

**3. Falhas de colisão no percurso caminhável**
Estratégia: verificar se todos os assets de piso e paredes têm collider configurado; testar a caminhada em primeira pessoa antes de considerar concluído.

**4. Cronograma comprimido pelo Pantanal Game Show**
Estratégia: priorizar a montagem funcional da fase (mesmo sem lightmap perfeito) sobre o polimento estético — o lightmap pode ser refeito até a Semana 16, mas uma fase não-caminhável compromete toda a apresentação.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Estudante sem saber por onde começar a montagem na Unity | Seguir a ordem da demonstração: importar → configurar material → posicionar → testar colisão → lightmap |
| Textura com aparência diferente entre 3D Coat e Unity | Comparar valores de Roughness/Metallic lado a lado nos dois softwares |
| Kit com assets insuficientes para uma fase minimamente interessante | Revisar o inventário da Semana 13 e priorizar a finalização dos Assets de Repetição pendentes |
| Ansiedade pela proximidade da apresentação final | Lembrar que esta semana não tem nota formal — é o momento de errar e corrigir antes da CF5 |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Mapas ORM (channel packing) aplicados | C7 — Otimização | Inspeção dos materiais na Unity |
| UV2 aberto e lightmap bake executado sem erros graves | C7, C8 — Otimização / Integração na Unity (observado) | Inspeção do lightmap e da cena |
| Fase caminhável funcional de ponta a ponta | C8 — Integração na Unity (observado) | Teste de caminhada; vídeo ou gif de evidência |
| Coerência visual do kit sob iluminação real | C2 — Direção Artística | Comparação com a referência de estúdio (Blender/3D Coat) |

---

## Entrega da Semana 15

| Entrega | Formato | Prazo |
|---|---|---|
| Fase caminhável montada na Unity com todos os assets, materiais ORM e lightmap baked | Projeto Unity | Até o fim do segundo encontro |
| Screenshots da cena (4 ângulos) | PNG ou JPG | Até o fim do segundo encontro |
| Teste de caminhada | Vídeo curto ou gif | Até o fim do segundo encontro |

> **Nota:** não há Ficha de Crítica Formal nem nota atribuída nesta semana — o professor registra observações qualitativas para orientar a preparação da CF5.

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 15 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
