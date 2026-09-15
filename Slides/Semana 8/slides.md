---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 08"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Texturização

## Do refinamento à exportação completa

**Semana 8** — Refinamento no 3D Coat e exportação PBR unificada (Albedo, Metallic, Roughness, Normal)

<!--
Notas: Marcar que hoje é a segunda Crítica Formal do semestre (CF2), fechando a Unidade II. É a mesma peça em jogo desde a Semana 3 — hoje o material fica tecnicamente completo e pronto para a Unity.
-->

---

## Onde vocês estão

Semana 7: Color, Roughness e Normal ativos no 3D Coat, via bake de AO/Curvature e pintura de Depth.

Hoje: falta o Metallic, mais refinamento intencional, e a exportação dos quatro mapas.

<!--
Notas: Recapitular em uma frase. Não reabrir o conteúdo técnico do bake da Semana 7 — isso já foi ensinado. Só situar o que falta.
-->

---

<div class="objectives">

Ao final da semana você será capaz de:

- Refinar Color, Roughness e Metallic combinando base, máscara e pintura manual
- Descrever quando o Subsurface Scattering é fisicamente adequado
- Pintar o canal Metallic com lógica física correta (binária, transições nítidas)
- Exportar os quatro mapas PBR do 3D Coat de forma unificada
- Configurar o material final no Blender sem nenhum nó procedural remanescente
- Apresentar e defender as decisões de material na Crítica Formal (CF2)

</div>

<!--
Notas: Os cinco primeiros objetivos são o trabalho técnico da semana; o sexto é a própria CF2.
-->

---

<!-- _class: question -->

# O que ainda falta pro material ir pra Unity?

<!--
Notas: Vocês já têm Color, Roughness e Normal ativos desde a semana passada. Conduzir a turma a perceber que falta: (1) o Metallic, ainda não trabalhado a fundo; (2) mais uma camada de detalhe intencional; (3) a exportação de tudo como imagem real.
-->

---

## Por que os mapas do 3D Coat são portáveis

Os mapas do 3D Coat são **imagens reais** (PNG/TGA) — abrem em qualquer software, conectam em qualquer motor.

Um material feito só de nós no Blender não sai do Blender.

<div class="tip">

Por isso o pipeline fecha assim: Blender (modelagem + UV) → **3D Coat (texturização)** → Unity (motor).

</div>

<!--
Notas: Recapitulação rápida de 1 min antes do conteúdo novo (SSS e combinação de camadas).
-->

---

## Subsurface Scattering (SSS)

Simula luz que penetra levemente antes de dispersar — pele, cera, mármore, folhas, tecidos finos.

Resultado: suavidade nas transições de luz/sombra e leve "brilho interno" nas bordas.

<div class="tip">

Valores de 0 a 1. Para elementos orgânicos: **0.05–0.15** costuma bastar sem "derreter" a leitura de material sólido.

</div>

<!--
Notas: Para a maioria dos Hero Assets do kit (pedra, metal, madeira, concreto) o SSS não se aplica — e não pintar nada nesse canal é a decisão fisicamente correta, não uma omissão.
-->

---

## Combinando fontes numa mesma camada

O material já tem três origens empilhadas: **base** (foto/Smart Material), **máscara** (AO/Curvature) e **pintura manual** (Depth, variação de cor).

Nenhuma sozinha deveria contar toda a história.

<div class="tip">

Teste: desligue só a camada de máscara. O material ainda deveria parecer razoável — só mais "novo", menos usado.

</div>

<!--
Notas: Se ao desligar a máscara o material sumir ou virar outra coisa, ela está fazendo trabalho demais sozinha. Como é uma única peça este semestre, vale ir além do mínimo: segunda camada de detalhe focal, revisar intensidade isoladamente no Render Room.
-->

---

## O pacote de exportação: quatro mapas, uma vez só

1. **Refinar** Color, Roughness e Metallic com detalhe adicional
2. **Exportar** os quatro mapas: Albedo, Roughness, Metallic e **Normal** (bakeado desde a Semana 7)
3. **Conectar** no Blender, com o Color Space correto em cada nó

<!--
Notas: Manter o ritmo desta mini aula curto — o conteúdo novo real é o SSS e a lógica de combinação de camadas; o resto é consolidação. Priorizar tempo de demonstração e estúdio.
-->

---

<!-- _class: invert -->

## Na indústria

Um material que só sai como nós de um software não viaja para o motor do jogo.

O pacote de mapas reais (Albedo, Metallic, Roughness, Normal) é o formato universal entre DCC e motor.

<!--
Notas: Amarrar a C4 (Materiais PBR) e C5 (Texturização) — critérios centrais da CF2 de hoje.
-->

---

<!-- _class: summary-slide -->

# Resumo

- **SSS**: 0.05–0.15 para orgânicos; nada para pedra/metal/madeira — omissão correta
- Nenhuma camada sozinha conta a história: **base + máscara + pintura** combinadas
- **Metallic** é binário — preto (0) ou branco (1), sem meio-termo
- Hoje é **CF2**: apresentem a trilha, os canais ativos e uma decisão justificada

<!--
Notas: Fechar a mini aula amarrando os conceitos antes da demonstração.
-->

---

## Agora: demonstração

Refinamento de Color, canal Metallic binário, revisão do Roughness combinado.

Exportação dos quatro mapas e reconexão no Blender — com o nó Normal Map obrigatório.

![diagram](assets/demo_exportacao_4_mapas.webp)

<!--
Notas: Transição para os 20 min de demonstração. Passo a passo: (1) camada de detalhe focal no Color, (2) Metallic Fill preto/branco conforme material — transição nítida, não gradiente, (3) revisão do Roughness ligando/desligando camadas, (4) exportação: File → Export Textures, PNG 1024×1024, os 4 mapas, (5) Blender: 4 nós Image Texture, Albedo em sRGB, os demais em Non-Color, nó Normal Map obrigatório entre o Image Texture do Normal e o Principled BSDF.

[!FIGURA]
Objetivo didático — Mostrar o resultado final: quatro mapas PNG exportados lado a lado e o node tree do Blender com a conexão correta, incluindo o nó Normal Map.
Arquivo sugerido — assets/demo_exportacao_4_mapas.webp
Descrição — Captura de tela combinando (1) os quatro arquivos PNG exportados (Albedo, Roughness, Metallic, Normal) visíveis no explorador de arquivos, e (2) o Shader Editor do Blender com os quatro nós Image Texture conectados ao Principled BSDF, incluindo o nó Normal Map intermediário.
Como produzir — Capturar no explorador de arquivos após a exportação de demonstração e no Blender após a reconexão do material.
-->

---

<!-- _class: chapter -->

<span class="chapter-number">08</span>

# Produção em estúdio

Refinamento, exportação e Crítica Formal 2

<!--
Notas: Divisória entre a mini aula e o estúdio. Os slides a seguir ficam projetados durante a produção — servem de consigna e timebox visíveis, apresentados um a um conforme a etapa correspondente começa.
-->

---

<!-- _class: exercise -->

## Etapa 1 — Refinamento do Color

**≈15 minutos.**

Adicionem uma camada de detalhe focal sobre a base já existente, reforçando a leitura de uso/desgaste.

<div class="tip">

A variação de cor conta uma história, sem apagar a base?

</div>

<!--
Notas: Encontro 1. Se houver tempo: testar uma segunda camada de detalhe em outra área, comparando o peso relativo das duas.
-->

---

<!-- _class: exercise -->

## Etapa 2 — Canal Metallic

**≈15 minutos.**

Materiais não-metálicos (pedra, madeira, concreto): **Fill preto puro**, sem pintar nada adicional.

Materiais metálicos: Fill branco, com preto nas áreas de ferrugem/tinta exposta, guiado pela máscara de Curvature.

<div class="warning">

Metallic é quase binário. Transições nítidas, não gradientes suaves.

</div>

<!--
Notas: Para quem tiver elemento orgânico/translúcido: localizar o canal Subsurface e testar 0.05–0.15, avaliando no Render Room antes de decidir se mantém.
-->

---

<!-- _class: exercise -->

## Etapa 3 — Revisão do Roughness

**≈10 minutos.**

Conferam se as camadas de base + desgaste + sujeira (Semana 7) ainda produzem contraste perceptível.

Ajustem a opacidade se necessário.

<!--
Notas: Verificar no Render Room ligando/desligando cada camada — a contribuição de cada uma deve ser visível.
-->

---

<!-- _class: exercise -->

## Etapa 4 — Exportação de teste e registro

**≈10 minutos.**

Exportem os quatro mapas (Albedo, Roughness, Metallic, Normal) em PNG 1024×1024.

Salvem o arquivo e capturem screenshots do painel de Layers e do Render Room.

<div class="warning">

Confiram no explorador de arquivos que os quatro PNGs foram gerados — exportação vazia por erro de seleção acontece.

</div>

<!--
Notas: Encerramento do Encontro 1. Distribuir a Autoavaliação agora, se ainda não foi distribuída — é pré-requisito para a Crítica Formal do Encontro 2.
-->

---

<!-- _class: exercise -->

## Crítica Formal 2 (CF2) — 20 minutos

**3–4 apresentações, 2 min cada + 1–2 min de feedback.**

Descrevam: o material, a trilha visual, os canais ativos, e uma decisão técnica ou artística — e leiam sua autoavaliação.

<div class="tip">

Critérios em foco: C1 (processo), C2 (direção artística), C4 (materiais PBR), C5 (texturização), C9 (apresentação).

</div>

<!--
Notas: Abertura do Encontro 2. Quem não tiver autoavaliação preenchida: 5 min emergenciais antes de começar. Turmas grandes: sortear 3-4 para apresentar formalmente, avaliar os demais pela Ficha de Crítica.
-->

---

<!-- _class: exercise -->

## Refinamento final — ≈20 minutos

Incorporem o feedback da crítica: intensidade da máscara, camada de sujeira, transições do Metallic, relevo do Normal.

<!--
Notas: Se sobrar tempo: revisar o canal Subsurface (quando aplicável) e comparar com o moodboard uma última vez.
-->

---

<!-- _class: exercise -->

## Exportação final — ≈10 minutos

Exportem os quatro mapas definitivos: Albedo, Roughness, Metallic, Normal — PNG, 1024×1024.

Pasta: `[Nome]_HeroAsset_Mapas_S08/`.

<!--
Notas: Confirmar no explorador de arquivos que os quatro PNGs foram gerados com tamanho esperado.
-->

---

<!-- _class: exercise -->

## Configuração final no Blender — ≈25 minutos

Criem um material novo e limpo. Quatro nós Image Texture: Albedo (**sRGB**), Roughness/Metallic/Normal (**Non-Color**).

<div class="warning">

O Normal precisa passar por um nó **Normal Map** antes do Principled BSDF — sem ele, o relevo sai incorreto.

</div>

Salvem: `[Nome]_HeroAsset_3DCoat_S08.blend`.

<!--
Notas: Verificar Color Space de cada nó — só o Albedo em sRGB, todos os outros em Non-Color. Erro silencioso: material roda sem erro, mas com aparência errada.
-->

---

<!-- _class: exercise -->

## Antes de sair

Confirmem as entregas de hoje:

- Arquivo do 3D Coat refinado (`_HeroAsset_3DCoat_S08`)
- **Quatro mapas PBR** exportados (`_Albedo`, `_Roughness`, `_Metallic`, `_Normal`)
- `.blend` com material final configurado, sem nós procedurais remanescentes
- Screenshots do Layers e do Render Room

<div class="warning">

Próxima crítica formal: CF3, na Semana 11.

</div>

<!--
Notas: Fechamento (10 min): "Hoje vocês fecharam a Unidade II: um material PBR completo, funcionando igualmente bem nas duas trilhas." Ponte: na Semana 9, texturização artística — edge wear, dirt e leitura de silhueta, sobre o mesmo Hero Asset Referência.
-->
