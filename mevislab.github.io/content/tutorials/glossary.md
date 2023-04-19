---
title: "Glossary"
date: 2023-04-19T08:56:33+02:00
draft: false
status: "OK"
weight: 315
tags: ["Search", "Glossary", "Usability"]
menu: 
  main:
    identifier: "glossary"
    title: "Glossary"
    weight: 315
    parent: "tutorials"
---

{{< bootstrap-table table_class="table table-striped" >}}
| <div style="width:230px">Term</div> | Description |
| --- | --- |
| `MeVisLab` | MeVisLab consists of the `MeVisLab SDK` and the `MeVisLab ApplicationBuilder`. |
| `MeVisLab SDK` | The MeVisLab Software Development Kit (SDK) is the `MeVisLab IDE` including the text editor `MATE` and any tools integrated for debugging, testing and profiling. |
| `MeVisLab ApplicationBuilder` | The MeVisLab ApplicationBuilder allows you to generate installable executables from your developed networks and applications. These executables can be delivered to customers. |
| `MeVisLab IDE` | The MeVisLab Integrated Development Environment (IDE) is your starting point whenever you are working with MeVisLab. It provides a programming interface and an advanced text editor. |
| `MeVisLab MATE` | The Advanced Text Editor (MATE) is an integrated text editor for Python and `MDL` development in MeVisLab. It provides auto-completion and syntax highlighting, as well as debugging functionalities. |
| `MDL` | The MeVisLab Definition Language (MDL) is the language for developing basic User Interfaces for `Networks` and `Modules` in MeVisLab. |
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
| `CSO` | Contour Segmentation Objects (CSOs) |
| `WEM` | Winged Edge Meshes (WEMs) |
| `GVR` | Giga Voxel Renderer (GVR) |
| `Lookup Table (LUT)` | |
| `Package` | |
{{< /bootstrap-table >}}