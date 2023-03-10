---
title: "Example 3: Region Growing"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Image Processing", "Segmentation", "Region Growing"]
menu: 
  main:
    identifier: "imageprocessing3"
    title: "In this example, you segment parts of an image by using a simple region growing."
    weight: 615
    parent: "imageprocessing"
---

# Example 3: Region Growing

{{< youtube "nQV2o_3BcJI" >}}

## Introduction
A very simple approach to segment parts of an image is the region growing method. A general explanation can be found [here]("https://en.wikipedia.org/wiki/Region_growing").

In this example, you will segment the brain of an image and show the segmentation results as an overlay on the original image.

## Steps to do
### Develop your network
Add a `LocalImage` module to your workspace and select load *$(DemoDataPath)/BrainMultiModal/ProbandT1.dcm*. Add a `View2D` module and connect both as seen below.

![Example Network](/images/tutorials/image_processing/network_example3.png "Example Network")

### Add the RegionGrowing module
Add the `RegionGrowing` module and connect the input with the `LocalImage` module. You will see a message *results invalid*. The reason is, that a region growing always needs a starting point for getting similar pixels. The output of the module does not show a result in *Output Inspector*.

![Results Invalid](/images/tutorials/image_processing/network_example3a.png "Results Invalid")

Add a `SoView2DMarkerEditor` to your network and connect it with your `RegionGrowing` and with the `View2D`. Clicking into your viewer now creates markers which can be used for the region growing. 

![SoView2DMarkerEditor](/images/tutorials/image_processing/SoView2DMarkerEditor.png "SoView2DMarkerEditor")

The region growing starts on manually clicking *Update* or automatically if *Update Mode* is set to *Auto-Update*. We recommend to set update mode to automatic update. Additionally you should set the *Neighborhood Relation* to *3D-6-Neighborhood (x,y,z)*, because then your segmentation will also affect the z-axis.

Set *Threshold Computation* to *Automatic* and define *Interval Size* as 1.600 % for relative, automatic threshold generation.

{{<alert class="info" caption="Extra Infos">}}
For more information, see {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/RegionGrowing.html" "MeVisLab Module Reference" >}}
{{</alert>}}

![Auto-Update for RegionGrowing](/images/tutorials/image_processing/RegionGrowing_AutoUpdate.png "Auto-Update for RegionGrowing")

Clicking into your image in the `View2D` now already generates a mask containing your segmentation. As you did not connect the output of the `RegionGrowing`, you need to select the output of the module and use the *Output Inspector* to visualize your results.

![Output Inspector Preview](/images/tutorials/image_processing/OutputInspector.png "Output Inspector Preview")

In order to visualize your segmentation mask as an overlay in the `View2D`, you need to add the `SoView2DOverlay` module. Connect it as seen below.

![SoView2DOverlay](/images/tutorials/image_processing/network_example3b.png "SoView2DOverlay")

Your segmentation is now shown in the `View2D`. You can change the color and transparency of the overlay via SoView2DOverlay.

### Close gaps
Scrolling through the slices, you will see that your segmentation is not closed. There are lots of gaps where the grey value of your image differs more than your threshold. You can simply add a `CloseGap` module to resolve this issue. Configure *Filter Mode* as *Binary Dilatation*, *Border Handling* as *Pad Src Fill* and set *KernelZ* to 3.

The difference before and after closing the gaps can be seen in the Output Inspector.

{{< imagegallery 2 "/images/tutorials/image_processing" "Output_Before" "Output_After">}}

You can play around with the different settings of the `RegionGrowing` and `CloseGap` modules to get a better result.

### Visualize 2D and 3D
You can now also add a `View3D` to show your segmentation in 3D. Your final result should look similar to this.

![Final Result](/images/tutorials/image_processing/network_example3c.png "Final Result")

## Summary
* The module `RegionGrowing` allows a very simple segmentation of similar grey values.
* Gaps in a segmentation mask can be closed by using the `CloseGap` module.
* Segmentation results can be visualized in 2D and 3D.

{{< networkfile "/examples/image_processing/example3/RegionGrowingExample.mlab" >}}