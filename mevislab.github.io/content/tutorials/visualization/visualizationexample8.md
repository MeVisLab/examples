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
In this tutorial, we'll walk you through the steps to craft a visually striking portrayal of vascular structures by harnessing the capabilities of the `DtfSkeletonization` module. By combining the vessel centerline extraction power of `DtfSkeletonization` with the immersive 3D visualization provided by the `SoVascularSystem` module, you'll effortlessly explore and interact with the intricacies of the resulting vascular system. This integration enhances your ability to comprehensively understand and analyze complex vascular structures.

## Steps to do
### Develop your network

Load your tree mask ML image using the `LocalImage` module. Then connect the output to the `DtfSkeletonization` module as seen below. Adjust parameters if needed and press the *Open* button to obtain the skeleton and a graph with distinct node and edge IDs.

![LocalImage](/images/tutorials/visualization/V8_1.png "LocalImage")

{{<alert class="info" caption="Extra Infos">}}

Please be aware that a sample tree mask file is included as an attachment for this example

{{</alert>}}

Next, access the `DtfSkeletonization` module's panel and activate *Update skeleton graph* and *Compile graph voxels* for enhanced functionality.

![DtfSkeletonization](/images/tutorials/visualization/V8_02.png "DtfSkeletonization")

Use the `GraphToVolume` module to convert the graph into an ML image. Connect the output graph from `DtfSkeletonization` to the `GraphToVolume` module.

{{<alert class="info" caption="Extra Infos">}}

Recognize that each graph edge comprises Skeletons (positions along the middle of an edge) and Vessel Voxels (voxels linked to the nearest Skeleton in that edge).

{{</alert>}}

![GraphToVolume](/images/tutorials/visualization/V8_03.png "GraphToVolume")

Now, connect the modules as illustrated in the example network image to ensure a proper flow of data and operations. 

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

Now, choose your preferred colors and navigate to the *Range* tab. Set the *New Range Max* setting to *160* to adapt the color range accordingly. Click on *Apply new Range* to ensure your color selections are applied. Execute the network to witness the 3D mask come to life, with distinct colors representing various graph node/edge IDs.

By the end of this process, you'll have two images at your dispose. 

![Enhanced Skeletonization Results (With Colors)](/images/tutorials/visualization/V8_08.png "Enhanced Skeletonization Results (With Colors)")

### Interaction with the Generated Vascular System Using SoVascularSystem

If you wish to engage with the generated vascular system interactively, the `SoVascularSystem` module is your gateway to seamless exploration and interaction. Connect it to your `DtfSkeletonization` module, explore its settings and observe the changes..

![ SoVascularSystem](/images/tutorials/visualization/V8_09.png " SoVascularSystem")

### Enhance Vessel Visualization Based on Distance Information

Now that you've successfully obtained the vessel skeleton graph using `DtfSkeletonization`, let's take the next step to enhance the vessel visualization based on the distance information. We'll modify the existing code to incorporate the Skeleton's property **Label** for storing distance information, which will subsequently be used to color the rendering.

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

Now, let's visualize the impact of the modifications in the script. After executing the updated network, head to the `SoLUTEditor` module in the interface. Once there, navigate to the *Range* tab and tweak the *New Range Max* to *10*.

With these adjustments made, click on *Apply New Range*. Immediately, you'll observe a dynamic transformation in the color representation of the vessel visualization. This alteration, driven by the minimal distance, enhances the clarity and informativeness of the displayed vascular structures. Take this opportunity to explore and analyze the results, providing valuable insights into the intricacies of the vessel system.

![ Enhanced_Vessel_Visualization_Result](/images/tutorials/visualization/V8_010.png "Enhanced_Vessel_Visualization_Result")