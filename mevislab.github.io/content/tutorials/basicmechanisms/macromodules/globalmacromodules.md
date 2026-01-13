---
title: "Example 2.2: Creation of global macro modules"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 390
tags: ["Beginner", "Tutorial", "Macro", "Macro modules", "Global Macro"]
menu: 
  main:
    identifier: "globalmacromodules"
    title: "Creation of global macro modules from a local macro using the Project Wizard"
    weight: 390
    parent: "macro_modules"
---

# Example 2.2: Global Macro Modules

{{< youtube "M4HnA0d1V5k">}}

## Introduction

In this chapter you will learn how to create global macro modules. There are many ways to do this. You can convert local macros into global macro modules or you can directly create global macro modules using the *Project Wizard*. In contrast to local macro modules, global macro modules are commonly available throughout projects and can be found via module search and under {{< menuitem "Modules" >}}.

## Steps to Do
### Transform a Local Macro Module into a Global Macro Module
To transform our local macro module `Filter` from [Chapter I](tutorials/basicmechanisms#TutorialMacroModules) into a global macro module,
right-click {{< mousebutton "right" >}} the macro module to open the context menu and select {{< menuitem "Extras" "Convert To Global Module..." >}}

![Convert local macro to global macro](images/tutorials/basicmechanics/GUI_03.png "Convert local macro to global macro")

### Define Module Properties

1.  Choose a unique module name.

2.  State the module's author.

3.  Select the genre of the module. For this, browse through the module
    genres to select the appropriate genre. In our case, as our macro module
    contains a contour filter, we will choose the genre *Filters*.

    The *Genre* defines the location where your module will be shown in MeVisLab {{< menuitem "Modules" >}} menu.

4. Tick the box *Add reference to example network* to directly create the template for an example network for your macro module.

5.  Select the package you like to store the module in. We choose the
    package we created [before](./tutorials/basicmechanisms/macromodules/package/). Your module is saved in the *.mlab* format
    and can be found in
    *\\MyPackageGroup\\General\\Modules\\Macros\\MyProject*.

{{<alert class="info" caption="Info">}}
If you are working with MeVisLab versions before 5.0, make sure to choose *Directory Structure* as *self-contained*. This makes sure that all files of your module are stored in a single directory. Later versions always use *self-contained*.

Also keep in mind that Python files are only created automatically if selected in the Project Wizard. Converting a local macro to a global macro does NOT create a Python file automatically.
{{</alert>}}

![Create global macro module](images/tutorials/basicmechanics/GUI_04.png "Create global macro module")

### Use the Project Wizard to Create Global Macro Modules
Instead of converting a local macro module into a global macro module, you can also use the *Project Wizard* to create new macro modules. Open the Project Wizard via {{< menuitem "File" "Run Project Wizard ..." >}}. Then, select {{< menuitem "Modules (Scripting)" "Macro module" >}} and *Run Wizard*.

### Define Module Properties

1.  Choose a unique module name.

2.  State the module's author.

3.  Select the genre of the module. For this, browse through the module
    genres to select the appropriate genre. In our case, as our macro module
    contains a contour filter, we will choose the genre *Filters*.

4. Tick the box *Add reference to example network* to directly create the template for an example network for your macro module.

5.  Select the package you like to store the module in. We choose the
    package we created [before](./tutorials/basicmechanisms/macromodules/package/). Your module is saved in the *.mlab* format
    and can be found in
    *\\MyPackageGroup\\General\\Modules\\Macros\\MyProject*.

{{<alert class="info" caption="Info">}}
Make sure to choose *Directory Structure* as *self-contained*. This ensures that all files of your module are stored in a single directory.
{{</alert>}}
 
 Press *Next >* to edit further properties. You have the opportunity to directly define the internal network of the macro module, for example, by copying an existing network. In this case, we could copy the network of the local macro module `Filter` we already created. In addition, you have the opportunity to directly create a Python file. Python scripting can be used for the implementation of module interactions and other module functionalities. More information about Python scripting can be found [here](./tutorials/basicmechanisms/macromodules/pythonscripting).

{{< imagegallery 2 "images" "ProjectWizard1" "ProjectWizard2" >}}

## Structure of Global Macro Modules
After creating your global macro module, you can find the created project *MyProject* in your package. This project contains your macro module `Filter`. For the macro module exist three files:
* *Filter.def*: module definition file
* *Filter.mlab*: network file that contains the internal network of your macro module
* *Filter.script*: MDL script file that defines inputs and outputs of your macro module as well as fields. This file defines the module panel, as well as references to Python scripts.

In addition, two folders may be created:
* *mhelp*: contains the help files of all modules of this project
* *network*: contains the example networks of all modules of this project

![Structure of global macro modules](images/tutorials/basicmechanics/GUI_04_2.png "Structure of global macro modules")

## How to Find Global Macro Modules
All available modules are categorized and can be found via {{< menuitem "Modules" >}} in
the respective genre. After creating a global
macro, the new module can be found via {{< menuitem "Modules" "Filters" >}}. In addition, you can now find your macro module via module search.

![Find module in menu](images/tutorials/basicmechanics/GUI_05.png "Find module in menu")


{{<alert class="info" caption="Hint">}}
If you do not find your new global macro module, try to reload the module database.
![Reload module database](images/tutorials/basicmechanics/GUI_05_2.png "Reload module database")
{{</alert>}}

## Summary
* Via right-click {{< mousebutton "right" >}} {{< menuitem "Extras" "Convert To Global Module..." >}}, global macro modules can be created out of local macro modules.
* You can use the Project Wizard to create new macro modules.
* You need to have a package structure to store your global macro module.
* Global macro modules are available throughout projects and can be found via *Module Search* and under menu item {{< menuitem "Modules" >}}.