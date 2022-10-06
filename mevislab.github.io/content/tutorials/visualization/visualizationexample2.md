---
title: "Example 2: Creating a magnifier"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Visualization", "2D", "Magnifier"]
menu: 
  main:
    identifier: "visualization_example2"
    title: "Display an image in different viewing directions and mark locations in the image for creating a Magnifier from a rectangle"
    weight: 560
    parent: "visualization"
---
# Example 2: Creating a magnifier {#TutorialVisualizationExample2}
## Introduction
Medical images are typically displayed in three different viewing directions (see image): coronal, axial and sagittal.

Using the Viewer `OrthoView2D` you are able to decide, which viewing direction you like to use. In addition to that, you have the opportunity to display all three orthogonal viewing directions simultaneously. Here, we like to display an image of the head in all three viewing directions and mark positions in the image.

![Body Planes](/images/tutorials/visualization/V2_00.png "Body Planes")

## Steps to do
### Develop your network
In this example, use the module `LocalImage` to load the example *image MRI_Head.tif*. Now, connect the module `OrthoView2D` with the loaded image. The image is displayed in three orthogonal viewing directions. The yellow marker displays the same voxel in all three images. You can scroll through the slices in all three viewing directions.


{{<alert class="info" caption="Extra Infos">}}
In case your image is black, change the *Window* and *Center* values by moving the mouse with right mouse button {{< mousebutton "right" >}} pressed.
{{</alert>}}

![OrthoView2D](/images/tutorials/visualization/V2_01.png "OrthoView2D")

### SoView2DPositioning
Next, we add the module `SoView2DPositioning` (an Open Inventor module).

The module enables the selection of an image position via mouse-click {{< mousebutton "left" >}}. The last-clicked location in the Viewer is marked in white. If you now scroll through the slices, both, the last-clicked location and the current image location are shown.

![SoView2DPositioning](/images/tutorials/visualization/V2_02.png "SoView2DPositioning")

### SoView2DRectangle
Instead of points, we like to mark areas. In order to do that, replace the module `SoView2DPosition` with the module `SoView2DRectangle`. The module allows to add a rectangle to the image. Right-click on the image and draw a rectangle. In the `OthoView2D`, the rectangle is displayed in every viewing direction.

![SoView2DRectangle](/images/tutorials/visualization/V2_03.png "SoView2DRectangle")

### Using a rectangle to build a magnifier

We like to use the module `SoView2DRectangle` to create a magnifier. In order to do that add the following modules to your workspace and connect them as shown below. We need to connect the module `SoView2DRectangle` to a hidden input connector of the module `SynchroView2D`. To be able to do this, click on your workspace and afterwards press {{< keyboard "SPACE" >}}. You can see, that `SynchroView2D` possesses Open Inventor input connectors. You can connect your module `SoView2DRectangle` to one of these connectors.

![Hidden Inputs of SynchroView2D](/images/tutorials/visualization/V2_05.png "Hidden Inputs of SynchroView2D")

![Connect Hidden Inputs of SynchroView2D](/images/tutorials/visualization/V2_06.png "Connect Hidden Inputs of SynchroView2D")

In addition to that, add two types of the module `DecomposeVector3` to your network. In MeVisLab exist different data types, for example vectors, or single variable, which contain the data type float or integer. This module can be used to convert field values of type vector (in this case a vector consisting of three entries) into three single coordinates. You will see in the next step, why this module can be useful.

![DecomposeVector3](/images/tutorials/visualization/V2_07.png "DecomposeVector3")

We like to use the module `SubImage` to select a section of a slice, which is than displayed in the Viewer. The idea is to display a magnified section of one slice next to the whole slice in the module `SynchroView2D`. In order to do that, we need to tell the module `SubImage` which section to display in the Viewer. The section is selected using the module `SoView2DRectangle`. As a last step, we need to transmit the coordinates of the chosen rectangle to the module `SubImage`. To do that, we will build some parameter connections.

![SubImage](/images/tutorials/visualization/V2_08.png "SubImage")

Now, open the panels of the modules `SoView2DRectangle` and `DecomposeVector3` and `DecomposeVector31`.

We here rename the `DecomposeVector3` modules (press {{< keyboard "F2" >}} to do that), for a better overview.

In the panel of the module `Rectangle` in the box Position you can see the position of the rectangle given in two 3D vectors.

We like to use the modules `DecomposeVector3` to extract the single x, y and z values of the vector. For that, create a parameter connection from the field *Start Wold Pos* to the vector of the module we named `StartWorldPos_Rectangle` and create a connection from the field *End World Pos* to the vector of module `EndWorldPos_Rectangle`. The decomposed coordinates can be now used for further parameter connections.

![Parameter Connections](/images/tutorials/visualization/V2_09.png "Parameter Connections")

Open the panel of the module `SubImage`. Select the *Mode World Start & End* (*Image Axis Aligned*). Enable the function *Auto apply*.

![World Coordinates](/images/tutorials/visualization/V2_10.png "World Coordinates")

Now, create parameter connections from the fields *X*, *Y*, *Z* of the module `StartWorldPos_Rectangle` to the field *Start X*, *Start Y*, *Start Z* in the panel of the module `SubImage`. Similarly, connect the parameter fields fields *X*, *Y*, *Z* of the module `EndWorldPos_Rectangle` to the field *End X*, *End Y*, *End Z* in the panel of the module `SubImage`.

![Another Parameter Connection](/images/tutorials/visualization/V2_11.png "Another Parameter Connection")

With this, you finished your magnifier. Open the Viewer and draw a rectangle on one slice, to see the result.

![Final Magnifier with SubImage](/images/tutorials/visualization/V2_12.png "Final Magnifier with SubImage")


## Exercises
Invert the image inside your magnified `SubImage` without changing the original image.

## Summary
* The module `OrthoView2D` provides coronal, axial and sagittal views of an image.
* The `SubImage` module allows to define a region of an input image to be treated as a separate image.
* Single x, y and z coordinates can be transferred to a 3-dimensional vector and vice versa by using `ComposeVector3` and `DecomposeVector3`
* Some modules provide hidden in- and outputs which can be shown via {{< keyboard "SPACE" >}}
