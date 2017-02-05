import sys
import export_x3d_radius
import export_x3d_colored
from matplotlib import cm
import random

if not len(sys.argv) >= 2:
    print('direct VTK filename (without .vtk)')
    quit()

input_filename = '/home/nebula/work/paraview/standardbrain20170131/' + sys.argv[1] + '.vtk'
output_filename = '/home/nebula/work/blender/x3d/standardbrain20170202/' + sys.argv[1] + '.x3d'

cmap = cm.get_cmap('jet')
if len(sys.argv) >= 4:
    neuron_color = cmap(float(sys.argv[2])/float(sys.argv[3]))
else:
    neuron_color = cmap(random.random())

print(neuron_color)
export_x3d_colored.export_x3d_colored(input_filename, output_filename, neuron_color)

