---
layout: post
title: "2D and 3D Visualization of Contours"
category: "data_objects"
---

# Contour Example 3: 2D and 3D Visualization of Contours
This example shows how to display CSOs in 2D as an overlay and additionally how the CSOs are displayed in 3D.

## Summary
Images are loaded by using a `LocalImage` module and displayed in a 2D viewer. A `SoCSOLiveWireEditor` is added to draw contours on the images. The `CSOSliceInterpolator` generates additional contours between the manually created CSOs by using linear interpolation.

The module `VoxelizeCSO` is used to create a three-dimensional voxel mask of the contours that can be used as an overlay on the images in a `View2D` panel. The `SoView2DOverlay` module defines the color and opacity of the overlay.

Lastly, the panel of the `View3D` module is used to visualize the voxel mask in 3D.

![Manually created CSOs are automatically interpolated and shown in 2D and in 3D](examples/data_objects/contours/example3/image.png "Manually created CSOs are automatically interpolated and shown in 2D and in 3D")

# Download
You can download the example network [here](examples/data_objects/contours/example3/ContourExample3.mlab)
