---
title: "Step 7: Refine - Re-Build Installer"
date: "2023-01-21"
status: "open"
draft: false
weight: 835
tags: ["Advanced", "Tutorial", "Prototyping", "Tool Runner", "Installer"]
menu: 
  main:
    identifier: "summaryexample7"
    title: "Re-build your executable and release a new version of your application."
    weight: 835
    parent: "summary"
---
# Step 7: Refine - Rebuild Installer

{{< youtube "E0GnWPXT8Og" >}}

## Introduction
In this step you are recreating your application installer after changing the UI in previous [Step 6: Refine - Update Application](/tutorials/summary/summary6/).

## Steps to Do
### Update the *.mlinstall* File
You do not need to use the Project Wizard now, because you already have a valid *.mlinstall* file. The location should be in your package under *.\Configuration\Installers\TutorialSummary*. Open the file in any text editor and search for the *$VERSION 0.5*. Change the version to something else, in our case, we now have our first major release 1.0.

{{<alert class="info" caption="Info">}}
You can also run the Project Wizard again but keep in mind that manual changes on your *.mlinstall* file might be overwritten. The wizard recreates your *.mlinstall* file whereas the ToolRunner just uses it.
{{</alert>}}

### Use MeVisLab ToolRunner
Save the file and open *MeVisLab ToolRunner*. 

![MeVisLab ToolRunner](/images/tutorials/summary/Example7_1.png "MeVisLab ToolRunner")

Open the *.mlinstall* file in ToolRunner and select the file. Click *Run on Selection*.

![Run on Selection](/images/tutorials/summary/Example7_2.png "Run on Selection")

The ToolRunner automatically builds your new installer using version 1.0.

### Install Application Again
Execute your installable executable again. You do not have to uninstall previous version(s) of your application first. Already existing applications will be replaced by new installation - at least if you select the same target directory.

![Install new version](/images/tutorials/summary/Example7_3.png "Install new version")

The installer already shows your updated version 1.0. It is not necessary to select your runtime license again because it has not been touched during update.

![Application version 1.0](/images/tutorials/summary/Example7_4.png "Application version 1.0")

The new installed application now provides your new UI element for defining the alpha value of the overlay.

## Summary
* Updates of your application installer can be applied by using the MeVisLab ToolRunner.
* The executable can be updated on your customers system(s) and your changes on the macro module and network(s) are applied.
