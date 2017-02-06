"""
$ ./bin/blender-2.78a-linux-glibc211-x86_64/blender --background --python ~/git/paraview-scripts/blender/import_x3d_3.py
$ ./bin/blender-2.78a-linux-glibc211-x86_64/blender --background ~/work/blender/test.blend -o ./test.png -f 1
"""
import bpy
import sys
import math


def apply_decimate(obj):
    print('Faces: %d' % len(obj.data.polygons))

    mod = obj.modifiers.new(name='decimate1', type='DECIMATE')
    mod.decimate_type = 'DISSOLVE'
    mod.angle_limit = math.radians(15)
    bpy.context.scene.objects.active = obj
    bpy.ops.object.modifier_apply(modifier='decimate1', apply_as='DATA')
    print('Faces (DISSOLVE): %d' % len(obj.data.polygons))

    mod = obj.modifiers.new(name='decimate2', type='DECIMATE')
    mod.decimate_type = 'COLLAPSE'
    mod.ratio = 0.4
    bpy.context.scene.objects.active = obj
    bpy.ops.object.modifier_apply(modifier='decimate2', apply_as='DATA')
    print('Faces (COLLAPSE): %d' % len(obj.data.polygons))



argv = sys.argv
argv = argv[argv.index("--") + 1:]
if not len(argv) == 1:
    print('Error: save filename')
    quit()


neuron = argv[0]

print('Processing %s' % neuron)
bpy.ops.import_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain20170201/' + neuron + '.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='Y')

bpy.ops.object.select_all(action='TOGGLE')

for ob in bpy.data.objects:
    if not ('Shape_IndexedFaceSet' in ob.name or 'Base' in ob.name):
        ob.select = True
        bpy.ops.object.delete()

bpy.ops.object.select_all(action='TOGGLE')


ob = bpy.data.objects['Shape_IndexedFaceSet']

ob.select = True
#ob.name = neuron
ob.scale = (0.01, 0.01, 0.01)
ob.location = (-5.12, -1.6, 4.5)
ob.rotation_euler[1] = math.radians(180)
apply_decimate(ob)

# print('Polygons: %d' % len(ob.data.polygons))

# bpy.ops.object.join()
bpy.ops.wm.save_as_mainfile(filepath='/home/nebula/work/blender/x3d/standardbrain_decimate20170205/' + neuron + '.blend')

# bpy.ops.export_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain_decimate20170205/' + neuron + '.x3d')
bpy.ops.export_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain_decimate20170205/' + neuron + '.x3d',
                         use_mesh_modifiers=True, use_normals=True,
                         use_selection=True, name_decorations=True)
print('Finished!')
