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
In this tutorial, we are using an input mask to create a vessel centerline using the `DtfSkeletonization` module and visualize the vascular structures in 3D using the `SoVascularSystem` module. The second part uses the distance between centerline and surface of the vessel structures to color thin vessels red and thick vessels green.

## Steps to do
### Develop your network

Load the example [tree mask](/examples/visualization/example8/EditedImage.mlimage) by using the `LocalImage` module. Connect the output to a `DtfSkeletonization` module as seen below. The initial output of the `DtfSkeletonization` module is empty. Press the *Update* button to calculate the skeleton and the erosion distances.

![Network](/images/tutorials/visualization/V8_1.png "Network")

Below you can see the output of the original image taken from the `LocalImage` module (left) compared to the output after calculating the skeleton via `DtfSkeletonization` module (right).

![Output comparison](/images/tutorials/visualization/V8_1b.png "Output comparison")

The output *DtfSkeletonization.outBase1* shows nothing. Here you can find the 3-dimensional graph of the vascular structures. To generate it, open the panel of the `DtfSkeletonization` module, set *Update Mode* to *Auto Update* and select *Update skeleton graph*. Now the output additionally provides a 3D graph. Additionally, enable the *Compile Graph Voxels* to provide all object voxels at the output. 

![DtfSkeletonization](/images/tutorials/visualization/V8_02.png "DtfSkeletonization")

You can use the *Output Inspector* to see the 3D graph.

![Graph output of DtfSkeletonization](/images/tutorials/visualization/V8_MLImage.png "Graph output of DtfSkeletonization")

If you want to visualize your graph, you should connect a `GraphToVolume` module to the `DtfSkeletonization` module. The result is a 2D or 3D volume of your graph which you can connect to any 2D or 3D viewer. Add a `View2D` and a `View3D` module to the `GraphToVolume` module and update the volume.

![GraphToVolume](/images/tutorials/visualization/V8_03.png "GraphToVolume")

For coloring the vessels depending on their distances to the centerline, we need a `SoLUTEditor` module. Change your network to use a `SoExaminerViewer` module, a `SoLUTEditor` module and a `SoBackground` module instead of a `View3D` module.

Use the `SoLUTEditor` for the `View2D`, too.

![Network](/images/tutorials/visualization/V8_04.png "Network")

 Open the output of the `GraphToVolume` module and inspect the images in Output Inspector. You will see that the HU value of the black background is defined as *-1*, the vessel tree is defined as *0*.

![Output Inspector](/images/tutorials/visualization/V8_04_OutputInspector.png "Output Inspector")

Open the Panel of the `SoLUTEditor` and select tab *Range*. Define *New Range Min* as *-1* and *New Range Max* as *0*.

![SoLUTEditor Range](/images/tutorials/visualization/V8_04_Range.png "SoLUTEditor Range")

Change to *Editor* tab and define the following LUT:

![SoLUTEditor Editor](/images/tutorials/visualization/V8_04_Editor.png "SoLUTEditor Editor")

The viewers now show your vessel graph.

![View2D and SoExaminerViewer](/images/tutorials/visualization/V8_04_Viewer.png "View2D and SoExaminerViewer")

### Store Edge IDs in Skeletons with RunPythonScript
Each edge of the calculated skeleton gets a unique ID defined by the `DtfSkeletonization` module. We now want to use this ID to define a different color for each edge of the skeleton. You can use the **Label** property of each skeleton to store the ID of the edge.

Add a `RunPythonScript` module to your network, open the panel of the module and enter the following Python code:

{{< highlight >}}
```Python
ctx.field("DtfSkeletonization.update").touch()

graph = ctx.field("DtfSkeletonization.outBase1").object()
if graph is not None:
  for edge in graph.getEdges():
    print(edge.getId())
  
ctx.field("GraphToVolume.update").touch()
```
{{</highlight>}}

First, we always want a fresh skeleton. We touch the *update* trigger of the module `DtfSkeletonization`. Then we get the graph from the *DtfSkeletonization.outBase1* output. If a valid graph is available, we walk through all edges of the graph and print the ID of each edge. In the end, we update the GraphToVolume module to get the calculated values of the Python script in the viewers. Click *Execute*.

The Debug Output of the MeVisLab IDE shows a numbered list of edge IDs from 1 to 153.

![RunPythonScript](/images/tutorials/visualization/V8_05.png "RunPythonScript")

We now want the edge ID to be used for coloring each of the skeletons differently. Open the Panel of the `SoLUTEditor` and select tab *Range*. Define *New Range Min* as *0* and *New Range Max* as *153*. Define different colors for your LUT.

![SoLUTEditor](/images/tutorials/visualization/V8_05_LUT.png "SoLUTEditor")

The `SoGVRVolumeRenderer` module also needs a different setting. Open its panel in the *Main* tab, select *Illuminated* as the *Render Mode*. Adjust the *Quality* setting to *0.10*. On tab *Advanced*, set *Filter Volume Data* to *Nearest*. Change to the *Illumination* tab and define below parameters:

{{<imagegallery 2 "/images/tutorials/visualization" "SoGVRVolumeRendererMain" "SoGVRVolumeRendererIllumination">}}

Change your Python script as follows:
{{< highlight >}}
```Python
ctx.field("DtfSkeletonization.update").touch()

graph = ctx.field("DtfSkeletonization.outBase1").object()
if graph is not None:
  label = "Label"
  for edge in graph.getEdges():
    for skeleton in edge.getSkeletons():
      if label not in skeleton.properties:
        skeleton.createPropertyDouble(label, edge.getId())
      skeleton.setProperty(label, edge.getId())
  
ctx.field("GraphToVolume.update").touch()
```
{{</highlight>}}

In case the graph is valid, we now define a static text for the label. Instead of printing the edge ID, we also walk through each skeleton of the edge and define the property for the label using the ID of the edge as value.

Your viewers now show a different color for each skeleton, based on our LUT.

![View2D and SoExaminerViewer](/images/tutorials/visualization/V8_05_Viewer.png "View2D and SoExaminerViewer")

### Render Vascular System Using SoVascularSystem
The `SoVascularSystem` module is optimized for rendering vascular structures. In comparison to the `SoGVRVolumeRenderer` module, it allows to render the surface, the skeleton or points of the structure in an open inventor scene graph. Interactions with edges of the graph are also already implemented.

Add a `SoVascularSystem` module to your workspace. Connect it to your `DtfSkeletonization` module and to the `SoLUTEditor` as seen below. Add another `SoExaminerViewer` for comparing the two visualization. The same `SoBackground` can be added to your new scene.

Uncheck *Use skeleton colors* and *Use integer LUT* on *Appearance* tab of the `SoVascularSystem` module panel.

![ EditedNetwork](/images/tutorials/visualization/V8_SoVascularSystem.png " EditedNetwork")

{{<alert class="info" caption="Extra Infos">}}
More information about the `SoVascularSystem` module can be found in the {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/SoVascularSystem.html" "help page" >}} of the module.
{{</alert>}}

Draw parameter connections from one `SoExaminerViewer` to the other. Use the fields seen below to synchronize your camera interaction.

![ Camera positions](/images/tutorials/visualization/V8_SyncFloat.png " Camera positions")

Connect the backwards direction of the two `SoExaminerViewer` by using multiple `SyncFloat` modules and two `SyncVector` modules for *position* and *orientation* fields.

{{<alert class="info" caption="Extra Infos">}}
To establish connections between fields with the type *Float*, you can use the *SyncFloat* module. For fields containing vector, the appropriate connection can be achieved using the *SyncVector* module.
{{</alert>}}

![ SyncFloat & SyncVector](/images/tutorials/visualization/V8_SyncFloat_Network.png " SyncFloat & SyncVector")

Camera interactions are now synchronized between both `SoExaminerViewer` modules.

Now you can notice the difference between the two modules. We use `SoVascularSystem` for a smoother visualization of the vascular structures by using the graph as reference. The `SoGVRVolumeRenderer` renders the volume from the `GraphToVolume` module, including the visible stairs from pixel representations in the volume. 

![ SoVascularSystem & SoGVRVolumeRenderer](/images/tutorials/visualization/V8_Difference1.png " SoVascularSystem & SoGVRVolumeRenderer")

The `SoVascularSystem` module has additional visualization examples unlike `SoGVRVolumeRenderer`. Open the panel of the `SoVascularSystem` module and select *Random Points* for *Display Mode* in the *Main* tab to see the difference. 

![ Random Points](/images/tutorials/visualization/V8_SoVasularSystem_DisplayMode1.png " Random Points")

Change it to *Skeleton* to only show the centerlines/skeletons of the vessels. 

![ Skeleton](/images/tutorials/visualization/V8_SoVasularSystem_DisplayMode2.png " Skeleton")

{{<alert class="warning" caption="Warning">}}
For volume calculations, use the original image mask instead of the result from `GraphToVolume`. 
{{</alert>}}

### Enhance Vessel Visualization Based on Distance Information
Now that you've successfully obtained the vessel skeleton graph using `DtfSkeletonization`, let's take the next step to enhance the vessel visualization based on the radius information of the vessels. We will modify the existing code to use the minimum distance between centerline and surface of the vessels for defining the color.

The values for the provided vascular tree vary between 0 and 10mm. Therefore define the range of the `SoLUTEditor` to *New Range Min* as *1* and *New Range Max* as *10*. On *Editor* tab, define the following LUT:

![SoLUTEditor](/images/tutorials/visualization/V8_SoLUTEditor2.png "SoLUTEditor")

In the `RunPythonScript` module, change the existing code to the following:
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
        skeleton.createPropertyDouble(label, skeleton.getProperty("MinDistance"))
      skeleton.setProperty(label, skeleton.getProperty("MinDistance"))

ctx.field("GraphToVolume.update").touch()
ctx.field("SoVascularSystem.apply").touch()
```
{{</highlight>}}


{{<alert class="warning" caption="Warning">}}
Be aware that the *MinDistance* and *MaxDistance* values are algorithm-specific and don't precisely represent vessel diameters. The result of `DTFSkeletonization` is a vascular graph with an idealized, circular profile while in reality, the vessels have more complicated profile.
{{</alert>}}

Instead of using the ID of each edge for the label property, we are now using the *MinDistance* property of the skeleton. The result is a color coded 3D visualization depending on the radius of the vessels. Small vessels are red, large vessels are green.

![Radius based Visualization](/images/tutorials/visualization/V8_010new.png "Radius based Visualization") 

{{<alert class="info" caption="Additional Info">}}
If you have a NIFTI file, convert it into an ML image. Load your tree mask NIfTI file using the `itkImageFileReader` module. Connect the output to a `BoundingBox` module, which removes black pixels and creates a volume without unmasked parts. In the end, add a `MLImageFormatSave` module to save it as *\*.mlimage* file. They are much smaller than a NIFTI file. 

![NIFTI file conversion](/images/tutorials/visualization/V8_ConvertToMlImage.png "NIFTI file conversion") 
{{</alert>}}

### Mouse Clicks on Vessel Graph
Open the *Interaction* tab of the `SoVascularSystem` module. In `SoExaminerViewer` module, change to *Pick Mode* and click into your vessel structure. The panel of the `SoVascularSystem` module shows all information about the hit of your click in the vessel tree.

![Getting the click point in a vascular tree](/images/tutorials/visualization/V8_Interactions.png "Getting the click point in a vascular tree") 

## Summary
* Vessel centerlines can be created using a `DtfSkeletonization` module
* Vascular structures can be visualized  using a `SoVascularSystem` module, which provides several vessel specific display modes
* The `SoVascularSystem` module provides information about mouse clicks into a vascular tree
* The labels of a skeleton can be used to store additional information for visualization

{{< networkfile "examples/visualization/example8/VisualizationExample8.mlab" >}}
