---
title: "Chapter I: Basic Mechanisms of MeVisLab"
date: 2022-06-15T08:54:53+02:00
status: "OK"
draft: false
weight: 350
tags: ["Beginner", "Tutorial", "Macro", "Macro Modules", "Local Macro"]
menu: 
  main:
    identifier: "basicmechanisms"
    title: "Examples explaining the basic mechanisms of MeVisLab like using Modules and connecting them to Networks for viewing images."
    weight: 350
    parent: "tutorials"
---

# MeVisLab Tutorial Chapter I {#TutorialChapter1}

{{< youtube "hRspMChITE4">}}

## Basic Mechanics of MeVisLab (Example: Building a Contour Filter) {#TutorialBasicMechanics}

In this chapter you will learn the basic mechanics of the MeVisLab IDE. You will learn how to re-use existing Modules to load and view data, and you will build your first processing pipeline.

{{<alert class="info" caption="Extra Infos">}}
Additional information about the basics of MeVisLab are explained {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/index.html" "here">}}
{{</alert>}}

[//]: <> (MVL-651)

### Loading Data {#TutorialLoadingData}
 
First, we need to load the data we like to work on. In MeVisLab, you usually use modules to perform specific tasks. Modules are the basic entities you will be working with. Each module has a specific functionality for processing, visualization and interaction. Connecting these modules enables the development of complex processing pipelines. You will get to know different types of modules throughout the course of this tutorial.

By now, we will load our data by using the module `ImageLoad`. You can find this module via search and add it to your Workspace.

![Search for ImageLoad](/images/tutorials/basicmechanics/BM_01.png "Search for ImageLoad")

As a next step, we like to select and load the data we like to process. Double-click the Module `ImageLoad` to open its Panel. Now, you can browse through your folders to select the data you like to open. You can find example data in the MeVisLab DemoData directory *$(InstallDir)/Packages/MeVisLab/Resources/DemoData* located in the MeVisLab installation path. Select a file, for example an MRI scan of a shoulder *Shoulder_Fracture.tif*. The image is loaded immediately and basic information of the loaded image can be seen in the Panel.

{{<alert class="info" caption="Extra Infos">}}
Multiple additional Modules for loading data are available such as:
* `DicomImport` for loading DICOM Images
* `LocalImage` for loading any image format
 
For details about loading DICOM images, see {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch03.html" "here">}}

{{</alert>}}

[//]: <> (MVL-651)

### The Output-Inspector and the Module Inspector {#The_Output_Inspector_and_the_Module_Inspector}

For a first inspection and visualization of the loaded data, we can use the Output Inspector located in the {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch04s09.html" "Views" >}} area. You can already interact with the image via Mouse-Wheel {{< mousebutton "middle" >}} and Mouse Buttons {{< mousebutton "left" >}} / {{< mousebutton "right" >}}. To preview the image, click on the triangle on the top side of the module `ImageLoad`, which offers the module output. All module outputs can be found at the top side of the respective module. 

You can now inspect your image in 2D.

[//]: <> (MVL-653 when reworking the Manual, add an anchor to the 4.9.8. Views on this page and create a reference directly to this part on the page, as this is more suitable ) 

![Output Inspector](/images/tutorials/basicmechanics/BM_03.png "Output Inspector")

Your image does not look like this? One reason might be that the slice of the image you are looking at has no information. Click on the Output Inspector and scroll through the slices (slicing) by using the mouse wheel {{< mousebutton "middle" >}}. Still not seeing anything? Then try to adjust the contrast of the given image by keeping the right mouse button {{< mousebutton "right" >}} pressed while moving the mouse.

You are not restricted to only see your image in 2D. The Output Inspector offers a 3D View of the selected data. For this, click on the tab 3D of the Output Inspector. The 3D view of the image can be rotated by left-clicking on the image and moving the courser around. The little cube in the lower right corner of the viewer shows the orientation of the image.

{{<alert class="info" caption="Notation">}}
* A = anterior, front
* P = posterior, back
* R = right side
* L = left side
* H = head
* F = feet
{{</alert>}}

Below the Output Inspector, you can find the Module Inspector. The Module Inspector displays properties and parameters of the selected module. Parameters are stored in so called **Fields**. Using the Module Inspector you can examine different fields of the module `ImageLoad`. The module has for example the fields *filename* (the path, the loaded image is stored in) and *sizeX*, *sizeY*, *sizeZ* (the size of the loaded image).

![Module Inspector](/images/tutorials/basicmechanics/BM_04.png "Module Inspector")

### Viewer {#TutorialViewer}

Instead of using the Output Inspector to inspect images, it is sensible to add a viewer to the network. Search for the module `View2D` and add it to your workspace. Most modules have different connectors. Data were transmitted via output connectors on the top side of a module and can be received by other modules via input connectors on the bottom side of the module.

The module `View2D` has one input connector for the voxel-images on the bottom side (triangle) and three other possible inputs (half-circles), which will be explained later on. In general, module outputs can be connected to module inputs with the same symbol and thus transmit information and data between modules.

![2D Viewer](/images/tutorials/basicmechanics/BM_05.png "2D Viewer")

You can now add the loaded image to the viewer by connecting the image output of the module `ImageLoad` with the image input of the module `View2D`. This is done as follows:

1.  Click the output connector of `ImageLoad`.

2.  Keep the left mouse button {{< mousebutton "left" >}} pressed while dragging the connection to the input connector of `View2D` (white line).

3.  Check that the connection is well-defined (green line).

4.  At the input connector of `View2D`, release the mouse button and establish the connection (blue line).

![Establish connection](/images/tutorials/basicmechanics/BM_06.png "Establish connection")

Although the connection is established, no image rendering has started yet. To initialize rendering, open the `View2D` panel by double-clicking the module `View2D` in your network. Similar to the Output Inspector, you can scroll through the slices and change the contrast. By pressing the {{< keyboard "A" >}} you can switch the annotation mode.

![View2D Panel](/images/tutorials/basicmechanics/BM_07.png "View2D Panel")

You can also disconnect the Modules by dragging the connection away from the input or output connector of the Modules.

Connections between compatible outputs and inputs are established automatically in case 2 Modules are moved close enough to each other.

{{<alert class="info" caption="Extra Infos">}}
Connecting, Disconnecting, Moving and Replacing Connections is explained {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s04.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-653)

### Image Processing {#TutorialImageProcessing}

Next, we like to add a processing step to our network. We like to smooth the image using an average kernel. In order to do that, search for the module `Convolution` and add it to the workspace. Delete the established connection from the module `ImageLoad` to the module `View2D` by clicking on the connection and pressing {{< keyboard "DEL" >}}. Now, you can build new connections from the module `ImageLoad` to the module `Convolution` and from this module to `View2D`.

![Convolution Module](/images/tutorials/basicmechanics/BM_08.png "Convolution Module")

Double-click the module `Convolution` to open its panel. The panel allows configurations of the module. You can adjust parameters or in this case select a kernel, for example the *3x3 Avarage Kernel*.

![Select a Kernel](/images/tutorials/basicmechanics/BM_09.png "Select a Kernel")

The module `View2D` is now displaying the smoothed image.

To see the difference between the processed and the unprocessed image, click on the output of the module `ImageLoad` to view the original image in the Output Inspector. The great thing about the Output Inspector is that it can display the output of any connector in the process chain (as long as a format is used, the inspector can interpret). Simply click the connector or connection to find out more about the module output.

There is another way of inspecting the difference between the processed and the unprocessed image. Add a second viewer module `View2D` to your workspace. The new module gets a different name: `View2D1`. It is possible to establish numerous connections from one module output to different other module inputs, but a module input can only receive one connection. Connect the module `ImageLoad` to the second viewer to display two images at the same time. You can scroll through the slices of both viewers and inspect the images.

![Multiple Viewer](/images/tutorials/basicmechanics/BM_10.png "Multiple Viewer")

### Parameter Connection for Synchronization {#TutorialParameterConnection}

In our example you can scroll through the slices of both viewers independently. To inspect the effect of the filter, it would be helpful to synchronize both viewers in a way, that both show the same slices.

We already know data connections between module inputs and outputs. Besides module connections, it is also possible to connect module fields via a parameter connection. The values of connected fields are synchronized, that means when changing the value of one field, all fields connected to this field will be adapted to the same value.

In this chapter we like to establish parameter connections to allow the synchronized use of both image viewers.  In order to do that, search for the module `SyncFloat` and add it to your workspace.

![SyncFloat Module](/images/tutorials/basicmechanics/BM_11.png "SyncFloat Module")

We like to synchronize the field *startSlice* of both viewers, to be able to show the same slice in both viewers simultaneously.

First, right-click the viewer `View2D` to open its context menu and select {{< menuitem "Show Window" "Automatic Panel" >}}.

![Automatic Panel View2D](/images/tutorials/basicmechanics/BM_12.png "Automatic Panel View2D")

This option shows all parameter fields of the module `View2D`.

Search for the field *startSlice*. The field indicates which slice is currently shown in the Viewer. If you scroll through the slices of an image the value of *startSlice* changes.

Now, double-click the module `SyncFloat` to open its panel.

Click on the label *startSlice* in the automatic panel of the module `View2D`, keep the button pressed and drag the connection to the label *Float1* in the panel of the module `SyncFloat`.

![Synchronize StartSlice](/images/tutorials/basicmechanics/BM_13.png "Synchronize StartSlice")

The connection is drawn as a thin grey arrow between both modules with the arrowhead pointing to the module that receives the field value as input. The value of the field *starSlice* is now transmitted to the field *Float1*. Changing *StartSlice* automatically changes *Float1*, but not the other way round.

![Parameter Connection StartSlice](/images/tutorials/basicmechanics/BM_14.png "Parameter Connection StartSlice")

We now like to establish a connection from the module `SyncFloat` to the second viewer, `Viewer2D1`. In order to do that, open the automatic panel `View2D1`. Draw a connection from the label `Float2` of the panel of the module `SyncFloat` to the label *startSlice* in the automatic panel of the module `View2D1`. At last, implement a connection between the parameter fields *startSlice* of both viewers. Draw the connection from `View2D1` to `View2D`.

![Synchronize both directions](/images/tutorials/basicmechanics/BM_15.png "Synchronize both directions")

As a result, scrolling through the slices with the mouse wheel {{< mousebutton "middle" >}} in one of the viewers synchronizes the rendered slice in the second viewer. In this case, you can inspect the differences between smoothed and unsmoothed data on every single slice.

![Your final Network](/images/tutorials/basicmechanics/BM_16.png "Your final Network")

You can also use the pre-defined Module `SynchroView2D` to reach the same goal (shown in [this chapter](/tutorials/visualization/visualizationexample1/) ).

### Grouping Modules {#TutorialGroupingModules}

In this chapter we like to create a contour filter. To finalize the filter, add the modules `Arithmetic2` and `Morphology` to your workspace and connect the modules as shown below. Double-click the module `Arithmetic2` to open its panel. Change the field *Function* of the module `Arithmetic2` to use the function *subtract* in the panel of the module. With this, we finished our contour filter. You can inspect each processing step using the Output Inspector by clicking on the input and output connectors of the respective modules. The final results can be inspected using the viewers. If necessary, adjust the contrast by pressing the right-key and moving the cursor.

![Grouping Modules](/images/tutorials/basicmechanics/BM_17.png "Grouping Modules")

If you like to know more information about each module, search for help. You can do this by right-clicking the module and select help, which offers an example network and further information about this module.

![Module Help](/images/tutorials/basicmechanics/BM_18.png "Module Help")

To distinguish the image processing pipeline, you can create a group for it. For that: Select the three modules, for example by dragging a selection rectangle around them. Right-click the selection to open the context menu and select {{< menuitem "Add to New Group" >}}.

![Add Modules to new Group](/images/tutorials/basicmechanics/BM_19.png "Add to new Group")

Enter a name for the new group, for example *Filter*. The new group is created and displayed as a green rectangle. The group allows for quick interactions with all its modules together.

![Your Filter Group](/images/tutorials/basicmechanics/BM_20.png "Your Filter Group")

Your network gets very complex and you lost track? No problem. Let MeVisLab arrange your modules automatically via {{< menuitem "Mein Menu" "Edit" "Auto Arrange Selection" >}} (or via keyboard shortcut {{< keyboard "CTRL" "1" >}}).

Now, it is time to save your first network. Open the tab {{< menuitem "File" "Save" >}} to save the network in an *.mlab* file.

{{<alert class="info" caption="Extra Infos">}}
More information on module groups can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s11.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-653)

### Macro-Modules {#TutorialMacroModules}

We now like to condense our filter into one single module. You have probably already noticed, that the modules have different colors. Each color represents a special type of modules. The blue modules are called ML-Modules and are responsible for the processing of voxel-images. The brown modules are called macro modules. Macro modules encapsulate a whole network in a single module. You can right-click on one macro-module to open the context menu and select *Show Internal Network* to see the internal network structure. In addition, macro modules enable the implementation of custom functionalities via python scripting.

We now like to condense the modules forming the contour filter into one single macro module. To do that, right-click on the group-title and select *Convert To Local Macro*. Now, you need to select a name for your macro module and finish the creation of the module. With this you create a local macro module. Local macro modules can only be used in your current network.

![Convert to Local Macro](/images/tutorials/basicmechanics/BM_21.png "Convert to Local Macro")
![Your first Local Macro](/images/tutorials/basicmechanics/BM_22.png "Your first Local Macro")

Right-click the macro module and select *Show Internal Network* to inspect and change the internal network. You can change the properties of the new macro module by changing the properties in the internal network. As before, you can for example right-click the module `Convolution` and change the Kernel. These changes will be preserved.

![Internal Network of your Local Macro](/images/tutorials/basicmechanics/BM_23.png "Internal Network of your Local Macro")

{{< youtube "VmK6qx-vKWk">}}

{{<alert class="info" caption="Extra Infos">}}
Module handling is explained {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s09.html" "here" >}}
More information about Marco Modules can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch09.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-651)

## Summary
* MeVisLab provides pre-defined Modules you can re-use and connect for building more or less complex networks.
* Each Module output can be previewed by using the Output Inspector.
* Each Module provides Example Networks to explain their usage.
* Parameters of each Module can be changed in the Module Inspector or Automatic Panel of the Module.
* Parameter connections can be established to synchronize the values of these parameters.
* Modules can be grouped. Grouped Modules can be encapsulated to Macro Modules.
* Macro Modules encapsulate networks. Internal networks can be shown and modified. Any changes of the internal network are applied to the Macro Module.

{{< networkfile "examples/basic_mechanisms/contour_filter/ContourFilter.zip" >}}
