#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

filepos = '/home/nebula/work/paraview/standardbrain20170107/'

filelist_small = [
    '0004_regist',
    '0005_regist',
    '0008_regist'
]

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



filelist = filelist_all

readers = []
displays = []
renderview = GetActiveViewOrCreate('RenderView')

for filename in filelist:
    reader = LegacyVTKReader(FileNames=[filepos + filename + '.vtk'])
    # fixvalLUT = GetColorTransferFunction('fixval')
    display = Show(reader, renderview)
    # display.ColorArrayName = ['CELLS', 'fixval']
    # display.LookupTable = fixvalLUT
    ColorBy(display, None)
    display.DiffuseColor = [0.0, 1.0, 0.0]
    #display.LookupTable = MakeBlueToRedLT(0, 256)

    renderview.ResetCamera()
    Render()

    readers.append(reader)
    displays.append(display)



