---
title: "Example 6.1: Visualization using Path Tracer"
date: "2023-12-21"
status: "open"
draft: false
weight: 579
tags: ["Advanced", "Tutorial", "Visualization", "3D", "Path Tracer"]
menu: 
  main:
    identifier: "pathtracer_example2"
    title: "Comparison between Volume Rendering and MeVisLab Path Tracer"
    weight: 579
    parent: "visualization_example6"
---
# Example 6.2: Visualization using SoPathTracer

## Introduction
In this tutorial, we will explain the basics of using the `SoPathTracer` module in MeVisLab. You will learn how to create a scene, assign materials, add light sources, and configure the PathTracer to generate enhanced renderings.

{{<alert class="warning" caption="Attention">}}
The MeVis Path Tracer requires an NVIDIA graphics card with CUDA support. In order to check your hardware, open MeVisLab and add a `SoPathTracer` module to your workspace. You will see a message if your hardware does not support CUDA:

*MeVisLab detected an Intel onboard graphics adapter. If you experience rendering problems, try setting the environment variables SOVIEW2D_NO_SHADERS and GVR_NO_GLSL.* <br />
*Handling cudaGetDeviceCount returned 35 (CUDA driver version is insufficient for CUDA runtime version)*
{{</alert>}}

## Steps to do
### Develop your network
Download and open the [images](/examples/visualization/example6/Volume_1.mlimage) by using a `LocalImage` module. Connect it to a `View2D` to visually inspect its contents.

![MR Image of Knee](/images/tutorials/visualization/pathtracer/V6.2_1.png "MR Image of Knee in 2D")

Replace the `View2D` module by a `SoExaminerViewer`. Add the modules `SoPathTracerVolume` and `SoPathTracer` to your workspace and connect them as seen below. 

The `SoPathTracerVolume` enables the loading and transforming the data into renderable volumes for Path Tracing. The `SoPathTracer` is the main rendering module of the MeVis Path Tracer framework. It provides a much more realistic way to visualize the behavior of light in a scene. It simulates the scattering and absorption of light within the volume.

{{<alert class="info" caption="Additional Info">}}
It's essential to consistently position the `SoPathTracer `module on the right side of the scene. This strategic placement ensures that the module can render all objects located in the scene before it accurately. 
{{</alert>}}

![SoPathTracerVolume & SoPathTracer](/images/tutorials/visualization/pathtracer/V6.2_2.png "SoPathTracerVolume & SoPathTracer")

If you check your `SoExaminerViewer` you will see a black box. We need to define a LUT for the grey values first.

![SoExaminerViewer](/images/tutorials/visualization/pathtracer/V6.2_3.png "SoExaminerViewer")

Now connect the `SoLUTEditor` module to your `SoPathTracerVolume` as illustrated down bellow and you will be able to see the knee. 

![SoLUTEditor](/images/tutorials/visualization/pathtracer/SoLUTEditor1.png "SoLUTEditor")

Add a `MinMaxScan` module to the `LocalImage` module and open the panel. The module shows the minimal and maximal grey values of the volume.

Open the panel of the `SoLUTEditor` module and define Range between *0* and *2047* as calculated by the `MinMaxScan`.

![SoLUTEditor](/images/tutorials/visualization/pathtracer/Range_MinMaxScan.png "MinMaxScan")

Next, add lights to your scene. Connect a `SoPathTracerAreaLight` and a `SoPathTracerBackgroundLight` module to your `SoExaminerViewer` to improve scene lighting. 

The `SoPathTracerAreaLight` module provides a physically based area light that illuminates the scene of a `SoPathTracer`. The lights can be rectangular or discs and have an area, color and intensity. They can be positioned with spherical coordinates around the bounding box of the renderer, or they can be position in world or camera space.

The `SoPathTracerBackgroundLight` module provides a background light for the `SoPathTracer`. It supports setting a top, middle and bottom color or alternatively it support image based lighting (IBL) using a sphere or cube map. Only one background light can be active for a given `SoPathTracer`.

![Lights](/images/tutorials/visualization/pathtracer/Lights2.png "Lights")

Open the panel of the `SoPathTracerBackgroundLight` module and choose your three colors.

![SoPathTracerBackgroundLight](/images/tutorials/visualization/pathtracer/BackgroundLight.png "SoPathTracerBackgroundLight")

#### Manually define LUT
Either define your desired colors for your LUT in the *Editor* tab manually as shown down below.

![LUT](/images/tutorials/visualization/pathtracer/V6.2_LUTandSoExaminerViewer.png "LUT")

#### Load example LUT from file
As an alternative, you can replace the `SoLUTEditor` with a `LUTLoad` and load this [XML file](/examples/visualization/example6/LUT_Original.xml) to use a pre-defined LUT.

![LUTLoad](/images/tutorials/visualization/pathtracer/LUTLoad.png "LUTLoad")

Now, let's enhance your rendering further by using the `SoPathTracerMaterial` module. This module provides essential material properties for geometry and volumes within the `SoPathTracer` scene.

Add a `SoPathTracerMaterial` module to your `SoPathTracerVolume`. Open it’s panel and navigate to the tab *Surface Brdf*. Change the *Diffuse* color for altering the visual appearance of surfaces. The *Diffuse* color determines how light interacts with the surface, influencing its overall color and brightness. Set *Specular* to *0.5*, *Shininess* to *1.0* and *Specular Intensity* to *0.5*.

![SoPathTracerMaterial](/images/tutorials/visualization/pathtracer/SoPathTracerMaterial_Knee.png "SoPathTracerMaterial")

{{<alert class="info" caption="Additional Info">}}
The resulting rendering in `SoExaminerViewer` might look different, depending on your defined LUT.
{{</alert>}}

## Visualize Bones
If you want to visualize multiple volumes at the same time, you need to add another `SoPathTracerVolume` and `LocalImage` for loading the mask to the `SoExaminerViewer`.

As the LUT of the second volume also differs, add another `SoLUTEditor` module or `LUTLoad` module to the new `SoPathTracerVolume`.

For later usage, you can also already add a `SoPathTracerMaterial` module to the `SoPathTracerVolume` module.

Load the [Bones mask](/examples/visualization/example6/edited_Bones.mlimage) by using the new `LocalImage` module and preview it in a `View2D`.

![Bones mask](/images/tutorials/visualization/pathtracer/View2D_Bones.png "Bones mask")

Start by disabling the visibility of your first volume by toggeling `SoPathTracerVolume` *Enabled* field to off. This helps improve the rendering of the bones itself and makes it easier to define colors for your LUT.

#### Load example LUT from file
Once again, you can decide to define the LUT yourself in `SoLUTEditor` module, or load a prepared XML File in a `LUTLoad` module as provided [here](/examples/visualization/example6/LUT_Bones.xml).

#### Manually define LUT
If you want to define your own LUT, connect a `MinMaxScan` module to your `LocalImage1` and define Range for the `SoLUTEditor` as already done before. 

![MinMaxScan of Bones mask](/images/tutorials/visualization/pathtracer/MinMaxScan_Bones.png "MinMaxScan of Bones mask")

Open the panel of `SoLUTEditor1` for the bones and go to tab *Range* and set *New Range Min* to *0* and *New Range Max* to *127*. Define the following colors in tab *Editor*. 

![SoLUTEditor1](/images/tutorials/visualization/pathtracer/V6.2_11_LUT_Bones.png "SoLUTEditor1")

You can increase the *Shininess* of the bones and change the *Diffuse* color in the *Surface Brdf* tab within the `SoPathTracerMaterial1`. Also set *Specular* to *0.5*, *Shininess* to *0.904* and *Specular Intensity* to *0.466*.

![SoPathTracerMaterial1](/images/tutorials/visualization/pathtracer/V6.2_SoPathTracerMaterial.png "SoPathTracerMaterial1")

## Visualize Vessels
Repeat the process for the vessels. Add another `LocalImage`, `SoPathTracerVolume`, `SoLUTEditor` (or `LUTLoad`) and `View2D` module as seen below. Load this [Vessels mask](/examples/visualization/example6/edited_Vessels.mlimage) and check it using `View2D`.

![Vessels mask](/images/tutorials/visualization/pathtracer/View2D_Vessels.png "Vessels mask")

#### Load example LUT from file
Load a prepared XML File in a `LUTLoad` module as provided [here](/examples/visualization/example6/LUT_Vessels.xml)

#### Manually define LUT
Connect the `MinMaxScan` to your `LocalImage2`.

Access the `SoLUTEditor2` panel in the tab *Range* and set the *New Range Min* to *0* and the *New Range Max* to *255*. Additionally, modify the illustrated color settings within the *Editor* tab. 

![Vessels](/images/tutorials/visualization/pathtracer/MinMaxScan_Vessels.png "MinMaxScan of Vessels mask")

![SoLUTEditor2](/images/tutorials/visualization/pathtracer/V6.2_SoLUTEditor1_Vessels.png "SoLUTEditor2")

Now you should set your first volume visible again by toggeling `SoPathTracerVolume` *Enabled* field to on.

![Final Resul](/images/tutorials/visualization/pathtracer/FinalResult.png "Final Result")

{{<alert class="info" caption="Additional Info">}}
The resulting rendering in `SoExaminerViewer` might look different, depending on your defined LUTs.
{{</alert>}}

![Final Resul](/images/tutorials/visualization/pathtracer/FinalResult2.png "Final Result with Enhanced Visualization")

## Summary:
*	You can achieve photorealistic renderings using `SoPathTracer` and associated modules.
* Render volumes efficiently in `SoPathTracer` scenes with `SoPathTracerVolume`, enabling diverse rendering options, LUT adjustments, lights and material enhancements.
* Enhance your scene's look by adjusting materials and colors interactively using `SoPathTracerMaterial` and `SoLUTEditor`.
* Use lighting modules such as `SoPathTracerAreaLight` and `SoPathTracerBackgroundLight` to optimize the illumination of your rendered scenes.

{{< networkfile "examples/visualization/example6/PathTracer2.mlab" >}}
