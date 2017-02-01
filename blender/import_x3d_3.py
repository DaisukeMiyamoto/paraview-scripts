"""
$ ./bin/blender-2.78a-linux-glibc211-x86_64/blender --background --python ~/git/paraview-scripts/blender/import_x3d_3.py
$ ./bin/blender-2.78a-linux-glibc211-x86_64/blender --background ~/work/blender/test.blend -o ./test.png -f 1
"""
import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]
if not len(argv) == 1:
    print('Error: save filename')
    quit()


filelist_all = [
    '0004_regist',
    '0005_regist',
    '0008_regist',
    '0009_regist',
    '0012_regist',
    '0017_regist',
    '0019_regist',
    '0021_regist',
    '0655_regist',
    '0661_regist',
    '0663_regist',
    '0664_regist',
    '0965_regist',
    '0966_regist',
    '0967_regist',
    '0969_regist',
    '0970_regist',
    '0973_regist',
    '0984_regist',
    '0986_regist',
    '0988_regist',
    '0993_regist',
    '1009_regist',
    '1020_regist',
    '1068_regist',
    '1080_regist',
    '090815_4_sn_reg'
]

filelist_simple = [
    '0004_regist',
]

# save_filepath = '/home/nebula/work/blender/test.blend'
save_filepath = argv[0]
base_filepath = '/home/nebula/work/blender/base_scene20170201.blend'

filelist = filelist_simple

print('Start importing!')
bpy.ops.wm.open_mainfile(filepath=base_filepath)

for neuron in filelist:
    print('Processing %s' % neuron)
    bpy.ops.import_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain20170201/' + neuron + '.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='-Y')
    bpy.ops.import_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain20170201/' + neuron + '_flip.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='-Y')

bpy.ops.object.select_all(action='TOGGLE')

for ob in bpy.data.objects:
    print(ob.name)
    if not ('Shape_IndexedFaceSet' in ob.name or 'Base' in ob.name):
        ob.select = True
        bpy.ops.object.delete()

bpy.ops.object.select_all(action='TOGGLE')

for ob in bpy.data.objects:
    print(ob.name)
    if 'Shape_IndexedFaceSet' in ob.name:
        ob.select = True
        ob.scale = (0.01, 0.01, 0.01)
        ob.location = (-5.12, -1.17, 7.81)
        ob.select = False

# bpy.ops.object.join()

bpy.ops.wm.save_as_mainfile(filepath=save_filepath)

print('Finished!')
