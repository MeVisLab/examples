---
title: "Chapter I: Basic Mechanisms of MeVisLab"
date: 2022-06-15T08:54:53+02:00
status: "OK"
draft: false
weight: 350
tags: ["Beginner", "Tutorial", "Macro", "Macro modules", "Local Macro"]
menu: 
  main:
    identifier: "basicmechanisms"
    title: "Examples Explaining the Basic Mechanisms of MeVisLab Such as Using Modules and Connecting Them to Networks for Viewing Images"
    weight: 350
    parent: "tutorials"
---

## Basic Mechanisms of MeVisLab (Example: Building a Contour Filter) {#TutorialBasicMechanics}
In this chapter you will learn the basic mechanisms of the MeVisLab IDE. You will learn how to reuse existing modules to load and view data, and you will build your first processing pipeline.

{{< youtube "hRspMChITE4">}}

{{<alert class="info" caption="Extra Infos">}}
Additional information on the basics of MeVisLab are explained {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/index.html" "here">}}
{{</alert>}}

[//]: <> (MVL-651)

### Loading Data {#TutorialLoadingData}
First, we need to load the data we would like to work on, e.g., a CT scan. In MeVisLab, modules are used to perform their associated specific task: they are the basic entities you will be working with. Each module has a different functionality for processing, visualization, and interaction. Connecting modules enables the development of complex processing pipelines. You will get to know different types of modules throughout the course of this tutorial.

Starting off, we will add the module `ImageLoad` to our network to load our data. The module can be found by typing its name into the search bar on the top-right corner and is added to your network by clicking it.

![Search for ImageLoad](images/tutorials/basicmechanics/BM_01.png "Search for ImageLoad")

Next, we select and load the data we'd like to process. Double-click the module `ImageLoad` to open its panel. You can browse through your folders to select the data you'd like to open. Example data can be found in the MeVisLab DemoData directory *$(InstallDir)/Packages/MeVisLab/Resources/DemoData* located in the MeVisLab installation path. Select a file, for example, an MRI scan of a shoulder *Shoulder_Fracture.tif*. The image is loaded immediately and basic information of the loaded image can be seen in the Panel.

{{<alert class="info" caption="Extra Infos">}}
There also are modules to load multiple other formats of data. These are the most common ones:
* `DicomImport` to load DICOM Images
* `LocalImage` to load any image format
 
For a more detailed description on loading DICOM images, see {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch03.html" "here">}}

{{</alert>}}

[//]: <> (MVL-651)

### The Output Inspector and the Module Inspector {#The_Output_Inspector_and_the_Module_Inspector}
To inspect and visualize the loaded data, we can use the Output Inspector located in the {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch04s09.html" "Views" >}} area. You can already interact with the image using the mouse wheel {{< mousebutton "middle" >}} and mouse buttons {{< mousebutton "left" >}} / {{< mousebutton "right" >}}. To preview the image, click on the triangle on the top side of the module `ImageLoad`, which offers the module's output. All module outputs can be found at the top side of the respective module. 

You can now inspect your image in 2D:

[//]: <> (MVL-653 when reworking the Manual, add an anchor to the 4.9.8. Views on this page and create a reference directly to this part on the page, as this is more suitable ) 

![Output Inspector](images/tutorials/basicmechanics/BM_03.png "Output Inspector")

Your image does not look like this? One reason might be that the slice of the image you are looking at has no information. Click on the Output Inspector and scroll through the slices (this process is called "Slicing") by using the mouse wheel {{< mousebutton "middle" >}}. Still not seeing anything? Then, try to adjust the contrast of the given image by keeping the right mouse button {{< mousebutton "right" >}} pressed while moving the mouse.

You are not restricted to 2D. The Output Inspector offers a 3D View of most loaded images. Try to click on the 3D tab located in the Output Inspector. The 3D display of the image can be rotated by left-clicking on the image and moving the courser around. The little cube in the lower right corner of the viewer shows the orientation of the image.

{{<alert class="info" caption="Notation">}}
* A = anterior, front
* P = posterior, back
* R = right side
* L = left side
* H = head
* F = feet
{{</alert>}}

Below the Output Inspector, you'll find the Module Inspector. The Module Inspector displays properties and parameters of the selected module. Parameters are stored in so called **Fields**. Using the Module Inspector, you can examine different fields of your `ImageLoad` module. The module has, for example, the fields *filename* (the path the loaded image is stored in), as well as *sizeX*, *sizeY*, and *sizeZ* (the extent of the loaded image).

![Module Inspector](images/tutorials/basicmechanics/BM_04.png "Module Inspector")

### Viewer {#TutorialViewer}
Instead of using the Output Inspector to inspect images, we'd suggest to add another viewer to the network. Search for the module `View2D` and add it to your workspace. Most modules have different connector options. Data is generally transmitted from the top side of a module to another modules bottom side.

The module `View2D` has one input connector for voxel images (triangle-shaped) and three other possible input connectors (shaped like half-circles) on the bottom. The half-circle-shaped input connectors will be explained later on. Generally, module outputs can be connected to module inputs with the same symbol and thus transmit information and data between those modules.

![2D Viewer](images/tutorials/basicmechanics/BM_05.png "2D Viewer")

You can now display the loaded image in the newly added viewer module by connecting the output of the module `ImageLoad` to the input connector of the module `View2D`. Follow these steps to do so:

1.  Click the output connector of `ImageLoad`.

2.  Keep the left mouse button {{< mousebutton "left" >}} pressed while dragging the connection to the input connector of `View2D` (white line).

3.  Check if the connection is well-defined (green line).

4.  Release the mouse button on the input connector of your `View2D` module to establish the connection. 

![Establish connection](images/tutorials/basicmechanics/BM_06.png "Establish connection")

Although the connection is established, no image rendering has started yet. To initialize rendering, open the `View2D` panel by double-clicking on the module. Similar to the Output Inspector, you can scroll through the slices and set different levels of contrast. The amount of displayed annotations is altered by pressing {{< keyboard "A" >}} on the keyboard (annotation-mode).

![View2D Panel](images/tutorials/basicmechanics/BM_07.png "View2D Panel")

By dragging the connection away from either the input or the output connector, the connection is interrupted.

Connections between compatible outputs and inputs are established automatically if two modules get close enough to each other.

{{<alert class="info" caption="Extra Infos">}}
Connecting, Disconnecting, Moving, and Replacing Connections is explained in more detail {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s04.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-653)

### Image Processing {#TutorialImageProcessing}
An average kernel will be used to smooth the image as our next step will be to actually process our image. Add the `Convolution` module to your workspace and disconnect the `View2D` module from the `ImageLoad` module by clicking on the connection and pressing {{< keyboard "DEL" >}}. Now, you can build new connections from the module `ImageLoad` to the module `Convolution` and the `Convolution` module to `View2D`.

![Convolution Module](images/tutorials/basicmechanics/BM_08.png "Convolution Module")

Open the panel of the `Convolution` module by double-clicking it. The panel allows configuration of the module. You can adjust parameters or select a kernel. We will be using the *3x3 Average Kernel* for now.

![Select a Kernel](images/tutorials/basicmechanics/BM_09.png "Select a Kernel")

The module `View2D` is now displaying the smoothed image.

To compare the processed and unprocessed image, click on the output connector of the module `ImageLoad` to display the original image in the Output Inspector. The Output Inspectors greatest advantage is that it's able to display the output of any connector in the process chain (as long as an interpretable format is used). Simply click the connector or connection to find out more about the module's output.

You can also inspect changes between processed (output connector) and unprocessed (input connector) images by adding a second or even third viewer to your network. "Layers" of applied changes can be inspected next to each other using more than one viewer and placing as well as connecting them accordingly. We will be using a second `View2D` module. Notice how the second viewer is numbered for you to be able to distinguish them better. It might be important to know at this point that numerous connections can be established from one output connector but an input connector can only receive one stream of data. Connect the module `ImageLoad` to the second viewer to display the images twice. You can now scroll through the slices of both viewers and inspect the images.

![Multiple Viewers](images/tutorials/basicmechanics/BM_10.png "Multiple Viewers")

### Parameter Connection for Synchronization {#TutorialParameterConnection}
You're now able to scroll through the slices of the image in two separate windows. To examine the effect of the filter even better, we will now synchronize both viewers.

We already know data connections between module inputs and outputs. Besides module connections, it is also possible to connect the fields within the panels of the modules via parameter connection. The values of connected fields are synchronized, which means that the changing value of one field will be adapted to all other connected fields.

In order to practice establishing parameter connections, add the `SyncFloat` module to your workspace.

![SyncFloat Module](images/tutorials/basicmechanics/BM_11.png "SyncFloat Module")

We will be synchronizing the *startSlice* fields of our viewers to be able to directly compare the effect our processing module has on the slices:
Right-click the viewer `View2D` to open its context menu and select {{< menuitem "Show Window" "Automatic Panel" >}}.

![Automatic Panel View2D](images/tutorials/basicmechanics/BM_12.png "Automatic Panel View2D")

Doing so shows all parameter fields of the module `View2D`.

Search for the field *startSlice*. The field indicates which slice is currently shown in the viewer. If you scroll through the slices of an image, the value of *startSlice* changes.

Now, double-click the module `SyncFloat` to open its panel.

Click on the label *startSlice* in the automatic panel of the module `View2D`, keep the button pressed, and drag the connection to the label *Float1* in the panel of the module `SyncFloat`.

![Synchronize StartSlice](images/tutorials/basicmechanics/BM_13.png "Synchronize StartSlice")

The connection is drawn as a thin gray arrow between both modules with the arrowhead pointing to the module that receives the field value as input. The value of the field *startSlice* is now transmitted to the field *Float1*. Changing *startSlice* automatically changes *Float1*, but not the other way round.

![Parameter Connection StartSlice](images/tutorials/basicmechanics/BM_14.png "Parameter Connection StartSlice")

We will now establish a connection from the module `SyncFloat` to the second viewer, `Viewer2D1`. In order to do that, open the automatic panel `View2D1`. Draw a connection from the label `Float2` of the panel of the module `SyncFloat` to the label *startSlice* in the automatic panel of the module `View2D1`. Lastly, implement a connection between the parameter fields *startSlice* of both viewers. Draw the connection from `View2D1` to `View2D`.

![Synchronize both directions](images/tutorials/basicmechanics/BM_15.png "Synchronize both directions")

As a result, scrolling through the slices with the mouse wheel {{< mousebutton "middle" >}} in one of the viewers synchronizes the rendered slice in the second viewer. In this case, you can inspect the differences between smoothed and unsmoothed data on every single slice.

![Your final Network](images/tutorials/basicmechanics/BM_16.png "Your final Network")

It is also possible to use the predefined module `SynchroView2D` to accomplish a similar result.(`SynchroView2D`'s usage is described in more detail in [this chapter](tutorials/visualization/visualizationexample1/) ).

### Grouping Modules {#TutorialGroupingModules}
A contour filter can be created based on our previously created network. To finalize the filter, add the modules `Arithmetic2` and `Morphology` to your workspace and connect the modules as shown below. Double-click the module `Arithmetic2` to open its panel. Change the field *Function* of the module `Arithmetic2` to use the function *subtract* in the panel of the module. The contour filter is done now. You can inspect each processing step using the Output Inspector by clicking on the input and output connectors of the respective modules. The final results can be displayed using the viewer modules. If necessary, adjust the contrast by pressing the right mouse button and moving the cursor.

![Grouping modules](images/tutorials/basicmechanics/BM_17.png "Grouping modules")

If you'd like to know more about specific modules, search for help. You can do this by right-clicking the module and select help, which offers an example network and further information about the selected module in particular.

![Module Help](images/tutorials/basicmechanics/BM_18.png "Module Help")

To be able to better distinguish the image processing pipeline, you can encapsulate it in a group: select the three modules, for example, by dragging a selection rectangle around them. Then, right-click the selection to open the context menu and select {{< menuitem "Add to New Group" >}}.

![Add modules to new group](images/tutorials/basicmechanics/BM_19.png "Add to new group")

Enter a name for the new group, for example, *Filter*. The new group is created and displayed as a green rectangle. The group allows for quick interactions with all its modules.

![Your Filter Group](images/tutorials/basicmechanics/BM_20.png "Your Filter Group")

Your network got very complex and you lost track? No problem. Let MeVisLab arrange your modules automatically via {{< menuitem "Mein Menu" "Edit" "Auto Arrange Selection" >}} (or via keyboard shortcut {{< keyboard "CTRL" "1" >}}).

Now, it is time to save your first network. Open the tab {{< menuitem "File" "Save" >}} to save the network in an *.mlab* file.

{{<alert class="info" caption="Extra Infos">}}
More information on module groups can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s11.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-653)

### Macro Modules {#TutorialMacroModules}
You have probably already noticed how the modules differ in color. Each color represents another type of module:
  
  * Blue modules are called ML modules: they process voxel images. 
  * Green modules are Open Inventor modules: they enable visual 3D scene graphs. 
  * Brown modules are called macro modules. Macro modules encapsulate a whole network in a single module. 
  
To condense our filter into one single module, we will now be creating a macro module out of it. To do that, right-click on the group's title and select *Convert To Local Macro*. Name your new macro module and finish. You just created a local macro module. Local macros can only be used from networks in the same or any parent directory.

![Convert to local macro](images/tutorials/basicmechanics/BM_21.png "Convert to local macro")
![Your first local macro](images/tutorials/basicmechanics/BM_22.png "Your first local macro")

Right-click the macro module and select *Show Internal Network* to inspect and change the internal network. You can change the properties of the new macro module by changing the properties in the internal network. You can, for example, right-click the module `Convolution` and change the kernel. These changes will be preserved.

![Internal Network of your local macro](images/tutorials/basicmechanics/BM_23.png "Internal Network of your local macro")

{{< youtube "VmK6qx-vKWk">}}

{{<alert class="info" caption="Extra Infos">}}
Module handling is explained {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s09.html" "here" >}}
More information on macro modules can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch09.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-651)

## Summary
* MeVisLab provides predefined modules you can reuse and connect for building more or less complex networks.
* Each module's output can be previewed using the Output Inspector.
* Each module provides example networks to explain their usage.
* Parameters of each module can be changed in the Module Inspector or automatic panel of the module.
* Parameter connections can be established to synchronize the values of these parameters.
* Modules can be clustered. Clustered modules can be encapsulated into local or global macro modules.
* Macro modules encapsulate networks. Internal networks can be shown and modified. Any changes of the internal network are applied to the macro module.

{{< networkfile "examples/basic_mechanisms/contour_filter/ContourFilter.zip" >}}
