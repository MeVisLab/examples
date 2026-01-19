---
title: "Chapter VIII: Third-party Components"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 850
tags: ["Advanced", "Tutorial", "Third-party"]
menu: 
  main:
    identifier: "thirdparty"
    title: "Usage of Third-party Software Integrated into MeVisLab"
    weight: 850
    parent: "tutorials"
---

# MeVisLab Tutorial Chapter VIII {#TutorialChapter8}

## Using Third-party Software Integrated into MeVisLab {#TutorialThirdParty}
MeVisLab is equipped with a lot of useful software right out of the box, like the Insight Segmentation and Registration Toolkit (ITK) or the Visualization Toolkit (VTK). This chapter works as a guide on how to use some of the third-party components integrated in MeVisLab for your projects via Python scripting.

{{<alert class="info" caption="Additional Information">}}
You will also find instructions to install and use any Python package (e.g., PyTorch) in MeVisLab using the `PythonPip` module. 
{{</alert>}}

### OpenCV
[OpenCV](https://opencv.org/ "OpenCV") (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. 
OpenCV includes, among others, algorithms to:
* detect and recognize faces
* identify objects
* classify human actions on video
* track camera movements
* track moving objects
* extract 3D models of objects
* produce 3D point clouds from stereo cameras
* stitch images together to produce a high resolution image of an entire scene
* find similar images from an image database
* remove red eyes from images taken using flash
* follow eye movements
* recognize scenery 
* establish markers to overlay with augmented reality

### assimp
The [THE ASSET IMPORTER LIBRARY](http://www.assimp.org/) supports loading and processing geometric scenes from various well known 3D formats. MeVisLab uses assimp to import these files and reuses the scenes directly in MeVisLab.

A list of supported formats can be found [here](https://assimp-docs.readthedocs.io/en/v5.1.0/about/introduction.html).

### PyTorch \[*not integrated initially*\]
[PyTorch](http://www.pytorch.org) is a machine learning framework based on the Torch library, used for applications such as Computer Vision and Natural Language Processing, originally developed by Meta AI and now part of the Linux Foundation umbrella.

The tutorials available here shall provide examples on how to integrate AI into MeVisLab. You can also integrate other Python AI packages the same way.

### Matplotlib
[Matplotlib](https://matplotlib.org/) is a library for creating static, animated, and interactive visualizations in Python.

* create publication quality plots
* Make interactive figures that can be zoomed, panned, and updated
* Customize visual style and layout
* Export to many file formats
