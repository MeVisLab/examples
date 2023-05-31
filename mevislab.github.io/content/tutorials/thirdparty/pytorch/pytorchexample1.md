---
title: "Example 1: Installing PyTorch using the PythonPip module"
date: 2023-05-16
status: "OK"
draft: false
weight: 871
tags: ["Advanced", "Tutorial", "PyTorch", "Python", "PythonPip", "AI"]
menu: 
  main:
    identifier: "pytorchexample1"
    title: "Installing PyTorch using the PythonPip module."
    weight: 871
    parent: "pytorch"
---
# Example 1: Installing PyTorch using the PythonPip module

## Introduction
The module `PythonPip` allows you to install additional Python packages to be used in MeVisLab. 

{{<alert class="warning" caption="Warning">}}
You should not use the general Python *pip* command from a locally installed Python, because MeVisLab will not know these packages and they cannot be used in MeVisLab directly.
{{</alert>}}

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

The panel shows all currently installed Python packages including their version and the MeVisLab package they are saved in. You can see a warning that the target package is set to read-only in case you are selecting a MeVisLab package. Changing to one of your user packages (see [Example 2.1: Package creation](/tutorials/basicmechanisms/macromodules/package/) for details) makes the warning disappear.

![Select user package](/images/tutorials/thirdparty/pytorch_example1_3.png "Select user package")

{{<alert class="info" caption="Additional information">}}
Additional Information on the `PythonPip` module can be found in [Example 4: Install additional Python packages via PythonPip module](/tutorials/basicmechanisms/macromodules/pythonpip "PythonPip module").
{{</alert>}}

#### Install torch and torchvision
For our tutorials, we need to install *torch* and *torchvision*. Enter *torch torchvision* into the *Command* textbox and press *Install*.

{{<alert class="info" caption="Info">}}
We are using the CPU version of PyTorch for our tutorials as we want them to be as accessible as possible. If you happen to have a large GPU capacity (and CUDA support) you can also use the GPU version. You can install the necessary packages by using the PyTorch documentation available [here](https://pytorch.org/get-started/locally "PyTorch documentation").
{{</alert>}}

Continuing with CUDA support:
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
* *PyTorch* can be installed using the `PythonPip` module.
* There are different versions available (CPU and GPU) depending on the hardware that is used
* Additional steps have to be taken depending on the version one wishes to install
* The module displays newly installed packages as soon as the installation was successful
