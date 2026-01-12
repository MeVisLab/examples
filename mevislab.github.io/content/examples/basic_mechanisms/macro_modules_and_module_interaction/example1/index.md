---
layout: post
title: "Panel for the contour filter"
category: "basic_mechanisms"
---

# Example 1: Panel for the Contour Filter
This example contains a whole package structure. Inside you can find the example contour filter for which a panel was created.

## Summary
A new macro module `Filter` has been created. Initially, macro modules do not provide an own panel containing user interface elements such as buttons. The *Automatic Panel* is shown on double-clicking the module providing the name of the module.

In this example we update the *.script* file of the `Filter` module to display the kernel selection field of the `Convolution` module within its network. 

{{<alert class="info" caption="Info">}}
Changes applied to fields in the macro module's panel are applied to their internal network as well.
{{</alert>}}

![Screenshot](/examples/basic_mechanisms/macro_modules_and_module_interaction/example1/image.png)

# Download
You can download the example network [here](/examples/basic_mechanisms/macro_modules_and_module_interaction/example1/FilterExample.zip)
