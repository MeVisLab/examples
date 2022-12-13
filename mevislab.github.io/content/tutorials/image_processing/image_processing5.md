---
title: "Example 5: Clip Planes"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Advanced", "Tutorial", "Image Processing", "3D", "Clip Planes"]
menu: 
  main:
    identifier: "imageprocessing5"
    title: "In this example, show some options for integrating clip planes into your 3D views."
    weight: 625
    parent: "imageprocessing"
---

# Example 4: Subtract 3D objects
## Introduction
In this example, we are using the `SoGVRDrawOnPlane` module to define the currently visible slice from a 2D view as a clip plane in 3D.

## Steps to do
### Develop your network
First we need to develop the network to scroll through the slices. Add a `LocalImage` module to your workspace and select the file *ProbandT1* from mevislab demo data.

Add the modules `OrthoReformat3`, `Switch`, `SoView2D`, `View2DExtensions` and `SoRenderArea` and connect them as seen below.

![Example Network](/images/tutorials/image_processing/network_example5.png "Example Network")

In previous tutorials, we already learned that it is possible to show 2D slices in a `SoRenderArea`. For scrolling through the slices, a `View3DExtensions` module is necessary. In this network, we also have a `OrthoReformat3` module. Its allows us to transform the input image (by rotating and/or flipping) into the three main views commonly used:
* Axial
* Coronal
* Sagittal

The `Switch` takes multiple input images and you can toggle between them to show one of the orthogonal transformations to be used as output.

The `SoRenderArea` now shows the 2D images in a view defined by the `Switch`.

{{< imagegallery 3 "/images/tutorials/image_processing" "View0" "View1" "View2" >}}

### Current 2D slice in 3D
We now want to visualize the slice visible in the 2D images as a 3D plane. Add a `SoGVRDrawOnPlane` and a `SoExaminerViewer` to your workspace and connect them. We should also add a `SoBackground` and a `SoLUTEditor`. The viewer remains empty because no source image is selected to display. Add a `SoGVRVolumeRenderer` and connect it to your viewer and the `LocalImage`.

![Example Network](/images/tutorials/image_processing/network_example5b.png "Example Network")

A 3-dimensional plane of the image is shown. Adapt the LUT as seen below.

![SoLUTEditor](/images/tutorials/image_processing/tutorial5_lut.png "SoLUTEditor")

We now have a single slice of the image in 3D, but the slice is static and cannot be changed. In order to use the currently visible slice from the 2D viewer, we need to create a parameter connection from the `SoView2D` Position *Slice as plane* to the `SoGVRDrawOnPlane` Plane vector.

![SoView2D Position](/images/tutorials/image_processing/SoView2D_Position.png "SoView2D Position")

![SoGVRDrawOnPlane Plane](/images/tutorials/image_processing/SoGVRDrawOnPlane_Plane.png "SoGVRDrawOnPlane Plane")

Now the plane representation of the visible slice is synchronized to the plane of the 3D view. Scrolling through your 2D slices changes the plane in 3D.

![Visible slice in 3D](/images/tutorials/image_processing/2DSlice_3D.png "Visible slice in 3D")

### Current 2D slice as clip plane in 3D
This slice shall now be used as a clip plane in 3D. In order to achieve this, you need another `SoExaminerViewer` and a `SoClipPlane`. Add them to your workspace and connect them as seen below. You can also use the same `SoLutEditor` and `SoBackground` for the 3D view. Also use the same `SoGVRVolumeRenderer`, the 3D volume does not change.

![Example Network](/images/tutorials/image_processing/network_example5c.png "Example Network")

Now your 3D scene shows a 3-dimenaional volume cut by a plane in the middle. Once again, the clipping is not the same slice as your 2D view shows.

![Clip plane in 3D](/images/tutorials/image_processing/3D_ClipPlane.png "Clip plane in 3D")

Again create a parameter connection from the `SoView2D` Position *Slice as plane*, but this time to the `SoClipPlane`. 

![SoClipPlane Plane](/images/tutorials/image_processing/SoClipPlane_Plane.png "SoClipPlane Plane")

If you now open all 3 viewers and scroll through the slices in 2D, the 3D viewers are both synchronized with the current slice. You can even toggle the view in the `Switch` and the plane is adapted automatically.

![Final 3 views](/images/tutorials/image_processing/Final3Views.png "Final 3 views")

## Summary
* The module `OthoReformat3` transforms input images to the three viewing directions: coronal, axial and sagittal
* A `Switch` can be used to toggle through multiple input images
* The `SoGVRDrawOnPlane` module renders a single slice as a 3-dimensional plane
* 3-dimensional clip planes on volumes can be created by using a `SoClipPlane` module

{{< networkfile "/examples/image_processing/example5/ImageProcessingExample5.mlab" >}}