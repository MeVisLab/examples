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

Load your tree mask ML image using the `LocalImage` module. Then connect the output to the `DtfSkeletonization` module as seen below. Press the *Load* button to obtain the skeleton and a graph with distinct node and edge IDs.

![LocalImage](/images/tutorials/visualization/V8_1.png "LocalImage")

{{<alert class="info" caption="Extra Infos">}}

The used sample tree mask is available for download [here](/examples/visualization/example8/EditedImage.mlimage)

{{</alert>}}

Next, access the `DtfSkeletonization` module's panel and activate *Update skeleton graph* for a clear picture of how the skeletonized structures connect visually. Additionally, enable the *Compile Graph Voxels* to get details about the specific image voxels contributing to these skeletal structures. 

![DtfSkeletonization](/images/tutorials/visualization/V8_02.png "DtfSkeletonization")


To see the changes, click first on the output of the LocalImage module to see the original image. You'll find the ML image in the output inspector.

![Output of DtfSkeletonization of LocalImage](/images/tutorials/visualization/V8_MLImage.png "Output of DtfSkeletonization of LocalImage")

And if you click on the output of the `DtfSkeletonization` module this ML image will be shown. The DtfSkeletonization module computes the skeletonization of the original image. The topology of the initial mask is preserved, vessel centerline extraction has been done. Erosion distances are coded in mm in the output image.

![Output of DtfSkeletonization](/images/tutorials/visualization/V8_MLImage1.png "Output of DtfSkeletonization")


{{<alert class="info" caption="Extra Infos">}}

This helps compare the characteristics before and after using other modules like `SoVascularSystem`. 

{{</alert>}}

By connecting `DtfSkeletonization` to `GraphToVolume` you effectively creat a new volume that includes the labels of the skeleton and the vessel voxel and you are essentially making a clearer picture of the skeleton and vessels in the ML image.



{{<alert class="info" caption="Extra Infos">}}

Recognize that each graph edge comprises Skeletons (positions along the middle of an edge) and Vessel Voxels (voxels linked to the nearest Skeleton in that edge).

{{</alert>}}

![GraphToVolume](/images/tutorials/visualization/V8_03.png "GraphToVolume")

Now, connect the modules as illustrated in the example network image to ensure a proper flow of data and operations. The `SoLUTEditor` module enables interactive editing of color lookup tables, producing MLLUT and SoMLLUT objects. We connect it with the `View2D` and `SoExaminerViewer` modules to set lookup tables in an Open Inventor scene, primarily designed for dynamic adjustments. On the other hand, the SoGVRVolumeRenderer module serves as a core tool for high-quality Volume Rendering of 3D/4D images using an octree-based approach and accepts an ML image as main volume dataset.

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

Proceed to explore some customization options with the `SoGVRVolumeRenderer` module. Open its panel in the *Main* tab, select *Illuminated* as the *Render Mode*. Adjust the *Quality* setting to *0.10* for enhanced visuals. Head over to the *Illumination* tab and implement these changes as demonstrated below.

![SoGVRVolumeRenderer](/images/tutorials/visualization/V8_07.png "SoGVRVolumeRenderer")

### Visualization with SoLUTEditor

Open the `SoLUTEditor` module to establish a connection between voxel values (edge IDs) and their respective colors. Keep in mind the concept of color interpolation, where not every ID is assigned a unique color.

Now, choose your preferred colors and navigate to the *Range* tab. Set the *New Range Max* setting to *160*, beacause we have 153 edges and need a unique color for each edge. Click on *Apply new Range* to ensure your color selections are applied. Execute the network to witness the 3D mask come to life, with distinct colors representing various graph node/edge IDs.

![SoLUTEditor](/images/tutorials/visualization/V8_SoLUTEditor.png "SoLUTEditor")


By the end of this process, you'll have two images at your dispose. 

![Enhanced Skeletonization Results (With Colors)](/images/tutorials/visualization/V8_081.png "Enhanced Skeletonization Results (With Colors)")

### Interaction with the Generated Vascular System Using SoVascularSystem

In comparison to the `SoGVRVolumeRenderer`, add a `SoVascularSystem` module to your workspace. Connect it to your `DtfSkeletonization` module and to the `SoLUTEditor` as seen below. Add another `SoExaminerViewer` for comparing the 2 visualization. The same `SoBackground` can be added to your new scene.

![ EditedNetwork](/images/tutorials/visualization/V8_SoVascularSystem.png " EditedNetwork")

Draw parameter connections from one `SoExaminerViewer` to the other. Use the fields seen below to synchronize your camera interaction.

![ Camera positions](/images/tutorials/visualization/V8_SyncFloat.png " Camera positions")

Connect the backwards direction of the two `SoExaminerViewer` by using a `SyncFloat` module.


{{<alert class="info" caption="Extra Infos">}}

To establish connections between fields with the type *Float*, you can use the *SyncFloat* module. For fields containing vector or rotation data, the appropriate connection can be achieved using the *SyncVector* module. Ensure they are moving concurrently.

{{</alert>}}

![ SyncFloat & SyncVector](/images/tutorials/visualization/V8_SyncFloat_Network.png " SyncFloat & SyncVector")

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

Now, let's visualize the impact of the modifications in the script. After executing the updated network, head to the `SoLUTEditor` module in the interface. Once there, navigate to the *Range* tab and tweak the *New Range Max* to *10*, beacause the maximum of the MinDistance is between 9 and 10. Choose red for the small distance and green for the large.

With these adjustments made, click on *Apply New Range*. Immediately, you'll observe a dynamic transformation in the color representation of the vessel visualization. This alteration, driven by the minimal distance, enhances the clarity and informativeness of the displayed vascular structures. Take this opportunity to explore and analyze the results, providing valuable insights into the intricacies of the vessel system.

![ Enhanced_Vessel_Visualization_Result](/images/tutorials/visualization/V8_010new.png "Enhanced_Vessel_Visualization_Result") 

Here in the 2D Viewers, you can also notice that the small vessels are red and the big ones are green.

![ 2D Viewers](/images/tutorials/visualization/V8_2DViewers.png "2D Viewers") 

### Tipp 

If you have a NIFTI file and want to convert it into an ML image. Therefore, Load your tree mask NIfTI file using the *itkFileImageReader* module. Adjust parameters if needed and press the *Open* button. Then connect the output to *BoundingBox*, which scans the input automatically and calculates all its voxels. Finally, you need *MLImageFormatSave* to save it as a file including user defined information and ML image properties, that is clearly much smaller than a NIFTI file. 

![ How to](/images/tutorials/visualization/V8_ConvertToMlImage.png "How to") 

## Summary
* Vessel centreline can be created using `DtfSkeletonization`
* Vascular structures can be visualized in 3D using `SoVascularSystem`
* It has several display modes available and other adjustments ragrading the coloring and point size
* The labels about skeleton and vessel voxels can be converted into a volume using `GraphToVolume`
* To perform volume rendering on 3D images you can use `SoGVRVolumeRenderer`
* You can visualize vessels based on their radius using  Python scripting 

{{< networkfile "examples/visualization/example8/VisualizationExample8.mlab" >}}
{{< networkfile "examples/visualization/example8/VisualizationExample8_01.mlab" >}}
