---
layout: post
title: "Contours and ghosting"
category: "data_objects"
---

# Contour Example 5: Contours and ghosting
This image shows how to automatically create CSOs based on ISO values. In addition the visualization of CSOs of previous and subsequent slices is shown.

## Summary
In this example, the `CSOIsoGenerator` is used to generate contours based on a given ISO value of the image. Contours are generated in the image where the given ISO value is close to the one configured. These contours are stored in the `CSOManager` and ghosting is activated in the `SoCSOVisualizationSettings`.

Ghosting means not only showing contours available on the currently visible slice but also contours of the neighbouring slices with increasing transparency.

The contours are also displayed in a three-dimensionsl `SoExaminerViewer` by using the `SoCSO3DRenderer`.

![Screenshot](/examples/data_objects/contours/example5/image.png)

# Download
You can download the example network [here](/examples/data_objects/contours/example5/ContourExample5.mlab)
