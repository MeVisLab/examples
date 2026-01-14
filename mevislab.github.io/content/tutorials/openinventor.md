---
title: "Chapter II: Open Inventor"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 500
tags: ["Beginner", "Tutorial", "Open Inventor", "3D"]
menu: 
  main:
    identifier: "openinventor"
    title: "Examples for Handling Open Inventor Modules and Scene Graphs in MeVisLab."
    weight: 500
    parent: "tutorials"
---

# Open Inventor Modules {#TutorialOpenInventorModules}

## Introduction
In total, there are three types of modules:
* blue ML modules
* brown macro modules
* green Open Inventor modules

The names of Open Inventor modules start with the prefix `So\*` (for Scene Objects). Open Inventor modules process and render 3D scene objects and enable image interactions. Scene objects are transmitted using the semicircle-shaped input and output connectors. With the help of these modules, Open Inventor scenes can be implemented.

An exemplary Open Inventor scene will be implemented in the following paragraph.

## Open Inventor Scenes and Execution of Scene Graphs{#sceneGraphs}
Inventor scenes are organized in structures called scene graphs. A scene graph is made up of nodes, which represent 3D objects to be drawn, properties of the 3D objects, nodes that combine other nodes and are used for hierarchical grouping, and others (cameras, lights, etc.). These nodes are accordingly called shape nodes, property nodes, group nodes, and so on. Each node contains one or more pieces of information stored in fields. For example, the `SoSphere` node contains only its radius, stored in its *radius* field. Open Inventor modules function as Open Inventor nodes, so they may have input connectors to add Open Inventor child nodes (modules) and output connectors to link themselves to Open Inventor parent nodes (modules).

{{<alert class="info" caption="Execution order in Open Inventor scenes">}}
The model below depicts the order in which the modules are traversed. The red arrow indicates the traversal order: from top to bottom and from left to right. The modules are numbered accordingly from 1 to 8. Knowing about the traversal order can be crucial to achieve a certain ouput.
![Traversing in Open Inventor](images/tutorials/openinventor/OI1_13.png "Traversing through a network of Open Inventor modules")
{{</alert>}}

## SoGroup and SoSeparator
The `SoGroup` and `SoSeparator` modules can be used as containers for child nodes. They both allow multiple inputs and combine the results in one single output as seen above. Nevertheless, there is a big difference in handling the traversal state of the scene graph.

![SoGroup vs. SoSeparator](images/tutorials/openinventor/SoGroup_SoSeparator.png "SoGroup vs. SoSeparator")

In the network above, we render four `SoCone` objects. The left side uses the `SoSeparator` modules, the right side uses the `SoGroup` ones. There is a `SoMaterial` module defining one of the left cone objects to be yellow. As you can see, the `SoMaterial` module is only applied to that cone, the other left cone remains in its default gray color, because the `SoSeparator` module isolates the separator's children from the rest of the scene graph.

On the right side, we are using `SoGroup` ({{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoGroup.html" "SoGroup module reference" >}}). The material of the cone is set to be of red color. As the `SoGroup` module does not alter the traversal state in any way, the second cone in this group is also colored in red.

{{<alert class="check" caption="Check">}}
Be aware of some Open Inventor modules altering the traversal order. If your scene turns out to differ from your expected result, check whether incorporated `SoSeparator` modules are the cause. 
Details on these can be found in the {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoSeparator.html" "SoSeparator module reference" >}}
{{</alert>}}
 
{{< networkfile "examples/open_inventor/SoGroupSoSeparator.mlab" >}}

More information about Open Inventor and Scene Graphs can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch07.html" "here" >}} , in the {{< docuLinks "/Standard/Documentation/Publish/Overviews/OpenInventorOverview.html" "Open Inventor Overview" >}} or the [Open Inventor Reference](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html).

