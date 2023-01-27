---
title: "Example 1: Synchronous view of two images"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Visualization", "2D"]
menu: 
  main:
    identifier: "visualization_example1"
    title: "Use the SynchroView2D Module for visualizing the same slice(s) of two images"
    weight: 555
    parent: "visualization"
---
# Example 1: Synchronous view of two images {#VisualizationExample1}
## Introduction
In this example we like to use the module `SynchroView2D` to be able to inspect two different images simultaneously.

The module `SynchroView2D` provides two 2D viewers that are synchronized.

As in Tutorial [Chapter 1 - Basic Mechanics of MeVisLab](/tutorials/basicmechanisms/#TutorialParameterConnection), the processed and the unprocessed image can be displayed simultaneously. Scrolling through one image automatically changes the slices of both viewers, so slices with the same slice number are shown in both images.

The difference is that we are now using an already existing Module named `SynchroView2D`.

{{<alert class="info" caption="Extra Infos">}}

The `SynchroView2D` module is explained {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SynchroView2D.html" "here" >}}

{{</alert>}}

## Steps to do
### Develop your network
Start the example by adding the module `LocalImage` to your workspace to load the example image *Tumor1_Head_t1.small.tif*. Next, add and connect the following modules as shown.

![SynchroView2D](/images/tutorials/visualization/V1_01.png "SynchroView2D Viewer")

## Summary
* Multiple images can be synchronized by the `SynchroView2D` module

{{< networkfile "examples/visualization/example1/VisualizationExample1.mlab" >}}
