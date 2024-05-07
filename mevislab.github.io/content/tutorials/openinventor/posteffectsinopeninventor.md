---
title: "Example 4: Post Effects in Open Inventor"
date: 2024-05-03T10:52:33+02:00
draft: false
weight: 540
status: "OK"
tags: ["Intermediate", "Tutorial", "Open Inventor", "Post Effects"]
menu: 
  main:
    identifier: "posteffectsinopeninventor"
    title: "Learn how to use Post Effects in Open Inventor"
    weight: 540
    parent: "openinventor"
---
# Example 4: Post Effects in Open Inventor
## Introduction

Up to this point, we practiced constructing Open Inventor scenes and placed three-dimensional Open Inventor objects of different colors and shapes within them.
In this tutorial, we will go over the steps to add shadows to our 3D-objects, make them glow and vary their opacity to make them transparent. We will also incorporate WEMs from multi-frame DICOMs and render them as scene objects to see how different post effects can be used on them.

## Steps to follow

### From DICOM to scene object

To incorporate DICOMs into your Open Inventor Scene, they have to be rendered as Open Inventor objects, which can be done through converting them into [WEMs](/glossary/#winged-edge-meshes) first. Begin by adding the modules `LocalImage`, `WEMIsoSurface` and `SoWEMRenderer` to your workspace. Open the panel of the `LocalImage` module, browse your files and choose a DICOM with multiple frames as input data. Connect the `LocalImage` module's output connector to `WEMIsoSurface` module's input connector to create a WEM of the study's surface. Then connect the `WEMIsoSurface` module's output connector to the `SoWEMRenderer` module's input connector to render a scene object, that can be displayed by adding a `SoExaminerViewer` module to the workspace and connecting the `SoWEMRenderer` module's output connector to its input connector. 

{{<alert class="check" caption="Check">}}
We don't recommend using single frame DICOMs for this example as a certain depth is required to interact with the scene objects as intended. Also make sure that the PixelData of the DICOM file you choose contains all slices of the study as it might be difficult to arrange scene objects of individual slices to resemble the originally captured study. 
{{</alert>}}

![From DICOM to SO](/images/tutorials/openinventor/multiframetoso.PNG "How to create a scene object out of a multiframe DICOM")






## Summary