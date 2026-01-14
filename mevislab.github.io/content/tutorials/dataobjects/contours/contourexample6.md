---
title: "Contour Example 6: Adding Labels to Contours"
date: "2024-03-11"
status: "OK"
draft: false
weight: 690
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Contours", "CSO", "Label"]
menu: 
  main:
    identifier: "contourexample6"
    title: "Adding Labels to Contours"
    weight: 690
    parent: "contours"
---

# Contour Example 6: Adding Labels to Contours {#TutorialContoursExample6}

{{< youtube "-ACAoeK2Fm8">}}

## Introduction
In this example, we are adding a label to a contour. The label provides information about measurements and about the contour itself. The label remains connected to the contour and can be moved via mouse interactions.

## Steps to Do

### Develop Your Network
Add the modules `LocalImage` and `View2D` to your workspace and connect them as shown below. Load the file *ProbandT1.dcm* from MeVisLab demo data. In order to create contours (CSOs), we need a `SoView2DCSOExtensibleEditor` module. It manages attached CSO editors, renderers and offers an optional default renderer for all types of CSOs.

The first CSO we want to create is a distance line. Add a `SoCSODistanceLineEditor` to the `SoView2DCSOExtensibleEditor`. It renders and interactively generates CSOs that consist of a single line segment. The line segment can be rendered as an arrow; it can be used to measure distances.

We are going to add some more editors later. In order to have the same look and feel for all types of CSOs, add a `SoCSOVisualizationSettings` module as seen below. The module is used to adjust visual parameters like color and line style for CSOs. Also add a `CSOManager` module to organize CSOs and CSOGroups within a network.

![Initial Network](images/tutorials/dataobjects/contours/Ex6_1.png "Initial Network")

We are now able to create lines in the `View2D`. You can also modify the lines by dragging the seed points to a different location.

![SoCSODistanceLineEditor](images/tutorials/dataobjects/contours/Ex6_2.png "SoCSODistanceLineEditor")

The created lines do neither provide any details about the length of your measurement, nor a unique ID to identify it in the case of multiple CSOs.

Add a `CSOLabelRenderer` module to your network and connect it to a `SoGroup`. Also connect your `SoCSODistanceLineEditor` to the `SoGroup` as seen below. The *ID* of each CSO appears next to your distance lines. Moving the ID also shows the *name* of the contour.

![CSOLabelRenderer](images/tutorials/dataobjects/contours/Ex6_14.png "CSOLabelRenderer")

We now want to customize the details to be shown for each distance line. Open the panel of the `CSOLabelRenderer`. You can see the two parameters *labelString* and *labelName*. The *labelString* is set to the *ID* of the CSO. The *labelName* is set to a static text and the *label* property of the CSO. The label can be defined in the module `CSOManager`. You can do this, but we are not defining a name for each contour in this example.

Enter the following to the panel of the `CSOLabelRenderer` module:
{{< highlight filename="CSOLabelRenderer" >}}
```Python
labelString = f'Length: {cso.getLength()} mm'
labelName = f'ID: {cso.getId()}'
deviceOffsetX = 0
deviceOffsetY = 0
```
{{</highlight>}}

We are setting the *labelName* to a static text showing the type of the CSO and the unique *ID* of the contour. We also define the *labelString* to the static description of the measurement and the *length* parameter of the CSO.

![labelString and labelName](images/tutorials/dataobjects/contours/Example6_5.png "labelString and labelName")

You can also round the length by using:
{{< highlight filename="CSOLabelRenderer" >}}
```Python
labelString = f'Length: {cso.getLength():.2f} mm'
```
{{</highlight>}}

In order to see all possible parameters of a CSO, add a `CSOInfo` module to your network and connect it to the `CSOManager`. The geometric information of the selected CSO from `CSOManager` can be seen there.

![CSOInfo](images/tutorials/dataobjects/contours/Ex6_CSOInfo.png "CSOInfo")

For labels shown on gray value images, it makes sense to add a shadow. Open the panel of the `SoCSOVisualizationSettings` module and on tab *Misc* check the option *Should render shadow*. This increases the readability of your labels.

{{< imagegallery 2 "images/tutorials/dataobjects/contours/" "Ex6_NoShadow" "Ex6_Shadow" >}}

If you want to define your static text as a parameter in multiple labels, you can open the panel of the `CSOLabelRenderer` module and define text as *User Data*. The values can then be used in Python via *userData*.

![User Data](images/tutorials/dataobjects/contours/Ex6_Parameters.png "User Data")

You can also add multiple CSO editors to see the different options. Add the `SoCSORectangleEditor` module to your workspace and connect it to the `SoGroup` module. As we now have two different editors, we need to tell the `CSOLabelRenderer` which CSO is to be rendered. Open the panel of the `SoCSODistanceLineEditor`. You can see the field *Extension Id* set to *distanceLine*. Open the panel of the `SoCSORectangleEditor`. You can see the field *Extension Id* set to *rectangle*.

![Extension ID](images/tutorials/dataobjects/contours/Ex6_ExtensionID.png "Extension ID")

We currently defined the *labelName* and *labelString* for the distance line. If we want to define different labels for different types of CSOs, we have to change the `CSOLabelRenderer` Python script. Open the panel of the `CSOLabelRenderer` and change the Python code to the following:

{{< highlight filename="CSOLabelRenderer" >}}
```Python
if cso.getSubType() == 'distanceLine':
  labelString =  f'{userData0} {cso.getLength():.2f} mm'
  labelName = userData1
  labelName += str(cso.getId())
elif cso.getSubType() == 'rectangle':
  labelString = f'{userData0} {cso.getLength():.2f} mm\n'
  labelString += f'{userData2} {cso.getArea():.2f} mm^2'
  labelName = userData3
  labelName += str(cso.getId())
deviceOffsetX = 0
deviceOffsetY = 0
```
{{</highlight>}}

![SoCSORectangleEditor](images/tutorials/dataobjects/contours/Ex6_LineAndRectangle.png "SoCSORectangleEditor")

If you now draw new CSOs, you will notice that you still always create distance lines. Open the panel of the `SoView2DCSOExtensibleEditor`. You can see that the *Creator Extension Id* is set to *__default*. By default, the first found eligible editor is used to create a new CSO. In our case this is the `SoCSODistanceLineEditor`.

![SoCSORectangleEditor](images/tutorials/dataobjects/contours/Ex6_DefaultExtension.png "SoCSORectangleEditor")

Change *Creator Extension Id* to *rectangle*.

![SoCSORectangleEditor & SoView2DCSOExtensibleEditor ](images/tutorials/dataobjects/contours/Ex6_8.png "SoCSORectangleEditor & SoView2DCSOExtensibleEditor")

Newly created CSOs are now rectangles. The label values are shown as defined in the `CSOLabelRenderer` and show the length and the area of the rectangle.

![Labeled Rectangle in View2D](images/tutorials/dataobjects/contours/Ex6_9.png "Labeled Rectangle in View2D")

{{<alert class="info" caption="Extra Infos">}}
The *Length* attribute in the context of rectangles represents the perimeter of the rectangle, calculated as *2a + 2b*, where *a* and *b* are the lengths of the two sides of the rectangle.
{{</alert>}}

You will find a lot more information in the `CSOInfo` module for your rectangles. The exact meaning of the values for each type of CSO is explained in the table below.

![CSOInfo](images/tutorials/dataobjects/contours/Ex6_10.png "CSOInfo")

## Parameters and Meanings for All CSO Types
<table class="table table-striped">
  <thead>
    <tr>
      <th>CSO Editor</th>
      <th>PCA X Ext.</th>
      <th>PCA Y Ext.</th>
      <th>PCA Z Ext.</th>
      <th>Length</th>
      <th>Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SoCSOPointEditor</td>
      <td>n.a.</td>
      <td>n.a.</td>
      <td>n.a.</td>
      <td>n.a.</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <td>SoCSOAngleEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSOArrowEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSODistanceLineEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Length (in mm)</td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSODistancePolylineEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Length of all lines (in mm)</td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSOEllipseEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Perimeter (in mm)</td>
      <td>Area (in mm2)</td>
    </tr>
    <tr>
      <td>SoCSORectangleEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Length of all sides (in mm)</td>
      <td>Area (in mm2)</td>
    </tr>
    <tr>
      <td>SoCSOSplineEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSOPolygonEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Length of all lines (in mm)</td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSOIsoEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SoCSOLiveWireEditor</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## Summary
* Custom labels can be added to contours using the `CSOLabelRenderer` module. 
* Python scripting is used within the `CSOLabelRenderer` module to customize label content based on CSO types.
* Visual properties can be adjusted within the `CSOLabelRenderer` and the `SoCSOVisualizationSettings` modules to improve label visibility and appearance.

{{< networkfile "examples/data_objects/contours/example6/ContourExample6.mlab" >}} 
