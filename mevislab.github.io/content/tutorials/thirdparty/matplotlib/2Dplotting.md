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

In this tutorial, we will equip the macro module we created in the [previous tutorial](/examples/tutorials/thirdparty/matplotlib/modulesetup.md/) with a responsive and interactable panel to plot grayscale distributions of single slices as well as defined sequences of slices in 2D.

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


