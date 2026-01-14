---
title: "Example 6: Creating Multi-View Layouts Using SoViewportRegion"
date: 2025-04-22
status: "OK"
draft: false
weight: 460
tags: ["Beginner", "Tutorial", "SoViewportRegion", "Layout", "Multi-View"]
menu: 
  main:
    identifier: "soviewportregion"
    title: "Creating Multi-View Layouts Using SoViewportRegion"
    weight: 460
    parent: "basicmechanisms"
---
# Example 6: Creating Multi-View Layouts Using SoViewportRegion

## Introduction
In this guide, we will show how to use the `SoViewportRegion` module to create custom layouts within the `SoRenderArea` module. This allows you to display multiple views or slices in a single window.

We will demonstrate how to: 
* Divide the render area into multiple regions. 
* Assign different content to each region. 
* Use alternative methods, such as `SoView2D`, when applicable.

## Prepare Your Network

### Displaying Three Images in One Panel
Add an `ImageLoad` module to your workspace and select a 3D image like *./MeVisLab/Resources/DemoData/MRI_Head.tif* from the MeVisLab demo data directory. Connect an `OrthoReformat3` module and add three `View2D` modules.

![Image Display Setup](/images/tutorials/basicmechanics/E6_1.png "Image Display Setup")

Opening the three `View2D` module panels now shows the image data in three orthogonal views. The module `OrthoReformat3` transforms the input image (by rotating and/or flipping) into the three main views commonly used.

![3 Views in 3 Viewers](/images/tutorials/basicmechanics/E6_2.png "3 Views in 3 Viewers")

The module `SoViewportRegion` divides the render window into multiple areas, allowing different views or slices to be shown in the same window. It's useful in medical applications, like displaying MRI or CT images from different angles (axial, sagittal, coronal) at once, making data analysis easier and faster.

Add three `SoViewportRegion` modules and connect each one to a `View2D` module. To display the hidden outputs of the `View2D` module, press {{< keyboard "SPACE" >}} and connect the output to the input of `SoViewportRegion` as shown below.

![Connect SoViewportRegion with View2D](/images/tutorials/basicmechanics/E6_3.png "Connect SoViewportRegion with View2D")

Add a `SoRenderArea` for your final result to the network and connect all three `SoViewportRegion` modules to it.

The result is that all of your viewers are initially displayed on top of each other in the bottom right corner.

![All three viewers on top of each other](/images/tutorials/basicmechanics/E6_4.png "All three viewers on top of each other")

This happens, because all three `SoViewportRegion` modules have the same settings for position and height or width.

![SoViewportRegion](/images/tutorials/basicmechanics/E6_5.png "SoViewportRegion")

The `SoViewportRegion` module allows to define the x- and y-position and the width and height of the image in the `SoRenderArea` module.

Values can be in pixels or as fractions from 0 to 1:

* 0 means the start of the render area (depending on the reference)
* 0.5 means the center of the render area
* 1 means the end of the render area  (depending on the reference)

We want to create a layout with the following setting:
* Axial view on the left side
* Coronal view on the top right side
* Sagittal view on the bottom right side 

![Target Layout](/images/tutorials/basicmechanics/E6_6.png "Target Layout")

Now open the left `SoViewportRegion` module and change settings:

* **X-Position and Width**
  * *Left Border* to 0
  * *Right Border* to 0.5
  * *Domain* Fraction of width
  * *Reference* Left window border
* **Y-Position and Height**
  * *Lower Border* to 1
  * *Upper Border* to 0 
  * *Domain* Fraction of height
  * *Reference* Upper window border

![Axial View](/images/tutorials/basicmechanics/E6_7.png "Axial View")

Continue with the middle `SoViewportRegion` module and change settings:

* **X-Position and Width**
  * *Left Border* to 0
  * *Right Border* to 0.5
  * *Domain* Fraction of width
  * *Reference* Right window border
* **Y-Position and Height**
  * *Lower Border* to 0.5
  * *Upper Border* to 0 
  * *Domain* Fraction of smallest dimension
  * *Reference* Upper window border

![Coronal View](/images/tutorials/basicmechanics/E6_8.png "Coronal View")

The right `SoViewportRegion` module should look as follows:

* **X-Position and Width**
  * *Left Border* to 0.5
  * *Right Border* to 0
  * *Domain* Fraction of width
  * *Reference* Right window border
* **Y-Position and Height**
  * *Lower Border* to 1
  * *Upper Border* to 0.5
  * *Domain* Fraction of smallest dimension
  * *Reference* Upper window border

![Sagittal View](/images/tutorials/basicmechanics/E6_9.png "Sagittal View")

#### Displaying Four Images in One Panel
In the next example, the `SoRenderArea` will display four views at the same time: axial, coronal, sagittal, and a 3D view.

![3D View Layout](/images/tutorials/basicmechanics/E6_11.png "3D View Layout")

These views will be arranged in a single panel that is split into two sides with each side showing two images. To add the 3D view, insert a `View3D` module and connect it to the `ImageLoad` module. Then connect the `View3D` to `SoCameraInteraction`, connect that to another `SoViewportRegion`, and finally to `SoRenderArea`.

![3D View Network](/images/tutorials/basicmechanics/E6_10.png "3D View Network")

Now open the left `SoViewportRegion` module and change settings:

* **X-Position and Width**
  * *Left Border* to 0
  * *Right Border* to 0.5
  * *Domain* Fraction of width
  * *Reference* Left window border
* **Y-Position and Height**
  * *Lower Border* to **0.5**
  * *Upper Border* to 0 
  * *Domain* Fraction of height
  * *Reference* Upper window border

Open the right `SoViewportRegion` connected to the `SoCameraInteraction` module and change settings:

* **X-Position and Width**
  * *Left Border* to 0
  * *Right Border* to 0.5
  * *Domain* Fraction of width
  * *Reference* Left window border
* **Y-Position and Height**
  * *Lower Border* to 1
  * *Upper Border* to 0.5 
  * *Domain* Fraction of height
  * *Reference* Upper window border

This setup will let you interact with the 3D view and display all four views together as shown in the figure below.

![3D View](/images/tutorials/basicmechanics/E6_12.png "3D View")

You will see that the orientation cube of the 3D viewer appears in the bottom right corner of the `SoRenderArea`. To resolve this, you can check *Render delayed paths* in the `SoViewportRegion` module of the 3D viewer.

![Final Network](/images/tutorials/basicmechanics/E6_13.png "Final Network")

## Alternatively Using `SoView2D`
In the case you want the same dataset to be visualized in multiple viewers, the module `SoView2D` already provides this functionality.

![Initial SoView2D](/images/tutorials/basicmechanics/SoView2D_1.png "Initial SoView2D")

Whenever you are using the `SoView2D` module to visualize a 2D dataset, you need to add a `View2DExtensions` module and, for example, a `SoRenderArea` module. Without the `View2DExtensions` module, interactions like scrolling through slices or changing the window and level settings will not be possible.

By default, you will see your images in a single viewer the same way as if you use the `View2D` module. The *number of columns* is defined as *1* by default. If you now change the *Number of Slices* to something like *3*, you will see three viewers shown in a single column. As we can only connect one dataset, this network cannot display multiple series at the same time.

![Multiple slices in SoView2D](/images/tutorials/basicmechanics/SoView2D_2.png "Multiple slices in SoView2D")

Changing the *number of columns* to *3* and the *Number of Slices* to *9* results in a 3x3 layout.

![Multiple slices and columns in SoView2D](/images/tutorials/basicmechanics/SoView2D_3.png "Multiple slices and columns in SoView2D")

By default, the module shows consecutive slices with a slice step size *1*. If you change this, you can define the size of the steps between the viewers. If the resulting slice does not exist in the dataset, the viewer remains empty. 

![Not existing slices](/images/tutorials/basicmechanics/SoView2D_4.png "Not existing slices")

You are also able to define a slab size. This means the depth of the slab. You can either use the blend mode *Maximum* or *Blend*.

## Exercise
You can play around with the different `SoViewportRegion` modules to create your own layouts by setting the values a little different.

![Exercise](/images/tutorials/basicmechanics/E6_14.png "Exercise")

## Summary
* Own layouts can be created by using multiple `SoViewportRegion` modules.

{{< networkfile "examples/basic_mechanisms/soviewportregion.mlab" >}}
