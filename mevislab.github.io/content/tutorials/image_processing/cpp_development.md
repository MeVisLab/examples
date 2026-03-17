---
title: "Developing your own C++ Modules"
date: 2026-03-15T08:56:33+02:00
status: "OK"
draft: false
weight: 601
tags: ["Advanced", "Tutorial", "Image Processing", "C++"]
menu: 
  main:
    identifier: "cpp"
    title: "Developing your own C++ Modules"
    weight: 601
    parent: "imageprocessing"
---

# C++ Module development
## Introduction
The development of your own C++ modules can be done by ML modules and by Inventor modules.

{{<alert class="info" caption="Important Information">}}
Make sure to use a compiler that is compatible to your currently installed MeVisLab version.
{{</alert>}}

### ML modules on the C++ level
* Image processing modules are objects derived from class Module defined in the ML library and therefore are also called ML modules.
* Image inputs and outputs are connectors to objects of class PagedImage, which are defined in the ML library.
* Inputs and outputs for abstract data structures are connectors to pointers of objects derived from class Base and are called Base objects.

### Inventor modules on the C++-level:
* Most Inventor modules are objects derived from class SoNode defined in the Open Inventor library.
* Inventor inputs and outputs are connectors to objects derived from class SoNode defined in the Open Inventor library. Many Inventor modules will return themselves as outputs (“self”). On inputs, they may have connectors to child Inventor modules.
* Some Inventor modules are objects derived from class SoEngine. They are used for calculations and return their output not via output connectors but via fields.
* Inventor modules may also have input and output connectors to Base objects and Image objects.
* All standard Inventor nodes defined in the Open Inventor library are available in MeVisLab as Inventor modules.

This chapter describes some examples for developing your own ML and Inventor modules.

## Some Tips for Module Design
### Macro Modules or C++ Modules?
In [Example 2: Macro Modules](tutorials/basicmechanisms/macromodules/), we already described Macro Modules and how to create them yourself.

**Advantages of macros:**
* Macros are useful for creating a layer of abstraction by hierarchical grouping of existing modules.
* Scripts can be edited on the fly:
  * no compilation and reload of the module database necessary
  * scripting possible on the module or network level
  * scripting supported by the Scripting Assistant View (basically a recorder for actions performed on the network)

**Disadvantages:**
* With macros, only existing functionalities and algorithms can be used.

**Conclusion:**
* For rapid prototyping based on existing image processing algorithms, use macros.
* For implementing new image processing, write new ML or Open Inventor modules.

### Combining Functionalities
It is possible to have ML and Open Inventor connectors in the same module. Two cases are possible:
* Type 1: **ML -> visualization:** Image data or properties are displayed by a visualization module. Usually a <field>SoSFXVImage</field> field gets random access to an ML image by *getTile()*. Examples: `SoView2D`, `GlobalStatistics`.
* Type 2: **visualization -> ML:** Modules generate an ML image from an Inventor scene. Examples: `VoxelizeInventorScene`, `SoExaminerViewer` (hidden functionality).

Generally, however, it is not always a good solution to combine that, as the processes of image processing and image visualization are usually separated.

Therefore, rather separate the ML and Open Inventor functionalities into two modules. This way,
* functionality is encapsulated and can be reused as module
* modules for the single steps may already be available in MeVisLab and spare you a new development
