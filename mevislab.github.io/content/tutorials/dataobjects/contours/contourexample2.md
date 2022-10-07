---
title: "Contour Example 2: Contour Interpolation"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO", "Interpolation"]
menu: 
  main:
    identifier: "contourexample2"
    title: "Creating Contours using Live Wire and linear Interpolation, grouping CSOs for different colors"
    weight: 670
    parent: "contours"
---
# Contour Example 2: Creating Contours using Live Wire and Interpolation {#TutorialContoursExample2}
## Introduction

In this example, we like to create CSOs using the **Live Wire
Algorithm**, which allows semi-automatic CSO creation. The algorithm
uses edge detection to support the user creating CSOs.

We also like to interpolate CSOs over slices. That means additional CSOs are
generated between manual segmentations based on a linear interpolation.

As a last step, we will group together CSOs of the same anatomical unit.

## Steps to do
### Develop your network and create CSOs

In order to do that, create the shown network. You can use the network
from the previous example and exchange the `SoCSO`-Editor. In addition to
that, load the example image *$(DemoDataPath)/Thorax1_CT.small.tif* .
Now, create some CSOs on different, not consecutive slices. Afterwards,
hover over the `CSOManager` and press the emerging plus-sign. This
displays the amount of existing CSOs.

![Data Objects Contours Example 2](/images/tutorials/dataobjects/contours/DO2_02.png "Data Objects Contours Example 2")

### Create CSO interpolations
We like to generate interpolated contours for existing CSOs. In order to
do that, add the module `CSOSliceInterpolator` to your workspace and
connect it as shown.

![Slice Interpolation](/images/tutorials/dataobjects/contours/DO2_03.png "Slice Interpolation")

Open the panel of module `CSOSliceInterpolator` and change the *Group
Handling* and the *Mode* as shown. If you now press *Update* interpolating
CSOs are created.

![Slice Interpolation Settings](/images/tutorials/dataobjects/contours/DO2_04_2.png "Slice Interpolation Settings")  

You can see the interpolated CSOs are added to the `CSOManager`. If you
now scroll through your slices, you can find the interpolated CSOs.

You can also take a look on all existing CSOs by inspecting the output
of the `CSOManager` using the Output Inspector. Custom CSOs are
displayed in white and interpolated CSOs are marked in yellow.

![Interpolated CSOs](/images/tutorials/dataobjects/contours/DO2_06.png "Interpolated CSOs")

### Group CSOs
We like to segment both lobes of the lung. To distinguish the CSOs of both lungs, we like to group CSOs together, according to the lung, they belong to. First, we like to group together all CSOs belonging to the lung we already segmented. In order to do this, open the `CSOManager`. Create a new Group and label that Group. We chose the label *Left Lung*. Now, mark the created Group and all CSOs you want to include into that group and press *Combine*. If you click on the Group, all CSOs belonging to this Group are marked with a star.

{{<alert class="warning" caption="Attention">}}
Keep in mind, that the right lung might be displayed on the left side of the image and vice versa, depending on your view.
{{</alert>}}

![Creating CSO Groups](/images/tutorials/dataobjects/contours/DO2_07.png "Creating CSO Groups")
![Creating CSO Groups](/images/tutorials/dataobjects/contours/DO2_07_2.png "Creating CSO Groups")

As a next step, segment the right lung by creating new CSOs. 
![Creation of further CSOs](/images/tutorials/dataobjects/contours/DO2_08.png "Creation of further CSOs")

Create a new Group for all CSOs of the right lung. We labeled this Group *Right Lung*. Again, mark the group and the CSOs you like to combine and press *Combine*.
![Grouping remaining CSOs](/images/tutorials/dataobjects/contours/DO2_09.png "Grouping remaining CSOs")

To visually distinguish the CSOs of both groups, change the color of each group under {{< menuitem "Group" "Visuals" >}}. We changed the color of the *Left Lung* to be green and of the *Right Lung* to be orange of path and seed points. In addition, we increased the *Width* of the path points.
![Interpolated CSOs](/images/tutorials/dataobjects/contours/DO2_10.png "Interpolated CSOs")

As a last step, we need to disconnect the module `SoCSOVisualizationSettings`, as this module overwrites the visualization settings we enabled for each group in the `CSOManager`.
![Interpolated CSOs](/images/tutorials/dataobjects/contours/DO2_11.png "Interpolated CSOs")

## Summary
* `SoCSOLiveWireEditor` can be used to create CSOs semi-automatically
* CSO interpolations can be created using `CSOSliceInterpolator`
* CSOs can be grouped together using the `CSOManager`

{{< networkfile "examples/data_objects/contours/example2" >}}

 [//]: <> (MVL-682)
