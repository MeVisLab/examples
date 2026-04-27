---
title: "Example 4: Subtracting 3D Surface Objects"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 620
tags: ["Advanced", "Tutorial", "Image Processing", "3D", "Subtraction"]
menu: 
  main:
    identifier: "imageprocessing4"
    title: "Subtracting 3D Surface Objects"
    weight: 620
    parent: "imageprocessing"
---

# Example 4: Subtracting 3D Objects

{{< youtube "VdvErVvoq2k" >}}

## Introduction
In this example, we load an image and render it as `WEMIsoSurface`. Then, we create a three-dimensional `SoSphere` and subtract the sphere from the initial WEM.

## Steps to Do

### Develop Your Network
Add a `LocalImage` module to your workspace and select load *$(DemoDataPath)/BrainMultiModal/ProbandT1.dcm*. Add a `WEMIsoSurface`, a `SoWEMRenderer`, a `SoBackground`, and a `SoExaminerViewer` module and connect them as seen below. Make sure to configure the `WEMIsoSurface` to use a <field>Iso Min. Value</field> of *420* and a <field>Voxel Sampling</field> of *1*.

![Example network](images/tutorials/image_processing/network_example4.png "Example network")

The `SoExaminerViewer` now shows the head as a three-dimensional rendering.

![SoExaminerViewer showing a head in 3D](images/tutorials/image_processing/SoExaminerViewer_initial.png "SoExaminerViewer showing a head in 3D")

### Add a 3D Sphere to Your Scene
We now want to add a three-dimensional sphere to our scene. Add a `SoMaterial` and a `SoSphere` to your network, connect them to a `SoSeparator` and then to the `SoExaminerViewer`. Set your material to use a *Diffuse Color* red and adapt the size of the sphere to *Radius* 50.

![Example network with a sphere](images/tutorials/image_processing/network_example4b.png "Example network with a sphere")

The `SoExaminerViewer` now shows the head and the red sphere inside.

![SoExaminerViewer shows the head and the sphere in 3D](images/tutorials/image_processing/SoExaminerViewer_sphere.png "SoExaminerViewer shows the head and the sphere in 3D")

### Set Location of Your Sphere
In order to define the best possible location of the sphere, we additionally add a `SoTranslation` module and connect it to the `SoSeparator` between the material and the sphere. Define a translation of x=0, y=20 and z=80.

![Translated sphere](images/tutorials/image_processing/network_example4c.png "Translated sphere")

### Subtract the Sphere from the Head
We now want to subtract the sphere from the head to get a hole. Add another `SoWEMRenderer`, a `WEMLevelSetBoolean`, and a `SoWEMConvertInventor` to the network and connect them to a `SoSwitch` as seen below. The `SoSwitch` also needs to be connected to the `SoWEMRenderer` of the head. Set your `WEMLevelSetBoolean` to use the *Mode* **Difference**.

![Network for subtracting a sphere from a head's surface](images/tutorials/image_processing/network_example4d.png "Network for subtracting a sphere from a head's surface")

What happens in your network now?

1) The `SoSphere` is converted to a WEM.
2) The WEMs from the head and from the sphere are subtracted by using a `WEMLevelSetBoolean`.
3) The result of the subtraction is used for a `SoWEMRenderer`
4) Both `SoWEMRenderer` (the head on the left side and the subtraction on the right side) are inputs for a `SoSwitch`.
5) The `SoSwitch` toggles through its inputs and you can show the original WEM of the head or the subtraction.

{{< imagegallery 2 "images/tutorials/image_processing" "SoExaminerViewer_1" "SoExaminerViewer_2" >}}

You can now toggle the hole to be shown or not, depending on your setting for the `SoSwitch`.

## Summary
* The module `WEMLevelSetBoolean` allows to subtract or add three-dimensional WEM objects.
* The `SoSwitch` can toggle multiple Open Inventor scenes as input.

{{< networkfile "examples/image_processing/example4/Subtract3DObjects.mlab" >}}
