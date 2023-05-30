---
title: "Example 2: Plotting in 2D"
date: 2023-05-30
status: "OK"
draft: false
weight: 882
tags: ["Advanced", "Tutorial", "Matplotlib", "Visualization"]
menu: 
  main:
    identifier: "matplotlibexample2"
    title: "Example 2: 2D Histogram Plotting"
    weight: 882
    parent: "matplotlib"
---
# Example 2: Plotting in 2D

## Introduction 

In this tutorial, we will equip the macro module we created in the [previous tuturial](/tutorials/thirdparty/matplotlib/modulesetup) with a responsive and interactable panel to plot grayscale distributions of single slices as well as defined sequences of slices in 2D.

## Steps to do

Open the module definition folder of your macro module and the related .script file in MATE. Then activate the Preview as shown below: 

![MATE Preview](/images/tutorials/thirdparty/Matplotlib7.png)

Drag the small Preview window the bottom right corner of your window where it does not bother you. We will now be adding contents to be displayed there. 

Adding the following code to your .script file will open a panel window if the macro module is clicked.
This new panel window contains a Matplotlib canvas where the plots will be displayed later on as well as two prepared boxes that we will add functions to in the next step.

{{< highlight filename = "BaseNetwork.script">}}
```Stan
 Window {
  Category{
    Horizontal{
      Vertical{
        expandY = True
        expandX = False
        Box {
          title= "Single Slice"
        }
        Box{
          title = "Sequence"
        }
        Empty{
          expandY = True
      }
    }
      Box{
        MatplotlibCanvas {
          expandY = True
          expandX = True
          name        = canvas
          useToolBar = True
        }
        expandY = True
        expandX = True
      }     
    }
  }
}   
``` {{</highlight>}}

Letting a box expand on the x- or y-axis or adding an empty object do so contributes to the panel looking a certain way and helps the positioning of the elements. You can also try to vary the positioning by adding or removing expand-statements or moving boxes from a vertical to a horizontal alignment. Hover over the boxes in the preview to explore the concept.

{{<alert class="info" caption="Info">}}
You can click and hold onto a box to move it within the Previw. Your code will automatically be changed according to the new positioning.
{{</alert>}}

**Now, we need to identify which module parameters we want to be able to access from the panel of our macro:**

To plot a slice or a defined sequence of slices, we need to be able to set a start and an end. 
Go back into your MeVisLab workspace, right click your `BaseNetwork` module and choose "Show Internal Network". 

![SubImage module info](/images/tutorials/thirdparty/Matplotlib8.png "The `SubImage` module provides the option to set sequences of slices.")
![SubImage module panel](/images/tutorials/thirdparty/Matplotlib9.PNG "The starting and ending slices of the sequence can be set in the module panel.")

{{<alert class="info" caption="Info">}}
To find out what the parameters are called, what type of values they contain and receive and what they refer to, you can right-click on them within the panel.
{{</alert>}}

We now know that we will need `SubImage.z` and `SubImage.sz` to define the start and end of a sequence. 
But there are a few other module parameters that must be set beforehand to make sure the data we extract to plot later is compareable and correct.

To do so, we will be defining a "setDefaults" function for our module. Open the .py file and add the code below.

{{< highlight filename = "BaseNetwork.py">}}
```Stan
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
``` {{</highlight>}}

As it is also incredibly important, that the values of the parameters we are referencing are regularly updated, we will be setting some global values containing those values.

{{< highlight filename = "BaseNetwork.py">}}
```Stan

firstSlice = None
startSlice = None
lastSlice = None
endSlice = None
bins = None 
slices = None

def updateSlices():
  global firstSlice, startSlice, lastSlice, endSlice, bins, slices
  firstSlice = ctx.field("SubImage.z").value
  startSlice = int(ctx.field("SubImage.z").value)
  lastSlice = int(ctx.field("SubImage.sz").value)+1
  endSlice = int(ctx.field("SubImage.sz").value)
  bins = ctx.field("Histogram.binSize").value
  slices = range(startSlice, endSlice)
``` {{</highlight>}}

Make sure that the variable declarations as none are put above the "setDefaults" function and add the execution of the "updateSlices()" function into the "setDefaults" function, like so:

{{< highlight filename = "BaseNetwork.py">}}
```Stan
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
``` {{</highlight>}}

Now we are ensuring, that the "setDefaults" function and therefore also the "updateSlices" function are executed everytime the panel is opened by setting "setDefaults" as a wake up command.

{{< highlight filename = "BaseNetwork.script">}}
```Stan
Commands {
    source = $(LOCAL)/BaseNetwork.py
    
    wakeupCommand = "setDefaults"
} 
``` {{</highlight>}}

And we add field listeners, so that the field values that we are working with are updated everytime they are changed.

{{< highlight filename = "BaseNetwork.script">}}
```Stan
Commands {
    source = $(LOCAL)/BaseNetwork.py
    
    wakeupCommand = "setDefaults"

    FieldListener {
      listenField = "SubImage.sz"
      listenField = "SubImage.z"
      listenField = "Histogram.binSize"

      command     = "updateSlices"
    }
} 
``` {{</highlight>}}

To see if all of this is working, we need to embed fields into our panel. 
Put this inside of the box titled "Single Slice":

{{< highlight filename = "BaseNetwork.script">}}
```Stan
 Field "SubImage.sz"{
                title = "Plot slice"
            }
              Button  { title = "in 2D"
                command = "singleSlice2D"
              }
              Button {
                title = "in 3D"
                command = "singleSlice3D"
          }
              Empty{}
``` {{</highlight>}}

And then add this to your box titled "Sequence":

{{< highlight filename = "BaseNetwork.script">}}
```Stan
 Field "SubImage.z"{
                title = "From slice"
              }
              Field "SubImage.sz"{
                title = "To slice"
              }
              Button{ title = "Plot 2D"
                command = "click2D"
              }
              Button{ title = "Plot 3D"
                command = "click3D"}
``` {{</highlight>}}

Lastly, put this under your two boxes, but above the empty element in the vertical alignment:
{{< highlight filename = "BaseNetwork.script">}}
```Stan
  Field "Histogram.binSize"{
          title = "Bin size"
        }
``` {{</highlight>}}

If you followed all of the listed steps, your panel preview should look like this and display all the current parameter values. 
![Adapted macro panel](/images/tutorials/thirdparty/Matplotlib10.PNG)

We can now work on the functions that visualize the data as plots on the Matplotlib canvas. 
You will have noticed how all of the buttons in the .script file have a command. Whenever that button is clicked, its designated command is executed. However, for any of the via command referenced functions to work, we need one that ensures, that the plots are shown on the integrated Matplotlib canvas. We will start with that one.

{{< highlight filename = "BaseNetwork.py">}}
```Stan
def initFigure(control):
  figure = control.object().figure()

def clearFigure():
  control = ctx.control("canvas").object()
  control.figure().clear()
``` {{</highlight>}}

Now that this is prepared and ready, we can add the functions to extract the data:

{{< highlight filename = "BaseNetwork.py">}}
```Stan
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
``` {{</highlight>}}

And lastly enable the plotting of a single slice as well as a sequence in 2D through our panel by adding the code below. 

{{< highlight filename = "BaseNetwork.py">}}
```Stan
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
``` {{</highlight>}}

You should now be able to reproduce results like these: 

![Single Slice 2D](/images/tutorials/thirdparty/Matplotlib13.PNG "2D plot of slice 28")
![Small Sequence 2D](/images/tutorials/thirdparty/Matplotlib11.PNG "Small sequence in 2D")
![Sequence in 2D](/images/tutorials/thirdparty/Matplotlib12.PNG "Sequence in 2D")

You can download the .py as well as the .script file below if you want. 
{{< py "/tutorials/thirdparty/matplotlib/BaseNetwork.py" >}}
{{< script "/tutorials/thirdparty/matplotlib/BaseNetwork.script" >}}

### Summary 
+ Functions are connected to fields of the panel through commands
+ The panel preview in MATE can be used to alter positioning of panel components without touching the code
+ An "expand" statement can help the positioning of components in the panel