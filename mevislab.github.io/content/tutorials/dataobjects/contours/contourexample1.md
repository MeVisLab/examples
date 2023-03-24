---
title: "Contour Example 1: Creation of Contours"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 665
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO"]
menu: 
  main:
    identifier: "contourexample1"
    title: "Creation of simple Contours changing their appearance"
    weight: 665
    parent: "contours"
---

# Contour Example 1: Creation of Contours {#TutorialContoursExample1}
## Introduction

We like to start with the creation of CSOs. To create CSOs, you need a `SoCSO*`-Editor. There are several different editors, which can be used to create CSOs (see [here](tutorials/dataobjects/contourobjects#CSOEditors)). Some of them are introduced in this example.

## Steps to do
### Develop your network
For this example, we need the following modules. Add the modules to your workspace, connect them as shown below and load the example image *$(DemoDataPath)/BrainMultiModal/ProbandT1.tif*.

![Data Objects Contours Example 1](/images/tutorials/dataobjects/contours/DO1_01.png "Data Objects Contours Example 1")

### Edit rectangular CSO
Now, open the module `View2D`. Use your left mouse key {{< mousebutton "left" >}}, to draw a rectangle, which is your first CSO.

![Rectangle Contour](/images/tutorials/dataobjects/contours/DO1_02.png "Rectangle Contour")

The involved modules have the following tasks:

1. `SoCSORectangleEditor`: Enables the creation of the CSO and defines the shape of the CSOs

2. `SoView2DCSOExtensibleEditor`: Manages attached CSO editors and the appearance of CSOs

3. `CSOManager`: Creates a list of all drawn CSOs and offers the possibility to group CSOs

If you now open the panel of the `CSOManager`, you will find one CSO, the one we created before. If you like, you can name the CSO.

![CSO Manager](/images/tutorials/dataobjects/contours/DO1_04.png "CSO Manager")

### Change properties of CSO
Now, add the module `SoCSOVisualizationSettings` to your workspace and connect it as shown below.

![CSO Manager](/images/tutorials/dataobjects/contours/DO1_05.png "CSO Manager")

Open the module to change the visualization settings of your CSOs. In
this case, we change the line style (to dashed lines) and the color (to
be red). Tick the *Auto apply* box at the bottom or press *Apply*.

![Visualization Settings](/images/tutorials/dataobjects/contours/DO1_07.png "Visualization Settings")

### CSOs of different shapes
Exchange the module `SoCSORectangleEditor` with another editor, for
example the `SoSCOPolygonEditor` or `SoCSOSplineEditor`. Other editors
allow to draw CSOs of other shapes. For polygon-shaped CSOs or CSOs
consisting of splines, left-click on the image viewer to add new points
to form the CSO. Double--click to finish the CSO.

![SoSCOPolygonEditor](/images/tutorials/dataobjects/contours/DO1_08.png "SoSCOPolygonEditor")
![SoCSOSplineEditor](/images/tutorials/dataobjects/contours/DO1_09.png "SoCSOSplineEditor")

## Exercises
Create CSOs with green color and ellipsoid shapes.

## Summary
* CSOs can be created using a SoCSO-Editor
* CSOs of different shapes can be created
* A list of CSOs can be stored in the `CSOManager`
* Properties of CSOs can be changed using `SoCSOVisualizationSettings`

{{< networkfile "examples/data_objects/contours/example1/ContourExample1.mlab" >}}

 [//]: <> (MVL-682)