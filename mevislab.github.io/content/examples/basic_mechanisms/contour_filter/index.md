---
layout: post
title: "Example 1: Contour Filter"
tags: ["Examples", "Example Networks", "Contour Filter"]
---

# Example 1: Contour Filter
This example shows how to create a contour filter.

# Summary
Images are loaded via `ImageLoad` module and visualized unchanged in a `View2D` module *View2D1*.
Additionally the images are modified by a local macro module `Filter` and shown in another `View2D` viewer *View2D*.

In order to display the same slice (unchanged and changed), the module `SyncFloat` is used to synchronize the field value *startSlice* in both viewers. The `SyncFloat` module duplicates the value *Float1* to the field *Float2*.

![Screenshot](/examples/basic_mechanisms/contour_filter/image.png)

# Download
You can download the example network [here](/examples/basic_mechanisms/contour_filter/ContourFilter.zip)
