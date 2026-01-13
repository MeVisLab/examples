---
title: "Example 3: Camera Interactions in Open Inventor"
date: "2023-03-22"
draft: false
weight: 530
status: "OK"
tags: ["Beginner", "Tutorial", "Open Inventor", "3D", "Camera", "Perspective Camera", "Orthographic Camera"]
menu: 
  main:
    identifier: "camerainteractions"
    title: "Examples for camera interactions in Open Inventor"
    weight: 530
    parent: "openinventor"
---

# Example 3: Camera Interactions in Open Inventor {#CameraInteraction}

{{< youtube "J6qtN8QfPEc" >}}

## Introduction
In this example, we are learning the basic principles of camera interactions in Open Inventor. We will show the difference between a `SoRenderArea` and a `SoExaminerViewer` and use different modules of the `SoCamera*` group.

## The `SoRenderArea` module
The module `SoRenderArea` is a simple renderer for Open Inventor scenes. It offers functionality to record movies and to create snapshots, but does not include an own camera or light.

Add a `SoBackground`, a `SoMaterial` and a `SoOrientationModel` module to your workspace and connect them to a `SoGroup`. Add a `SoRenderArea` to the `SoGroup` and open the viewer.

![SoRenderArea without camera and lights](images/tutorials/openinventor/Camera_1.png "SoRenderArea without camera and lights")

You can not interact with your scene and the rendered content is very dark. Open the `SoOrientationModel` and change *Model* to *Skeleton* to see that a little better. You can also change the material by using the panel of the `SoMaterial` module.

Add a `SoCameraInteraction` module and connect it between the `SoGroup` and the `SoRenderArea`.

![SoRenderArea with SoCameraInteraction](images/tutorials/openinventor/Camera_2.png "SoRenderArea with SoCameraInteraction")

The `SoCameraInteraction` does not only allow you to change the camera position in your scene but also adds light. The module automatically adds a headlight you can switch off in the fields of the module.

{{< imagegallery 2 "images/tutorials/openinventor" "Headlight_TRUE" "Headlight_FALSE" >}}

The `SoCameraInteraction` can also be extended by a `SoPerspectiveCamera` or a `SoOrthographicCamera`. Add a `SoSwitch` to your `SoGroup` and connect a `SoPerspectiveCamera` and a `SoOrthographicCamera`.

![SoPerspectiveCamera and SoOrthographicCamera](images/tutorials/openinventor/Camera_3.png "SoPerspectiveCamera and SoOrthographicCamera")

You can now switch between both cameras, but you can not interact with them in the viewer. Select the `SoCameraInteraction` and toggle *detectCamera*. Now the default camera of the `SoCameraInteraction` is replaced by the camera selected in the `SoSwitch`. 

Whenever you change the camera in the switch, you need to detect the new camera in the `SoCameraInteraction`.

{{< imagegallery 2 "images/tutorials/openinventor" "SoPerspectiveCamera" "SoOrthographicCamera" >}}

A `SoPerspectiveCamera` camera defines a perspective projection from a viewpoint.

The viewing volume for a perspective camera is a truncated pyramid. By default, the camera is located at (0,0,1) and looks along the negative z-axis; the Position and Orientation fields can be used to change these values. The Height Angle field defines the total vertical angle of the viewing volume; this and the Aspect Ratio field determine the horizontal angle.

A `SoOrthographicCamera` camera defines a parallel projection from a viewpoint.

This camera does not diminish objects with distance, as an SoPerspectiveCamera does. The viewing volume for an orthographic camera is a cuboid (a box).

By default, the camera is located at (0,0,1) and looks along the negative z-axis; the Position and Orientation fields can be used to change these values. The Height field defines the total height of the viewing volume; this and the Aspect Ratio field determine its width.

Add a `SoCameraWidget` and connect it to your `SoGroup`. 

![SoCameraWidget](images/tutorials/openinventor/Camera_3.png "SoCameraWidget")

This module shows a simple widget on an Inventor viewer that can be used to rotate, pan, or zoom the scene. You can configure the *Main Interaction* in the panel of the `SoCameraWidget`.

You can also add more than one widget to show multiple widgets in the same scene, see example network of the `SoCameraWidget` module.

## The `SoExaminerViewer` module
The `SoExaminerViewer` makes some things much easier, because a camera and a light are already integrated. 

Add a `SoExaminerViewer` to your workspace and connect it to the `SoBackground`, the `SoMaterial` and the `SoOrientationModel` modules.

![SoExaminerViewer](images/tutorials/openinventor/Camera_4.png "SoExaminerViewer")

The difference to the `SoRenderArea` can be seen immediately. You can interact with your scene and a light is available initially.

The module also allows you to switch between perspective and orthographic camera by changing the field *cameraType*.

{{< imagegallery 2 "images/tutorials/openinventor" "SoExaminerViewer_Perspective" "SoExaminerViewer_Orthographic" >}}

The module also provides UI elements to interact.

## Summary
* MeVisLab provides multiple options for adding a camera to a scene
* The `SoExaminerViewer` already has an integrated camera and light, the `SoRenderArea` requires additional modules.
* You can use perspective and orthographic cameras

{{< networkfile "examples/open_inventor/example3/CameraInteractions.mlab" >}}
