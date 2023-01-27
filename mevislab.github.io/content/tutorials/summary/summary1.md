---
title: "Example 1: Prototyping - Develop your Network"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Advanced", "Tutorial", "Prototyping"]
menu: 
  main:
    identifier: "summaryexample1"
    title: "Develop a prototype of your application in MeVisLab SDK."
    weight: 805
    parent: "summary"
---
# Example 1: Prototyping - Develop your Network
## Introduction
In this example, we will develop a network which fulfills the requirements from the [overview page](/tutorials/summary#DevelopNetwork). The network will be developed by re-using existing modules and defining basic field values.

## Steps to do
### 2D viewer
The 2D viewer shall visualize the loaded images. In addition to that, it shall be possible to click into the image for starting a RegionGrowing algorithm segmenting parts of the loaded image based on a threshold.

The following requirements from [Overview](/tutorials/summary#DevelopNetwork) will be implemented:
* **Requirement 1**: The application shall be able to load DICOM data.
* **Requirement 3**: The 2D viewer shall display the loaded images
* **Requirement 4**: The 2D viewer shall provide the possibility to segment parts of the image based on a RegionGrowing algorithm
  * **Requirement 4.1**: It shall be possible to click into the image for defining a marker position for starting the RegionGrowing
  * **Requirement 4.2**: It shall be possible to define a threshold for the RegionGrowing algorithm
* **Requirement 5**: The 2D viewer shall display the segmentation results as a semi-transparent overlay
  * **Requirement 5.1**: It shall be possible to define the color of the overlay

Add a `LocalImage` and a `View2D` module to your workspace. You are now able to load an image and view the slices. 

![Loading an image](/images/tutorials/summary/Example1_1.png "Loading an image")

For the RegionGrowing, we need a `SoView2DMarkerEditor`, a `SoView2DOverlay` and a `RegionGrowing` module. Add them and connect them as seen below. Configure the `RegionGrowing` module to use a *3D-6-Neighborhood (x,y,z)* relation and an automatic threshold value of *1.500*. Also select *Auto-Update*.

Set `SoView2DMarkerEditor` to allow only 1 Marker by defining *Max Size = 1* and *Overflow Mode = Remove All*. For our application we only want 1 Marker to be set for defining the `RegionGrowing`.

If you now click into your loaded image via left mouse button {{< mousebutton "left" >}}, the `RegionGrowing` module segments all neighborhood pixels with a mean intensity value plus/minus defined percentage value from your click position.

The overlay is shown in white.

![RegionGrowing via marker editor](/images/tutorials/summary/Example1_2.png "RegionGrowing via marker editor")

Open the `SoView2DOverlay` module, define Blend Mode to *Blend* and select any color and *Alpha Factor* for your overlay. The changes are applied automatically in the viewer.

![Overlay color and transparency](/images/tutorials/summary/Example1_3.png "Overlay color and transparency")

The segmented results from the `RegionGrowing` module might contain some holes because of differences in the intensity value of neighboring pixels. You can close those holes by using a `CloseGap` module. Connect it between the `RegionGrowing` and the `SoView2DOverlay` and configure Filter Mode as *Binary Dilatation*, Border Handling as *Pad Dst Fill* and set KernelZ to *3*.

In the end we want to calculate the volume of the segmented parts. Add a `CalculateVolume` module to the `CloseGap`.

The 2D viewer now provides the basic functionalities. For a better overview, you should select all modules except the `LocalImage` and select {{<menuitem "Grouping" "Add to new Group..." >}}. Name the group *2D Viewer*. Your network should now look like this:

![Group 2D Viewer](/images/tutorials/summary/Example1_4.png "Group 2D Viewer")

### 3D Viewer
The 3D viewer shall visualize your loaded image in 3D and additionally provide the possibility to render your segmentation results. It shall be possible to switch between different views for showing image and segmentation, only image or only segmentation.

In the end, the volume (in ml) of your segmentation results shall be calculated.

The following requirements from [Overview](/tutorials/summary#DevelopNetwork) will be implemented:
* **Requirement 2**: The application shall provide a 2D and a 3D viewer.
* **Requirement 6**: The 3D viewer shall visualize the loaded data in a 3-dimensional volume rendering
* **Requirement 7**: The 3D viewer shall additionally show the segmentation result as a 3-dimensional mesh
* **Requirement 8**: The total volume of the segmented area shall be calculated and shown (in ml)
* **Requirement 9**: It shall be possible to toggle the visible 3D objects
  * **Requirement 9.1**: Original data
  * **Requirement 9.2**: Segmentation results
  * **Requirement 9.3**: All

Add a `SoExaminerViewer`, a `SoWEMRenderer` and an `IsoSurface` to your existing network and connect it to the `LocalImage`. Configure the `IsoSurface` to use an IsoValue of *200*, a Resolution of *1* and check *Auto-Update* and *Auto-Apply*.

![3D Viewer](/images/tutorials/summary/Example1_5.png "3D Viewer")

The result should be a 3-dimensional rendering of your image.

![SoExaminerViewer](/images/tutorials/summary/Example1_6.png "SoExaminerViewer")

{{<alert class="info" caption="Info">}}
If you do not see the rendering immediately, click *Apply* in your `IsoSurface` module.
{{</alert>}}

Define the field instanceName of your `IsoSurface` module as *IsoSurfaceImage* and add another `IsoSurface` to your network. Set the instanceName to *IsoSurfaceSegmentation* and connect the module to the output of the `CloseGap` module from the image segmentation. Set IsoValue to *420*, a Resolution of *1* and check *Auto-Update* and *Auto-Apply*.

Set instanceName of the `SoWEMRenderer` to *SoWEMRendererImage* and add another `SoWEMRenderer`. Set this instanceName to *SoWEMRendererSegmentation* and connect it to the *IsoSurfaceSegmentation*. Selecting the output of the new `SoWEMRenderer` shows the segmented parts as a 3D object in Output Inspector.

![Segmentation preview in Output Inspector](/images/tutorials/summary/Example1_7.png "Segmentation preview in Output Inspector")

Once again, we should group the modules used for 3D viewing and name the new group *3D Viewer*.

![Grouped network](/images/tutorials/summary/Example1_8.png "Grouped network")

We now want to allow the user to toggle the different 3D visualizations as defined by the requirements above. It shall be possible to show:
* Original data only
* Segmentation only
* Both

Add a `SoSwitch` to your network. Connect the switch to both of your `SoWEMRenderer` and to the `SoExaminerViewer`. 

![SoSwitch](/images/tutorials/summary/Example1_9.png "SoSwitch")

The default input of the switch is *None*. Your 3D viewer remains black. Using the arrows on the `SoSwitch` allows you to toggle between the segmentation and the image. Input 0 shows the segmented brain, input 1 shows the head. You are now able to toggle between them. A view with both objects is still missing.

{{< imagegallery 2 "/images/tutorials/summary" "Example1_Segmentation" "Example1_Image" >}}

Add a `SoGroup` and connect both `SoWEMRenderer` as input. The output needs to be connected to the right input of the `SoSwitch`. 

![SoGroup](/images/tutorials/summary/Example1_10.png "SoGroup")

You can now also toggle Input 2 of the switch showing both 3D objects. The only problem is: You cannot see the brain because it is located inside the head. Open the `SoWEMRendererImage` panel and set faceAlphaValue to *0.5*. The viewer now shows the head semi transparent and you can see the brain inside. Transparencies are difficult to render. You need to add a `SoDepthPeelRenderer` and connect it to the semi transparent `SoWEMRendererImage`. Set Layers of the renderer to *1*.

![SoDepthPeelRenderer](/images/tutorials/summary/Example1_Both.png "SoDepthPeelRenderer")

You have a 2D and a 3D viewer now. In the end, we want to define the colors of the overlay to be re-used for the 3D segmentation.

### Parameter connections for visualization
Open the panels of the `SoView2DOverlay` and the `SoWEMRendererSegmentation`. Draw a parameter connection from *SoView2DOverlay.baseColor* to *SoWEMRendererSegmentation.faceDiffuseColor*.

![Synchronized segmentation colors](/images/tutorials/summary/Example1_11.png "Synchronized segmentation colors")

Now the 3D visualization uses the same color as the 2D overlay.

## Summary
* You now built a network providing the basic functionalities of your application.
* Actions inside your application need to be executed by changing fields in your network or by manually touching a trigger.

{{< networkfile "examples/summary/Tutorial_Summary.mlab" >}}
