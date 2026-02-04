---
title: "Surface Example 5: WEM - Primitive Value Lists"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 725
tags: ["Advanced", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM", "PVM", "Primitive Value Lists", "LUT"]
menu: 
  main:
    identifier: "surfaceexample5"
    title: "Examples How to Calculate Distances Between WEM Objects"
    weight: 725
    parent: "surfaces"
---

# Surface Example 5: WEM - Primitive Value Lists

{{< youtube "Rap1RY6l5Cc">}}

## Introduction
WEMs do not only contain the coordinates of nodes and surfaces, they can also contain additional information. That information is stored in so-called *Primitive Value Lists* (PVLs). Every node, every surface, and every edge can contain such a list. In these lists, you can, for example, store the color of the node or specific patient information. This information can be used for visualization or for further statistical analysis.

In this example we like to use PVLs to color-code and visualize the distance between two WEMs.

## Steps to Do

### Develop Your Network
We start our network by initializing two WEMs using `WEMInitialize`. We chose an *Octasphere* and a resized *Cube*. Use the modules `SoWEMRenderer`, `SoExaminerViewer`, and `SoBackground` to visualize the WEMs.

![WEMInitialize](images/tutorials/dataobjects/surfaces/DO12_01.png "WEMInitialize")

#### Subdividing WEM Edges
As a next step, add and connect two modules `WEMSubdivide` to further divide edges and surfaces. With this step we increase the node density to have an accurate distance measurement.

![WEMSubdivide](images/tutorials/dataobjects/surfaces/DO12_02.png "WEMSubdivide")

The difference when selecting different maximum edge lengths can be seen in the following images.

{{< imagegallery 2 "images/tutorials/dataobjects/surfaces" "EdgeLength1" "EdgeLength01">}}

#### Distances Between WEMs are Stored in PVLs
Now, add the modules `WEMSurfaceDistance` and `WEMInfo` to your workspace and connect them as shown. `WEMSurfaceDistance` calculates the minimum distance between the nodes of both WEM. The distances are stored in the nodes' PVLs as LUT values.

![Distances between surfaces](images/tutorials/dataobjects/surfaces/DO12_05.png "Distances between surfaces")

Open the panels of the modules `WEMSurfaceDistance` and `WEMInfo`. In the panel of `WEMInfo` select the tab *Statistics*. You can see the statistics of the stored PVLs. The *Minimum Value* and the *Maximum Value* are similar to the calculated *Min Dist.* and *Max. Dist.* of `WEMSurfaceDistance`.

![WEM information](images/tutorials/dataobjects/surfaces/DO12_06.png "WEM information")

#### Color-coding the Distance Between WEMs
What can we do with this information? We can use the calculated distances, stored in LUT values, to color-code the distance between the WEMs. For this, add and connect the module `SoLUTEditor`. Each LUT value from the PVLs will in the next step be translated into a color. But first, open the panel of `SoWEMRenderer` to select the *Color Mode* *LUT Values*. Now, the module `SoLUTEditor` defines the coloring of the WEM.

![SoWEMRenderer](images/tutorials/dataobjects/surfaces/DO12_07.png "SoWEMRenderer")

To translate the LUT values from the PVLs into color, open the panel of `SoLUTEditor` and select the tab *Range*. We need to define the value range we like to work with. As the distance and thus the PVL value is expected to be 0 when the surfaces of both WEMs meet, we set the *New Range Min* to 0. As the size of the WEMs does not exceed 3, we set the *New Range Max* to 3. After that, press *Apply New Range*.

![SoLUTEditor](images/tutorials/dataobjects/surfaces/DO12_08.png "SoLUTEditor")

Our goal is to colorize faces of the *Octasphere* in red if they are close to or even intersect the cubic WEM. And we like to colorize faces of the *Octasphere* in green if these faces are far away from the cubic WEM.

Open the tab *Editor* of the panel of `SoLUTEditor`. This tab allows to interactively select a color for each PVL value. Select the color point on the left side. Its <field>Position</field> value is supposed to be *0*, so we like to set the *Color* to *red* in order to color-code small distances between the WEMs in red. In addition to that, increase the <field>Opacity</field> of this color point. Next, select the right color point. Its <field>Position</field> is supposed to be *3* and thus equals the value of the field <field>New Range Max</field>. As these color points colorize large distances between WEMs, set the Color to *green*. You can add new color points by clicking on the colorized bar in the panel. Select, for example, the Color *yellow* for a color point in the middle. Select and shift the color points to get the desired visualization.

![Changing the LUT](images/tutorials/dataobjects/surfaces/DO12_09.png "Changing the LUT")

Add the module `WEMModify` to your workspace and connect the module as shown. If you now shift the WEM using `WEMModify`, you can see that the colorization adapts.

![WEMModify](images/tutorials/dataobjects/surfaces/DO12_10.png "WEMModify")

### Interactive Shift of WEMs
As a next step, we like to implement the interactive shift of the WEM. Add the modules `SoTranslateDragger1` and `SyncVector`. Connect all translation vectors: Draw connections from the field <field>Translate</field> of `SoTranslateDragger1` to <field>Vector1</field> of `SyncVector`, from <field>Vector2</field> of `SyncVector` to <field>Translate</field> of `WEMModify`, and at last from <field>Translate</field> of `WEMModify` to <field>Translate</field> of `SoTranslateDragger1`.

You can now interactively drag the WEM inside the viewer.

![Dragging the WEM](images/tutorials/dataobjects/surfaces/DO12_11.png "Dragging the WEM")

At last, exchange the `WEMInitialize` module showing the cube with `WEMLoad` and load *venus.off*. You can decrease the <field>Face Alpha</field> in the panel of `SoWEMRenderer1` to make that WEM transparent.

![WEM transparency](images/tutorials/dataobjects/surfaces/DO12_12.png "WEM transparency")

The result can be seen in the next image.

![Your final result](images/tutorials/dataobjects/surfaces/DO12_13.png "Your final result")

## Summary
* Additional information of WEMs can be stored in *Primitive Value Lists* (PVL), attached to nodes, edges, or faces.
* The module `WEMSurfaceDistance` stores the minimum distance between nodes of different WEMs in PVLs as LUT values.
* PVLs containing LUT values can be used to color-code additional information on the WEM surface.

{{< networkfile "examples/data_objects/surface_objects/example5/SurfaceExample5.mlab" >}}
