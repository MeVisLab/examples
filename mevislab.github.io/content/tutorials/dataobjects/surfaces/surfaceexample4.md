---
title: "Surface Example 4: Interactively moving WEM"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 720
tags: ["Beginner", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM"]
menu: 
  main:
    identifier: "surfaceexample4"
    title: "Example for implementing WEM translations via mouse interaction"
    weight: 720
    parent: "surfaces"
---
# Surface Example 4: Interactively Moving WEM

{{< youtube "WKiCddNGKrw">}}

## Introduction
In this example, we like to interactively move WEMs using `SoDragger` modules inside a viewer.

### Develop Your Network
### Interactively Translating Objects in 3D Using SoDragger Modules
Add and connect the following modules as shown. On the panel of the module `WEMInitialize`, select the *Model* *Octasphere*. After that, open the viewer `SoExaminerViewer` and make sure to select the *Interaction Mode*. Now, you are able to click on the presented *Octasphere* and move it alongside one axis. The following modules are involved in the interactions: 

* `SoMITranslate1Dragger`: This module allows interactive translation of the object alongside one axis. You can select the axis for translation in the panel of the module.
* `SoMIDraggerContainer`: This module is responsible for actually changing the translation values of the object.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_01.png "Interactive dragging of objects")

### Interactively Translating a WEM Alongside Three Axes
We like to be able to interactively move a WEM alongside all three axes. In MeVisLab, there is the module `SoMITranslate2Dragger`, which allows translations alongside two axes, but there is no module that allows object translation in all three directions. Therefore, we will create a network that solves this task. The next steps will show you how you create three planes intersecting the objects. Dragging one plane will drag the object alongside one axis. In addition, these planes will only be visible when hovering over them.

#### Creation of Planes Intersecting an Object
We start creating a plane that will allow dragging in x-direction. In order to do that, modify your network as shown: Add the modules `WEMModify` and `SoBackground`, and connect the module `SoCube` to the dragger modules. You can select the translation direction in the panel of `SoMITranslate1Dragger`. 

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_02.png "Interactive dragging of objects")

We will modify the cube to be able to use it as a dragger plane. In order to do this, open the panel of `SoCube` and reduce the *Width* to be 0. This sets a plane in y- and z-direction. 

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_02_1.png "Interactive dragging of objects")

We want to move the object when dragging the plane. Thus, we need to modify the translation of our object when moving the plane. Open the panels of the modules `WEMModify` and `SoMIDraggerContainer` and draw a parameter connection from one *Translation* vector to the other. 

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_03.png "Interactive dragging of objects")

As a next step, we want to adapt the size of the plane to the size of the object we have. Add the modules `WEMInfo` and `DecomposeVector3` to your workspace and open their panels. The module `WEMInfo` presents information about the given WEM, for example, its position and size. The module `DecomposeVector3` splits a 3D vector into its components. Now, draw a parameter connection from *Size* of `WEMInfo` to the vector in `DecomposeVector3`. As a next step, open the panel of `SoCube` and draw parameter connections from the fields *Y* and *Z* of `DecomposeVector3` to *Height* and *Depth* of `SoCube`. Now, the size of the plane adapts to the size of the object. 

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_04.png "Interactive dragging of objects")

The result can be seen in the next image. You can now select the plane in the *Interaction Mode* of the module `SoExaminerViewer` and move the plane together with the object alongside the x-axis.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_05.png "Interactive dragging of objects")

#### Modifying the Appearance of the Plane

For changing the visualization of the dragger plane, add the modules `SoGroup`, `SoSwitch`, and `SoMaterial` to your network and connect them as shown. In addition, group all modules together that are responsible for the translation in the  x-direction.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_06.png "Interactive dragging of objects")

We want to switch the visualization of the plane dependent on the mouse position in the viewer. In other words, when hovering over the plane, the plane should be visible, when the mouse is in another position and the possibility to drag the object is not given, the plane should be invisible. We use the module `SoMaterial` to edit the appearance of the plane. Open the panel of the module `SoMITranslate1Dragger`. The box of the field *Highlighted* is ticked when the mouse hovers over the plane. Thus, we can use the field's status to switch between different presentations of the plane. In order to do this, open the panel of `SoSwitch` and draw a parameter connection from *Highlighted* of `SoMITranslate1Dragger` to *Which Child* of `SoSwitch`.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_06_02.png "Interactive dragging of objects")

Open the panels of the modules `SoMaterial`. Change the *Transparency* of the first `SoMaterial` module to make the plane invisible when not hovering over the plane. Furthermore, we changed the *Diffuse Color* of the module `SoMaterial1` to red, so that the plane appears in red when hovering over it.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_07.png "Interactive dragging of objects")

When hovering over the plane, the plane becomes visible and the option to move the object alongside the x-axis is given. When you do not hover over the plane, the plane is invisible.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_08.png "Interactive dragging of objects")

#### Interactive Object Translation in Three Dimensions
We do not only want to move the object in one direction, we like to be able to do interactive object translations in all three dimensions. For this, copy the modules responsible for the translation in one direction and change the properties to enable translations in other directions.

We need to change the size of `SoCube1` and `SoCube2` to form planes that cover surfaces in x- and z-, as well as x- and y-directions. To do that, draw the respective parameter connections from `DecomposeVector3` to the fields of the modules `SoCube`. In addition, we need to adapt the field *Direction* in the panels of the modules `SoMITranslate1Dragger`. 

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_09.png "Interactive dragging of objects")

Change width, height, and depth of the three cubes so that each of them represents one plane. The values need to be set to (0, 2, 2), (2, 0, 2), and (2, 2, 0). 

As a next step, we like to make sure that all planes always intersect the object, even though the object is moved. To do this, we need to synchronize the field *Translation* of all `SoMIDraggerContainer` modules and the module `WEMModify`. Draw parameter connections from one *Translation* field to the next, as shown below.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_10.png "Interactive dragging of objects")

We like to close the loop, so that a change in one field *Translation* causes a change in all the other *Translation* fields. To do this, we need to include the module `SyncVector`. The module `SyncVector` avoids an infinite processing loop causing a permanent update of all fields *Translation*.

Add the module `SyncVector` to your workspace and open its panel. Draw a parameter connection from the field *Translation* of the module `SoMIDraggerContainer2` to *Vector1* of `SyncVector`. The field *Vector1* is automatically synchronized to the field *Vector2*. Now, connect the field *Vector2* to the field *Translate* of the module `WEMModify`. Your synchronization network is now established.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_11.png "Interactive dragging of objects")

To enable transformations in all directions, we need to connect the modules `SoMIDraggerContainer` to the viewer. First, connect the modules to `SoGroup`, after that connect `SoGroup` to `SoExaminerViewr`.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_12.png "Interactive dragging of objects")

As a next step, we like to enlarge the planes to make them exceed the object. For that, add the module `CalculateVectorFromVectors` to your network. Open its panel and connect the field *Size* of `WEMInfo` to *Vector 1*. We like to enlarge the size by one, so we add the vector (1, 1, 1), by editing the field *Vector 2*. Now, connect the *Result* to the field *V* of the module `DecomposeVector3`.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_13.png "Interactive dragging of objects")

At last, we can condense all the modules enabling the transformation into one local macro module. For that, group all the modules together and convert the group into a macro module as shown in [Chapter I: Basic Mechanisms](tutorials/basicmechanisms#TutorialMacroModules).

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_14.png "Interactive dragging of objects")

The result can be seen in the next image. This module can now be used for interactive 3D transformations for all kinds of WEMs.

![Interactive dragging of objects](images/tutorials/dataobjects/surfaces/DO10_15.png "Interactive dragging of objects")


## Summary
* A family of `SoDragger` modules is available that can be used to interactively modify Open Inventor objects.


{{< networkfile "examples/data_objects/surface_objects/example4/SurfaceExample4.zip" >}}
