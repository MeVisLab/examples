---
title: "Example 1: Arithmetic operations on two images"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Image Processing", "Arithmetic"]
menu: 
  main:
    identifier: "imageprocessing1"
    title: "In this example, you will apply scalar functions on two images like Add, Multiply, Subtract, etc."
    weight: 605
    parent: "imageprocessing"
---

# Example 1: Arithmetic operations on two images

{{< youtube "ToTQ3XRPmlk" >}}

## Introduction
We are using the `Arithmetic2` module to apply basic scalar functions on two images. The module provides 2 inputs for images and 1 output image for the result.

## Steps to do
### Develop your network
Add two `LocalImage` modules to your workspace for the input images. Select *$(DemoDataPath)/BrainMultiModal/ProbandT1.dcm* and *$(DemoDataPath)/BrainMultiModal/ProbandT2.dcm* from MeVisLab demo data and add a `SynchroView2D` to your network.

In the end, add the `Arithmetic2` module and connect them as seen below.

![Example Network](/images/tutorials/image_processing/network_example1.png "Example Network")

Your `SynchroView2D` shows two images. On the left hand side, you can see the original image from your left `LocalImage` module. The right image shows the result of the arithmetic operation executed by the `Arithmetic2` module on the two input images.

![SynchroView2D](/images/tutorials/image_processing/arithmetic_viewer.png "SynchroView2D")

The `SynchroView2D` module automatically synchronizes the visible slice of both input images, you can see the same slice with and without applied filter.

## Arithmetic operations
Double-click {{< mousebutton "left" >}} the `Arithmetic2` module to select different functions to be applied.

![Arithmetic2](/images/tutorials/image_processing/arithmetic2.png "Arithmetic2")

The selected function is applied automatically.

## Summary
* Arithmetic operations on two images can be applied on images by using `Arithmetic*` modules.
* The `SynchroView2D` module allows to scroll through slices synchronized on two images.

{{< networkfile "examples/image_processing/example1/BasicFilter.mlab" >}}
