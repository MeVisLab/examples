---
title: "Example 2: Mouse Interactions in Open Inventor"
date: 2022-06-15T08:56:33+02:00
draft: false
weight: 520
status: "OK"
tags: ["Beginner", "Tutorial", "Open Inventor", "3D", "Mouse Interactions"]
menu: 
  main:
    identifier: "mouseinteractions"
    title: "Implementation of Mouse Interactions in Open Inventor Scenes"
    weight: 520
    parent: "openinventor"
---

# Example 2: Mouse Interactions in Open Inventor {#TutorialVisualizationExample5}

{{< youtube "Ye5lOHDWcRo" >}}

## Introduction
In this example, we implement some image or object interactions. We will create a 3D scene in which we display a cube and change its size using the mouse. We also get to know another viewer, the module `SoExaminerViewer`. This viewer is important: It enables the rendering of Open Inventor scenes and allows interactions with the Open Inventor scenes.

## Steps to Do

### Develop Your Network
For implementing the example, build the following network. We already know the module `SoCube`, which builds a 3D scene object forming a cube. In addition to that, add the module `SoMouseGrabber`. Connect the modules as shown below.

{{<alert class="info" caption="Extra Infos">}}
Additional information about the `SoMouseGrabber` can be found here: {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoMouseGrabber.html#top" "SoMouseGrabber">}}
{{</alert>}}

[//]: <> (MVL-653)

![Network with a SoMouseGrabber](images/tutorials/openinventor/V5_01.png "Network with a SoMouseGrabber")
### Configure Mouse Interactions
Now, open the panels of the module `SoMouseGrabber` and the module `SoExaminerViewer`, which displays a cube. In the viewer, press the right button of your mouse {{< mousebutton "right" >}} and move the mouse around. This action can be seen in the panel of the module SoMouseGrabber.

{{<alert class="warning" caption="Attention">}}
Make sure to configure `SoMouseGrabber` fields as seen below.
{{</alert>}}

![Network with a SoMouseGrabber and panels](images/tutorials/openinventor/V5_02.png "Network with a SoMouseGrabber and panels")

**You can see:**
1. <field>Button 3</field>, the right mouse button {{< mousebutton "right" >}}, is tagged as being pressed
2. Changes of the mouse coordinates are displayed in the box *Output*

![Mouse interactions](images/tutorials/openinventor/V5_03.png "Mouse interactions")

### Resize Cube via Mouse Interactions
We like to use the detected mouse movements to change the size of our cube. In order to that, open the panel of `SoCube`. Establish parameter connections from the mouse coordinates to the width and depth of the cube.

![Change cube size with mouse events](images/tutorials/openinventor/V5_04.png "Change cube size with mouse events")

If you now press the right mouse button {{< mousebutton "right" >}} in the viewer and move the mouse around, the size of the cube changes.

## Exercises
1. Change location of the cube via Mouse Interactions by using the module `SoTransform`.
1. Add more objects to the scene and interact with them.

## Summary
* The module `SoExaminerViewer` enables the rendering of Open Inventor scenes and allows interactions with the Open Inventor scenes.
* Mouse interactions can be applied to the objects in the scene.

{{< networkfile "examples/open_inventor/example2/OpenInventorExample2.mlab" >}}
