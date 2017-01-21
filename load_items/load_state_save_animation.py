import os
from paraview.simple import *

home_path = '/home/nebula/work/paraview'
state_file_path = os.path.join(home_path, 'sb_simulation20170120.pvsm')
animation_dir_path = os.path.join('Movies', 'test_pvbatch_ospray20170121')

def set_ospray(renderview):
    renderview.Shadows = 1
    renderview.AmbientSamples = 1
    renderview.SamplesPerPixel = 2
    renderview.LightScale = 3.0
    renderview.EnableOSPRay = 1


servermanager.LoadState(state_file_path)
# paraview.simple._DisableFirstRenderCameraReset()

SetActiveView(GetRenderView())
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.ViewSize = [1920, 1080]
set_ospray(renderView1)
Render()

animationScene1 = GetAnimationScene()
animationScene1.StartTime = 100.0

animation_file_path = os.path.join(home_path, animation_dir_path, 'frame100.png')
WriteAnimation(animation_file_path, Magnification=1, FrameRate=15.0, Compression=True)

'''
# Setup the rendering parameters
scene.NumberOfFrames=1000
view.ViewSize = [1920,1080]
view.StereoRender = 1
view.StereoType = "Left"
view.UseOffscreenRendering = 1
WriteAnimation("animationC_L.png")
view.StereoType = "Right"
view.UseOffscreenRendering = 1
WriteAnimation("animationC_R.png")
'''
