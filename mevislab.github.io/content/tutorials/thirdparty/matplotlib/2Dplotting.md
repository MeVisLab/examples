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

Letting a box expand on the x- or y-axis or adding an empty object do so contributes to the panel looking a certain way and helps the positioning of the elements. You can also try to vary the positioning by adding or removing expand-statements or moving boxes from a vertical to a horizontal alignment. Hover over your Preview to explore the boy concept or click and hold on a box and move it within the Preview. Your code will be changed according to the new positioning in the Preview. 

