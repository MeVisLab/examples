---
title: "Surface Example 3: Interactions With WEM"
date: "2023-03-21"
status: "OK"
draft: false
weight: 715
tags: ["Beginner", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM"]
menu: 
  main:
    identifier: "surfaceexample3"
    title: "Interactions With WEM"
    weight: 715
    parent: "surfaces"
---

# Surface Example 3: Interactions with WEM

{{< youtube "YDOEqCOmUFw">}}

## Introduction
In these examples, we are showing two different possibilities to interact with the visualization of the WEM:
* Scale, rotate, and move a WEM's visualization in a scene
* Modify a WEM in a scene

### Scale, Rotate, and Move a WEM in a Scene
We are using a `SoTransformerDragger` module to apply transformations to the visualization of a 3D WEM object via mouse interactions.

Add a `SoCube` and a `SoBackground` module and connect both to a `SoExaminerViewer`. For a better understanding, you should also add a `SoCoordinateSystem` module and connect it to the viewer. Change the *User Transform Mode* to *User Transform Instead Of Input* and set *User Scale* to 2 for *x*, *y*, and *z*.

![Initial Network](images/tutorials/dataobjects/surfaces/WEMExample3_1.png "Initial Network")

The `SoExaminerViewer` shows your cube and the world coordinate system. You can interact with the camera (rotate, zoom, and pan), the visualization of the cube itself does not change. It remains in the center of the coordinate system.

![Initial Cube](images/tutorials/dataobjects/surfaces/WEMExample3_2.png "Initial Cube")

Scaling, rotating, and translating the visualization of the cube can be done by using the module `SoTransformerDragger`.

Additionally, add a `SoTransform` module to your network. Add all modules except the `SoCoordinateSystem` to a `SoSeparator`, so that transformations are not applied to the coordinate system.

![SoTransformerDragger and SoTransform](images/tutorials/dataobjects/surfaces/WEMExample3_3.png "SoTransformerDragger and SoTransform")

Draw parameter connections from *Translation*, *Scale Factor*, and *Rotation* of the `SoTransformerDragger` to the same fields of the `SoTransform` module.

Opening your SoExaminerViewer now allows you to use handles of the `SoTransformerDragger` to scale, rotate, and move the visualization of the cube. The cube itself remains unchanged in memory, a matrix for translation is applied to the original 3D object's visualization.

You can additionally interact with the camera as already done before.

{{<alert class="info" caption="Info">}}
You need to change the active tool on the right side of the `SoExaminerViewer`. Use the *Pick Mode* for applying transformations and the *View Mode* for adjusting the camera.
{{</alert>}}

![Moved, Rotated, and Scaled Cube](images/tutorials/dataobjects/surfaces/WEMExample3_4.png "Moved, Rotated, and Scaled Cube")

You can also try the other `So*Dragger` modules in MeVisLab for variations of the `SoTransformerDragger`.

{{< networkfile "examples/data_objects/surface_objects/example3/SurfaceExample3.mlab" >}}

### Interactively Modify WEMs
The big difference to the previously described scenario, where we modified the visualization of the WEM, is that this example modifies the WEM itself.

We are using the `WEMBulgeEditor` module to interactively modify the WEM via mouse interactions.

Add the modules `WEMInitialize`, `SoWEMRenderer`, and `SoBackground` to your workspace and connect them to a `SoExaminerViewer` as seen below. Select model *Icosahedron* for the `WEMInitialize` module.

![WEMLoad and SoWEMRenderer](images/tutorials/dataobjects/surfaces/WEMExample3_5.png "WEMLoad and SoWEMRenderer")

You can see the WEM and interact with it in the viewer (zoom, move, and rotate). In the case the object does not rotate around its center, trigger the field *viewAll* of the `SoExaminerViewer`.

Add a `WEMBulgeEditor` and a `SoWEMBulgeEditor` to your network and connect them as seen below. 

![WEMBulgeEditor and SoWEMBulgeEditor](images/tutorials/dataobjects/surfaces/WEMExample3_6.png "WEMBulgeEditor and SoWEMBulgeEditor")

Opening the viewer, you can still not edit the object.

We need a lookup table (LUT) to interact with the WEM. Add a `WEMGenerateStatistics` between the WEMInitialize and the WEMBulgeEditor. The module `WEMGenerateStatistics` generates node, edge, and face statistics of a WEM and stores the information in the WEM's Primitive Value Lists.

{{<alert class="info" caption="Info">}}
More information about Primitive Value Lists (PVL) can be found in [Surface Example 5](tutorials/dataobjects/surfaces/surfaceexample5).
{{</alert>}}

Check *New node PVL* and set *New PVL Name* to *myPVL*.

![WEMGenerateStatistics](images/tutorials/dataobjects/surfaces/WEMExample3_7.png "WEMGenerateStatistics")

In the `WEMBulgeEditor`, set *PVL Used as LUT Values* to previously generated *myPVL*.

![WEMBulgeEditor PVL](images/tutorials/dataobjects/surfaces/WEMExample3_8.png "WEMBulgeEditor PVL")

Add a `SoLUTEditor` and connect it to `SoWEMRenderer`. You also have to connect the `WEMGenerateStatistics` to the `SoWEMRenderer`. Set `SoWEMRenderer` *Color Mode* to *Lut Values* and select *PVL Used as LUT Values* to *myPVL*.

![Final Network](images/tutorials/dataobjects/surfaces/WEMExample3_10.png "Final Network")

Open the panel of the `SoLUTEditor`. Configure *New Range Min* as -1 and *New Range Max* as 1 in *Range* tab. Apply the new range. Define the LUT as seen below in *Editor* tab.

![SoLUTEditor](images/tutorials/dataobjects/surfaces/WEMExample3_9.png "SoLUTEditor")

Now, your Primitive Value List is used to colorize the affected region for your tansformations. You can see the region by the color on hovering the mouse over the WEM.

![Affected region colored](images/tutorials/dataobjects/surfaces/Affected_Region.png "Affected region colored")

The size of the region can be changed via {{<keyboard "ALT" >}} and mouse wheel {{< mousebutton "middle" >}}. Make sure that the *Influence Radius* in `WEMBulgeEditor` is larger than 0.

{{<alert class="info" caption="Info">}}
You need to change the active tool on the right side of the `SoExaminerViewer`. Use the *Pick Mode* for applying transformations and the *View Mode* for adjusting the camera.
{{</alert>}}

![Modify WEM](images/tutorials/dataobjects/surfaces/Modify.png "Modify WEM")

{{< networkfile "examples/data_objects/surface_objects/example3/WEMExample3b.mlab" >}}

A much more complex example using medical images and allowing to modify in 3D and on 2D slices can be seen by opening the example network of the `WEMBulgeEditor`.

![WEMBulgeEditor Example Network](images/tutorials/dataobjects/surfaces/WEMExample3_11.png "WEMBulgeEditor Example Network")

{{<alert class="info" caption="Info">}}
For other interaction possibilities, you can play around with the example networks of the modules `SoCSODrawOnSurface`, `SoVolumeCutting` and `WEMExtrude`.
{{</alert>}}

## Summary
* MeVisLab provides multiple options to interact with 3D surfaces.
* Modules of the `So\*Dragger` family allow to scale, rotate, and translate a WEM.
* You can always use a `SoCoordinateSystem` to see the current world coordinates.
* The `WEMBulgeEditor` allows you to interactively modify a WEM via mouse.
