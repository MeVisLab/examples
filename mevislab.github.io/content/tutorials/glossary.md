---
title: "Glossary"
date: 2023-04-19T08:56:33+02:00
draft: false
status: "OK"
weight: 250
tags: ["Search", "Glossary", "Usability", "Definitions", "Descriptions", "Terms", "Abbreviations", "Components"]
---
### Abbreviations
{{< bootstrap-table table_class="table table-striped" >}}
| <div>Abbreviation</div> | Meaning |
| --- | --- |
| `CSO` | Contour Segmentation Objects (CSOs) |
| `WEM` | Winged Edge Meshes (WEMs) |
| `GVR` | Giga Voxel Renderer (GVR) |
{{< /bootstrap-table >}}

### Filetypes 
{{< bootstrap-table table_class="table table-striped" >}}
| <div>Extension</div> | Description |
| --- | --- |
| `.mlab` | Network file, includes all information about the network\'s modules, their settings, their connections, and module groups. Networks developed by using the `MeVisLab SDK` are stored as `.mlab` file and can only be opened having a valid SDK license. |
| `.def` | Module definition file, necessary for a module to be added to the common MeVisLab module database. May also include all MDL script parts (if they are not sourced out to the `.script` file). |
| `.script` | `MDL` script file, typically includes the user interface definition for panels. See [Chapter GUI Development](./tutorials/basicmechanisms/macromodules/guidesign#Example_Paneldesign "GUI Development") for an example on GUI programming. |
| `.mlimage` | MeVisLab internal image format for 6D images saved with all DICOM tags, lossless compression, and in all data types. |
| `.mhelp` | File with descriptions of all fields and the use of a module, edit- and creatable by using `MATE`. See [Help files](./tutorials/basicmechanisms/macromodules/helpfiles "Help files") for details. |
| `.py` | Python file, used for scripting in macro modules. See [Python scripting](./tutorials/basicmechanisms/macromodules/pythonscripting#TutorialPythonScripting "Python scripting") for an example on macro programming. |
| `.dcm` | DCM part of the imported DICOM file, see [Importing DICOM Data](./tutorials/basicmechanisms/dataimport#DICOMImport "Importing DICOM Data"). |
{{< /bootstrap-table >}}

### Components of MeVisLab
{{< bootstrap-table table_class="table table-striped" >}}
| <div>Component</div> | Description |
| --- | --- |
| `MeVisLab` | MeVisLab consists of the `MeVisLab SDK` and the `MeVisLab ApplicationBuilder`. |
| `MeVisLab SDK` | The MeVisLab Software Development Kit (SDK) is the `MeVisLab IDE` including the text editor `MATE` and any tools integrated for debugging, testing and profiling. |
| `MeVisLab ApplicationBuilder` | The MeVisLab ApplicationBuilder allows you to generate installable executables from your developed networks and applications. These executables can be delivered to customers. |
| `MeVisLab IDE` | The MeVisLab Integrated Development Environment (IDE) is your starting point whenever you are working with MeVisLab. It provides a programming interface and an advanced text editor. |
| `MeVisLab MATE` | The Advanced Text Editor (MATE) is an integrated text editor for Python and `MDL` development in MeVisLab. It provides auto-completion and syntax highlighting, as well as debugging functionalities. |
| `MDL` | The MeVisLab Definition Language (MDL) is the language for developing basic User Interfaces for `Networks` and `Modules` in MeVisLab. |
{{< /bootstrap-table >}}

### MeVisLab Terminology and Concepts
{{< bootstrap-table table_class="table table-striped" >}}
| <div>Term</div> | Description |
| --- | --- |
| `Module` | A Module is a single instance providing encapsulated functionalities for a specific purpose. MeVisLab provides thousands of such pre-defined Modules and you can develop your own Modules for extending functionalities. Modules provide inputs and outputs for connections in a `Network` and/or one or more `Panels` for interacting. |
| `Panel` | A Panel is a User Interface providing possibilities to interact with MeVisLab. |
| `Field` | Parameters of Modules are called fields. Several different types of fields are available such as numbers, text, trigger buttons, etc. Publicly accessible fields can be modified in the `Module Inspector` or Panel of the selected Module.         |
| `Macro Module` | Macro Modules encapsulate `Networks` including input and output into a single `Module`. In order to see whats inside a Macro Module, you can open the Context Menu via Right-Click and select *[ Show Internal Network ]*. You can choose to create `Local Macros` and `Global Macros`. |
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
| `Open Inventor` | Open Inventor Modules process and render 3D scene objects and enable image interactions. |
| `Scene Objects` | |
| `Lookup Table (LUT)` | |
| `Package` | |
{{< /bootstrap-table >}}

