---
title: "Developing Your Own C++ Modules"
date: 2026-03-15T08:56:33+02:00
status: "OK"
draft: false
weight: 601
tags: ["Advanced", "Tutorial", "Image Processing", "C++"]
menu: 
  main:
    identifier: "cpp"
    title: "Developing Your Own C++ Modules"
    weight: 601
    parent: "imageprocessing"
---

# C++ Module Development
## Introduction
The development of your own C++ modules can be done by ML modules and by Open Inventor modules.

{{<alert class="info" caption="Important Information">}}
Make sure to use a compiler that is compatible with your currently installed MeVisLab version.
{{</alert>}}

### ML Modules on the C++ Level
* Image processing modules are objects derived from class Module defined in the ML library and therefore are also called ML modules.
* Image inputs and outputs are connectors to objects of class PagedImage, which are defined in the ML library.
* Inputs and outputs for abstract data structures are connectors to pointers of objects derived from class Base and are called Base objects.

### Open Inventor Modules on the C++ Level
* Most Open Inventor modules are objects derived from class SoNode, defined in the Open Inventor library.
* Open Inventor inputs and outputs are connectors to objects derived from class SoNode, defined in the Open Inventor library. Many Open Inventor modules will return themselves as outputs (“self”). On inputs, they may have connectors to child Open Inventor modules.
* Some Open Inventor modules are objects derived from class SoEngine. They are used for calculations and return their output not via output connectors but via parameter fields.
* Open Inventor modules may also have input and output connectors to Base objects and Image objects.
* All standard Open Inventor nodes defined in the Open Inventor library are available in MeVisLab as Open Inventor modules.

This chapter describes some examples for developing your own ML and Open Inventor modules.

## Some Tips for Module Design
### Macro Modules or C++ Modules?
In [Example 2: Macro Modules](tutorials/basicmechanisms/macromodules/), we already described Macro Modules and how to create them yourself.

**Advantages of macros:**
* Macros are useful for creating a layer of abstraction by hierarchical grouping of existing modules.
* Scripts can be edited on the fly:
  * no compilation and reload of the module database necessary
  * scripting possible on the module or network level
  * scripting supported by the Scripting Assistant View (basically a recorder for actions performed on the network)

**Conclusion:**
* For rapid prototyping based on existing image processing algorithms, use macros.
* For implementing new image processing, write new ML or Open Inventor modules.

### Combining Functionalities
It is possible to have ML and Open Inventor connectors in the same module. Two cases are possible:
* Type 1: **ML -> visualization:** Image data or properties are displayed by a visualization module. Usually a <field>SoSFXVImage</field> field gets random access to an ML image by *getTile()*. Examples: `SoView2D`, `GlobalStatistics`.
* Type 2: **visualization -> ML:** Modules generate an ML image from an Open Inventor scene. Examples: `VoxelizeInventorScene`, `SoExaminerViewer` (hidden functionality).

Generally, however, it is not always a good solution to combine that, as the processes of image processing and image visualization are usually separated.

Therefore, rather separate the ML and Open Inventor functionalities into two modules. This way,
* functionality is encapsulated and can be reused as module
* modules for the single steps may already be available in MeVisLab and spare you a new development

## Code Examples
In addition to the tutorials in this chapter, you can find additional code examples in your MeVisLab installation directory.
