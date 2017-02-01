import bpy

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

for neuron in filelist_all:
    bpy.ops.import_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain20170201/' + neuron + '.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='-Y')
    bpy.ops.import_scene.x3d(filepath='/home/nebula/work/blender/x3d/standardbrain20170201/' + neuron + '_flip.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='-Y')
