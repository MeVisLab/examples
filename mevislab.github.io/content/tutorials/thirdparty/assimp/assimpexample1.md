---
title: "Example 1: 3D Printing in MeVisLab"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 862
tags: ["Beginner", "Tutorial", "assimp", "3D", "3D Printing", "stl"]
menu: 
  main:
    identifier: "assimpexample1"
    title: "3D Printing in MeVisLab"
    weight: 862
    parent: "assimp"
---

# Example 1: 3D Printing in MeVisLab

{{< youtube "82ysCYNTyso">}}

## Introduction
This example uses the *assimp* library to load a 3D file and save the file as *.stl* for 3D printing.

## Steps to Do

### Develop Your Network
Add the modules `SoSceneLoader`, `SoBackground`, and `SoExaminerViewer` to your workspace and connect them as seen below.

![Example Network](images/tutorials/thirdparty/assimp_example1.png "Example Network")

### Open the 3D File
Select the file *vtkCow.obj* from MeVisLab demo data directory. Open `SoExaminerViewer` and inspect the scene. You will see a 3D cow.

{{<alert class="info" caption="Info">}}
In the case you cannot see the cow, it might be located outside your current camera location. Trigger the field *rescanScene* in the case the cow is not visible.
{{</alert>}}

![Cow in SoExaminerViewer](images/tutorials/thirdparty/vtkCow.png "Cow in SoExaminerViewer")

Add a `SoSphere` to the workspace and connect it to your viewer. Define the *Radius* of your sphere to 2 and inspect your viewer.

![Cow and Sphere in SoExaminerViewer](images/tutorials/thirdparty/CowAndSphere.png "Cow and Sphere in SoExaminerViewer")

You can also define a material for your sphere but what we wanted to show is: You can use the loaded 3D files in MeVisLab Open Inventor scenes.

![Cow and red Sphere in SoExaminerViewer](images/tutorials/thirdparty/CowAndSphere_red.png "Cow and red Sphere in SoExaminerViewer")

### Save Your Scene as *.stl* File for 3D Printing
Add a `SoSceneWriter` module to your workspace. The `SoExaminerViewer` has a hidden output that can be shown on pressing {{<keyboard "SPACE">}}. Connect the `SoSceneWriter` to the output.

Name your output *.stl* file and select *Stl Ascii* as output format, so that we can inspect the result afterward.

![SoSceneWriter](images/tutorials/thirdparty/SoSceneWriter.png "SoSceneWriter")

{{<alert class="info" caption="Info">}}
The `SoSceneWriter` can save node color information when saving in Open Inventor (ASCII or binary) or in VRML format. The `SoSceneWriter` needs to be attached to a `SoWEMRenderer` that renders in *ColorMode:NodeColor*.

There are [tools](https://www.patrickmin.com/meshconv/) to convert from at least VRML to STL available for free.
{{</alert>}}

Write your scene and open the resulting file in your preferred editor. As an alternative, you can also open the file in an *.stl* file reader like Microsoft 3D Viewer.

![Microsoft 3D-Viewer](images/tutorials/thirdparty/Microsoft_3D_Viewer.png "Microsoft 3D-Viewer")

### Load the File Again
For loading your *.stl* file, you can use a `SoSceneLoader` and a `SoExaminerViewer`. 

{{<alert class="info" caption="Info">}}
More information about the *.stl* format can be found [here](https://en.wikipedia.org/wiki/STL_(file_format))
{{</alert>}}

![SoSceneLoader](images/tutorials/thirdparty/SoSceneLoader_2.png "SoSceneLoader")

## Summary
* MeVisLab is able to load and write many different 3D file formats including *.stl* format for 3D printing.
* Open Inventor scenes can be saved by using a `SoExaminerViewer` together with a `SoSceneWriter`.
