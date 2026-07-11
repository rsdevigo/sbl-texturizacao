# academic-course — Tema Marp para ensino

Um tema **[Marp](https://marp.app/)** limpo, moderno e altamente configurável para aulas de ensino superior, cursos técnicos, pós-graduação e treinamentos corporativos. Toda a identidade visual é controlada por **variáveis CSS**: para adaptar a qualquer disciplina ou instituição, basta trocar as variáveis e os metadados do Markdown — sem tocar no restante do código.

> A paleta padrão (índigo `#3B2F68`, verde `#B6D7A8`, cinza `#EFEFEF`) e a fonte **Open Sans** foram derivadas do template institucional *Apresentação Jogos IFMS v2*. Como tudo está em variáveis, é só editar o `:root` para adotar outra identidade.

Compatível com **Marp CLI**, **Marp for VS Code**, **GitHub Actions** e exportação para **HTML**, **PDF** e **PPTX**.

---

## Sumário

- [Instalação](#instalação)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como utilizar](#como-utilizar)
- [Como alterar as cores](#como-alterar-as-cores)
- [Como trocar o logotipo](#como-trocar-o-logotipo)
- [Como alterar as fontes](#como-alterar-as-fontes)
- [Layouts (classes de slide)](#layouts-classes-de-slide)
- [Componentes (callouts)](#componentes-callouts)
- [Imagens](#imagens)
- [Tabelas, código e diagramas](#tabelas-código-e-diagramas)
- [Como criar novos layouts](#como-criar-novos-layouts)
- [Exportação com Marp CLI](#exportação-com-marp-cli)
- [Boas práticas](#boas-práticas)
- [Limitações](#limitações)
- [Licença](#licença)

---

## Instalação

### Opção A — VS Code (recomendado para preparar aulas)

1. Instale a extensão **Marp for VS Code**.
2. Nas configurações da extensão, adicione o caminho do tema em `markdown.marp.themes`:

   ```json
   "markdown.marp.themes": [
     "./themes/academic-course.css"
   ]
   ```

3. No cabeçalho do seu `.md`, use `theme: academic-course`.

### Opção B — Marp CLI

Nenhuma instalação de tema é necessária; aponte para o CSS no comando (veja [Exportação](#exportação-com-marp-cli)).

---

## Estrutura do projeto

```text
.
├── themes/
│   └── academic-course.css     # o tema (único arquivo)
├── examples/
│   ├── cover.md                # capa
│   ├── chapter.md              # abertura de capítulo / seção
│   ├── content.md              # slide de conteúdo padrão
│   ├── image-right.md          # texto + imagem à direita
│   ├── image-left.md           # imagem à esquerda + texto
│   ├── comparison.md           # duas colunas (correto × incorreto)
│   ├── question.md             # pergunta motivadora + exercício
│   ├── timeline.md             # linha do tempo
│   └── diagram.md              # diagrama Mermaid
└── README.md
```

---

## Como utilizar

Todo deck começa com um bloco de metadados (front-matter). Os campos de `header` e `footer` alimentam o cabeçalho e o rodapé do tema.

```markdown
---
marp: true
theme: academic-course
paginate: true
header: 'Nome da disciplina ou seção atual'
footer: 'Instituição · Curso · Disciplina'
---

## Título do slide

Conteúdo aqui.
```

Para aplicar um layout a um slide específico, use um comentário de classe no topo do slide:

```markdown
<!-- _class: cover -->
```

O sublinhado (`_class`) aplica a classe **apenas àquele slide**. Sem o sublinhado (`class`), a classe passa a valer para todos os slides seguintes.

---

## Como alterar as cores

Abra `themes/academic-course.css` e edite o bloco `:root`. Você não precisa mexer em mais nada.

```css
:root {
  --primary-color: #1f4e79;   /* cor institucional principal */
  --secondary-color: #2e75b6; /* apoio */
  --accent-color: #f2a900;    /* destaques e barras */
  --text-color: #1c2430;      /* texto do corpo */
  --background-color: #ffffff;
  /* ... demais variáveis ... */
}
```

Exemplo — trocar para uma identidade verde:

```css
--primary-color: #14532d;
--secondary-color: #2e9e5b;
--accent-color: #f2a900;
```

Também é possível sobrescrever variáveis **por deck**, sem editar o tema, adicionando um `<style>` no Markdown:

```markdown
<style>
:root { --primary-color: #7a1f2b; --accent-color: #d9a441; }
</style>
```

---

## Como trocar o logotipo

O logotipo é apenas uma imagem no slide de capa. Substitua a URL/caminho em `cover.md`:

```markdown
![logo](caminho/para/seu-logo.png)
```

O tamanho é controlado pela variável `--logo-width` (padrão `140px`). Recomenda-se um PNG com fundo transparente. Para logotipos em outros slides, use a classe utilitária `.right` ou posicione com um `<style>` local.

---

## Como alterar as fontes

O tema usa **Open Sans** (texto, mesma fonte do template institucional IFMS) e **JetBrains Mono** (código), importadas do Google Fonts no topo do CSS. Para mudar:

1. Ajuste o `@import` (ou remova-o para trabalhar offline).
2. Atualize as variáveis:

   ```css
   --font-family: 'Open Sans', 'Segoe UI', Roboto, Arial, sans-serif;
   --code-font-family: 'JetBrains Mono', Consolas, monospace;
   ```

Tamanhos pensados para projeção (também são variáveis):

| Elemento          | Variável                | Padrão |
|-------------------|-------------------------|--------|
| Título principal  | `--title-font-size`     | 44 px  |
| Subtítulo         | `--subtitle-font-size`  | 32 px  |
| Seção (h3)        | `--heading-font-size`   | 27 px  |
| Texto             | `--body-font-size`      | 24 px  |
| Legenda           | `--caption-font-size`   | 19 px  |
| Código            | `--code-font-size`      | 20 px  |

---

## Layouts (classes de slide)

Aplique com `<!-- _class: nome -->`.

| Classe            | Uso                                                        |
|-------------------|------------------------------------------------------------|
| `cover`           | Capa: título, subtítulo, professor, instituição, logo      |
| `chapter`         | Abertura de capítulo — grande título, pouco texto          |
| `section`         | Divisória mais leve entre blocos                           |
| `image-right`     | Texto à esquerda, imagem à direita (grid)                  |
| `image-left`      | Imagem à esquerda, texto à direita                         |
| `comparison`      | Duas colunas — antes × depois, correto × incorreto         |
| `two-columns`     | Duas colunas genéricas                                     |
| `three-columns`   | Três colunas                                               |
| `full-image`      | Imagem em tela cheia com legenda opcional (`.overlay`)     |
| `timeline`        | Linha do tempo com marcadores conectados                   |
| `question`        | Pergunta motivadora centralizada                           |
| `exercise`        | Atividade / desafio / discussão                            |
| `summary-slide`   | Slide de resumo                                            |
| `quote`           | Citação em tela inteira (`.author` para o autor)           |
| `diagram`         | Diagramas Mermaid centralizados                            |
| `code`            | Slide dedicado a um bloco de código maior                  |
| `invert`          | Fundo escuro institucional para um slide de ênfase         |

**Estruturas auxiliares** usadas dentro dos layouts:

- `image-right` / `image-left`: envolva o texto em `<div class="text">` e a imagem em `<div class="media">`.
- `comparison` / colunas: use `<div class="columns">` com `<div class="col">` (adicione `positive` ou `negative` para as bordas coloridas).
- `cover`: agrupe os metadados em `<div class="meta">`.
- `chapter`: use `<span class="chapter-number">01</span>` para o número gigante ao fundo.
- `full-image`: legenda em `<div class="overlay">`.
- `quote`: autor em `<div class="author">`.

---

## Componentes (callouts)

Blocos de destaque com estilo próprio. Use uma `div` com a classe correspondente:

```markdown
<div class="tip">

Comece sempre pelo Roughness.

</div>
```

| Classe        | Rótulo automático   |
|---------------|---------------------|
| `tip`         | 💡 Dica             |
| `best`        | ✅ Boas práticas    |
| `warning`     | ⚠️ Atenção          |
| `error`       | 🚫 Erro comum       |
| `curiosity`   | 🔎 Curiosidade      |
| `industry`    | 🏭 Na indústria     |
| `objectives`  | 🎯 Objetivos        |
| `summary`     | 📌 Resumo           |

> Deixe **uma linha em branco** depois de abrir a `div` e antes de fechá-la — é o que permite ao Marp interpretar o Markdown interno.

---

## Imagens

Controle o tamanho pelo texto alternativo (`alt`):

```markdown
![small](img.png)    <!-- 260px -->
![medium](img.png)   <!-- 460px -->
![large](img.png)    <!-- 720px -->
![flat](img.png)     <!-- sem sombra -->
![plain](img.png)    <!-- sem sombra e sem borda arredondada -->
```

Todas as imagens recebem borda arredondada (`--image-radius`) e sombra discreta (`--image-shadow`) por padrão. Para imagem em tela cheia, use o layout `full-image`.

---

## Tabelas, código e diagramas

**Tabelas** têm cabeçalho destacado e zebra striping ativado por padrão. Para desativar o striping em um slide: `<!-- _class: no-zebra -->`.

**Código** usa fundo suave, borda arredondada e fonte monoespaçada. Blocos com cerca (```) são estilizados automaticamente.

**Mermaid**: o tema apenas centraliza e dá respiro ao contêiner — não sobrescreve as cores internas do Mermaid. Habilite o Mermaid no Marp (o Marp for VS Code já o suporta) e use a classe `diagram` no slide.

---

## Como criar novos layouts

1. Escolha um nome de classe, por exemplo `case-study`.
2. Adicione a regra ao final da seção **11. LAYOUTS** do CSS:

   ```css
   section.case-study {
     display: flex;
     flex-direction: column;
     justify-content: center;
     border-left: 12px solid var(--accent-color);
   }
   ```

3. Prefira **variáveis CSS** a valores fixos, para manter a coerência com o resto do tema.
4. Use no Markdown: `<!-- _class: case-study -->`.
5. Documente a nova classe nesta tabela de layouts.

---

## Exportação com Marp CLI

Instale o CLI (uma vez):

```bash
npm install -g @marp-team/marp-cli
```

Exportar um deck:

```bash
# HTML
marp --theme themes/academic-course.css examples/content.md -o out/content.html

# PDF (bom para impressão / distribuição)
marp --theme themes/academic-course.css examples/content.md --pdf -o out/content.pdf

# PowerPoint (editável)
marp --theme themes/academic-course.css examples/content.md --pptx -o out/content.pptx

# Diagramas Mermaid exigem o motor com Chromium; use --pdf/--pptx normalmente.
```

Exemplo de passo no **GitHub Actions**:

```yaml
- name: Build slides
  run: |
    npx @marp-team/marp-cli@latest \
      --theme themes/academic-course.css \
      --pdf slides/*.md -o dist/
```

---

## Boas práticas

- **Pouco texto por slide.** Deixe o professor narrar; o slide é apoio visual.
- Use **um layout por intenção**: pergunta → `question`, comparação → `comparison`, etc.
- Aproveite os **callouts** para separar dica, erro comum e curiosidade — ajuda a memória visual.
- Padronize `header`/`footer` em todos os decks da disciplina para dar unidade.
- Mantenha o contraste alto e nunca dependa só da cor (os callouts têm rótulo textual justamente por isso — acessibilidade).
- Teste em **16:9** e, se necessário, em **4:3** (`size: 4:3` no front-matter).

---

## Limitações

- O **PPTX** exportado pelo Marp gera slides como imagens de fundo — ótimo para projetar, limitado para edição fina no PowerPoint.
- Layouts em grid (`image-right`, `columns`) dependem de `<div>` no Markdown; lembre das **linhas em branco** internas.
- Mermaid requer o motor Chromium do Marp CLI/VS Code para renderizar em PDF/PPTX.
- Emojis dos callouts dependem da fonte de emoji do sistema no momento da renderização.

---

## Licença

MIT — livre para usar, modificar e redistribuir em qualquer disciplina ou instituição.
