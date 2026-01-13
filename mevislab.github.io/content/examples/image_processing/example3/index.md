---
layout: post
title: "Region Growing (Segmentation)"
category: "image_processing"
---

# Image Processing Example 3: Region Growing (Segmentation)
In this example, we create a simple mask on an image by using the `RegionGrowing` module.

## Summary
We are loading images by using the `LocalImage` module and show them in a `SynchroView2D`. The same image is used as input for the `RegionGrowing` module. The starting point for the algorithm is a list of markers created by the `SoView2DMarkerEditor`. As the `RegionGrowing` may leave gaps, an additional `CloseGap` module is added. The resulting segmentation mask is shown as an overlay on the original image via `SoView2DOverlay`. 

![Screenshot](examples/image_processing/example3/image.png)

# Download
You can download the example network [here](examples/image_processing/example3/RegionGrowingExample.mlab)
