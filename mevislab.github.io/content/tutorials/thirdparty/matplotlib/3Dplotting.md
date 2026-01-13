---
title: "Example 4: 3D Plotting"
date: 2023-05-31
status: "OK"
draft: false
weight: 884
tags: ["Advanced", "Tutorial", "Matplotlib", "Visualization"]
menu: 
  main:
    identifier: "matplotlibexample4"
    title: "Example 4: 3D Plotting"
    weight: 884
    parent: "matplotlib"
---
# Example 4: 3D Plotting

## Introduction 

In this tutorial, we will equip the macro module we created in the [Example 1: Module Setup](tutorials/thirdparty/matplotlib/modulesetup) and later on adapted by enabling it to plot grayscale distributions of single slices and sequences in 2D in [Example 2: 2D Plotting](tutorials/thirdparty/matplotlib/2dplotting) with a three-dimensional plotting functionality. 

## Steps to do 

The fields and commands needed have already been prepared in the second tutorial. We will just have to modify our .py file a little to make them usable. Integrate the following code into your .py file and import numpy.

{{< highlight filename = "BaseNetwork.py">}}
```Stan
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
``` {{</highlight>}}

After saving, you should be able to reproduce results like these:

{{<alert class="warning" caption="Warning">}}
You cannot zoom into 3D plots on a Matplotlib canvas. Try changing the viewing angle instead.
{{</alert>}}

![Single Slice 3D](images/tutorials/thirdparty/Matplotlib27.PNG)
![Single Slice 3D](images/tutorials/thirdparty/Matplotlib29.PNG)

You can download the .py file below if you want.
{{< networkfile "/tutorials/thirdparty/matplotlib/BaseNetwork3D.py" >}}
