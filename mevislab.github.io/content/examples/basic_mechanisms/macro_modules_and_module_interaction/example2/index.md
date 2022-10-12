---
layout: post
title: "Example 2: Python scripting"
tags: ["Examples", "Example Networks", "Contour Filter"]
---

# Example 2: Python scripting
This example shows how to create module interactions via Python scripting.

## Summary
A new Macro Module `IsoCSOs` is created providing 2 viewers in the internal network. One `View2D` and one `SoExaminerViewer`. Both viewers are added to the custom user interface of the module.

Additional Buttons for Browsing directories and creating contours (`CSOIsoGenerator`) are added calling Python functions to explain how Python can be used in MeVisLab. In the end, a field listener is implemented calling a Python function whenever a field of the internal network changes. This is used to colorize the contours under the mouse.

![Screenshot](/examples/basic_mechanisms/macro_modules_and_module_interaction/example2/image.png)

# Download
The files need to be added to a package. You can download the example network [here](/examples/basic_mechanisms/macro_modules_and_module_interaction/example2/ScriptingExample2.zip)
