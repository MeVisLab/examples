---
title: "Introduction to MeVisLab"
date: 2022-06-15T08:56:33+02:00
draft: false
status: "OK"
weight: 310
tags: ["Tutorial", "Introduction", "Glossary", "Modules", "ML Module", "Filetypes", "UI", "Workspace", "Search"]
menu: 
  main:
    identifier: "tutorial_introduction"
    title: "Overview of MeVisLab Tutorials and general information about User Interface, modules, types of modules, searching for modules and Glossary including filetypes."
    weight: 310
    parent: "tutorials"
---

## Tutorial Introduction {#tutorial_introduction} 

Welcome to [MeVisLab](glossary/#mevislab)!

More than 20 years of experience and the continuous implementation of adaptations made MeVisLab one of
the most powerful development platforms for medical image processing.
Several applications and their prototypes are based on and could be realized because of
MeVisLab, including software assistants for neuro-imaging, dynamic image
analysis, surgery planning, and cardiovascular analysis.

MeVisLab is a development environment for rapid prototyping and product
development of medical and industrial imaging applications. It includes
a [*Software Development Kit (SDK)*](glossary/#mevislab-sdk) and an [*ApplicationBuilder*](glossary/#mevislab-apk) for deploying your applications to end-customers.

In turn, the *MeVisLab SDK* consists of an [*Integrated Development Environment (IDE)*](glossary/#mevislab-ide)
for visual programming and the advanced text editor [*MATE*](glossary/#mevislab-mate) for Python
scripting, providing code completion, debugging, profiling, and automated
test development as well as execution.

You can re-use thousands of pre-defined [*Modules*](glossary/#module) for image processing
(2D up to 6D images) and visualization, combine them, or even build your own.

A quick introduction on available modules and [example networks](glossary/#example-network) will be given in the following tutorials.

### Structure and Usage of Provided Tutorials

This tutorial is a hands-on training. You will learn about basic mechanics and
features of MeVisLab. 

Starting with this introduction, we will be leading you through all relevant aspects of the user interface,
commonly used functionalities, and provide you with all the basic knowledge you need to build your own web applications.

Additional information is accessible through embedded links, forwarding you to a related glossary entry or tutorial and shortcuts, advice and hints will be highlighted as shown [here](about/about/).

The tutorials are divided into chapters by their topic and each chapter contains at least one example for you to try.
You find them at the end of the tutorial or, also sorted by chapters, under the menu entry [Examples](examples/howto).
The examples under the designated menu entry are more suitable if you already have a little experience and rather search for inspiration than for explanations.  

### Starting MeVisLab for the First Time

Right after installation of MeVisLab, you will find some new icons on your Desktop (if selected during setup).

![MeVisLab Desktop Icons](images/tutorials/basicmechanics/WindowsIcons.png "MeVisLab Desktop Icons (Windows)")

Use the top middle icon to start the MeVisLab IDE. You can also start the integrated text editor MATE or the ToolRunner. For this tutorial, you will generally require the IDE.

{{<alert class="warning" caption="Warning">}}
Maybe postpone the usage of the *QuickStart* icons as they can cause created packages not to be loaded.
{{</alert>}}

### MeVisLab IDE User Interface {#tutorial_ide}

First, start the MeVisLab IDE. After the Welcome Screen, the standard user interface opens.

![MeVisLab IDE User Interface](images/tutorials/introduction/IDE1.png "MeVisLab IDE User Interface")

#### Workspace

By default, MeVisLab starts with an empty [workspace](glossary/#workspace). 

This is where you will be developing and editing networks. Essentially, networks form the base of all processing and visualization pipelines, so the workspace is where the visual programming is done. 

#### Views Area

The standard [Views Area](glossary/#views-area) contains the [Output Inspector and Module Inspector](./tutorials/basicmechanisms#The_Output_Inspector_and_the_Module_Inspector "Output Inspector and Module Inspector"). With the help of the Output Inspector, you can visualize the modules output.

{{<alert class="info" caption="Info">}}
Further information on each module, e.g., about [module parameters](glossary/#field), can be found using the [Module Inspector](glossary/#module-inspector).
{{</alert>}}

#### Debug Output

Debugging information can be found using the [Debug Output](glossary/#debug-output).

The MeVisLab IDE and its layout are completely configurable. You can
rearrange the items and add new views via {{< menuitem "Main Menu" "View" "Views" >}}.

### File Types Used in, for, and With MeVisLab

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:230px">Extension</div> | Description |
| --- | --- |
| `.mlab` | Network file, includes all information about the networks modules, their settings, their connections, and module groups. Networks developed using the `MeVisLab SDK` are stored as *.mlab* files and can only be opened having a valid SDK license. |
| `.def` | Module definition file, necessary for a module to be added to the common MeVisLab module database. May also include all MDL script parts (if they are not sourced out to the *.script* file). |
| `.script` | `MDL` script file, typically includes the user interface definition of panels. See [Chapter GUI Development](./tutorials/basicmechanisms/macromodules/guidesign#Example_Paneldesign "GUI Development") for an example on GUI programming. |
| `.mlimage` | MeVisLab internal image format for 6D images saved with all DICOM tags, lossless compression, and in all data types. |
| `.mhelp` | File with descriptions of all fields and possible use cases of a module, edit- and creatable by using `MATE`. See [Help files](./tutorials/basicmechanisms/macromodules/helpfiles "Help files") for details. |
| `.py` | Python file, used for scripting in macro modules. See [Python scripting](./tutorials/basicmechanisms/macromodules/pythonscripting#TutorialPythonScripting "Python scripting") for an example on macro programming. |
| `.dcm` | DCM part of the imported DICOM file, see [Importing DICOM Data](./tutorials/basicmechanisms/dataimport#DICOMImport "Importing DICOM Data"). |
{{< /bootstrap-table >}}

### Module Types {#Module_Types}

{{<alert class="info" caption="Info">}}
[Modules](glossary/#module) are the basic entities the MeVisLab concept is built upon. <br>
They provide the functionalities to process, display, and interact with images.
{{</alert>}}

The three existing module types (ML, [Open Inventor](glossary/#open-inventor), and [macro module](glossary/#macro-module)) can be distinguished by their colors:

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:230px">Type</div> | <div style="width:430px">Appearance</div> | Characteristics |
| --- | --- | --- |
| ML module (blue) | ![ML module](images/tutorials/introduction/MLMModuleML.png "ML module") | Page-based, demand-driven processing of voxels. |
| Open Inventor module (green) | ![Open Inventor module](images/tutorials/introduction/MLMModuleSo.png "Open Inventor module") | Visual scene graphs (3D). Usually starting with *So* (for **S**cene **o**bject) as a naming convention. |
| Macro module (brown) | ![Macro module](images/tutorials/introduction/MLMModuleMacro.png "Macro module") | Combination of other module types, allowing the implementation of hierarchies and scripted interaction. |
{{< /bootstrap-table >}}

### Invalid Modules

If a module is invalid, it is displayed in bright red. This might happen if the module itself is not available for your system.

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:330px">Appearance</div> | Explanation |
| --- | --- |
| ![Invalid module](images/tutorials/introduction/MLMModuleStateInvalid.png "Invalid module") | Invalid module |
  ![Macro State Invalid](images/tutorials/introduction/MLMModuleStateMacroInvalidModule.png "Macro State Invalid") | Macro containing an invalid module |
{{< /bootstrap-table >}}

As you can see, the number of warning and error messages that are being printed to the
debug console are listed in the upper right corner of the module. This is intentional, as it enables the developer to quickly find the module causing the errors. 

{{<alert class="check" caption="Check">}}
Once the debug console is cleared, the warning and error indicators next to the
module are also cleared.
{{</alert>}}

Informational messages are indicated in a similar manner on the same spot, but in a subtle gray color.

### Module Interactions Through the Context Menu
Each module has a context menu, providing the following options:

![Context Menu of a module](images/tutorials/introduction/ModuleContextMenu.png "Context Menu of a module")

* **Show Internal Network:** [Macro modules](glossary/#macro-module) provide an entry to open the internal network. You can see what happens inside a macro module. The internal network may also contain other macro modules.
* **Show Window:** If a module does not provide a User Interface, you will see the automatic panel showing the module's name. Modules may additionally have one or more windows that can be opened. You can also open the Scripting Console of a module to integrate Python.
* **Instance Name:** You can edit or copy the instance name. Renaming can be useful if the same module appears more than once in one network and/or if you want to access and distinguish the modules in your Python script. 
* **Help:** The menu entry Help provides access to the Module Help pages and to an example network where the module is used. This example network often helps to understand which additional modules can be added to create your desired effect.
* **Extras:** Automated tests written for the specific module can be executed here. You can also run this module in a separate process.
* **Reload Definition:** In the case you are currently working on a module, you may need to reload the definition so that your changes are applied on the module (for example, attached Python scripts).
* **Related Files:** Related files allows a quick access to the modules *.script* or *.py* files. The files are automatically opened in [MATE](glossary/#mevislab-mate) for editing.
* **Show Enclosing Folder:** This entry opens the directory where your module is stored.
* **Grouping:** Multiple modules can be clustered and the groups can be named. This adds clarity to the structure of your network. In addition to that, grouped modules can be converted to local or global macro modules easily.

### Input and Output Connectors {#Module_Connectors}
As the creation of a network requires connected modules, each module has input and output connectors, located on their top and bottom side. Data is transmitted from the output connector on the top side of one module to the input connector on another module's bottom side.

Once again, three types can be distinguished:

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:330px">Appearance</div> | <div style="width:130px">Shape</div> | Definition |
| --- | --- | --- |
| ![Triangle](images/tutorials/introduction/MLMConnectorTriangle.png "Triangle - ML Image") | triangle | ML images |
| ![Circle](images/tutorials/introduction/MLMConnectorHalfCircle.png "Circle - Inventor Scene") | half-circle | Inventor scene |
| ![Square](images/tutorials/introduction/MLMConnectorSquare.png "Square - Base Object") | square | Base objects: Pointers to data structures |
{{< /bootstrap-table >}}

{{<alert class="info" caption="Info">}}
A connection can be established by dragging one module close to the other. 
{{</alert>}}

Some modules even contain hidden connectors in addition to the ones displayed on the module's surface. Click on the workspace and press {{< keyboard "SPACE" >}} to see the hidden connectors as well as the internal networks of each macro module. You can now also use the hidden connectors for building connections.

For more information about connectors and different types of connections, click {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s03.html" "here" >}}. <br>
If you want to know more about establishing, removing, moving, and replacing connections, have a look at {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s04.html" "this." >}}

### Parameter Connections
Besides through a module's input and output connectors, connections can also be established between parameters in the module's panel. 

{{<alert class="check" caption="Check">}}
An exemplary use case for a parameter connection is synchronization. Have a look [here](tutorials/basicmechanisms/#TutorialParameterConnection).
{{</alert>}}

### Macro Modules {#Macro_Modules}

{{<alert class="info" caption="Info">}}
The creation of macros is explained in more detail in [Tutorial Chapter I - Example 2.2](tutorials/basicmechanisms/macromodules/globalmacromodules) 
{{</alert>}}

### Adding Modules to your Workspace {#Searching_and_Adding_Modules}

There are several ways to add a module to your current network:
-   via the menu bar entry {{< menuitem "Modules" >}}
-   via {{< menuitem "Quick Search" >}}
-   via the View Module Search
-   via the View Module Browser
-   via copy and paste from another network
-   by scripting, see the {{< docuLinks "/Resources/Documentation/Publish/SDK/ScriptingReference/index.html" "Scripting Reference" >}}

Both the menu entry{{< menuitem "Modules" >}} and the Module Browser display all available modules. The modules are sorted hierarchically by topic and name, as defined in the file `Genre.def`.

Therefore, both places are a good starting point when in need of a specific function, like an `ImageLoad` module.

![Modules Menu and Module Browser](images/tutorials/introduction/GSExampleNetworkViewImage01c.png "Modules Menu and Module Browser")

The advantage of the Module Browser is that you can right-click {{< mousebutton "right" >}} the
entries, open the context menu and, for example, open the help (in your
default Internet browser) or the module files (in MATE, the built-in
text editor).

{{<alert class="check" caption="Check">}}
For a module to be listed, it has to be available in the [SDK](glossary/#mevislab-sdk) or in your self-defined 
[packages](glossary/#package). A detailed tutorial on how to create packages can be found [here](tutorials/basicmechanisms/macromodules/package/). If in doubt or missing something, check out the loaded packages in the preferences. 
{{</alert>}}

Usually the quickest way to add modules to a network is the quick search in the menu bar. It offers the possibility to search for modules by module name. By default, the search will also be extended to keywords and substrings and is case-insensitive. To change these settings, click the magnifier button for the search options.

![Quick Search Options](images/tutorials/introduction/MLMQuickSearch.png "Quick Search Options")

{{<alert class="info" caption="Info">}}
Any time you enter something in the MeVisLab GUI while not focussing a dialog window, your entry will be put into the quick search automatically.
{{</alert>}}

 Use the {{< keyboard "ArrowUp" >}} and {{< keyboard "ArrowDown" >}} keys on your keyboard to move to one of the listed modules. The module's decription will appear next to it, allowing you to decide if this is the right module for your use case.

![Quick Search Results](images/tutorials/introduction/GSExampleNetworkViewImage02.png "Quick Search Results")

{{<alert class="info" caption="Tip">}}
For a more complex search, use the Module Search View.
{{</alert>}}