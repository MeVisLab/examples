---
title: "Surface Example 1: Creation of WEMs"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 705
tags: ["Beginner", "Tutorial", "Data Objects", "3D", "Surfaces", "Meshes", "WEM"]
menu: 
  main:
    identifier: "surfaceexample1"
    title: "Creation of Surface Objects (WEMs) From an Image Via WEMIsoSurface Module"
    weight: 705
    parent: "surfaces"
---

# Surface Example 1: Create Winged Edge Mesh out of Voxel Images and CSOs

{{< youtube "-KnZ5a27T0c">}}

## Introduction
In this example you will learn how to create a Winged Edge Mesh (WEM). There are several approaches on creating WEMs, a few of them are shown in this example. Instead of creating WEMs, they can also be imported, see chapter [Surface Objects (WEM)](tutorials/dataobjects/surfaceobjects).

## Steps to Do

### From Image to Surface: Generating WEMs out of Voxel Images
At first, we will create a WEM out of a voxel image using the module `WEMIsoSurface`. Add and connect the shown modules. Load the image *$(DemoDataPath)/Bone.tiff* and set the *Iso Min. Value* in the panel of `WEMIsoSurface` to 1200. Tick the box *Use image max. value*. The module `WEMIsoSurface` creates surface objects out of all voxels with an isovalue equal or above 1200 (and smaller than the image max value). The module `SoWEMRenderer` can now be used to generate an Open Inventor scene, which can be displayed by the module `SoExaminerViewer`.

![WEM](images/tutorials/dataobjects/surfaces/DO6_01.png "WEM")

### From Surface to Image: Generating Voxel Images out of WEM
It is not only possible to create WEMs out of voxel images. You can also transform WEMs into voxel images: Add and connect the modules `VoxelizeWEM` and `View2D` as shown and press the *Update* button of the module `VoxelizeWEM`. 

![WEM](images/tutorials/dataobjects/surfaces/DO6_02.png "WEM")

### From Contour to Surface: Generating WEMs out of CSOs
Now, we like to create WEMs out of CSOs. To create CSOs, load the network from [Contour Example 2](tutorials/dataobjects/contours/contourexample2) and create some CSOs.

Next, add and connect the module `CSOToSurface` to convert CSOs into a surface object. To visualize the created WEM, add and connect the modules `SoWEMRenderer` and `SoExaminerViewer`.

![WEM](images/tutorials/dataobjects/surfaces/DO6_03.png "WEM")

It is also possible to display the WEM in 2D in addition to the original image. In order to do that, add and connect the modules `SoRenderSurfaceIntersection` and `SoView2DScene`. The module `SoRenderSurfaceIntersection` allows to display the voxel image and the created WEM in one viewer using the same coordinates. In its panel, you can choose the color used for visualizing the WEM. The module `SoView2DScene` renders an Open Inventor scene graph into 2D slices.

![WEM](images/tutorials/dataobjects/surfaces/DO6_04.png "WEM")

If you like to transform WEMs back into CSOs, have a look at the module `WEMClipPlaneToCSO`.

## Summary
* Voxel images can be transformed into WEMs using `WEMIsoSurface`.
* WEMs can be transformed into voxel images using `VoxelizeWEM`.
* CSOs can be transformed into WEMS using `CSOToSurface`.
* WEMs can be transformed into voxel images using `WEMClipPlaneToCSO`.

{{<alert class="warning" caption="Warning">}}
Whenever converting voxel data to pixel data, keep the so called **Partial Volume Effect** in mind, see [wikipedia](https://en.wikipedia.org/wiki/Partial_volume_(imaging) "Partial Volume Effect") for details.
{{</alert>}}

{{< networkfile "examples/data_objects/surface_objects/example1/SurfaceExample1.mlab" >}}
