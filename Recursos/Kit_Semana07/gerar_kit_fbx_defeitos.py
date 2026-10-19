# Gera o "Kit de FBX com defeito" da Semana 7 (Texturização — Jogos Digitais).
#
# Como usar:
#   1. Abra o Blender com um arquivo NOVO (File → New → General) e salve-o
#      numa pasta (ex.: Kit_Semana07/kit.blend). Os FBX serão criados em
#      Kit_Semana07/Kit_FBX_Defeitos/.
#   2. Aba Scripting → New → cole este script → Run Script.
#
# O script cria seis caixotes (um correto e cinco com defeito), cada um
# exportado como FBX separado. Ele só cria e exporta os próprios objetos;
# não apaga nada que já esteja na cena.

import bpy
import math
import os

if bpy.data.filepath:
    OUT = os.path.join(os.path.dirname(bpy.data.filepath), "Kit_FBX_Defeitos")
else:
    OUT = os.path.join(os.path.expanduser("~"), "Kit_FBX_Defeitos")
os.makedirs(OUT, exist_ok=True)


def caixote(nome, x):
    """Caixote com reentrâncias (bom para AO/Curvature) e UV por Smart UV Project."""
    bpy.ops.object.mode_set(mode="OBJECT") if bpy.context.object else None
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 0, 0.5))
    ob = bpy.context.active_object
    ob.name = nome
    ob.data.name = nome
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.inset(thickness=0.12, use_individual=True)
    bpy.ops.transform.shrink_fatten(value=-0.04)
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.02)
    bpy.ops.object.mode_set(mode="OBJECT")
    ob.data.uv_layers[0].name = "UVMap_Textura"
    return ob


def exportar(ob, arquivo, aplicar_modificadores=True):
    bpy.ops.object.select_all(action="DESELECT")
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.export_scene.fbx(
        filepath=os.path.join(OUT, arquivo),
        use_selection=True,
        object_types={"MESH"},
        use_mesh_modifiers=aplicar_modificadores,
    )


# K1 — Controle: tudo correto (cenário 1)
k1 = caixote("K1_OK", 0)
exportar(k1, "K1_OK.fbx")

# K2 — Sem UV (cenário 2)
k2 = caixote("K2_SemUV", 3)
while k2.data.uv_layers:
    k2.data.uv_layers.remove(k2.data.uv_layers[0])
exportar(k2, "K2_SemUV.fbx")

# K3 — Mirror sem deslocar o UV: duas metades com ilhas sobrepostas (cenário 3)
k3 = caixote("K3_UV_Sobreposto", 6)
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.transform.translate(value=(0.6, 0, 0))
bpy.ops.object.mode_set(mode="OBJECT")
mod = k3.modifiers.new("Mirror", "MIRROR")
mod.use_axis[0] = True  # espelha em X; use_mirror_u fica desligado (sobreposição)
exportar(k3, "K3_UV_Sobreposto.fbx", aplicar_modificadores=True)

# K4 — Escala e rotação não aplicadas (cenário 9)
k4 = caixote("K4_Escala_Rotacao", 9)
k4.scale = (100, 100, 100)
k4.rotation_euler = (math.radians(90), 0, math.radians(37))
exportar(k4, "K4_Escala_Rotacao.fbx")

# K5 — Modificador Array exportado sem aplicar: chega só 1 de 3 caixotes (cenário 8)
k5 = caixote("K5_Modificador", 12)
arr = k5.modifiers.new("Array", "ARRAY")
arr.count = 3
exportar(k5, "K5_Modificador.fbx", aplicar_modificadores=False)

# K6 — Duas camadas de UV, com a de lightmap em primeiro lugar (cenário 7)
k6 = caixote("K6_Duas_UV", 15)
k6.data.uv_layers.new(name="UVMap_Textura_Copia")  # cópia do UV bom (fica em 2º)
k6.data.uv_layers.active_index = 0
bpy.context.view_layer.objects.active = k6
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.uv.lightmap_pack(PREF_CONTEXT="ALL_FACES", PREF_MARGIN_DIV=0.2)
bpy.ops.object.mode_set(mode="OBJECT")
k6.data.uv_layers[0].name = "Lightmap"
exportar(k6, "K6_Duas_UV.fbx")

print("Kit gerado em:", OUT)
