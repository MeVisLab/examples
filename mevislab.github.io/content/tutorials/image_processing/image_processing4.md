---
title: "Example 4: Subtract 3D objects"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Advanced", "Tutorial", "Image Processing", "3D", "Subtraction"]
menu: 
  main:
    identifier: "imageprocessing4"
    title: "In this example, we create two 3-dimensional and subtract them."
    weight: 620
    parent: "imageprocessing"
---

# Example 4: Subtract 3D objects
## Introduction
In this example, we load an image and render it as `WEMIsoSurface`. Then we create a 3-dimensional `SoSphere` and subtract the sphere from the initial WEM.

## Steps to do
### Develop your network
Add a `LocalImage` module to your workspace and select load *$(DemoDataPath)/BrainMultiModal/ProbandT1.dcm*. Add a `WEMIsoSurface`, a `SoWEMRenderer`, a `SoBackground` and a `SoExaminerViewer` module and connect them as seen below. Make sure to configure the `WEMIsoSurface` to use a *Iso Min. Value* of 420 and a *Voxel Sampling* 1.

![Example Network](/images/tutorials/image_processing/network_example4.png "Example Network")

The `SoExaminerViewer` now shows the head as a 3-dimensional rendering.

![SoExaminerViewer](/images/tutorials/image_processing/SoExaminerViewer_initial.png "SoExaminerViewer")

### Add a 3D sphere to your scene
We now want to add a 3-dimensional sphere to our scene. Add a `SoMaterial` and a `SoSphere` to your network, connect them to a `SoSeparator` and then to the `SoExaminerViewer`. Set your material to use a *Diffuse Color* red and adapt the size of the sphere to *Radius* 50.

![Example Network](/images/tutorials/image_processing/network_example4b.png "Example Network")

The `SoExaminerViewer` now shows the head and the red sphere inside.

![SoExaminerViewer](/images/tutorials/image_processing/SoExaminerViewer_sphere.png "SoExaminerViewer")

### Set location of your sphere
In order to define the best possible location of the sphere, we additionally add a `SoTranslation` Module and connect it to the `SoSeparator` between the material and the sphere. Define a translation of x=0, y=20 and z=80.

![Example Network](/images/tutorials/image_processing/network_example4c.png "Example Network")

### Subtract the sphere from the head
We now want to subtract the sphere from the head to get a hole. Add another `SoWEMRenderer`, a `WEMLevelSetBoolean` and a `SoWEMConvertInventor` to the network and connect them to a `SoSwitch` as seen below. The `SoSwitch` also needs to be connected to the `SoWEMRenderer` of the head. Set your `WEMLevelSetBoolean` to use the *Mode* **Difference**.

![Example Network](/images/tutorials/image_processing/network_example4d.png "Example Network")

What happens in your network now?

1) The `SoSphere` is converted to a WEM.
2) The WEMs from the head and from the sphere are subtracted by using a `WEMLevelSetBoolean`.
3) The result of the subtraction is used for a `SoWEMRenderer`
4) Both `SoWEMRenderer` (the head on the left side and the subtraction on the right side) are inputs for a `SoSwitch`.
5) The `SoSwitch` toggles through its inputs and you can show the original WEM of the head or the subtraction.

{{< imagegallery 2 "/images/tutorials/image_processing" "SoExaminerViewer_1" "SoExaminerViewer_2" >}}

You can now toggle the hole to be shown or not, depending on your setting for the `SoSwitch`.

## Summary
* The module `WEMLevelSetBoolean` allows to subtract or add 3-dimensional WEM objects.
* The `SoSwitch` can toggle multiple inventor scenes as input

{{< networkfile "/examples/image_processing/example4/Subtract3DObjects.mlab" >}}