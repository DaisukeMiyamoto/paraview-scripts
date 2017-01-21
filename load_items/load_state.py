import os
from paraview.simple import *

home_path = '/home/nebula/work/paraview'
state_file_path = os.path.join(home_path, 'sb_simulation20170120.pvsm')

screenshot_file_path = os.path.join(home_path, 'tmp2.png')
servermanager.LoadState(state_file_path)

SetActiveView(GetRenderView())
# Render()

renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.ViewSize = [1920, 1080]
layout1 = GetLayout()

SaveScreenshot(screenshot_file_path, layout=layout1, magnification=1, quality=100)
