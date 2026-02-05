---
layout: post
title: "Contour Filter"
category: "basic_mechanisms"
---

# Example 1: Contour Filter
This example shows how to create a contour filter.

# Summary
Images are loaded via `ImageLoad` module and visualized unchanged in a `View2D` module *View2D1*.
Additionally, the images are modified by a local macro module `Filter` and shown in another `View2D` viewer *View2D*.

In order to display the same slice (unchanged and changed), the module `SyncFloat` is used to synchronize the field value <field>startSlice</field> in both viewers. The `SyncFloat` module duplicates the value <field>Float1</field> to the field <field>Float2</field> if it differs by <field>Epsilon</field>.

![Screenshot](examples/basic_mechanisms/contour_filter/image.png)

# Download
You can download the example network [here](examples/basic_mechanisms/contour_filter/ContourFilter.zip)
