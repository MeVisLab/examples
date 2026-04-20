---
title: "Contour Example 2: Contour Interpolation"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 670
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO", "Interpolation"]
menu: 
  main:
    identifier: "contourexample2"
    title: "Creating Contours Using Live Wire and Linear Interpolation, Grouping CSOs for Different Colors"
    weight: 670
    parent: "contours"
---

# Contour Example 2: Creating Contours using Live Wire and Interpolation {#TutorialContoursExample2}

{{< youtube "l2ih_maKfSw">}}

## Introduction
In this example, we like to create CSOs using the [**Live Wire
Algorithm**](https://en.wikipedia.org/wiki/Livewire_Segmentation_Technique),
which allows semiautomatic CSO creation. The algorithm
uses edge detection to support the user creating CSOs.

We also like to interpolate CSOs over slices. That means additional CSOs are
generated between manual segmentations based on a linear interpolation.

As a last step, we will group together CSOs of the same anatomical unit.

## Steps to Do

### Develop Your Network and Create CSOs
In order to do that, create the shown network. You can use the network
from the previous example and exchange the `SoCSO*Editor`. In addition to
that, load the example image *$(DemoDataPath)/Thorax1_CT.small.tif* .
Now, create some CSOs on different, not consecutive slices. Afterward,
hover over the `CSOManager` and press the emerging *plus* symbol. This
displays the amount of existing CSOs.

![Left lung has been segmented on four slices](images/tutorials/dataobjects/contours/DO2_02.png "Left lung has been segmented on four slices")

### Create CSO Interpolations
We like to generate interpolated contours for existing CSOs. In order to
do that, add the module `CSOSliceInterpolator` to your workspace and
connect it as shown.

![Added a slice interpolator](images/tutorials/dataobjects/contours/DO2_03.png "Added a slice interpolator")

Open the panel of module `CSOSliceInterpolator` and change the <field>Group
Handling</field> and the <field>Mode</field> as shown. If you now press <field>Update</field>, interpolated CSOs are created.

![Slice interpolator settings](images/tutorials/dataobjects/contours/DO2_04_2.png "Slice interpolator settings")

You can see the interpolated CSOs are added to the `CSOManager`. If you
now scroll through your slices, you can find the interpolated CSOs.

You can also take a look on all existing CSOs by inspecting the output
of the `CSOManager` using the Output Inspector. Custom CSOs are
displayed in white and interpolated CSOs are marked in yellow.

![Interpolated CSOs](images/tutorials/dataobjects/contours/DO2_06.png "Interpolated CSOs")

### Group CSOs
We like to segment both lobes of the lung. To distinguish the CSOs of both lungs, we like to group CSOs together, according to the lung they belong to. First, we like to group together all CSOs belonging to the lung we already segmented. In order to do this, open the `CSOManager`. Create a new CSOGroup and label that CSOGroup. We chose the label *Left Lung*. Now, mark the created CSOGroup and all CSOs you want to include into that group and press <field>Combine</field>. If you click {{< mousebutton "left" >}} on the CSOGroup, all CSOs belonging to this CSOGroup are marked with an asterisk.

{{<alert class="warning" caption="Attention">}}
Keep in mind that the right lung might be displayed on the left side of the image, and vice versa, depending on your view.
{{</alert>}}

![Creating CSOGroups: labeling](images/tutorials/dataobjects/contours/DO2_07.png "Creating CSOGroups: labeling")
![Creating CSOGroups: combining](images/tutorials/dataobjects/contours/DO2_07_2.png "Creating CSOGroups: combining")

As a next step, segment the right lung by creating new CSOs. 
![Creation of further CSOs for the right lung](images/tutorials/dataobjects/contours/DO2_08.png "Creation of further CSOs for the right lung")

Create a new CSOGroup for all CSOs of the right lung. We labeled this CSOGroup *Right Lung*. Again, mark the group and the CSOs you like to combine and press <field>Combine</field>.
![Grouping CSOs for the right lung](images/tutorials/dataobjects/contours/DO2_09.png "Grouping CSOs for the right lung")

To visually distinguish the CSOs of both groups, change the color of each group under {{< menuitem "Group" "Visuals" >}}. We changed the color of the *Left Lung* to be green and of the *Right Lung* to be orange for path and seed points. In addition, we increased the <field>Width</field> of the path points.
![Setting visual parameters for CSOGroups](images/tutorials/dataobjects/contours/DO2_10.png "Setting visual parameters for CSOGroups")

As a last step, we need to disconnect the module `SoCSOVisualizationSettings`, as this module overwrites the visualization settings we enabled for each group in the `CSOManager`.
![Interpolated CSOs](images/tutorials/dataobjects/contours/DO2_11.png "Interpolated CSOs")

## Summary
* `SoCSOLiveWireEditor` can be used to create CSOs semiautomatically.
* CSO interpolations can be created using `CSOSliceInterpolator`.
* CSOs can be grouped together using the `CSOManager`.

{{< networkfile "examples/data_objects/contours/example2/ContourExample2.mlab" >}}

 [//]: <> (MVL-682)
