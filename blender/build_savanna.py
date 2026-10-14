"""RunAdventures: no-cost Blender 3D blocking scene (NOT final AAA art).
Run: blender -b -t 2 --python blender/build_savanna.py
Requires Blender 4.x and no external libraries/assets.
Creates output/savanna_preview.png (single still) and output/savanna_scene.blend.
"""
import bpy, math, os, random
from mathutils import Vector
random.seed(87)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=16
scene.render.resolution_x=960
scene.render.resolution_y=540
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.world.color=(0.3,0.4,0.6)
def mat(name,color,rough=0.85):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*color,1);bs.inputs['Roughness'].default_value=rough
 return m
ground=mat('Dry ochre earth',(.48,.29,.12))
grass=mat('Savanna golden grass',(.42,.33,.11))
trunk=mat('Acacia dark wood',(.12,.082,.04))
leaves=mat('Acacia canopy',(.16,.24,.065))
rock=mat('Rock',(.27,.22,.16))
path=mat('Sandy running trail',(.58,.4,.23))
def cube(name,loc,scale,material):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name
 o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(material);return o
cube('terrain',(0,22,-.27),(100,110,.5),ground)
cube('safe visible running path',(0,21,.015),(3.5,105,.035),path)
for i in range(65):
 x=random.uniform(-40,40);y=random.uniform(2,75)
 if abs(x)<3.1:continue
 z=random.uniform(.28,.65);cube('low grass patch',(x,y,z/2),(.4,.6,z),grass)
for i in range(17):
 x=random.choice([-1,1])*random.uniform(6,32);y=random.uniform(8,85)
 h=random.uniform(3,6)
 bpy.ops.mesh.primitive_cylinder_add(vertices=8,radius=.22,depth=h,location=(x,y,h/2))
 o=bpy.context.object;o.name='Acacia trunk';o.data.materials.append(trunk)
 bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=6,location=(x,y,h))
 o=bpy.context.object;o.name='Acacia foliage';o.scale=(random.uniform(2.5,4),random.uniform(2,3.5),.6);o.data.materials.append(leaves)
for i in range(15):
 x=random.choice([-1,1])*random.uniform(6,38);y=random.uniform(18,90)
 bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=random.uniform(1,4),location=(x,y,.3))
 bpy.context.object.name='Distant rock';bpy.context.object.data.materials.append(rock)
bpy.ops.object.camera_add(location=(0,-7,1.7))
cam=bpy.context.object;direction=Vector((0,30,1.3))-cam.location
cam.rotation_euler=direction.to_track_quat('-Z','Y').to_euler();cam.data.lens=24
scene.camera=cam
bpy.ops.object.light_add(type='SUN',location=(0,0,20));bpy.context.object.rotation_euler=(math.radians(35),math.radians(-20),math.radians(25));bpy.context.object.data.energy=3
scene.view_settings.view_transform='AgX'
os.makedirs('output',exist_ok=True)
scene.render.filepath=os.path.abspath('output/savanna_preview.png')
bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath('output/savanna_scene.blend'))
bpy.ops.render.render(write_still=True)
print('Generated basic 3D blocking still; no lion, hyena, animation or AAA claim.')
