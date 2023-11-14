---
title: "Tips and Tricks"
date: 2023-11-13
status: "OK"
draft: false
weight: 890
tags: ["Basic", "Tutorial"]
menu: 
  main:
    identifier: "shorts"
    title: "Short Tips and Tricks in MeVisLab"
    weight: 890
    parent: "tutorials"
---

# MeVisLab Tips and Tricks

This chapter shows some features and functionalities which are helpful but do not provide its own tutorial.

* [Using Snippets](/tutorials/shorts#snippets)
* [Scripting Assistant](/tutorials/shorts#scriptingassistant)

## Using Snippets {#snippets}

{{< youtube "xX7wJiyfxhA" >}}

Sometimes you have to create the same network over and over again -- for example, to quickly preview DICOM files. Generally, you will at least add one module to load and another module to display your images. Sometimes you may also want to view the DICOM header data. A network you possibly generate whenever opening DICOM files will be the following:

![Open DICOM files](/images/tutorials/Snippets_Network.png "Open DICOM files")

Create a snippet of your commonly used networks by adding the snippets list from the main menu. Open {{< menuitem "View" "Views" "Snippets List">}}. A new panel is shown. Select all modules of your network and double-click *New...* in your *Snippets List*.

Enter a name for your snippet like *DICOM Viewer* and click *Add*.

A new snippet will be shown in your Snippets List. You can drag and drop the snippet to your workspace and the modules are re-used, including all defined field values.

![Snippets List](/images/tutorials/Snippets_Panel.png "Snippets List")

## Scripting Assistant {#scriptingassistant}

{{< youtube "y6110PW5N_w" >}}

If you are new to Python or don't have experiences in accessing fields in MeVisLab via Python scripting, the Scripting Assistant might help you.

Open {{< menuitem "View" "Views" "Scripting Assistant">}}. A new panel is shown. 

If you now interact with a network, module or macro module, your user interactions are converted into Python calls. You can see the calls in the panel of the Scripting Assistant and copy and paste them for your Python script.

![Scripting Assistant](/images/tutorials/ScriptingAssistant_Panel.png "Scripting Assistant")
