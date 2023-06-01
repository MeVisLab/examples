---
title: "Example 1: Module Setup"
date: 2023-05-26
status: "OK"
draft: false
weight: 881
tags: ["Beginner", "Tutorial", "Matplotlib", "Visualization"]
menu: 
  main:
    identifier: "matplotlibexample1"
    title: "Example 1: Module Setup"
    weight: 881
    parent: "matplotlib"
---

# Example 1: Module Setup

## Introduction

To be able to access the data needed for our grayscale distribution plots, we need a network consisting of a module that imports DICOM data, a module that differentiates between slices and another that ouputs histogram data. 

## Steps to do 

Open up your MeVisLab workspace and add the modules `LocalImage`, `SubImage` and `Histogram` to it.
Connect the output of `LocalImage` to the input of `SubImage` and the output of `SubImage` with the input of `Histogram`.
If you feel like using a shortcut, you can also download the base network below and open it in your MeVisLab.

Your finished network should look like this: 

![Base network](/images/tutorials/thirdparty/Matplotlib1.PNG)

{{< networkfile "/tutorials/thirdparty/matplotlib/MatplotlibBaseNetwork.mlab" >}}

### Excursion on the concept behind modules

To be able to build on the foundation we just set, it can be useful to understand how modules are conceptualized:
You will have noticed how, for every module, a panel will pop up if you double-click it. The modules panel contains all of its functional parameters and enables you, as the user, to change them within a graphical user interface (GUI). We will do something similar later on. 
But where and how is a module panel created? To answer this question, please close the module panel and right-click on the module. 
A context menu will open, click on "Related Files". 

![Context menu of the "SubImage" module](/images/tutorials/thirdparty/Matplotlib2.png)

As you can see, each module has a .script and a .py file, named like the module itself: 
+ The .script file is, where the appearance and structure of the module panel as well as their commands are declared. 
+ The .py file contains Python functions and methods, which are triggered by their referenced commands within the .script file.

Some modules also reference a .mlab file which usually contains their internal network as the module is a macro. 

**Let's continue with our module setup now:**  
If your network is ready, group it by right-clicking on your group's title and select "Grouping", then "Add To A New Group".
After, convert your grouped network into a macro module. 

![Converting to a macro](/images/tutorials/thirdparty/Matplotlib3.png)
{{<alert class="info" caption="Info">}}
Information on how to convert groups into macros can be found [here](/tutorials/basicmechanisms#TutorialMacroModules). 
{{</alert>}}
Depending on whether you like to reuse your projects in other workspaces, it can make sense to convert them.
We'd recommend to do so. 

Now open the .script file of your newly created macro through the context menu. The file will be opened within MATE (MeVisLab Advanced Text Editor). Add this short piece of code into your .script file and make sure that the .script and the .py are named exactly the same as the module they are created for.

{{< highlight filename = "BaseNetwork.script">}}
```Stan
    Commands{
      source = $(LOCAL)/BaseNetwork.py
    }
``` {{</highlight>}}


Click the "Reload" button that is located above the script for the .py file to be added into the module definition folder, then open it using the "Files" button on the same bar as demonstrated below:
![MATE](/images/tutorials/thirdparty/Matplotlib5.png)

{{<alert class="info" caption="Info">}}
The [MDL Reference](https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Resources/Documentation/Publish/SDK/MDLReference/index.html) is a very handy tool for this and certainly also for following projects. 
{{</alert>}}

You have now created your own module and enabled the .script file (hence the GUI or panel later on) to access functions and methods written in the .py file. 

### Summary 
+ Modules are defined by the contents within their definition folder.
+ A module consists of of a .script file that contains the panel configuration and a .py file containing methods that are accessed via the panel and provide functionalities (Interacting with the parameters of modules in the macros internal network).
+ A macro module's panel can access parameters of its internal modules. 
+ The panel is layouted using MDL.













