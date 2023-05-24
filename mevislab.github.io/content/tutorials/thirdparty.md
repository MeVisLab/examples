---
title: "Chapter VIII: ThirdParty components"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 850
tags: ["Advanced", "Tutorial", "ThirdParty"]
menu: 
  main:
    identifier: "thirdparty"
    title: "Usage of ThirdParty software integrated into MeVisLab"
    weight: 850
    parent: "tutorials"
---

# MeVisLab Tutorial Chapter VIII {#TutorialChapter8}

## Using ThirdParty software integrated into MeVisLab {#TutorialThirdParty}
MeVisLab comes with a lot of software already integrated and ready to use. Even if these tools are not available as a module, like itk and vtk for example, they can be used via Python scripting. This chapter shall give some examples of how to use a selection of integrated ThirdParty components.

{{<alert class="info" caption="Additional Information">}}
PyTorch is not directly integrated into MeVisLab. These tutorials additionally explain how you can install and use any Python packages in MeVisLab by using the `PythonPip` module.
{{</alert>}}

### OpenCV
[OpenCV](https://opencv.org/ "OpenCV") (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV includes algorithms to:
* detect and recognize faces,
* identify objects,
* classify human actions in video,
* track camera movements,
* track moving objects,
* extract 3D models of objects,
* produce 3D point clouds from stereo cameras,
* stitch images together to produce a high resolution image of an entire scene,
* find similar images from an image database,
* remove red eyes from images taken using flash,
* follow eye movements,
* recognize scenery and
* establish markers to overlay it with augmented reality, etc.

### assimp
The [THE ASSET IMPORTER LIBRARY](http://www.assimp.org/) supports loading and processing geometric scenes from various well known 3D formats. MeVisLab uses assimp to import these files and use the scenes directly in MeVisLab.

A list of supported formats can be found [here](https://assimp-docs.readthedocs.io/en/v5.1.0/about/introduction.html).

### PyTorch \[*not integrated initially*\]
[PyTorch](http://www.pytorch.org) is a machine learning framework based on the Torch library, used for applications such as Computer Vision and Natural Language Processing, originally developed by Meta AI and now part of the Linux Foundation umbrella.

The tutorials available here shall provide examples how to integrate AI into MeVisLab. You can also integrate other Python AI packages the same way.

### matplotlib
[Matplotlib](https://matplotlib.org/) is a library for creating static, animated, and interactive visualizations in Python.

* Create publication quality plots.
* Make interactive figures that can zoom, pan, update.
* Customize visual style and layout.
* Export to many file formats.
