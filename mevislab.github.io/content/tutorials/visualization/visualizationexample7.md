---
title: "Example 7: Add 3D viewer to OrthoView2D"
date: 2023-11-21
status: "OK"
draft: false
weight: 590
tags: ["Beginner", "Tutorial", "Visualization", "3D", "OrthoView2D"]
menu: 
  main:
    identifier: "visualization_example7"
    title: "Add 3D viewer to OrthoView2D."
    weight: 590
    parent: "visualization"
---
# Example 7: Add 3D viewer to OrthoView2D {#TutorialVisualizationExample7}

## Introduction
In this example we like to use the `OrthoView2D` module and add a 3D viewer to the layout *Cube*.

## Steps to do
### Develop your network
Add the modules `LocalImage` and `OrthoView2D` to your workspace and connect them.

![Network](/images/tutorials/image_processing/network_example7.png "Network")

The `OrthoView2D` module allows you to select multiple layouts. Select layout *Cube Equal*. The layout shows your image in three orthogonal viewing directions. The top left segment remains empty.

![OrthoView2D Layouts](/images/tutorials/image_processing/network_example7_2.png "OrthoView2D Layouts")

We now want to use a 3D rendering in the top left segment, whenever the layout *Cube Equal* is chosen. Add a `View3D` and a `SoViewportRegion` module to your workspace. Connect the `LocalImage` with your `View3D`. The image is rendered in 3D. Hit {{< keyboard "SPACE" >}} on your keyboard to make the hidden output of the `View3D` module visible. Connect it with your `SoViewportRegion` and connect the `SoViewportRegion` with the *inInvPreLUT* input of the `OrthoView2D`.

![Network with SoViewportRegion](/images/tutorials/image_processing/network_example7_3.png "Network with SoViewportRegion")

Open the `OrthoView2D` and inspect your layout.

![OrthoView2D with 3D](/images/tutorials/image_processing/network_example7_4.png "OrthoView2D with 3D")

You can see your `View3D` being visible in the bottom right segment of the layout behind the coronal view of the image. Open the panel of the `SoViewportRegion` module. In section *X-Position and Width*, set *Left Border* to *0* and *Right Border* to *0.5*. In section *Y-Position and Height*, set *Lower Border* to *0* and *Upper Border* to *0.5*. Also check *Render delayed paths*.

![Define viewport region](/images/tutorials/image_processing/network_example7_5.png "Define viewport region")

The `View3D` image is now rendered to the top left segment of the `OrthoView2D` because the module `SoViewportRegion` renders a sub graph into a specified viewport region (VPR). The problem is: We cannot rotate and pan the 3D object, because there is no camera interaction anymore after adding the `SoViewportRegion`. The camera interaction is taken by the `View3D` module before the viewport is taken.

Add a `SoCameraInteraction` module between the `View3D` and the `SoViewportRegion`. You can now interact with your 3D scene but the rotation is not executed on the center of the object. Trigger *ViewAll* on your `SoCameraInteraction` module.

![SoCameraInteraction](/images/tutorials/image_processing/network_example7_6.png "SoCameraInteraction")

You finally added the `View3D` to the `OrthoView2D`. We have another problem now. If you change the layout to something different than *LAYOUT_CUBE_EQUAL*, the 3D content remains visible.

We can use a `StringUtils` to resolve that. Set *Operation* to *Compare* and draw a parameter connection from the field *OrthoView2D.layout* to the field *StringUtils.string1*. The currently selected layout is written as *String A*. Enter *LAYOUT_CUBE_EQUAL* as *String B*. Now, draw a parameter connection from the field *StringUtils.boolResult* to the field *SoViewportRegion.on*.

![StringUtils](/images/tutorials/image_processing/network_example7_7.png "StringUtils")

If the selected layout in `OrthoView2D` now matches the string *LAYOUT_CUBE_EQUAL* (the field *boolResult* of the `StringUtils` module is *TRUE*), the `SoViewportRegion` is turned *on*. In any other case, the 3D segment is not visible.

![Final Network](/images/tutorials/image_processing/network_example7_8.png "Final Network")

## Summary
* The module `SoViewportRegion` renders a sub graph into a specified viewport region (VPR)

{{< networkfile "examples/visualization/example5/VisualizationExample7.mlab" >}}
