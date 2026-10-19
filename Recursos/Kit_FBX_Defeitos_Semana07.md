# Kit de FBX com defeito — Semana 7

> Material do professor para o **quiz "Esse modelo está pronto para exportar?"** (mini aula) e para a **clínica de exportação** (estúdio do Encontro 1) da Semana 7.
> Complementa a página [Cenários de Exportação Blender → 3DCoatTextura](/Recursos/Cenarios_Exportacao_Blender_3DCoatTextura.md).

O kit tem **seis caixotes simples** (cubo com reentrâncias em todas as faces, bom para AO e Curvature): um correto e cinco com defeitos de exportação comuns.

---

## Como gerar

Os FBX já estão prontos no repositório, em `Recursos/Kit_Semana07/Kit_FBX_Defeitos/`. Para gerar de novo (por exemplo, numa versão diferente do Blender):

1. Abra o Blender com um arquivo **novo** (*File → New → General*) e salve-o, por exemplo, em `Kit_Semana07/kit.blend`.
2. Aba **Scripting → New**, cole o conteúdo de [`gerar_kit_fbx_defeitos.py`](https://github.com/rsdevigo/sbl-texturizacao/blob/main/Recursos/Kit_Semana07/gerar_kit_fbx_defeitos.py) e clique em **Run Script**.
3. Os FBX aparecem em `Kit_FBX_Defeitos/`, ao lado do `.blend`. Os objetos ficam na cena: use-os para fazer os prints do quiz.

O script foi testado no Blender 5.2 (módulo `bpy`). Ele só cria e exporta os próprios objetos e não apaga nada da cena.

---

## Gabarito

| Arquivo | Defeito | Cenário | Sintoma esperado | Correção no Blender |
|---|---|---|---|---|
| `K1_OK.fbx` | Nenhum (controle) | 1 | Importa normalmente; ilhas organizadas no Texture Editor | Nada. A dupla precisa justificar com o checklist |
| `K2_SemUV.fbx` | Malha sem nenhuma camada de UV | 2 | A importação Per-Pixel não encontra UV (ou oferece mapeamento automático); textura não alinha | Abrir o UV (Smart UV Project para teste, seams para entrega) e reexportar |
| `K3_UV_Sobreposto.fbx` | Mirror aplicado sem deslocar o UV: as duas metades usam as mesmas ilhas | 3 | O que se pinta num caixote aparece no outro; AO calculado pode sair estranho | Separar as ilhas da segunda metade (ou ligar *Mirror U* no modificador e reorganizar o UV); se a simetria for intencional, documentar |
| `K4_Escala_Rotacao.fbx` | Escala 100 e rotação não aplicadas | 9 | Modelo chega gigante e/ou girado (depende das opções de importação) | `Ctrl+A → All Transforms` e reexportar |
| `K5_Modificador.fbx` | Array (3 cópias) exportado com *Apply Modifiers* desligado | 8 | Chega **um** caixote em vez de três | Aplicar o modificador (ou marcar *Apply Modifiers*) e **conferir o UV**: as três cópias passam a compartilhar as ilhas (volta ao cenário 3) |
| `K6_Duas_UV.fbx` | Duas camadas de UV; a primeira é um *Lightmap Pack* | 7 | O 3DCoatTextura pode usar a camada errada: ilhas pequenas e desorganizadas no Texture Editor, textura da Semana 6 desalinhada | Apagar a camada `Lightmap` (a Unity gera o lightmap) ou mover a UV de textura para a primeira posição; reexportar |

---

## Uso em aula

### Quiz da mini aula (Bloco 4, 5 min)

Projetar prints do Blender (não do 3DCoat) de **K2, K3, K4 e K5**, um por slide. A turma responde em voz alta: *qual é o problema e o que fazer?* Os slides da Semana 7 já têm os quatro espaços reservados (`assets/quiz_k2_sem_uv.webp` etc.), com a descrição do print esperado nas notas.

| Print | O que deve aparecer no print |
|---|---|
| K2 | UV Editor vazio; *Object Data → UV Maps* sem entradas |
| K3 | Viewport com os dois caixotes; painel de modificadores com o Mirror; UV Editor com uma só cópia das ilhas |
| K4 | Painel N (*Item*) com Scale 100 e rotação diferente de zero |
| K5 | Viewport com três caixotes; painel de modificadores com o Array (Count 3) não aplicado |

### Clínica de exportação (estúdio, 10 min, em duplas)

1. Distribuir um FBX por dupla (K1–K6, repetindo se houver mais duplas), **sem dizer qual é o defeito**.
2. A dupla importa no 3DCoatTextura, descreve o sintoma, encontra o cenário na página *Cenários de Exportação*, corrige no Blender (*File → Import → FBX*), reexporta e confirma.
3. Nos 2 minutos finais, duas duplas contam **sintoma → causa → correção**.

> Quem recebe o **K1** tem uma resposta válida: *"não há nada a corrigir"*, justificada item a item com o checklist.
