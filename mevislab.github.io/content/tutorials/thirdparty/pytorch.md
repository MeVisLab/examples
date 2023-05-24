---
title: "PyTorch"
date: 2023-05-16
status: "OK"
draft: false
weight: 870
tags: ["Advanced", "Tutorial", "PyTorch", "AI"]
menu: 
  main:
    identifier: "pytorch"
    title: "PyTorch"
    weight: 870
    parent: "thirdparty"
---
# PyTorch {#pytorch}
## Introduction
[PyTorch](http://www.pytorch.org "pytorch") is a machine learning framework based on the Torch library, used for applications such as Computer Vision and Natural Language Processing, originally developed by Meta AI and now part of the Linux Foundation umbrella.

A lot of AI frameworks can be used within MeVisLab. We currently do not provide a preintegrated AI framework though as we try to avoid compatibility issues and AI frameworks are very fast-moving by nature.

Maybe also take a look at:
* [TensorFlow](https://www.tensorflow.org "tensorflow")
* [Keras](https://keras.io "Keras")
* [scikit-learn](https://scikit-learn.org "scikit-learn")

{{<alert class="info" caption="Attention">}}
We are not explaining PyTorch itself. These tutorials shall be examples how to integrate and use PyTorch in MeVisLab. Detailed tutorials for using PyTorch can be found [here](https://pytorch.org/tutorials/).
{{</alert>}}

## Available Tutorials
### Install PyTorch by using the PythonPip module
The first example shows how to install *torch* and *torchvision* by using the MeVisLab module `PythonPip`. This module can be used to install Python packages not integrated into MeVisLab.

### Use trained PyTorch networks in MeVisLab
In this example, we are using a pre-trained network from [torch.hub](https://pytorch.org/hub/) to generate an AI based image overlay of a brain parcellation map.

### Segment persons in webcam videos
The second tutorial adapts the XXX tutorial to segment a person in a webcam stream. The network has been taken from [torchvision](https://pytorch.org/vision/stable/index.html).

