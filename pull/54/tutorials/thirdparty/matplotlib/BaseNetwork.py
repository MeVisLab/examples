firstSlice = None
startSlice = None
lastSlice = None
endSlice = None
bins = None 
slices = None


def setDefaults():
  ctx.field("SubImage.fullSize").touch()
  ctx.field("SubImage.autoApply").value = True
  ctx.field("Histogram.updateMode").value = "AutoUpdate" 
  ctx.field("Histogram.xRange").value = "Dynamic Min/Max"
  ctx.field("Histogram.useZeroAsBinCenter").value = False
  ctx.field("Histogram.binSize").value = 1.0
  ctx.field("Histogram.backgroundValue").value = False
  ctx.field("Histogram.curveType").value = "Area"
  ctx.field("Histogram.useStepFunction").value = True
  ctx.field("Histogram.curveStyle").value = 7
  updateSlices()

def updateSlices():
  global firstSlice, startSlice, lastSlice, endSlice, bins, slices
  firstSlice = ctx.field("SubImage.z").value
  startSlice = int(ctx.field("SubImage.z").value)
  lastSlice = int(ctx.field("SubImage.sz").value)+1
  endSlice = int(ctx.field("SubImage.sz").value)
  bins = ctx.field("Histogram.binSize").value
  slices = range(startSlice, endSlice)

def initFigure(control):
  figure = control.object().figure()

def clearFigure():
  control = ctx.control("canvas").object()
  control.figure().clear()

def getX():
  x = ctx.field("Histogram.outputHistogramCurve").object().getXValues()
  stringx = ",".join([str(i) for i in x])
  splittingx = stringx.split(",")
  global xs
  xs = [float(s) for s in splittingx]
   
def getY():
  y = ctx.field("Histogram.outputHistogramCurve").object().getYValues()
  stringy = ",".join([str(i) for i in y])
  splittingy = stringy.split(",")
  global ys
  ys = [float(s) for s in splittingy]  

def singleSlice2D():
  ctx.field("SubImage.z").value = endSlice
  click2D()

def plotSequence():
  clearFigure()
  figure = ctx.control("canvas").object().figure()
  values = [i for i in range(startSlice, lastSlice)]
  sub = 410
  if len(values)<=4:
    for i in values:      
      sub = sub +1
      ctx.field("SubImage.z").value = i
      ctx.field("SubImage.sz").value = i
      getY()
      getX()
      subplot = figure.add_subplot(sub)
      subplot.bar(xs,ys,bins,color='r', label=f'Slice {i}')
      subplot.legend()
    figure.canvas.draw()
  else:
    for i in values:
      ctx.field("SubImage.z").value = i
      ctx.field("SubImage.sz").value = i
      getX()
      getY()
      subplot = figure.add_subplot(111)
      subplot.plot(xs, ys,bins,label=f'Slice {i}')
    subplot.legend()
    figure.canvas.draw()

def click2D():
  clearFigure()
  figure = ctx.control("canvas").object().figure()
  
  if startSlice == endSlice:
    getX()
    getY()
    subplot = figure.add_subplot(111)
    subplot.bar(xs,ys,bins, color = 'b',label = f"Slice {endSlice}")
    subplot.legend()
    subplot.plot()
    figure.canvas.draw()
  else:
    plotSequence()
