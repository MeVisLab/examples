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
This tutorial explains how to load and visualize DICOM RT (Radiotherapy) data in MeVisLab. You will learn how to:
* Load CT and related RTSTRUCT data.
* Visualize RTSTRUCTs as colored CSOs.
* Show labels next to each RTSTRUCT contour.
* Visualize RTDOSE as a semi-transparent colored overlay.

*DICOM RT* files are essential in radiotherapy treatment planning.

They include:
* **RT Structure Set**, containing information related to patient anatomy, for example structures, markers, and isocenters. These entities are typically identified on devices such as CT scanners, physical or virtual simulation workstations, or treatment planning systems.
* **RT Plan**, containing geometric and dosimetric data specifying a course of external beam and/or brachytherapy treatment, for example beam angles, collimator openings, beam modifiers, and brachytherapy channel and source specifications. The RT Plan entity may be created by a simulation workstation, and subsequently enriched by a treatment planning system before being passed on to a record and verify system or treatment device. An instance of the RT Plan object usually references an RT Structure Set instance to define a coordinate system and set of patient structures.
* **RT Dose**, containing dose data generated by a treatment planning system in one or more of several formats: three-dimensional dose data, isodose curves, DVHs, or dose points.

Additional objects not used in this tutorial are:
* **RT Image**, specifying radiotherapy images which have been obtained on a conical imaging geometry, such as those found on conventional simulators and portal imaging devices. It can also be used for calculated images using the same geometry, such as digitally reconstructed radiographs (DRRs).
* **RT Beams Treatment Record**, **RT Brachy Treatment Record**, and **RT Treatment Summary Record**, containing data obtained from actual radiotherapy treatments. These objects are the historical record of treatment, and are linked with the other „planning” objects to form a complete picture of the treatment.

## Precondition
If you do not have DICOM RT data, you can download an example dataset at:
https://medicalaffairs.varian.com/headandneckbilat-imrtsx2 

{{<alert class="warning" caption="Attention">}}
This data is FOR EDUCATIONAL AND SCIENTIFIC EXCHANGE ONLY – NOT FOR SALES OR PROMOTIONAL USE.
{{</alert>}}

Extract the ZIP file into a new folder named *DICOM_FILES*.

## Prepare your network

Add the module `DicomImport` to your workspace. 

Then click {{< mousebutton "left" >}} Browse and select the new folder named *DICOM_FILES* where you copied the content of the ZIP file earlier. Click Import {{< mousebutton "left" >}}. You can see the result after import below:

![DICOM RT Data in DicomImport module](/images/tutorials/image_processing/Example6_1.png "DICOM RT Data in DicomImport module")

The dataset contains an anonymized patient with four series:
   * RTPLAN \<no image data\>
   * RTSTRUCT \<no image data\>
   * CT 512×512×272×1
   * RTDOSE 199×115×147×1

In order to see the images, add a `View2D` module and connect it to the `DicomImport` module.

The *RTPLAN* and *RTSTRUCT* files do not contain pixel data. Therefore the `DicomImport` module informs that there is no image data available. The *CT* series contains the original CT data and the *RTDOSE* series contains a mask providing three-dimensional dose data.

{{< imagegallery 4 "/images/tutorials/image_processing/" "RTPLAN" "RTSTRUCT" "CT512" "RTDOSE">}}

Select the *CT 512×512×272×1* series.

We now want to view the CT images and the *RTSTRUCT* data together. The module `DicomImport` only allows to select one single object. In order to select more than one object, we use a `DicomImportExtraOutput` module. Select the CT series in the `DicomImport` module and the *RTSTRUCT* in the `DicomImportExtraOutput` module.

You have to select the correct index for the *RTSTRUCT*. In our example it is index 2.

![RTSTRUCT in DicomImportExtraOutput](/images/tutorials/image_processing/Example6_2.png "RTSTRUCT in DicomImportExtraOutput")

### Visualize RTSTRUCTs as colored CSOs

Add an `ExtractRTStruct` module to the `DicomImportExtraOutput` to convert *RTSTRUCT* data into MeVisLab contours (CSOs). CSOs allow to visualize the contours on the CT scan and to interact with them in MeVisLab.

A preview of the resulting CSOs can be seen in the *Output Inspector*.

![ExtractRTStruct in Output Inspector](/images/tutorials/image_processing/Example6_3.png "ExtractRTStruct in Output Inspector")

Add a `SoView2DCSOExtensibleEditor` module to enable visualization and interaction with the CSOs in the 2D viewer.

![SoView2DCSOExtensibleEditor](/images/tutorials/image_processing/Example6_4.png "SoView2DCSOExtensibleEditor")

We want to display the names for the contours available in the *RTSTRUCT* file to identify the segmented structure. Use the `CSOLabelRenderer` module to show labels (e.g., 'Bladder', 'Prostate') next to each contour.

![CSOLabelRenderer](/images/tutorials/image_processing/Example6_5.png " CSOLabelRenderer")

By default, the ID of the contours is rendered. Open the panel of the `CSOLabelRenderer` and change the *labelString* parameter as seen below.
 
![CSOLabelRenderer labelString](/images/tutorials/image_processing/Example6_6.png "CSOLabelRenderer labelString")

{{< highlight >}}
```Python
labelString = cso.getGroupAt(0).getLabel()
```
{{</highlight>}}

Then press apply {{< mousebutton "left" >}}. The name of the structure is defined in the group of each CSO. We now show the label of the group next to the contour. Add a `CSOLabelPlacementGlobal` module to define a better readable location of these labels.

The module `CSOLabelPlacementGlobal` implements an automatic label placement strategy that considers all CSOs on a slice.

![Edited CSOLabelRenderer Panel](/images/tutorials/image_processing/Example6_7.png " Edited CSOLabelRenderer Panel")

### 3D Visualization of Contours Using `SoExaminerViewer`
The contours can also be shown in 3D.

Add a `SoCSO3DRenderer` and a `SoExaminerViewer` module and connect them to the `ExtractRTStruct` module. The `SoCSO3DRenderer` will render the contours (CSOs) into the `SoExaminerViewer`.

![CSOs in 3D](/images/tutorials/image_processing/Example6_8.png "CSOs in 3D")

### Visualizing RTDOSE as a colored overlay
We now want to show the *RTDOSE* data as provided for the patient as a semi-transparent, colored overlay.

Add another `DicomImportExtraOutput` module to get the *RTDOSE* object. Again, select the correct index. In this case, we select index 4.

Add a `MinMaxScan` module to scan the input image and calculate the minimum and maximum values of the image. Connect it with the `DicomImportExtraOutput` module.

![MinMaxScan](/images/tutorials/image_processing/Example6_9.png "MinMaxScan")

Add a `Histogram` and a `SoLUTEditor` module to calculate the image's intensity distribution and define a colored lookup table for the overlay.

Change update mode of the `Histogram` module to *Auto Update*.

Open the panel of the `SoLUTEditor` module and go to tab *Range*. Click  {{< mousebutton "left" >}} *Update Range From Histogram* to apply the histogram values for the *Range* of the lookup table.

![Lookup table and Histogram](/images/tutorials/image_processing/Example6_10.png "Lookup table and Histogram")

On tab *Editor*, define a lookup table as seen below.

![Lookup table](/images/tutorials/image_processing/Example6_11.png "Lookup table")

The lookup table shall be used for showing the RT Dose data as a semi-transparent overlay on the CT image. Add a `SoView2DOverlay` and a `SoGroup` module to your network. Replace the input of the View2D module from the `SoView2DCSOExtensibleEditor` with the `SoGroup`.

![RT Dose data using SoView2DOverlay](/images/tutorials/image_processing/Example6_12.png "RT Dose data using SoView2DOverlay")

If you want to visualize the RT Struct contours together with the RT Dose overlay, connect the `SoView2DCSOExtensibleEditor` module and the `SoGroup` module. 

![RT Dose and RT Struct](/images/tutorials/image_processing/Example6_13.png "RT Dose and RT Struct")

## Summary
* DICOM RT data can be loaded and processed in MeVisLab.
* RT Structure Sets can be converted to MeVisLab contours and visualized using `ExtractRTStruct` and `CSOLabelRenderer` modules
* Anatomical information can be shown using the module `CSOLabelRenderer`.
* RT Dose files can be shown as a semi-transparent colored overlay using `SoView2DOverlay`.

{{< networkfile "/examples/image_processing/example6/DICOMRT.mlab" >}}
