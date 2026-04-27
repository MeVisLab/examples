---
title: "Example 2: Profiling in MeVisLab"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 760
tags: ["Beginner", "Tutorial", "Profiling"]
menu: 
  main:
    identifier: "testingexample2"
    title: "Profiling in MeVisLab"
    weight: 792
    parent: "testing"
---

# Example 2: Profiling in MeVisLab

{{< youtube "DZ4BcAne4hM" >}}

## Introduction
In this example we are using the MeVisLab Profiler to inspect the memory and CPU consumption of the modules in an example network.

## Steps to Do

### Creating the Network to be Used for Profiling
You can open any network you like, here we are using the example network of the module `MinMaxScan` for profiling. Add the module `MinMaxScan` to your workspace, open the example network via right-click {{<mousebutton "right">}} and select {{<menuitem "Help" "Show Example Network">}}.

![MinMaxScan example network](images/tutorials/testing/profiling_network.png "MinMaxScan example network")

### Enable Profiling
Next, enable the MeVisLab Profiler via menu item {{<menuitem "View" "Views" "Profiling">}}. The Profiler is opened in your views area but can be detached and dragged over the workspace holding the left mouse button {{<mousebutton "left">}}.

![MeVisLab profiling](images/tutorials/testing/Profiling.png "MeVisLab profiling")

Enable profiling by checking *Enable* in the top left corner of the Profiling window.

### Inspect Your Network
Now open the `View2D` module's panel via double-click {{< mousebutton "left" >}} and scroll through the slices. Inspect the Profiler.

![MeVisLab Profiling Network](images/tutorials/testing/Profiling_Network1.png "MeVisLab profiling network")

The Profiler shows detailed information about each module in your network. 

{{<alert class="info" caption="Info">}}
Macro modules are not profiled on default. You can check the *Show macros* option in order to have `View2D` and `LocalImage` profiled.
Also, filtering by module name is handy when you are working with larger networks.
{{</alert>}}

Field values and their changes for all modules in your network can be inspected in the *Fields* tab:

![MeVisLab profiling fields](images/tutorials/testing/Profiling_Network2.png "MeVisLab profiling fields")

In addition to the Profiler window, your modules also provide a tiny bar indicating their current memory and time consumption relative to the other modules in the network.

![MeVisLab profiling module](images/tutorials/testing/Module_Info.png "MeVisLab profiling module")

{{<alert class="info" caption="Info">}}
More information about profiling in MeVisLab can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch17.html" "here">}}
{{</alert>}}

{{<alert class="warning" caption="Attention">}}
You need to uncheck the <field>Enable</field> checkbox in the top left corner to stop profiling. Closing the window will not automatically end the profiling.
{{</alert>}}

## Summary
* Profiling allows you to inspect the behavior of modules and networks including CPU and memory consumption.
* Field value changes can be observed in the Profiler's *Fields* tab.
