---
title: "Example 2: Profiling in MeVisLab"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Profiling"]
menu: 
  main:
    identifier: "testingexample2"
    title: "Enabling the profiler and inspecting the behavior of your network"
    weight: 760
    parent: "testing"
---
# Example 2: Profiling in MeVisLab

{{< youtube "DZ4BcAne4hM" >}}

## Introduction
In this example, we are using the MeVisLab Profiler to inspect the memory and CPU consumption of the modules in an example network.

## Steps to do
### Creating the network to be used for profiling
You can open any network you like, here we are using the example network of the module `MinMaxScan` for profiling. Add the module `MinMaxScan` to your workspace and open the example network via right-click {{<mousebutton "right">}} and selecting {{<menuitem "Help" "Show Example Network">}}.

![MinMaxScan Example Network](/images/tutorials/testing/profiling_network.png "MinMaxScan Example Network")

### Enable Profiling
Next, enable the MeVisLab Profiler via menu item {{<menuitem "View" "Views" "Profiling">}}. The Profiler is opened in your Views Area but can be detached and dragged over the workspace via left mouse button {{<mousebutton "left">}}.

![MeVisLab Profiling](/images/tutorials/testing/Profiling.png "MeVisLab Profiling")

Enable profiling by checking *Enable* in the top left corner.

### Inspect your network
Now open the `View2D` via double-click and scroll through the slices. Inspect the Profiler.

![MeVisLab Profiling Network](/images/tutorials/testing/Profiling_Network1.png "MeVisLab Profiling Network")

The Profiler shows very detailed information about each module in your network. 

{{<alert class="info" caption="Info">}}
By default, used macro modules are not shown in the Profiler. You need to check *Show macros* first, in order to see the profiling of the `View2D` and the `LocalImage` module.
{{</alert>}}

You can filter by module name in case of large networks so that you only get the information you need.

The *Fields* tab shows any changes of field values in your network.

![MeVisLab Profiling Fields](/images/tutorials/testing/Profiling_Network2.png "MeVisLab Profiling Fields")

In addition to the Profiler view, your modules also provide a tiny bar showing the current memory and time consumption of the module.

![MeVisLab Profiling Module](/images/tutorials/testing/Module_Info.png "MeVisLab Profiling Module")

{{<alert class="info" caption="Info">}}
More information about profiling in MeVisLab can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch17.html" "here">}}
{{</alert>}}

{{<alert class="warning" caption="Attention">}}
You need to uncheck the *Enable* checkbox in the top left corner to stop profiling. Closing the window will not automatically end the profiling.
{{</alert>}}

## Summary
* Profiling allows you to inspect the behavior of modules and networks including CPU and memory consumption.
* Field value changes in the entire network are also shown.