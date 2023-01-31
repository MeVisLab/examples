---
title: "Example 6: MeVis Path Tracer"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Visualization", "3D", "Volume Rendering", "Path Tracer"]
menu: 
  main:
    identifier: "visualization_example6"
    title: "Example usage of the MeVis Path Tracer"
    weight: 575
    parent: "visualization"
---
# Example 6: MeVis Path Tracer

## Introduction
The MeVis Path Tracer offers a Monte Carlo Path Tracing framework running on CUDA GPUs. It offers photorealistic rendering of volumes and meshes, physically based lightning with area lights and soft shadows and fully integrates into MeVisLab Open Inventor (camera, depth buffer, clipping planes, etc.).

{{<alert class="info" caption="Extra Infos">}}
CUDA is a parallel computing platform and programming model created by NVIDIA. For further information, see [NVIDIA website](https://blogs.nvidia.com/blog/2012/09/10/what-is-cuda-2/).
{{</alert>}}

The `SoPathTracer` module implements the main renderer (like the `SoGVRVolumeRenderer`). It collects all `SoPathTracer*` extensions (on its left side) in the scene and renders them. Picking is also supported, but currently only the first hit position. It supports an arbitrary number of objects with different orientation and bounding boxes.

## Path Tracing
Path Tracing allows interactive, photorealistic 3D environments with dynamic light and shadow, reflections and refractions.

In the beginning, 3D images have been generated as seen from a single viewpoint. A mapping has been done from scene geometry in 3D to a pixel on the screen. The color of each pixel on screen has been assigned by a pixel shader. A pixel shader is able to take into account physical effects such as light position. Computation is very fast but the results do not include effects such as shadows, illumination and indirect lightning.

Todays rendering is based on tracing light paths. Objects in a 3D scene contribute illumination to every other object. The illumination can be emitted from a light source or reflected by a surface. Illumination coming from surfaces must scatter in a particular direction that is some function of the incoming direction of the arriving illumination, and the outgoing direction being sampled ([Wikipedia - Path Tracing](https://en.wikipedia.org/wiki/Path_tracing)).

{{<alert class="info" caption="Extra Infos">}}
For more information about Path Tracing, see the [NVIDIA website](https://blogs.nvidia.com/blog/2022/03/23/what-is-path-tracing/).
{{</alert>}}

## Modules
The [SoPathTracer](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracer.html#SoPathTracer) is the main renderer of the framework and should always appear on the right in your scene. It collects the current Open Inventor camera and clipping planes and uses them when rendering.

There are various extensions that can be used.
### Volumes
* [SoPathTracerVolume](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerVolume.html#SoPathTracerVolume) loads and renders a volume, multiple volumes with arbitrary world coordinates are supported
  * Volumes support:
    * Diffuse/emissive/material LUT
    * Shading options
    * Subvolume mixing
    * Additional transformation matrix
    * Material selection

* [SoPathTracerMaskVolume](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerMaskVolume.html#SoPathTracerMaskVolume) can be used to mask voxels in [SoPathTracerVolume](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerVolume.html#SoPathTracerVolume) volumes
  * Allows to load a 8bit mask volume
  * THe mask volume can be used by any volume or instance
  * It allows to:
    * Change the alpha and color of inside/outside voxels
    * Change the tag value (see `SoPathTracerVolume`)
  * Very useful in combination with `SoVolumeCutting`
* [SoPathTracerTagVolume](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerTagVolume.html#SoPathTracerTagVolume) can be used to tag voxels in [SoPathTracerVolume](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerVolume.html#SoPathTracerVolume) volumes
  * Allows to load a 8bit tag volume
  * The tags are used to select a per-object LUT and/or material
  * A 2D LUT can be provided using `LUTConcat` or `SoLUTEditor2D`
  * Per-tag materials can be provided by adding multiple materials to the *inMaterial* scene
  * Useful to render segmented objects
* [SoPathTracerVolumeInstance](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerVolumeInstance.html#SoPathTracerVolumeInstance) can be used to render a [SoPathTracerVolume](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerVolume.html#SoPathTracerVolume) with differnt transformation, subvolume, LUT, material, ...
  * Allows to instantiate an existing volume
  * Supports all options of a normal volume, but only references the volume itself
  * This allows to:
    * Use a different LUT
    * Change shading options
    * Change subvolume
    * Change transformation matrix
    * Different material selection
* [SoPathTracerSlice](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerSlice.html#SoPathTracerSlice) renders a slice at the given plane, showing the volume data of the given volume
  * Allows to render a cut slice through a volume
  * Allows to set an arbitrary plane and works on volumes and instances
  * Has its own LUT and can be opaque or transparent
* [SoPathTracerIsoSurface](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerIsoSurface.html#SoPathTracerIsoSurface) renders an iso surface (with first hit refinement) on the given base volume
  * Allows to render an ISO surface of a volume
  * Works on volumes and instances
  * Supports opaque and transparent surfaces
  ISO surface is rendered on-the-fly
  * Hit refinement is used to provide high-quality surfaces
  * Arbitrary material can be specified

### Geometry
* [SoPathTracerMesh](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerMesh.html#SoPathTracerMesh) scans the input scene for triangle meshes and ray traces them
  * Allows to render arbitrary triangle meshes
  * Scans the input scene for triangle meshes and converts them to a bounding volume hierarchy (BVH)
  * Supports different materials by adding `SoPathTracerMaterials`
  * Objects can be turned on/off via material nodes (without BVH rebuilding)
  * Supports opaque and transparent meshes
* [SoPathTracerLines](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerLines.html#SoPathTracerLines) scans the input scene for line sets and ray traces them as cylinders with round caps
  * Allows to render thick lines (capsules)
  * Scans the input scene for `SoLineSet`/`SoIndexedLineSet` and converts them to a BVH
  * Different materials are supported by adding `SoPathTracerMaterial` nodes
  * Supports opaque and transparent lines
  * Useful to render fibers or stream lines
* [SoPathTracerSpheres](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerSpheres.html#SoPathTracerSpheres) renders a marker list as ray traced spheres
  * Allows to render markers as spheres
  * Converts marker list to spheres and creates a BVH
  * Currently only supports single material

### Lights
* [SoPathTracerAreaLight](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerAreaLight.html#SoPathTracerAreaLight) provides a realistic area light with attenuation, area and distance
  * Provides an area light
  * Multiple area lights are supported
  * Lights can be placed:
    * Around the scene bounding box using polar coordinates
    * At absolute camera or world position (as head or local light)
  * Light intensity is automatically adapted to the scene size
  * Otherwise it would be hard to select an intensity that works on different scales
* [SoPathTracerBackgroundLight](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerBackgroundLight.html#SoPathTracerBackgroundLight) provides a background light, using image based lighting from a sphere or cube map
  * Provides environmental lighting
  * It supports:
    * Specifying environment light colors
    * Image based lighting using a cube map or sphere map
  * Only one background light can be added to a scene

### Material
* [SoPathTracerMaterial](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/SoPathTracerMaterial.html#SoPathTracerMaterial) allows to specify which material should be used for a given object.
  * Provides material settings for other nodes
  * Offers to select the used material and its parameters
  * Is connected to the *inMaterial* of other nodes
  * Multiple materials may be placed into the input scene of `SoPathTracerMesh` and `SoPathTracerLines`
  * Allows to override volume shader settings as well

The following examples shall help you to learn how to use them.

## Example images
![MeVis Path Tracer Image 1](/images/tutorials/visualization/pathtracer/heartMasked.jpg "MeVis Path Tracer Image 1")
![MeVis Path Tracer Image 2](/images/tutorials/visualization/pathtracer/heartMaskedDof.jpg "MeVis Path Tracer Image 2")
![MeVis Path Tracer Image 3](/images/tutorials/visualization/pathtracer/head5.jpg "MeVis Path Tracer Image 3")
![MeVis Path Tracer Image 4](/images/tutorials/visualization/pathtracer/liver1.jpg "MeVis Path Tracer Image 4")
![MeVis Path Tracer Image 5](/images/tutorials/visualization/pathtracer/liverclip.jpg "MeVis Path Tracer Image 5")
![MeVis Path Tracer Image 6](/images/tutorials/visualization/pathtracer/motor5.jpg "MeVis Path Tracer Image 6")
![MeVis Path Tracer Image 7](/images/tutorials/visualization/pathtracer/motorCloseup4.jpg "MeVis Path Tracer Image 7")
![MeVis Path Tracer Image 8](/images/tutorials/visualization/pathtracer/stagClip1.jpg "MeVis Path Tracer Image 8")
![MeVis Path Tracer Image 9](/images/tutorials/visualization/pathtracer/stagPlane1.jpg "MeVis Path Tracer Image 9")
![MeVis Path Tracer Image 10](/images/tutorials/visualization/pathtracer/tensorLines.jpg "MeVis Path Tracer Image 10")

