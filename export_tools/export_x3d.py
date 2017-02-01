import sys
import export_x3d_radius
import export_x3d_colored
from matplotlib import cm
import random


if not len(sys.argv) == 2:
    print('direct VTK filename (without .vtk)')
    quit()

filename = sys.argv[1]

cmap = cm.get_cmap('rainbow')
neuron_color = cmap(random.random())

export_x3d_colored.export_x3d_colored(filename, neuron_color)

