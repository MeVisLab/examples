---
title: "Example 1: Installing MONAI Using the PythonPip Module"
date: 2025-11-13
status: "OK"
draft: false
weight: 878
tags: ["Advanced", "Tutorial", "MONAI", "Python", "PythonPip", "AI"]
menu: 
  main:
    identifier: "monaiexample1"
    title: "Installing MONAI Using the PythonPip Module"
    weight: 878
    parent: "monai"
---

# Example 1: Installing MONAI Using the PythonPip Module

## Introduction
With the `PythonPip` module, you can import additional Python libraries into MeVisLab.

### Steps to Do

#### Install PyTorch
As *MONAI* requires *PyTorch*, install it by using the `PythonPip` module as described [here](tutorials/thirdparty/pytorch/pytorchexample1/).

#### Install MONAI
After installing *torch* and *torchvision*, we install *MONAI*.

For installing *MONAI* enter \"*monai*\" into the Command textbox and press *Install*.

![Install MONAI](images/tutorials/thirdparty/monai_example1_1.png "Install MONAI")

After clicking *Install*, the pip console output opens and you can follow the process of the installation.

{{<alert class="info" caption="Attention">}}
If you are behind a proxy server, you may have to set the **HTTP_PROXY** and **HTTPS_PROXY** environment variables to the hostname and port of your proxy. These are used by pip when accessing the internet.

Alternatively, you can also add a parameter to *pip install* command: *--proxy https://proxy:port*
{{</alert>}}

![PythonPip MONAI](images/tutorials/thirdparty/monai_example1_2.png "PythonPip MONAI")

After the installation has finished with exit code 0, you should see the new packages in the `PythonPip` module.

![MONAI installed](images/tutorials/thirdparty/monai_example1_3.png "MONAI installed")

## Summary
* *MONAI* can be installed and directly used in MeVisLab by using the `PythonPip` module.
