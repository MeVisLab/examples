---
title: "Example 2: Use trained PyTorch network in MeVisLab"
date: 2023-05-16
status: "OK"
draft: false
weight: 860
tags: ["Advanced", "Tutorial", "PyTorch", "Python", "PythonPip", "AI"]
menu: 
  main:
    identifier: "pytorchexample2"
    title: "Use a trained network from PyTorch hub in MeVisLab Python."
    weight: 893
    parent: "pytorch"
---
# Example 2: Use trained PyTorch network in MeVisLab

## Introduction
In the previous tutorial, you learned how to install PyTorch for usage in MeVisLab. In this example we are using a trained network from torch.hub for creating a brain parcellation map on MeVisLab demo images.

Make sure that you successfully executed [Example 1: Install PyTorch by using the PythonPip module](/tutorials/thirdparty/pytorch/pytorchexample1/) before starting.

Add the module `PythonPip` to your workspace and make sure that *torch* and *torchvision* are installed in your MeVisLab package.

## Steps to do
Add a `PythonImage` module to your workspace. We are using it to load an image from disk and execute the PyTorch network. Create your own MeVisLab package as described in [Example 2.1: Package creation](/tutorials/basicmechanisms/macromodules/package/)

Save your network containing the `PythonImage` module as *\*.mlab* file. Create a Macro Module as described in [Example 2.2: Global Macro modules](/tutorials/basicmechanisms/macromodules/globalmacromodules/) and use the network you just saved. Make sure to add a Python file in Macro Module Wizard.

Open the *\*.script* file of your Macro Module via right click {{< mousebutton "right" >}} and select {{< menuitem "Related Files" "<MODULE_NAME>.script">}}

### Write the script file
Enter the following:


{{< highlight filename="<MODULE_NAME>.script" >}}
```Stan
Interface {
  Inputs {
    Field inputImage { type = Image }
  }
  Outputs {
    Field outImage { internalName = PythonImage.output0 }
  }
  Parameters {
    Field start { type = Trigger }
  }
}


Commands {
  source = $(LOCAL)/DemoAI.py
  
  FieldListener start { command = onStart }
}
```
{{</highlight>}}

First, we define the fields *inputImage* and *outputImage* to connect external images and viewer to our Macro Module.

Then we have a trigger field *start* to start processing of the image. The FieldListener calls a Python function *onStart* whenever the trigger is executed, means we also need the Python function *onStart*.

### The Python file

