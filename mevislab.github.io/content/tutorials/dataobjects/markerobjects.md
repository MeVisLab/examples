---
title: "Marker Objects"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 750
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Marker"]
menu: 
  main:
    identifier: "markers"
    title: "Marker Objects in MeVisLab"
    weight: 750
    parent: "dataobjects"
---

# Markers in MeVisLab {#MarkersInMeVisLab}
In MeVisLab, you can attach markers to images and other data objects. In this example, you will see how to create, process, and use markers.

## Creation and Rendering
To create markers, you can use a marker editor, for example, the `SoView2DMarkerEditor`. Connect this editor to a viewer as shown below. Now you can interactively create new markers. Connect the module `XMarkerListContainer` to your marker editor to store markers in a list.

![Create markers](images/tutorials/dataobjects/markers/DO_Markers_01.png "Create markers")

Using the `StylePalette` module, you can define a style for your markers. In order to set different styles for different markers, change the field <field>Color Mode</field> in the panel of `SoView2DMarkerEditor` to *Index*.

![Style of markers](images/tutorials/dataobjects/markers/DO_Markers_08.png "Style of markers")

With the help of the module `So3DMarkerRenderer`, markers of an `XMarkerList` can be rendered in 3D.

![Rendering of markers in 2D and in 3D](images/tutorials/dataobjects/markers/DO_Markers_09.png "Rendering of markers in 2D and in 3D")

## Working With Markers
{{<alert class="info" caption="Info">}}
It is possible to convert other data objects into markers and also to convert markers into other data objects. 
It is, for example, possible to set markers by using the `MaskToMarkers` module and later on generate a surface object from a list of markers using the `MaskToSurface` module. Marker conversion can also be done by various other modules, listed in [ *Modules* &rarr; *Geometry* &rarr; *Marker* ].
{{</alert>}}

Learn how to convert markers by building the following network. Press the <field>Update</field>/<field>Apply</field> buttons of the modules `MaskToMarkers` and `MarkersToSurface` to enable the conversion. Now you can see both the markers and the created surface in the module `SoExaminerViewer`. Use the toggle options of the modules `SoToggle` and `SoWEMRenderer` to enable or disable the visualization of markers and surface.

{{<alert class="info" caption="Info">}}
Make sure to set <field>Lower Threshold</field> of the `MaskToMarkers` module to *1000*, so that the 3D object is rendered correctly.
{{</alert>}}

![Convert markers to surface](images/tutorials/dataobjects/markers/DO_Markers_02.png "Convert markers to surface")

## Exercise
Get the HU value of the image at your markers location.

## Summary
* Markers are single point objects located at a defined location in your image.
* Markers can be converted to be rendered in 3D.