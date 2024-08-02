---
title: "Contour Example 7: Using the CSOListContainer"
date: "2024-08-01"
status: "OK"
draft: false
weight: 691
tags: ["Advanced", "Tutorial", "Data Objects", "2D", "Contours", "CSO", "Notifications", "CSOListContainer"]
menu: 
  main:
    identifier: "contourexample7"
    title: "Using the CSOListContainer"
    weight: 691
    parent: "contours"
---
# Contour Example 7: Using the CSOListContainer {#TutorialContoursExample7}

## Introduction

In this example, we are using the module `CSOListContainer` instead of the `CSOManager`. The `CSOManager` is a heavy weight, UI driven module. You can use it to see all of your CSOs, CSOLists and CSOGroups in the module panel. The `CSOListContainer` is a light weight module with focus on Python scripting. We recommend to use this module for final application development, because Python provides much more flexibility in handling CSO objects.

![CSOManager](/images/tutorials/dataobjects/contours/Example_7_1.png "CSOManager")

![CSOListContainer](/images/tutorials/dataobjects/contours/Example_7_2.png "CSOListContainer")

We will create multiple CSOs by using the `SoCSOEllipseEditor` and dynamically add these CSOs to different groups via Python scripting depending on their size. CSOs larger than a configurable threshold will be red, small CSOs will be drawn green. The colors will also be adapted if we manually resize the contours.

## Steps to do
### Develop your network

Add a `LocalImage` and a `View2D` module to your workspace and connect them as shown below. Load the file *ProbandT1.dcm* from MeVisLab demo data. In order to create contours (CSOs), we need a `SoView2DCSOExtensibleEditor` module. It manages attached CSO editors, renderers and offers an optional default renderer for all types of CSOs.

Add a `SoCSOEllipseEditor` and a `CSOListContainer` to the `SoView2DCSOExtensibleEditor`

![Initial Network](/images/tutorials/dataobjects/contours/Example_7_3.png "Initial Network")

You are now able to draw CSOs.

Create a separate directory for this tutorial and save your network in this empty directory. This makes the final structure easier to read.

### Create a local macro module
Select the module `CSOListContainer` and open menu {{<menuitem "File" "Create Local Macro" >}}. Enter some details about your new local macro module and click finish. Leave the already defined output as is.

![Create Local Macro](/images/tutorials/dataobjects/contours/Example_7_4.png "Create Local Macro")

The appearance of the `CSOListContainer` module changes, because it is a macro module named `csoList` now.

![Network with new local macro](/images/tutorials/dataobjects/contours/Example_7_5.png "Network with new local macro")

The behavior of your network does not change. You can still draw the same CSOs and they are still managed by the `CSOListContainer` module. The reason why we created a local macro with a single module inside is, that we want to add Python scripting to the module. Python scripts can only be added to macro modules.

Open the context menu of your `csoList` module {{< mousebutton "right" >}} and select {{<menuitem "Related Files" "csoList.script" >}}.

The MeVisLab text editor MATE opens, showing your script file. You can see the output of your module as *CSOListContainer.outCSOList*. We want to define a threshold for the color of our CSOs. Therefore add another field to the *Parameters* section of your script file named *areaThreshold*. Define the *type* as *Float* and *value* as *2000.0*.

In order to call Python functions, we also need a Python file. Add a *Commands* section and define the *source* of the Python file as *$(LOCAL)/csoList.py*. Also add an *initCommand* as *initCSOList*. The initCommand defines the Python function which is called whenever the module is added to the workspace or reloaded.

{{< highlight filename="csoList.script" >}}
```Stan
Interface  {
  Inputs {}
  Outputs  {
    Field baseOut0 {
      internalName = CSOListContainer.outCSOList
    }
  }
  Parameters {
    Field areaThreshold { type = Float value = 2000.0 }
  }
}

Commands {
  source = $(LOCAL)/csoList.py
  initCommand = initCSOList
}
```
{{</highlight>}}

Right-click {{< mousebutton "right" >}} on the *initCSOList* command and select {{<menuitem "Create Python Function initCSOList" >}}. The Python file and the function are generated automatically.

Back in MeVisLab, the new field *areaThreshold* can be seen in Module Inspector when selecting your module. The next step is to write the Python function *initCSOList*.

### Write Python script
Whenever the local macro module is added to the workspace or reloaded, new CSOLists shall be created and we need a possibility to update the lists whenever a new CSO has been created or existing contours changed.

Define a function *setupCSOList*.

{{< highlight filename="csoList.py" >}}
```Python
def setupCSOList():
    csoList = _getCSOList()
    csoList.removeAll()
    csoGroupSmall = csoList.addGroup("small")
    csoGroupLarge = csoList.addGroup("large")

    csoGroupSmall.setUsePathPointColor(True)
    csoGroupSmall.setPathPointColor((0,0,1))

    csoGroupLarge.setUsePathPointColor(True)
    csoGroupLarge.setPathPointColor((1,0,0))

def _getCSOList():
    return ctx.field("CSOListContainer.outCSOList").object()
```
{{</highlight>}}

The function gets the current CSOList from the output field of the `CSOListContainer`. Initially it should be empty. If not, we want to start with an empty list, therefore we remove all existing CSOs.

We also create two new CSO lists: one list for small contours, one list for larger contours, depending on the defined *areaThreshold* from the modules parameter.

Additionally, we also want to define different colors for the CSOs in the lists. Small contours shall be drawn green, large contours shall be red.

In order to listen for changes on the contours, we need to register for notifications. Create a new function *registerForNotification*.

{{< highlight filename="csoList.py" >}}
```Python
def registerForNotification():
    csoList = _getCSOList()
    csoList.registerForNotification(csoList.NOTIFICATION_CSO_FINISHED, ctx, "csoFinished")

def csoFinished(_arg):
    csoList = _getCSOList()
    for cso in csoList.getCSOs():
      cso.removeFromAllGroups()
      csoArea = cso.getArea()
      csoGroup = csoList.getGroupByLabel("large")
      if csoArea <= _getAreaThreshold():
        csoGroup = csoList.getGroupByLabel("small")
      csoGroup.addCSO(cso.getId())

def _getAreaThreshold():
    return ctx.field("areaThreshold").value
```
{{</highlight>}}

The function gets all currently existing CSOs from the `CSOListContainer`. Then, we register for notifications on this list. Whenever the notification *NOTIFICATION_CSO_FINISHED* is sent in the current context, we call the function *csoFinished*.

The *csoFinished* function again needs all existing contours. We walk through all single CSOs in the list and remove it from all groups. As we do not know which CSO has been changed from the notification, we evaluate the area of each CSO and add them to the correct list again.

The function *getAreaThreshold* returns the current value of our parameter field *areaThreshold*.

Now we can call our functions in the *initCSOList* function and test our module.

{{< highlight filename="csoList.py" >}}
```Python
def initCSOList():
    setupCSOList()
    registerForNotification()

def setupCSOList():
    csoList = _getCSOList()
    csoList.removeAll()
    csoGroupSmall = csoList.addGroup("small")
    csoGroupLarge = csoList.addGroup("large")

    csoGroupSmall.setUsePathPointColor(True)
    csoGroupSmall.setPathPointColor((0,1,0))

    csoGroupLarge.setUsePathPointColor(True)
    csoGroupLarge.setPathPointColor((1,0,0))

def registerForNotification():
    csoList = _getCSOList()
    csoList.registerForNotification(csoList.NOTIFICATION_CSO_FINISHED, ctx, "csoFinished")

def csoFinished(_arg):
    csoList = _getCSOList()
    for cso in csoList.getCSOs():
      cso.removeFromAllGroups()
      csoArea = cso.getArea()
      csoGroup = csoList.getGroupByLabel("large")
      if csoArea <= _getAreaThreshold():
        csoGroup = csoList.getGroupByLabel("small")
      csoGroup.addCSO(cso.getId())

def _getAreaThreshold():
    return ctx.field("areaThreshold").value

def _getCSOList():
    return ctx.field("CSOListContainer.outCSOList").object()
```
{{</highlight>}}

![Final Network](/images/tutorials/dataobjects/contours/Example_7_6.png "Final Network")

If you now draw contours, they are automatically colored depending on the size. You can also edit existing contours and the color is adapted.

## Summary
* The module `CSOListContainer` provides a lightweight Python interface to manage contours. 
* It makes sense to encapsulate a single module into a macro module to provide additional functionalities via Python scripting.
* Notifications can be used to react on events.

{{< networkfile "examples/data_objects/contours/example7/CSOListContainer.zip" >}} 
