import os
import sys
from paraview.simple import *


def set_ospray(renderview):
    renderview.Shadows = 1
    renderview.AmbientSamples = 1
    renderview.SamplesPerPixel = 2
    renderview.LightScale = 1.8
    renderview.EnableOSPRay = 1


def make_animation(start=0, steps=10):
    home_path = '/home/nebula/work/paraview'
    state_file_path = os.path.join(home_path, 'standardbrain20170125.pvsm')
    animation_dir_path = os.path.join(home_path, 'Movies', 'standardbrain20170125')

    if not os.path.isdir(animation_dir_path):
        os.mkdir(animation_dir_path)

    servermanager.LoadState(state_file_path)

    SetActiveView(GetRenderView())
    renderView1 = GetActiveViewOrCreate('RenderView')
    renderView1.ViewSize = [1000, 1000]
    set_ospray(renderView1)
    Render()

    animationScene1 = GetAnimationScene()

    screenshot_file_path = os.path.join(animation_dir_path, 'frame.%04d.png')
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
    steps = 10
    if len(sys.argv) >= 2:
        start_time = int(sys.argv[1])
    if len(sys.argv) >= 3:
        steps = int(sys.argv[2])

    make_animation(start=start_time, steps=steps)

