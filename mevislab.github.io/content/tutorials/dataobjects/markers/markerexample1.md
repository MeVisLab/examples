---
title: "Example 1: Distance between Markers"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 755
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "3D", "Marker"]
menu: 
  main:
    identifier: "markerexample1"
    title: "Calculate the distance between Marker objects."
    weight: 755
    parent: "markers"
---
# Example 1: Calculating the Distance Between Markers

{{< youtube "xYR5Qkze0lE">}}

## Introduction
In this example, we will measure the distance between one position in an image to a list of markers.

## Steps to Do
### Develop Your Network
Add the following modules and connect them as shown.

We changed the names of the modules `SoView2DMarkerEditor` and `XMarkerListContainer`, to distinguish these modules from two similar modules we will add later on. Open the panel of `SoView2DMarkerEditor` and select the tab *Drawing*. Now choose the *Color* *red*. 

![Marker Color](images/tutorials/dataobjects/markers/DO_Markers_03.png "Marker Color")

As a next step, add two more modules: `SoView2DMarkerEditor` and `XMarkerListContainer`.

Change their names and the marker color to *green* and connect them as shown. We also like to change the mouse button you need to press in order to create a marker. This allows to place both types of markers, the red ones and the green ones. In order to do this, open the panel of `GreenMarker`. Under *Buttons*, you can adjust which button needs to be pressed in order to place a marker. Select the *Button2* (the middle button of your mouse {{< mousebutton "middle" >}}) instead of *Button1* (the left mouse button {{< mousebutton "left" >}}).

In addition to that, we like to allow only one green marker to be present. If we place a new marker, the old marker should vanish. For this, select the *Max Size* to be one and select *Overflow Mode: Remove All*.

![Marker Editor Settings](images/tutorials/dataobjects/markers/DO_Markers_04.png "Marker Editor Settings")

### Create Markers of Different Type
Now, we can place as many red markers as we like, using the left mouse button {{< mousebutton "left" >}} and only one green marker using the middle mouse button {{< mousebutton "middle" >}}.

![Two Types of Markers](images/tutorials/dataobjects/markers/DO_Markers_05.png "Two Types of Markers")

### Calculate the Distance Between Markers
We like to calculate the minimum and maximum distance of the green marker to all red markers. In order to do this, add the module `DistanceFromXMarkerList` and connect it to `RedMarkerList`. Open the panels of `DistanceFromXMarkerList` and `GreenMarkerList`. Now, draw a parameter connection from the coordinate of the green marker, which is stored in the field *Current Item -> Position* in the panel of `GreenMarkerList`, to the field *Position* of `DistanceFromXMarkerList`. You can now press *Calculate Distance* in the panel of `DistanceFromXMatkerList` to see the result, meaning the distance of the green marker to all red markers in the panel of `DistanceFromXMarkerList`.

![Module DistanceFromXMarkerList](images/tutorials/dataobjects/markers/DO_Markers_06.png "Module DistanceFromXMarkerList")

### Automation of Distance Calculation
To automatically update the calculation when placing a new marker, we need to tell the module `DistanceFromXMarkerList` **when** a new green marker is placed. Open the panels of `DistanceFromXMarkerList` and `GreenMarker` and draw a parameter connection from the field *Currently busy* in the panel of `GreenMarker` to *Calculate Distance* in the panel of `DistanceFromXMarkerList`. If you now place a new green marker, the distance from the new green marker to all red markers is calculated automatically.
![Calculation of Distance between Markers](images/tutorials/dataobjects/markers/DO_Markers_07.png "Calculation of Distance between Markers")

{{<alert class="info" caption="Additional Information">}}
Another example for using a `SoView2DMarkerEditor` module can be found at [Image Processing - Example 3: Region Growing](tutorials/image_processing/image_processing3 "Image Processing - Example 3: Region Growing")
{{</alert>}}

## Summary
* Markers can be created using `SoView2DMarkerEditor`.
* Markers can be stored and managed using `XMarkerListContainer`.
* The distance between markers can be calculated using `DistanceFromXMarkerList`.

{{< networkfile "examples/data_objects/markers/example1/Marker_Example1.mlab" >}}
