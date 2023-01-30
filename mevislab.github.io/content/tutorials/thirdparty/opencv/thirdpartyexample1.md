---
title: "Example 1: WebCam access with OpenCV"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Advanced", "Tutorial", "OpenCV", "Python", "WebCam", "Macro", "Macro Modules", "Global Macro"]
menu: 
  main:
    identifier: "thirdpartyexample1"
    title: "Access your webcam and use the live video in MeVisLab via OpenCV."
    weight: 855
    parent: "opencv"
---
# Example 1: WebCam access with OpenCV

## Introduction
In this example, we are using the `PythonImage` module and access your WebCam to show the video in a `View2D`.

## Steps to do
### Creating the network to be used for testing
Add the modules to your workspace and connect them as seen below. 

![Example Network ](/images/tutorials/thirdparty/network_example1.png "Example Network ")

The viewer is empty because the image needs to be set via Python scripting.

{{<alert class="info" caption="Info">}}
More information about the `PythonImage` module can be found {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/PythonImage.html" "here" >}}
{{</alert>}}

### Create a Macro Module
Now you need to create a Macro Module from your network. You can either group your modules, create a local Macro and convert it to a global Macro Module, or you use the Project Wizard and load your \*.mlab file.

{{<alert class="info" caption="Info">}}
A tutorial how to create your own Macro Modules can be found in [Example 2.2: Global Macro Modules](/tutorials/basicmechanisms/macromodules/globalmacromodules "Example 2.2: Global Macro Modules"). Make sure to add a Python file to your Macro Module.
{{</alert>}}

### Add the View2D to your UI
Next, we need to add the `View2D` to a Window of your Macro Module. Right click on your module {{< mousebutton "right" >}}, open the context menu and select {{< menuitem "Related Files" "<YOUR_MODULE_NAME>.script" >}}. The text editor {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MATE">}} opens. You can see the \*.script file of your module.

Add the following to your file:
{{< highlight filename="<YOUR_MODULE_NAME>.script" >}}
```Stan
Interface  {
  Inputs {}
  Outputs {}
  Parameters {}
}

Commands {
  source = $(LOCAL)/<YOUR_MODULE_NAME>.py
}

Window {
  h = 500
  w = 500
  initCommand = setupInterface
  destroyedCommand = releaseCamera
  
  Vertical {
    Horizontal {
      Button {
        title = Start
        command = startCapture
      }
      Button {
        title = Pause
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

Now open the Python file of your module and define the commands to be called from the \*.script file:
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
# from mevis import *

# Setup the interface for PythonImage module
def setupInterface():
  pass

# Release camera in the end
def releaseCamera(_):
  pass

# Start capturing WebCam
def startCapture():
  pass

# Stop capturing WebCam
def stopCapture():
  pass

```
{{</highlight>}}

### Use OpenCV
Your `View2D` is still empty, lets get access to the WebCam and show the video in your module. Open the Python file of your network again and enter the following code:
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
# from mevis import *
import cv2
import OpenCVUtils

_interfaces = []
camera = None

# Setup the interface for PythonImage module
def setupInterface():
  global _interfaces
  _interfaces = []
  interface = ctx.module("PythonImage").call("getInterface")
  _interfaces.append(interface)

# Release camera in the end
def releaseCamera(_):
  pass

# Start capturing WebCam
def startCapture():
  pass

# Stop capturing WebCam
def stopCapture():
  pass
```
{{</highlight>}}

We now imported *cv2* and *OpenCVUtils* so that we can use them in Python. Additionally we defined a list of *_interfaces* and a *camera*. The import of *mevis* is not necessary for this example.

The *setupInterfaces* function is called whenever the *Window* of your module is opened. Here we are getting the interface of the `PythonImage` module and append it to our global list.

### Access the WebCam
Now we want to start capturing the camera.
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
# Start capturing WebCam
def startCapture():
  global camera
  if not camera:
    camera = cv2.VideoCapture(0)
  ctx.callWithInterval(0.1, grabImage)

# Grab image from camera and update
def grabImage():
  _, img = camera.read()
  updateImage(img)

# Update image in interface
def updateImage(image):
  _interfaces[0].setImage(OpenCVUtils.convertImageToML(image), minMaxValues = [0,255])
```
{{</highlight>}}

The *startCapture* function gets the camera from the *cv2* object if not already available. Then it calls the current MeVisLab network context and creates a timer which calls a *grabImage* function every 0.1 seconds.

The *grabImage* function reads an image from the *camera* and calls *updateImage*. The interface from the `PythonImage` module is used to set the image from the WebCam. The MeVisLab *OpenCVUtils* convert the OpenCV image to the MeVisLab image format *MLImage*.

Next, we define what happens if you click the *Pause* button.
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
...
# Stop capturing WebCam
def stopCapture():
  ctx.removeTimers()
...
```
{{</highlight>}}

As we started a timer in our network context which updates the image every 0.1 seconds, we just stop this timer and the camera is paused.

In the end, we need to release the camera whenever you close the Window of your Macro Module.
{{< highlight filename="<YOUR_MODULE_NAME>.py" >}}
```Python
...
# Release camera in the end
def releaseCamera(_):
  global camera, _interfaces
  ctx.removeTimers()
  _interfaces = []
  if camera:
    camera.release()
    camera = None
...
```
{{</highlight>}}

Again, the timers are removed, all interfaces are reset and the camera is released. The light indicating WebCam usage should turn off.

Opening your Macro Module via double-click {{< mousebutton "left" >}} should now allow to start and pause your WebCam video in MeVisLab. You can modify your internal network using a `Convolution` filter module or any other module available in MeVisLab for modifying the stream on the fly.

## Summary
* The `PythonImage` module allows to use Python for defining the image output
* OpenCV can be used in MeVisLab via Python scripting
* Images and videos from OpenCV can be used in MeVisLab networks

{{<alert class="info" caption="Info">}}
You can download the Python file [here](/examples/thirdparty/example1/OpenCVExample.zip)
{{</alert>}}
