---
title: "Structure of this Documentation"
date: 2022-06-15T08:54:53+02:00
draft: false
---
# Structure of this Documentation
In the main menu you will find the topic `Tutorials` which shows an overview of the different chapters we currently describe.

The following chapters are available:
* [Basic Mechanisms of MeVisLab](#BasicMechanisms)
* [Open Inventor](#OpenInventor)
* [Visualization](#Visualization)
* [Image Processing](#ImageProcessing)
* [Data Objects](#DataObjects)
* [Macro Modules and Module interactions via Python scripting](#Modules)

Each of these chapters provides examples you can try yourself, explanations about the used Modules and links to our [YouTube channel](https://www.youtube.com/channel/UCUGi64NseroIGjga8l7EX8g) where you can find videos for each tutorial.

The examples always give a short introduction, explain the steps to do and in the end sometimes provide additional ideas to improve the developed networks yourself. In addition to that, we created a [Glossary](../tutorials/tutorials/##tutorial_glossary) where you can find explanations of terms used in this document.

Very important information is always marked like this:
{{<alert class="info" caption="Info">}}
This is an Information Text providing additional links or info on the current topic.
{{</alert>}}
{{<alert class="check" caption="Check">}}
This is a Check Text to show you that something else needs to be done by you.
{{</alert>}}
{{<alert class="warning" caption="Warning">}}
This is a Warning which shows you important hints or things you should not do.
{{</alert>}}

Keyboard shortcuts are highlighted like this: {{< keyboard "CTRL" "ALT" "2" >}}.

## Basic Mechanisms of MeVisLab {#BasicMechanisms}
In this chapter you will learn the basic mechanics of the MeVisLab IDE. You will learn how to re-use existing Modules to load and view data, and you will build your first processing pipeline.
## Open Inventor {#OpenInventor}
Beside blue modules (ML Modules) and brown macro modules, there is a third type of modules, called `Open Inventor` modules. These modules are green and start with the letters `So\*` (for `Scene Objects`). Open Inventor Modules process and render 3D scene objects and enable image interactions.
## Visualization {#Visualization}
MeVisLab contains a whole toolkit to visualize data and images. 2D, 3D and 4D rendering is possible as well as the interaction with images. Visualization is a key functionality in MeVisLab and provides lots of examples how to visualize your data.
## Image Processing {#ImageProcessing}
Image Processing means filtering and transforming images, evaluating image statistics and executing arithmetic operations on images.
## Data Objects {#DataObjects}
MeVisLab provides a lot of pre-defined data objects for usage in MeVisLab, such as:
* [Contours](../tutorials/dataobjects/contours/contour-objects#CSO)
* [Surface Objects](../tutorials/dataobjects/surfaces/surface-objects/#Introduction)
* [Markers](../tutorials/dataobjects/markers/#MarkersInMeVisLab)
## Macro Modules and Module interactions via Python scripting {#Modules}
Macro Modules encapsulate the functionality of a Network in a single Macro Module. The Macro Module may have an own user interface which can be scripted via Python Scripting.