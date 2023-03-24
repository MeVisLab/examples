---
title: "Example 1.2: DICOM Coordinate Systems"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 365
tags: ["Beginner", "Tutorial",  "Data Import", "DICOM", "Coordinate Systems"]
menu: 
  main:
    identifier: "coordinatesystems2"
    title: "The different coordinate systems in DICOM."
    weight: 365
    parent: "data_import"
---

# Example 1.2: DICOM Coordinate Systems
## General
Coordinate systems in [DICOM](https://en.wikipedia.org/wiki/DICOM) are basically the same as world coordinates in MeVisLab (except for the 0.5 voxel offset).
World coordinates also refer to the patient axes. They are:
* Based on the patient's main body axes (transverse, coronal, sagittal)
* Measured as 1 coordinate unit = 1 millimeter
* Right-handed
* Not standardized regarding their origin

![World Coordinates in Context of the Human Body](/images/tutorials/visualization/V2_00.png "World Coordinates in Context of the Human Body")

The DICOM (Digital Imaging and Communications in Medicine) standard defines a data format that groups information into data sets. This way, the image data is always kept together with all meta information like patient ID, study time, series time, acquisition data etc. The image slice is represented by another tag with pixel information.

DICOM tags have unique numbers, encoded as two 16 bit numbers, usually shown in hexadecimal notation as two four-digit numbers (xxxx,xxxx). These numbers are the data group number and the data element number.

{{<alert class="info" caption="Info">}}
Although DICOM is a standard, often the data that is received / recorded does not follow the standard. Wrongly used tags or missing mandatory tags may cause problems in data processing.
{{</alert>}}

Some typical modules for DICOM handling:
* `DirectDicomImport` is a module for DICOM import that generates 3D or 4D images (as ML images) from a list of DICOM files which can directly be used by other modules. It has a lot of options to control the import process, which can, e.g., determine which slices are combined into an image stack.
* `DicomImport` is a new module for DICOM import. The new implementation does not yet provide all known functionalities from `DirectDicomImport`, most of them will be added in future releases. Its main advantage is that the import process is faster and happens asynchronously.
* You can view the the DICOM tags of a DICOM image or a processed ML image with the module `DicomTagBrowser`.
* You can view and cut out frame-specific tags with the module `DicomFrameSelect`.
* You can modify DICOM tags with the module `DicomTagModify`.
* You can also create a new DICOM header for an image file with the `ImageSave` module, tab Options, Save DICOM header file only.
* Saving of loaded DICOM data to the filesystem or sending to a PACS (Picture Archiving and Communication System) is possible with the `DicomTool` macro module.
* Basic support for querying and receiving DICOM data from a PACS is available via the `DicomQuery` and `DicomReceiver` modules.

{{<alert class="info" caption="Info">}}
For handling and manipulating DICOM data in C++, the DICOM toolkit [DCMTK](https://dicom.offis.de/dcmtk.php.en) (DICOM@offis) is recommended. Parts of this toolkit are also used in MeVisLab.

Another option for Python is [pydicom](https://pydicom.github.io/).
{{</alert>}}

## Orthogonal views
The module `OrthoView2D` provides a 2D view displaying the input image in three orthogonal viewing directions. By default, the view is configured as *Cube* where the transverse view is placed in the top right segment, sagittal in bottom left and coronal in bottom right segment. Use the left mouse button to set a position in the data set. This position will be displayed in all available views and is available as field *worldPosition*. 

![OrthoView2D](/images/tutorials/basicmechanics/OrthoView2D.png "OrthoView2D")

As already learned in the previous example [1.1: MeVisLab Coordinate Systems](/tutorials/basicmechanisms/coordinatesystems/coordinatesystems), world and voxel positions are based on different coordinate systems. Selecting the top left corner of any of your views will not show a world position of 0, 0, 0. You can move the mouse cursor to the voxel position 0, 0, 0 as seen in the image information of the viewers in brackets *(x, y, z)*. The field *worldPosition* then shows the location of the image in world coordinate system (see `Info` module).

![OrthoView2D Voxel- and World Position](/images/tutorials/basicmechanics/OrthoView2D_WorldPosition.png "OrthoView2D Voxel- and World Position")

Another option is to use the module `OrthoReformat3` which transforms the input image (by rotating and/or flipping) into the three main views commonly used: 
* Output 0: Sagittal view
* Output 1: Coronal view
* Output 2: Transverse view

![OrthoReformat3](/images/tutorials/basicmechanics/OrthoReformat3.png "OrthoReformat3")

The general `View2D` always uses the original view from the image data without reconstructing another view. In case of *ProbandT1*, this is the sagittal view.
