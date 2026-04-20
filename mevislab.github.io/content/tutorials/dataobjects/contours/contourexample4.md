---
title: "Contour Example 4: Annotation of Images"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 680
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO", "Annotations"]
menu: 
  main:
    identifier: "contourexample4"
    title: "Calculate the Volume of Your Segmentation and Display Milliliter Value on Your Image in the Viewer"
    weight: 680
    parent: "contours"
---

# Contour Example 4: Annotation of Images {#TutorialContoursExample4}

{{< youtube "bT2ZprYcuOU">}}

## Introduction
In this example, we like to calculate the volume of our object, in this
case, the part of the lung we have segmented. 

## Steps to Do

### Develop Your Network and Calculate the Lung Volume
Add the modules `CalculateVolume` and `SoView2DAnnotation` to your workspace
and connect both modules as shown. Update the module `CalculateVolume`,
which directly shows the volume of our object.

![Network for segmenting and viewing contours in 2D and in 3D](images/tutorials/dataobjects/contours/DO4_01.png "Network for segmenting and viewing contours in 2D and in 3D")

### Display the Lung Volume in the Image
We now like to display the volume in the image viewer. For this, open
the panel of the modules `CalculateVolume` and `SoView2DAnnotation`.
Open the tab *Input* in the panel of the module `SoView2DAnnotation`. Now,
establish a parameter connection between <field>Total Volume</field> calculated in
the module `CalculateVolume` and the <field>input00</field> of the module
`SoView2DAnnotation`. This connection projects the <field>Total Volume</field> to the
input of `SoView2DAnnotation`.

![Display volume](images/tutorials/dataobjects/contours/DO4_02.png "Display volume")

Go back to the tab *General* to select the <field>Annotation Mode</field> *User*. A separate tab exists for
each annotation mode.

![Annotate image: settings](images/tutorials/dataobjects/contours/DO4_03_2.png "Annotate image: settings")

We select the tab *User* that we like to work on. You can see four
fields that display four areas of a viewer in which you can add
information text to the image.

![Annotate image: user annotations](images/tutorials/dataobjects/contours/DO4_04.png "Annotate image: user annotations")

In this example we only like to add the volume, so delete all present
input and replace that by the shown text. Now, you can see that the
volume is displayed in the image viewer. If this is not the case, switch
the annotations of the viewer by pressing the keyboard shortcut {{< keyboard "A" >}}.

![Display volume in image](images/tutorials/dataobjects/contours/DO4_05.png "Display volume in image")

## Summary
* `CalculateVolume` calculates the volume of a voxel image.
* `SoView2DAnnotation` enables to manually change the annotation mode of a viewer.
* Annotations shown in a `View2D` can be customized by using a `SoView2DAnnotation` module.

{{< networkfile "examples/data_objects/contours/example4/ContourExample4.mlab" >}}

 [//]: <> (MVL-682)
