---
layout: post
title: "Masking images"
category: "image_processing"
---

# Image Processing Example 2: Masking Images
In this example, we create a simple mask on an image, so that background voxels are not affected by changes of the window/level values.

## Summary
We are loading images by using the `LocalImage` module and show them in a `SynchroView2D`. The same image is shown in the right viewer of the `SynchroView2D` but with a `Threshold` based `Mask`.

![Screenshot](/examples/image_processing/example2/image.png)

# Download
You can download the example network [here](/examples/image_processing/example2/ImageMask.mlab)
