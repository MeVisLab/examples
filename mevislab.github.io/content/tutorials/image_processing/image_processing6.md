---
title: "Example 6: DICOM RT Visualization in MeVisLab – RTSTRUCT and RTDOSE Workflow"
date: 2025-05-05
status: "OK"
draft: false
weight: 630
tags: ["Advanced", "Tutorial", "Image Processing", "DICOM", "RTSTRUCT"]
menu: 
  main:
    identifier: "imageprocessing6"
    title: "Step-by-Step Guide to Loading and Visualizing DICOM RT Data (RTSTRUCT & RTDOSE) in MeVisLab."
    weight: 630
    parent: "imageprocessing"
---

# Example 6: DICOM RT Visualization in MeVisLab – RTSTRUCT and RTDOSE Workflow

## Introduction
This tutorial explains how to load and visualize DICOM RT data in MeVisLab step by step. You will learn how to:
* Load CT and RTSTRUCT data.
* Visualize RTSTRUCTs as colored CSOs.
* Show labels next to each RTSTRUCT contour.

We use the `ExtractRTStruct` module and explain each step in a simple way, with supporting screenshots.

`DICOM RT (Radiotherapy)` files are essential in radiotherapy treatment planning. They include:
* **RTSTRUCT**: Defines contours of tumors and organs.
* **RTDOSE**: Shows planned 3D dose distribution. 
* **RTPLAN**: Contains treatment plan details like beams and dose settings.
Together, they ensure accurate and safe radiotherapy delivery.s


## Prepare your network
So we need in first to download the "DICOM patient export ZIP" it contains the CT, RTSTRUCT, and RTDOSE files needed for this tutorial to work correctly in MeVisLab. from:  

https://medicalaffairs.varian.com/headandneckbilat-imrtsx2

(*Create new folder named `DICOM_from_Varian ` ➤ Copy the ZIP file into this folder*).

We will use it in this tutorial. 

Now,
 Import DicomImport 

![DicomImport](/images/tutorials/image_processing/Dico.png "DicomImport")
Then click Browse and select the new folder named `DICOM_from_Varian` where you copied the ZIP file earlier , then press Import . you can see it in the below figure:
![Importing DICOM RT Data from the DICOM_from_Varian Folder](/images/tutorials/image_processing/Varian.png "Importing DICOM RT Data from the DICOM_from_Varian Folder")
Now import the `View2D` module and connect it to `DicomImport`. 

As shown in the Data Tree (middle pane), the imported DICOM RT structure includes:
* **RTPLAN** \<no image data\>  the treatment plan metadata.

* **RTSTRUCT** \<no image data\> contours (e.g., organs or tumors).

* **CT 512*512*272*1** – the CT scan volume, with dimensions.

* **RTDOSE 199*115*147*1** – the 3D dose distribution data.

And you will see :

* **eByLuKOZoWxBUrIW** – An anonymized Patient ID

* **0000-00-00** – Missing or anonymized Birth/Study Date

👉 After connecting, click on each of these items to visualize the corresponding data in the viewer, as shown in the figures below.

![RTPLAN View2D](/images/tutorials/image_processing/RTPLAN.png "RTPLAN View2D")
![RTSTRUCT View2D](/images/tutorials/image_processing/RTSTRUCT.png "RTSTRUCT View2D")

![CT View2D](/images/tutorials/image_processing/ctct.png "CT View2D")
![RTDOSE View2D](/images/tutorials/image_processing/RTDOSE.png "RTDOSE View2D")

We select the CT 512×512×272×1 because it’s the foundation for viewing and aligning all other radiotherapy data.


We now want to view the CT images and the RTSTRUCT files together. The module `DicomImport` only allows to select one single object. In order to select more than one object, we use a `DicomImportExtraOutput` module. Select the CT series in the `DicomImport` module and the RTSTRUCT in the `DicomImportExtraOutput` module.

You have to select the right index for the RTSTRUCT. In our example it is index 2.
Now add `DicomImportExtraOutput`module as showen in the below figure :

![Selecting CT and RTSTRUCT in DicomImport](/images/tutorials/image_processing/SelectingC.png "Selecting CT and RTSTRUCT in DicomImport")


### **Visualize RTSTRUCTs as colored CSOs:**

Now we need  `ExtractRTStruct`module to converts RTSTRUCT data into CSOs (Contour Segmentation Objects). CSOs allow MeVisLab to display and interact with the contours on the CT scan.

Then coonect it with the `DicomImportExtraOutput` as shown in the figure :

![ExtractRTStruct vonverter](/images/tutorials/image_processing/converter.png "ExtractRTStruct converter")


Add `SoView2DCSOExtensibleEdito ` to enable visualization and interaction with the CSOs in the 2D viewer, allowing you to edit and work with the contours directly. Connect it with `View2D`D and `ExtractRTStruct`, as shown, where `View2D` displays the CT scan with the contours.

![Connecting SoView2DCSOExtensibleEditor](/images/tutorials/image_processing/cotour.png "Connecting SoView2DCSOExtensibleEditor")

There are no names for the contours by default, so we need the `CSOLabelRenderer` module to add labels (e.g., 'Bladder', 'Prostate') next to each contour, helping to clearly identify the anatomy. The figure below shows that :

![CSOLabelRenderer](/images/tutorials/image_processing/CSOLabelRenderer.png " CSOLabelRenderer")

As you can see, the contours are labeled with numbers, so we need to display proper names. To do this, open the `CSOLabelRenderer` panel — it will display the panel shown below.

 
![CSOLabelRenderer panel](/images/tutorials/image_processing/CSOLabelRendererpanel.png "CSOLabelRenderer panel")

Now , add this line to make the numbers names for the contour ?
labelString = cso.getGroupAt(0).getLabel() 
then pess apply : 

![Edited CSOLabelRenderer Panel](/images/tutorials/image_processing/contournamed.png " Edited CSOLabelRenderer Panel")


### **3D Visualization of Contours Using SoExaminerViewer**

Now, to view the contours in 3D, follow these steps:

Add the `SoCSO3DRenderer` module and connect it to the `ExtractRTStruc`t module.
(The `SoCSO3DRenderer` will render the contours (CSOs) in the 3D space.)

Add the `SoExaminerViewer` module and connect it to the `SoCSO3DRenderer` module.
( The `SoExaminerViewer` will allow you to view the 3D contours. You can rotate, zoom, and move around the 3D image.)
The following figure is the network and the result : 

![3D Visualization of Contours Using SoExaminerViewe](/images/tutorials/image_processing/3D.png "3D Visualization of Contours Using SoExaminerViewe")



### **Visualizing RTDOSE as a Color Overlay Using LUT**

Now we need to add another `DicomImportExtraOutput` module to import multiple DICOM objects ,You have to select the right index for the  example it is index 4 thats mean RTDOSE 199*115*147*1 . Add `MinMaxScan`module to scan the input image and updates the minimum and maximum values of the output image  , and connect it with the `DicomImportExtraOutput` 
![Importing RTDOSE Data and Applying MinMaxScan for Image Normalization](/images/tutorials/image_processing/minmaxscan.png "Importing RTDOSE Data and Applying MinMaxScan for Image Normalization")

Add ` Histogram`  module to calculate the image's intensity distribution, and connect it with `MinMaxScan` .

The `Histogram` module computes the image's intensity distribution, and is connected to the `SoLUTEditor` to modify the lookup table (LUT). The LUT is then passed to the `SoGroup`, which is connected to the `SoView2DOverlay` to blend the 2D image overlay in a 2D viewer. The `SoLUTEditor` allows interactive editing of the LUT, while `SoView2DOverlay` facilitates overlaying the modified image in a 2D scene. Note that `SoView2DOverlay` is for 2D blending, and `GVROrthoOverlay` should be used for OrthoView2D.
 The below figure is the connnection of the network :

![Workflow for Intensity Distribution and 2D Image Overlay using LUT Editing"](/images/tutorials/image_processing/net.png "Workflow for Intensity Distribution and 2D Image Overlay using LUT Editing")


Now we should update the `Histogram` by pressing the update button on it.


![Update Histogram](/images/tutorials/image_processing/histo.png " Update Histogram")

Sure! Here's a polished and clear version of that instruction:

Now Open `SoLUTEditor`, go to ➤ *Range* ➤ *Update Range From Histogram* to apply the histogram values, as shown in the figure :

![SoLUTEditor Panel](/images/tutorials/image_processing/solut.png "SoLUTEditor Panel")

Then in the same panel from (Editor ➤ change the color of the values) , as shown in the figure : 


![SoLUTEditor Panel Editior](/images/tutorials/image_processing/editior.png " SoLUTEditor Panel Editior")


Finally when you press on View2D it will show the following: 

![Visualizing RTDOSE as a Color Overlay Using LUT](/images/tutorials/image_processing/2df.png "Visualizing RTDOSE as a Color Overlay Using LUT")

Got it! Here's the summary rewritten using bullet points instead of full sentences (points, not narrative):

---

## **Summary**

* Load DICOM data using `DicomImport` (CT and RTSTRUCT).
* Visualize RTSTRUCTs with `ExtractRTStruct` and `CSOLabelRenderer`.
* Display contour labels using `CSOLabelRenderer`.
* View images in 2D (`View2D`) and 3D (`SoExaminerViewer`).
* Visualize RTDOSE as a color overlay using `SoLUTEditor`.
* Adjust dose intensity with `Histogram` and `MinMaxScan`.



{{< networkfile "/examples/image_processing/example6/DICOMRT.mlab" >}}