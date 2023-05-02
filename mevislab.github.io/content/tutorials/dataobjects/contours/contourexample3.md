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
## Introduction

In this example, we like to use the created CSOs to display an overlay.
This allows us to mark one of two lungs. In addition to
that, we will display the whole segmented lobe of the lung in a 3D
image.

## Steps to do
### Develop your network
Use the network from the [contour example 2](/tutorials/dataobjects/contours/contourexample2) and add the modules `VoxelizeCSO`,
`SoView2DOverlay` and `View2D` to your workspace. Connect the module as
shown. The module `VoxelizeCSO` allows to convert CSOs into voxel images.

![Data Objects Contours Example 3](/images/tutorials/dataobjects/contours/DO3_02.png "Data Objects Contours Example 3")

### Convert CSOs into voxel images
Update the module `VoxelizeCSOs` to create overlays based on your CSOs.
The result can be seen in `View2D1`.

![Overlay](/images/tutorials/dataobjects/contours/DO3_03.png "Overlay")

Next, we like to inspect the marked lobe of the lunge. This means, we
like to inspect the object, build out of CSOs. In order to do that, add
the `View3D` module. The 3D version of your lung can be seen in the
viewer.

![Additional 3D Viewer](/images/tutorials/dataobjects/contours/DO3_04.png "Additional 3D Viewer")
![Extracted Object](/images/tutorials/dataobjects/contours/DO3_05.png "Extracted Object")

## Summary
* The module `VoxelizeCSO` converts CSOs to voxel images
* Create an overlay out of voxel images using `SoView2DOverlay`

{{< networkfile "examples/data_objects/contours/example3/ContourExample3.mlab" >}}

 [//]: <> (MVL-682)
