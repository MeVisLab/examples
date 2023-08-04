---
layout: post
title: "2D and 3D visualization of contours"
category: "data_objects"
---

# Contour Example 3: 2D and 3D visualization of contours
This example shows how to display CSOs in 2D as an overlay and additionally how the CSOs are displayed in 3D.

## Summary
Images are loaded by using a `LocalImage` module and displayed in a 2D viewer. A `SoCSOLiveWireEditor` is added to draw contours on the images. The `CSOSliceInterpolator` generates additional contours between the manual CSOs by using linear interpolation.

The module `VoxelizeCSO` is used to create a three-dimensional voxel mask of the contours which can be used as an overlay on the images in a `View2D` panel. The `SoView2DOverlay` module defines the color and opacity of the overlay.

Lastly the panel of the `View3D` module is used to visualize the voxel mask in 3D.

![Screenshot](/examples/data_objects/contours/example3/image.png)

# Download
You can download the example network [here](/examples/data_objects/contours/example3/ContourExample3.mlab)
