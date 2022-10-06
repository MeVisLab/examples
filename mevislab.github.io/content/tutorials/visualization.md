---
title: "Chapter III: Visualization"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Visualization", "2D", "3D"]
menu: 
  main:
    identifier: "visualization"
    title: "Examples for different possibilities of visualizations in MeVisLab."
    weight: 550
    parent: "tutorials"
---
# Visualization in MeVisLab {#TutorialVisualization}
## Introduction
MeVisLab contains a whole toolkit to visualize data and images. 2D, 3D and 4D rendering is possible as well as the interaction with images and data objects.

In this chapter, we focus on 2D and 3D visualization and simple image interactions. Not only pixel- and voxel-based data can be visualized, but also scene objects and 3D scenes (see [here](/tutorials/openinventor#TutorialOpenInventorModules)).

## View2D and View3D

An easy way to display data and images in 2D and 3D is by using the Modules `View2D` and `View3D`. What can you do with these viewers?

![View2D and View3D](/images/tutorials/visualization/V0.png "View2D and View3D")

### View2D

1. Scroll through the slices using the mouse wheel {{< mousebutton "middle" >}}.

2. Change the contrast of the image by clicking the right mouse button {{< mousebutton "right" >}} and move the mouse

3. Zoom in and out by pressing {{< keyboard "+" >}} and {{< keyboard "-" >}}

4. Toggle between multiple timepoints (if available) via {{< keyboard "ArrowLeft" >}} and {{< keyboard "ArrowRight" >}}

5. More features can be found on the help page.

### View3D

1. Zoom in and out using the mouse wheel {{< mousebutton "middle" >}}.

2. Change the contrast of the image by clicking the right mouse button {{< mousebutton "right" >}} and move the mouse

3. Grab the object by pressing the left mouse button {{< mousebutton "left" >}} and move the object around. The present orientation is displayed by a cube in the bottom right corner.

4. More features, like recording movies, can be found on the help page.

5. Toggle between multiple timepoints (if available) via {{< keyboard "ArrowLeft" >}} and {{< keyboard "ArrowRight" >}}

{{<alert class="info" caption="Additional Information">}}
More Information about Image Processing in MeVisLab can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch12.html" "here" >}}
{{</alert>}}

## Examples:
1. [Synchronous view of two images](/tutorials/visualization/visualizationexample1)
2. [Creating a magnifier](/tutorials/visualization/visualizationexample2)
3. [Image Overlays](/tutorials/visualization/visualizationexample3)
4. [Display 2D images in Open Inventor SoRenderArea](/tutorials/visualization/visualizationexample4)
5. [Volume rendering and interactions](/tutorials/visualization/visualizationexample5)
6. [MeVisLab PathTracer](/tutorials/visualization/visualizationexample6)