---
title: "Contour Example 3: 2D and 3D Visualization of Contours"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 675
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO", "3D"]
menu: 
  main:
    identifier: "contourexample3"
    title: "Overlay Creation and 3D Visualization of Contours"
    weight: 675
    parent: "contours"
---

# Contour Example 3: Overlay Creation and 3D Visualization of Contours {#TutorialContoursExample3}

{{< youtube "6NmKQagTDKg">}}

## Introduction
In this example, we'd like to use the created CSOs to display an overlay.
This allows us to mark one of two lungs. In addition to
that, we will display the whole segmented lobe of the lung in a 3D
viewer.

## Steps to Do
### Develop Your Network
Use the network from the [contour example 2](tutorials/dataobjects/contours/contourexample2) and add the modules `VoxelizeCSO`,
`SoView2DOverlay` and `View2D` to your workspace. Connect the module as
shown. The module `VoxelizeCSO` allows to convert CSOs into a voxel image.

![Network for segmenting and viewing contours in 2D](images/tutorials/dataobjects/contours/DO3_02.png "Network for segmenting and viewing contours in 2D")

### Convert CSOs into a Voxel Image
Update the module `VoxelizeCSOs` to create voxel masks based on your CSOs.
The result can be seen in `View2D1`.

![Showing an overlay of the voxel mask in 2D](images/tutorials/dataobjects/contours/DO3_03.png "Showing an overlay of the voxel mask in 2D")

Next, we like to inspect the marked lobe of the lung. This means we
like to inspect the object that is built out of CSOs. In order to do that, add
the `View3D` module. The 3D version of the lung can be seen in the
viewer.

![Additional 3D viewer](images/tutorials/dataobjects/contours/DO3_04.png "Additional 3D viewer")
![Extracted object](images/tutorials/dataobjects/contours/DO3_05.png "Extracted object")

## Summary
* The module `VoxelizeCSO` converts CSOs to a voxel image.
* Create an overlay out of a voxel image using `SoView2DOverlay`.

{{< networkfile "examples/data_objects/contours/example3/ContourExample3.mlab" >}}

 [//]: <> (MVL-682)
