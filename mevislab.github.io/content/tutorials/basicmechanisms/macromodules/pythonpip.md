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

It provides the full Python package eco-system to MeVisLab, but it has several drawbacks!
* On macOS:
  * you can only install Python-only packages (packages that contain Python C-Extensions are not supported)
* On Windows and Linux:
  * packages can contain C-Extensions (since we use the same MSVC compiler resp. same GCC settings as Python 3 itself)
  * *but* you can only install packages that do not interfere with packages or DLLs that are already part of MeVisLab
  * this means that installing packages with C-Extensions might work in many circumstances, but is not guaranteed to work
  * **all installed packages with C-Extensions are release only**, so you can only import them in a release MeVisLab

{{<alert class="info" caption="Attention">}}
Since the `PythonPip` module is running in Python itself, make sure that you started a fresh MeVisLab when you want to upgrade an existing package (like *NumPy*), since it can not be upgraded if already loaded by MeVisLab’s Python.
{{</alert>}}

Packages that you should not upgrade or install (because they interfere with DLLs in MeVisLab):
* vtk
* cv2 (OpenCV)
* PySide2 / PyQt (we have our own PythonQt binding and our own Qt DLLs)
* matplotlib (we have our own patched version to support PythonQt)
* probably other packages that we have not thought about

### Using the Module
The module `PythonPip` can be found via module search. It provides a user interface showing the currently installed Python packages including version and MeVisLab package it has been installed to.

![PythonPip interface](/images/tutorials/thirdparty/pytorch_example1_2.png "PythonPip interface")

Select the package to install the Python package into, write the name of the package and click install.

{{<alert class="info" caption="Attention">}}
We strongly recommend to install the packages into a MeVisLab user package. This has many advantages:
* User packages can be updated without administrator privileges
* User packages remain available after uninstalling and/or updating MeVisLab
* It is possible to install multiple versions of the Python packages into different user packages 
{{</alert>}}

### Using the commandline
Another option is using the commandline tool provided by MeVisLab.

{{< highlight filename="commandline" >}}
```cmd
MeVisPython -m pip ...
```
{{</highlight>}}

In [Example 1: Install PyTorch by using the PythonPip module](/tutorials/thirdparty/pytorch/pytorchexample1/) we are installing PyTorch to use it in MeVisLab scripting.
