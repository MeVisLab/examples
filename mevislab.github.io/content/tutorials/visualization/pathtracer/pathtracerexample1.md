---
title: "Example 6.1: Volume Rendering vs. Path Tracer"
date: "2023-02-23"
status: "open"
draft: false
weight: 578
tags: ["Advanced", "Tutorial", "Visualization", "3D", "Volume Rendering", "Path Tracer"]
menu: 
  main:
    identifier: "pathtracer_example1"
    title: "Comparison Between Volume Rendering and MeVisLab Path Tracer"
    weight: 578
    parent: "visualization_example6"
---

# Example 6.1: Volume Rendering vs. Path Tracer

{{< youtube "E0H87Cimu_M">}}

## Introduction
In this example, you develop a network to show some differences between volume rendering and the **MeVis Path Tracer**. You will visualize the same scene using both 3D rendering techniques and some of the modules for path tracing.

<!--more-->

{{<alert class="warning" caption="Attention">}}
The **MeVis Path Tracer** requires an NVIDIA graphics card with CUDA support. In order to check your hardware, open MeVisLab and add a `SoPathTracer` module to your workspace. You will see a message if your hardware does not support CUDA:

*MeVisLab detected an Intel onboard graphics adapter. If you experience rendering problems, try setting the environment variables SOVIEW2D_NO_SHADERS and GVR_NO_GLSL.* <br />
*Handling cudaGetDeviceCount returned 35 (CUDA driver version is insufficient for CUDA runtime version)*
{{</alert>}}

## Steps to Do
As a first step for comparison, you are creating a 3D scene with two spheres using the already known volume rendering.

### Volume Rendering

#### Create 3D Objects
Add three `WEMInitialize` modules for one *Cube* and two *Icosphere* to your workspace and connect each of them to a `SoWEMRenderer`. Set <field>instanceName</field> of the `WEMInitialize` modules to *Cube*, *Sphere1*, and *Sphere2*. Set <field>instanceName</field> of the `SoWEMRenderer` modules to and *RenderCube*, *RenderSphere1*, and *RenderSphere2*.

For *RenderSphere1*, define a <field>Diffuse Color</field> *yellow* and set <field>Face Alpha</field> to *0.5*. The *RenderCube* remains as is and the *RenderSphere2* is defined as <field>Diffuse Color</field> *red* and <field>Face Alpha</field> *0.5*.

Group your modules and name the group *Initialization*. Your network should now look like this:

![Example initialization](images/tutorials/visualization/pathtracer/Example1_1.png "Example initialization")

Use the Output Inspector for your `SoWEMRenderer` outputs and inspect the 3D rendering. You should have a yellow and a red sphere, and a grey cube.

{{< imagegallery 3 "images/tutorials/visualization/pathtracer" "Sphere1" "Sphere2" "Cube" >}}

#### Rendering
Add two `SoGroup` modules and one `SoBackground` to your network. Connect the modules as seen below.

![Example group](images/tutorials/visualization/pathtracer/Example1_2.png "Example group")

If you now inspect the output of the `SoGroup`, you will see an orange sphere. 

![Missing translation](images/tutorials/visualization/pathtracer/Example1_3.png "Missing translation")

You did not translate the locations of the three objects; they are all located at the same place in world coordinates. Open the `WEMInitialize` panels of your 3D objects and define the following translations and scalings:

{{< imagegallery 3 "images/tutorials/visualization/pathtracer" "WEMInitializeSphere1" "WEMInitializeSphere2" "WEMInitializeCube" >}}

The result of the `SoGroup` now shows two spheres on a rectangular cube.

![Objects translated and scaled](images/tutorials/visualization/pathtracer/Example1_4.png "Objects translated and scaled")

For the viewer, you now add a `SoCameraInteraction`, a `SoDepthPeelRenderer`, and a `SoRenderArea` module to your network and connect them.

![Network with viewer](images/tutorials/visualization/pathtracer/Example1_5.png "Network with viewer")

You now have a 3D volume rendering of our three objects.

In order to distinguish between the two viewers, you now add a label to the `SoRenderArea` describing that this is the *Volume Rendering*. Add a `SoMenuItem`, a `SoBorderMenu`, and a `SoSeparator` to your `SoRenderArea`.

![SoMenuItem](images/tutorials/visualization/pathtracer/Example1_6.png "SoMenuItem")

Define the <field>Label</field> of the `SoMenuItem` as *Volume Rendering* and set <field>Border Alignment</field> to *Top Right* and <field>Menu Direction</field> to *Horizontal* for the `SoBorderMenu`.

![Label in SoRenderArea](images/tutorials/visualization/pathtracer/Example1_7.png "Label in SoRenderArea")

Finally, you should group all modules belonging to your volume rendering.

![Volume rendering network](images/tutorials/visualization/pathtracer/Example1_8.png "Volume rendering network")

### Path Tracing
For the path tracer, you can just reuse our 3D objects from volume rendering. This helps us to compare the rendering results.

#### Rendering
Path tracer modules fully integrate into MeVisLab Open Inventor; therefore, the general principles and the necessary modules are not completely different. Add a `SoGroup` module to your workspace and connect it to your 3D objects from `SoWEMRenderer`. A `SoBackground` as in volume rendering network is not necessary but you add a `SoPathTracerMaterial` and connect it to the `SoGroup`. You can leave all settings as default for now.

![Path tracer material](images/tutorials/visualization/pathtracer/Example1_9.png "Path tracer material")

Add a `SoPathTracerAreaLight`, a `SoPathTracerMesh`, and a `SoPathTracer` to a `SoSeparator` and connect the `SoPathTracerMesh` to your `SoGroup`. This adds your 3D objects to a path tracer scene. 

![Path tracer network](images/tutorials/visualization/pathtracer/Example1_10.png "Path tracer network")

Selecting the `SoSeparator` output already shows a preview of the same scene rendered via path tracing.

![Path tracer preview](images/tutorials/visualization/pathtracer/Example1_11.png "Path tracer preview")

Add a `SoCameraInteraction` and a `SoRenderArea` to your network and connect them as seen below.

![Added SoCameraInteraction](images/tutorials/visualization/pathtracer/Example1_12.png "Added SoCameraInteraction")

You can now use both `SoRenderArea` modules to visualize the differences side by side. You should also add the `SoMenuItem`, a `SoBorderMenu`, and a `SoSeparator` to your `SoRenderArea` in order to have a label for path tracing inside the viewer.

Define the <field>Label</field> of the `SoMenuItem` as *Path Tracing* and set <field>Border Alignment</field> to *Top Right* and <field>Menu Direction</field> to *Horizontal* for the `SoBorderMenu`.

![SoMenuItem as a label in SoRenderArea](images/tutorials/visualization/pathtracer/Example1_13.png "SoMenuItem as a label in SoRenderArea")

Finally, group your path tracer modules to another group named *Path Tracing*.

![New group for path tracing](images/tutorials/visualization/pathtracer/Example1_14.png "New group for path tracing")

![Side by side: volume rendering vs. path tracing](images/tutorials/visualization/pathtracer/Example1_15.png "Side by side: volume rendering vs. path tracing")

### Share the Same Camera
Finally, you want to have the same camera perspective in both viewers, so that you can see the differences. Add a `SoPerspectiveCamera` module to your workspace and connect it to the volume rendering and the path tracer network. The Path Tracer network additionally needs a SoGroup, see below for connection details. You have to trigger <field>Detect Camera From Scene</field> in both of your `SoCameraInteraction` modules in order to synchronize the view for both `SoRenderArea` viewers.

![Camera synchronization by sharing a camera](images/tutorials/visualization/pathtracer/Example1_16.png "Camera synchronization by sharing a camera")

{{<alert class="info" caption="Additional Info">}}
Path tracing requires a lot of iterations before reaching the best possible result. You can see the maximum number of iterations defined and the current iteration in the `SoPathTracer` panel. The more iterations, the better the result but the more time it takes to finalize your image.
{{</alert>}}

{{< imagegallery 3 "images/tutorials/visualization/pathtracer" "PathTracer_1_Iteration" "PathTracer_100_Iterations" "PathTracer_1000_Iterations" >}}

## Results
Path tracing provides a much more realistic way to visualize the behavior of light in a scene. It simulates the scattering and absorption of light within the volume. 

## Exercises
1. Play around with different `SoPathTracerMaterial` settings and define different materials.
2. Change the maximum number of iterations in `SoPathTracer` module.
3. Change the configurations in `SoPathTracerAreaLight` module.

## Summary
* Path tracer modules can be used the same way as Open Inventor modules.
* A `SoPerspectiveCamera` can be used for multiple viewers to synchronize camera position.
* Path tracing produces beautiful, photorealistic renderings but can be computationally expensive.

{{< networkfile "examples/visualization/example6/pathtracer1.mlab" >}}
