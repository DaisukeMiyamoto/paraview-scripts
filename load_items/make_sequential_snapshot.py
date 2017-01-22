import os
import sys
from paraview.simple import *


def set_ospray(renderview):
    renderview.Shadows = 1
    renderview.AmbientSamples = 1
    renderview.SamplesPerPixel = 2
    renderview.LightScale = 3.0
    renderview.EnableOSPRay = 1


def make_animation(start=0, steps=10):
    home_path = '/home/nebula/work/paraview'
    state_file_path = os.path.join(home_path, 'sb_simulation_rot_20170122.pvsm')
    animation_dir_path = os.path.join('Movies', 'test_pvbatch_ospray_rot_4k_20170122')

    servermanager.LoadState(state_file_path)
    # paraview.simple._DisableFirstRenderCameraReset()

    SetActiveView(GetRenderView())
    renderView1 = GetActiveViewOrCreate('RenderView')
    renderView1.ViewSize = [4000, 4000]
    set_ospray(renderView1)
    Render()

    animationScene1 = GetAnimationScene()

    screenshot_file_path = os.path.join(home_path, animation_dir_path, 'frame.%04d.png')
    for i in range(start, start + steps):
        print('Processing: ' + (screenshot_file_path % i))
        # animationScene1.StartTime = i
        animationScene1.AnimationTime = i
        # renderView1.ViewTime = i
        # Render()
        SaveScreenshot(screenshot_file_path % i, magnification=1, quality=100)


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


if __name__ == '__main__':
    start_time = 0
    if len(sys.argv) == 2:
        start_time = int(sys.argv[1])

    make_animation(start=start_time)


