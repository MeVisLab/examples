---
title: "Chapter VII: Application Development"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Advanced", "Tutorial"]
menu: 
  main:
    identifier: "summary"
    title: "Application Development in MeVisLab"
    weight: 800
    parent: "tutorials"
---

# MeVisLab Tutorial Chapter VII {#TutorialChapter7}
## Summary
This chapter will summarize all previous chapters and you will develop a whole application in MeVisLab. The complete workflow from developing a prototype to delivering your final application to your customer is explained step-by-step.

![Prototype to Product](/images/tutorials/summary/Prototyping.png "Prototype to Product")

{{<alert class="warning" caption="Licensing">}}
Some of the features described here will require a separate license. Building an installable executable requires the **MeVisLab ApplicationBuilder** license. It extends the **MeVisLab SDK** so that you can generate an installer of your developed Macro Module.

Free evaluation licenses of the **MeVisLab ApplicationBuilder**, time-limited to 3 months, can be requested at [sales(at)mevislab.de](mailto://sales@mevislab.de).
{{</alert>}}

## Prototype
### Example 1: Develop your network {#DevelopNetwork}
In the first example, you are developing an application based on the following requirements:
* **Requirement 1**: The application shall be able to load DICOM data.
* **Requirement 2**: The application shall provide a 2D and a 3D viewer.
* **Requirement 3**: The 2D viewer shall display the loaded images
* **Requirement 4**: The 2D viewer shall provide the possibility to segment parts of the image based on a RegionGrowing algorithm
  * **Requirement 4.1**: It shall be possible to click into the image for defining a marker position for starting the RegionGrowing
  * **Requirement 4.2**: It shall be possible to define a threshold for the RegionGrowing algorithm
* **Requirement 5**: The 2D viewer shall display the segmentation results as a semi-transparent overlay
  * **Requirement 5.1**: It shall be possible to define the color of the overlay
* **Requirement 6**: The 3D viewer shall visualize the loaded data in a 3-dimensional volume rendering
* **Requirement 7**: The 3D viewer shall additionally show the segmentation result as a 3-dimensional mesh
* **Requirement 8**: The total volume of the segmented area shall be calculated and shown (in ml)
* **Requirement 9**: It shall be possible to toggle the visible 3D objects
  * **Requirement 9.1**: Original data
  * **Requirement 9.2**: Segmentation results
  * **Requirement 9.3**: All

### Example 2: Create your Macro Module
Your network will be encapsulated in a Macro Module for later application development. For details about Macro Modules, see [Example 2.2: Global Macro Modules](/tutorials/basicmechanisms/macromodules/globalmacromodules/).

### Example 3: Develop a User Interface and add Python Scripting {#UIDesign}
Develop the UI and Python Scripts based on your requirements from Example 1. The resulting UI will look like below mockup:

![User Interface Design](/images/tutorials/summary/UIMockUp.png "User Interface Design")

## Review
### Example 4: Write automated tests for your Macro Module
Test your Macro Module in MeVisLab. Your requirements from Example 1 are translated into test cases written in Python. The fields accessible via Python as defined in Example 2 shall be used to test your application.

### Example 5: Create an installable executable
Create a standalone application by using the **MeVisLab ApplicationBuilder** and install the application on another system.

## Refine
### Example 6: Update your network and Macro Module
Integrate feedback from customers having installed your executable and adapt your test cases from Example 4.

### Example 7: Update your installable executable
Re-build your executable and release a new version of your application.

The above loop can easily be repeated until your product completely fulfills your defined requirements.
