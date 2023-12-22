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
# Example 6.2: Visualization using Path Tracer

## Introduction
In this tutorial, we will explain the basics of using the `SoPathTracer` module in MeVisLab. You will learn how to create a scene, assign materials, add light sources, and configure the PathTracer to generate renderings.

## Steps to do
### Develop your network

Begin by loading the example [medical images](/examples/visualization/example6/Volume_1.mlimage) using the `LocalImage` module. Connect it to a `View2D` to visually inspect its contents.

![MR Image of Knee](/images/tutorials/visualization/pathtracer/V6.2_1.png "MR Image of Knee")


Connect your `LocalImage` to the `SoPathTracerVolume` module to initiate volume rendering. Add the `SoPathTracer` module into your SDK and connect both to the `SoExaminerViewer` module to visualize the rendered volume. the `SoPathTracer` module serves as the main rendering component. It offers parameters for resulotion, camera settings, background colors and iteration control.

{{<alert class="info" caption="Additional Info">}}
It's essential to consistently position the `SoPathTracer `module on the right side of the scene. This strategic placement ensures that the module can render all objects located in the scene before it accurately. 
{{</alert>}}

![SoPathTracerVolume & SoPathTracer](/images/tutorials/visualization/pathtracer/V6.2_2.png "SoPathTracerVolume & SoPathTracer")

If you check your `SoExaminerViewer` you will see a black box, this indicates often a need for additional adjustments to color, light and transparency.

![SoExaminerViewer](/images/tutorials/visualization/pathtracer/V6.2_3.png "SoExaminerViewer")

To brighten up your scene, connect both the `SoPathTracerAreaLight` and `SoPathTracerBackgroundLight` modules to your `SoExaminerViewer` to improve scene lighting. 

The `SoPathTracerAreaLight` shapes and colors specific areas realistically, while `SoPathTracerBackgroundLight` illuminates the whole scene with your chosen three colors. These lights make your scene vibrant, providing a solid base for further adjustments with other modules.

![Lights](/images/tutorials/visualization/pathtracer/V6.2_4.png "Lights")

Connect `SoLUTEditor` to your `SoPathTracerVolume` to visualize the knee. However, it might initially appear in black and with shading.

![SoLUTEditor](/images/tutorials/visualization/pathtracer/V6.2_5_SoLUTEditor.png "SoLUTEditor")


To easily identify your minimum and maximum range, connect the `MinMaxScan` module to your `LocalImage`. Open it's panel and read your *Static Min Value* and *Static Max Value*. This step allows you to set the appropriate values with convenience.

![MinMaxScan](/images/tutorials/visualization/pathtracer/V6_MinMaxScan.png "MinMaxScan")

Then open the panel of the `SoLUTEditor` and select tab *Range*. Define *New Range Min* as *0* and *New Range Max* as *2047*. Once done, manually define your desired colors for your LUT in the *Editor* tab.

{{<alert class="info" caption="Additional Info">}}
You can replace `SoLUTEditor` with `LUTLoad` and load the attached xml files to store the same adjustments.
{{</alert>}}

![LUT](/images/tutorials/visualization/pathtracer/V6.2_LUTandSoExaminerViewer.png "LUT")

Now, let's enhance your rendering further by using the `SoPathTracerMaterial` module. This module provides essential material properties for geometry and volumes within the `SoPathTracer` scene. Open it’s panel and navigate to the tab *Surface Brdf*. Change the *Diffuse* color for altering the visual appearance of surfaces. The *Diffuse* color determines how light interacts with the surface, influencing its overall color and brightness.

![SoPathTracerMaterial](/images/tutorials/visualization/pathtracer/V6.2_8.png "SoPathTracerMaterial")

## Visualize Bones

Follow the same steps for this scenario. Load this [Bones mask](/examples/visualization/example6/edited_Bones.mlimage) and examine it using `View2D`.  

![Bones](/images/tutorials/visualization/pathtracer/V6.2_9.png "Bones")

Start by refining the transparency of the cartilage structures using the `SoLUTEditor` to improve visibility and achieve a clearer depiction of the bones. Open it’s panel in the *Editor* tab, choose your *Index* number *3* and reduce the *Opacity* to *0*. 

Alternatively, you can disable the toggle of the `SoPathTracerVolume` to make all structures disappear.


![Bones](/images/tutorials/visualization/pathtracer/V6.2_10.png "Bones")

Open the panel of `SoLUTEditor1` for the bones and make the following adjustments. Go to tab *Range* and set *New Range Min* to *0* and *New Range Max* to *127*.

![SoLUTEditor1](/images/tutorials/visualization/pathtracer/V6.2_11_LUT_Bones.png "SoLUTEditor1")

You can increase the *Shininess* of the bones and change the *Diffuse* color in the *Surface Brdf* tab within the `SoPathTracerMaterial1`.

![SoPathTracerMaterial1](/images/tutorials/visualization/pathtracer/V6.2_SoPathTracerMaterial.png "SoPathTracerMaterial1")

Enable the toggle of the `SoPathTracerVolume` to view both bones and structers. 

![Result](/images/tutorials/visualization/pathtracer/V6.2_BonesResult.png "Result")

## Visualize Vessels

Repeat the process for the vessels. Load this [Vessels mask](/examples/visualization/example6/edited_Vessels.mlimage) and check it using `View2D`.

![Vessels](/images/tutorials/visualization/pathtracer/V6.2_13.png "Vessels")

Access the `SoLUTEditor2` panel for the vessels and modify the color settings within the *Editor* tab. Additionally, in the *Range tab*, set the *New Range Min* to *0* and the *New Range Max* to *255*.

![SoLUTEditor2](/images/tutorials/visualization/pathtracer/V6.2_SoLUTEditor1_Vessels.png "SoLUTEditor2")

![Final Result](/images/tutorials/visualization/pathtracer/V6.2_Final_Result.png "Final Result")

## Summary:
*	You can achieve impressive renderings using SoPathTracer and associated modules.
* Render volumes efficiently in `SoPathTracer` scenes with `SoPathTracerVolume`, enabling diverse rendering options, LUT adjustments, and material enhancements.
* Enhance your scene's look by adjusting materials and colors interactively using `SoPathTracerMaterial` and `SoLUTEditor`.
* Use lighting modules such as `SoPathTracerAreaLight` and `SoPathTracerBackgroundLight` to optimize the illumination of your rendered scenes.

{{< networkfile "examples/visualization/example6/pathtracer2.mlab" >}}

[Bones mask](/examples/visualization/example6/LUT_Knee.xml)
[Bones mask](/examples/visualization/example6/LUT_Bones.xml)
[Bones mask](/examples/visualization/example6/LUT_Vessels.xml)