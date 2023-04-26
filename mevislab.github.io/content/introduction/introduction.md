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

# MeVisLab Tutorial {#tutorial_main}

## Introduction {#tutorial_introduction}

Welcome to [MeVisLab](/tutorials/glossary/#mevislab)!

MeVisLab is a development environment for rapid prototyping and product
development of medical and industrial imaging applications. It includes
a *Software Development Kit (SDK)* and an *ApplicationBuilder* for deploying
your applications to end-customers.

The *MeVisLab SDK* consists of an *Integrated Development Environment (IDE)*
for visual programming and the advanced text editor *MATE* for Python
scripting including code completion, debugging, profiling and automated
test development or execution.

You can re-use thousands of pre-defined *Modules* for image processing
(2D up to 6D images) and visualization. You will get a quick
introduction into the available modules and example networks in the following tutorials.

More than 20 years of experience and development made MeVisLab one of
the most powerful development platforms for medical image processing.
Several prototypes and applications have been realized on the basis of
MeVisLab, including software assistants for neuro-imaging, dynamic image
analysis, surgery planning, and cardiovascular analysis.

#### How to read this tutorial:

This tutorial is a hands-on training. You will learn basic mechanics and
features of MeVisLab. We will start by explaining the user interface and
end building our own web-applications. While reading the tutorial, open
the MeVisLab SDK and try to implement each step yourself. You will learn
new mechanics and possibilities in MeVisLab step-by-step. Additional
information and links are provided in colored boxes.

The tutorials are divided into chapters for a specific topic. Each chapter contains one or more example(s).

### Installation and first start
Right after installation of MeVisLab, you will find some new icons on your Desktop (if selected during setup).

![MeVisLab Desktop Icons](images/tutorials/basicmechanics/WindowsIcons.png "MeVisLab Desktop Icons (Windows)")

Use the top middle icon to start the MeVisLab IDE. You can also start the integrated text editor MATE or the ToolRunner. For this tutorial, you will generally require the IDE.

You can also use the *QuickStart* icons but any packages developed yourself during these tutorials will not be loaded, so you should not use this for now.

### MeVisLab IDE User Interface {#tutorial_ide}

First, start MeVisLab IDE. After the Welcome Screen, the standard user interface opens.

![MeVisLab IDE User Interface](/images/tutorials/introduction/IDE1.png "MeVisLab IDE User Interface")

#### Workspace

By default, MeVisLab starts with an empty workspace. The workspace is
the place for developing and editing Networks via visual programming.
Networks of modules form the basis for all processing and visualization
pipelines.

#### Views Area

The standard Views Area contains the [Output Inspector and Module Inspector](./tutorials/basicmechanisms#The_Output_Inspector_and_the_Module_Inspector "Output Inspector and Module Inspector"). With the help of the Output Inspector, you can visualize the modules output.

Further information of each module, like information about module parameters, can be found using the module Inspector.

#### Debug Output

In the Debug Output, you can find any debugging information about
your MeVisLab installation.

The MeVisLab IDE and the layout is completely configurable. You can
rearrange the items and add new views via {{< menuitem "Main Menu" "View" "Views" >}}.

### Filetypes in MeVisLab

Here a list of the most important file types:
{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:230px">Extension</div> | Description |
| --- | --- |
| `.mlab` | Network file, includes all information about the networks modules, their settings, their connections, and module groups. Networks developed by using the `MeVisLab SDK` are stored as `.mlab` file and can only be opened having a valid SDK license. |
| `.def` | Module definition file, necessary for a module to be added to the common MeVisLab module database. May also include all MDL script parts (if they are not sourced out to the `.script` file). |
| `.script` | `MDL` script file, typically includes the user interface definition for panels. See [Chapter GUI Development](./tutorials/basicmechanisms/macromodules/guidesign#Example_Paneldesign "GUI Development") for an example on GUI programming. |
| `.mlimage` | MeVisLab internal image format for 6D images saved with all DICOM tags, lossless compression, and in all data types. |
| `.mhelp` | File with descriptions of all fields and the use of a module, edit- and creatable by using `MATE`. See [Help files](./tutorials/basicmechanisms/macromodules/helpfiles "Help files") for details. |
| `.py` | Python file, used for scripting in macro modules. See [Python scripting](./tutorials/basicmechanisms/macromodules/pythonscripting#TutorialPythonScripting "Python scripting") for an example on macro programming. |
| `.dcm` | DCM part of the imported DICOM file, see [Importing DICOM Data](./tutorials/basicmechanisms/dataimport#DICOMImport "Importing DICOM Data"). |
{{< /bootstrap-table >}}

### Types of modules {#Module_Types}

Within the concept of MeVisLab the basic entities we are working with
a graphical representation of modules having their specific functions
for image processing, image visualization, and image interaction.

The three basic module types (ML, Open Inventor and Macro module) are
distinguished by their colors:

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:230px">Type</div> | <div style="width:430px">Look</div> | Characteristics |
| --- | --- | --- |
| ML module (blue) | ![ML module](/images/tutorials/introduction/MLMModuleML.png "ML module") | Page-based, demand-driven processing of voxels |
| Open Inventor module (green) | ![Open Inventor module](/images/tutorials/introduction/MLMModuleSo.png "Open Inventor module") | Visual scene graphs (3D); naming convention: all modules starting with *So* (for **s**cene **o**bject) |
| Macro module (brown) | ![Macro module](/images/tutorials/introduction/MLMModuleMacro.png "Macro module") | Combination of other module types, allowing implementing hierarchies and scripted interaction |
{{< /bootstrap-table >}}

If a module is invalid, it is displayed in bright red. This might happen if the module itself is not available on your system.

### Invalid modules

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:330px">Appearance</div> | Explanation |
| --- | --- |
| ![Invalid module](/images/tutorials/introduction/MLMModuleStateInvalid.png "Invalid module") | Invalid module |
  ![Macro State Invalid](/images/tutorials/introduction/MLMModuleStateMacroInvalidModule.png "Macro State Invalid") | Macro containing an invalid module |
{{< /bootstrap-table >}}

The number of warning and error messages that are being printed to the
debug console are listed in the upper right corner of the module. Once
the debug console is cleared, the warning and error indicators at the
module are also cleared. If the module produces information messages,
their number is printed in gray at this position. This enables a network
or module developer to find the modules in a network that produce
messages quickly.

### Module context menu
Each module provides a context menu to get additional information.

![Context Menu of a module](/images/tutorials/introduction/ModuleContextMenu.png "Context Menu of a module")

* **Show Internal Network:** Macro modules provide an entry to open the internal network. You can see what happens inside a Macro module. This network may also contain other Macro modules.
* **Show Window:** In case a module does not provide an own User Interface, you will see the Automatic Panel of the module showing the name. Modules may additionally have one or more Windows to be opened. You can also open the Scripting Console of a module to use Python.
* **Instance Name:** You can also edit or copy the instance name. Editing is useful if you have the same module multiple times in one network. You should give the modules a useful name to access and distinguish them in Python. Copying the name is useful if you want to access the module in Python. You will have the correct name in your clipboard for usage in Python.
* **Help:** The menu entry Help provides access to the Module Help pages and to an example network where the module is used. This example network often helps to understand which additional modules are necessary for usage.
* **Extras:** Automated tests written for the specific module can be executed here. You can also run this module in a separate process.
* **Reload Definition:** In case you are currently working on a module, you may need to reload the definition so that your changes are applied on the module (for example attached Python scripts).
* **Related Files:** Related files allows a quick access to the modules *\*.script* or *\*.py* files. The files are automatically opened in MATE for editing.
* **Show Enclosing Folder:** This entry opens the directory where your module has been stored.
* **Grouping:** Multiple modules can be Grouped and the groups can be named. This makes sense to structure your network for a better overview. In addition to that, grouped modules can be converted to local- or global Macro modules easily.

### Module Connectors {#Module_Connectors}
Most modules have connectors which are displayed on the module. These represent the inputs (bottom) and outputs (top) of modules.

In MeVisLab, three types of connectors are defined.

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:330px">Look</div> | <div style="width:130px">Appearance</div> | Definition |
| --- | --- | --- |
| ![Triangle](/images/tutorials/introduction/MLMConnectorTriangle.png "Triangle - ML Image") | triangle | ML images |
| ![Circle](/images/tutorials/introduction/MLMConnectorHalfCircle.png "Circle - Inventor Scene") | half-circle | Inventor scene |
| ![Square](/images/tutorials/introduction/MLMConnectorSquare.png "Square - Base Object") | square | Base objects: pointers to data structures |
{{< /bootstrap-table >}}

By connecting these connectors and therefore establishing a so-called data connection, image data, or Open Inventor information is transported from one module to one or more others.

Besides connecting connectors, basically any field of modules can be connected to other compatible fields of modules with a parameter connection.

Some modules contain hidden connectors in addition to the ones you can see when adding a module to the workspace. Click on the workspace and press {{< keyboard "SPACE" >}} to see the hidden connectors as well as the internal networks of each module. You can now use the hidden connectors for building connections.

{{<alert class="info" caption="Extra Infos">}}
For more information about connector and connection types click {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s03.html" "here" >}}
For more information about connecting, disconnecting, moving, and replacing connections click {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s04.html" "here" >}}
{{</alert>}}

### Macro modules {#Macro_Modules}

{{<alert class="info" caption="More Information">}}
More information about creating macro modules is available in [Tutorial Chapter I - Example 2.2](/tutorials/basicmechanisms/macromodules/globalmacromodules) 
{{</alert>}}
### Searching and Adding Modules {#Searching_and_Adding_Modules}

There are several ways to add a module to the current network, for example:
-   via the menu bar, entry {{< menuitem "Modules" >}}.
-   via the menu bar, {{< menuitem "Quick Search" >}}.
-   via the View Module Search.
-   via the View Module Browser.
-   via copy and paste from another network.
-   by scripting, see the {{< docuLinks "/Resources/Documentation/Publish/SDK/ScriptingReference/index.html" "Scripting Reference" >}}

Both the {{< menuitem "Modules" >}} menu and the Module Browser display all available modules. The modules are sorted hierarchically by topics and by module
name, as given in the file `Genre.def`.

Therefore, both places are a good starting point when in need of a specific function, like an image load module.

![Modules Menu and Module Browser](/images/tutorials/introduction/GSExampleNetworkViewImage01c.png "Modules Menu and Module Browser")

The advantage of the Module Browser is that you can right-click {{< mousebutton "right" >}} the
entries, open the context menu and, for example, open the help (in your
default Internet browser) or the module files (in MATE, the in-built
text editor).

{{<alert class="info" caption="Note">}}
For a module to get listed, it has to be available in the SDK distribution or in your user-defined packages. If in doubt or missing something, check out the loaded packages in the Preferences.

For details on packages, see [Package Creation](/tutorials/basicmechanisms/macromodules/package/).
{{</alert>}}

Usually the quickest way to add modules to a network is the quick search in the menu bar. It offers you the possibility to search for modules by module name. By default, the search will also be extended to keywords and substrings and is case-insensitive. To change these settings, click the magnifier button for the search options.

{{<alert class="info" caption="Tip">}}
The quick search field does not need to have the focus. Any time you enter something in the MeVisLab GUI while not being in a dialog window, this will be entered into the quick search automatically.
{{</alert>}}

![Quick Search Options](/images/tutorials/introduction/MLMQuickSearch.png "Quick Search Options")

To search for a module to load an image, you could either type *load* or *image*. Let us go with the second option this time. While typing *image*, the possible results appear. Use the {{< keyboard "ArrowUp" >}} or {{< keyboard "ArrowDown" >}} keys on your keyboard to move to one of the listed modules. The module's About information will appear next to it, allowing you to decide if this is the right module for you.

![Quick Search Results](/images/tutorials/introduction/GSExampleNetworkViewImage02.png "Quick Search Results")

{{<alert class="info" caption="Tip">}}
For a more complex search, use the Module Search View.
{{</alert>}}