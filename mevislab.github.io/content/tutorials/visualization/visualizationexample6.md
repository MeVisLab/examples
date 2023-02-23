---
title: "Example 6: MeVis Path Tracer"
date: "2023-02-23"
status: "OK"
draft: false
tags: ["Advanced", "Tutorial", "Visualization", "3D", "Volume Rendering", "Path Tracer"]
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

{{< imagegallery 5 "/images/tutorials/visualization/pathtracer" "PathTracer1" "PathTracer2" "PathTracer3" "PathTracer4" "PathTracer5" >}}

The `SoPathTracer` module implements the main renderer (like the `SoGVRVolumeRenderer`). It collects all `SoPathTracer*` extensions (on its left side) in the scene and renders them. Picking is also supported, but currently only the first hit position. It supports an arbitrary number of objects with different orientation and bounding boxes.

## Path Tracing
Path Tracing allows interactive, photorealistic 3D environments with dynamic light and shadow, reflections and refractions.

Traditional volume rendering is a technique used to visualize 3D volumetric data by rendering 2D images of the data from different viewpoints. It typically uses a transfer function that maps the scalar values of the volume to colors and opacities, which are then used to create a 2D image of the volume. This technique can produce visually pleasing images of volumetric data, but it can struggle with complex lighting and shadow effects, and it may not accurately capture the scattering and absorption of light within the volume.

Monte Carlo path tracing is a technique used to simulate the behavior of light in a scene by tracing rays of light as they bounce around the scene and interact with objects. It uses statistical methods to simulate the behavior of light, making it more accurate than traditional volume rendering for simulating the scattering and absorption of light within the volume. However, path tracing can be computationally expensive, as it requires many iterations to produce a high-quality image.

[Ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) is a technique for modeling light transport. It follows all light rays throughout the entire scene. Depending on the scene this takes a lot of time to fully compute the resulting pixels. Other than ray tracing, path tracing only traces the most likely path of the light by using the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method). Computation is much faster but the results are comparable.

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
  * The mask volume can be used by any volume or instance
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
  * ISO surface is rendered on-the-fly
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

The following examples shall help you to learn how to use the modules.
