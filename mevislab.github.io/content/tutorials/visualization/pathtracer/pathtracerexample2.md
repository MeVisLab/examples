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

## Steps to do
### Develop your network

Begin by loading the example [medical images](/examples/visualization/example6/Volume_1.mlimage) using the `LocalImage` module. Connect it to a `View2D` to visually inspect its contents.

![MR Image of Knee](/images/tutorials/visualization/pathtracer/V6.2_1.png "MR Image of Knee in 2D")


Replace the `View2D` module by a `SoExaminerViewer`. Add the modules `SoPathTracerVolume` and `SoPathTracer` to your workspace and connect them as seen below. 

The `SoPathTracerVolume` enables the loading and transforming the data into renderable volumes for Path Tracing. The `SoPathTracer` module simulates natural lighting in the digital images, enhancing the realism of our renderings by accurately calculating illumination levels throughout the entire scene.

{{<alert class="info" caption="Additional Info">}}
It's essential to consistently position the `SoPathTracer `module on the right side of the scene. This strategic placement ensures that the module can render all objects located in the scene before it accurately. 
{{</alert>}}

![SoPathTracerVolume & SoPathTracer](/images/tutorials/visualization/pathtracer/V6.2_2.png "SoPathTracerVolume & SoPathTracer")

If you check your `SoExaminerViewer` you will see a black box. this indicates often a need for adjustments to define transparencies and colors of the volume with a LUT. 

![SoExaminerViewer](/images/tutorials/visualization/pathtracer/V6.2_3.png "SoExaminerViewer")

First, brighten up your scene to ensure visibility of your defined LUTs. Connect both the `SoPathTracerAreaLight` and `SoPathTracerBackgroundLight` modules to your `SoExaminerViewer` to improve scene lighting. 

The `SoPathTracerAreaLight` shapes and colors specific areas realistically, while `SoPathTracerBackgroundLight` illuminates the whole scene with your chosen three colors. These lights make your scene vibrant, providing a solid base for further adjustments with other modules like `SoLUTEditor`.

![Lights](/images/tutorials/visualization/pathtracer/V6.2_4.png "Lights")

Now connect the `SoLUTEditor` module to your `SoPathTracerVolume` as illustrated down bellow and you will be able to see the knee. 

![SoLUTEditor](/images/tutorials/visualization/pathtracer/V6_InitialView.png "SoLUTEditor")


To easily identify your min and max range, connect the `MinMaxScan` module to your `LocalImage`. Open it's panel and read the *Static Min Value* and *Static Max Value* of the loaded image. This step allows you to set the appropriate values with convenience.

![MinMaxScan](/images/tutorials/visualization/pathtracer/MinMaxScan1.png "MinMaxScan of Knee")

Then open the panel of the `SoLUTEditor` and select tab *Range*. Define *New Range Min* as *0* and *New Range Max* as *2047*. Once done, manually define your desired colors for your LUT in the *Editor* tab.

{{<alert class="info" caption="Additional Info">}}
You can replace the `SoLUTEditor` with a `LUTLoad` and load this [Knee XML](/examples/visualization/example6/LUT_Knee.xml) to store the same adjustments.
{{</alert>}}

![LUT](/images/tutorials/visualization/pathtracer/V6.2_LUTandSoExaminerViewer.png "LUT")

Now, let's enhance your rendering further by using the `SoPathTracerMaterial` module. This module provides essential material properties for geometry and volumes within the `SoPathTracer` scene. Open it’s panel and navigate to the tab *Surface Brdf*. Change the *Diffuse* color for altering the visual appearance of surfaces. The *Diffuse* color determines how light interacts with the surface, influencing its overall color and brightness.

![SoPathTracerMaterial](/images/tutorials/visualization/pathtracer/SoPathTracerMaterial_Knee.png "SoPathTracerMaterial")

## Visualize Bones

Follow the same steps for this scenario. Load this [Bones mask](/examples/visualization/example6/edited_Bones.mlimage) and examine it using `View2D`.  

![Bones mask](/images/tutorials/visualization/pathtracer/View2D_Bones.png "Bones mask")

Start by disabling the toggle of the `SoPathTracerVolume` to temporarily hide the the knee structures. This helps improve the visibility of the bones and makes it easier to define colors for your LUT.


Connect the `MinMaxScan` module to your `LocalImage1` and read you range. 

![MinMaxScan of Bones mask](/images/tutorials/visualization/pathtracer/MinMaxScan_Bones.png "MinMaxScan of Bones mask")

Open the panel of `SoLUTEditor1` for the bones and go to tab *Range* and set *New Range Min* to *0* and *New Range Max* to *127*. Define the following colors in tab *Editor* or load this [Bones XML](/examples/visualization/example6/LUT_Bones.xml) . 

![SoLUTEditor1](/images/tutorials/visualization/pathtracer/V6.2_11_LUT_Bones.png "SoLUTEditor1")

You can increase the *Shininess* of the bones and change the *Diffuse* color in the *Surface Brdf* tab within the `SoPathTracerMaterial1`.

![SoPathTracerMaterial1](/images/tutorials/visualization/pathtracer/V6.2_SoPathTracerMaterial.png "SoPathTracerMaterial1")

## Visualize Vessels

Repeat the process for the vessels. Load this [Vessels mask](/examples/visualization/example6/edited_Vessels.mlimage) and check it using `View2D`.

![Vessels mask](/images/tutorials/visualization/pathtracer/View2D_Vessels.png "Vessels mask")

Connect the `MinMaxScan` to your `LocalImage2`.

![Vessels](/images/tutorials/visualization/pathtracer/MinMaxScan_Vessels.png "MinMaxScan of Vessels mask")

Access the `SoLUTEditor2` panel in the tab *Range* and set the *New Range Min* to *0* and the *New Range Max* to *255*. Additionally, modify the illustrated color settings within the *Editor* tab. 

![SoLUTEditor2](/images/tutorials/visualization/pathtracer/V6.2_SoLUTEditor1_Vessels.png "SoLUTEditor2")

![Final Resul](/images/tutorials/visualization/pathtracer/FinalResult.png "Final Result")

You can refine the transparency of the knee cartilage structures in the `SoLUTEditor` to achieve a clearer depiction of the bones and the vessels. Open it’s panel in the *Editor* tab, choose *Index* number *3* and reduce the *Opacity* to *0*. 

![Final Resul](/images/tutorials/visualization/pathtracer/FinalResult2.png "Final Result with Enhanced Visualization")

## Summary:
*	You can achieve impressive renderings using SoPathTracer and associated modules.
* Render volumes efficiently in `SoPathTracer` scenes with `SoPathTracerVolume`, enabling diverse rendering options, LUT adjustments, and material enhancements.
* Enhance your scene's look by adjusting materials and colors interactively using `SoPathTracerMaterial` and `SoLUTEditor`.
* Use lighting modules such as `SoPathTracerAreaLight` and `SoPathTracerBackgroundLight` to optimize the illumination of your rendered scenes.

{{< networkfile "examples/visualization/example6/PathTracer2.mlab" >}}
