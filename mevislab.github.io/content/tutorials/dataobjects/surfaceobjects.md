---
title: "Surface Objects (WEM)"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM"]
menu: 
  main:
    identifier: "surfaces"
    title: "Surface Objects (WEM) in MeVisLab"
    weight: 700
    parent: "dataobjects"
---
# Surface Objects (WEMs){#WEMs}
## Introduction
In MeVisLab it is possible to create, visualize, process and manipulate surface objects, also known as polygon meshes. Here, we call surface objects *Winged Edge Mesh*, in short WEM. In this chapter you will get an introduction into WEMs. In addition, you will find examples on how to work with WEMs. For more information on WEMs take a look at the {{< docuLinks "/Resources/Documentation/Publish/SDK/ToolBoxReference/WEMDataStructure.html" "MeVislab Toolbox Reference" >}}. If you like to know which WEM formats can be imported into MeVisLab, take a look at the assimp documentation [here](https://github.com/assimp/assimp).

[//]: <> (MVL-653)

## WEM explained with MeVisLab
To explain WEMs in MeVisLab we will build a network, which shows the structure and the characteristics of WEMs. We will start the example by generating a WEM forming a cube. With this, we will explain structures of WEMs called *Edges*, *Nodes*, *Surfaces*, and *Normals*.

### Initialize a WEM
Add the module `WEMInitialize` to your workspace, open its panel and select a *Cube*. In general, a WEM is made up of surfaces. Here all surfaces are squares. In MeVisLab it is common to build WEMs out of triangles.

![WEM initializing](/images/tutorials/dataobjects/surfaces/WEM_01_1.png "WEM initializing")

### Rendering of WEMs

For rendering WEMs, you can use the module `SoWEMRenderer` in combination with the viewer `SoExaminerViewer`. Add both modules to your network and connect them as shown. A background is always a nice feature to have.
![WEM rendering](/images/tutorials/dataobjects/surfaces/WEM_01_2.png "WEM rendering")

### Geometry of WEMs
The geometry of WEMs is given by different structures. Using specialized WEM-Renderer modules, all structures can be visualized.
#### Edges
Add and connect the module `SoWEMRendererEdges` to your workspace to enable the rendering of WEM Edges. Here, we manipulated the line thickness, to make the lines of the edges thicker. 
![WEM Edges](/images/tutorials/dataobjects/surfaces/WEM_01_3.png "WEM Edges")
#### Nodes
Nodes mark the corner points of each surface. Therefore, nodes define the geometric properties of every WEM. To visualize the nodes, add and connect the module `SoWEMRendererNodes` as shown. Per default, the nodes are visualized with an offset to the position they are located in. We reduced the offset to be zero, increased the point size and changed the color. 
![WEM Nodes](/images/tutorials/dataobjects/surfaces/WEM_01_4.png "WEM Nodes")
#### Faces
Between the nodes and alongside the edges surfaces are created. The rendering of these surfaces can be enabled and disabled using the panel of `SoWEMRenderer`.
![WEM Faces](/images/tutorials/dataobjects/surfaces/WEM_01_5.png "WEM Faces")
#### Normals
Normals display the orthogonal vector either to the faces (Face Normals) or to the nodes (Nodes Normals). With the help of the module `SoWEMRendererNormals` these structures can be visualized.  
![WEM normal editor](/images/tutorials/dataobjects/surfaces/WEM_01_6.png "WEM normal editor")
{{< imagegallery 2 "images/tutorials/dataobjects/surfaces/" "WEMNodeNormals" "WEMFaceNormals">}}

### WEMs in MeVisLab {#WEMsInMevislab}
In MeVisLab WEMs can consist of triangles, squares or other polygons. Most common in MeVisLab are surfaces composed of triangles, as shown in the following example. With the help of the module `WEMLoad` existing WEMs can be loaded into the network.

{{< imagegallery 3 "images/tutorials/dataobjects/surfaces/" "WEMTriangles" "WEMNetwork" "WEMSurface" >}}

## Summary
* WEMs are polygon meshes, in most cases composed of triangles
* WEM's geometry is determined by nodes, edges, faces and normals, which can be visualized using renderer modules

