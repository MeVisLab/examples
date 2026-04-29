---
title: "Example 2: Masking Images"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 610
tags: ["Beginner", "Tutorial", "Image Processing", "Mask"]
menu: 
  main:
    identifier: "imageprocessing2"
    title: "Masking Images"
    weight: 610
    parent: "imageprocessing"
---

# Example 2: Masking Images

{{< youtube "k003ytr8ZQA" >}}

## Introduction
The background of medical images typically contains small values. When an image is inverted, these small-valued voxels outside clinically relevant regions can become very large-valued. As a result, they appear bright or even white on the screen.

In a dark environment, especially when using a large display, these bright background regions can be uncomfortable to look at.

This effect occurs because the entire image is processed, including regions that are not relevant for analysis. A common way to avoid this is to restrict processing to the relevant regions using image masking. Image masking allows selecting a defined region (the masked region) in which image modifications are applied, while voxels outside the mask remain unchanged.

Beyond avoiding visual artifacts, image masking is generally useful for focusing processing on regions of interest. It helps reduce the influence of irrelevant data, improves the robustness of many algorithms, and can also reduce computation time by limiting operations to a smaller part of the image.

## Steps to Do

### Develop Your Network
Add a `LocalImage` and a `SynchroView2D` module to your network and connect the modules as seen below.

![Example network](images/tutorials/image_processing/network_example2a.png "Example network")

Open the Automatic Panel of the `SynchroView2D` module via the context menu {{< mousebutton "right" >}} by selecting {{< menuitem "Show Window" "Automatic Panel" >}}. Set the field <field>synchLUTs</field> to *Yes*.

![Synchronize LUTs in SynchroView2D](images/tutorials/image_processing/synchLUTs.png "Synchronize LUTs in SynchroView2D")

Double-click {{< mousebutton "left" >}} the `SynchroView2D` and change window/level values via right mouse button {{< mousebutton "right" >}}. You can see that the background of your images gets very bright and changes based on the LUT are applied to all voxels of your input image &mdash; even to the background. Hovering your mouse over the image(s) shows the current value under your cursor.

![Without masking the image](images/tutorials/image_processing/SynchroView2D_before.png "Without masking the image")

Hovering the mouse over black background voxels shows a value between *0* and about *60*. This means we want to create a mask that only allows modifications on voxels having a value larger than *60*.

Add a `Mask` and a `Threshold` module to your workspace and connect them as seen below.

![Example network: using Mask](images/tutorials/image_processing/network_example2b.png "Example network: using Mask")

Changing the window/level values in your viewer still also changes the appearance of background voxels. The `Threshold` module still leaves the voxels as is because the threshold value is configured as larger than *0*. Open the panels of the modules `Threshold` and `Mask` via double-click {{< mousebutton "left" >}} and set the values as seen below.

{{< imagegallery 2 
    "images/tutorials/image_processing"
    "Threshold|Threshold panel"
    "Mask|Mask panel"
>}}

Now, all voxels having a value less than or equal to *60* are set to *0*, all others are set to *1*. The resulting image from the `Threshold` module is a binary image that can now be used as a mask by the `Mask` module.

![Output of the Threshold module](images/tutorials/image_processing/OutputInspector_Threshold.png "Output of the Threshold module")

The `Mask` module is configured to use the *Masked Original* image. Changing the window/level values in your images now, you can see that the background voxels are not affected anymore (at least as long as you do not reach a very large value).

![After masking the image](images/tutorials/image_processing/SynchroView2D_after.png "After masking the image")

## Summary
* The module `Threshold` applies a relative or an absolute threshold to a voxel image. It can be defined what should be written to those voxels that pass or fail the adjustable comparison.
* The module `Mask` masks the image of input one with the mask at input two.
* A mask can be used to filter voxels inside images.

{{< networkfile "examples/image_processing/example2/ImageMask.mlab" >}}
