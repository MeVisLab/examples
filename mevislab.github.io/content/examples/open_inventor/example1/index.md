---
layout: post
title: "Open Inventor objects"
category: "open_inventor"
---

# Open Inventor Example 1: Open Inventor objects
In this example a simple Open Inventor scene is created. The Open Inventor scene shows three objects of different color and shape.

## Summary
A `SoExaminerViewer` is used to render open inventor scenes in 3D. The `SoBackground` module defines the background of the whole scene.

Three 3D objects are created (`SoCone`, `SoSphere` and `SoCube`) having a defined `SoMaterial` module for setting the *DiffuseColor* of the object. The cube and the cone are also transformed by a `SoTransform` module so that they are located next to the centered sphere.

In the end, all three objects including their materials and transformations are added to the `SoExaminerViewer` by a `SoGroup`.

![Screenshot](/examples/open_inventor/example1/image.png)

# Download
You can download the example network [here](/examples/open_inventor/example1/OpenInventorExample1.mlab)
