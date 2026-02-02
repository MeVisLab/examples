---
title: "Example 2: Creating a Magnifier"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 560
tags: ["Beginner", "Tutorial", "Visualization", "2D", "Magnifier"]
menu: 
  main:
    identifier: "visualization_example2"
    title: "Display an Image in Different Viewing Directions and Mark Locations in the Image for Creating a Magnifier From a Rectangle"
    weight: 560
    parent: "visualization"
---

# Example 2: Creating a Magnifier {#TutorialVisualizationExample2}

{{< youtube "lfq_TkWOuCo" >}}

## Introduction
Medical images are typically displayed in three different viewing directions (see image): coronal, axial, and sagittal.

Using the viewer `OrthoView2D`, you are able to decide which viewing direction you like to use. In addition to that, you have the opportunity to display all three orthogonal viewing directions simultaneously. Here, we like to display an image of the head in all three viewing directions and mark positions in the image.

![Body Planes](images/tutorials/visualization/V2_00.png "Body Planes")

## Steps to Do

### Develop Your Network
In this example, use the module `LocalImage` to load the example *image MRI_Head.tif*. Now, connect the module `OrthoView2D` to the loaded image. The image is displayed in three orthogonal viewing directions. The yellow marker displays the same voxel in all three images. You can scroll through the slices in all three viewing directions.


{{<alert class="info" caption="Extra Infos">}}
In the case your image is black, change the *Window* and *Center* values by moving the mouse with right mouse button {{< mousebutton "right" >}} pressed.
{{</alert>}}

![OrthoView2D](images/tutorials/visualization/V2_01.png "OrthoView2D")

### SoView2DPosition
Next, we add the module `SoView2DPosition` (an Open Inventor module).

The module enables the selection of an image position via mouse click {{< mousebutton "left" >}}. The last clicked location in the viewer is marked in white. If you now scroll through the slices, both the last clicked location and the current image location are shown.

![SoView2DPosition](images/tutorials/visualization/V2_02.png "SoView2DPosition")

### SoView2DRectangle
Instead of points, we like to mark areas. In order to do that, replace the module `SoView2DPosition` with the module `SoView2DRectangle`. The module allows to add a rectangle to the image. Left-click {{< mousebutton "left" >}} on the image and draw a rectangle. In the `OthoView2D`, the rectangle is displayed in every viewing direction.

![SoView2DRectangle](images/tutorials/visualization/V2_03.png "SoView2DRectangle")

### Using a Rectangle to Build a Magnifier
We like to use the module `SoView2DRectangle` to create a magnifier. In order to do that, add the following modules to your workspace and connect them as shown below. We need to connect the module `SoView2DRectangle` to a hidden input connector of the module `SynchroView2D`. To be able to do this, click on your workspace and afterward press {{< keyboard "SPACE" >}}. You can see that `SynchroView2D` possesses Open Inventor input connectors. You can connect your module `SoView2DRectangle` to one of these connectors.

![Hidden Inputs of SynchroView2D](images/tutorials/visualization/V2_05.png "Hidden Inputs of SynchroView2D")

![Connect Hidden Inputs of SynchroView2D](images/tutorials/visualization/V2_06.png "Connect Hidden Inputs of SynchroView2D")

In addition to that, add two instances of the module `DecomposeVector3` to your network. In MeVisLab, different data types exist, for example, vectors, or single variables, which contain the data type float or integer. This module can be used to convert field values of type vector (in this case, a vector consisting of three entries) into three single coordinates. You will see in the next step why this module can be useful.

![DecomposeVector3](images/tutorials/visualization/V2_07.png "DecomposeVector3")

We like to use the module `SubImage` to select a section of a slice, which is then displayed in the viewer. The idea is to display a magnified section of one slice next to the whole slice in the module `SynchroView2D`. In order to do that, we need to tell the module `SubImage` which section to display in the viewer. The section is selected by using the module `SoView2DRectangle`. As a last step, we need to transmit the coordinates of the chosen rectangle to the module `SubImage`. To do that, we will build some parameter connections.

![SubImage](images/tutorials/visualization/V2_08.png "SubImage")

Now, open the panels of the modules `SoView2DRectangle`, `DecomposeVector3`, and `DecomposeVector31`.

We rename the `DecomposeVector3` modules (press {{< keyboard "F2" >}} to do that) here for a better overview.

In the panel of the module `Rectangle` in the box *Position*, you can see the position of the rectangle given in two 3D vectors.

We like to use the modules `DecomposeVector3` to extract the single x, y, and z values of the vector. For that, create a parameter connection from the field <field>Start Wold Pos</field> to the vector of the module we named `StartWorldPos_Rectangle` and create a connection from the field <field>End World Pos</field> to the vector of module `EndWorldPos_Rectangle`. The decomposed coordinates can be now used for further parameter connections.

![Parameter Connections](images/tutorials/visualization/V2_09.png "Parameter Connections")

Open the panel of the module `SubImage`. Select the <field>Mode World Start & End</field> (<field>Image Axis Aligned</field>). Enable the function <field>Auto apply</field>.

{{<alert class="info" caption="Extra Infos">}}
Make sure to also check <field>Auto-correct for negative subimage extents</field>, so that you can draw rectangles from left to right and from right to left.
{{</alert>}}

![World Coordinates](images/tutorials/visualization/V2_10.png "World Coordinates")

Now, create parameter connections from the fields <field>X</field>, <field>Y</field>, <field>Z</field> of the module `StartWorldPos_Rectangle` to the field <field>Start X</field>, <field>Start Y</field>, <field>Start Z</field> in the panel of the module `SubImage`. Similarly, connect the parameter fields <field>X</field>, <field>Y</field>, <field>Z</field> of the module `EndWorldPos_Rectangle` to the field <field>End X</field>, <field>End Y</field>, <field>End Z</field> in the panel of the module `SubImage`.

![Another Parameter Connection](images/tutorials/visualization/V2_11.png "Another Parameter Connection")

With this, you finished your magnifier. Open the viewer and draw a rectangle on one slice to see the result.

![Final Magnifier with SubImage](images/tutorials/visualization/V2_12.png "Final Magnifier with SubImage")

## Exercises
Invert the image inside your magnified `SubImage` without changing the original image. You can use `Arithmetic*` modules for inverting.

## Summary
* The module `OrthoView2D` provides coronal, axial, and sagittal views of an image.
* The `SubImage` module allows to define a region of an input image to be treated as a separate image.
* Single x, y, and z coordinates can be transferred to a 3-dimensional vector and vice versa by using `ComposeVector3` and `DecomposeVector3`.
* Some modules provide hidden inputs and outputs that can be shown via {{< keyboard "SPACE" >}}.

{{< networkfile "examples/visualization/example2/VisualizationExample2.mlab" >}}
