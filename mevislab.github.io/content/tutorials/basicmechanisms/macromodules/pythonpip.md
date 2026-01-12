---
title: "Example 4: Installing additional Python packages using the PythonPip module"
date: 2023-05-16
status: "OK"
draft: false
weight: 450
tags: ["Advanced", "Tutorial", "Python", "PythonPip", "pip"]
menu: 
  main:
    identifier: "pythonpip"
    title: "Installing additional Python packages using the PythonPip module"
    weight: 450
    parent: "basicmechanisms"
---
# Example 4: Installing Additional Python Packages Using the PythonPip Module
## Introduction
MeVisLab already comes with a lot of integrated third-party software tools ready to use. Nevertheless, it might be necessary to install additional Python packages for your specific needs. This example will walk you through the process of adding packages through usage of/using the `PythonPip` module.

The `PythonPip` module allows to work with the Python package manager pip. It can be used to install Python packages into the site-packages of the MeVisLab Python installation.

It technically provides the full Python package ecosystem, though you will have to keep some things in mind to avoid your newly added packages to interfere with the existing ones that MeVisLab operates on:

* Packages can contain C-Extensions (since we use the same MSVC compiler resp. same GCC settings as Python 3 itself), *but* you can only install packages that do not interfere with packages or DLLs that are already part of MeVisLab. This means that installing packages with C-Extensions might work in many circumstances, but is not guaranteed to work
* **All installed packages with C-Extensions are release only**, so you can only import them in a release MeVisLab (under Windows)

{{<alert class="info" caption="Attention">}}
On Windows: Existing packages (e.g., *NumPy*) can only be upgraded if they haven't already been loaded by MeVisLab's Python. So please make sure to start with a *fresh* MeVisLab
{{</alert>}}

**Packages that you should not upgrade or install (because they have been adapted for MeVisLab):**
* vtk
* cv2 (OpenCV)
* PySide2 / PyQt (we have our own PythonQt binding and our own Qt DLLs)
* matplotlib

These are some of the most important packages that have been adapted for MeVisLab. If you seem to have a problem upgrading another one that is not listed here, make sure to ask in the [MeVisLab forum](https://forum.mevislab.de) or directly contact our developers via [EMail](mailto://info@mevislab.de).

### Working with the PythonPip Module on your MeVisLab Workspace
The module `PythonPip` can be found via module search. It provides a user interface showing the currently installed Python packages including version and MeVisLab package it has been installed to.

![PythonPip interface](/images/tutorials/thirdparty/pytorch_example1_2.png "PythonPip interface")

Select the package to install the Python package into, write the name of the package and click install.

In the case you want to install a specific version, you can also use *<PACKAGE>==1.2.0*

{{<alert class="info" caption="Attention">}}
We strongly recommend to install the packages into a MeVisLab user package. This has many advantages:
* User packages can be updated without administrator privileges
* User packages remain available after uninstalling and/or updating MeVisLab
* It is possible to install multiple versions of the Python packages into different user packages. Possible conflicts will be shown in the `PythonPip` module panel.

The only disadvantage: Python commands will not be recognized outside of MeVisLab by default. 
{{</alert>}}

Thirdparty information and *.mli* files are updated automatically.

### Using the Commandline
Another option is using the commandline tool provided by MeVisLab. Under Windows, you need to change to directory *Packages\MeVis\ThirdParty\Python* first.

{{< highlight filename="commandline" >}}
```cmd
MeVisPython -m pip ...
```
{{</highlight>}}

{{<alert class="info" caption="Attention">}}
The commandline option does not provide the possibility to install into a specified user package. Third-party information and *.mli* files are not adapted automatically with the commandline tool.
{{</alert>}}

In [Example 1: Installing PyTorch using the PythonPip module](/tutorials/thirdparty/pytorch/pytorchexample1/) we are installing PyTorch to use it in MeVisLab scripting.

## Summary
* The `PythonPip` module allows to install additional Python packages to adapt MeVisLab to a certain extent.
