---
title: "Example 3: Creating a simple application"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 445
tags: ["Advanced", "Tutorial", "Macro", "Macro modules", "Global Macro", "Python", "Scripting"]
menu: 
  main:
    identifier: "viewerexample"
    title: "Adding viewer to your UI and implement a field listener in Python"
    weight: 445
    parent: "basicmechanisms"
---
# Example 3: Creating a Simple Application
## Introduction
In the previous examples, you already learned how to create macro modules, user interfaces, and how to interact with your UI via Python scripting.

In this example, you will learn how to create a simple prototype application in MeVisLab including a user interface with 2D and 3D viewer. You will learn how to implement field listeners and react on events.

## Steps to Do
### Create Your Network
Start with an empty network and add the Module `ImageLoad` to your workspace. Then, add a `View2D` and `View3D` to your workspace and connect the modules as seen below.

![Loading and viewing images](images/tutorials/basicmechanics/SimpleApp_01.png "Loading and viewing images")
### Load an Image
Now double-click {{< mousebutton "left" >}} on the `ImageLoad` module and open any image. You can use the included file *./MeVisLab/Resources/DemoData/MRI_Head.dcm*.

Opening your viewers should now show the images in 2D and 3D.

![Show images in 2D and 3D](images/tutorials/basicmechanics/SimpleApp_02.png "Show images in 2D and 3D")

### Save Your Network
Now, save your network as *.mlab* file and remember the location.

### Create a Macro Module
Open the Project Wizard via {{< menuitem "File" "Run Project Wizard" >}} and run the Wizard for a *macro module*. Name your module *MyViewerApplication*, enter your details, and click *Next >*.

![Module Properties](images/tutorials/basicmechanics/SimpleApp_03.png "Module Properties")

On the next screen, make sure to add a Python file and use the existing network you previously saved. Click *Next >*.

![Macro module Properties](images/tutorials/basicmechanics/SimpleApp_04.png "Macro module Properties")

You can leave all fields empty for now and just click *Create*.

![Module Field Interface](images/tutorials/basicmechanics/SimpleApp_05.png "Module Field Interface")

MeVisLab reloads its internal database and you can open a new tab. Search for your newly created module, in our case it was *MyViewerApplication*.

![MyViewerApplication](images/tutorials/basicmechanics/SimpleApp_06.png "MyViewerApplication")

In the case you double-click {{< mousebutton "left" >}} your module now, you will see the *Automatic Panel* only showing the name of your module, because we did not add any own *Window* until now.

### Develop Your User Interface
Before adding your own UI, open the internal network of your macro module via right-click {{< mousebutton "right" >}} and {{< menuitem "Related Files" "MyViewerApplication.mlab" >}}. Open the panel of your `ImageLoad` module and set *filename* to an empty string (clear). This is necessary for later.

Now, right-click on your *MyViewerApplication* and select {{< menuitem "Related Files" "MyViewerApplication.script" >}}

{{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MATE">}} opens showing your script file. You already learned how to create simple UI elements in [Example 2.4](tutorials/basicmechanisms/macromodules/guidesign). Now, we will create a little more complex UI including your `View2D` and `View3D`.

First we need a new *Field* in your *Parameters* section. Name the field *filepath* and set *internalName* to *ImageLoad.filename*. 

{{< highlight filename="MyViewerApplication.script" >}}
``` Stan
Interface {
  Inputs {}
  Outputs {}
  Parameters {
    Field filepath {
      internalName = ImageLoad.filename
    }
  }
}
``` 
{{</highlight>}}

We now re-use the *filepath* field from the `ImageLoad` module for our interface. Add a *Window* and a *Vertical* to the bottom of your *.script* file. Add the just created parameter field *filepath* inside your *Vertical* as seen below.

{{< highlight filename="MyViewerApplication.script" >}}
``` Stan
Interface {
  Inputs {}
  Outputs {}
  Parameters {
    Field filepath {
      internalName = ImageLoad.filename
    }
  }
}

Commands {
  source = $(LOCAL)/MyViewerApplication.py
}

Window {
  Vertical {
    Field filepath {}
  }
}
``` 
{{</highlight>}}

If you now double-click {{< mousebutton "left" >}} on your module, you can see your just created filepath field.

![Filepath field in UI](images/tutorials/basicmechanics/SimpleApp_08.png "Filepath field in UI")

Next, we will add your 2D and 3D viewers and a *Button* to your *Window*. Change your *.script* file as seen below:

{{< highlight filename="MyViewerApplication.script" >}}
``` Stan
Window {
  Vertical {
    Horizontal {
      Field filepath {}
      Button {
        title = "Reset"
        
      }
    }
    Horizontal {
      Viewer View2D.self {
        type    = SoRenderArea
        pw      = 400 ph = 400
        expandX = yes
        expandY = yes
      }
      Viewer View3D.self {
        pw      = 400 ph = 400
        expandX = yes
        expandY = yes
      }
    }
  }
}
```
{{</highlight>}}

We have a vertical layout having two items placed horizontally next to each other. The new *Button* gets the title *Reset* but does nothing yet, because we did not add a Python function to a command.

Additionally, we added the `View2D` and the `View3D` to our *Window* and defined the *height*, *width* and the *expandX/Y* property to *yes*. This leads our viewers to resize together with our *Window*.

{{<alert class="info" caption="Extra Infos">}}
Additional information about the `View2D` and `View3D` options can be found in the MeVisLab {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Viewer" "MDL Reference">}}
{{</alert>}}

You can now play around with your module in MeVisLab SDK. Open the *Window* and select a file. You can see the two viewers showing the 2D and 3D images. You can interact with your viewers the same way as in your MeVisLab network. All functionalities are taken from the modules and transferred to your user interface.

![2D and 3D viewers in our application](images/tutorials/basicmechanics/SimpleApp_09.png "2D and 3D viewers in our application")

### Develop a Python Function for Your Button
Next we want to reset the filepath to an empty string on clicking our *Reset* button. Add the *reset* command to your Button.
{{< highlight filename="MyViewerApplication.script" >}}
``` Stan
...
Button {
  title = "Reset"
  command = reset
}
...
```
{{</highlight>}}

Right-click {{< mousebutton "left" >}} on *reset* and select {{< menuitem "Create Python function 'reset'" >}}. MATE opens the Python file of your module and automatically adds the function definition. Set the filename of the `ImageLoad` module to an empty string.

{{< highlight filename="MyViewerApplication.py" >}}
``` Python
from mevis import *

def reset():
  ctx.field("filepath").value = ""
```
{{</highlight>}}

Clicking on *Reset* in your module now clears the filename field and the viewers do not show any images anymore.

#### Field Listeners {#fieldlisteners}

A field listener watches a given field in your network and reacts on any changes of the field value. You can define Python functions to execute in the case a change has been detected.

In order to define such a listener, you need to add it to the *Commands* section in your *.script* file.

**Example:**
{{< highlight filename="MyViewerApplication.script" >}}
```Stan
Commands {
    source = $(LOCAL)/MyViewerApplication.py

    FieldListener View2D.startSlice {
        command = printCurrentSliceNumber
    }
}
```
{{</highlight>}}

In the above example, we react on changes of the field *startSlice* of the module `View2D`. Whenever the field value (currently displayed slice) changes, the Python function *printCurrentSliceNumber* is executed.

In your Python file `MyViewerApplication.py`, you can now add the following:

{{< highlight filename="MyViewerApplication.py" >}}
```Python
def printCurrentSliceNumber(field):
    MLAB.log(field.value)
```
{{</highlight>}}

Scrolling through slices in the `View2D` module now logs a message containing the slice number currently visible to the MeVisLab Debug Output.

## Summary
* You can add any Viewers to your application UI by reusing them in MDL.
* Parameter Fields using the internalName of an existing field in your network allows re-using this UI element in your own UI. Changes in your UI are applied to the field in the module.
* Field Listeners allow reacting on changes of a field value in Python.

{{< networkfile "examples/basic_mechanisms/viewer_application/viewerexample.mlab" >}}
