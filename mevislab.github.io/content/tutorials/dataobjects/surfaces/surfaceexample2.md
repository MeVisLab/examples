---
title: "Surface Example 2: Processing and Modification of WEM"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM"]
menu: 
  main:
    identifier: "surfaceexample2"
    title: "Examples for modification, smoothing and annotations on WEM"
    weight: 710
    parent: "surfaces"
---
# Surface Example 2: Processing and Modification of WEM
## Introduction
In this example, you will learn how to modify and process WEMs.

## Steps to do
### Develop your network
#### Modification of WEMs
Use the module `WEMLoad` to load the file *venus.off*. Then add and connect the shown modules. We like to display the WEM *venus* two times, one time this WEM is modified. You can use the module `WEMModify` to apply modifications. In its panel, change the scale and the size of the WEM. Now you see two times the `venus` next to each other.

![WEMModify](/images/tutorials/dataobjects/surfaces/DO7_01.png "WEMModify")

#### Smoothing of WEMs
It is possible to smooth the WEM using the module `WEMSmooth`. Add this module to your network as shown. You can see the difference of the smoothed and the unsmoothed WEM in your viewer. There are more modules, which can modify WEMs, for example `WEMExtrude`. You can find them via search or in {{< menuitem "Modules" "Visualization" "Surface Meshes (WEM)" >}}.

![WEMSmooth](/images/tutorials/dataobjects/surfaces/DO7_02.png "WEMSmooth")

#### Calculate distance between WEMs
Now, we like to calculate the distance between our two WEMs. In order to do this, add and connect the module `WEMSurfaceDistance` as shown.

![Calculate surface distance](/images/tutorials/dataobjects/surfaces/DO7_03.png "Calculate surface distance")

#### Annotations in 3D
As a last step, we like to draw the calculated distances as annotations into the image. This is a little bit tricky as we need the module `SoView2DAnnotation` to create annotations in a 3D viewer. Add and connect the following modules as shown. What is done here? We use the module `SoView2D` to display a 2D image in the `SoExaminerViewer`, in addition to the WEMs we already see in the viewer. We do not see an additional image in the viewer, as we chose no proper input image to the module `SoView2D` using the module `ConstantImage` with value 0. Thus, we pretend to have a 2D image, which we can annotate. Now, we use the module `SoView2DAnnotation` to annotate the pretended-2D-image, displayed in the viewer of `SoExaminerViewer`. We already used the module `SoView2DAnnotation` in [Contour Example 4](tutorials/dataobjects/contours/contourexample4/).

![Annotation modules](/images/tutorials/dataobjects/surfaces/DO7_05.png "Annotation modules")

Now, change the *Annotation Mode* to *User*, as we like to insert custom annotations. In addition, disable to *Show vertical ruler*.

![Select annotation mode](/images/tutorials/dataobjects/surfaces/DO7_06.png "Select annotation mode")

Next, open the tab *Input* and draw parameter connections from the results of the distance calculations, which can be found in the panel of `WEMSufaceDistance`, to the input fields in the panel of `SoView2DAnnotation`.

![Define annotation parameters](/images/tutorials/dataobjects/surfaces/DO7_07.png "Define annotation parameters")

You can design the annotation overlay as you like in the tab *User*. We decided to only display the minimum and maximum distance between both WEMs.

![Annotation design](/images/tutorials/dataobjects/surfaces/DO7_04.png "Annotation design")

As we use a 2D annotation module to annotate a 3D viewer, it is important to get rid of all 2D orientation annotations, which you can edit in the tab *Orientation*.

![Disable 2D orientation annotations](/images/tutorials/dataobjects/surfaces/DO7_08.png "Disable 2D orientation annotations")

Now, you can see the result in the viewer. If the annotations are not visible, press {{< keyboard "a">}} a few times to change the annotation mode.
![Display surface distance in viewer](/images/tutorials/dataobjects/surfaces/DO7_09.png "Display surface distance in viewer")

## Summary
* There are several modules to modify and process WEMs, e.g. `WEMModify`, `WEMSmooth`.
* To calculate the minimal and maximal surface distance between two WEMs, use the module `WEMSurfaceDistance`.
* To create annotations in 3D, the module `SoView2DAnnotation` can be used, when adapted to be used in combination with a 3D viewer. 


{{< networkfile "examples/data_objects/surface_objects/example1/SurfaceExample1.mlab" >}}
