---
title: "Step 2: Prototyping - Create a macro module"
date: "2023-01-16"
status: "open"
draft: false
weight: 810
tags: ["Advanced", "Tutorial", "Prototyping", "Macro modules"]
menu: 
  main:
    identifier: "summaryexample2"
    title: "Create a macro module from your network."
    weight: 810
    parent: "summary"
---
# Step 2: Prototyping - Create a macro module

{{< youtube "gNlOTiEOJgU" >}}

## Introduction
In this example, we encapsulate the previously developed prototype network into a macro module for future application development and automated testing.

## Steps to do
Make sure to have your *.mlab file from the previous [tutorial](tutorials/summary/summary1/) available.

### Package creation
Packages are described in detail in [Example 2.1: Package creation](tutorials/basicmechanisms/macromodules/package/). If you already have your own package, you can skip this part and continue creating a macro module.

Open Project Wizard via {{< menuitem "File" "Run Project Wizard..." >}} and select *New Package*. Run the Wizard and enter details of your new package and click *Create*.

![Package wizard](images/tutorials/summary/Example2_1.png "Package wizard")

MeVisLab reloads and you can start creating your macro module.

### Create a macro module
Open Project Wizard via {{< menuitem "File" "Run Project Wizard..." >}} and select *macro module*. Run the Wizard and enter details of your new macro module. 

![Macro module wizard](images/tutorials/summary/Example2_2.png "Macro module wizard")

Select the created package and click *Next*.

![Macro module wizard](images/tutorials/summary/Example2_3.png "Macro module wizard")

Select your \*.mlab file from [Step 1](tutorials/summary/summary1/) and check *Add Python file*. Click *Next*.

![Macro module wizard](images/tutorials/summary/Example2_4.png "Macro module wizard")

You do not have to define fields of your macro module now, we will do that later. Click *Create*. The Windows Explorer opens showing the directory of your macro module. It should be the same directory you selected for your Package.

### Directory Structure of a macro module
The directory structure for a macro module is as follows:
* From Package Wizard:
  * Package target directory is the root directory of the module
  * The next directory is the package group and package name
* From macro module Wizard:
  * The name of the macro module defines the directory containing all files of your module
  * An additional directory *Modules* is created containing the following files:
    * <MACRO_NAME>.def
    * <MACRO_NAME>.mlab
    * <MACRO_NAME>.py
    * <MACRO_NAME>.script

![Directory Structure](images/tutorials/summary/Example2_6.png "Directory Structure")

#### Definition (\*.def) file
The initial \*.def file contains information you entered into the Wizard for the macro module.

{{< highlight filename="<MACRO_NAME>.def" >}}
```Stan
Macro module TutorialSummary {
  genre              = "VisualizationMain"
  author             = "MeVis Medical Solutions AG"
  comment            = "Macro module for MeVisLab Tutorials"
  keywords           = "2D 3D RegionGrowing"
  seeAlso            = ""
   
  externalDefinition = "$(LOCAL)/TutorialSummary.script"
}
```
{{</highlight>}}

An *externalDefinition* to a script file is also added (see below for the \*.script file).

#### MeVisLab Network (\*.mlab) file
The \*.mlab file is a copy of the \*.mlab file you developed in [Step 1](tutorials/summary/summary1/) and re-used in the wizard. In the next chapters, this file will be used as *internal network*. 

#### Python (\*.py) file
The initial \*.py file only contains the import of MeVisLab specific objects and functions. In the future steps, we will add functionalities to our application in Python.

{{< highlight filename="<MACRO_NAME>.py" >}}
```Python
from mevis import *
```
{{</highlight>}}

#### Script (\*.script) file
The script (\*.script) file defines fields accessible from outside the macro module, inputs and outputs and allows you to develop a User Interface for your prototype and your final application.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
  Inputs {}
  Outputs {}
  Parameters {}
}


Commands {
  source = $(LOCAL)/TutorialSummary.py
}
```
{{</highlight>}}

The source also defines your Python file to be used when calling functions and events from the User Interface.

### Using your macro module
As you created a global macro module, you can search for it in the MeVisLab *Module Search*.

![Module Search](images/tutorials/summary/Example2_7.png "Module Search")

We did not define inputs or outputs. You cannot connect your module to others. In addition to that, we did not develop a User Interface. Double-clicking your module {{< mousebutton "left" >}} only opens the Automatic Panel showing the *instanceName*.

![Automatic Panel](images/tutorials/summary/Example2_8.png "Automatic Panel")

Right-click on your module allows you to open the internal network as developed in [Step 1](tutorials/summary/summary1/).

## Summary
* Macro modules encapsulate an entire MeVisLab network including all modules.
* The internal network can be shown (and edited) via right-click {{< mousebutton "right" >}} {{< menuitem "Show Internal Network" >}}
* The Wizard already creates the necessary folder structure and generates files for User Interface and Python development.

{{< networkfile "examples/summary/TutorialSummary.zip" >}}
