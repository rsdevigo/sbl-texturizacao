---
marp: true
paginate: true
theme: academic-course
size: 16:9
header: "Tecnologia em Jogos Digitais • Texturização"
footer: "IFMS • Semana 06"
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Texturização

## Da cor plana à imagem real

**Semana 6** — Texturas seamless e tileable (trilha fotorrealista ou estilizada)

<!--
Notas: Marcar a virada da semana: pela primeira vez uma imagem real entra no pipeline — o Albedo deixa de ser cor sólida e passa a ser textura. Também é a semana em que cada estudante começa a declarar sua trilha visual (fotorrealista ou estilizada). Sem crítica formal — a próxima é a CF2, na Semana 8.
-->

---

## Onde vocês estão

Semana 5: Hero Asset Referência com UV revisado e material PBR de **valores planos**.

Hoje: a primeira imagem real entra no Albedo — e cada um escolhe sua trilha visual.

<!--
Notas: Recapitular em uma frase. Não reabrir o conteúdo técnico de PBR da Semana 5 (Albedo/Metallic/Roughness) — isso já foi ensinado. Só situar a transição.
-->

---

<div class="objectives">

Ao final da semana você será capaz de:

- Explicar o que é uma textura seamless e por que ela é necessária em jogos
- Diferenciar uma textura seamless de uma simples repetição direta de imagem
- Criar uma textura seamless no Krita com o método de offset e patch de bordas
- Conectar a textura ao canal Albedo do Hero Asset Referência no Blender
- Localizar texturas PBR livres — fotográficas ou estilizadas — conforme sua trilha

</div>

<!--
Notas: Os dois primeiros objetivos são conceituais (mini aula); os três últimos são o trabalho prático do estúdio de hoje.
-->

---

## Antes do conteúdo novo: UVPackmaster (5 min)

Pendência da Semana 4: o add-on **UVPackmaster** empacota UV islands com rotação livre — mais eficiente que o Pack Islands nativo em islands orgânicas.

<div class="tip">

Vale reabrir o Pack Islands do Hero Asset com essa ferramenta antes de aplicar a textura de hoje?

</div>

<!--
Notas: Recapitulação rápida de 5 min antes do conteúdo novo. Se o add-on não estiver disponível no laboratório, mencionar apenas verbalmente com uma imagem comparativa — não é essencial para a semana.
-->

---

<!-- _class: question -->

# O que está errado nesta parede?

![diagram](assets/parede_costura_comparacao.webp)

<!--
Notas: Mostrar duas imagens estáticas lado a lado (sem abrir software ainda): a mesma parede de pedra, uma com textura repetida sem tratamento (costuras visíveis) e outra já seamless. Perguntar "o que está diferente? onde está o problema?" e aguardar 2-3 respostas antes de nomear "costura".

[!FIGURA]
Objetivo didático — Evidenciar visualmente o problema da costura antes de nomear o conceito de textura seamless.
Arquivo sugerido — assets/parede_costura_comparacao.webp
Descrição — Duas renderizações lado a lado de uma mesma parede de pedra: à esquerda, textura de 512×512 repetida sem tratamento (linhas de corte visíveis em grade); à direita, a mesma textura tornada seamless (repetição imperceptível).
Como produzir — Renderizar no Blender um plano com a textura de demonstração aplicada via nó Image Texture com Mapping repetido, uma vez antes e uma vez depois do tratamento seamless no Krita.
-->

---

## Textura seamless: exigência funcional, não estética

Uma textura seamless é matematicamente contínua nas bordas — repetida lado a lado, o olho não detecta a transição.

Paredes, pisos e terrenos em jogos são maiores que uma única tile — a textura pequena repetida só funciona se for seamless.

<div class="tip">

Vale tanto para uma foto quanto para uma textura pintada — o requisito de continuidade de borda é o mesmo nas duas trilhas.

</div>

<!--
Notas: O problema da costura não é estético, é funcional: quebra a ilusão de realidade independentemente da qualidade artística do resto do material.
-->

---

## Por que a imagem bruta nunca é seamless

Fotografias capturam variação de iluminação, sombra e perspectiva — as bordas ficam diferentes entre si.

Uma pintura do zero tem o mesmo problema se o artista não planejar a continuidade das pinceladas.

<div class="error">

Mesmo com conteúdo visual idêntico nos quatro lados, gradientes de luz ou de pincelada vazam pela borda.

</div>

<!--
Notas: Reforçar que o problema é o mesmo nas duas trilhas — muda a fonte da imagem, não o requisito técnico.
-->

---

## O método: offset + patch

1. Deslocar a imagem **50% em X e 50% em Y**
2. As bordas (antes invisíveis) ficam explícitas, cruzadas no **centro**
3. Pintar sobre as costuras com Clone Stamp, Healing ou pintura direta
4. Resultado: bordas seamless, centro com conteúdo variado

<!--
Notas: Esse é o método clássico e vale para as duas trilhas — a única diferença é se o artista clona pixels de uma foto ou continua pinceladas de uma pintura.
-->

---

## Krita: ferramentas do fluxo

**Wrap Around** (`W`) — pré-visualização de repetição em tempo real, *enquanto* pinta.

**Clone Stamp** (`S`) — copia pixels de outra região para cobrir a costura.

**Smudge Tool** — suaviza transições entre áreas patcheadas e o entorno.

<div class="tip">

Pincéis de textura/papel do Krita ajudam quem estiver pintando uma textura estilizada do zero.

</div>

<!--
Notas: Wrap Around elimina a necessidade de exportar e testar a cada ajuste — é o único feedback confiável em tempo real. Insistir nisso: quem só olha o PNG isolado não vê a costura.
-->

---

## Fontes de textura livre — duas trilhas

**Trilha fotorrealista:** Poly Haven e AmbientCG — mapas PBR completos (Albedo, Normal, Roughness, AO), licença CC0.

**Trilha estilizada:** bancos de texturas pintadas/seamless (Poliigon "Painted", pacotes hand-painted no itch.io) — nem sempre vêm com o pacote PBR completo.

<div class="warning">

Baixar uma textura pronta não isenta de entender o processo — a entrega exige evidência do processo, não só o arquivo final.

</div>

<!--
Notas: Para a trilha estilizada, frequentemente só o Albedo vem pronto — Roughness/Metallic precisam ser calibrados manualmente, como já foi feito na Semana 5.
-->

---

<!-- _class: invert -->

## Na indústria

Um kit modular profissional reaproveita a mesma textura seamless em dezenas de superfícies diferentes.

Uma costura mal resolvida se multiplica — e fica mais cara de corrigir quanto mais tarde for descoberta.

<!--
Notas: Amarrar a C4 (Materiais PBR) e C2 (Direção Artística) — coerência da textura com o universo do kit e com a trilha visual escolhida.
-->

---

<!-- _class: summary-slide -->

# Resumo

- **Seamless** é exigência funcional, igual nas trilhas fotorrealista e estilizada
- Método: **offset 50%/50%** + patch das costuras que aparecem no centro
- **Wrap Around** no Krita é o único feedback confiável em tempo real
- Baixar é válido — **entender e documentar o processo** não é opcional

<!--
Notas: Fechar a mini aula amarrando os conceitos antes da demonstração.
-->

---

## Agora: demonstração

Do offset ao patch: transformando uma fotografia de pedra em textura seamless, ao vivo no Krita.

Importação no Blender e conexão ao Albedo — comparação com o caso estilizado.

![diagram](assets/demo_krita_offset_patch.webp)

<!--
Notas: Transição para os 20 min de demonstração: Krita (offset, Clone Stamp, Wrap Around, exportação) → Blender (nó Image Texture → Base Color) → comparação rápida com uma textura estilizada já preparada, mostrando que o processo é idêntico.

[!FIGURA]
Objetivo didático — Mostrar as etapas do processo de offset+patch no Krita, da foto bruta ao resultado seamless.
Arquivo sugerido — assets/demo_krita_offset_patch.webp
Descrição — Sequência de 3 capturas de tela do Krita lado a lado: (1) foto bruta com Wrap Around ativado mostrando costuras nas bordas, (2) a mesma imagem após o offset de 50%/50% com as costuras agora cruzando o centro, (3) resultado final após o patch com Clone Stamp, sem costuras visíveis no Wrap Around.
Como produzir — Capturar no Krita usando a fotografia de pedra de demonstração do professor, salvando as três etapas do mesmo arquivo.
-->

---

<!-- _class: chapter -->

<span class="chapter-number">06</span>

# Produção em estúdio

Da imagem de origem à textura seamless aplicada ao Hero Asset

<!--
Notas: Divisória entre a mini aula e o estúdio. Os slides a seguir ficam projetados durante a produção — servem de consigna e timebox visíveis, apresentados um a um conforme a etapa correspondente começa.
-->

---

<!-- _class: exercise -->

## Etapa 1 — Criar a textura seamless

**≈30 minutos.**

Preparem a imagem de origem (foto, textura pintada, ou download do Poly Haven/AmbientCG/banco estilizado).

Apliquem offset 50%/50%, façam o patch com Clone Stamp e verifiquem no Wrap Around (`W`).

Exportem: `[Nome]_[material]_seamless_S06.png`.

<!--
Notas: Encontro 1. A escolha de trilha (fotorrealista ou estilizada) deve ser coerente com o moodboard do kit. Circular perguntando: "essa textura poderia existir no universo do seu kit?"
-->

---

<!-- _class: exercise -->

## Etapa 2 — Aplicar ao Hero Asset no Blender

**≈20 minutos.**

Abram o Hero Asset Referência da Semana 5. No Shader Editor, adicionem um nó Image Texture e conectem ao Base Color.

<div class="warning">

Verifiquem: Metallic e Roughness calibrados na Semana 5 continuam lá? Adicionar o nó pode desconectá-los sem querer.

</div>

Salvem: `[Nome]_HeroAsset_Textura_S06.blend`.

<!--
Notas: Circular verificando três pontos: a textura está seamless (Wrap Around), Metallic/Roughness preservados, e a escala da textura coerente com o asset (nó Mapping se necessário).
-->

---

<!-- _class: exercise -->

## Crítica coletiva informal — 20 minutos

**Rodada circulante, 4–5 estações — sem apresentação individual obrigatória.**

Foco duplo: a textura está seamless (de 2 metros de distância)? E ela poderia existir no universo do kit?

<!--
Notas: Abertura do Encontro 2. Perguntar à turma: "alguém consegue ver onde termina um tile e começa outro?" Fechar nomeando o erro de seamless mais comum observado (tipicamente patch em linha reta) e o estado geral de coerência temática da turma.
-->

---

<!-- _class: exercise -->

## Refinamento da textura principal — ≈20 minutos

Se a crítica apontou costura ou incoerência: voltem ao Krita, refinem o patch, re-exportem.

No Blender, usem **Reload** no nó Image Texture — não precisa reimportar.

Quem já está satisfeito: pulem direto para a próxima etapa.

<!--
Notas: Para quem precisar. Perguntar: "o que mudou com o patch? mostra no Wrap Around antes e depois" — estimula verbalização do processo para C1.
-->

---

<!-- _class: exercise -->

## Aprofundamento — ≈40 minutos

Para quem já concluiu: criem uma **segunda textura seamless** para outra superfície do Hero Asset (ex.: argamassa, couro, metal de um encaixe).

Configurem um segundo slot de material com Metallic e Roughness próprios.

<!--
Notas: Não é obrigatório terminar tudo — o objetivo é sair da semana com domínio real do fluxo Krita → Blender. Perguntar: "esse segundo material é fisicamente diferente do primeiro? o Roughness dele deveria ser igual?"
-->

---

<!-- _class: exercise -->

## Antes de sair

Confirmem as entregas de hoje:

- Textura seamless principal (`_seamless_S06.png`) **+ arquivo `.kra` de origem**
- Hero Asset Referência com textura aplicada ao Albedo (`_HeroAsset_Textura_S06.blend`)
- Segunda textura de apoio, se concluída (opcional)

<div class="warning">

Sem crítica formal hoje. Guardem o `.kra` (não só o PNG) — vocês vão precisar dele na Semana 7.

</div>

<!--
Notas: Fechamento (10 min): "O Albedo do Hero Asset não é mais uma cor — é uma superfície com história." Ponte: na Semana 7 a ferramenta muda para o 3D Coat, com bake de AO/Curvature/Normal direto da malha — quem está na trilha fotorrealista reforça o desgaste sobre a textura de hoje; quem está na estilizada usa os mesmos mapas como máscara para Smart Materials.
-->
