---
title: "Example 2: Face Detection with OpenCV"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 856
tags: ["Advanced", "Tutorial", "OpenCV", "Python", "WebCam", "Face Detection"]
menu: 
  main:
    identifier: "thirdpartyexample2"
    title: "Enhance OpenCV WebCam example and build a face detection using MeVisLab, OpenCV and Python."
    weight: 856
    parent: "opencv"
---
# Example 2: Face Detection with OpenCV

## Introduction
This example uses the OpenCV WebCam Python script and adds a basic face detection.

{{<alert class="info" caption="Info">}}
The Python code used in this example has been taken from [Towards Data Science](https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81).
{{</alert>}}

## Steps to do
### Open Example 1
Add the Macro Module developed in [Example 1](/tutorials/thirdparty/opencv/thirdpartyexample1) to your workspace.

### Download trained classifier XML file
Initially you need to download the trained classifier XML file. It is available in the [OpenCV GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml). Save the file somewhere and remember the path for later usage in Python.

### Extend Python file
Right click on your module {{< mousebutton "right" >}}, open the context menu and select {{< menuitem "Related Files" "<YOUR_MODULE_NAME>.py" >}}. The text editor {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MATE">}} opens. You can see the Python file of your module.

You have to load the previously downloaded XML file first.
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
# from mevis import *
import cv2
import OpenCVUtils

_interfaces = []
camera = None
face_cascade = cv2.CascadeClassifier('<YOUR_PATH>/haarcascade_frontalface_default.xml')
```
{{</highlight>}}

After loading the file, go to the previously implemented *grabImage* function and extend it as follows:
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
def grabImage():
  _, img = camera.read()
  updateImage(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
  # Display the output
  cv2.imshow('img', img)
```
{{</highlight>}}

In the end, destroy all OpenCV windows in *releaseCamera* function.
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
def releaseCamera(_):
  global camera, _interfaces
  ctx.removeTimers()
  _interfaces = []
  if camera:
    camera.release()
    camera = None
  cv2.destroyAllWindows()
```
{{</highlight>}}

Opening your Macro Module and pressing *Start* should now open your WebCam stream and an additional OpenCV window which shows a blue rectangle around a detected face.

![Face Detection in MeVisLab using OpenCV](/images/tutorials/thirdparty/bigbang.png "Face Detection in MeVisLab using OpenCV")

## Summary
This is just one example for using OpenCV in MeVisLab. You will find lots of other examples and tutorials online, we just wanted to show one possibility.

{{<alert class="info" caption="Info">}}
You can download the Python file [here](/examples/thirdparty/example2/FaceDetection.py)
{{</alert>}}
