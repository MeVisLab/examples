---
title: "Example 3: Segment persons in webcam videos"
date: 2023-05-16
status: "OK"
draft: false
weight: 875
tags: ["Advanced", "Tutorial", "PyTorch", "Python", "PythonPip", "AI", "Segmentation", "WebCam"]
menu: 
  main:
    identifier: "pytorchexample3"
    title: "Segment persons in webcam videos."
    weight: 875
    parent: "pytorch"
---
# Example 3: Segment Persons in WebCam Videos

## Introduction
This tutorial is based on [Example 2: Face Detection with OpenCV](tutorials/thirdparty/opencv/thirdpartyexample2 "Example 2: Face Detection with OpenCV"). You can reuse some of the scripts already developed in the other tutorial.

## Steps to Do
Add the macro module developed in the previous example to your workspace.

![WebCamTest module](images/tutorials/thirdparty/pytorch_example3_1.png "WebCamTest module")

Open the internal network of the module via middle mouse button {{< mousebutton "middle" >}} and right click {{< mousebutton "right" >}} on the tab of the workspace showing the internal network. Select *Show Enclosing Folder*.

![Show Enclosing Folder](images/tutorials/thirdparty/pytorch_example3_2.png "Show Enclosing Folder")

The file browser opens showing the files of your macro module. Copy the *.mlab* file somewhere you can remember.

### Create the Macro Module
Open the the Project Wizard via {{< menuitem "File" "Run Project Wizard">}} and select *Macro Module*. Click *Run Wizard*.

![Project Wizard](images/tutorials/thirdparty/pytorch_example3_3.png "Project Wizard")

Define the module properties as shown below, though you can choose your own name. Click *Next*.

![Module Properties](images/tutorials/thirdparty/pytorch_example3_4.png "Module Properties")

Define the module properties and select the copied *.mlab* file. Make sure to add a Python file and click *Next*.

![Macro Module Properties](images/tutorials/thirdparty/pytorch_example3_5.png "Macro Module Properties")

Leave the module field reference as is and click *Create*. Close Project Wizard and select {{< menuitem "Extras" "Reload Module Database (Clear Cache)">}}.

### Re-use Script and Python Code
Open the script file of the `WebCamTest` module and copy the contents to your new PyTorch module. The result should be something like this:

{{< highlight filename="PyTorchSegmentationExample.script" >}}
```Stan
Interface  {
  Inputs {}
  Outputs {}
  Parameters {}
}

Commands {
  source = $(LOCAL)/PyTorchSegmentationExample.py
}

Window {
  h                = 500
  w                = 500
  destroyedCommand = releaseCamera
  initCommand      = setupInterface
  
  Vertical {
    Horizontal {
      Button {
        title   = Start
        command = startCapture
      }
      Button {
        title   = Pause
        command = stopCapture
      }
    }
    Horizontal {
      expandX = True
      expandY = True
      
      Viewer View2D.self {
        type = SoRenderArea
      }
    }
  }
}
```
{{</highlight>}}

If you open the panel of your new module, you can see the UI elements added. You cannot use the buttons, because they require the Python function called. Copy the Python code to your new module, too.


{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
# from mevis import *
import cv2
import OpenCVUtils

_interfaces = []
camera = None
face_cascade = cv2.CascadeClassifier('C:/tmp/haarcascade_frontalface_default.xml')

# Set up the interface for PythonImage module
def setupInterface():
  global _interfaces
  _interfaces = []
  interface = ctx.module("PythonImage").call("getInterface")
  _interfaces.append(interface)

# Grab image from camera and update
def grabImage():
  _, img = camera.read()
  updateImage(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
  # Display the output
  cv2.imshow('img', img)

# Update image in interface
def updateImage(image):
  _interfaces[0].setImage(OpenCVUtils.convertImageToML(image), minMaxValues = [0,255])

# Start capturing WebCam
def startCapture():
  global camera
  if not camera:
    camera = cv2.VideoCapture(0)
  ctx.callWithInterval(0.1, grabImage)

# Stop capturing WebCam
def stopCapture():
  ctx.removeTimers()

# Release camera in the end
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

You should now have the complete functionality of the [Example 2: Face Detection with OpenCV](tutorials/thirdparty/opencv/thirdpartyexample2 "Example 2: Face Detection with OpenCV").

### Adapt the Network
For *PyTorch*, we require some additional modules in our network. Open the internal network of your module and add another `PythonImage` module. Connect a `Resample3D` and an `ImagePropertyConvert` module.

In `Resample3D` module, define the *Image Size* 693, 520, 1. Change *VoxelSize* for all dimensions to 1.

![Resample3D](images/tutorials/thirdparty/pytorch_example3_7.png "Resample3D")

Open the Panel of the `ImagePropertyConvert` module and check *World Matrix*. 

![ImagePropertyConvert](images/tutorials/thirdparty/pytorch_example3_9.png "ImagePropertyConvert")

Then add a `SoView2DOverlayMPR` module and connect it to the `ImagePropertyConvert` and the `View2D`. Change *Blend Mode* to *Blend*, *Alpha* to something between 0 and 1, and define a color for the overlay.

![SoView2DOverlayMPR](images/tutorials/thirdparty/pytorch_example3_8.png "SoView2DOverlayMPR")

Save the internal network.

### Remove OpenCV-specific Code
We want to use PyTorch for segmentation, therefore you need to add all necessary imports.

{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
import cv2
import OpenCVUtils
from torchvision.io.image import read_image
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights
from torchvision.transforms.functional import to_pil_image
import torch
```
{{</highlight>}}

Additionally, remove the *face_cascade* parameter from your Python code. This was necessary for detecting a face in OpenCV and is not necessary anymore in PyTorch. The only parameters you need here are:

{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
_interfaces = []
camera = None
```
{{</highlight>}}

You can also remove the OpenCV-specific lines in *grabImage*. The function should look like this now:

{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
# Grab image from camera and update
def grabImage():
  _, img = camera.read()
  updateImage(img)
```
{{</highlight>}}

Adapt the function *releaseCamera* and remove the line *cv2.destroyAllWindows()*.

{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
# Release camera in the end
def releaseCamera(_):
  global camera, _interfaces
  ctx.removeTimers()
  _interfaces = []
  if camera:
    camera.release()
    camera = None
```
{{</highlight>}}

### Implement PyTorch Segmentation
The first thing we need is a function for starting the camera. It closes the previous segmentation and calls the existing function *startCapture*.

{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
def startWebcam():
  # Close previous segmentation
  ctx.module("PythonImage1").call("getInterface").unsetImage()
  # Start webcam
  startCapture()
```
{{</highlight>}}

As this function is not called in our user interface, we need to update the *.script* file. Change the first Button to below script:

{{< highlight filename="PyTorchSegmentationExample.script" >}}
```Stan
Button {
  title   = "Start Webcam"
  command = startWebcam
}
```
{{</highlight>}}

Now your new function *startWebcam* is called whenever touching the left button. As a next step, define a Python function *segmentSnapshot*. We are using a pre-trained network from Torchvision. In case you want to use other PyTorch possibilities, you can find lots of examples on their [website](https://pytorch.org/tutorials/).

{{< highlight filename="PyTorchSegmentationExample.py" >}}
```Python
def segmentSnapshot():
  # Step 1: Get image from webcam capture
  stopCapture()
  inImage = ctx.field("PythonImage.output0").image()
  img = inImage.getTile((0,0,0,0,0,0), inImage.imageExtent())[0,0,:,0,:,:]
    
  # Step 2: Convert image into torch tensor
  img = torch.Tensor(img).type(torch.uint8)
    
  # Step 3: Initialize model with the best available weights
  weights = FCN_ResNet50_Weights.DEFAULT
  model = fcn_resnet50(weights=weights)
  model.eval()
    
  # Step 4: Initialize the inference transforms
  preprocess = weights.transforms()
    
  # Step 5: Apply inference preprocessing transforms
  batch = preprocess(img).unsqueeze(0)
    
  # Step 6: Use the model to segment persons in snapshot
  prediction = model(batch)["out"]
  normalized_masks = prediction.softmax(dim=1)
  class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}
  mask = normalized_masks[0, class_to_idx["person"]]
    
  # Step 7: Set output image to module
  interface = ctx.module("PythonImage1").call("getInterface")
  interface.setImage(mask.detach().numpy())
    
  # Step 8: Resize network output to original image size
  origImageSize = inImage.imageExtent()
  ctx.field("Resample3D.imageSize").value = (origImageSize[0], origImageSize[1], origImageSize[2])
```
{{</highlight>}}

In order to call this function, we have to change the command of the right button by adapting the *.script* file.

{{< highlight filename="PyTorchSegmentationExample.script" >}}
```Stan
Button {
  title   = "Segment Snapshot"
  command = segmentSnapshot
}
```
{{</highlight>}}

In step 5, we selected the class *person*. Whenever you click *Segment Snapshot*, PyTorch will try to segment all persons in the video.

{{<alert class="info" caption="Additional information">}}
The following classes are available:
* aeroplane
* bicycle
* bird
* boat
* bottle
* bus
* car
* cat
* chair
* cow
* diningtable
* dog
* horse
* motorbike
* person
* pottedplant
* sheep
* sofa
* train
* tvmonitor
{{</alert>}}

The final result of the segmentation should be a semi-transparent red overlay of the persons segmented in your webcam stream.

![Final Segmentation result](images/tutorials/thirdparty/pytorch_example3_10.png "Final Segmentation result")

## Summary
* You can install additional Python AI packages by using the `PythonPip` module.
* PyTorch trained networks can be used directly in MeVisLab via `PythonImage` module.
* You can integrate AI algorithms into your MeVisLab networks.

{{< networkfile "examples/thirdparty/pytorch1/PyTorchSegmentationExample.zip" >}}
