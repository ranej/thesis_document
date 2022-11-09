# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


CP1 = 0.2799780773364582 
CP2 = 0.038769412061300745
CP3 = 10000.1
CF1 = 0.2799780773364582
CF2 = 0.038769412061300745
CF3 = 0.1
CPS = 0.5762038068561304


#M0
for phase_iter in range(180,345,15):

	# create a new 'Legacy VTK Reader'
	vtk_file = LegacyVTKReader(FileNames=['C:\\Users\\spook\\Desktop\\Mv2\\highRe\\M0\\spavg_files\\M0_sliced_spavg_cycle2_'+str(phase_iter)+'.vtk'])

	# get active view
	renderView1 = GetActiveViewOrCreate('RenderView')
	# uncomment following to set a specific view size
	# renderView1.ViewSize = [1404, 775]

	# get layout
	layout1 = GetLayout()

	# show data in view
	vtk_fileDisplay = Show(vtk_file, renderView1, 'GeometryRepresentation')

	# get color transfer function/color map for 'Result'
	resultLUT = GetColorTransferFunction('Result')

	# trace defaults for the display properties.
	vtk_fileDisplay.Representation = 'Surface'
	vtk_fileDisplay.ColorArrayName = ['POINTS', 'Result']
	vtk_fileDisplay.LookupTable = resultLUT
	vtk_fileDisplay.OSPRayScaleArray = 'Result'
	vtk_fileDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	vtk_fileDisplay.SelectOrientationVectors = 'Gradients'
	vtk_fileDisplay.ScaleFactor = 10.0
	vtk_fileDisplay.SelectScaleArray = 'Result'
	vtk_fileDisplay.GlyphType = 'Arrow'
	vtk_fileDisplay.GlyphTableIndexArray = 'Result'
	vtk_fileDisplay.GaussianRadius = 0.5
	vtk_fileDisplay.SetScaleArray = ['POINTS', 'Result']
	vtk_fileDisplay.ScaleTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.OpacityArray = ['POINTS', 'Result']
	vtk_fileDisplay.OpacityTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.DataAxesGrid = 'GridAxesRepresentation'
	vtk_fileDisplay.PolarAxes = 'PolarAxesRepresentation'

	# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
	vtk_fileDisplay.ScaleTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
	vtk_fileDisplay.OpacityTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# reset view to fit data
	renderView1.ResetCamera()

	#changing interaction mode based on data extents
	renderView1.CameraPosition = [0.0, 0.0, 10000.1]
	renderView1.CameraFocalPoint = [0.0, 0.0, 0.1]

	# get the material library
	materialLibrary1 = GetMaterialLibrary()

	# show color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, True)

	# update the view to ensure updated data information
	renderView1.Update()

	# get opacity transfer function/opacity map for 'Result'
	resultPWF = GetOpacityTransferFunction('Result')

	# hide color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, False)

	# Show orientation axes
	renderView1.OrientationAxesVisibility = 1

	# Hide orientation axes
	renderView1.OrientationAxesVisibility = 0

	# Properties modified on renderView1
	renderView1.Background = [0.0, 0.0, 0.0]

	# Properties modified on renderView1
	renderView1.Background = [1.0, 1.0, 1.0]

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# current camera placement for renderView1
# current camera placement for renderView1
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CP1, CP2, CP3]
	renderView1.CameraFocalPoint = [CF1, CF2, CF3]
	renderView1.CameraParallelScale = CPS
	# save screenshot
	SaveScreenshot('C:\\Users\\spook\\Desktop\\Mv2\\highRe\\vorticity_plots\\M0\\phase_'+str(phase_iter)+'.png', renderView1, ImageResolution=[1404, 775])

	Delete(vtk_file)
	del vtk_file
	

#Mza1_50
	
for phase_iter in range(180,345,15):

	# create a new 'Legacy VTK Reader'
	vtk_file = LegacyVTKReader(FileNames=['C:\\Users\\spook\\Desktop\\Mv2\\highRe\\Mza1_50\\spavg_files\\Mza1_50_sliced_spavg_cycle2_'+str(phase_iter)+'.vtk'])

	# get active view
	renderView1 = GetActiveViewOrCreate('RenderView')
	# uncomment following to set a specific view size
	# renderView1.ViewSize = [1404, 775]

	# get layout
	layout1 = GetLayout()

	# show data in view
	vtk_fileDisplay = Show(vtk_file, renderView1, 'GeometryRepresentation')

	# get color transfer function/color map for 'Result'
	resultLUT = GetColorTransferFunction('Result')

	# trace defaults for the display properties.
	vtk_fileDisplay.Representation = 'Surface'
	vtk_fileDisplay.ColorArrayName = ['POINTS', 'Result']
	vtk_fileDisplay.LookupTable = resultLUT
	vtk_fileDisplay.OSPRayScaleArray = 'Result'
	vtk_fileDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	vtk_fileDisplay.SelectOrientationVectors = 'Gradients'
	vtk_fileDisplay.ScaleFactor = 10.0
	vtk_fileDisplay.SelectScaleArray = 'Result'
	vtk_fileDisplay.GlyphType = 'Arrow'
	vtk_fileDisplay.GlyphTableIndexArray = 'Result'
	vtk_fileDisplay.GaussianRadius = 0.5
	vtk_fileDisplay.SetScaleArray = ['POINTS', 'Result']
	vtk_fileDisplay.ScaleTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.OpacityArray = ['POINTS', 'Result']
	vtk_fileDisplay.OpacityTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.DataAxesGrid = 'GridAxesRepresentation'
	vtk_fileDisplay.PolarAxes = 'PolarAxesRepresentation'

	# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
	vtk_fileDisplay.ScaleTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
	vtk_fileDisplay.OpacityTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# reset view to fit data
	renderView1.ResetCamera()

	#changing interaction mode based on data extents
	renderView1.CameraPosition = [0.0, 0.0, 10000.1]
	renderView1.CameraFocalPoint = [0.0, 0.0, 0.1]

	# get the material library
	materialLibrary1 = GetMaterialLibrary()

	# show color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, True)

	# update the view to ensure updated data information
	renderView1.Update()

	# get opacity transfer function/opacity map for 'Result'
	resultPWF = GetOpacityTransferFunction('Result')

	# hide color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, False)

	# Show orientation axes
	renderView1.OrientationAxesVisibility = 1

	# Hide orientation axes
	renderView1.OrientationAxesVisibility = 0

	# Properties modified on renderView1
	renderView1.Background = [0.0, 0.0, 0.0]

	# Properties modified on renderView1
	renderView1.Background = [1.0, 1.0, 1.0]

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# current camera placement for renderView1
# current camera placement for renderView1
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CP1, CP2, CP3]
	renderView1.CameraFocalPoint = [CF1, CF2, CF3]
	renderView1.CameraParallelScale = CPS
	# save screenshot
	SaveScreenshot('C:\\Users\\spook\\Desktop\\Mv2\\highRe\\vorticity_plots\\Mza1_50\\phase_'+str(phase_iter)+'.png', renderView1, ImageResolution=[1404, 775])

	Delete(vtk_file)
	del vtk_file


#Mza2_100

for phase_iter in range(180,345,15):

	# create a new 'Legacy VTK Reader'
	vtk_file = LegacyVTKReader(FileNames=['C:\\Users\\spook\\Desktop\\Mv2\\highRe\\Mza1_100\\spavg_files\\Mza1_100_sliced_spavg_cycle2_'+str(phase_iter)+'.vtk'])

	# get active view
	renderView1 = GetActiveViewOrCreate('RenderView')
	# uncomment following to set a specific view size
	# renderView1.ViewSize = [1404, 775]

	# get layout
	layout1 = GetLayout()

	# show data in view
	vtk_fileDisplay = Show(vtk_file, renderView1, 'GeometryRepresentation')

	# get color transfer function/color map for 'Result'
	resultLUT = GetColorTransferFunction('Result')

	# trace defaults for the display properties.
	vtk_fileDisplay.Representation = 'Surface'
	vtk_fileDisplay.ColorArrayName = ['POINTS', 'Result']
	vtk_fileDisplay.LookupTable = resultLUT
	vtk_fileDisplay.OSPRayScaleArray = 'Result'
	vtk_fileDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	vtk_fileDisplay.SelectOrientationVectors = 'Gradients'
	vtk_fileDisplay.ScaleFactor = 10.0
	vtk_fileDisplay.SelectScaleArray = 'Result'
	vtk_fileDisplay.GlyphType = 'Arrow'
	vtk_fileDisplay.GlyphTableIndexArray = 'Result'
	vtk_fileDisplay.GaussianRadius = 0.5
	vtk_fileDisplay.SetScaleArray = ['POINTS', 'Result']
	vtk_fileDisplay.ScaleTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.OpacityArray = ['POINTS', 'Result']
	vtk_fileDisplay.OpacityTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.DataAxesGrid = 'GridAxesRepresentation'
	vtk_fileDisplay.PolarAxes = 'PolarAxesRepresentation'

	# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
	vtk_fileDisplay.ScaleTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
	vtk_fileDisplay.OpacityTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# reset view to fit data
	renderView1.ResetCamera()

	#changing interaction mode based on data extents
	renderView1.CameraPosition = [0.0, 0.0, 10000.1]
	renderView1.CameraFocalPoint = [0.0, 0.0, 0.1]

	# get the material library
	materialLibrary1 = GetMaterialLibrary()

	# show color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, True)

	# update the view to ensure updated data information
	renderView1.Update()

	# get opacity transfer function/opacity map for 'Result'
	resultPWF = GetOpacityTransferFunction('Result')

	# hide color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, False)

	# Show orientation axes
	renderView1.OrientationAxesVisibility = 1

	# Hide orientation axes
	renderView1.OrientationAxesVisibility = 0

	# Properties modified on renderView1
	renderView1.Background = [0.0, 0.0, 0.0]

	# Properties modified on renderView1
	renderView1.Background = [1.0, 1.0, 1.0]

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# current camera placement for renderView1
# current camera placement for renderView1
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CP1, CP2, CP3]
	renderView1.CameraFocalPoint = [CF1, CF2, CF3]
	renderView1.CameraParallelScale = CPS
	# save screenshot
	SaveScreenshot('C:\\Users\\spook\\Desktop\\Mv2\\highRe\\vorticity_plots\\Mza1_100\\phase_'+str(phase_iter)+'.png', renderView1, ImageResolution=[1404, 775])

	Delete(vtk_file)
	del vtk_file
	
	#Mza2_100

for phase_iter in range(180,345,15):

	# create a new 'Legacy VTK Reader'
	vtk_file = LegacyVTKReader(FileNames=['C:\\Users\\spook\\Desktop\\Mv2\\highRe\\Mza2_50\\spavg_files\\Mza2_50_sliced_spavg_cycle2_'+str(phase_iter)+'.vtk'])

	# get active view
	renderView1 = GetActiveViewOrCreate('RenderView')
	# uncomment following to set a specific view size
	# renderView1.ViewSize = [1404, 775]

	# get layout
	layout1 = GetLayout()

	# show data in view
	vtk_fileDisplay = Show(vtk_file, renderView1, 'GeometryRepresentation')

	# get color transfer function/color map for 'Result'
	resultLUT = GetColorTransferFunction('Result')

	# trace defaults for the display properties.
	vtk_fileDisplay.Representation = 'Surface'
	vtk_fileDisplay.ColorArrayName = ['POINTS', 'Result']
	vtk_fileDisplay.LookupTable = resultLUT
	vtk_fileDisplay.OSPRayScaleArray = 'Result'
	vtk_fileDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	vtk_fileDisplay.SelectOrientationVectors = 'Gradients'
	vtk_fileDisplay.ScaleFactor = 10.0
	vtk_fileDisplay.SelectScaleArray = 'Result'
	vtk_fileDisplay.GlyphType = 'Arrow'
	vtk_fileDisplay.GlyphTableIndexArray = 'Result'
	vtk_fileDisplay.GaussianRadius = 0.5
	vtk_fileDisplay.SetScaleArray = ['POINTS', 'Result']
	vtk_fileDisplay.ScaleTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.OpacityArray = ['POINTS', 'Result']
	vtk_fileDisplay.OpacityTransferFunction = 'PiecewiseFunction'
	vtk_fileDisplay.DataAxesGrid = 'GridAxesRepresentation'
	vtk_fileDisplay.PolarAxes = 'PolarAxesRepresentation'

	# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
	vtk_fileDisplay.ScaleTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
	vtk_fileDisplay.OpacityTransferFunction.Points = [-3192.4517419450212, 0.0, 0.5, 0.0, 650.374252512619, 1.0, 0.5, 0.0]

	# reset view to fit data
	renderView1.ResetCamera()

	#changing interaction mode based on data extents
	renderView1.CameraPosition = [0.0, 0.0, 10000.1]
	renderView1.CameraFocalPoint = [0.0, 0.0, 0.1]

	# get the material library
	materialLibrary1 = GetMaterialLibrary()

	# show color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, True)

	# update the view to ensure updated data information
	renderView1.Update()

	# get opacity transfer function/opacity map for 'Result'
	resultPWF = GetOpacityTransferFunction('Result')

	# hide color bar/color legend
	vtk_fileDisplay.SetScalarBarVisibility(renderView1, False)

	# Show orientation axes
	renderView1.OrientationAxesVisibility = 1

	# Hide orientation axes
	renderView1.OrientationAxesVisibility = 0

	# Properties modified on renderView1
	renderView1.Background = [0.0, 0.0, 0.0]

	# Properties modified on renderView1
	renderView1.Background = [1.0, 1.0, 1.0]

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultLUT.RescaleTransferFunction(-10.0, 10.0)

	# Rescale transfer function
	resultPWF.RescaleTransferFunction(-10.0, 10.0)

	# current camera placement for renderView1
# current camera placement for renderView1
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CP1, CP2, CP3]
	renderView1.CameraFocalPoint = [CF1, CF2, CF3]
	renderView1.CameraParallelScale = CPS
	# save screenshot
	SaveScreenshot('C:\\Users\\spook\\Desktop\\Mv2\\highRe\\vorticity_plots\\Mza2_50\\phase_'+str(phase_iter)+'.png', renderView1, ImageResolution=[1404, 775])

	Delete(vtk_file)
	del vtk_file
	