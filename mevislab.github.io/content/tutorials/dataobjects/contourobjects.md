---
title: "Contour Objects (CSO)"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 660
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO"]
menu: 
  main:
    identifier: "contours"
    title: "Contour Segmented Objects (CSOs) in MeVisLab"
    weight: 660
    parent: "dataobjects"
---
# Contour Segmentation Objects (CSOs) in MeVisLab {#CSO}
## Introduction
### Structure of CSOs

MeVisLab provides modules to create contours in images. 3D objects that encapsulate these contours are called Contour Segmentation Objects (CSOs).

In the next image, you can see a rectangular shaped CSO. The pink circles you can see are called *Seed Points*.

*Seed Points* define the shape of the CSO. In the case of a rectangle, you need four *Seed Points* forming the corners to define the whole rectangle.

The points forming the blue lines are called *Path Points*.

The *Path Points* form the connection between the *Seed Points* whereby contour objects (CSOs) are generated. CSOs are often closed, but do not need to be.

In general, the *Seed Points* are created interactively using an editor module and the *Path Points* are generated automatically by interpolation or other algorithms.

![Contour Segmented Object (CSO)](/images/tutorials/dataobjects/contours/CSO_Expl_01.png "Contour Segmented Object (CSO)")

#### CSO Editors {#CSOEditors}

As mentioned, when creating CSOs, you can do this interactively by using an editor.

The following images show editors available in MeVisLab for drawing CSOs:

{{< imagegallery 6 "/images/tutorials/dataobjects/contours" "SoCSOPointEditor" "SoCSOAngleEditor" "SoCSOArrowEditor" "SoCSODistanceLineEditor" "SoCSODistancePolylineEditor" "SoCSOEllipseEditor" "SoCSORectangleEditor" "SoCSOSplineEditor" "SoCSOPolygonEditor" "SoCSOIsoEditor" "SoCSOLiveWireEditor">}}

{{<alert class="info" caption="Extra Infos">}}
The `SoCSOIsoEditor` and `SoCSOLiveWireEditor` are special, because they are using an algorithm to detect edges themselves.

* The `SoCSOIsoEditor` generates isocontours interactively.
* The `SoCSOLiveWireEditor` renders and semi-interactively generates CSOs based on the LiveWire algorithm.
{{</alert>}}

### CSO Lists and CSO Groups

All created CSOs are stored in CSO lists that can be saved and loaded on demand. The lists cannot only store the coordinates of the CSOs, but also additional information in the form of name-value pairs (using specialized modules or Python scripting).

![Basic CSO Network](/images/tutorials/dataobjects/contours/BasicCSONetwork.png "Basic CSO Network")

Each `SoCSO*Editor` requires a `SoView2DCSOExtensibleEditor` that manages attached CSO editors and renderers and offers an optional default renderer for all types of CSOs. In addition to that, the list of CSOs needs to be stored in a `CSOManager`.

The appearance of the CSO can be defined by using a `SoCSOVisualizationSettings` module.

CSOs can also be grouped together. The following image shows two different CSO groups. Groups can be used to organize CSOs, in this case to distinguish the CSOs of the right and the left lung. [Here](/tutorials/dataobjects/contours/contourexample2/) you can find more information about CSO Groups.

![CSO Groups](/images/tutorials/dataobjects/contours/DO2_11_2.png "CSO Groups")

{{<alert class="info" caption="Extra Infos">}}
For more information, see {{< docuLinks "/Standard/Documentation/Publish/Overviews/CSOOverview.html" "CSO Overview" >}}
{{</alert>}}

[//]: <> (MVL-653)
