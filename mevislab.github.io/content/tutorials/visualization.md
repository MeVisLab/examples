---
title: "Chapter III: Visualization"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 550
tags: ["Beginner", "Tutorial", "Visualization", "2D", "3D"]
menu: 
  main:
    identifier: "visualization"
    title: "Examples for Different Possibilities of Visualizations in MeVisLab"
    weight: 550
    parent: "tutorials"
---

# Visualization in MeVisLab {#TutorialVisualization}

## Introduction
Images and data objects can be rendered in 2D and 3D and interacted with in several ways using a set of tools available through MeVisLab. 
In this chapter in particular, we will focus on simple image interaction with two- and three-dimensional visualizations. 

{{<alert class="info" caption="Info">}}
Not only pixel- and voxel-based data, but also scene objects and 3D scenes can be visualized. See our tutorial on [OpenInventorModules](tutorials/openinventor#TutorialOpenInventorModules) for further information.
{{</alert>}}

## View2D and View3D
An easy way to display data and images in 2D and 3D is by using them modules `View2D` and `View3D`. What can be done with these viewers?

![View2D and View3D](images/tutorials/visualization/V0.png "View2D and View3D")

### View2D
1. Scroll through the slices using the mouse wheel {{< mousebutton "middle" >}}  and/or middle mouse button {{< mousebutton "middle" >}}.

2. Change the contrast of the image by clicking the right mouse button {{< mousebutton "right" >}} and moving the mouse.

3. Zoom in and out by pressing {{< keyboard "CTRL" >}} and middle mouse button {{< mousebutton "middle" >}}.

4. Toggle between multiple timepoints (if available) via {{< keyboard "ArrowLeft" >}} and {{< keyboard "ArrowRight" >}}.

5. More features can be found on the help page.

{{<alert class="info" caption="Info">}}
The `View2DExtensions` module provides additional ways to interact with an image. ![View2DExtensions](images/tutorials/visualization/V0a.png "View2DExtensions")
{{</alert>}}

### View3D
1. Zoom in and out using the mouse wheel {{< mousebutton "middle" >}}.

2. Drag the 3D objects using the middle mouse button {{< mousebutton "middle" >}}.

3. Change the contrast of the image by clicking the right mouse button {{< mousebutton "right" >}} and moving the mouse.

4. Rotate the object by pressing the left mouse button {{< mousebutton "left" >}} and moving the object around. The present orientation is displayed by a cube in the bottom right corner.

5. More features, like recording movies, can be found on the help page.

6. Toggle between multiple timepoints (if available) via {{< keyboard "ArrowLeft" >}} and {{< keyboard "ArrowRight" >}}.

{{<alert class="info" caption="Info">}}
More information on Image Processing in MeVisLab can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch12.html" "here" >}}
{{</alert>}}
