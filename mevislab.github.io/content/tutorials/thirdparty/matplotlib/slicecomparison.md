---
title: "Example 3: Slice Comparison"
date: 2023-05-31
status: "OK"
draft: false
weight: 883
tags: ["Beginner", "Tutorial", "Matplotlib", "Visualization"]
menu: 
  main:
    identifier: "matplotlibexample3"
    title: "Slice Comparison"
    weight: 883
    parent: "matplotlib"
---

# Example 3: Slice Comparison

## Introduction 
We will adapt the previously created macro module to be able to overlay two defined slices to compare their grayscale distributions. 
* The module we are adapting has been set up in the [Example 1: Module Setup](tutorials/thirdparty/matplotlib/modulesetup) tutorial.
* The panel and two-dimensional plotting functionality has been added in [Example 2: 2D Plotting]
  (tutorials/thirdparty/matplotlib/2dplotting).

## Steps to Do
At first, we will extend the panel: Open your `BaseNetwork` macro module within an empty MeVisLab workspace and select the *.script* file from its related files. 

Add the following code into your *.script* file between the "Single Slice" and the "Sequence" box.

{{< highlight filename = "BaseNetwork.script">}}
```Stan
        Box {
            title = "Comparison"
            Field "SubImage.z" {
                title = "Compare slice"
            }
            Field "SubImage.sz" {
                title = "With slice"
            }
            Button {
                title   = "Plot"
                command = "comparison"
            }
        }
```
{{</highlight>}}

Your panel should now be changed to look like this: 

![MATE Preview](images/tutorials/thirdparty/Matplotlib14.PNG)

We will now add the "comparison" function, to give the "Plot" button in our "Comparison" box a purpose. To do so, switch to your module's *.py* file and choose a cosy place for the following piece of code:

{{< highlight filename = "BaseNetwork.py">}}
```Python
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
```
{{</highlight>}}

You should now be able to reproduce results like these:

![Comparison](images/tutorials/thirdparty/Matplotlib16.PNG)
![Comparison](images/tutorials/thirdparty/Matplotlib17.PNG)

## Summary
* Grayscale distributions of two slices can be layered to compare them and make deviations noticeable.

