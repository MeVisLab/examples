---
title: "Surface Example 4: Interactively Moving WEM"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 720
tags: ["Beginner", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM"]
menu: 
  main:
    identifier: "surfaceexample4"
    title: "Example for Implementing WEM Translations via Mouse Interaction"
    weight: 720
    parent: "surfaces"
---

# Surface Example 4: Interactively Moving WEM

{{< youtube "WKiCddNGKrw">}}

## Introduction
In this example, we like to interactively move WEMs using `SoDragger` modules inside a viewer.

### Develop Your Network

### Interactively Translating Objects in 3D Using SoDragger Modules
Add and connect the following modules as shown. On the panel of the module `WEMInitialize`, select the <field>Model</field> *Octasphere*. After that, open the viewer `SoExaminerViewer` and make sure to select the *Interaction Mode*. Now, you are able to click {{< mousebutton "left" >}} on the presented *Octasphere* and move it alongside one axis. The following modules are involved in the interactions: 

* `SoMITranslate1Dragger`: This module allows interactive translation of the object alongside one axis. You can select the axis for translation in the panel of the module.
* `SoMIDraggerContainer`: This module is responsible for actually changing the translation values of the object.

![Initial network](images/tutorials/dataobjects/surfaces/DO10_01.png "Initial network")

### Interactively Translating a WEM Alongside Three Axes
We like to be able to interactively move a WEM alongside all three axes. In MeVisLab, there is the module `SoMITranslate2Dragger`, which allows translations alongside two axes, but there is no module that allows object translation in all three directions. Therefore, we will create a network that solves this task. The next steps will show you how you create three planes intersecting the objects. Dragging one plane will drag the object alongside one axis. In addition, these planes will only be visible when hovering over them.

#### Creation of Planes Intersecting an Object
We start creating a plane that will allow dragging in the x-direction. In order to do that, modify your network as shown: Add the modules `WEMModify` and `SoBackground`, and connect the module `SoCube` to the dragger modules. You can select the translation direction in the panel of `SoMITranslate1Dragger`. 

![Network for dragging alongside one axis](images/tutorials/dataobjects/surfaces/DO10_02.png "Network for dragging alongside one axis")

We will modify the cube to be able to use it as a dragger plane. In order to do this, open the panel of `SoCube` and reduce the <field>Width</field> to be *0*. This defines a plane in the y- and z-direction. 

![Parameters for showing a plane](images/tutorials/dataobjects/surfaces/DO10_02_1.png "Parameters for showing a plane")

We want to move the object when dragging the plane. Thus, we need to modify the translation of our object when moving the plane. Open the panels of the modules `WEMModify` and `SoMIDraggerContainer` and establish a parameter connection from one <field>Translation</field> vector to the other. 

![Dragging alongside an axis maps to a translation](images/tutorials/dataobjects/surfaces/DO10_03.png "Dragging alongside an axis maps to a translation")

As a next step, we want to adapt the size of the plane to the size of the object we have. Add the modules `WEMInfo` and `DecomposeVector3` to your workspace and open their panels. The module `WEMInfo` presents information about the given WEM, for example, its position and size. The module `DecomposeVector3` splits a 3D vector into its components. Now, establish a parameter connection from <field>Size</field> of `WEMInfo` to the vector in `DecomposeVector3`. As a next step, open the panel of `SoCube` and establish parameter connections from the fields <field>Y</field> and <field>Z</field> of `DecomposeVector3` to <field>Height</field> and <field>Depth</field> of `SoCube`. Now, the size of the plane adapts to the size of the object. 

![Dynamic size of the plane](images/tutorials/dataobjects/surfaces/DO10_04.png "Dynamic size of the plane")

The result can be seen in the next image. You can now select the plane in the *Interaction Mode* of the module `SoExaminerViewer` and move the plane together with the object alongside the x-axis.

![Network for dragging alongside one axis](images/tutorials/dataobjects/surfaces/DO10_05.png "Network for dragging alongside one axis")

#### Modifying the Appearance of the Plane
For changing the visualization of the dragger plane, add the modules `SoGroup`, `SoSwitch`, and `SoMaterial` to your network and connect them as shown. In addition, group all modules together that are responsible for the translation in the x-direction.

![Different materials and grouping of modules](images/tutorials/dataobjects/surfaces/DO10_06.png "Different materials and grouping of modules")

We want to switch the visualization of the plane depending on the mouse position in the viewer. In other words, when hovering over the plane, the plane should be visible, and when the mouse is in another position and the possibility to drag the object is not given, the plane should be invisible. We use the module `SoMaterial` to edit the appearance of the plane. Open the panel of the module `SoMITranslate1Dragger`. The checkbox of the field <field>Highlighted</field> is ticked when the mouse hovers over the plane. Thus, we can use the field's status to switch between different presentations of the plane. In order to do this, open the panel of `SoSwitch` and establish a parameter connection from <field>Highlighted</field> of `SoMITranslate1Dragger` to <field>Which Child</field> of `SoSwitch`.

![Controling the visibility of the plane](images/tutorials/dataobjects/surfaces/DO10_06_02.png "Controling the visibility of the plane")

Open the panels of the modules `SoMaterial`. Change the <field>Transparency</field> of the first `SoMaterial` module to make the plane invisible when not hovering over the plane. Furthermore, we changed the <field>Diffuse Color</field> of the module `SoMaterial1` to red, so that the plane appears in red when hovering over it.

![Setting visual parameters for the plane](images/tutorials/dataobjects/surfaces/DO10_07.png "Setting visual parameters for the plane")

When hovering over the plane, the plane becomes visible and the option to move the object alongside the x-axis is given. When you do not hover over the plane, the plane is invisible.

![Showing the plane in red](images/tutorials/dataobjects/surfaces/DO10_08.png "Showing the plane in red")

#### Interactive Object Translation in Three Dimensions
We do not only want to move the object in one direction, we like to be able to do interactive object translations in all three dimensions. For this, copy the modules responsible for the translation in one direction and change the properties to enable translations in other directions.

We need to change the size of `SoCube1` and `SoCube2` to form planes that cover surfaces in x- and z-, as well as x- and y-directions. To do that, establish the respective parameter connections from `DecomposeVector3` to the fields of the modules `SoCube`. In addition, we need to adapt the field <field>Direction</field> in the panels of the modules `SoMITranslate1Dragger`. 

![Dragging in all three cardinal directions](images/tutorials/dataobjects/surfaces/DO10_09.png "Dragging in all three cardinal directions")

Change width, height, and depth of the three cubes, so that each of them represents one plane. The values need to be set to *(0, 2, 2)*, *(2, 0, 2)*, and *(2, 2, 0)*.

As a next step, we like to make sure that all planes always intersect the object, even though the object is moved. To do this, we need to synchronize the field <field>Translation</field> of all `SoMIDraggerContainer` modules and the module `WEMModify`. Establish parameter connections from one <field>Translation</field> field to the next, as shown below.

![Setting the initial translation](images/tutorials/dataobjects/surfaces/DO10_10.png "Setting the initial translation")

We like to close the loop, so that a change in one field <field>Translation</field> causes a change in all the other <field>Translation</field> fields. To do this, we need to include the module `SyncVector`. The module `SyncVector` avoids an infinite processing loop causing a permanent update of all fields <field>Translation</field>.

Add the module `SyncVector` to your workspace and open its panel. Establish a parameter connection from the field <field>Translation</field> of the module `SoMIDraggerContainer2` to <field>Vector1</field> of `SyncVector`. The field <field>Vector1</field> is automatically synchronized to the field <field>Vector2</field>. Now, connect the field <field>Vector2</field> to the field <field>Translate</field> of the module `WEMModify`. Your synchronization network is now established.

![Avoiding an infinite processing loop](images/tutorials/dataobjects/surfaces/DO10_11.png "Avoiding an infinite processing loop")

To enable transformations in all directions, we need to connect the modules `SoMIDraggerContainer` to the viewer. First, connect the modules to `SoGroup`, after that, connect `SoGroup` to `SoExaminerViewr`.

![All draggers are connected](images/tutorials/dataobjects/surfaces/DO10_12.png "All draggers are connected")

As a next step, we like to enlarge the planes to make them exceed the object. For that, add the module `CalculateVectorFromVectors` to your network. Open its panel and connect the field <field>Size</field> of `WEMInfo` to <field>Vector1</field>. We like to enlarge the size by one, so we add the vector *(1, 1, 1)*, by editing the field <field>Vector2</field>. Now, connect the <field>Result</field> to the field <field>V</field> of the module `DecomposeVector3`.

![Enlarging the initial size of the planes](images/tutorials/dataobjects/surfaces/DO10_13.png "Enlarging the initial size of the planes")

At last, we can condense all the modules enabling the transformation into one local macro module. For that, group all the modules together and convert the group into a macro module as shown in [Chapter I: Basic Mechanisms](tutorials/basicmechanisms#TutorialMacroModules).

![All dragger modules are selected](images/tutorials/dataobjects/surfaces/DO10_14.png "All dragger modules are selected")

The result can be seen in the next image. This module can now be used for interactive 3D translations for all kinds of WEMs.

![Final network](images/tutorials/dataobjects/surfaces/DO10_15.png "Final network")

## Summary
* A family of `SoDragger` modules is available that can be used to interactively modify Open Inventor objects.

{{< networkfile "examples/data_objects/surface_objects/example4/SurfaceExample4.zip" >}}
