---
layout: post
title: "Creation of Contours"
category: "data_objects"
---

# Contour Example 1: Creation of contours
Contours are stored as CSOs or Contour Segmented Objects in MeVisLab.
This example highlights ways of creating CSOs using modules of the `SoCSOEditor` group.

{{<alert class="info" caption="Info">}}
You may want to look at the glossary entry on [*CSOs*](/glossary/#contour-segmented-objects).
{{</alert>}}

The `SoCSOEditor` module group contains several modules, some of which are listed right below:

* `SoCSOPointEditor`
* `SoCSOAngleEditor`
* `SoCSOArrowEditor`
* `SoCSODistanceLineEditor`
* `SoCSODistancePolylineEditor`
* `SoCSOEllipseEditor`
* `SoCSORectangleEditor`
* `SoCSOSplineEditor`
* `SoCSOPolygonEditor`
* `SoCSOIsoEditor`
* `SoCSOLiveWireEditor`

{{<alert class="info" caption="Info">}}
Whenever Contour Segmented Objects are created, they are temporarily stored by and can be managed with the `CSOManager`. 
{{</alert>}}

In this example, contours are created and colors and styles of these CSOs are customized by using the `SoCSOVisualizationSettings` module.

![Screenshot](/examples/data_objects/contours/example1/image.png)

## Summary
+ Contours are stored as their own abstract data type called Contour Segmented Objects (Often abbreviated to *CSO*).
+ The `SoEditor` module group contains several useful modules to create, interact with or modify CSOs.
+ Created CSOs are temporarily stored and can be managed using the `CSOManager`.

# Download
The example network can be downloaded [here](/examples/data_objects/contours/example1/ContourExample1.mlab)
