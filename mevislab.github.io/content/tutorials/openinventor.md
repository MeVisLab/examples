---
title: "Chapter II: Open Inventor"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Open Inventor", "3D"]
menu: 
  main:
    identifier: "openinventor"
    title: "Examples for handling Open Inventor Modules and Scene Graphs in MeVisLab."
    weight: 500
    parent: "tutorials"
---

# Open Inventor Modules {#TutorialOpenInventorModules}
## Introduction

Besides blue modules (ML Modules) and brown macro modules, there is a third type of modules, called Open Inventor modules. These modules are green and start with the letters `So\*` (for Scene Objects). Open Inventor Modules process and render 3D scene objects and enable image interactions. Scene objects are transmitted via round input and output connectors. With the help of these modules, Open Inventor scenes can be implemented.

This chapter will start with an example Open Inventor scene. Explanations to Open Inventor scenes will follow the example.

## Open Inventor Scenes and Execution of Scene Graphs{#sceneGraphs}

Inventor scenes are organized in structures called scene graphs. A scene graph is made up of nodes, which represent 3D objects to be drawn, properties of the 3D objects, nodes that combine other nodes and are used for hierarchical grouping, and others (cameras, lights, etc.). These nodes are accordingly called shape nodes, property nodes, group nodes and so on. Each node contains one or more pieces of information stored in fields. For example, the Sphere node contains only its radius, stored in its *radius* field. Open Inventor modules function as Inventor nodes, so they may have input connectors to add Inventor child nodes (modules) and output connectors to link themselves to Inventor parent nodes (modules).

{{<alert class="info" caption="Open Inventor Scenes">}}
The following shows the order in which the modules are executed. The red arrow shows the order of traversal, from top to bottom and left to right. The numbers designate the order in which each module is passed first, from 1 to 8. As shown in the example before, the order of transversal is important.

![Traversing in Open Inventor](/images/tutorials/openinventor/OI1_13.png "Traversing in Open Inventor")

{{</alert>}}

{{<alert class="info" caption="Extra Info">}}
More Information about Open Inventor and Scene Graphs can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch07.html" "here" >}} or else in the {{< docuLinks "/Standard/Documentation/Publish/Overviews/OpenInventorOverview.html" "Open Inventor Overview" >}} and the [Open Inventor Reference](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html)
{{</alert>}}

## Examples:
1. [Open Inventor Objects](./tutorials/openinventor/openinventorobjects)
2. [Mouse Interactions in Open Inventor](./tutorials/openinventor/mouseinteractions)
3. [Camera Interactions](./tutorials/openinventor/camerainteraction)