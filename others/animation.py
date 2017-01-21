from paraview.simple import *

# Properties modified on renderView1
# renderView1.EnableOSPRay = 1

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [960, 540]

# current camera placement for renderView1
renderView1.CameraPosition = [511.999992370605, 481.263313293457, 1715.96537027743]
renderView1.CameraFocalPoint = [511.999992370605, 481.263313293457, 161.693189620972]
renderView1.CameraViewUp = [4.44089209850063e-16, -1.0, 0.0]
renderView1.CameraParallelScale = 402.275241626917

# current camera placement for renderView1
renderView1.CameraPosition = [511.999992370605, 481.263313293457, 1715.96537027743]
renderView1.CameraFocalPoint = [511.999992370605, 481.263313293457, 161.693189620972]
renderView1.CameraViewUp = [4.44089209850063e-16, -1.0, 0.0]
renderView1.CameraParallelScale = 402.275241626917

# save animation images/movie
path = 'path to dir'
WriteAnimation('frame.png', Magnification=2, FrameRate=15.0, Compression=True)

