---
title: "Structure of this Documentation"
date: 2022-06-15T08:54:53+02:00
draft: false
---
# Structure of this Documentation
In the main menu you will find the topic `Tutorials` which shows an overview of the different chapters we currently describe.
## Overview
The following chapters are available:
* [Chapter I: Basic Mechanisms of MeVisLab](tutorials/basicmechanisms/)
  * [Macro Modules and Module interactions via Python scripting](tutorials/basicmechanisms/macromodules/)
* [Chapter II: Open Inventor](tutorials/openinventor/)
* [Chapter III: Visualization](tutorials/visualization/)
* [Chapter IV: Image Processing](tutorials/image_processing/)
* [Chapter V: Data Objects](tutorials/dataobjects/)
* [Chapter VI: Testing](tutorials/testing/)
* [Chapter VII: Application Development](tutorials/summary/)
* [Chapter VIII: ThirdParty components](tutorials/thirdparty/)

Each of these chapters provides examples you can try yourself, explanations about the used Modules and links to our [YouTube channel](https://www.youtube.com/channel/UCUGi64NseroIGjga8l7EX8g) where you can find videos for each tutorial.

The examples always give a short introduction, explain the steps to do and in the end sometimes provide additional ideas to improve the developed networks yourself. In addition to that, we created a [Glossary](/tutorials/introduction/#tutorial_glossary) where you can find explanations of terms used in this document.

# Information Boxes
Very important information is always marked like this:
## Info
{{<alert class="info" caption="Info">}}
This is an Information Text providing additional links or info on the current topic.
{{</alert>}}
## Check
{{<alert class="check" caption="Check">}}
This is a Check Text to show you that something else needs to be done by you.
{{</alert>}}
## Warning
{{<alert class="warning" caption="Warning">}}
This is a Warning which shows you important hints or things you should not do.
{{</alert>}}

# Keyboard Shortcuts
Keyboard shortcuts are highlighted like this: {{< keyboard "CTRL" "ALT" "2" >}}.

# Chapters
## Basic Mechanisms of MeVisLab {#BasicMechanisms}
In this chapter you will learn the basic mechanics of the MeVisLab IDE. You will learn how to re-use existing Modules to load and view data, and you will build your first processing pipeline.
### Macro Modules and Module interactions via Python scripting {#Modules}
Macro Modules encapsulate the functionality of a Network in a single Macro Module. The Macro Module may have an own user interface which can be scripted via Python Scripting.

Macro Modules are explained as a part of the basic mechanics.
## Open Inventor {#OpenInventor}
Beside blue modules (ML Modules) and brown macro modules, there is a third type of modules, called `Open Inventor` modules. These modules are green and start with the letters `So\*` (for `Scene Objects`). Open Inventor Modules process and render 3D scene objects and enable image interactions.
## Visualization {#Visualization}
MeVisLab contains a whole toolkit to visualize data and images. 2D, 3D and 4D rendering is possible as well as the interaction with images. Visualization is a key functionality in MeVisLab and provides lots of examples how to visualize your data.
## Image Processing {#ImageProcessing}
Image Processing means filtering and transforming images, evaluating image statistics and executing arithmetic operations on images.
## Data Objects {#DataObjects}
MeVisLab provides a lot of pre-defined data objects for usage in MeVisLab, such as:
* [Contours](tutorials/dataobjects/contourobjects#CSO)
* [Surface Objects](tutorials/dataobjects/surfaceobjects#Introduction)
* [Markers](tutorials/dataobjects/markerobjects#MarkersInMeVisLab)
* [Curves](tutorials/dataobjects/curves#CurvesInMeVisLab)
## Testing, Profiling and Debugging {#Testing}
The MeVisLab IDE provides tools for writing automated tests in Python, profiling your network performance and debugging your Python code.
## ThirdParty components {#ThirdParty}
Examples for using integrated ThirdParty components such as *OpenCV* or *Matplotlib* are explained in this chapter.

# YouTube
Some of our tutorials are also available on [YouTube](https://www.youtube.com/channel/UCUGi64NseroIGjga8l7EX8g). They are marked like this on top of the tutorial:
{{< youtube "dzUEg3wvc9w" >}}

# Example networks
The networks used in the tutorials and many more examples can be found in the [Examples](/examples) section of this page. The related example network of a tutorial is available at the end of each page and marked like this:
{{< networkfile "examples/basic_mechanisms/contour_filter/" >}}