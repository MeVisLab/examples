---
title: "Step 1: Prototyping - Develop Your Network"
date: "2023-01-15"
status: "open"
draft: false
weight: 805
tags: ["Advanced", "Tutorial", "Prototyping"]
menu: 
  main:
    identifier: "summaryexample1"
    title: "Develop a Prototype of Your Application in MeVisLab SDK"
    weight: 805
    parent: "summary"
---

# Step 1: Prototyping - Develop Your Network

{{< youtube "-hbddg0bXcA" >}}

## Introduction
In this example, we will develop a network that fulfills the requirements mentioned on the [overview page](tutorials/summary#DevelopNetwork). The network will be developed by reusing existing modules and defining basic field values.

## Steps to Do

### 2D Viewer
The 2D viewer shall visualize the loaded images. In addition to that, it shall be possible to click into the image to trigger a region growing algorithm to segment parts of the loaded image based on a position and a threshold.

The following requirements from the [overview](tutorials/summary#DevelopNetwork) will be implemented:
* **Requirement 1**: The application shall be able to load DICOM data
* **Requirement 3**: The 2D viewer shall display the loaded images
* **Requirement 4**: The 2D viewer shall provide the possibility to segment parts of the image based on a region growing algorithm
  * **Requirement 4.1**: It shall be possible to click into the image to set a marker position to start the region growing algorithm
  * **Requirement 4.2**: It shall be possible to define a threshold for the region growing algorithm
* **Requirement 5**: The 2D viewer shall display the segmentation results as a semitransparent overlay
  * **Requirement 5.1**: It shall be possible to define the color of the overlay

Add a `LocalImage` and a `View2D` module to your workspace. You are now able to load an image and view the slices. 

![Loading an image](images/tutorials/summary/Example1_1.png "Loading an image")

Region growing requires a `SoView2DMarkerEditor`, a `SoView2DOverlay`, and a `RegionGrowing` module. Add them to your network and connect them as seen below. Configure the `RegionGrowing` module to use a *3D-6-Neighborhood (x,y,z)* relation and an automatic threshold value of *1.500*. Also select *Auto-Update*.

Set `SoView2DMarkerEditor` to allow only one marker by defining *Max Size = 1* and *Overflow Mode = Remove All*. For our application we only want one marker to be set for defining the `RegionGrowing`.

If you now click into your loaded image via left mouse button {{< mousebutton "left" >}}, the `RegionGrowing` module segments all neighborhood voxels with a mean intensity value plus/minus the defined percentage value from your click position.

The overlay is shown in white.

![RegionGrowing via marker editor](images/tutorials/summary/Example1_2.png "RegionGrowing via marker editor")

Open the `SoView2DOverlay` module, change *Blend Mode* to *Blend*, and select any color and *Alpha Factor* for your overlay. The applied changes are immediately visible. 
![Overlay color and transparency](images/tutorials/summary/Example1_3.png "Overlay color and transparency")

The segmented results from the `RegionGrowing` module might contain gaps because of differences in the intensity value of neighboring voxels. You can close these gaps by adding a `CloseGap` module. Connect it to the `RegionGrowing` and the `SoView2DOverlay` module and configure *Filter Mode* as *Binary Dilatation*, *Border Handling* as *Pad Dst Fill*, and set *KernelZ* to *3*.

Lastly, we want to calculate the volume of the segmented parts. Add a `CalculateVolume` module to the `CloseGap` module. The 2D viewer now provides the basic functionalities. 

You can group the modules in your network for an improved overview by selecting {{<menuitem "Grouping" "Add to new Group..." >}}. Leave `LocalImage` out of the group and name it *2D Viewer*. Your network should now look like this:

![Group 2D Viewer](images/tutorials/summary/Example1_4.png "Group 2D Viewer")

### 3D Viewer
The 3D viewer shall visualize your loaded image in 3D and additionally provide the possibility to render your segmentation results. You will be able to decide for different views, displaying the image and the segmentation, only the image or only the segmentation. The volume (in ml) of your segmentation results shall be calculated.

The following requirements from [overview](tutorials/summary#DevelopNetwork) will be implemented:
* **Requirement 2**: The application shall provide a 2D and a 3D viewer
* **Requirement 6**: The 3D viewer shall visualize the loaded data in a three-dimensional volume rendering
* **Requirement 7**: The 3D viewer shall additionally show the segmentation result as a three-dimensional mesh
* **Requirement 8**: The total volume of the segmented area shall be calculated and shown (in ml)
* **Requirement 9**: It shall be possible to toggle the visible 3D objects
  * **Requirement 9.1**: Original data
  * **Requirement 9.2**: Segmentation results
  * **Requirement 9.3**: All

Add a `SoExaminerViewer`, a `SoWEMRenderer`, and an `IsoSurface` module to your existing network and connect them to the `LocalImage` module. Configure the `IsoSurface` to use an *IsoValue* of *200*, a *Resolution* of *1* and check *Auto-Update* and *Auto-Apply*.

![3D Viewer](images/tutorials/summary/Example1_5.png "3D Viewer")

The result should be a three-dimensional rendering of your image.

![SoExaminerViewer](images/tutorials/summary/Example1_6.png "SoExaminerViewer")

{{<alert class="info" caption="Info">}}
If the rendering is not immediately applied, click *Apply* in your `IsoSurface` module.
{{</alert>}}

Define the field <attribute>instanceName</attribute> of your `IsoSurface` module as <field>IsoSurfaceImage</field> and add another `IsoSurface` module to your network. Set the <field>instanceName</field> to *IsoSurfaceSegmentation* and connect the module to the output of the `CloseGap` module from the image segmentation. Set <field>IsoValue</field> to *420*, <field>Resolution</field> to *1*, and check <field>Auto-Update</field> and <field>Auto-Apply</field>.

Set <field>instanceName</field> of the `SoWEMRenderer` module to *SoWEMRendererImage* and add another `SoWEMRenderer` module. Set this <field>instanceName</field> to *SoWEMRendererSegmentation* and connect it to the `IsoSurfaceSegmentation` module. Selecting the output of the new `SoWEMRenderer` shows the segmented parts as a 3D object in the output inspector.

![Segmentation preview in output inspector](images/tutorials/summary/Example1_7.png "Segmentation preview in output inspector")

Once again, we should group the modules used for 3D viewing and name the new group *3D Viewer*.

![Grouped network](images/tutorials/summary/Example1_8.png "Grouped network")

We now want to allow the user to toggle the different 3D visualizations as defined by the requirements above. It shall be possible to show:
* Original data only
* Segmentation only
* Original data and segmentation combined

Add a `SoSwitch` module to your network. Connect the switch to both of your `SoWEMRenderer` modules and to the `SoExaminerViewer`. 

![SoSwitch](images/tutorials/summary/Example1_9.png "SoSwitch")

The default input of the switch is *None*. Your 3D viewer remains black. Using the arrows on the `SoSwitch` allows you to toggle between the segmentation and the image. Input *0* shows the segmented brain, input *1* shows the head. You are now able to toggle between them. A view with both objects is still missing.

{{< imagegallery 2 "images/tutorials/summary" "Example1_Segmentation" "Example1_Image" >}}

Add a `SoGroup` module and connect both `SoWEMRenderer` modules as input. The output needs to be connected to the right input of the `SoSwitch` module. 

![SoGroup](images/tutorials/summary/Example1_10.png "SoGroup")

You can now also toggle input *2* of the switch showing both 3D objects. The only problem is: You cannot see the brain because it is located inside the head. Open the `SoWEMRendererImage` module panel and set <field>faceAlphaValue</field> to *0.5*. The viewer now shows the head in a semitransparent manner, so that you can see the brain. Certain levels of opacity are difficult to render. Add a `SoDepthPeelRenderer` module and connect it to the semitransparent `SoWEMRendererImage` module. Set <field>Layers</field> of the renderer to *1*.

![SoDepthPeelRenderer](images/tutorials/summary/Example1_Both.png "SoDepthPeelRenderer")

You have a 2D and a 3D viewer now. Let's define the colors of the overlay to be reused for the 3D segmentation.

### Parameter Connections for Visualization
Open the panels of the `SoView2DOverlay` and the `SoWEMRendererSegmentation` module. Draw a parameter connection from <field>SoView2DOverlay.baseColor</field> to <field>SoWEMRendererSegmentation.faceDiffuseColor</field>.

![Synchronized segmentation colors](images/tutorials/summary/Example1_11.png "Synchronized segmentation colors")

Now, the 3D visualization uses the same color as the 2D overlay.

## Summary
* You built a network providing the basic functionalities of your application.
* Actions inside your application need to be executed by changing fields in your network or by manually touching a trigger.

{{< networkfile "examples/summary/TutorialSummary.mlab" >}}
