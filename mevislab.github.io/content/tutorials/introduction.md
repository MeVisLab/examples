---
title: "Introduction"
date: 2022-06-15T08:56:33+02:00
draft: false
status: "open"
tags: ["Tutorial", "Introduction", "Glossary", "Modules", "ML Module", "Filetypes", "UI", "Workspace", "Search"]
menu: 
  main:
    identifier: "tutorial_introduction"
    title: "Overview of MeVisLab Tutorials and general information about User Interface, Modules, types of Modules, searching for Modules and Glossary including filetypes."
    weight: 310
    parent: "tutorials"
---

# MeVisLab Tutorial {#tutorial_main}

## Introduction {#tutorial_introduction}

### Welcome {#tutorial_welcome}

Welcome to MeVisLab!

MeVisLab is a development environment for rapid prototyping and product
development of medical and industrial imaging applications. It includes
a *Software Development Kit (SDK)* and an *ApplicationBuilder* for deploying
your applications to end-customers.

The *MeVisLab SDK* consists of an *Integrated Development Environment (IDE)*
for visual programming and the advanced text editor *MATE* for Python
scripting including code completion, debugging, profiling and automated
test development or execution.

You can re-use thousands of pre defined *Modules* for image processing
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

### Glossary {#tutorial_glossary}
| <div style="width:230px">Term</div> | Description |
| --- | --- |
| `MeVisLab` | MeVisLab consists of the `MeVisLab SDK` and the `MeVisLab ApplicationBuilder`. |
| `MeVisLab SDK` | The MeVisLab Software Development Kit (SDK) is the `MeVisLab IDE` including the text editor `MATE` and any tools integrated for debugging, testing and profiling. |
| `MeVisLab ApplicationBuilder` | The MeVisLab ApplicationBuilder allows you to generate installable executables from your developed networks and applications. These executables can be delivered to customers. |
| `MeVisLab IDE` | The MeVisLab Integrated Development Environment (IDE) is your starting point whenever you are working with MeVisLab. It provides a programming interface and an advanced text editor. |
| `MeVisLab MATE` | The Advanced Text Editor (MATE) is an integrated text editor for Python and `MDL` development in MeVisLab. It provides auto completion and syntax highlighting as well as debugging functionalities. |
| `MDL` | The MeVisLab Definition Language (MDL) is the language for developing basic User Interfaces for `Networks` and `Modules` in MeVisLab. |
| `Module` | A Module is a single instance providing encapsulated functionalities for a specific purpose. MeVisLab provides thousands of such pre-defined Modules and you can develop your own Modules for extending existing functionalities. Modules provide inputs and outputs for connections in a `Network` and/or one or more `Panels` for interacting. |
| `Panel` | A Panel is a User Interface providing possibilities to interact with MeVisLab. |
| `Field` | Parameters of Modules are called fields. Several different types of fields are available such as numbers, text, trigger buttons, etc. Publicly accessible fields can be modified in the `Module Inspector` or Panel of the selected Module.         |
| `Macro Module` | Macro Modules encapsulate `Networks` including input and output into a single `Module`. In order to see whats inside a Macro Module, you can open the Context Menu via Right-Click and select {{< menuitem "Show Internal Network" >}}. You can chose to create `Local Macros` and `Global Macros`. |
| `Local Macro` | Local Macros are only available in your currently opened `Network`. You cannot use the Module Search in MeVisLab to find Local Macros. |
| `Global Macro` | Global Macros are integrated into MeVisLab and can be used in any future Networks. They are available in Module search. |
| `Network` | A Network defines at least two connected `Modules`. |
| `Example Network` | Each `Module` provides an Example Network to see how it can be used. Right-Click on the `Module` and select Help > Show Example Network |
| `Output Inspector` | The Output Inspector is a quick preview of the output of a specific `Module`. The output can be an image or any other user defined output format. |
| | For images, a 2D and 3D view including basic interactions is already available. |
| `Module Inspector` | The Module Inspector shows publicly available properties of the selected module and their current values. Changes in Module Inspector are applied on the fly. |
| `Workspace` | The Workspace is the area where you can add and connect `Modules`. Multiple `Networks` are organized in separate Tabs. |
| `Views Area` | The right side of the `MeVisLab IDE` provides a space to add several predefined panels like `Output-` and `Module inspectors`. |
| `Debug Output` | The Debug Output shows debugging messages of your `Modules` and the `MeVisLab IDE`. |
| `Open Inventor` | |
| `Scene Objects` | |
| `CSO` | Contour Segmentation Objects (CSOs) |
| `WEM` | Winged Edge Meshes (WEMs) |
| `GVR` | Giga Voxel Renderer (GVR) |
| `Lookup Table (LUT)` | |
| `Package` | |


### MeVisLab IDE User Interface {#tutorial_ide}

First, start MeVisLab IDE. After the Welcome Screen, the standard user interface opens.

![MeVisLab IDE User Interface](/images/IDE1.png "MeVisLab IDE User Interface")

#### Workspace

By default, MeVisLab starts with an empty workspace. The workspace is
the place for developing and editing Networks via visual programming.
Networks of Modules form the basis for all processing and visualization
pipelines.

#### Views Area

The standard Views Area contains the [Output Inspector and the Module Inspector](./tutorials/basicmechanisms#The_Output_Inspector_and_the_Module_Inspector "Output Inspector and the Module Inspector"). With the help of the Output Inspector, you can visualize the Module output.

Further information of each module, like information about Module parameters can be found using the Module Inspector .

#### Debug Output

In the Debug Output, you can find any debugging information about
your MeVisLab installation.

The MeVisLab IDE and the layout is completely configurable. You can
rearrange the items and add new views via {{< menuitem "Main Menu" "View" "Views" >}}.

### Filetypes in MeVisLab

Here a list of the most important file types:

| <div style="width:230px">Extension</div> | Description |
| --- | --- |
| `.mlab` | Network file, includes all information about the network\'s modules, their settings, their connections, and module groups. Networks developed by using the `MeVisLab SDK`are stored as `.mlab` file and can only be opened having a valid SDK license. |
| `.def` | Module definition file, necessary for a module to be added to the common MeVisLab module database. May also include all MDL script parts (if they are not sourced out to the `.script` file). |
| `.script` | `MDL` script file, typically includes the user interface definition for panels. See [Chapter GUI Development](./tutorials/basicmechanisms/macromodules/guidesign#Example_Paneldesign "GUI Development") for an example on GUI programming. |
| `.mlimage` | MeVisLab internal image format for 6D images saved with all DICOM tags, lossless compression, and in all data types. |
| `.mhelp` | File with descriptions of all fields and the use of a module, edit- and creatable by using `MATE`. See [Help files](./tutorials/basicmechanisms/macromodules/helpfiles "Help files") for details. |
| `.py` | Python file, used for scripting in macro modules. See [Python scripting](./tutorials/basicmechanisms/macromodules/pythonscripting#TutorialPythonScripting "Python scripting") for an example on macro programming. |
| `.dcm` | DCM part of the imported DICOM file, see [Importing DICOM Data](./tutorials/basicmechanisms/dataimport#DICOMImport "Importing DICOM Data"). |

### Types of Modules {#Module_Types}

Within the concept of MeVisLab the basic entities we are working with
a graphical representations of modules having their specific functions
for image processing, image visualization, and image interaction.

The three basic module types (ML, Open Inventor and Macro Module) are
distinguished by their colors:

| <div style="width:230px">Type</div> | <div style="width:430px">Look</div> | Characteristics |
| --- | --- | --- |
| ML Module (blue) | ![ML Module](/images/MLMModuleML.png "ML Module") | Page-based, demand-driven processing of voxels |
| Open Inventor Module (green) | ![Open Inventor Module](/images/MLMModuleSo.png "Open Inventor Module") | Visual scene graphs (3D); naming convention: all modules starting with *So* (for **s**cene **o**bject) |
| Macro Module (brown) | ![Macro Module](/images/MLMModuleMacro.png "Macro Module") | Combination of other module types, allowing implementing hierarchies and scripted interaction |

If a module is invalid, it is displayed in bright red. This might happen if the module itself is not available on your system.


| <div style="width:330px">Appearance</div> | Explanation |
| --- | --- |
| ![Invalid Module](/images/MLMModuleStateInvalid.png "Invalid Module") | Invalid module |
  ![Macro State Invalid](/images/MLMModuleStateMacroInvalidModule.png "Macro State Invalid") | Macro containing an invalid module |

The number of warning and error messages that are being printed to the
debug console are listed at the upper right corner of the module. Once
the debug console is cleared, the warning and error indicators at the
module are also cleared. If the module produces information messages,
their number is printed in gray at this position. This enables a network
or module developer to find the modules in a network that produce
messages quickly.

### Module Connectors {#Module_Connectors}
Most modules have connectors which are displayed on the module. These represent the inputs (bottom) and outputs (top) of modules.

In MeVisLab, three types of connectors are defined.

| <div style="width:330px">Look</div> | <div style="width:130px">Appearance</div> | Definition |
| --- | --- | --- |
| ![Triangle](/images/MLMConnectorTriangle.png "Triangle - ML Image") | triangle | ML images |
| ![Circle](/images/MLMConnectorHalfCircle.png "Circle - Inventor Scene") | half-circle | Inventor scene |
| ![Square](/images/MLMConnectorSquare.png "Square - Base Object") | square | Base objects: pointers to data structures |

By connecting these connectors and therefore establishing a so-called data connection, image data, or Open Inventor information is transported from one module to one or more others.

Besides connecting connectors, basically any field of modules can be connected to other compatible fields of modules with a parameter connection.

Some modules contain hidden connectors in addition to the ones you can see when adding a module to the workspace. Click on the workspace and press {{< keyboard "SPACE" >}} to see the hidden connectors as well as the internal networks of each module. You can now use the hidden connectors for building connections.

{{<alert class="info" caption="Extra Infos">}}
For more information about connector and connection types click {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s03.html" "here" >}}
For more information about connecting, disconnecting, moving, and replacing connections click {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch03s04.html" "here" >}}
{{</alert>}}

### Macro Modules {#Macro_Modules}

{{<alert class="info" caption="More Information">}}
More information about creating Macro Modules is available in [Tutorial Chapter I - Example 2.2](/tutorials/basicmechanisms/macromodules/globalmacromodules) 
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

![Modules Menu and Module Browser](/images/GSExampleNetworkViewImage01c.png "Modules Menu and Module Browser")

The advantage of the Module Browser is that you can right-click {{< mousebutton "right" >}} the
entries, open the context menu and, for example, open the help (in your
default Internet browser) or the module files (in MATE, the in-built
text editor).

{{<alert class="info" caption="Note">}}
For a module to get listed, it has to be available in the SDK distribution or in your user-defined packages. If in doubt or missing something, check out the loaded packages in the Preferences.

For details on packages, see [Package Creation](/tutorials//basicmechanisms/macromodules/package/).
{{</alert>}}

Usually the quickest way to add modules to a network is the quick search in the menu bar. It offers you the possibility to search for modules by module name. By default, the search will also be extended to keywords and substrings and is case-insensitive. To change these settings, click the magnifier button for the search options.

{{<alert class="info" caption="Tip">}}
The quick search field does not need to have the focus. Any time you enter something in the MeVisLab GUI while not being in a dialog window, this will be entered into the quick search automatically.
{{</alert>}}

![Quick Search Options](/images/MLMQuickSearch.png "Quick Search Options")

To search for a module to load an image, you could either type *load* or *image*. Let us go with the second option this time. While typing *image*, the possible results appear. Use the {{< keyboard "ArrowUp" >}} or {{< keyboard "ArrowDown" >}} keys on your keyboard to move to one of the listed modules. The module's About information will appear next to it, allowing you to decide if this is the right module for you.

![Quick Search Results](/images/GSExampleNetworkViewImage02.png "Quick Search Results")

{{<alert class="info" caption="Tip">}}
For a more complex search, use the Module Search View.
{{</alert>}}