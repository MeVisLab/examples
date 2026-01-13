---
title: "Example 2: Mouse interactions in Open Inventor"
date: 2022-06-15T08:56:33+02:00
draft: false
weight: 520
status: "OK"
tags: ["Beginner", "Tutorial", "Open Inventor", "3D", "Mouse Interactions"]
menu: 
  main:
    identifier: "mouseinteractions"
    title: "Implementation of mouse interactions in Open Inventor Scenes"
    weight: 520
    parent: "openinventor"
---
# Example 2: Mouse Interactions in Open Inventor {#TutorialVisualizationExample5}

{{< youtube "Ye5lOHDWcRo" >}}

## Introduction
In this example, we implement some image or object interactions. We will create a 3D scene, in which we display a cube and change its size using the mouse. We also get to know another viewer, the module `SoExaminerViewer`. This viewer is important. It enables the rendering of Open Inventor scenes and allows interactions with the Open Inventor scenes.

## Steps to Do
### Develop Your Network
For implementing the example, build the following network. We already know the module `SoCube`, which builds a 3D scene object forming a cube. In addition to that, add the module `SoMouseGrabber`. Connect the modules as shown below.

{{<alert class="info" caption="Extra Infos">}}
Additional information about the `SoMouseGrabber` can be found here: {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoMouseGrabber.html#top" "SoMouseGrabber">}}
{{</alert>}}

[//]: <> (MVL-653)

![SoMouseGrabber](images/tutorials/openinventor/V5_01.png "SoMouseGrabber")
### Configure Mouse Interactions
Now, open the panels of the module `SoMouseGrabber` and the module `SoExaminerViewer`, which displays a cube. In the viewer, press the right button of your mouse {{< mousebutton "right" >}} and move the mouse around. This action can be seen in the panel of the module SoMouseGrabber.

{{<alert class="warning" caption="Attention">}}
Make sure to configure `SoMouseGrabber` fields as seen below.
{{</alert>}}

![SoMouseGrabber](images/tutorials/openinventor/V5_02.png "SoMouseGrabber")

**You can see:**
1. *Button 3*, the right mouse button {{< mousebutton "right" >}}, is tagged as being pressed
2. Changes of the mouse coordinates are displayed in the box *Output*

![Mouse Interactions](images/tutorials/openinventor/V5_03.png "Mouse Interactions")

### Resize Cube via Mouse Interactions

We like to use the detected mouse movements to change the size of our cube. In order to that, open the panel of `SoCube`. Build parameter connections from the mouse coordinates to the width and depth of the cube.

![Change Cube size by Mouse Events](images/tutorials/openinventor/V5_04.png "Change Cube size by Mouse Events")

If you now press the right mouse button {{< mousebutton "right" >}} inside the viewer and move the mouse around, the size of the cube changes.

## Exercises
1. Change location of the cube via Mouse Interactions by using the Module `SoTransform`
1. Add more objects to the scene and interact with them

## Summary
* The module `SoExaminerViewer` enables the rendering of Open Inventor scenes and allows interactions with the Open Inventor scenes.
* Mouse interactions can be applied to the objects in the scene.

{{< networkfile "examples/open_inventor/example2/OpenInventorExample2.mlab" >}}
