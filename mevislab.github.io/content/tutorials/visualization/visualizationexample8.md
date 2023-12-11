---
title: "Example 8: Vessel Segmentation using SoVascularSystem"
date: 2023-12-08
status: "OK"
draft: false
weight: 592
tags: ["Advanced", "Tutorial", "Visualization", "3D", "Vessel Segmentation"]
menu: 
  main:
    identifier: "visualization_example8"
    title: "Vessel Segmentation using SoVascularSystem."
    weight: 592
    parent: "visualization"
---
# Example 8: Vessel Segmentation using SoVascularSystem {#TutorialVisualizationExample8}

## Introduction
In this tutorial, we are using an input mask to create a vessel centerline using the `DtfSkeletonization` module and visualize the vascular structures in 3D using the `SoVascularSystem` module.

## Steps to do
### Develop your network

Load your tree mask ML image using the `LocalImage` module. Then connect the output to the `DtfSkeletonization` module as seen below. Adjust parameters if needed and press the *Open* button to obtain the skeleton and a graph with distinct node and edge IDs.

![LocalImage](/images/tutorials/visualization/V8_1.png "LocalImage")

{{<alert class="info" caption="Extra Infos">}}

Please be aware that a sample tree mask file is included as an attachment for this example

{{</alert>}}

Next, access the `DtfSkeletonization` module's panel and activate *Update skeleton graph* for a clear picture of how the skeletonized structures connect visually. Additionally, enable the *Compile Graph Voxels* to get details about the specific image voxels contributing to these skeletal structures. 

![DtfSkeletonization](/images/tutorials/visualization/V8_02.png "DtfSkeletonization")


To see the changes, click on the output of the LocalImage module. You'll find the ML image in the output inspector.

![Output of DtfSkeletonization of LocalImage](/images/tutorials/visualization/V8_MLImage.png "Output of DtfSkeletonization of LocalImage")

And if you click on the output of the `DtfSkeletonization` module this ML image will be shown.

![Output of DtfSkeletonization](/images/tutorials/visualization/V8_MLImage1.png "Output of DtfSkeletonization")


{{<alert class="info" caption="Extra Infos">}}

This helps compare the characteristics before and after using other modules like `SoVascularSystem`. 

{{</alert>}}

By connecting `DtfSkeletonization` to `GraphToVolume` you effectively convert the information about skeleton and vessel voxels into a volume and you are essentially making a clearer picture of the skeleton and vessels in the ML image.



{{<alert class="info" caption="Extra Infos">}}

Recognize that each graph edge comprises Skeletons (positions along the middle of an edge) and Vessel Voxels (voxels linked to the nearest Skeleton in that edge).

{{</alert>}}

![GraphToVolume](/images/tutorials/visualization/V8_03.png "GraphToVolume")

Now, connect the modules as illustrated in the example network image to ensure a proper flow of data and operations. The `SoLUTEditor` module enables interactive editing of color lookup tables, producing MLLUT and SoMLLUT objects. We connect it with `View2D` and `SoExaminerViewer` modules to set lookup tables in an Open Inventor scene, primarily designed for dynamic adjustments. On the other hand, the SoGVRVolumeRenderer module serves as a core tool for high-quality Volume Rendering of 3D/4D images using an octree-based approach and accepts an ML image as main volume dataset.

![Example Network](/images/tutorials/visualization/V8_04.png "Example Network")

### Store Edge IDs in Skeletons with RunPythonScript

The Skeletons can possess a **Label** property, which is not inherently available but can be created. Add `RunPythonScript` into your MeVisLab SDK and place the provided Python code into the RunPythonScript module in the network. Execute the network, ensuring that edge IDs are saved in the Skeletons for later use in coloring.


{{< highlight >}}
```Python

ctx.field("DtfSkeletonization.update").touch()

graph = ctx.field("DtfSkeletonization.outBase1").object()
if graph is not None:
  label = "Label"
  print('Num edges', len(graph.getEdges()))
  for edge in graph.getEdges():
    end_node = edge.getEndNode()
    for skeleton in edge.getSkeletons():      
      if label not in skeleton.properties:
        skeleton.createPropertyDouble(label, edge.getId())
      skeleton.setProperty(label, edge.getId())
  
  ctx.field("GraphToVolume.update").touch()

  {{</highlight>}}

  
{{<alert class="info" caption="Extra Infos">}}

This code is essential for creating the **Label** property for Skeletons, allowing for the assignment of Edge IDs to Skeletons. It ensures the existence of the **Label** property and populates it with the corresponding IDs. This step is crucial for subsequent visualization, especially if you aim to represent graph information in the 3D mask.

{{</alert>}}

![RunPythonScript](/images/tutorials/visualization/V8_05.png "RunPythonScript")

After pressing *Execute*, the network should resemble the image below:

![Initial Skeletonization Results (Without Colors)](/images/tutorials/visualization/V8_06.png "Initial Skeletonization Results (Without Colors)")

Proceed to explore some customization options with the `SoGVRVolumeRenderer` module. Open its panel in the *Main* tab, and for a more illuminated rendering, select *Illuminated* as the *Render Mode*. Adjust the *Quality* setting to *0.10* for enhanced visuals. Head over to the *Illumination* tab and implement these changes as demonstrated below.

![SoGVRVolumeRenderer](/images/tutorials/visualization/V8_07.png "SoGVRVolumeRenderer")

### Visualization with SoLUTEditor

Open the `SoLUTEditor` module to establish a connection between voxel values (edge IDs) and their respective colors. Keep in mind the concept of color interpolation, where not every ID is assigned a unique color.

Now, choose your preferred colors and navigate to the *Range* tab. Set the *New Range Max* setting to *160* beacause we have 165 edges and need a unique color for each edge. Click on *Apply new Range* to ensure your color selections are applied. Execute the network to witness the 3D mask come to life, with distinct colors representing various graph node/edge IDs.

By the end of this process, you'll have two images at your dispose. 

![Enhanced Skeletonization Results (With Colors)](/images/tutorials/visualization/V8_081.png "Enhanced Skeletonization Results (With Colors)")

### Interaction with the Generated Vascular System Using SoVascularSystem

If you wish to engage with the generated vascular system interactively, the `SoVascularSystem` module is your gateway to seamless exploration and interaction. Add it to your MeVisLab SDK and Connect it to your `DtfSkeletonization` module. But first, you may need to connect it to an extra `SoExaminerViewer1` to observe the dirfferece wenn using this module. 

![ EditedNetwork](/images/tutorials/visualization/V8_SoVascularSystem.png " EditedNetwork")

You can also connect the camera positions of your both `SoExaminerViewer` modules with a syntaxfloat as shown bellow to move them simultaneously. 

![ Camera positions](/images/tutorials/visualization/V8_SyntaxFloat.png " Camera positions")

Now you can notice the difference between the two modules. We use `SoVascularSystem` for a smoother and visually pleasing viewer, while the `SoGVRVolumeRenderer`, despite having many steps, provides precise results and is better suited for calculating totale volume and similiar metrics. 

![ SoVascularSystem & SoGVRVolumeRenderer](/images/tutorials/visualization/V8_Difference1.png " SoVascularSystem & SoGVRVolumeRenderer")

the `SoVascularSystem` module have many visualization examples unlike `SoGVRVolumeRenderer`, which can just render a mask in 3D . Open `SoVascularSystem`'s panel and select *Random Points* for *Display Mode* in the *Main* tab to observe the changes. 

![ Random Points](/images/tutorials/visualization/V8_SoVasularSystem_DisplayMode1.png " Random Points")

Change it for example to *Skeleton*, which shows only the centrelines of the vessels. 


![ Skeleton](/images/tutorials/visualization/V8_SoVasularSystem_DisplayMode2.png " Skeleton")

### Enhance Vessel Visualization Based on Distance Information

Now that you've successfully obtained the vessel skeleton graph using `DtfSkeletonization`, let's take the next step to enhance the vessel visualization based on the radius information. We'll modify the existing code to incorporate the Skeleton's property **Label** for storing the radius of the vessels, which will subsequently be used to color the rendering.

In your `RunPythonScript` module, replace the existing code with the following:

{{< highlight >}}
```Python

ctx.field("DtfSkeletonization.update").touch()

graph = ctx.field("DtfSkeletonization.outBase1").object()
if graph is not None:
  label = "Label"
  print('Num edges', len(graph.getEdges()))
  for edge in graph.getEdges():
    end_node = edge.getEndNode()
    for skeleton in edge.getSkeletons():
      if label not in skeleton.properties:
        skeleton.createPropertyDouble(label, edge.getId())
      skeleton.setProperty(label, skeleton.getProperty("MinDistance"))

  ctx.field("GraphToVolume.update").touch()
  ctx.field("SoVascularSystem.apply").touch()

  {{</highlight>}}


{{<alert class="info" caption="Extra Infos">}}

This modified script ensures that the Skeleton's property **Label** is utilized to store its distance information. The vessels will now be displayed with colors based on their minimal distance. 

{{</alert>}}

Now, let's visualize the impact of the modifications in the script. After executing the updated network, head to the `SoLUTEditor` module in the interface. Once there, navigate to the *Range* tab and tweak the *New Range Max* to *10*. Choose red for the small distance and green for the large.

With these adjustments made, click on *Apply New Range*. Immediately, you'll observe a dynamic transformation in the color representation of the vessel visualization. This alteration, driven by the minimal distance, enhances the clarity and informativeness of the displayed vascular structures. Take this opportunity to explore and analyze the results, providing valuable insights into the intricacies of the vessel system.

![ Enhanced_Vessel_Visualization_Result](/images/tutorials/visualization/V8_010new.png "Enhanced_Vessel_Visualization_Result") 

Here in the 2D Viewers, you can also notice that the small vessels are red and the big ones are green.

![ 2D Viewers](/images/tutorials/visualization/V8_2DViewers.png "2D Viewers") 

