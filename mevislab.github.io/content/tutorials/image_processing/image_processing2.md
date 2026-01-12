---
title: "Example 2: Masking images"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 610
tags: ["Beginner", "Tutorial", "Image Processing", "Mask"]
menu: 
  main:
    identifier: "imageprocessing2"
    title: "In this example, you will apply a mask on an image, so that contrast changes are not applied on black background pixels"
    weight: 610
    parent: "imageprocessing"
---

# Example 2: Masking Images

{{< youtube "k003ytr8ZQA" >}}

## Introduction
The background of medical images is black for most cases. In the case an image is inverted or window/level values are adapted, these black voxels outside clinical relevant voxels might become very bright or even white.

Being in a dark room using a large screen, the user might be blended by these large white regions.

Image masking is a very good way to select a defined region where image processing shall be applied. A mask allows to define a region (the masked region) to allow image modifications whereas voxels outside the mask remain unchanged.

## Steps to Do
### Develop Your Network
Add a `LocalImage` and a `SynchroView2D` module to your network and connect the modules as seen below.

![Example Network](/images/tutorials/image_processing/network_example2a.png "Example Network")

Open the Automatic Panel of the `SynchroView2D` module via context menu {{< mousebutton "right" >}} and selecting {{< menuitem "Show Window" "Automatic Panel" >}}. Set the field *synchLUTs* to *TRUE*.

![Synchronize LUTs in SynchroView2D](/images/tutorials/image_processing/synchLUTs.png "Synchronize LUTs in SynchroView2D")

Double-click the `SynchroView2D` and change window/level values via right mouse button {{< mousebutton "right" >}}. You can see that the background of your images gets very bright and changes based on the LUT are applied to all voxels of your input image - even on the background. Hovering your mouse over the image(s) shows the current gray value under your cursor in [Hounsfield Unit (HU)](https://en.wikipedia.org/wiki/Hounsfield_scale).

![Without masking the image](/images/tutorials/image_processing/SynchroView2D_before.png "Without masking the image")

Hovering the mouse over black background voxels shows a value between 0 and about 60. This means we want to create a mask that only allows modifications on voxels having a gray value larger than 60.

Add a `Mask` and a `Threshold` module to your workspace and connect them as seen below.

![Example Network](/images/tutorials/image_processing/network_example2b.png "Example Network")

Changing the window/level values in your viewer still also changes background voxels. The `Threshold` module still leaves the voxels as is because the threshold value is configured as larger than 0. Open the panels of the modules `Threshold` and `Mask` via double-click {{< mousebutton "left" >}} and set the values as seen below.

{{< imagegallery 2 "/images/tutorials/image_processing" "Threshold" "Mask">}}

Now all voxels having a HU value lower or equal 60 are set to 0, all others are set to 1. The resulting image from the `Threshold` module is a binary image that can now be used as a mask by the `Mask` module.

![Output of the Threshold module](/images/tutorials/image_processing/OutputInspector_Threshold.png "Output of the Threshold module")

The `Mask` module is configured to use the *Masked Original* image. Changing the window/level values in your images now, you can see that the background voxels are not affected anymore (at least as long as you do not reach a very large value).

![After masking the image](/images/tutorials/image_processing/SynchroView2D_after.png "After masking the image")

## Summary
* The module `Threshold` applies a relative or an absolute threshold to a voxel image. It can be defined what should be written to those voxels that pass or fail the adjustable comparison.
* The module `Mask` masks the image of input one with the mask at input two.
* A mask can be used to filter voxels inside images.

{{< networkfile "examples/image_processing/example2/ImageMask.mlab" >}}
