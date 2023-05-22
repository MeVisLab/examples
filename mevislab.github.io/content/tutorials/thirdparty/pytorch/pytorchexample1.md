---
title: "Example 1: Install PyTorch by using the PythonPip module"
date: 2023-05-16
status: "OK"
draft: false
weight: 860
tags: ["Advanced", "Tutorial", "PyTorch", "Python", "PythonPip", "AI"]
menu: 
  main:
    identifier: "pytorchexample1"
    title: "Install PyTorch by using the PythonPip module."
    weight: 860
    parent: "pytorch"
---
# Example 1: Install PyTorch by using the PythonPip module

## Introduction
The module `PythonPip` allows you to install additional Python packages to be used in MeVisLab. You should not use the general Python *pip* command from locally installed Python, because MeVisLab will not know these packages and they cannot be used in MeVisLab directly.

The module either allows to install packages into the global MeVisLab installation directory, or into your defined user package. We will use the user package directory, because then the installed packages remain available in your packages even if you uninstall or update MeVisLab. In addition to that, no administrative rights are necessary if you did install MeVisLab for all users.

{{<alert class="warning" caption="Warning">}}
Installing additional Python packages into MeVisLab by using the `PythonPip` module requires administrative rights if you do not install into a user package. In addition to that, the installed packages are removed when uninstalling MeVisLab.
{{</alert>}}

### Steps to do
#### The PythonPip module
Add a `PythonPip` module to your workspace. 

![PythonPip module](/images/tutorials/thirdparty/pytorch_example1_1.png "PythonPip module")

Double-click {{< mousebutton "left" >}} the module and inspect the panel.

![PythonPip panel](/images/tutorials/thirdparty/pytorch_example1_2.png "PythonPip panel")

The panel shows all currently installed Python packages including version and MeVisLab package. You can see a warning that the target package is write protected in case you are selecting a MeVisLab package. Change to one of your user packages (see [Example 2.1: Package creation](/tutorials/basicmechanisms/macromodules/package/) for details). The warning disappears.

![Select user package](/images/tutorials/thirdparty/pytorch_example1_3.png "Select user package")

{{<alert class="info" caption="Additional Information">}}
Additional Information about the `PythonPip` module can be found in [Example 4: Install additional Python packages via PythonPip module](/tutorials/basicmechanisms/macromodules/pythonpip "PythonPip module").
{{</alert>}}

#### Install torch and torchvision
For our tutorials, we need to install *torch* and *torchvision*. Enter *torch torchvision* into the *Command* textbox and press *Install*.

{{<alert class="info" caption="Info">}}
We are using the CPU version of PyTorch for our tutorials, because it shall be possible to execute all steps without having a large GPU. In case you have a GPU with CUDA support, you can install the necessary packages by using the PyTorch documentation available [here](https://pytorch.org/get-started/locally "PyTorch documentation").
{{</alert>}}

Example for CUDA support:
{{< highlight filename="Command" >}}
```txt
torch torchvision --index-url https://download.pytorch.org/whl/cu117

```
{{</highlight>}}

{{<alert class="info" caption="Attention">}}
If you are behind a proxy server, you may have to set the **HTTP_PROXY** and **HTTPS_PROXY** environment variables to the hostname and port of your proxy. These are used by pip when accessing the internet.

Alternatively you can also add a parameter to *pip install* command: *--proxy https://proxy:port*
{{</alert>}}

![Install torch and torchvision](/images/tutorials/thirdparty/pytorch_example1_4.png "Install torch and torchvision")

After clicking *Install*, the pip console output opens and you can follow the process of the installation.

![Python pip output](/images/tutorials/thirdparty/pytorch_example1_5.png "Python pip output")

After the installation was finished with exit code 0, you should see the new packages in the `PythonPip` module.

![PyTorch installed](/images/tutorials/thirdparty/pytorch_example1_6.png "PyTorch installed")


## Summary
* The module `PythonPip` allows you to install additional Python packages for using them in MeVisLab
