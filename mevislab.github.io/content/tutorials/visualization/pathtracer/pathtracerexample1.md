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
    title: "Comparison of a Volume Rendering and MeVisLab Path Tracer"
    weight: 575
    parent: "visualization_example6"
---
# Example 6.1: Volume Rendering vs. Path Tracer

## Introduction
In this example we develop a network to show some differences between volume rendering and the MeVisLab Path Tracer. You will visualize the same scene in both 3D rendering techniques and use some of the modules for path tracing.

{{<alert class="warning" caption="Attention">}}
The MeVis Path Tracer requires a NVIDIA graphics card with CUDA support. In order to check your hardware, open MeVisLab and add a `SoPathTracer` module to your workspace. You will see a message if your hardware does not support CUDA.

*MeVisLab detected an Intel onboard graphics adapter. If you experience rendering problems, try setting the environment variables SOVIEW2D_NO_SHADERS and GVR_NO_GLSL.* <br />
*Handling cudaGetDeviceCount returned 35 (CUDA driver version is insufficient for CUDA runtime version)*
{{</alert>}}

## Steps to do
As a first step for comparison, we are creating a 3D scene with 2 spheres using the already known volume rendering.

### Volume Rendering
#### Create 3D objects
Add 3 `WEMInitialize` modules for 1 *Cube* and 2 *Icosphere* to your workspace and connect each of them to a `SoWEMRenderer`. Set *instanceName* of the `WEMInitialize` modules to *Sphere1*, *Sphere2* and *Cube*. Set *instanceName* of the `SoWEMRenderer` modules to *RenderSphere1*, *RenderSphere2* and *RenderCube*.

For *RenderSphere1* define a *Diffuse Color* *yellow* and set *Face Alpha* to *0.5*. The *RenderCube* remains as is and the *RenderSphere2* is defined as *Diffuse Color* *red* and *Face Alpha* *0.5*.

Group your modules and name the group *Initialization*. Your network should now look like this:

![Example Initialization](/images/tutorials/visualization/pathtracer/Example1_1.png "Example Initialization")

Use the Output Inspector for your `SoWEMRenderer` outputs and inspect the 3D rendering. You should have a yellow and a red sphere and a grey cube.

{{< imagegallery 3 "/images/tutorials/visualization/pathtracer" "Sphere1" "Sphere2" "Cube" >}}

#### Rendering
Add 2 `SoGroup` modules and a `SoBackground` to your network. Connect the modules as seen below.

![Example Group](/images/tutorials/visualization/pathtracer/Example1_2.png "Example Group")

If you now inspect the output of the `SoGroup`, you will see an orange sphere. 

![Missing Translation](/images/tutorials/visualization/pathtracer/Example1_3.png "Missing Translation")

We did not translate the locations of our 3 objects, they are all located at the same place in world coordinates. Open the `WEMInitialize` panels of your 3D objects and define the following translations and scalings:

{{< imagegallery 3 "/images/tutorials/visualization/pathtracer" "WEMInitializeSphere1" "WEMInitializeSphere2" "WEMInitializeCube" >}}

The result of the `SoGroup` now shows 2 spheres on a rectangular cube.

![Objects Translated and Scaled](/images/tutorials/visualization/pathtracer/Example1_4.png "Objects Translated and Scaled")

For the viewer, we now add a `SoCameraInteraction`, a `SoDepthPeelRenderer` and a `SoRenderArea` module to your network and connect them.

![Network with Viewer](/images/tutorials/visualization/pathtracer/Example1_5.png "Network with Viewer")

You now have a 3D volume rendering of our 3 objects.

In order to distinguish between the 2 viewers, we now want to add a label to the `SoRenderArea` describing that this is the *Volume Rendering*. Add a `SoMenuItem`, a `SoBorderMenu` and a `SoSeparator` to your `SoRenderArea`.

![SoMenuItem](/images/tutorials/visualization/pathtracer/Example1_6.png "SoMenuItem")

Define the *Label* of the `SoMenuItem` as *Volume Rendering* and set *Border Alignment* to *Top Right* and *Menu Direction* to *Horizontal* for the `SoBorderMenu`.

![Label in SoRenderArea](/images/tutorials/visualization/pathtracer/Example1_7.png "Label in SoRenderArea")

In the end, you should group all modules belonging to your volume rendering.

![Volume Rendering Network](/images/tutorials/visualization/pathtracer/Example1_8.png "Volume Rendering Network")

### Path Tracing
For the Path Tracer, we can just re-use our 3D objects from volume rendering. This helps us to compare the rendering results.

#### Rendering
Path Tracer modules fully integrate into MeVisLab Open Inventor, therefore the general principles and the necessary modules are not completely different. Add a `SoGroup` module to your workspace and connect it to your 3D objects from `SoWemRenderer`. A `SoBackground` as in volume rendering network is not necessary but we add a `SoPathTracerMaterial` and connect it to the `SoGroup`. You can leave all settings as default for now.

![Path Tracer Material](/images/tutorials/visualization/pathtracer/Example1_9.png "Path Tracer Material")

Add a `SoPathTracerAreaLight`, a `SoPathTracerMesh` and a `SoPathTracer` to a `SoSeparator` and connect the `SoPathTracerMesh` to your `SoGroup`. This adds your 3D objects to a Path Tracer Scene. 

![Path Tracer](/images/tutorials/visualization/pathtracer/Example1_10.png "Path Tracer")

Selecting the `SoSeparator` output already shows a preview of the same scene rendered via Path Tracing.

![Path Tracer Preview](/images/tutorials/visualization/pathtracer/Example1_11.png "Path Tracer Preview")

Add a `SoCameraInteraction` and a `SoRenderArea` to your network and connect them as seen below.

![SoCameraInteraction](/images/tutorials/visualization/pathtracer/Example1_12.png "SoCameraInteraction")

You can now use both `SoRenderArea` modules to visualize the differences side by side. You should also add the `SoMenuItem`, a `SoBorderMenu` and a `SoSeparator` to your `SoRenderArea` in order to have a label for Path Tracing inside the viewer.

Define the *Label* of the `SoMenuItem` as *Path Tracing* and set *Border Alignment* to *Top Right* and *Menu Direction* to *Horizontal* for the `SoBorderMenu`.

![Label in SoRenderArea](/images/tutorials/visualization/pathtracer/Example1_13.png "Label in SoRenderArea")

Finally, group your Path Tracer modules to another group named *Path Tracing*.

![New Group for Path Tracing](/images/tutorials/visualization/pathtracer/Example1_14.png "New Group for Path Tracing")

![Side by Side](/images/tutorials/visualization/pathtracer/Example1_15.png "Side by Side")

### Share the same camera
In the end, we want to have the same camera perspective in both viewers so that we see the differences. Add a `SoPerspectiveCamera` module to your workspace and connect it to the volume rendering and the Path Tracer network. The Path Tracer network additionally needs a SoGroup, see below for connection details. You have to toggle *detectCamera* in both of your `SoCameraInteraction` modules in order to synchronize the view for both `SoRenderArea` viewers.

![Camera Synchronization](/images/tutorials/visualization/pathtracer/Example1_16.png "Camera Synchronization")

{{<alert class="info" caption="Additional Info">}}
Path Tracing requires a lot of iterations through the image before reaching the best possible result. You can see the maximum number of iterations defined and the current iteration in the `SoPathTracer` panel. The more iterations, the better the result but the more time it takes to finalize your image.
{{</alert>}}

{{< imagegallery 3 "/images/tutorials/visualization/pathtracer" "PathTracer_1_Iteration" "PathTracer_100_Iterations" "PathTracer_1000_Iterations" >}}

## Results
Path Tracing provides a much more realistic way to visualize the behavior of light in a scene. It simulates the the scattering and absorption of light within the volume. 

## Exercises
1. Play around with different `SoPathTracerMaterial` settings and define
2. Change the maximum number of iterations in `SoPathTracer` module
3. Change the configurations in `SoPathTracerAreaLight` module

## Summary
* Path Tracer modules can be used the same way as Open Inventor modules
* A `SoPerspectiveCamera` can be used for multiple viewers to synchronize camera position
* Path Tracing produces beautiful, photorealistic renderings, but can be computationally expensive

{{< networkfile "examples/visualization/example6/pathtracer1.mlab" >}}
