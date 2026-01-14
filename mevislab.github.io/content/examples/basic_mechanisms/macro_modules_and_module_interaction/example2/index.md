---
layout: post
title: "Python scripting"
category: "basic_mechanisms"
---

# Example 2: Python Scripting
This example shows how to create module interactions via Python scripting.

## Summary
A new macro module `IsoCSOs` is created providing two viewers in its internal network, `View2D` and `SoExaminerViewer`. Both viewers are included in the panel of the module.

To showcase how Python functions can be implemented in MeVisLab and called from within a module, additional buttons to browse directories, and create contours via the `CSOIsoGenerator` are added. Lastly, a field listener is implemented reacting to field changes by colorizing contours when the user hovers over them with the mouse. 

![Screenshot](/examples/basic_mechanisms/macro_modules_and_module_interaction/example2/image2.png)

![Screenshot](/examples/basic_mechanisms/macro_modules_and_module_interaction/example2/image.png)

# Download
The files need to be added to a package. You can download the example network [here](/examples/basic_mechanisms/macro_modules_and_module_interaction/example2/ScriptingExample2.zip)
