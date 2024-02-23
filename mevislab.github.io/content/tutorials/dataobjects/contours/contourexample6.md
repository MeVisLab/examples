---
title: "Contour Example 6: Adding Labels to Contours"
date: "2024-02-19"
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

## Introduction

In this example, we like to add a label to a contour. The label provides information about measurements and about the contour itself. The label remains connected to the contour and can be moved via mouse interactions.

## Steps to do
### Develop your network

Add the following modules to your workspace and connect them as shown. Load the example DICOM image *ProbandT1.dcm*.

![Data Objects Contours Example 6](/images/tutorials/dataobjects/contours/Ex6_1.png "Data Objects Contours Example 6")

The `SoView2DCSOExtensibleEditor` manages attached CSO editors and renderers and offers an optional default renderer for all types of CSOs.

The `SoCSODistanceLineEditor` renders and interactively generates CSOs that consist of a single line segment. The line segment can be rendered as an arrow; it can be used to measure distances.

The `SoCSOVisualizationSettings` module is used to adjust visual parameters like color and line style for CSOs, while the `CSOManager` module organizes CSOs and CSOGroups within a network.

By using these modules, we can effectively work with CSOs in our workspace, allowing us to draw single lines, for example, to measure distances on images.

![DistanceLine](/images/tutorials/dataobjects/contours/Ex6_2.png "DistanceLine")

Next, we want to add a label to the distance line showing the distance between the two points of our measurement. To achieve this, we'll use the `CSOLabelRenderer` module. Begin by adding a `SoGroup` and connecting both the `CSOLabelRenderer` and the `SoCSODistanceLineEditor` to the `SoGroup`. After moving the label with mouse, the *name* will appear above the line as illustrated below. 

Adding the CSOLabelRenderer, the ID of the CSO is shown next to the measurement for all previously created CSOs. All newly created CSOs will also show the ID

![CSOLabelRenderer](/images/tutorials/dataobjects/contours/Ex6_14.png "CSOLabelRenderer")

The `CSOLabelRenderer` module is responsible for rendering labels for CSOs in the medical imaging context. These labels can be configured using Python scripting.

To ensure synchronization between modules and specify the active editor for creating *distanceLine* CSOs, we need to set the same *Extension Id* in both the `SoCSODistanceLineEditor` and `SoView2DCSOExtensibleEditor` modules. In the `SoView2DCSOExtensibleEditor` module, navigate to the *General* tab and locate the *Creator Extension Id* field. Here, input the same *Extension Id* used in the `SoCSODistanceLineEditor` module. This ensures proper coordination and enables the creation of new *distanceline* CSOs using the designated editor.

![Setting Extension Id in SoView2DCSOExtensibleEditor](/images/tutorials/dataobjects/contours/Example6_5.png "Setting Extension Id in SoView2DCSOExtensibleEditor")

When connected to a `SoView2DCSOExtensibleEditor`, the `CSOLabelRenderer` module allows access to the currently rendered CSO. Python scripting is used to configure the labels and to define the properties of the label displayed for each CSO in the viewer. *labelString* is set to the unique ID of each CSO, while *labelName* combines the word *name* with the label assigned to the CSO. *deviceOffsetX* and *deviceOffsetY* determine the label's position relative to the CSO, both set to 0 for direct overlay. The labeling displaying the number 1 represent a default label because no specific name is provided for the CSO.

Replace the default *Label Code* with the following script:

{{< highlight filename="" >}}
```Python
if cso.getSubType() == 'distanceLine':
    labelString = 'Length: ' + str(cso.getLength())
    labelName = 'Distance '
else:
    labelString = ''
    labelName = ''
labelName += str(cso.getId())
labelCaption = labelName + ":  "

```
{{</highlight>}}

This script will ensure that the label displays the length of the line for *distanceLine* CSOs and remains empty for other CSO types.

![Labeled DistanceLine in View2D](/images/tutorials/dataobjects/contours/Ex6_11.png "Labeled DistanceLine in View2D")

In the `CSOLabelRenderer` panel, head to the *Options* tab. Here, you can fine-tune various settings to enhance the appearance of CSO labels. Set the *Label Border Margin X* to *5* to create a margin around selected CSOs. Increase the *Font Size* to *15* for larger and more readable text. Additionally, adjust the *Min Connecting Line Length* to *15* to specify a minimum distance for drawing connecting lines, maintaining a clean and organized layout. 

![CSOLabelRendering Options](/images/tutorials/dataobjects/contours/Ex6_6.png "CSOLabelRendering Options")

Now, let's proceed with another type of CSO and follow similar steps. Add the `SoCSORectangleEditor` module to your workspace and connect it to the `SoGroup` module.

![SoCSORectangleEditor](/images/tutorials/dataobjects/contours/Ex6_7.png "SoCSORectangleEditor")

Ensure to update the *Creator Extension Id* field in the `SoView2DCSOExtensibleEditor` module with the *Extension Id* of the `SoCSORectangleEditor` module.

![SoCSORectangleEditor & SoView2DCSOExtensibleEditor ](/images/tutorials/dataobjects/contours/Ex6_8.png "SoCSORectangleEditor & SoView2DCSOExtensibleEditor")

Open the `CSOLabelRenderer` panel and add similar script as for the *distanceLine* subtype, but include *Area* calculation as well, since we are dealing with a rectangle.

{{< highlight filename="" >}}
```Python
...
elif cso.getSubType() == 'rectangle':
    labelString = str('Length: ') + str(cso.getLength()) + '\n'
    labelString += str('Area: ') + str(cso.getArea()) + '\n'
    labelName = 'Rectangle '
...
```
{{</highlight>}}

![Labeled Rectangle in View2D](/images/tutorials/dataobjects/contours/Ex6_9.png "Labeled Rectangle in View2D")

{{<alert class="info" caption="Extra Infos">}}

The *Length* attribute in the context of rectangles represents the perimeter of the rectangle, calculated as *2a + 2b*, where *a* and *b* are the lengths of the two sides of the rectangle.

{{</alert>}}

Connect the `CSOInfo` module to the `CSOManager` module in your network. Then, navigate to the *Geometry* tab to access detailed information about the width (*PCA X EXT*) and height (*PCA Y EXT*) of the rectangles. 

![CSOInfo](/images/tutorials/dataobjects/contours/Ex6_10.png "CSOInfo")


To define label placement, connect a `CSOLabelPlacementLocal` module to your `CSOLaberRenderer`. This offers three positioning options: *Seed Point*, where labels align with the right-most seed point; *Path Point*, aligning with the right-most path point; or *Seed or Path Point*, which considers both for optimal placement. 

![CSOLabelPlacementLocal](/images/tutorials/dataobjects/contours/Ex6_13.png "CSOLabelPlacementLocal")

{{<alert class="info" caption="Extra Infos">}}

When working with an ellipse, the *length* means the perimeter around its curved edge, not its width or height. Unlike a rectangle, an ellipse doesn't have sharp corners, so its *length* is the total distance around its outer curve. You calculate it by adding twice the length of its longer side (called the major axis, represented by *a*) and twice the length of its shorter side (called the minor axis, represented by *b*), often denoted as *2πa + 2πb*. 

{{</alert>}}

## Summary
* Labels can be added to contours using the `CSOLabelRenderer` module. 
* Python scripting is used within the `CSOLabelRenderer` module to customize label content based on CSO types.
* Visiual properties can be adjusted within the `CSOLabelRenderer` and the `SoCSOVisualizationSettings` modules to improve label visibility and appearance. 
* `SoView2DCSOExtensibleEditor` and `SoCSODistanceLineEditor` are interduced for managing and interacting with CSOs. 
* Label placement strategies for CSOs can be defined using the `CSOLabelPlacementLocal` module.

{{< networkfile "examples/data_objects/contours/example6/ContourExample6.mlab" >}} 