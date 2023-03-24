---
title: "Example 4: Display 2D images in Open Inventor SoRenderArea"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 570
tags: ["Beginner", "Tutorial", "Visualization", "2D", "3D", "Open Inventor", "Snapshots", "Movies"]
menu: 
  main:
    identifier: "visualization_example4"
    title: "Example for displaying images in Open Inventor SoRenderArea"
    weight: 570
    parent: "visualization"
---
# Example 4: Display images converted to Open Inventor scene objects {#TutorialVisualizationExample4}

{{< youtube "WaD6zuvVNek" >}}

## Introduction
In the previous example you learned how to use the module `SoView2DOverlay` together with a `View2D`. MeVisLab provides a whole family of `SoView2D*` modules (`SoView2DOverlay`, `SoView2DRectangle`, `SoView2DGrid`, ...). All these modules create or interact with scene objects and are based on the module `SoView2D`, which can convert a voxel-image into a scene object. In this example, you will get to know some members of the `SoView2D`-family.

{{<alert class="info" caption="Extra Infos">}}

More information about the SoView2D-family can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/ToolBoxReference/SoView2DDocPage.html" "here" >}} and in the {{< docuLinks "/Resources/Documentation/Publish/SDK/ToolBoxReference/classSoView2D.html" "SoView2D Reference" >}}

{{</alert>}}

[//]: <> (MVL-653)

## Steps to do
### Develop your network
We will start the example by creating an overlay again. Add the following modules and connect them as shown. Select a *Threshold* and a *Comparison Operator* for the module `Threshold` as in the previous example. The module `SoView2D` converts the image into a scene-object. The image as well as the overlay is rendered and displayed by the module `SoRenderArea`.

![SoRenderArea](/images/tutorials/visualization/V4_01.png "SoRenderArea")

### Add Extension
You may have noticed, that you are not able to scroll through the slices. This functionality is not yet implemented in the viewer `SoRenderArea`. To add a set of functionalities and viewer extensions, which are commonly used in conjunction with a 2D viewer, add the module `View2DExtensions` to the workspace and connect it as shown below. Now, additional information of the image can be displayed in the viewer and you can navigate and scroll through the slices.

![View2DExtensions](/images/tutorials/visualization/V4_02.png "View2DExtensions")

### Add Screenshot Gallery to Viewing Area
With the help of the module `SoRenderArea` you can record screenshots and movies. Before we do that, open {{< menuitem "View" "Views" "Screenshot Gallery" >}}, to add the Screenshot Gallery to your viewing area.

![Screenshot Gallery](/images/tutorials/visualization/V4_03.png "Screenshot Gallery")

### Create screenshots and movies
If you now select your favorite slice of the bone in the Viewer `SoRenderArea` and press {{< keyboard "F11" >}}, a screenshot is taken and displayed in the Screenshot Gallery. For recording a movie, press {{< keyboard "F9" >}} to start the movie and {{< keyboard "F10" >}} to stop recording. You can find the movie in the Screenshot Gallery.

![Record Movies and Snapshots](/images/tutorials/visualization/V4_05.png "Record Movies and Snapshots")

## Exercises
1. Create movies of a 3D Scene

## Summary
* Modules of the `SoView2D`-family create or interact with scene objects and are based on the module `SoView2D`, which can convert a voxel-image into a scene object
* The `SoRenderArea` module provides functionalities for screenshots and movie generation

{{< networkfile "examples/visualization/example4/VisualizationExample4.mlab" >}}
