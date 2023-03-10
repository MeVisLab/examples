---
title: "Example 6.2: Capture a video using the Path Tracer"
date: "2023-02-23"
status: "open"
draft: false
tags: ["Advanced", "Tutorial", "Visualization", "3D", "Volume Rendering", "Path Tracer", "Video Capturing"]
menu: 
  main:
    identifier: "pathtracer_example2"
    title: "Capture a video using the Path Tracer."
    weight: 580
    parent: "visualization_example6"
---
# Example 6.2: Capture a video using the Path Tracer

## Introduction
The MeVis Path Tracer allows you to create photorealistic renderings. In this example we will use the `AnimationRecorder` module to create a video from camera movements inside the `SoRenderArea` module.

## Steps to do
Add an `ImageLoad` module to your workspace and connect in to a `SoPathTracerVolume`. Add a `PathTracer`, a `SoRenderArea`, a `SoCameraInteraction` and a `SoSeparator` module to your workspace and connect them as seen below. Load the file 

Add a `SoLUTEditor` and a `LUTConcat` module and connect them to the `SoPathTracerVolume`.