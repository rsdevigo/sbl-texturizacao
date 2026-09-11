# Plano de Aula — Semana 8
**Disciplina:** Texturização | **Curso:** Tecnologia em Jogos Digitais | **Metodologia:** Studio-Based Learning
**Unidade:** II — Materiais PBR e Workflow no 3D Coat (Semanas 6–9)
**Tema da semana:** Refinamento no 3D Coat e exportação PBR unificada (Albedo, Metallic, Roughness, Normal)
**Apostila:** Parte III, Cap. 10 — Construção e Análise de Materiais Reais (workflow de texturização PBR: camadas e exportação). Leitura de apoio: Parte VI, Cap. 23 — Controle de Qualidade de Materiais
**Carga horária:** 3h (2 encontros de 1h30)
**Crítica:** 🔴 **FORMAL — CF2** (25% do Portfolio de Artefatos)

---

## O que já foi ministrado (Semana 7 — não repetir)

Na **Semana 7**, os estudantes migraram o Hero Asset do Blender para o 3D Coat e ativaram os três primeiros canais — Color (base fotográfica ou Smart Material guiado por máscara de AO/Curvature), Roughness e Normal via Depth — sem ainda exigir refinamento artístico aprofundado.

**Esta semana fecha o ciclo de texturização base no 3D Coat.** O foco muda de "ativar canais" para "refinar e exportar corretamente": Metallic entra formalmente pela primeira vez desde a calibração de valores da Semana 5, e Subsurface Scattering é introduzido para quem tem materiais orgânicos no Hero Asset. É a segunda Crítica Formal do semestre.

---

## Objetivos de Aprendizagem

Ao final da semana, o estudante será capaz de:

1. Explicar o que é Subsurface Scattering (SSS) e quando aplicá-lo a materiais orgânicos (pele, cera, certos tipos de pedra e madeira).
2. Combinar camadas de base, máscara e pintura manual no 3D Coat sem que nenhuma camada isolada "conte toda a história" do material — o resultado final deve ser a soma coerente das partes.
3. Refinar as camadas de Color e Metallic do Hero Asset com atenção a plausibilidade física e intenção artística.
4. Exportar os quatro mapas PBR unificados (Albedo, Metallic, Roughness, Normal) do 3D Coat.
5. Reconfigurar o material do Hero Asset no Blender usando os mapas exportados, com o nó Normal Map corretamente conectado, sem nós procedurais remanescentes da Semana 5.
6. Apresentar o Hero Asset texturizado na segunda Crítica Formal do semestre.

---

## Critérios da Rubrica Mestre ativos nesta semana — CF2

| Critério | Peso na CF2 | Foco desta semana |
|---|---|---|
| C1 — Processo de Projeto | parte da nota | Organização das camadas no 3D Coat; nomenclatura clara dos arquivos exportados |
| C2 — Direção Artística | parte da nota | Coerência total entre o material refinado e a proposta visual desde a Semana 3 |
| C3 — UV Mapping | observado (não pontua) | Verificação de que o UV continua funcional após o ciclo completo de texturização |
| C4 — Materiais PBR | parte da nota | Os quatro mapas exportados e reconfigurados corretamente no Blender, com plausibilidade física |
| C5 — Texturização | parte da nota | Qualidade artística do resultado: variação, desgaste coerente, ausência de aparência "plástica" |
| C9 — Apresentação | parte da nota | Organização da entrega e clareza ao apresentar o resultado na crítica formal |

> Esta é a **CF2**, com peso de 25% no Portfolio de Artefatos. Gera Ficha de Crítica Formal e Autoavaliação obrigatória (Instrumentos 1 e 2 da Rubrica Mestre).

---

## Recursos necessários

- Computadores com Blender e 3D Coat instalados
- Hero Asset com três canais ativos da Semana 7
- Referências de materiais orgânicos (para SSS) e inorgânicos, para calibração de Metallic
- Ficha de Crítica Formal e formulário de Autoavaliação (Instrumentos 1 e 2)
- Projetor para demonstração e crítica formal
- Apostila — Parte III, Cap. 10, e Parte VI, Cap. 23 — disponibilizadas antes da aula

---

## ENCONTRO 1 (1h30)

### Mini Aula — 20 minutos

1. **Subsurface Scattering:** simula luz que penetra levemente a superfície antes de ser espalhada de volta — comum em pele, cera, mármore fino e alguns tipos de folhagem. Aplicar apenas onde o material real justifica; SSS aplicado indiscriminadamente cria aparência de plástico ou borracha.
2. **A lógica de combinar camadas sem que nenhuma "conte toda a história":** a base (fotografia ou Smart Material) dá a textura geral; a máscara de AO/Curvature guia onde o desgaste acontece; a pintura manual adiciona os toques finais que nenhuma automação replica (uma mancha específica, um risco proposital). O material final é a soma das três — nenhuma sozinha é suficiente.
3. **Preparação para exportação:** os quatro mapas PBR (Albedo, Metallic, Roughness, Normal) precisam sair do 3D Coat com resolução e nomenclatura consistentes, prontos para o nó Normal Map no Blender.

---

### Demonstração — 20 minutos

1. **(8 min) Refinamento de Color e Metallic** ao vivo em um material de referência, combinando base + máscara + um toque de pintura manual.
2. **(6 min) Exportação dos quatro mapas PBR** do 3D Coat.
3. **(6 min) Reconfiguração no Blender:** conectar os quatro mapas ao Principled BSDF, com atenção especial ao nó Normal Map (Color Space non-color, conectado via nó Normal Map, não diretamente ao input Normal).

---

### Produção em Estúdio — 50 minutos

**Consigna:**

> *"Refinem Color e Metallic do Hero Asset combinando base, máscara e pintura manual. Se houver material orgânico na peça, testem SSS com moderação."*

**Atividade estruturada:**

1. **(30 min) Refinamento de camadas** no 3D Coat.
2. **(20 min) Exportação e reconfiguração no Blender**, verificando o resultado visual comparado ao 3D Coat.

**Papel do professor:** verificar especificamente a conexão do Normal Map no Blender — é o erro técnico mais comum desta etapa.

---

## ENCONTRO 2 (1h30)

### Crítica Coletiva Formal — 20 minutos

**Formato: CF2**

1. Cada estudante apresenta o Hero Asset texturizado, com render no Blender (mapas reconfigurados) e, se possível, comparação com a visualização no 3D Coat.
2. Perguntas guiadas: *"Por que esse valor de Metallic aqui? Onde está o SSS, se houver, e por que ali?"*
3. Ficha de Crítica Formal preenchida; Autoavaliações recolhidas.

---

### Produção em Estúdio — 60 minutos

**Consigna:**

> *"Ajustem o que for possível a partir do feedback recebido. Registrem por escrito o que ficou pendente."*

**Atividade:**

1. Incorporar ajustes pontuais.
2. Capturar renders finais (com e sem iluminação, conforme Rubrica Mestre C4).
3. Salvar: `[Nome]_HeroAsset_Semana08_final.blend` + mapas exportados.

---

### Fechamento — 10 minutos

1. **(3 min)** Síntese: *"Vocês fecharam o ciclo completo de um material PBR: da malha nua até quatro mapas exportados e reconfigurados. Esse é o fluxo que vocês vão repetir, em escala menor, para cada asset do Kit Modular a partir da Semana 10."*
2. **(3 min)** Reflexão: *"Qual camada — base, máscara ou pintura manual — teve mais peso no resultado final?"*
3. **(2 min)** Ponte para a Semana 9: *"Na próxima semana, aprofundamos a pintura de desgaste e sujeira — é a semana da SCT, então o ritmo de estúdio pode variar."*
4. **(2 min)** Confirmação das entregas.

---

## Possíveis Dificuldades

**1. Normal Map conectado incorretamente no Blender**
Estratégia: verificar sempre a presença do nó Normal Map intermediário e o Color Space "Non-Color" na textura importada.

**2. SSS aplicado a materiais inorgânicos**
Estratégia: perguntar *"Esse material deixa luz passar através dele na vida real?"* — se a resposta for não, remover o SSS.

**3. Nós procedurais remanescentes da Semana 5 competindo com os mapas exportados**
Estratégia: revisar o Shader Editor por completo antes de finalizar, removendo qualquer node de cor sólida esquecido.

---

## Estratégias de Mediação

| Situação | Estratégia |
|---|---|
| Resultado com aparência "plástica" | Verificar variação de Roughness — superfície uniforme demais é a causa mais comum |
| Estudante inseguro na apresentação da CF2 | Relembrar a estrutura de justificativa usada na Semana 3 (representa porque / é viável porque / se conecta porque), adaptada para decisões técnicas |
| Exportação com resolução inconsistente entre mapas | Padronizar todos os mapas na mesma resolução antes de exportar |

---

## Evidências de Aprendizagem

| Evidência | Critério da Rubrica | Como avaliar |
|---|---|---|
| Quatro mapas PBR exportados e reconfigurados | C4 — Materiais PBR | Inspeção do Shader Editor no Blender |
| Resultado com variação e desgaste coerente | C5 — Texturização | Render comparado à referência visual |
| UV ainda funcional após o ciclo de texturização | C3 — UV Mapping (observado) | Verificação rápida do UV Editor |
| Apresentação clara na crítica formal | C9 — Apresentação | Observação direta durante a CF2 |

---

## Entrega da Semana 8 (CF2)

| Entrega | Formato | Prazo |
|---|---|---|
| Hero Asset texturizado no 3D Coat | Arquivo nativo do 3D Coat | Até o fim do segundo encontro |
| Quatro mapas PBR exportados (Albedo, Metallic, Roughness, Normal) | PNG | Até o fim do segundo encontro |
| Material configurado no Blender | `.blend` com sufixo `_Semana08_final` | Até o fim do segundo encontro |
| Autoavaliação (Instrumento 2) | Preenchida antes da crítica formal | Início do Encontro 2 |
| Ficha de Crítica Formal preenchida pelo professor | Devolução com feedback escrito | Até a Semana 9 |

---

*Plano de Aula — Texturização — Jogos Digitais | Semana 8 | 2026 | Prof. Rodrigo Devigo — IFMS Campus Dourados*
