---
title: "Example 4: Post Effects in Open Inventor"
date: 2024-05-03T10:52:33+02:00
draft: false
weight: 540
status: "OK"
tags: ["Advanced", "Tutorial", "Open Inventor", "Post Effects"]
menu: 
  main:
    identifier: "posteffectsinopeninventor"
    title: "Learn how to use Post Effects in Open Inventor"
    weight: 540
    parent: "openinventor"
---
# Example 4: Post Effects in Open Inventor
## Introduction
Up to this point, we practiced constructing Open Inventor scenes and placed three-dimensional Open Inventor objects of different colors and shapes within them.

In this tutorial, we will go over the steps to add shadows to our 3D objects, make them glow, and vary their opacity to make them transparent. We will also incorporate WEMs from multi-frame DICOMs and render them as scene objects to see how different post effects can be used on them.

## Steps to Follow
### From DICOM to Scene Object
To incorporate DICOMs into your Open Inventor Scene, they have to be rendered as Open Inventor objects, which can be done by converting them into [WEMs](/glossary/#winged-edge-meshes) first. Begin by adding the modules `LocalImage`, `WEMIsoSurface`, and `SoWEMRenderer` to your workspace. Open the panel of the `LocalImage` module, browse your files, and choose a DICOM with multiple frames as input data. Connect the `LocalImage` module's output connector to `WEMIsoSurface` module's input connector to create a WEM of the study's surface. Then, connect the `WEMIsoSurface` module's output connector to the `SoWEMRenderer` module's input connector to render a scene object that can be displayed by adding a `SoExaminerViewer` module to the workspace and connecting the `SoWEMRenderer` module's output connector to its input connector. 

{{<alert class="check" caption="Check">}}
We don't recommend using single-frame DICOMs for this example as a certain depth is required to interact with the scene objects as intended. Also make sure that the pixel data of the DICOM file you choose contains all slices of the study, as it might be difficult to arrange scene objects of individual slices to resemble the originally captured study. 
{{</alert>}}

![From DICOM to SO](/images/tutorials/openinventor/multiframetoso.PNG "How to create a scene object out of a multi-frame DICOM")

{{<alert class="info" caption="Info">}}
Consider adding a `View2D` and an `Info` module to your `LocalImage` module's output connector to be able to compare the rendered object with the original image and adapt the isovalues to minimize noise.
{{</alert>}}

### PostEffectShader
To apply shading to our DICOM scene object, add a `SoShaderPipeline` and a `SoShaderPipelineCellShading` module to our network and connect their output connectors to a `SoToggle` module's input connector. Then, connect the `SoToggle` module's output connector to the `SoExaminerViewer`, but on the left side of the connection to the `SoWEMRenderer` module. This way, shading can be toggled and is applied to all scene objects connected to the right of the `SoToggle` module's connection. 

![Shading toggled off](/images/tutorials/openinventor/shadingtoggled1.PNG "Shading toggled off")
![Shading toggled on](/images/tutorials/openinventor/shadingtoggledon1.PNG "Shading toggled on")

### Tidying Your Workspace and Preparing the Next Steps
Now, add a `SoPostEffectBackground` module to your workspace and connect its output connector to the `SoExaminerViewer` module's input connector. Group the modules `SoToggle`, `SoShaderPipeline`, and `SoShaderPipelineCellShading` together and name the group "Toggle Shading". Then, group the modules `SoWEMRenderer`, `WEMIsoSurface`, and `LocalImage` together and name the group "DICOM Object". 

{{<alert class="info" caption="Info">}}
Structuring the workspace by grouping modules based on their functionality helps to stay focused and keeps everything tidy. 
{{</alert>}}

Use a `SoPostEffectMainGeometry` module to connect both of the groups you just created to the `SoExaminerViewer` module. Lastly, add a `SoPostEffectRenderer` module to your workspace and connect its output connector to the `SoExaminerViewer` module's input connector. 

![Grouped](/images/tutorials/openinventor/GroupedModules.PNG "Grouped modules")

You can now change your Open Inventor scene's background color. 

### PostEffectEdges
Add the module `SoPostEffectEdges` to your workspace and connect its output connector with the `SoExaminerViewer` module's input connector.
 
Then, open its panel and choose a color. You can try different modes, sampling distances and thresholds: 

![Colored Edges](/images/tutorials/openinventor/Edges1.PNG "Colored edges")
![Colored Edges 2](/images/tutorials/openinventor/Edges2.PNG "Varying settings of colored edges")
![Colored Edges 3](/images/tutorials/openinventor/Edges3.PNG "Varying settings of colored edges")

### PostEffectGeometry
To include geometrical objects in your Open Inventor scene, add two `SoSeparator` modules to the workspace and connect them to the input connector of `SoPostEffectMainGeometry`. Then, add a `SoMaterial`, `SoTransform`, and `SoSphere` or `SoCube` module to each `SoSeparator` and adjust their size (using the panel of the `SoSphere` or `SoCube` module) and placement within the scene (using the panel of the `SoTransform` module) as you like. 

{{<alert class="check" caption="Check">}}
You'll observe that the transparency setting in the `SoMaterial` module does not apply to the geometrical objects. Add a `SoPostEffectTransparentGeometry` module to your workspace, connect its output connector to the `SoExaminerViewer` module's input connector and its input connectors to the `SoSeparator` module's output connector to create transparent geometrical objects in your scene. 
{{</alert>}}

 ![Workspace](/images/tutorials/openinventor/WorkspaceAndNetwork.PNG "Workspace")

### PostEffectGlow
To put a soft glow on the geometrical scene objects, the module `SoPostEffectGlow` can be added to the workspace. 

![Glow](/images/tutorials/openinventor/WorkspaceWithGlow.PNG "Applied SoPostEffectGlow")

## Summary
* Multi-frame DICOM images can be rendered to be scene objects by converting them into WEMs first.
* Open Inventor scenes can be augmented by adding PostEffects to scene objects.

{{< networkfile "examples/open_inventor/PostEffectTutorial.mlab" >}}
