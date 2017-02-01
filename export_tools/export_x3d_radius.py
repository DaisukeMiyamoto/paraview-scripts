from paraview.simple import *

def export_x3d_radius(filename):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'Legacy VTK Reader'
    a0004_registvtk = LegacyVTKReader(FileNames=['/home/nebula/work/paraview/standardbrain20170131/' + filename + '.vtk'])

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1778, 1128]

    # get color transfer function/color map for 'data'
    dataLUT = GetColorTransferFunction('data')

    # show data in view
    a0004_registvtkDisplay = Show(a0004_registvtk, renderView1)
    # trace defaults for the display properties.
    a0004_registvtkDisplay.ColorArrayName = ['CELLS', 'data']
    a0004_registvtkDisplay.LookupTable = dataLUT
    a0004_registvtkDisplay.OSPRayScaleArray = 'data'
    a0004_registvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    a0004_registvtkDisplay.SelectOrientationVectors = 'None'
    a0004_registvtkDisplay.ScaleFactor = 25.386285400390626
    a0004_registvtkDisplay.SelectScaleArray = 'data'
    a0004_registvtkDisplay.GlyphType = 'Arrow'
    a0004_registvtkDisplay.ScalarOpacityUnitDistance = 8.491697285811899
    a0004_registvtkDisplay.GaussianRadius = 12.693142700195313
    a0004_registvtkDisplay.SetScaleArray = [None, '']
    a0004_registvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    a0004_registvtkDisplay.OpacityArray = [None, '']
    a0004_registvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

    # reset view to fit data
    renderView1.ResetCamera()

    # show color bar/color legend
    a0004_registvtkDisplay.SetScalarBarVisibility(renderView1, True)

    # get opacity transfer function/opacity map for 'data'
    dataPWF = GetOpacityTransferFunction('data')

    # set scalar coloring
    ColorBy(a0004_registvtkDisplay, ('CELLS', 'radius'))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(dataLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    a0004_registvtkDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    a0004_registvtkDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'radius'
    radiusLUT = GetColorTransferFunction('radius')

    # get opacity transfer function/opacity map for 'radius'
    radiusPWF = GetOpacityTransferFunction('radius')

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    radiusLUT.ApplyPreset('rainbow', True)

    # Rescale transfer function
    radiusLUT.RescaleTransferFunction(0.0, 8.0)

    # Rescale transfer function
    radiusPWF.RescaleTransferFunction(0.0, 8.0)

    # create a new 'Extract Surface'
    extractSurface1 = ExtractSurface(Input=a0004_registvtk)

    # show data in view
    extractSurface1Display = Show(extractSurface1, renderView1)
    # trace defaults for the display properties.
    extractSurface1Display.ColorArrayName = ['CELLS', 'data']
    extractSurface1Display.LookupTable = dataLUT
    extractSurface1Display.OSPRayScaleArray = 'data'
    extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    extractSurface1Display.SelectOrientationVectors = 'None'
    extractSurface1Display.ScaleFactor = 25.386285400390626
    extractSurface1Display.SelectScaleArray = 'data'
    extractSurface1Display.GlyphType = 'Arrow'
    extractSurface1Display.GaussianRadius = 12.693142700195313
    extractSurface1Display.SetScaleArray = [None, '']
    extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
    extractSurface1Display.OpacityArray = [None, '']
    extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(a0004_registvtk, renderView1)

    # show color bar/color legend
    extractSurface1Display.SetScalarBarVisibility(renderView1, True)

    # create a new 'Generate Surface Normals'
    generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface1)

    # Properties modified on generateSurfaceNormals1
    generateSurfaceNormals1.FeatureAngle = 115.2

    # show data in view
    generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1)
    # trace defaults for the display properties.
    generateSurfaceNormals1Display.ColorArrayName = ['CELLS', 'data']
    generateSurfaceNormals1Display.LookupTable = dataLUT
    generateSurfaceNormals1Display.OSPRayScaleArray = 'data'
    generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    generateSurfaceNormals1Display.SelectOrientationVectors = 'None'
    generateSurfaceNormals1Display.ScaleFactor = 25.386285400390626
    generateSurfaceNormals1Display.SelectScaleArray = 'data'
    generateSurfaceNormals1Display.GlyphType = 'Arrow'
    generateSurfaceNormals1Display.GaussianRadius = 12.693142700195313
    generateSurfaceNormals1Display.SetScaleArray = [None, '']
    generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
    generateSurfaceNormals1Display.OpacityArray = [None, '']
    generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # hide data in view
    Hide(extractSurface1, renderView1)

    # show color bar/color legend
    generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

    # set scalar coloring
    ColorBy(generateSurfaceNormals1Display, ('CELLS', 'radius'))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(dataLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    generateSurfaceNormals1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

    # export view
    ExportView('/home/nebula/work/blender/x3d/standardbrain20170131/' + filename + '.x3d', view=renderView1)
