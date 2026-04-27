---
layout: post
title: "Contours and Ghosting"
category: "data_objects"
---

# Contour Example 5: Contours and Ghosting
This image shows how to automatically create CSOs based on isovalues. In addition, the visualization of CSOs on previous and subsequent slices is shown.

## Summary
In this example, the `CSOIsoGenerator` is used to generate contours based on a given isovalue out of the image. Contours are generated in the image where the given isovalue is close to the one configured. These contours are stored in the `CSOManager` and ghosting is activated in the `SoCSOVisualizationSettings`.

"Ghosting" means not only showing contours available on the currently visible slice but also contours on the neighboring slices with increasing transparency.

The contours are also displayed in a three-dimensionsal `SoExaminerViewer` by using the `SoCSO3DRenderer`.

![CSOs on slices below and above the current slice are shown with ghosting](examples/data_objects/contours/example5/image.png "CSOs on slices below and above the current slice are shown with ghosting")

# Download
You can download the example network [here](examples/data_objects/contours/example5/ContourExample5.mlab)
