#########################################################################
#  Assumptions
#  1. data size and image size are of the same ratio
#########################################################################

sateliteImageSizeX = 1350.0
sateliteImageSizeY = 675.0
# dataSizeX range is from 0 to 360
dataSizeX = 360.0
# dataSizeY range is from -90 to 90
dataSizeY = 180.0
imageToDataRatio = sateliteImageSizeX / dataSizeX
imageToDataScale = 1 / imageToDataRatio

minLon = 190
minLon = 10
maxLon = 260
minLat = 25
minLat = -15
maxLat = 70
minPressure = 150
maxPressure = 1000


OpenDatabase("localhost:/local2/home/projects/gfdl/af-20110426/testtest/atmos.2010050900-2010051323.O3.nc", 0)
DefineScalarExpression("new_O3", "O3*1000000000")

AddPlot("Volume", "new_O3", 1, 0)
SetActivePlots(0)

AddOperator("Box", 0)
BoxAtts = BoxAttributes()
BoxAtts.amount = BoxAtts.Some  # Some, All
BoxAtts.minx = minLon
BoxAtts.maxx = maxLon
BoxAtts.miny = minLat
BoxAtts.maxy = maxLat
BoxAtts.minz = minPressure
BoxAtts.maxz = maxPressure
SetOperatorOptions(BoxAtts, 0)

AddOperator("Transform", 0)
TransformAtts = TransformAttributes()
TransformAtts.doScale = 1
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = -0.1
SetOperatorOptions(TransformAtts, 0)

VolumeAtts = VolumeAttributes()
VolumeAtts.legendFlag = 1
VolumeAtts.lightingFlag = 1
VolumeAtts.colorControlPoints.GetControlPoints(0).colors = (0, 0, 255, 255)
VolumeAtts.colorControlPoints.GetControlPoints(0).position = 0
VolumeAtts.colorControlPoints.GetControlPoints(1).colors = (0, 255, 255, 255)
VolumeAtts.colorControlPoints.GetControlPoints(1).position = 0.25
VolumeAtts.colorControlPoints.GetControlPoints(2).colors = (0, 255, 0, 255)
VolumeAtts.colorControlPoints.GetControlPoints(2).position = 0.5
VolumeAtts.colorControlPoints.GetControlPoints(3).colors = (255, 255, 0, 255)
VolumeAtts.colorControlPoints.GetControlPoints(3).position = 0.75
VolumeAtts.colorControlPoints.GetControlPoints(4).colors = (255, 0, 0, 255)
VolumeAtts.colorControlPoints.GetControlPoints(4).position = 1
VolumeAtts.colorControlPoints.smoothingFlag = 1
VolumeAtts.colorControlPoints.equalSpacingFlag = 0
VolumeAtts.colorControlPoints.discreteFlag = 0
VolumeAtts.colorControlPoints.externalFlag = 0
VolumeAtts.opacityAttenuation = 1
VolumeAtts.opacityMode = VolumeAtts.FreeformMode  # FreeformMode, GaussianMode, ColorTableMode
#controlPoints does not contain any GaussianControlPoint objects.
VolumeAtts.resampleTarget = 50000
VolumeAtts.opacityVariable = "default"
VolumeAtts.freeformOpacity = (0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 23, 23, 23, 23, 23, 23, 23, 23, 23, 26, 26, 26, 26, 29, 29, 29, 29, 29, 29, 29, 29, 32, 32, 32, 35, 35, 38, 38, 38, 38, 41, 41, 41, 44, 44, 44, 44, 44, 47, 47, 47, 47, 47, 50, 50, 50, 50, 50, 50, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 56, 56, 56, 59, 59, 59, 62, 62, 65, 65, 68, 68, 71, 71, 74, 74, 74, 77, 77, 77, 80, 80, 80, 83, 83, 85, 85, 85, 85, 88, 88, 88, 91, 91, 94, 97, 97, 97, 100, 100, 100, 103, 103, 103, 103, 103, 106, 106, 106, 109, 109, 112, 112, 112, 115, 115, 115, 118, 121, 121, 124, 124, 130, 130, 133, 136, 136, 139, 139, 142, 142, 145, 148, 148, 151, 154, 154, 157, 160, 163, 163, 166, 166, 169, 171, 171, 174, 177, 180, 183, 183, 186, 186, 186, 189, 189, 189, 189, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254)
VolumeAtts.useColorVarMin = 1
VolumeAtts.colorVarMin = 70
VolumeAtts.useColorVarMax = 1
VolumeAtts.colorVarMax = 120
VolumeAtts.useOpacityVarMin = 0
VolumeAtts.opacityVarMin = 0
VolumeAtts.useOpacityVarMax = 0
VolumeAtts.opacityVarMax = 0
VolumeAtts.smoothData = 0
VolumeAtts.samplesPerRay = 500
VolumeAtts.rendererType = VolumeAtts.RayCasting  # Splatting, Texture3D, RayCasting, RayCastingIntegration, SLIVR, Tuvok
VolumeAtts.gradientType = VolumeAtts.SobelOperator  # CenteredDifferences, SobelOperator
VolumeAtts.num3DSlices = 200
VolumeAtts.scaling = VolumeAtts.Linear  # Linear, Log, Skew
VolumeAtts.skewFactor = 15
VolumeAtts.limitsMode = VolumeAtts.OriginalData  # OriginalData, CurrentPlot
VolumeAtts.sampling = VolumeAtts.Rasterization  # KernelBased, Rasterization
VolumeAtts.rendererSamples = 3
#transferFunction2DWidgets does not contain any TransferFunctionWidget objects.
VolumeAtts.transferFunctionDim = 1
VolumeAtts.lowGradientLightingReduction = VolumeAtts.Lower  # Off, Lowest, Lower, Low, Medium, High, Higher, Highest
VolumeAtts.lowGradientLightingClampFlag = 0
VolumeAtts.lowGradientLightingClampValue = 1
SetPlotOptions(VolumeAtts)

OpenDatabase("localhost:/local2/home/projects/gfdl/af-20110426/testtest/satellite_image_height.vtk", 0)
AddPlot("Truecolor", "color", 1, 0)
SetActivePlots(1)

AddOperator("Box", 0)
BoxAtts = BoxAttributes()
BoxAtts.amount = BoxAtts.Some  # Some, All
BoxAtts.minx = minLon * imageToDataRatio
BoxAtts.maxx = maxLon * imageToDataRatio
if (minLat < 0):
  BoxAtts.miny = (minLat * -1) * imageToDataRatio
else:
  BoxAtts.miny = (minLat + 90) * imageToDataRatio
if (maxLat < 0):
  BoxAtts.maxy = (maxLat * -1) * imageToDataRatio
else:
  BoxAtts.maxy = (maxLat + 90) * imageToDataRatio
BoxAtts.minz = 1.1625
BoxAtts.maxz = 32.85
SetOperatorOptions(BoxAtts, 0)

AddOperator("Transform", 0)
TransformAtts = TransformAttributes()
TransformAtts.doScale = 1
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = imageToDataScale
TransformAtts.scaleY = imageToDataScale
TransformAtts.scaleZ = imageToDataScale
TransformAtts.doTranslate = 1
TransformAtts.translateX = 0
TransformAtts.translateY = -89.75
TransformAtts.translateZ = -100
SetOperatorOptions(TransformAtts, 0)

v = GetView3D()
v.viewNormal = (-0.724234, -0.684734, 0.081394)
v.focus = (225, 47.5, -56.0379)
v.viewUp = (0.0584616, 0.056641, 0.996682)
v.viewAngle = 30
v.parallelScale = 60.5448
v.nearPlane = -121.09
v.farPlane = 121.09
v.imagePan = (0.0596107, 0.00181653)
v.imageZoom = 1.00548
SetView3D(v)

AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.OutsideEdges  # ClosestTriad, FurthestTriad, , StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 0
AnnotationAtts.axes3D.xAxis.label.visible = 0
AnnotationAtts.axes3D.yAxis.title.visible = 0
AnnotationAtts.axes3D.yAxis.label.visible = 0
AnnotationAtts.axes3D.zAxis.title.visible = 0
AnnotationAtts.axes3D.zAxis.label.visible = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
SetAnnotationAttributes(AnnotationAtts)

InvertBackgroundColor()

for i in range(TimeSliderGetNStates()):
  if (i == 31):
    TimeSliderSetState(i)
    sw = SaveWindowAttributes()
    sw.family = 0
    sw.resConstraint = 1
    sw.height=1080
    sw.width=1480
    sw.fileName = "filename_%03d" %(i)
    SetSaveWindowAttributes(sw)
    DrawPlots()
    SaveWindow()

exit()
