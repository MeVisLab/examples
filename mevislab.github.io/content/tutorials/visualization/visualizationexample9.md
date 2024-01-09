---
title: "Example 9: Creating Dynamic 3D Animations using AnimationRecorder"
date: 2024-01-08
status: "OK"
draft: false
weight: 593
tags: ["Advanced", "Tutorial", "Visualization", "3D", "Vessel Segmentation"]
menu: 
  main:
    identifier: "visualization_example9"
    title: "Creating Dynamic 3D Animations using AnimationRecorder"
    weight: 593
    parent: "visualization"
---
# Example 9: Creating Dynamic 3D Animations using AnimationRecorder {#TutorialVisualizationExample9}

## Introduction
In this tutorial, our focus will be on using the `AnimationRecorder` module to generate dynamic and visually appealing animations of our 3D scenes. We'll be recording the results of our previous project, particularly the detailed visualizations of the muscles, bones and blood vessels created using `PathTracer`.

## Steps to do

Open the network of *Example 6.2: Visualisation using `PathTracer`*, add a `SoSeparator` and an `AnimationRecorder` into your workspace and connect them as shown down below. 

`SoSeparator`’s role is to isolate and organize scene components, enabling precise control over the animation's focus without affecting the entire scene. 

`AnimationRecorder`, equipped with a key frame editor, facilitates smooth transitions between different states of the 3D scene by allowing field additions via drag-and-drop. The tree view allows for easy reordering of fields and modules, enhancing overall organization.

![ AnimationRecorder](/images/tutorials/visualization//pathtracer/Example9_1.png " AnimationRecorder")

Define the following LUTs in `SoLUTEditor` of the knee or load this [XML file](/examples/visualization/example6/LUT_AnimationRecorder1.xml) with `LUTLoad1` to use a pre-defined LUT.

![ SoLUTEditor](/images/tutorials/visualization//pathtracer/V9_LUT.png " SoLUTEditor")


Open the `AnimationRecorder` module and click on *New* to initiate a new animation, selecting a filename for the recorded video.

At the bottom of the `AnimationRecorder` panel, you'll find the key frame editor, which is initially enabled. It contains the camera track with a key frame at position *0*. The key frame editor at the bottom serves as a control hub for playback and recording.

![ AnimationRecorder](/images/tutorials/visualization//pathtracer/V9_AnimationRecorder.png " AnimationRecorder")

Open the `AnimationRecorder` panel and locate the key frame editor. Move to the desired timepoint on the timeline, adjusting the camera to the preferred position in your 3D scene. Upon double-clicking on the timeline at the chosen timepoint, a Key frame will be added and a window labeled *Edit Camera Key Frame* will open.

Within the *Edit Camera Key Frame* window, set the camera position as desired. Save each key frame by clicking on the *Store Current Camera State* button.
Repeat this process for each timepoint where adjustments to the camera position are needed, thus creating a sequence of key frames. Ensure to set the *Duration* of the animation to *45* seconds. 

Before proceeding further, use the playback options situated at the base of the key frame editor. This allows for a quick review of the initial camera sequence, ensuring the adjustments align seamlessly for a polished transition between key frames.

![ AnimationRecorder](/images/tutorials/visualization//pathtracer/V9_AnimationRecorder1.png " AnimationRecorder")

## Modulating Knee Visibility with LUTRescale in Animation

We want to showcase the complete scene, followed by the bones and vessels, then only the bones, and finally the entire scene once again. Add two `LUTRescale` modules to your workspace and connect them as illustrated down below. This configuration allows you to use the `LUTRescale` to modifiy the index range of the LUT loaded with `LUTLoad`, affecting the rendering of the `SoPathTracerVolume`. The rationale behind using `LUTRescale` is to control the transparency or visibility of elements in the scene at different intervals.

![ LUTRescale](/images/tutorials/visualization//pathtracer/V9_3.png " LUTRescale")

## Animate Bones and Vessels

Now, let's shift our focus to highlighting bones and vessels within the animation. Right-click on the `LUTRescale` module, navigate to *Show Window*, and select *Automatic Panel*. This will bring up the control window for the ` LUTRescale` module. Find the field named *targetMax*. You can either drag or drop it directly from the *Automatic Panel*, or alternatively, locate the *Max* field in the *Output Index Range* box within the module panel and then drag and drop it onto the fields section in the `AnimationRecorder` module, specifically under the *Perspective Camera* field.
 
By linking the *targetMax* field of the `LUTRescale` module to the `AnimationRecorder` in this manner, you establish a connection that allows you to synchronize the visibility of the knee muscles and structures in your animation. 

![ LUTRescale & AnimationRecorder](/images/tutorials/visualization//pathtracer/LUTRescale_AnimationRecorder2.png " LUTRescale & AnimationRecorder")


To initiate the animation sequence, start by adding a key frame at position *0* for the *targetMax* field. Set the *Target Max* value in the *Edit Key Frame – [LUTRescale.targetMax]* window to *1*, and click on the *Store Current Field Value* button to save it.

Next, proceed to add key frames at the same timepoints as the desired key frames of the *Perspective Camera* field's first sequence. For each selected key frame, progressively set values for the *Target Max* field, gradually increasing to *10*. This ensures specific synchronization between the visibility adjustments controlled by the `LUTRescale` module and the camera movements in the animation, creating a seamless transition. This gradual shift visually reveals the bones and vessels while concealing the knee structures and muscles.

To seamlessly incorporate the new key frame at the same timepoints as the *Perspective Camera* field, you have two efficient options. Simply click on the key frame of the first sequence, and the line will automatically appear in the middle of the key frame. A quick double-click will effortlessly insert a key frame at precisely the same position. If you prefer more accurate adjustments, you can also set your frame manually using the *Edit Key Frame - [LUTRescale.targetMax]* window. This flexibility allows for precise control over the animation timeline, ensuring key frames align precisely with your intended moments.

![ LUTRescale & AnimationRecorder](/images/tutorials/visualization//pathtracer/V9_7.png " LUTRescale & AnimationRecorder")

## Showcasing only Bones

To control the visibility of the vessels, right-click on the ` LUTRescale1` module connected to the vessels. Open the *Show Window* and select *Automatic Panel*. Effortlessly drag and drop the *targetMax* field into the `AnimationRecorder` module's fields section. 

![ LUTRescale1 & AnimationRecorder](/images/tutorials/visualization//pathtracer/V9_8.png " LUTRescale1 & AnimationRecorder")

Add key frames for both the *Perspective Camera* field and the *targetMax* in `LUTRescale1` at the same timepoints. Access the *Edit Camera Key Frame* window for the added key frame in the *Perspective Camera* field and save the *current camera state*. To exclusively highlight only bones, adjust the *Target Max* values from *1* to *10000* in *Edit Key Frame - [LUTRescale1.targetMax]*.

![ LUTRescale1 & AnimationRecorder](/images/tutorials/visualization//pathtracer/V9_9.png " LUTRescale1 & AnimationRecorder")

To feature everything again at the end, copy the initial key frame of each field and paste it at the end of the timeline. This ensures a comprehensive display of all elements in the closing frames of your animation.

![ Final Animation Sequence Key Frames](/images/tutorials/visualization//pathtracer/V9_10.png " Final Animation Sequence Key Frames")

Finally, use the playback and recording buttons at the bottom of the key frame editor to preview and record your animation.

## Summary
* The animation was created by placing key frames strategically at different timepoints in the timeline using the `AnimationRecorder` module.
* Smooth transitions were ensured for both camera movements and visibility adjustments.
* The `LUTRescale` module played a vital role in controlling vessel visibility and emphasizing bones.
* Playback was utilized throughout the process for previewing and making necessary adjustments.
* The final animation was recorded with a  duration of 45 seconds.

{{< networkfile "examples/visualization/example6/AnimationRecorder.mlab" >}}