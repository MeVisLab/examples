---
title: "Contour Example 5: Contours and Ghosting"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO"]
menu: 
  main:
    identifier: "contourexample5"
    title: "Visualizing Contours on currently visible and neighboring slices (ghosting)"
    weight: 635
    parent: "contours"
---
# Contour Example 5: Visualizing Contours and Images {#TutorialContoursExample5}
## Introduction

In this example, we like to automatically create CSOs based on a predefined iso value. 

## Steps to do
### Develop your network
Add the following modules to your workspace and connect them as shown.
Load the example image *Bone.tiff*.

### Automatic creation of CSOs based on the iso value
Now, open the panel of `CSOIsoGenerator` to set the *Iso Value* to 1200. If you press *Update* in
the panel, you can see the creation of CSOs on every slide, when opening
the module `View2D`. In addition to that the number of CSOs ins displayd in the `CSOManager`. The module
`CSOIsoGenerator` generates iso-controus for each slice at a fixed iso
value. This means, closed CSOs are formed based on the detection of the
voxel value of 1200 on every slice.

![Data Objects Contours Example 5](/images/tutorials/dataobjects/contours/DO5_02.png "Data Objects Contours Example 5")

### Ghosting
Now, we like to make CSOs of previous and subsequent slices visible (Ghosting). In
order to do that, open the panel of `SoCSOVisualizationSettings` and
open the tab *Misc*. Increase the parameter `Ghosting depth in voxel`,
which shows you the number of slices above an below the current slice,
which CSOs are also seen in the viewer. The result can be seen in the
viewer.

![Ghosting](/images/tutorials/dataobjects/contours/DO5_04.png "Ghosting")

### Display created CSOs
At last, we like to make all CSOs visible in a 3D viewer. To do that,
add the modules `SoCSO3DRenderer` and `SoExaminerViewer` to your network
and connect them as shown. In the viewer `SoExaminerViewer` you can see
all CSOs together. In this case all scanned bones can be seen.

![CSOs in 3D View](/images/tutorials/dataobjects/contours/DO5_05.png "CSOs in 3D View")

## Summary
* `CSOIsoGenerator` enables automatic COS generation based on an iso value
* Ghosting allows to display CSOs of previous and following slices

{{< networkfile "examples/data_objects/contours/example5" >}}

 [//]: <> (MVL-682)