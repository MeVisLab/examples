---
title: "Example 6: DICOM RT Visualization in MeVisLab – RTSTRUCT and RTDOSE Workflow"
date: 2025-05-05
status: "OK"
draft: false
weight: 630
tags: ["Advanced", "Tutorial", "Image Processing", "DICOM", "RTSTRUCT", "RTDOSE", "RTPLAN"]
menu: 
  main:
    identifier: "imageprocessing6"
    title: "Loading and Visualizing DICOM RT Data (RTSTRUCT & RTDOSE) in MeVisLab."
    weight: 630
    parent: "imageprocessing"
---

# Example 6: DICOM RT Visualization in MeVisLab – RTSTRUCT and RTDOSE Workflow

## Introduction
This tutorial explains how to load and visualize DICOM RT data in MeVisLab step by step. You will learn how to:
* Load CT and related RTSTRUCT data.
* Visualize RTSTRUCTs as colored CSOs.
* Visualize RTDOSE as a colored overlay.
* Show labels next to each RTSTRUCT contour.
We use the `ExtractRTStruct`module for this example.

**DICOM RT (Radiotherapy)** files are essential in radiotherapy treatment planning. They include:
* **RTSTRUCT**: Defines contours of tumors and organs.
* **RTDOSE**: Shows planned 3D dose distribution. 
* **RTPLAN**: Contains treatment plan details like beams and dose settings.
Together, they ensure accurate and safe radiotherapy delivery.

## Prepare your network
First, we need to download the ZIP file from:

https://medicalaffairs.varian.com/headandneckbilat-imrtsx2 

It contains the CT, RTSTRUCT, and RTDOSE files needed for this tutorial to work correctly in MeVisLab.

{{<alert class="warning" caption="Attention">}}
This data is FOR EDUCATIONAL AND SCIENTIFIC EXCHANGE ONLY – NOT FOR SALES OR PROMOTIONAL USE.
{{</alert>}}

Create a new folder named *DICOM_FILES*. Extract the ZIP file into this folder.

We will use it in this tutorial. 

Add the module `DicomImport` to your workspace. 

!["DicomImport](/images/tutorials/image_processing/Dicommm.png "DicomImport")

Then click {{< mousebutton "left" >}} Browse and select the new folder named *DICOM_FILES* where you copied the content of the ZIP file earlier. Click Import {{< mousebutton "left" >}}. You can see the result after import in the below figure:

![Importing DICOM RT Data from the DICOM_FILES Folder](/images/tutorials/image_processing/Import.png "Importing DICOM RT Data from the DICOM_FILES Folder")

Now add a `View2D` module and connect it to the `DicomImport` module. 

As shown in the Data Tree (middle pane), the imported DICOM RT structure includes:

* **eByLuKOZoWxBUrIW** – An anonymized Patient ID.
* **0000-00-00** – Missing or anonymized Birth/Study Date.

When you expand the tree view you will see: 

   * **RTPLAN** – Treatment plan metadata (no image).
   * **RTSTRUCT** – Contour data (e.g., organs, tumors; no image).
   * **CT 512×512×272×1** – The full CT scan volume (visible anatomy).
   * **RTDOSE 199×115×147×1** – The 3D dose distribution (dose grid).

After connecting, open the `View2D` and click on each of these items to visualize the corresponding data in the viewer, as shown in the figures below.

{{< imagegallery 4 "/images/tutorials/image_processing/" "RTPLAN" "RTSTRUCT" "CT512" "RTDOSE">}}

Select the CT 512×512×272×1 series.

We now want to view the CT images and the RTSTRUCT data together. The module `DicomImport` only allows to select one single object. In order to select more than one object, we use a `DicomImportExtraOutput` module. Select the CT series in the `DicomImport` module and the RTSTRUCT in the `DicomImportExtraOutput` module.

You have to select the correct index for the RTSTRUCT. In our example it is index 2.

![Selecting CT and RTSTRUCT in DicomImport](/images/tutorials/image_processing/SELECTINGCTRTSTRUCT.png "Selecting CT and RTSTRUCT in DicomImport")

### Visualize RTSTRUCTs as colored CSOs

Now we need an `ExtractRTStruct` module to convert RTSTRUCT data into CSOs (Contour Segmentation Objects). CSOs in MeVisLab allow to visualize the contours on the CT scan and to interact with them.

Then connect it with the `DicomImportExtraOutput` as shown in the figure:

![ExtractRTStruct vonverter](/images/tutorials/image_processing/converter.png "ExtractRTStruct converter")

Add a `SoView2DCSOExtensibleEditor` module to enable visualization and interaction with the CSOs in the 2D viewer. Connect it with a `View2D` module and the `ExtractRTStruct` module. The `View2D` module shows the CT scan with the contours from the *RTSTRUCT* file.

![Connecting SoView2DCSOExtensibleEditor](/images/tutorials/image_processing/cotour.png "Connecting SoView2DCSOExtensibleEditor")

There are no names for the contours shown by default. We want to display the names for the contours available in the *RTSTRUCT* file to identify the segmented structure. Use the `CSOLabelRenderer` module to show labels (e.g., 'Bladder', 'Prostate') next to each contour. The figure below shows that:

![CSOLabelRenderer](/images/tutorials/image_processing/CSOLabelRenderer.png " CSOLabelRenderer")

As you can see, the contours are labeled with numbers. The number is the internal ID of the contour. We want to show the names for the contour to identify the segmented structure. To do this, open the `CSOLabelRenderer` panel.
 
![CSOLabelRenderer panel](/images/tutorials/image_processing/CSOLabelRendererpanel.png "CSOLabelRenderer panel")

Now, add this line to make the numbers names for the contour:
{{< highlight >}}
```Python
labelString = cso.getGroupAt(0).getLabel()
```
{{</highlight>}}

Then press apply. The label of the CSO provides the name of each contour. You can see them next to the contours.

![Edited CSOLabelRenderer Panel](/images/tutorials/image_processing/contournamed.png " Edited CSOLabelRenderer Panel")

{{<alert class="info" caption="Extra Information">}}
You can use a `CSOLabelPlacementLocal` module or a `CSOLabelPlacementGlobal` module to define the locations of these labels.
{{</alert>}}

### 3D Visualization of Contours Using `SoExaminerViewer`

If you want to visualize the contours in 3D, follow these steps:

Add the `SoCSO3DRenderer` module and connect it to the `ExtractRTStruct` module. The `SoCSO3DRenderer` will render the contours (CSOs) in 3D.

Add the `SoExaminerViewer` module and connect it to the `SoCSO3DRenderer` module. The `SoExaminerViewer` will allow you to view the 3D contours. You can rotate, zoom, and move around the 3D image.

The following figure shows the network and the result: 

![3D Visualization of Contours Using SoExaminerViewe](/images/tutorials/image_processing/3D.png "3D Visualization of Contours Using SoExaminerViewe")

### Visualizing RTDOSE as a Color Overlay Using LUT
We now ant to show the *RTDOSE* data as provided for the patient as a semi-transparent overlay.

Now we need to add another `DicomImportExtraOutput` module to import multiple DICOM objects. You have to select the correct index for the example. In this case, we select index 4 for the *RTDOSE* 199*115*147*1 data. Add a `MinMaxScan` module to scan the input image and calculate the minimum and maximum values of the image. Connect it with the `DicomImportExtraOutput` module.

![Importing RTDOSE Data and Applying MinMaxScan for Image Normalization](/images/tutorials/image_processing/minmaxscan.png "Importing RTDOSE Data and Applying MinMaxScan for Image Normalization")

Add a `Histogram` module to calculate the image's intensity distribution, and connect it to the `MinMaxScan` module.

The `Histogram` module computes the image's intensity distribution and is connected to the `SoLUTEditor` module to modify the lookup table (LUT). The LUT is then passed to the `SoGroup` module, which is connected to the `SoView2DOverlay` module to blend the 2D image overlay in a 2D viewer. The `SoLUTEditor` module allows interactive editing of the LUT, while the `SoView2DOverlay` module facilitates overlaying *RTDOSE* in a 2D scene.

{{<alert class="info" caption="Extra Information">}}
Note that the `SoView2DOverlay` module is for 2D blending. The `GVROrthoOverlay` module should be used for `OrthoView2D`.
{{</alert>}}

The below figure shows the connections of the network:

![Workflow for Intensity Distribution and 2D Image Overlay using LUT Editing"](/images/tutorials/image_processing/net.png "Workflow for Intensity Distribution and 2D Image Overlay using LUT Editing")

Now we should update the `Histogram` module by pressing the update button on it.

![Update Histogram](/images/tutorials/image_processing/histo.png " Update Histogram")

Now open `SoLUTEditor` module panel, go to *Range*, *Update Range From Histogram* to apply the histogram values, as shown in the figure:

![SoLUTEditor Panel](/images/tutorials/image_processing/solut.png "SoLUTEditor Panel")

In the same panel, on tab *Editor*, change the colors as shown in the figure: 

![SoLUTEditor Panel Editior](/images/tutorials/image_processing/editior.png " SoLUTEditor Panel Editior")

Finally, when you open the `View2D` panel, it will display a 2D anatomical image with a colored *RTDOSE* overlay, where the dose distribution is visualized using a customized Lookup Table (LUT) that clearly highlights the radiation intensity levels within the body.

![Visualizing RTDOSE as a Color Overlay Using LUT](/images/tutorials/image_processing/2df.png "Visualizing RTDOSE as a Color Overlay Using LUT")

## **Summary**

* Load DICOM RT data including RTDOSE and RTSTRUCT.
* Visualize RTSTRUCTs with `ExtractRTStruct` and `CSOLabelRenderer`.
* Display contour labels using `CSOLabelRenderer`.
* View images in 2D (`View2D`) and 3D (`SoExaminerViewer`).
* Visualize RTDOSE as a color overlay using `SoLUTEditor`.
* Adjust dose intensity with `Histogram` and `MinMaxScan`.

{{< networkfile "/examples/image_processing/example6/DICOMRT.mlab" >}}
