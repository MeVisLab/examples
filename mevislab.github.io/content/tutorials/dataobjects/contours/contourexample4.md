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
    title: "Calculate the volume of your segmentation and display ml value on your image in viewer"
    weight: 680
    parent: "contours"
---
# Contour Example 4: Annotation of Images {#TutorialContoursExample4}

{{< youtube "bT2ZprYcuOU">}}

## Introduction
In this example we like to calculate the volume of our object, in this
case the part of the lung we have segmented. 

## Steps to do
### Develop your network and calculate the lung volume
Add the module `CalculateVolume` and `SoView2DAnnotation` to your workspace
and connect both modules as shown. Update the module `CalculateVolume`,
which directly shows the volume of our object.

![Data Objects Contours Example 4](/images/tutorials/dataobjects/contours/DO4_01.png "Data Objects Contours Example 4")

### Display the lung volume in the image
We now like to display the volume in the image viewer. For this, open
the panel of the modules `CalculateVolume` and `SoView2DAnnotation`.
Open the tab *Input* in the panel of the module `SoView2DAnnotation`. Now
construct a parameter connection between *Total Volume* calculated in
the module `CalculateVolume` and the *input00* of the module
`SoView2DAnnotation`. This connection projects the *Total Volume* to the
input of `SoView2DAnnotation`.

![Display Volume](/images/tutorials/dataobjects/contours/DO4_02.png "Display Volume")

Go back to the tab *General* to select the *Annotation Mode User*. A separate tab exists for
each annotation mode.

![Annotate Image](/images/tutorials/dataobjects/contours/DO4_03_2.png "Annotate Image")

We select the tab *User* which we like to work on. You can see four
fields, which display four areas of a viewer in which you can add
information text to the image.

![Annotate Image 2](/images/tutorials/dataobjects/contours/DO4_04.png "Annotate Image")

In this example we only like to add the volume, so delete all present
input and replace that by the shown text. Now, you can see that the
volume is displayed in the image viewer. If this is not the case, switch
the annotations of the viewer by pressing the keyboard shortcut {{< keyboard "A" >}}.

![Display Volume in Image](/images/tutorials/dataobjects/contours/DO4_05.png "Display Volume in Image")

## Summary
* `CalculateVolume` can calculate the volume of a voxel image
* `SoView2DAnnotation` enables to manually change the annotation mode of a viewer
* Annotations shown in a `View2D` can be customized by using a `SoView2DAnnotation` module

{{< networkfile "examples/data_objects/contours/example4/ContourExample4.mlab" >}}

 [//]: <> (MVL-682)
