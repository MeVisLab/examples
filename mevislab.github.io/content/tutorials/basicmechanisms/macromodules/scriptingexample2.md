---
title: "Example 2.5.2: Module interactions via Python scripting"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
tags: ["Advanced", "Tutorial", "Macro", "Macro Modules", "Global Macro", "Python", "Scripting"]
menu: 
  main:
    identifier: "scriptingexample2"
    title: "Module interactions via Python scripting"
    weight: 440
    parent: "macro_modules"
---
# Example 2.5.2: Module interactions via Python scripting
## Introduction

In this example, you will learn how to add Python scripting to your User Interface. The network used in [Chapter V](tutorials/dataobjects/contours/contourexample5/) will be used for creating the Macro Module.

## Steps to do
### Creating the macro module
First, we condense the example network into a macro module and then we create a panel for that module. To create a macro module use the
Project Wizard, which you find under {{< menuitem "File" "Run Project Wizard" >}}. Select
*Macro Module* and press *Run*.

Now, you have to edit:
1.  Name: The name of your module
2.  Package: Select the package you like to save the macro module in. 
3.  Directory Structure: Change to *Self-contained*
4.  Project: Select you project name

Press *Next* and edit the following:

1.  Copy existing network: Select the example network
2.  Check the box: Add Python file

Now, create your macro module and reload MeVisLab. You can find your module via search in MeVisLab.

![Creating macro module](/images/tutorials/basicmechanics/CreatingMacroModule.png "Creating macro module")

![Enable Python scripting](/images/tutorials/basicmechanics/EnablePythonScripting.png "Enable Python scripting")

To design a panel and create a user interface for the macro module, open the *.script* file. You can see, that a Command environment exist, which defines the python file as source for all commands.

![Open the script file](/images/tutorials/basicmechanics/OpenScriptFile.png "Open the script file")

![Script file](/images/tutorials/basicmechanics/ScriptFile.png "Script file")

### Creating a panel with tabs and viewers

At first, we create a {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Window" "Window" >}} with two {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html##mdl_TabView" "Tabs" >}}. One *Main* tab, in which both viewers of the network are represented and one tab for *Settings*. For generating tabs, we can use the control {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_TabView" "TabView" >}}, with its items {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_TabViewItem" "TabViewItem" >}}. The control *TabView* enables to add a command, which is executed when opening the tab. For adding the viewers to the panel, we use the Control *Viewer*.

[//]: <> (MVL-653)

{{< highlight filename="IsoCSOs.script" >}}
```Stan
Window {
    TabView {
        TabViewItem Main {
            Horizontal {
                Viewer View2D.self {
                    type = SoRenderArea
                    pw = 400
                    ph = 400
                }
                Viewer SoExaminerViewer.self {
                    type = SoExaminerViewer
                    pw = 400
                    ph = 400
                }
            }
        }
        
        TabViewItem Settings {
        }
    }
}
```
{{</highlight>}}

![Panel with Tabs and Viewers](/images/tutorials/basicmechanics/PanelWithTabsAndViewers.png "Panel with Tabs and Viewers")

### Edit viewer settings in the panel

You may want to change the design setting of the right viewer. This is
still possible via the internal network of the macro module. Open the
internal network either via the context menu or using the middle mouse
button {{< mousebutton "middle" >}} and click on the module. After that, open the Automatic Panel of
the module `SoExaminerViewer` via context menu {{< menuitem "Show Windows" "Automatic Panel" >}} and change the field *decoration* to *False*. Keep in mind, as we did not create CSOs by now, the right viewer stays black.

![Change viewer settings](/images/tutorials/basicmechanics/ChangeViewerSettings.png "Change viewer settings")

![Changed viewer settings](/images/tutorials/basicmechanics/ChangedViewerSettings.png "Changed viewer settings")

### Selection of images

Next, we like to add the option to browse through the folders and select
the image, we like to create CSOs from. This functionality is already given in the internal network in the module `LocalImage`. We can copy this functionality from `LocalImage` and add this option to the panel above both viewers. But, how should we know, which field name we
reference to? To find this out, open the
internal network of your macro module. Now you are able to open the panel of
the module `LocalImage`. Right-click {{< mousebutton "right" >}} the desired field: In this case, right-click the label
*Name:*. Select *Copy Name*, to copy the internal name of this field.

![Copy the field name](/images/tutorials/basicmechanics/GUI_Exp_09.png "Copy the field name")

Now, you can add this field as a new field to your window by pasting the
name. All field settings are taken over from the internal field from the module `LocalImage`.

{{< highlight filename="IsoCSOs.script" >}}
```Stan
Window {
    TabView {
        TabViewItem Main {
            Vertical {
                Field LocalImage.name {}
                Horizontal {
                    Viewer View2D.self {
                        type = SoRenderArea
                        pw = 400
                        ph = 400
                    }
                    Viewer SoExaminerViewer.self {
                        type = SoExaminerViewer
                        pw = 400
                        ph = 400
                    }
                }
            }
        }
        
        TabViewItem Settings {
        }
    }
}
```
{{</highlight>}}

![Add name field](/images/tutorials/basicmechanics/AddNameField.png "Add name field")

### Add buttons to your panel

As a next step, we like to add a *Browse\...*-Button, like in the module
`LocalImage`, and also a button to create the CSOs.

To create the *Browse\...*-Button:

1.  Create a button containing the command *fileDialog*.
2.  Right-click {{< mousebutton "right" >}} the command to create the respective function in the.
    Python file.
3.  Edit the function in the Python file, to enable the file dialog (similar function as in *LocalImage.py*).

To create the Iso Generator Button:

We like to copy the field of the Update-Button from the internal module
`IsoCSOGenerator`, but not its layout so:

1.  Create a new Field in the interface, called *IsoGenerator*, which contains the internal field *Update* from the module `IsoCSOGenerator`.
2.  Create a new Button in your Window which uses the field *IsoGenerator*.

After these steps, you can use the Iso Generator button to create CSOs.

{{< highlight filename="IsoCSOs.script" >}}
```Stan
Interface {
    Inputs {}
    Outputs {}
    Parameters {
        Field IsoGenerator {
            internalName = CSOIsoGenerator.apply
        }
    }
}

Commands {
    source = $(LOCAL)/IsoCSOs.py
}

Window {
    TabView {
        TabViewItem Main {
            Vertical {
                Horizontal {
                    Field LocalImage.name {}
                    Button {
                        title = "Browse..."
                        command = fileDialog
                    }
                    Button IsoGenerator {
                        title = "Iso Generator"
                    }
                }
                Horizontal {
                    Viewer View2D.self {
                        type = SoRenderArea
                        pw = 400
                        ph = 400
                    }
                    Viewer SoExaminerViewer.self {
                        type = SoExaminerViewer
                        pw = 400
                        ph = 400
                    }
                }
            }
        }
        
        TabViewItem Settings {
        }
    }
}
```
{{</highlight>}}

{{< highlight filename="IsoCSOs.py" >}}
```Python
from mevis import *

def fileDialog():
    exp = ctx.expandFilename(ctx.field("LocalImage.name").stringValue())
    filename = MLABFileDialog.getOpenFileName(exp, "", "Open file")
    if filename:
        ctx.field("LocalImage.name").value = ctx.unexpandFilename(filename)
```
{{</highlight>}}

![Automatically generate CSOs based on Iso value](/images/tutorials/basicmechanics/GUI_Exp_14.png "Automatically generate CSOs based on Iso value")

### Colorizing CSOs

We like to colorize the CSO we hover over with our
mouse in the 2D viewer. Additionally, when clicking a CSO with the left mouse key {{< mousebutton "left" >}}, this CSO shall be
colorized in the 3D viewer. This functionality can be implemented via Python
scripting (even though MeVisLab has a build-in function to do that). We
can do this in the following way:

1. Enable the View *Scripting Assistant*, which translates actions into Python code. 
    
    ![Scripting Assistant](/images/tutorials/basicmechanics/GUI_Exp_15.png "Scripting Assistant")

2. Enable a functionality which allows us to notice the id of the CSO we are currently hovering over with our mouse. For this open the internal network of our macro module. We will use the module `SoView2DCSOExtensibleEditor`. Open its panel and select the tab *Advanced*. You can check a box to enable *Update CSO id under mouse*. If you now hover over a CSO, you can see its id in the panel. We can save the internal network to save this functionality, but we can also solve our problem via scripting. The Scripting Assistant translated our action into code, which we can use.
    
    ![Enabling CSO id identification](/images/tutorials/basicmechanics/GUI_Exp_16.png "Enabling CSO id identification")

    We like to activate this functionality when opening the panel of our macro module `IsoCSOs`. Thus, we add a starting command to the control Window. We can call this command for example *enableFunctionalities*.

    In the *.script* file:

{{< highlight filename="IsoCSOs.script" >}}
```Stan
Window {
    windowActivatedCommand = enableFunctionalities
    TabView {
        TabViewItem Main {
            ...
        }
    }
}
```
{{</highlight>}}

In the Python file, we define the function *enableFunctionalities*. We see our action as Python code in the *Scripting Assistant*. Just copy the code into our Python function.

{{< highlight filename="IsoCSOs.py" >}}
```Python
def enableFunctionalities():
    ctx.field("SoView2DCSOExtensibleEditor.updateCSOIdUnderMouseCursor").value = True
```
{{</highlight>}}

3.  Implement a field listener. This field listener will detect when you hover over a CSO and the CSO id changes. Triggered by a CSO id change, a colorization function will be executed and colorize the selected CSO.

In the *.script* file:

{{< highlight filename="IsoCSOs.script" >}}
```Stan
Commands {
    source = $(LOCAL)/IsoCSOs.py
    FieldListener SoView2DCSOExtensibleEditor.csoIdUnderMouseCursor {
        command = colorizeCSO
    }
}
```
{{</highlight>}}

In the Python file:

{{< highlight filename="IsoCSOs.py" >}}
```Python
# global variables
listCSOs = []
idxCSO = -1

def colorizeCSO():
    if ctx.field("CSOManager.numCSOs") == 0:
        pass
    else:
        global listCSOs
        global idxCSO
        if listCSOs == []:
            listCSOs = ctx.field("CSOManager.outCSOList").object()
        
        # COLORIZATION OF CSO
        # Changing back color of previously selected CSO to default value
        if idxCSO >= 0:
            oldCSO = listCSOs.getCSOAt(idxCSO)
            oldCSO.setPathPointColor((1.0, 1.0, 0.0)) # Color change of CSO
            oldCSO.setPathPointWidth(1)               # Line width change
        
        # Changing color and width of selected CSO
        idxCSO = ctx.field("SoView2DCSOExtensibleEditor.csoIdUnderMouseCursor").value - 1 # -1 because CSOs are indexed starting at 1
        if idxCSO >= 0:
            currentCSO = listCSOs.getCSOAt(idxCSO)
            currentCSO.setPathPointColor((1.0, 0.0, 1.0))
            currentCSO.setPathPointWidth(5)
```
{{</highlight>}}

Reload your module ({{< keyboard "F5" >}}) and open the panel. After generating CSOs, the CSO under your mouse is marked. Clicking this CSO {{< mousebutton "left" >}} enables the marking in the 3D viewer. If you like, you can add some settings to your *Settings*
page. For example

{{< highlight filename="IsoCSOs.script" >}}
```Stan
TabViewItem Settings {
    Field CSOIsoGenerator.isoValue {}
    Field SoCSOVisualizationSettings.ghostingDepthInVoxel {}
}
```
{{</highlight>}}

![Colored selection](/images/tutorials/basicmechanics/GUI_Exp_22.png "Colored selection")

## Summary
* The control *Tabview* creates tabs in panels.
* The control *Viewer* allows to add viewers to your panel.
* The control *Button* creates a button executing a Python function when pressed.
* The tag *WindowActivationCommand* of the control Window triggers Python functions executed when opening the panel.
* Field listeners can be used to activate Python functions triggered by a change of defined parameter fields.
* Use the view *Scripting Assistant* can be used to translate actions into Python code.

{{< networkfile "examples/basic_mechanisms/macro_modules_and_module_interaction/example2/" >}}
