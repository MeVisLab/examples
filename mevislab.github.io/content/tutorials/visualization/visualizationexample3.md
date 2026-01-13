---
title: "Example 3: Image Overlays"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 565
tags: ["Beginner", "Tutorial", "Visualization", "2D", "Overlays", "Masks"]
menu: 
  main:
    identifier: "visualization_example3"
    title: "How to blend images and masks over each other "
    weight: 565
    parent: "visualization"
---
# Example 3: How to Blend Images Over Each Other {#TutorialVisualizationExample3}

{{< youtube "e8iFGp-St0c" >}}

## Introduction
In this example we will show you how to blend a 2D image over another one. With the help of the module `SoView2DOverlay` we will create an overlay, which allows us to highlight all bones in the scan.

## Steps to Do
### Develop Your Network
Start this example by adding the shown modules, connecting the modules to form a network and loading the example image *Bone.tiff*.

Open the panel of the module `Threshold` and configure the module as shown below.

{{<alert class="info" caption="Extra Infos">}}

The `Threshold` module is explained {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/Threshold.html" "here" >}}

{{</alert>}}

[//]: <> (MVL-653)

The module `Threshold` compares the value of each voxel of the image with a customized threshold. In this case: If the value of the chosen voxel is lower than the threshold, the voxel value is replaced by the minimum value of the image. If the value of the chosen voxel is higher than the threshold, the voxel value is replaced by the maximum value of the image. With this, we can construct a binary image that divides the image into bone (white) and no bone (black).

Select output of the `Threshold` module to see the binary image in Output Inspector.

![Image Threshold](images/tutorials/visualization/V3_01.png "Image Threshold")

### Overlays
The module `SoView2DOverlay` blends a 2D image over another one in a 2D viewer. In this case, all voxels with a value above the `Threshold` are colored and therefore highlighted. The colored voxels are then blended over the original image. Using the panel of `SoView2DOverlay`, you can select the color of the overlay.

![SoView2DOverlay](images/tutorials/visualization/V3_02.png "SoView2DOverlay")

{{<alert class="info" caption="Extra Infos">}}

The `SoView2DOverlay` module is explained {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoView2DOverlay.html" "here" >}}

{{</alert>}}

[//]: <> (MVL-653)

## Exercises
1. Play around with different `Threshold` values and `SoView2DOverlay` colors.
2. Visualize your generated threshold mask in 3D by using the `View3D` module.

## Summary
* The module `Threshold` applies a relative or an absolute threshold to a voxel image.
* The module `SoView2DOverlay` blends an 2D image over another one in a 2D viewer.
* You can also use a 3D `SoRenderArea` for the same visualizations. An example can be seen in the next [Example 4](tutorials/visualization/visualizationexample4 "Display images converted to Open Inventor scene objects").

{{<alert class="warning" caption="Warning">}}
The `SoView2DOverlay` module is not intended to work with `OrthoView2D`; in this case, use a `GVROrthoOverlay`.
{{</alert>}}

{{< networkfile "examples/visualization/example3/VisualizationExample3.mlab" >}}
