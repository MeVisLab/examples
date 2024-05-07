---
title: "Example 1: Open Inventor Objects"
date: 2022-06-15T08:56:33+02:00
draft: false
weight: 510
status: "OK"
tags: ["Beginner", "Tutorial", "Open Inventor", "3D"]
menu: 
  main:
    identifier: "openinventorobjects"
    title: "Create Open Inventor objects, change their Material, translate location in 3D and general explanation about Scene Graphs."
    weight: 510
    parent: "openinventor"
---

# Example 1: Open Inventor Objects {#TutorialOpenInventorModules}

{{< youtube "aFCK_aqmPsg" >}}

## Introduction
In this example, we'll learn to construct Open Inventor scenes in which three-dimensional objects of different colors and shapes are displayed.

## Steps to do
### Generating Open Inventor Objects {#TutorialGenerateOpenInventorObjects}

First, add the modules `SoExaminerViewer` and `SoCone` to the workspace and connect both modules as shown. The module `SoCone` creates a cone shaped object, which can be displayed in the `SoExaminerViewer`.

![SoExaminerViewer](/images/tutorials/openinventor/OI1_01.png "SoExaminerViewer")

To change the color of the cone, add the `SoMaterial` module to the workspace and connect the module as shown below. When creating an Open Inventor scene (by creating networks of Open Inventor modules), the sequence of module connections, in this case the sequence of the inputs to the module `SoExaminerViewer` determines the functionality of the network.

Open Inventor modules are executed like scene graphs. This means, modules are executed from top to bottom and from left to right. Here, it is important to connect the module `SoMaterial` to an input on the left side of the connection between `SoCone` and `SoExaminerViewer`. We do so to make sure that the selected color attribute is applied to all objects whose connections are placed to the right of it. Now, open the panel of the module `SoMaterial` and select any *Diffuse Color* you like. We chose green in this example.

![Colors and Material in Open Inventor](/images/tutorials/openinventor/OI1_02.png "Colors and Material in Open Inventor")

To add a second object to the scene, add the `SoSphere` module to the workspace and connect it to the `SoExaminerViewer`. 

{{<alert class="info" caption="Info">}}
Observe that when connecting the `SoSphere` module to an input on the right side of the connection between the viewer and the `SoMaterial` module, the sphere also turns green, confirming the traversal order.
{{</alert>}}

 Currently, both objects are displayed in the same position.

![Adding a SoSphere](/images/tutorials/openinventor/OI1_03.png "Adding a SoSphere")

To change an objects position and avoid overlapping of objects, add the modules `SoSeparator` and `SoTransform` to the scene and connect both modules as shown on the following screenshot. To display both objects at different positions, add . Open the panel of `SoTransform` and implement a translation in x-direction to shift the object. Now you can examine two things:

1. The sphere loses its green color
2. The cone shifts to the side

![Transformation](/images/tutorials/openinventor/OI1_05.png "Transformation")

The module `SoTransform` is responsible for shifting objects, in this case the cone, to the side. The module `SoSeparator` ensures that only the cone is shifted and also only the cone is colored green. It separates this features from the rest of the scene.

To add a third object, a cube, to the scene and shift it to the other side of the sphere, add the modules `SoCube` and `SoTransform` to the workspace and connect both modules as shown below. To shift the cube to the other side of the sphere, open the panel of `SoTransform` and adjust the Translation in x direction. The sphere is not affected by the translation, as the connection from `SoTransform1` to `SoExaminerViewer` is established on the right side of the connection between `SoSphere` and `SoExaminerViewer`.

![Adding a SoCube](/images/tutorials/openinventor/OI1_07.png "Adding a SoCube")

Again, the `SoMaterial` module can be used to select a color for the cone and the sphere:

![Multiple Materials](/images/tutorials/openinventor/OI1_08.png "Multiple Materials")

For easier handling we group an object with its applied features by using the module `SoGroup`. This does not separate features, which is the reason for the colored cube. All modules that are derived from `SoGroup` offer a basically infinite number of input connectors (a new connector is added for every new connection).

![SoGroup](/images/tutorials/openinventor/OI1_09.png "SoGroup")

If we don't wish to color the cube, we have to exchange the module `SoGroup` with another `SoSeparator` module.

![SoSeparator](/images/tutorials/openinventor/OI1_10.png "SoSeparator")

All objects can be grouped together.

![Grouping](/images/tutorials/openinventor/OI1_11.png "Grouping")

In addition to the objects, a background can be added to the scene using the module `SoBackground`.

![SoBackground](/images/tutorials/openinventor/OI1_12.png "SoBackground")

## Summary
* Scene objects are represented by nodes.
* Size and position are defined by transformation nodes.
* A rendering node represents the root of the scene graph.
* Nodes are rendered in order of traversal.
* Nodes on the same level are traversed from left to right.
* All modules that are derived from `SoGroup` offer a basically infinite number of input connectors (a new connector is added for every new connection).

{{< networkfile "examples/open_inventor/example1/OpenInventorExample1.mlab" >}}
