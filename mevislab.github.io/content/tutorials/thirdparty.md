---
title: "Chapter VIII: ThirdParty components"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
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