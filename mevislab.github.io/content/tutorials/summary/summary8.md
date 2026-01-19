---
title: "Extra: Run Your Application in a Browser"
date: "2023-02-24"
status: "open"
draft: false
weight: 840
tags: ["Advanced", "Tutorial", "Prototyping", "Browser", "Web"]
menu: 
  main:
    identifier: "summaryexample8"
    title: "Adapt an Existing Application to Run in a Browser"
    weight: 840
    parent: "summary"
---

# Extra: Run Your Application in a Browser

{{< youtube "XgOyeu65f7Q" >}}

## Introduction
This step explains how to run your developed application in a browser. The MeVisLab network remains the same, only some adaptations are necessary for running any macro module in a browser window.

{{<alert class="warning" caption="Licensing">}}
This step requires a valid **MeVisLab Webtoolkit** license. It extends the **MeVisLab SDK**, so that you can develop web macro modules.

Free evaluation licenses of the **MeVisLab Webtoolkit**, time-limited to three months, can be requested at [sales(at)mevislab.de](mailto://sales@mevislab.de).
{{</alert>}}

## Steps to Do
Make sure to have your macro module from previous [Step 2](tutorials/summary/summary2/) available.

### Create a Web Macro Module
Open Project Wizard via {{< menuitem "File" "Run Project Wizard..." >}} and select *Web Macro module*. Run the Wizard and enter details of your new macro module.

![Web macro module wizard](images/tutorials/summary/Example8_1.png "Web macro module wizard")

Run the Wizard and enter details of your web macro module.

![Web macro module properties](images/tutorials/summary/Example8_2.png "Web macro module properties")

Click *Next* and select optional web plugin features. Click *Create*.

![Web macro module](images/tutorials/summary/Example8_3.png "Web macro module")

The folder of your project automatically opens in an Explorer window.

### Using Your Web Macro Module
As you created a global web macro module, you can search for it in the MeVisLab *Module Search*. In the case the module cannot be found, select {{< menuitem "Extras" "Reload Module Database (Clear Cache)" >}}.

![Web macro module](images/tutorials/summary/Example8_4.png "Web macro module")

The internal network of your module is empty. We will reuse the internal network of your macro module developed in [Step 2](tutorials/summary/summary2/).

#### Add the Internal Network of Your Application
Open the internal network of your previously created macro module from [Step 2](tutorials/summary/summary2/). Select all and copy to your internal network of the *TutorialSummaryBrowser* module. Save the internal network and close the tab in MeVisLab.

![Internal network](images/tutorials/summary/Example8_5a.png "Internal network")

We are going to develop a web application; therefore, we need special `RemoteRendering` modules for the viewer. Add two `RemoteRendering` modules and a `SoCameraInteraction` to your workspace and connect them to your existing modules as seen below.

![Remote Rendering](images/tutorials/summary/Example8_5b.png "Remote Rendering")

{{<alert class="info" caption="Additional Info">}}
We are using the hidden outputs of the `View2D` and the `SoExaminerViewer`. You can show them by pressing the *SPACE* key.
{{</alert>}}

#### Develop the User Interface
Make sure to have both macro modules visible in MeVisLab SDK, we are reusing the *.script* and *.py* files developed in [Step 3](tutorials/summary/summary3/).

![Macro modules](images/tutorials/summary/Example8_6.png "Macro modules")

Right-click {{< mousebutton "right" >}} the module *TutorialSummaryBrowser* and select {{< menuitem "Related Files" "TutorialSummaryBrowser.script" >}}.

The file opens in MATE and you will see that it looks similar to the *.script* file of a normal macro module. The only difference is an additional *Web* section at the end of the file. It defines the locations of some *JavaScript* libraries and the *URL* to be used for a preview of your website.

{{< highlight filename="TutorialSummaryBrowser.script" >}}
```Stan
Web {
  plugin = "$(MLAB_MeVisLab_Private)/Sources/Web/application/js/jquery/Plugin.js"
  plugin = "$(MLAB_MeVisLab_Private)/Sources/Web/application/js/yui/Plugin.js"
  
  // Specify web plugins here. If you have additional JavaScript files, you can load them from 
  // the plugin. It is also possible to load other plugins here.
  plugin = "$(LOCAL)/www/js/Plugin.js"

  Deployment {
    // Deploy the www directory recursively when building web application installers
    directory = "$(LOCAL)/www"
  }
  
  // The developer URL is used by the startWorkerService.py user script.
  developerUrl = "MeVis/TutorialSummary/Projects/TutorialSummaryBrowser/Modules/www/TutorialSummaryBrowser.html"
}
```
{{</highlight>}}

Open the script file of the *TutorialSummary* module from [Step 3](tutorials/summary/summary3/). Copy the output section to your web macro and define *internalName* as the output of your `RemoteRendering` modules.

You can also copy all fields from *Parameters* section to your web macro module script.

{{< highlight filename="TutorialSummaryBrowser.script" >}}
```Stan
Interface {
  Inputs {}
  Outputs {
    Field out2D { internalName = RemoteRendering2D.output }
    Field out3D { internalName = RemoteRendering3D.output }
    Field outSegmentationMask { internalName = CloseGap.output0 }
  }
  Parameters {
    Field openFile {
      type         = String
      internalName = LocalImage.name
    }
    Field selectOverlayColor {
      internalName = SoView2DOverlay.baseColor
      type         = Color
    }
    Field selectOverlayTransparency {
      internalName = SoView2DOverlay.alphaFactor
    }
    Field imageAlpha {
      internalName = SoWEMRendererImage.faceAlphaValue
      type         = Integer
      min          = 0
      max          = 1
    }
    Field thresholdInterval {
      internalName = RegionGrowing.autoThresholdIntervalSizeInPercent
      type         = Integer
      min          = 0
      max          = 100
    }
    Field isoValueImage  {
      internalName = IsoSurfaceImage.isoValue
      type         = Integer
      min          = 0
      max          = 1000
    }
    Field selected3DView {
      type   = Enum
      values = Segmented,File,Both
    }
    Field totalVolume {
      internalName = CalculateVolume.totalVolume
      editable     = False
    }
    Field resetApplication {
      type  = Trigger
      title = Reset
    }
    Field markerPosition {
      type         = Vector3
    }
    Field applyMarker {
      type  = Trigger
      title = Add
    }
  }
}
```
{{</highlight>}}

Reloading your web macro in MeVisLab SDK now shows the same outputs as the original macro module. The only difference is the type of your output. It changed from MLImage and Open Inventor scene to MLBase from your `RemoteRendering` modules.

![Macro modules](images/tutorials/summary/Example8_7.png "Macro modules")

The internal network of your web macro should look like this:

![Macro modules](images/tutorials/summary/Example8_8.png "Macro modules")

You can emulate the final viewer by adding a `RemoteRenderingClient` module to the outputs of your web macro.

![RemoteRenderingClient](images/tutorials/summary/Example8_9.png "RemoteRenderingClient")

Open the *.script* files of your macro modules and copy the *FieldListeners* from the *Commands* section of your *TutorialSummary.script* to *TutorialSummaryBrowser.script*.

{{< highlight filename="TutorialSummaryBrowser.script" >}}
```Stan
Commands {
  source = $(LOCAL)/TutorialSummaryBrowser.py
  
  FieldListener selected3DView {
    command = viewSelectionChanged
  }
  FieldListener resetApplication {
    command = resetApplication
  }
  FieldListener markerPosition {
    command = insertPosition
  }
  FieldListener applyMarker {
    command = applyPosition
  }
}
```
{{</highlight>}}

Also copy the *Window* section to your web macro module. The *Box* of the *Viewing* tab needs to be modified because we are now using the `RemoteRendering` outputs instead of the `View3D` and `SoExaminerViewer` outputs.

{{< highlight filename="TutorialSummaryBrowser.script" >}}
```Stan
Window "MainPanel" {
  // Define minimum width and height
  minimumWidth  = 400
  minimumHeight = 300
  initCommand   = resetApplication
  // Vertical Layout and 4 Boxes with Horizontal Layout
  Vertical {
    Box Source {
      layout = Horizontal
      Field openFile {
        browseButton = True
        browseMode   = open
      }
      Field resetApplication { }
    }
    Box Viewing {
      layout = Horizontal
      RemoteRendering out2D {
        expandX = True
        expandY = True
      }
      RemoteRendering out3D {
        expandX = True
        expandY = True
      }
    }
    Box Settings {
      layout = Horizontal
      Field selectOverlayColor {
        title   = Color
      }
      Field selectOverlayTransparency {
        title   = Alpha
      }
      Field imageAlpha {
        step   = 0.1
        slider = True
      }
      Field thresholdInterval {
        step   = 0.1
        slider = True
      }
      Field isoValueImage {
        step   = 2
        slider = True
      }
      Field markerPosition {}
      Field applyMarker {}
      ComboBox selected3DView {
        alignX   = Left
        editable = False
      }
    }
    Box Info {
      layout    = Horizontal
      Field totalVolume {}
    }
  }
}
```
{{</highlight>}}

#### Python Functions
After we reused the scripts, we now need to copy the Python functions from *TutorialSummary.py* to *TutorialSummaryBrowser.py*. Open the Python file of your web macro. You will see an additional import from *MLABRemote*, which is required for remote rendering calls. The *MLABRemote* context is already setup automatically and can be used.

{{< highlight filename="TutorialSummaryBrowser.py" >}}
```Python
from mevis import *

from MLABRemote import MLABRemote, allowedRemoteCall
MLABRemote.setup(ctx)
```
{{</highlight>}}

Copy the Python functions from *TutorialSummary.py* to *TutorialSummaryBrowser.py*. They can remain unchanged but require an additional *@allowedRemoteCall* function. This is necessary to explicitly allow remote execution of the function and is disabled by default for security reasons.

{{< highlight filename="TutorialSummaryBrowser.py" >}}
```Python
from mevis import *

from MLABRemote import MLABRemote, allowedRemoteCall
MLABRemote.setup(ctx)

@allowedRemoteCall
def viewSelectionChanged(field):
  if field.value == "Segmented":
    ctx.field("SoSwitch.whichChild").value = 0
  if field.value == "File":
    ctx.field("SoSwitch.whichChild").value = 1
  if field.value == "Both":
    ctx.field("SoSwitch.whichChild").value = 2

@allowedRemoteCall
def resetApplication():
  ctx.field("RegionGrowing.clear").touch()
  ctx.field("SoView2DMarkerEditor.deleteAll").touch()
  ctx.field("LocalImage.close").touch()
  ctx.field("imageAlpha").value = 0.5
  ctx.field("thresholdInterval").value = 1.0
  ctx.field("isoValueImage").value = 200
  ctx.field("selected3DView").value = "Both"

@allowedRemoteCall
def insertPosition(field):
  ctx.field("SoView2DMarkerEditor.newPosXYZ").value = field.value

@allowedRemoteCall
def applyPosition():
  ctx.field("SoView2DMarkerEditor.useInsertTemplate").value = True
  ctx.field("SoView2DMarkerEditor.add").touch()
```
{{</highlight>}}

### Run Your Application in a Browser
MeVisLab provides a local webserver and you can preview your application in a browser by selecting the module and open {{< menuitem "Scripting" "Web" "Start Module Through Webservice" >}}. The integrated webserver starts and your default browser opens the local website showing your application.

![Webserver preview](images/tutorials/summary/Example8_10.png "Webserver preview")

Select your web macro *TutorialSummaryBrowser* and right-click {{< mousebutton "right" >}} to select {{< menuitem "Related Files" "Show Definition Folder" >}}. You can see the folder structure of your web macro and modify the stylesheet depending on your needs.

### Open the Current Web Instance in MeVisLab SDK
If you want to inspect the internal state of the modules and your internal network, open the console of your browser and enter *MLAB.GUI.Application.module('TutorialSummaryBrowser').showIDE()*. MeVisLab opens and you can change your internal network while all modifications are applied on the website on-the-fly.

![MeVisLab SDK](images/tutorials/summary/Example8_11.png "MeVisLab SDK")

## Summary
* MeVisLab macro modules can easily be adapted to run in a browser window.
* MeVisLab `RemoteRendering` allows to run in a browser or embedded into other application user interfaces. It does so by sending updated images to a client and receiving input events from this client.
* Clients can be emulated by using a `RemoteRenderingClient` module.

{{< networkfile "examples/summary/TutorialSummaryBrowser.zip" >}}
