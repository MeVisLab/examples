---
title: "Example 1: Open Inventor Objects"
date: 2022-06-15T08:56:33+02:00
draft: false
status: "OK"
tags: ["Beginner", "Tutorial", "Open Inventor", "3D"]
menu: 
  main:
    identifier: "openinventorobjects"
    title: "Create Open Inventor Objects, change Material, Translate location in 3D and general explanation about Scene Graphs."
    weight: 510
    parent: "openinventor"
---

# Example 1: Open Inventor Objects {#TutorialOpenInventorModules}
## Introduction
In this example we like to construct an Open Inventor scene in which we display three 3D objects of different color and shape.


## Steps to do
### Generating Open Inventor Objects {#TutorialGenerateOpenInventorObjects}

First, add the modules `SoExaminerViewer` and `SoCone` to the workspace and connect both modules as shown. The module `SoCone` creates a cone shaped object, which can be displayed in the Viewer `SoExaminerViewer`.

![SoExaminerViewer](/images/tutorials/openinventor/OI1_01.png "SoExaminerViewer")

We like to change the color of the cone. In order to do so, add the module `SoMaterial` to the workspace and connect the module as shown below. When creating an Open Inventor scene (by creating networks of Open Inventor modules), the sequence of module connections, in this case the sequence of the inputs to the module `SoExaminerViewer` determines the functionality of the network.

Open Inventor modules are executed like scene graphs. This means, modules are executed from top to bottom and from left to right. Here, it is important to connect the module `SoMaterial` to an input on the left side of the connection between `SoCone` and `SoExaminerViewer`. With this, we first select features like a color and these features are then assigned to all objects, which were executed afterwards. Now, open the panel of the module `SoMaterial` and select any *Diffuse Color* you like. Here, we choose green.

![Colors and Material in Open Inventor](/images/tutorials/openinventor/OI1_02.png "Colors and Material in Open Inventor")

We like to add a second object to the scene.

In order to do that, add the module `SoSphere` to the workspace. Connect this module to `SoExaminerViewer`. When connecting `SoSphere` to an input on the right side of the connection between the viewer and the module `SoMaterial`, the sphere is also colored in green. One problem now is, that currently both objects are displayed at the same position.

![Adding a SoSphere](/images/tutorials/openinventor/OI1_03.png "Adding a SoSphere")

They display both objects at different positions, add the modules `SoSeparator` and `SoTransform` to the scene and connect both modules shown on the following picture. Open the panel of `SoTransform` and implement a translation in x-direction to shift the object. Now you can examine two things:

1. The sphere loses its green color
2. The cone is shifted to the side

![Transformation](/images/tutorials/openinventor/OI1_05.png "Transformation")

The module `SoTransform` is responsible for shifting objects, in this case the cone, to the side. The module `SoSeparator` ensures that only the cone is shifted and also only the cone is colored in green. It separates this features from the rest of the scene.

We like to add a third object, a cube, and shift it to the other side of the sphere. Add the modules `SoCube` and `SoTransform` to the workspace and connect both modules as shown below. To shift the cube to the other side of the sphere, open the panel of `SoTransform` and adjust the Translation in x direction. The sphere is not affected by the translation, as the connection from `SoTransform1` to `SoExaminerViewer` is established on the right side of the connection between `SoSphere` and `SoExaminerViewer`.

![Adding a SoCube](/images/tutorials/openinventor/OI1_07.png "Adding a SoCube")

Again, we use the module `SoMaterial` to select a color for the cone and the sphere.

![Multiple Materials](/images/tutorials/openinventor/OI1_08.png "Multiple Materials")

For easier handling we group an object together with its features by using the module `SoGroup`. This does not separate features, which is the reason for the cube to be colorized. All modules that are derived from `SoGroup` offer a basically infinite number of input connectors (a new connector is added for every new connection).

![SoGroup](/images/tutorials/openinventor/OI1_09.png "SoGroup")

If we do not want to colorize the cube, we have to exchange the module `SoGroup` by another `SoSeparator` module.

![SoSeparator](/images/tutorials/openinventor/OI1_10.png "SoSeparator")

The implementation of all objects can be grouped together.

![Grouping](/images/tutorials/openinventor/OI1_11.png "Grouping")

In addition to the objects, a background can be added to the scene using the module `SoGBackground`.

![SoBackground](/images/tutorials/openinventor/OI1_12.png "SoBackground")

## Summary
* Scene objects are represented by nodes.
* Size and position is defined by transformation nodes.
* A rendering node represents the root of the scene graph.
* Nodes are rendered in the order of traversal.
* Nodes on the same level are traversed from left to right.
* All modules that are derived from `SoGroup` offer a basically infinite number of input connectors (a new connector is added for every new connection).

{{< networkfile "examples/open_inventor/example1/" >}}
