---
layout: post
title: "2D and 3D visualization of contours"
category: "data_objects"
---

# Contour Example 3: 2D and 3D visualization of contours
This example shows how to display CSOs in 2D as an overlay. In addition, the CSOs are displayed in 3D.

## Summary
Images are loaded by using a `LocalImage` module and visualized in a 2D viewer. A `SoCSOLiveWireEditor` is added to draw contours on the images. The `CSOSliceInterpolator` generates additional contours between the manual CSOs by using a linear interpolation.

The module `VoxelizeCSO` is used to create a 3-dimensional voxel mask of the contours which can be used as overlay on the images in a `View2D`. The `SoView2DOverlay` module defines the color and transparency of the overlay.

In the end, a `View3D` is used to visualize the voxel mask in 3D.

![Screenshot](/examples/data_objects/contours/example3/image.png)

# Download
You can download the example network [here](/examples/data_objects/contours/example3/ContourExample3.mlab)
