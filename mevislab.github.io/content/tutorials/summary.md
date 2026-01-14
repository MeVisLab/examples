---
title: "Chapter VII: Application Development"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 800
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
This chapter will summarize all previous chapters and you will develop an entire application in MeVisLab. The complete workflow from developing a prototype to delivering your final application to your customer is explained step-by-step.

![Prototype to Product](images/tutorials/summary/Prototyping.png "Prototype to Product")

{{<alert class="warning" caption="Licensing">}}
Some of the features described here will require a separate license. Building an installable executable requires the **MeVisLab ApplicationBuilder** license. It extends the **MeVisLab SDK** so that you can generate an installer of your developed macro module.

Free evaluation licenses of the **MeVisLab ApplicationBuilder**, time-limited to three months, can be requested at [sales(at)mevislab.de](mailto://sales@mevislab.de).
{{</alert>}}

## Prototype
### Step 1: Develop your network {#DevelopNetwork}
In the first step, you are developing an application based on the following requirements:
* **Requirement 1**: The application shall be able to load DICOM data
* **Requirement 2**: The application shall provide a 2D and a 3D viewer
* **Requirement 3**: The 2D viewer shall display the loaded images
* **Requirement 4**: The 2D viewer shall provide the possibility to segment parts of the image based on a region growing algorithm
  * **Requirement 4.1**: It shall be possible to click into the image for defining a marker position for starting the  region growing algorithm
  * **Requirement 4.2**: It shall be possible to define a threshold for the region growing algorithm
* **Requirement 5**: The 2D viewer shall display the segmentation results as a semitransparent overlay
  * **Requirement 5.1**: It shall be possible to define the color of the overlay
* **Requirement 6**: The 3D viewer shall visualize the loaded data in a three-dimensional volume rendering
* **Requirement 7**: The 3D viewer shall additionally show the segmentation result as a three-dimensional mesh
* **Requirement 8**: The total volume of the segmented area shall be calculated and shown (in ml)
* **Requirement 9**: It shall be possible to toggle the visible 3D objects
  * **Requirement 9.1**: Original data
  * **Requirement 9.2**: Segmentation results
  * **Requirement 9.3**: All

### Step 2: Create Your Macro Module
Your network will be encapsulated in a macro module for later application development. For details about macro modules, see [Example 2.2: Global macro modules](tutorials/basicmechanisms/macromodules/globalmacromodules/).

### Step 3: Develop a User Interface and Add Python Scripting {#UIDesign}
Develop the UI and Python Scripts based on your requirements from Step 1. The resulting UI will look like the below mockup:

![User Interface Design](images/tutorials/summary/UIMockUp.png "User Interface Design")

## Review
### Step 4: Write Automated Tests for Your Macro Module
Test your macro module in MeVisLab. Your requirements from Step 1 are translated into test cases written in Python. The fields accessible via Python as defined in Step 2 shall be used to test your application.

### Step 5: Create an Installable Executable
Create a standalone application by using the **MeVisLab ApplicationBuilder** and install the application on another system.

## Refine
### Step 6: Update Your Network and Macro Module
Integrate feedback from customers having installed your executable and adapt your test cases from Step 4.

### Step 7: Update Your Installable Executable
Rebuild your executable and release a new version of your application.

The above loop can easily be repeated until your product completely fulfills your defined requirements.
