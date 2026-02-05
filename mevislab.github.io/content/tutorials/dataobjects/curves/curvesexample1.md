---
title: "Example 1: Drawing Curves"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 780
tags: ["Beginner", "Tutorial", "Data Objects", "2D", "Curves"]
menu: 
  main:
    identifier: "curvesexample1"
    title: "Draw One or More Curves Into a Diagram"
    weight: 780
    parent: "curves"
---

# Example 1: Drawing Curves

{{< youtube "sj6muyInkRc">}}

## Introduction
In this example, you will draw one or more curves into a diagram and define different styles for the curves.

## Steps to Do

### Develop Your Network
A curve requires x- and y-coordinates to be printed. You can use the `CurveCreator` module as input for these coordinates. The `SoDiagram2D` draws the curves into a `SoRenderArea`. You can also define the style of the curves by using the `StylePalette` module.

Add the modules to your workspace and connect them as seen below.

![Example Network](images/tutorials/dataobjects/curves/example_network.png "Example Network")

### Creating a Curve
Click on the output of the `CurveCreator` module and open the Output Inspector.

![Empty Output Inspector](images/tutorials/dataobjects/curves/OutputInspector_empty.png "Empty Output Inspector")

Double-click {{<mousebutton "left">}} on the `CurveCreator` module and open the Panel.

![CurveCreator Module](images/tutorials/dataobjects/curves/CurveCreatorModule.png "CurveCreator Module")

You can see a large input field <field>Curve Table</field>. Here you can enter the x- and y-values of your curve. The values of the first column will become the x-values and the second column will become the y-series. Comment lines start with a '#' character.

Enter the following into the *Curve Table*:
{{< highlight filename="Curve Table" >}}
```Text
# My first curve
0 0
1 1
2 2
3 3
4 4
5 5
10 10
50 50
```
{{</highlight>}}

Now, your *Output Inspector* shows a yellow line through the previously entered coordinates. Exactly the same curve is shown in the `SoRenderArea`.

![SoRenderArea](images/tutorials/dataobjects/curves/SoRenderArea.png "SoRenderArea")

### Creating Multiple Curves
Now, update the *Curve Table*, so that you are using three columns and click *Update* {{<mousebutton "left">}}:
{{< highlight filename="Curve Table" >}}
```Text
# My first curves
0 0 0
1 1 2
2 2 4
3 3 6
4 4 8
5 5 10
10 10 20
50 50 100
```
{{</highlight>}}

You can see two curves. The second and third columns are printed as separate curves. Both appear yellow. After checking *Split columns into data sets*, you will see one yellow and one red curve.

{{<imagegallery 2 "images/tutorials/dataobjects/curves" "before_split" "after_split">}}

If the flag *Split columns into data sets* is set to *TRUE*, then a table with more than two columns is split into different *CurveData* objects. This gives the user the possibility to assign a different style and title for each series.

### Titles and Styles
Let's do this. Open the panel of the `SoDiagram2D` module and check *Draw legend*. Enter *"Curve1 Curve2"* into the *Title(s)* text box of the `CurveCreator` module and click *Update* {{<mousebutton "left">}}.

![SoRenderArea with Legend](images/tutorials/dataobjects/curves/SoRenderArea2.png "SoRenderArea with Legend")

You can also define a different location of the legend and set font sizes.

Now, open the panel of the `StylePalette` module.

![StylePalette](images/tutorials/dataobjects/curves/StylePalette.png "StylePalette")

The `StylePalette` module allows you to define twelve different styles for curves. Initially, without manual changes, the styles are applied one after the other. The first curve gets style 1, the second curve style 2, and so on.

Open the panel of your `CurveCreator` module again and define *Curve Style(s)* as *"3 6"*. *Update* {{<mousebutton "left">}} your curves.

![StylePalette applied](images/tutorials/dataobjects/curves/StylePalette_applied.png "StylePalette applied")

You now applied the style three for your first curve and style six for the second. This is how you can create twelve different curves with unique appearance.

### Using Multiple Tables for Curve Generation
In addition to adding multiple columns for different y-coordinates, you can also define multiple tables as input, so that you can also have different x-coordinates for multiple curves.

Update the *Curve Table* as defined below and click *Update* {{<mousebutton "left">}}:
{{< highlight filename="Curve Table" >}}
```Text
# My first curves
0 0 0
1 1 2
2 2 4
3 3 6
4 4 8
5 5 10
10 10 20
50 50 100
---
# My third curve
0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
10 100
```
{{</highlight>}}

Also add another title to your curves and define a third style.

![Multiple tables as input](images/tutorials/dataobjects/curves/Multiple_tables.png "Multiple tables as input")

{{<alert class="info" caption="Additional Information">}}
For more complex visualizations, you can also use *Matplotlib*. See examples at [Third-party - Matplotlib](tutorials/thirdparty/matplotlib "Third-party - Matplotlib").
{{</alert>}}

## Summary
* Curves can be created to draw two-dimensional diagrams.
* The `StylePalette` module allows you to define the appearance of a curve.
* Details of the different curves can be visualized by using the `SoDiagram2D` module.

{{<alert class="info" caption="Additional Information">}}
The attached example network shows the curves after clicking *Update* on `CurveCreator` module.
{{</alert>}}

{{< networkfile "examples/data_objects/curves/example1/Curves.mlab" >}}
