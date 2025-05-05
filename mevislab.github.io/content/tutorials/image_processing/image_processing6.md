---
title: "Example 6: DICOM RT Visualization in MeVisLab – RTSTRUCT and RTDOSE Workflow"
date: 2025-05-05
status: "OK"
draft: false
weight: 630
tags: ["Advanced", "Tutorial", "Image Processing", "3D", "Clip Planes"]
menu: 
  main:
    identifier: "imageprocessing6"
    title: "In this example, show some options for integrating clip planes into your 3D views."
    weight: 630
    parent: "imageprocessing"
---

# Example 6: DICOM RT Visualization in MeVisLab – RTSTRUCT and RTDOSE Workflow

## Abstract
This tutorial explains how to load and visualize DICOM RT data in MeVisLab step by step. You will learn how to:
* Load CT and RTSTRUCT data. 
* Visualize RTSTRUCTs as colored CSOs.
* Show labels next to each RTSTRUCT contour.
 We use the `ExtractRTStruct` module and explain each step in a simple way with screenshots. 


## Introduction
In this example, we are using the `SoGVRDrawOnPlane` module to define the currently visible slice from a 2D view as a clip plane in 3D.
DICOM RT files are essential in radiotherapy planning. They include: 
* **RTSTRUCT**: Defines contours of tumors and organs.
* **RTDOSE**: Shows planned 3D dose distribution. 
* **RTPLAN**: Contains treatment plan details like beams and dose settings.
Together, they ensure accurate and safe radiotherapy delivery.


## Step very important to do 

 Download the "DICOM patient export ZIP" from: 

https://medicalaffairs.varian.com/headandneckbilat-imrtsx2

(*Create new folder named `DICOM_from_Varex` ➤ Copy the ZIP file into this folder*).
We will use it in this tutorial. 

Now,


Load DICOM CT and RT data 
(*Add `DicomImport` ➤ `Open it`➤  ` Browse to "DICOM_from_Varex`➤ Click `Import`➤ then as shown in the figure 1*).


![panel DicomImport](/images/tutorials/image_processing/DicomImport.png "panel DicomImport")




**Visualize RTSTRUCTs as colored CSOs:**


Now we need the following modulus, import them then connect them as showed in figure :
 (`DicomImportExtraOutput`, `ExtractRTStruct`,` CSOLabelRenderer `,`SoView2DCSOExtensibleEdito `, `View2D` ).
Important information about the modulus: 
* **DicomImportExtraOutput**


Selects one image (like CT or RTSTRUCT) from the loaded DICOM data.
* **ExtractRTStruct**


Extracts contours (structures) from RTSTRUCT files as CSOs (Contour Segmentation Objects).
* **CSOLabelRenderer**


Shows the names (labels) next to each contour in the image.
* **SoView2DCSOExtensibleEditor**


Allows you to view and interact with the contours in a 2D image viewer.
* **View2D**


Displays 2D medical images (like CT scans) with overlays such as contours and dose.

![Connection and the output of View2D](/images/tutorials/image_processing/ConnectionandtheoutputofView2D.png "Connection and the output of View2D")


👉As we can see here, there are no contours displayed in the image yet, so we need to add them:


From `DicomImportExtraOutput` change using the arrow to 2/4 to show the contour as it show in the figure:

![panel DicomImportExtraOutput to show the contourD](/images/tutorials/image_processing/panelDicomImportExtraOutputtoshowthecontour.png "panel DicomImportExtraOutput to show the contour")


Now open the View2D panel, its will show the contour with numbers as it’s shown in the below figure :

![panel of View2D with contouring and numbers](/images/tutorials/image_processing/panelofView2Dwithcontouringandnumbers.png "panel of View2D with contouring and numbers")


**Show labels next to each RTSTRUCT contour:**

Open `CSOLabelRenderer panel`, its will appear in the main **(Label Code)**, we will add to it this line   
{ `labelString = cso.getGroupAt(0).getLabel`() }, then press apply as shown in the figure:

![panel CSOLabelRenderer to name the contour](/images/tutorials/image_processing/panelCSOLabelRenderertonamethecontour..png "panel CSOLabelRenderer to name the contour")


![Panel View2D after named the contour](/images/tutorials/image_processing/PanelView2Dafternamedthecontour.png "Panel View2D after named the contour")


Now Add SoExaminerViewer and SoCSO3DRenderer as it shown in the below figure to see the 3D image: 

![Output of the SoExaminerViewer](/images/tutorials/image_processing/OutputoftheSoExaminerViewer.png "Output of the SoExaminerViewer")


**Important information:**


* **SoExaminerViewer**

Shows 3D medical data (`rotate, zoom, and pan`).

* **SoCSO3DRenderer**
Displays CSO contours in 3D view.

Visualizing RTDOSE as a Color Overlay Using LUT
Add to tour network ( `DicomImportExtraOutput , Soview2DOverlay , SoLUTEditor , Min max scan , Sogroup , Histogram` ) as shown in figure . 


* **DicomImportExtraOutput**

Adds extra data during DICOM import.
* **Soview2DOverlay**

Displays 2D overlays on images.
* **SoLUTEditor**

Edits image color mapping (LUT).
* **Min max scan**

 Finds image intensity range.
* **Sogroup**

Groups visual elements together.

* **Histogram**

Displays dose distribution for LUT adjustment.

![Visualizing RTDOSE as a Color Overlay Using LUT](/images/tutorials/image_processing/Visualizing.png "Visualizing RTDOSE as a Color Overlay Using LUT")

Then change in the DicomImportExtaOutput1 to 4/4 as shown in the below figure .

![Panel DicomImportExtaOutput1](/images/tutorials/image_processing/PanelDicomImportExtaOutput1.png "Panel DicomImportExtaOutput1")


Update the histogram by press on refresh bottom: 
![Update Histogram](/images/tutorials/image_processing/histo.png "Update Histogram")


Now, as shown in figure, do these steps :

(`open SoLUTEdtitor ➤ Range ➤ Update Range From Histogram `)

![LUT Editor SoLUTEditor(Range).](/images/tutorials/image_processing/LUT.png "LUT Editor SoLUTEditor(Range).")


Then in the same panel from (`Editor ➤ change the color of the values`).


![LUT Editor SoLUTEditor( Editor).](/images/tutorials/image_processing/LUTEditor.png "LUT Editor SoLUTEditor( Editor).")


Finally when you press on View2D it will show the following: 

![Panel View2D Panel (Visualizing RTDOSE as a Color Overlay Using LUT).](/images/tutorials/image_processing/PanelView2DPanel.png "Panel View2D Panel (Visualizing RTDOSE as a Color Overlay Using LUT).")

## Summary

* **Load DICOM Data:**

 Import CT and RTSTRUCT files using DicomImport.
* **Visualize RTSTRUCTs:**

 Display contours as colored CSOs with ExtractRTStruct and CSOLabelRenderer.
* **Add Labels:**

 Show contour labels using CSOLabelRenderer.
* **View in 2D/3D:**

 Use View2D for 2D and SoExaminerViewer for 3D visualization.
* **Visualize RTDOSE:**

 Apply color overlay for dose distribution with SoLUTEditor and adjust using the histogram.


{{< networkfile "/examples/image_processing/example6/DICOMRT.mlab" >}}

