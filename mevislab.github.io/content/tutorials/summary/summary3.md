---
title: "Step 3: Prototyping - User Interface and Python Scripting"
date: "2023-01-17"
status: "open"
draft: false
weight: 815
tags: ["Advanced", "Tutorial", "Prototyping", "User Interface", "Python", "GUI Editor"]
menu: 
  main:
    identifier: "summaryexample3"
    title: "Develop Your User Interface and Add Python Functions"
    weight: 815
    parent: "summary"
---

# Step 3: Prototyping - User Interface and Python Scripting

{{< youtube "dOyncLUpclU" >}}

## Introduction
In this step, we will develop a user interface and add Python scripting to the macro module you created in [Step 2](tutorials/summary/summary2).

## Steps to Do

### Develop the User Interface
A mockup of the user interface you are going to develop is available [here](tutorials/summary#UIDesign). The interface provides the possibility to load files and shows a 2D and a 3D viewer. In addition to that, some settings and information for our final application are available.

Search for your macro module and add it to your workspace. Right-click {{< mousebutton "right">}} and select {{< menuitem "Related Files" "<MACRO_MODULE_NAME>.script" >}}.

The MeVisLab text editor MATE opens showing the *.script* file of your module.

#### Layout
You can see that the interface is divided into four parts in vertical direction:
* Source or file/directory selection
* Viewing (2D and 3D)
* Settings
* Info

Inside the vertical parts, the elements are placed next to each other horizontally.

Add a *Window* section to your *.script* file. Inside the *Window*, we need a *Vertical* for the four parts and a *Box* for each part. Name the boxes "Source", "Viewing", "Settings", and "Info". The layout inside each *Box* shall be *Horizontal*.

In addition to that, we define the minimal size of the Window as 400 x 300 pixels.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Window {
    // Define minimum width and height
    minimumWidth  = 400
    minimumHeight = 300

    Category {
        // Vertical Layout and 4 Boxes with Horizontal Layout
        Vertical {
            Box Source {
                layout = Horizontal
            }
            Box Viewing {
                layout = Horizontal
            }
            Box Settings {
                layout = Horizontal
            }
            Box Info {
                layout = Horizontal
            }
        }
    }
}
```
{{</highlight>}}

You can preview your initial layout in MeVisLab by double-clicking your module {{< mousebutton "left" >}}.

![Initial Window Layout](images/tutorials/summary/Example3_1.png "Initial Window Layout")

You can see the four vertical aligned parts as defined in the *.script* file. Now, we are going to add the content of the boxes.

{{<alert class="info" caption="Additional Info">}}
An overview over the existing layout elements in MeVisLab Definition Language (MDL) can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#N11695" "here" >}}
{{</alert>}}

#### Adding the UI Elements

##### Source
The *Source Box* shall provide the possibility to select a file for loading into the viewers. You have many options to achieve that in MeVisLab and Python. The easiest way is to reuse the existing field of the `LocalImage` module in your internal network.

Add a field to the *Parameters* section of your *.script* file. Name the field *openFile* and set type to *String* and internalName to *LocalImage.name*.

Then, add another field to your *Box* for the *Source* and use the field name from *Parameters* section, in this case *openFile*. Set *browseButton = Yes* and *browseMode = open* and save your script.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
    Inputs {}
    Outputs {}
    Parameters {
      Field openFile {
          type         = String
          internalName = LocalImage.name
      }
    }
}

...

Window {
    // Define minimum width and height
    minimumWidth  = 400
    minimumHeight = 300
    
    Category {
        // Vertical Layout and 4 Boxes with Horizontal Layout
        Vertical {
            Box Source {
                layout = Horizontal
                Field openFile {
                    browseButton = Yes
                    browseMode   = open
                }
            }
            Box Viewing {
                layout = Horizontal
            }
            Box Settings {
                layout = Horizontal
            }
            Box Info {
                layout = Horizontal
            }
        }
    }
}
```
{{</highlight>}}

Again, you can preview your user interface in MeVisLab directly. You can already select a file to open. The image is available at the output of the `LocalImage` module in your internal network but the viewers are missing in our interface.

![Source Box](images/tutorials/summary/Example3_2.png "Source Box")

##### Viewing
Add the two viewer modules to the *Viewing* section of your *.script* file and define their field as *View2D.self* and *SoExaminerViewer.self*. Set *expandX = Yes* and *expandY = Yes* for both viewing modules. We want them to resize in the case the size of the Window changes.

Set the 2D viewer's type to *SoRenderArea* and the 3D viewer's type to *SoExaminerViewer* and inspect your new user interface in MeVisLab.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
...

    Box Viewing {
        layout = Horizontal
        Viewer View2D.self {
            expandX = Yes
            expandY = Yes
            type    = SoRenderArea
        }
        Viewer SoExaminerViewer.self {
            expandX = Yes
            expandY = Yes
            type    = SoExaminerViewer
        }
    }

...
```
{{</highlight>}}

![2D and 3D Viewer](images/tutorials/summary/Example3_3.png "2D and 3D Viewer")

The images selected in the *Source* section are shown in 2D and 3D. We simply reused the existing fields and viewers from your internal network and are already able to interact with the images. As the `View2D` of your internal network itself provides the possibility to accept markers and starts the `RegionGrowing`, this is also already possible and the segmentations are shown in 2D and 3D.

##### Settings
Let's define the *Settings* section. Once again, we first define the necessary fields. For automated tests that we are going to develop later, it makes sense to make some of the fields of the internal network available from outside.

The following shall be accessible as *Field* for our macro module:
* Filename to be opened
* Color of the 2D overlay and 3D segmentation
* Transparency of the 3D image
* Threshold to be used for `RegionGrowing`
* Isovalue of the 3D surface to use for rendering
* Position of the marker to use for `RegionGrowing`
* Selection for 3D visualization (image, segmentation, or both)
* Trigger to reset the application to its initial state

We already defined the filename as a field. Next we want to change the color of the overlay. Add another field to your *Parameters* section as *selectOverlayColor*. Define *internalName = SoView2DOverlay.baseColor* and *type = Color*. You may also define a title for the field, for example, *Color*.

The *baseColor* field of the `SoView2DOverlay` already has a parameter connection to the color of the `SoWEMRendererSegmentation`. This has been done in the internal network. The defined color is used for 2D and 3D automatically.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
    Inputs {}
    Outputs {}
    Parameters {
        ...
        Field selectOverlayColor {
            internalName = SoView2DOverlay.baseColor
            type         = Color
        }
    }
}

...

    Box Settings {
        layout = Horizontal
        Field selectOverlayColor {
            title   = Color
        }
    }

...

```
{{</highlight>}}

The next elements follow the same rules; therefore, the final script will be available at the end for completeness.

In order to set the transparency of the 3D image, we need another field reusing the *SoWEMRendererImage.faceAlphaValue*. Add a field *imageAlpha* to the *Parameters* section. Define *internalName = SoWEMRendererImage.faceAlphaValue*, *type = Integer*, *min = 0*, and *max = 1*.

Add the field to the *Settings Box* and set *step = 0.1* and *slider = Yes*.

For the `RegionGrowing` threshold, add the field *thresholdInterval* to *Parameters* section and set *type = Integer*,  *min = 1*,  *max = 100*, and *internalName = RegionGrowing.autoThresholdIntervalSizeInPercent*.

Add the field to the *Settings* UI, and define *step = 0.1* and *slider = Yes*.

Define a field *isoValueImage* in the *Parameters* section and set *internalName = IsoSurfaceImage.isoValue*,  *type = Integer*,  *min = 1*, and  *max = 1000*.

In the *Settings* section of the UI, set *step = 2* and *slider = Yes*.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
    Inputs {}
    Outputs {}
    Parameters {
        Field openFile {
            type         = String
            internalName = LocalImage.name
        }
        Field selectOverlayColor {
            internalName = SoView2DOverlay.baseColor
            type         = Color
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
    }
}

Commands {
    source = $(LOCAL)/TutorialSummary.py
}

Window {
    // Define minimum width and height
    minimumWidth  = 400
    minimumHeight = 300

    Category {
        // Vertical Layout and 4 Boxes with Horizontal Layout
        Vertical {
            Box Source {
                layout = Horizontal
                Field openFile {
                    browseButton = Yes
                    browseMode   = open
                }
            }
            Box Viewing {
                layout = Horizontal
                Viewer View2D.self {
                    expandX = Yes
                    expandY = Yes
                    type    = SoRenderArea
                }
                Viewer SoExaminerViewer.self {
                    expandX = Yes
                    expandY = Yes
                    type    = SoExaminerViewer
                }
            }
            Box Settings {
                layout = Horizontal
                Field selectOverlayColor {
                    title   = Color
                }
                Field imageAlpha {
                    step    = 0.1
                    slider  = Yes
                }
                Field thresholdInterval {
                    step    = 0.1
                    slider  = Yes
                }
                Field isoValueImage {
                    step    = 2
                    slider  = Yes
                }
            }
            Box Info {
                layout = Horizontal
            }
        }
    }
}

```
{{</highlight>}}

Your user interface of the macro module should now look similar to this:

![User Interface without Python Scripting](images/tutorials/summary/Example3_4.png "User Interface without Python Scripting")

For the next elements, we require Python scripting. Nevertheless, you are already able to use your application and perform the basic functionalities without writing any line of code.

### Python Scripting
Python scripting is always necessary in the case you do not want to reuse an existing field for your user interface but implement functions to define what happens in the case of any event.

Events can be raised by the user (e.g., by clicking a button) or by the application itself (e.g., when the window is opened).

#### 3D Visualization Selection
You will now add a selection possibility for the 3D viewer. This allows you to define the visibility of the 3D objects File, Segmented, or Both.

Add another field to your *Parameters* section. Define the field as *selected3DView* and set *type = Enum* and *values =Segmented,File,Both*.

Add a *ComboBox* to your *Settings* and use the field name defined above. Set *alignX = Left* and *editable = False* and open the *Window* of the macro module in MeVisLab.

The values of the field can be selected, but nothing happens in our viewers. We need to implement a *FieldListener* in Python that reacts on any value changes of the field *selected3DView*.

Open your script file and go to the *Commands* section. Add a *FieldListener* and reuse the name of our internal field *selected3DView*. Add a *Command* to the *FieldListener* calling a Python function *viewSelectionChanged*.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Commands {
    source = $(LOCAL)/TutorialSummary.py
    
    FieldListener selected3DView {
        command = viewSelectionChanged
    }
}
```
{{</highlight>}}

Right-click {{< mousebutton "right" >}} the command select {{< menuitem "Create Python Function 'viewSelectionChanged'" >}}. MATE automatically opens the Python file of your macro module and creates a function *viewSelectionChanged*.

{{< highlight filename="<MACRO_NAME>.py" >}}
```Python
from mevis import *

def viewSelectionChanged(field):
    if field.value == "Segmented":
        ctx.field("SoSwitch.whichChild").value = 0
    if field.value == "File":
        ctx.field("SoSwitch.whichChild").value = 1
    if field.value == "Both":
        ctx.field("SoSwitch.whichChild").value = 2
```
{{</highlight>}}

The function sets the `SoSwitch` to the child value depending on the selected field value from the *ComboBox* and you should now be able to switch the 3D rendering by selecting an entry in the user interface.

#### Setting the Marker
The marker for the `RegionGrowing` is defined by the clicked position as Vector3. Add another field *markerPosition* to the *Parameters* section and define *type = Vector3*.

Then, add a trigger field *applyMarker* to your *Parameters* section. Set *type  = Trigger* and *title = Add*.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
...
    Field markerPosition {
        type         = Vector3
    }
    Field applyMarker {
        type         = Trigger
        title        = Add
    }
...
```
{{</highlight>}}

Add another *FieldListener* to both fields:
{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
...
    FieldListener markerPosition {
        command = insertPosition
    }
    FieldListener applyMarker {
        command = applyPosition
    }
...
```
{{</highlight>}}

Finally, add both fields to the *Settings* section of your user interface:
{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
...
    Field markerPosition {}
    Field applyMarker {}
...
```
{{</highlight>}}

The Python functions should look like this:
{{< highlight filename="<MACRO_NAME>.py" >}}
```Python
...
def insertPosition(field):
    ctx.field("SoView2DMarkerEditor.newPosXYZ").value = field.value

def applyPosition():
    ctx.field("SoView2DMarkerEditor.useInsertTemplate").value = True
    ctx.field("SoView2DMarkerEditor.add").touch()
...
```
{{</highlight>}}

Whenever the field *markerPosition* changes its value, the value is automatically applied to the *SoView2DMarkerEditor.newPosXYZ*. Clicking *SoView2DMarkerEditor.add* adds the new position to the `SoView2DMarkerEditor` and the region growing starts.

{{<alert class="info" caption="Info">}}
The *Field* *SoView2DMarkerEditor.useInsertTemplate* needs to be set to *True* in order to allow adding markers via Python.
{{</alert>}}

#### Reset
Add a new field *resetApplication* to the *Parameters* section and set *type = Trigger* and *title = Reset*.

Add another *FieldListener* to your *Commands* and define *command = resetApplication*.

Add the field to your *Source* region.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
...
  Parameters {
      Field resetApplication {
          type         = Trigger
          title        = Reset
      }
  }
...
Commands {
    ...
    FieldListener resetApplication {
        command = resetApplication
    }
}
...
    Box Source {
        layout = Horizontal
        Field openFile {
            browseButton = Yes
            browseMode   = open
        }
        Field resetApplication { }
    }
...
```
{{</highlight>}}

What shall happen when we reset the application?
* The loaded image shall be unloaded, the viewer shall be empty
* The marker shall be reset if available

Add the Python function *resetApplication* and implement the following:
{{< highlight filename="<MACRO_NAME>.py" >}}
```Python
from mevis import *

def resetApplication():
    ctx.field("RegionGrowing.clear").touch()
    ctx.field("SoView2DMarkerEditor.deleteAll").touch()
    ctx.field("LocalImage.close").touch()
```
{{</highlight>}}

You can also reset the application to initial state by adding a *initCommand* to your *Window*. Call the *resetApplication* function here, too, and whenever the window is opened, the application is reset to its initial state.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Window {
    // Define minimum width and height
    minimumWidth  = 400
    minimumHeight = 300
    initCommand   = resetApplication
  ...
}
```
{{</highlight>}}

This can also be used for setting/resetting to default values of the application. For example, update your Python function *resetApplication* the following way:

{{< highlight filename="<MACRO_NAME>.py" >}}
```Python
from mevis import *

def resetApplication():
    ctx.field("RegionGrowing.clear").touch()
    ctx.field("SoView2DMarkerEditor.deleteAll").touch()
    ctx.field("LocalImage.close").touch()
    ctx.field("imageAlpha").value = 0.5
    ctx.field("thresholdInterval").value = 1.0
    ctx.field("isoValueImage").value = 200
    ctx.field("selected3DView").value = "Both"
```
{{</highlight>}}

### Information
In the end, we want to provide some information about the volume of the segmented area (in ml).

Add one more field to your *Parameters* section and reuse the internal network fields *CalculateVolume.totalVolume*. Set field to *editable = False*

Add the field to the *Info* section of your window.

Opening the window of your macro module in MeVisLab now provides all functionalities we wanted to achieve. You can also play around in the window and define some additional boxes or other MDL controls but the basic application prototype is now finished.

![Final Macro module](images/tutorials/summary/Example3_5.png "Final Macro module")

### MeVisLab GUI Editor
MATE provides a powerful GUI editor showing a preview of your current user interface and allowing to reorder elements in the UI via drag and drop. In MATE, open {{< menuitem "Extras" "Enable GUI Editor" >}}.

![MeVisLab GUI Editor](images/tutorials/summary/Example3_4b.png "MeVisLab GUI Editor")

Changing the layout via drag and drop automatically adapts your *.script* file. Save and reload the script and your changes are applied.

{{<alert class="info" caption="Info">}}
If the GUI editor is not shown in MATE, make sure to check *[View &rarr; Preview]*.
{{</alert>}}

## Final Script and Python Files
{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
    Inputs {}
    Outputs {}
    Parameters {
        Field openFile {
            type         = String
            internalName = LocalImage.name
        }
        Field selectOverlayColor {
            internalName = SoView2DOverlay.baseColor
            type         = Color
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
            items {
                item Segmented {}
                item File {}
                item Both {}
            }
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

Commands {
    source = $(LOCAL)/<MACRO_NAME>.py
    
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

Window {
    // Define minimum width and height
    minimumWidth  = 400
    minimumHeight = 300
    initCommand   = resetApplication

    Category {
        // Vertical Layout and 4 Boxes with Horizontal Layout
        Vertical {
            Box Source {
              layout = Horizontal
              Field openFile {
                  browseButton = Yes
                  browseMode   = open
              }
              Field resetApplication { }
            }
            Box Viewing {
              layout = Horizontal
              Viewer View2D.self {
                  expandX = Yes
                  expandY = Yes
                  type    = SoRenderArea
              }
              Viewer SoExaminerViewer.self {
                  expandX = Yes
                  expandY = Yes
                  type    = SoExaminerViewer
              }
            }
            Box Settings {
              layout = Horizontal
              Field selectOverlayColor {
                  title   = Color
              }
              Field imageAlpha {
                  step   = 0.1
                  slider = Yes
              }
              Field thresholdInterval {
                  step   = 0.1
                  slider = Yes
              }
              Field isoValueImage {
                  step   = 2
                  slider = Yes
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
}
```
{{</highlight>}}

{{< highlight filename="<MACRO_NAME>.py" >}}
```Python
from mevis import *

def viewSelectionChanged(field):
    if field.value == "Segmented":
        ctx.field("SoSwitch.whichChild").value = 0
    if field.value == "File":
        ctx.field("SoSwitch.whichChild").value = 1
    if field.value == "Both":
        ctx.field("SoSwitch.whichChild").value = 2

def resetApplication():
    ctx.field("RegionGrowing.clear").touch()
    ctx.field("SoView2DMarkerEditor.deleteAll").touch()
    ctx.field("LocalImage.close").touch()
    ctx.field("imageAlpha").value = 0.5
    ctx.field("thresholdInterval").value = 1.0
    ctx.field("isoValueImage").value = 200
    ctx.field("selected3DView").value = "Both"

def insertPosition(field):
    ctx.field("SoView2DMarkerEditor.newPosXYZ").value = field.value

def applyPosition():
    ctx.field("SoView2DMarkerEditor.useInsertTemplate").value = True
    ctx.field("SoView2DMarkerEditor.add").touch()
```
{{</highlight>}}

## Summary
* You now added a user interface to your macro module.
* The window opens automatically on double-click {{< mousebutton "right" >}}.
* Fields defined in the *Parameters* section can be modified in the MeVisLab Module Inspector.
* Python allows to implement functions executed on events raised by the user or by the application itself.

{{< networkfile "examples/summary/TutorialSummary_UI.zip" >}}
