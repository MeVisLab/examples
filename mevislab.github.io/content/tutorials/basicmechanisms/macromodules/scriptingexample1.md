---
title: "Example 2.5.1: The module RunPythonScript"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 430
tags: ["Beginner", "Tutorial", "Python", "Scripting", "RunPythonScript"]
menu: 
  main:
    identifier: "scriptingexample1"
    title: "The module RunPythonScript"
    weight: 430
    parent: "macro_modules"
---

# Example 2.5.1: The module RunPythonScript

{{< youtube "O5Get1PMOq8" >}}

## Introduction

The module `RunPythonScript` allows to execute Python scripts from within a MeVisLab network. You can draw parameter connection from modules to `RunPythonScript` and back, to process parameter fields using Python scripting. 

## Steps to do
### Develop your network

In this example, we like to dynamically change the color of a cube in an Open Inventor scene. For that, add and connect the following modules as shown. 

![RunPythonScript Example](/images/tutorials/basicmechanics/Scripting_06.png "RunPythonScript")

### Scripting using the moduule `RunPythonScript`

Open the panel of `RunPythonScript`. There is an option to display input and output fields. For that, tick the box *Fields* on the top left side of the panel. 

You can also name these fields individually, by ticking the box *Edit field titles*. Call the first input field *TimeCounter* and draw a parameter connection from the field *Value* of the panel of `TimeCounter` to the input field *TimeCounter* of the module `RunPythonScript`.
We can name the first output field *DiffuseColor* and draw a parameter connection from this field to the field *Diffuse Color* in the panel of the module `SoMaterial`.

![TimeCounter](/images/tutorials/basicmechanics/Scripting_07.png "TimeCounter")

The module `TimeCounter` counts in a defined *Frequency*. We like to randomly change the color of the cube in the frequency the `TimeCounter` counts. Add this code:

{{< highlight filename="IsoCSOs.py" >}}
```Python
import random

red = TimeCounter * random.randrange(0,52)/255
green = TimeCounter * random.randrange(0,52)/255
blue = TimeCounter * random.randrange(0,52)/255

updateOutputValue("DiffuseColor", str(red) + " " + str(green) + " " + str(blue))
```
{{</highlight>}}

To update the output field *DiffuseColor*, it is important to use the methods *updateOutputValue(name, value)* or *setOutputValue(name, value)* instead of simply assigning a value to the output field.

You can now see a color change in the viewer `SoExaminerViewer` every time the `TimeCounter` counts.

![Triggered color change](/images/tutorials/basicmechanics/Scripting_08.png "Triggered color change")


## Summary
* The module `RunPythonScript` can be used to process module fields in your network using Python scripting.
* Use the methods *updateOutputValue(name, value)* or *setOutputValue(name, value)* to update output fields of `RunPythonScript`.