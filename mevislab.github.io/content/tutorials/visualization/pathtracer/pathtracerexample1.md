---
title: "Example 6.1: Loading a SoPathTracerVolume"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Visualization", "3D", "Volume Rendering", "Path Tracer"]
menu: 
  main:
    identifier: "pathtracer_example1"
    title: "Example usage of the MeVis Path Tracer SoPathTracerVolume module"
    weight: 575
    parent: "visualization_example6"
---
# Example 6.1: Loading a SoPathTracerVolume

## Introduction
In this example we are having a closer look at the example network of the `SoPathTracer` module. This network uses the `SoPathTracerVolume` module to render a dataset downloaded from our website.

{{<alert class="info" caption="Extra Infos">}}
The engine dataset is a downscaled version of a 1024x1024 CT scan.<br/>
<b>The dataset was provided by:</b><br/>
Varex Industrial CT Services & Engineering<br/>
425 Barclay Boulevard<br/>
Lincolnshire, Illinois 60069<br/>

Industrial.CTServices@vareximaging.com
{{</alert>}}

## Steps to do
Add the `SoPathTracer` module to your workspace and open the example network via right mouse button {{< mousebutton "right" >}} {{< menuitem "Help" "Show Example Network">}}.

![SoPathTracer Example Network](/images/tutorials/visualization/pathtracer/Example1_1.png "SoPathTracer Example Network")

The `SoExaminerViewer` is empty. You need to load the dataset first. Click *LoadDataFromWeb* and inspect the viewer module. A 3-dimensional engine is shown.

![3D engine with SoPathTracer](/images/tutorials/visualization/pathtracer/Example1_2.png "3D engine with SoPathTracer")

Opening the same file in a `SoGVRVolumeRenderer` looks completely different.

![3D engine with SoGVRVolumeRenderer](/images/tutorials/visualization/pathtracer/Example1_SoGVRVolumeRenderer.png "3D engine with SoGVRVolumeRenderer")

Open the panel of the `SoPathTracer`. You have lots of different settings for your rendering. We will try to explain some of them so that you understand what's the difference.

![SoPathTracer](/images/tutorials/visualization/pathtracer/Example1_3.png "SoPathTracer")

### Render Mode
The most important field for MeVis Path Tracer is the render mode. 
