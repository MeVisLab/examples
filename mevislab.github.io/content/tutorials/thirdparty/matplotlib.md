---
title: "Matplotlib"
date: 2023-05-25
status: "OK"
draft: false
weight: 880
tags: ["Advanced", "Tutorial", "Matplotlib", "Visualization"]
menu: 
  main:
    identifier: "matplotlib"
    title: "Matplotlib"
    weight: 880
    parent: "thirdparty"
---
# Matplotlib

Matplotlib, introduced by John Hunter in 2002 and initially released in 2003, is a comprehensive data visualization library in Python. It is widely used among the scientific world as it is easy to grasp for beginners and provides high quality plots and images, that are widely customizable. The documentation on Matplotlib along with general examples, cheat sheets and a starting guide can be found [here](https://matplotlib.org/).

As MeVisLab supports the integration of Python scripts e. g. for test automation, Matplotlib can be used to visualize any data you might want to see. And as it is directly integrated into MeVisLab, you don't have to install it (via `PythonPip` module) first.

In the following tutorial pages on Matplotlib, you will be shown how to create a module in MeVisLab, that helps you plot grayscale distributions of single slices or defined sequences of slices of a DICOM and layer the grayscale distributions of two chosen slices for comparison.