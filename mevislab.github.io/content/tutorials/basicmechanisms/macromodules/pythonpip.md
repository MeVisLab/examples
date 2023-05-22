---
title: "Example 4: Install additional Python packages via PythonPip module"
date: 2023-05-16
status: "OK"
draft: false
weight: 450
tags: ["Advanced", "Tutorial", "Python", "PythonPip", "pip"]
menu: 
  main:
    identifier: "pythonpip"
    title: "Install additional Python packages via PythonPip module"
    weight: 450
    parent: "basicmechanisms"
---
# Example 4: Install additional Python packages via PythonPip module
## Introduction
MeVisLab already comes with a lot of integrated third party software tools ready to use. Nevertheless it might be necessary to install additional Python packages for your specific needs. This example shows the usage of the `PythonPip` module in MeVisLab for installing additional Python packages.

The `PythonPip` module allows to work with the Python package manager pip. It can be used to install Python packages into the site-packages of the MeVisLab Python installation.

It provides the full Python package eco-system to MeVisLab, but it has some drawbacks:

* packages can contain C-Extensions (since we use the same MSVC compiler resp. same GCC settings as Python 3 itself)
* *but* you can only install packages that do not interfere with packages or DLLs that are already part of MeVisLab
* this means that installing packages with C-Extensions might work in many circumstances, but is not guaranteed to work
* **all installed packages with C-Extensions are release only**, so you can only import them in a release MeVisLab (under Windows)

{{<alert class="info" caption="Attention">}}
Under Windows: Since the `PythonPip` module is running in Python itself, make sure that you started a fresh MeVisLab when you want to upgrade an existing package (like *NumPy*), since it can not be upgraded if already loaded by MeVisLab’s Python.
{{</alert>}}

Packages that you should not upgrade or install (because they have been adapted for MeVisLab):
* vtk
* cv2 (OpenCV)
* PySide2 / PyQt (we have our own PythonQt binding and our own Qt DLLs)
* matplotlib
* probably other packages that we have not thought about

### Using the Module
The module `PythonPip` can be found via module search. It provides a user interface showing the currently installed Python packages including version and MeVisLab package it has been installed to.

![PythonPip interface](/images/tutorials/thirdparty/pytorch_example1_2.png "PythonPip interface")

Select the package to install the Python package into, write the name of the package and click install.

In case you want to install a specific version, you can also use *<PACKAGE>==1.2.0*

{{<alert class="info" caption="Attention">}}
We strongly recommend to install the packages into a MeVisLab user package. This has many advantages:
* User packages can be updated without administrator privileges
* User packages remain available after uninstalling and/or updating MeVisLab
* It is possible to install multiple versions of the Python packages into different user packages. Possible conflicts will be shown in module panel.

One disadvantage is, that Python commands outside MeVisLab will not find Python packages installed into user packages by default.
{{</alert>}}

Thirdparty information and *\*.mli* files are updated automatically.

### Using the commandline
Another option is using the commandline tool provided by MeVisLab. Under Windows, you need to change to directory *Packages\MeVis\ThirdParty\Python* first.

{{< highlight filename="commandline" >}}
```cmd
MeVisPython -m pip ...
```
{{</highlight>}}

{{<alert class="info" caption="Attention">}}
The commandline option does not provide the possibility to install into a specified user package. Thirdparty information and *\*.mli* files are not adapted automatically with the commandline tool.
{{</alert>}}

In [Example 1: Install PyTorch by using the PythonPip module](/tutorials/thirdparty/pytorch/pytorchexample1/) we are installing PyTorch to use it in MeVisLab scripting.

## Summary
* The module `PythonPip` allows you to install additional Python packages for using them in MeVisLab
