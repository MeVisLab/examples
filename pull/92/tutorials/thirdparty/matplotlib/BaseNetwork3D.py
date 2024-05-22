import numpy as np

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


def comparison():
    clearFigure()
    figure = ctx.control("canvas").object().figure()

    values = [startSlice, endSlice]
    ctx.field("SubImage.z").value = values[0]
    ctx.field("SubImage.sz").value = values[0]
    y1 = getY()
    x1 = getX()
    ctx.field("SubImage.z").value = values[1]
    ctx.field("SubImage.sz").value = values[1]
    y2 = getY()
    x2 = getX()

    subplot = figure.add_subplot(211)
    subplot.bar(x1, y1, bins, color='r')
    subplot.bar(x2, y2, bins, color='b')
    subplot.legend([f'Slice {i}' for i in values])
    subplot.plot()
    subplot = figure.add_subplot(212)
    subplot.bar(x2, y2, bins, color='b')
    subplot.bar(x1, y1, bins, color='r')
    subplot.legend([f'Slice {i}' for i in values])
    figure.canvas.draw()
    ctx.field("SubImage.z").value = values[0]


def click3D():
    clearFigure()
    figure = ctx.control("canvas").object().figure()

    values = [i for i in range(startSlice, endSlice + 1)]

    if startSlice == endSlice:
        subplot = figure.add_subplot(111, projection='3d')
        subplot.bar3d(x=getX(), y=startSlice, z=0, dx=1, dy=1, dz=getY())
        subplot.set_yticks(np.arange(startSlice, endSlice))
        subplot.set_title(f'Slice {startSlice}')
        figure.canvas.draw()
    else:
        clearFigure()
        figure = ctx.control("canvas").object().figure()
        subplot = figure.add_subplot(111, projection='3d')
        for i in values:
            ctx.field("SubImage.z").value = i
            ctx.field("SubImage.sz").value = i
            subplot.bar3d(x=getX(), y=i, z=0, dx=1, dy=1, dz=getY())
            subplot.set_yticks(values)
        subplot.set_title(f'Sequence from {values[0]} to {endSlice}')
        ctx.field("SubImage.z").value = values[0]
        figure.canvas.draw()
