---
title: "Example 5: Volume rendering and interactions"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Visualization", "3D", "Volume Rendering", "GVR", "LUT"]
menu: 
  main:
    identifier: "visualization_example5"
    title: "Volume rendering with lookup table (LUT) rotating automatically."
    weight: 575
    parent: "visualization"
---
# Example 5: Volume rendering and interactions {#TutorialVisualizationExample6}
## Introduction
In this example we like to convert a scan of a head into a 3D scene-object. The scene-object allows to add some textures, interactions and animations.

## Steps to do
### Develop your network
Implement the following network and open the image *$(DemoDataPath)/BrainMultiModal/ProbandT1.tif*.

![SoGVRVolumeRenderer](/images/tutorials/visualization/V6_01.png "SoGVRVolumeRenderer")

The module `SoGVRVolumeRenderer` allows volume rendering of 3D and 4D images.

{{<alert class="info" caption="Extra Infos">}}
Additional information about Volume Rendering can be found here: {{< docuLinks "/Standard/Documentation/Publish/Overviews/GVROverview.html#top" "Giga Voxel Renderer">}}
{{</alert>}}

[//]: <> (MVL-653)

### Change LUT
We like to add a surface color to the head. In order to do that, we add the module `SoLUTEditor`, which adds an RGBA Look up table (LUT) to the scene. Connecting this module to `SoExaminerViewer` left to the connection between `SoGVRRenderer` and `SoExaminerViewer` (remember the order in which Open Inventor modules are executed) allows you to set the surface color of the head.

![SoLUTEditor](/images/tutorials/visualization/V6_02.png "SoLUTEditor")

To change the color, open the panel of `SoLUTEditor`. In this editor we can change color and transparency interactively (for more information take a look at the {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoLUTEditor.html" "help page">}}). Here, we have a range from black to white and from complete transparency to full opacity.

![SoLUTEditor change colors](/images/tutorials/visualization/V6_03.png "SoLUTEditor change colors")

We now like to add color. New color-points can be added by clicking on the color bar at the bottom side of the graph and existing points can be moved by dragging. You can change the color of each point under Color.

![SoLUTEditor add colors](/images/tutorials/visualization/V6_04.png "SoLUTEditor add colors")

### Interactions
As a next step, we add some dynamics to the 3D scene: We like to rotate the head. In Order to do this, add the modules `SoRotationXYZ` and `SoElapsedTime` to the workspace and connect the modules as shown.

![SoRotationXYZ](/images/tutorials/visualization/V6_05.png "SoRotationXYZ")

Open the panels of both modules and select the axis the image should rotate around. In this case the z-axis was selected. Now, build a parameter connection from the parameter *Time* out of the module `SoElapsedTime` to the parameter *Angle* of the module `SoRotationXYZ`. The angle changes with time and the head starts turning.

![Time and Angle](/images/tutorials/visualization/V6_06.png "Time and Angle")

## Exercises
1. Change rotation speed
2. change rotation angle
3. Pause rotation on pressing {{< keyboard "SPACE" >}}

## Summary
* The module `SoGVRVolumeRenderer` renders paged images like DICOM files in a GVR.
* Lookup Tables (LUT) allow you to modify the color of your renderings
