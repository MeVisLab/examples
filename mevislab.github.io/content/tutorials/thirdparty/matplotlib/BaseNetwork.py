startSlice = None
endSlice = None
bins = None


def setDefaults():
    ctx.field("Histogram.xRange").value = "Dynamic Min/Max"
    ctx.field("Histogram.useZeroAsBinCenter").value = False
    ctx.field("Histogram.binSize").value = 1.0
    ctx.field("Histogram.backgroundValue").value = False
    ctx.field("Histogram.curveType").value = "Area"
    ctx.field("Histogram.useStepFunction").value = True
    ctx.field("Histogram.curveStyle").value = 7
    ctx.field("SubImage.fullSize").touch()
    ctx.field("SubImage.autoApply").value = True
    ctx.field("Histogram.updateMode").value = "AutoUpdate"
    updateSlices()


def updateSlices():
    global startSlice, endSlice, bins
    startSlice = int(ctx.field("SubImage.z").value)
    endSlice = int(ctx.field("SubImage.sz").value)
    bins = ctx.field("Histogram.binSize").value


def clearFigure():
    control = ctx.control("canvas").object()
    control.figure().clear()


def getX():
    x = ctx.field("Histogram.outputHistogramCurve").object().getXValues()
    stringx = ",".join([str(i) for i in x])
    xValues = stringx.split(",")
    return [float(s) for s in xValues]


def getY():
    y = ctx.field("Histogram.outputHistogramCurve").object().getYValues()
    stringy = ",".join([str(i) for i in y])
    yValues = stringy.split(",")
    return [float(s) for s in yValues]


def singleSlice2D():
    ctx.field("SubImage.z").value = endSlice
    click2D()


def plotSequence():
    clearFigure()
    figure = ctx.control("canvas").object().figure()
    values = [i for i in range(startSlice, endSlice + 1)]
    if len(values) <= 4:
        # adapt the height of the subplot to the number of plots
        sub = 100 * len(values) + 11
        for i in values:
            subplot = figure.add_subplot(sub)
            sub += 1
            ctx.field("SubImage.z").value = i
            ctx.field("SubImage.sz").value = i
            subplot.bar(getX(), getY(), bins, color='r', label=f'Slice {i}')
    else:
        subplot = figure.add_subplot()
        for i in values:
            ctx.field("SubImage.z").value = i
            ctx.field("SubImage.sz").value = i
            subplot.plot(getX(), getY(), bins)
    ctx.field("SubImage.z").value = values[0]
    subplot.legend([f'Slice {i}' for i in values])
    figure.canvas.draw()


def click2D():
    clearFigure()
    figure = ctx.control("canvas").object().figure()

    if startSlice == endSlice:
        subplot = figure.add_subplot(111)
        subplot.bar(getX(), getY(), bins, color='b', label=f"Slice {endSlice}")
        subplot.legend()
        subplot.plot()
        figure.canvas.draw()
    else:
        plotSequence()


def click3D():
    pass


def singleSlice3D():
    pass
