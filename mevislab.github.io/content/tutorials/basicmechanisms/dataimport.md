---
title: "Example 1: Data import in MeVisLab"
date: 2022-06-15T08:54:53+02:00
status: "OK"
draft: false
weight: 360
tags: ["Beginner", "Tutorial",  "Data Import", "DICOM"]
menu: 
  main:
    identifier: "data_import"
    title: "How to import several data formats into MeVisLab like DICOM, Contours, Surface Objects, or 3D Scenes."
    weight: 360
    parent: "basicmechanisms"
---

# Example 1: Data Import in MeVisLab
MeVisLab provides several pre-defined modules to import data for processing in your networks.

{{<alert class="info" caption="Extra Infos">}}
The easiest way to load data in MeVisLab is to drop the file onto the MeVisLab workspace. MeVisLab will try to find a module that is capable of loading your file automatically.
{{</alert>}}

These chapters explain the data formats and modules related to this example:
* [Images](tutorials/basicmechanisms/dataimport#ImageImport)
* [DICOM Data](tutorials/basicmechanisms/dataimport#DICOMImport)
* [Segmentations / 2D Contours](tutorials/basicmechanisms/dataimport#2DContours)
* [3D Data / Meshes](tutorials/basicmechanisms/dataimport#3DMeshes)

Example files and images can be found in your MeVisLab installation directory under Packages > MeVisLab > Resources > DemoData

{{<alert class="info" caption="Extra Infos">}}
Detailed explanations on loading images onto your MeVisLab workspace can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch03.html" "here" >}}
{{</alert>}}

## Images {#ImageImport}
A good option to load images is the `ImageLoad` module.
![ImageLoad Module](images/tutorials/basicmechanics/ImageLoad.png "ImageLoad Module")

The `ImageLoad` module can import the following formats:
* DICOM
* TIFF
* DICOM/TIFF
* RAW
* LUMISYS
* PNM
* Analyze
* PNG
* JPEG
* MLImageFileFormat

Basic information of the imported images are available on the Panel that opens via double-click.

## DICOM Data {#DICOMImport}
{{<alert class="info" caption="Extra Infos">}}
Additional information about **Digital Imaging and Communications in Medicine (DICOM)** can be found at [Wikipedia](https://en.wikipedia.org/wiki/DICOM "DICOM Format")
{{< /alert >}}
Even if the above explained `ImageLoad` is able to import DICOM data, a much better way is to use one of the specialized modules for DICOM images such as `DicomImport`.

The `DicomImport` module allows to define a directory containing DICOM files to import as well as a list of files that can be dropped to the UI and imported. After import, the volumes are shown in a patient tree providing the following patient, study, series, and volume information (depending on the availability in the DICOM file(s)):

* **PATIENT LEVEL** Patient Name (0010,0010) - Patient Birthdate (0010,0030)
  * **STUDY LEVEL** Study Date (0008,0020) - Study Description (0008,1030)
    * **SERIES/VOLUME LEVEL** Modality (0008,0060) - Series Description (0008,103e) - Rows (0028,0010) - Columns (0028,0011) - number of slices in volume - number of timepoints in volume

![DicomImport Module](images/tutorials/basicmechanics/DicomImport.png "DicomImport Module")

### Configuration
The `DicomImport` module generates volumes based on the **Dicom Processor Library (DPL)** that allows to define sorting and partitioning options.

![DicomImport Sort Part Configuration](images/tutorials/basicmechanics/DicomImportSortPart.png "DicomImport Sort Part Configuration")

### DicomTree Information
In order to get all DICOM tags from your currently imported and selected volume, you can connect the `DicomImport` module to a `DicomTagBrowser`.

![DicomTagBrowser Module](images/tutorials/basicmechanics/DicomTagBrowser.png "DicomTagBrowser Module")

In MeVisLab versions later than 4.2.0, the *Output Inspector* provides the option to show the DICOM tags of the currently selected output directly. You do not need to add a separate `DicomTagBrowser` module anymore.

![DICOM Information in Output Inspector](images/tutorials/basicmechanics/OutputInspectorDICOM.png "DICOM Information in Output Inspector")

## Segmentations / 2D Contours {#2DContours}
Two-dimensional contours in MeVisLab are handled via *CSO*s (**C**ontour **S**egmentation **O**bjects).

{{<alert class="info" caption="Extra Infos">}}
Tutorials for CSOs are available [here](../../dataobjects/contours/contour-objects)

Detailed explanations about CSOs can be found {{< docuLinks "/Standard/Documentation/Publish/Overviews/CSOOverview.html" "here" >}}
{{</alert>}}

The CSO library provides data structures and modules for an interactive or automatic generation of contours in voxel images. Furthermore, these contours can be analyzed, maintained, grouped, and converted into a voxel image or a set of markers.

CSOs can be created by the existing `SoCSO*Editor` modules. The following modules are available:
* `SoCSOPointEditor`
* `SoCSOAngleEditor`
* `SoCSOArrowEditor`
* `SoCSODistanceLineEditor`
* `SoCSODistancePolylineEditor`
* `SoCSOEllipseEditor`
* `SoCSORectangleEditor`
* `SoCSOIsoEditor`
* `SoCSOSplineEditor`
* `SoCSOPolygonEditor`
* `SoCSOLiveWireEditor`

For saving and loading existing CSOs, the modules `CSOSave` and `CSOLoad` can be used.

## 3D Data / Meshes {#3DMeshes}
### Winged Edge Mesh (WEM)
Three-dimensional meshes in MeVisLab are handled via *WEM*s (**W**inged **E**dge **M**esh).

The module `WEMLoad` loads different 3D mesh file formats like:
* Object File Format (*.off* *.geom*)
* Wavefront (*.obj*)
* Polygon File Format (*.ply*)
* Standard Tessellation Language (*.stl*)
* VRML (*.wrl*)
* Winged Edge Mesh (*.wem*)

![WEMLoad Module](images/tutorials/basicmechanics/WEMLoad.png "WEMLoad Module")

WEMs can be rendered via Open Inventor by using the modules `SoExaminerViewer` or `SoRenderArea` and `SoCameraInteraction`.

Before visualizing a WEM, it needs to be converted to a scene object via `SoWEMRenderer`.

![SoWEMRenderer Module](images/tutorials/basicmechanics/SoWEMRenderer.png "SoWEMRenderer Module")

{{<alert class="info" caption="Extra Infos">}}
Tutorials for WEMs are available [here](../../dataobjects/surfaces/surfaceobjects).
{{</alert>}}

### Loading Arbitrary 3D Files
The `SoSceneLoader` module is able to load external 3D formats. MeVisLab uses the integrated *assimp* third-party library that is able to import most common 3D file types. The currently integrated *assimp* version can be found {{< docuLinks "/../MeVis/ThirdParty/Documentation/Publish/ThirdPartyReference/index.html" "here" >}}

{{<alert class="info" caption="Extra Infos">}}
Supported file formats of the assimp library are documented on their [website](https://github.com/assimp/assimp/blob/master/doc/Fileformats.md).
{{</alert>}}

![SoSceneLoader Module](images/tutorials/basicmechanics/SoSceneLoader.png "SoSceneLoader Module")

The {{< docuLinks "/../MeVisLab/Standard/Documentation/Publish/ModuleReference/SoSceneLoader.html" "SoSceneLoader" >}} module generates a 3D scene from your loaded files that can be rendered via {{< docuLinks "/../MeVisLab/Standard/Documentation/Publish/ModuleReference/SoExaminerViewer.html" "SoExaminerViewer" >}} or {{< docuLinks "/../MeVisLab/Standard/Documentation/Publish/ModuleReference/SoRenderArea.html" "SoRenderArea" >}} and {{< docuLinks "/../MeVisLab/Standard/Documentation/Publish/ModuleReference/SoCameraInteraction.html" "SoCameraInteraction" >}}

{{<alert class="info" caption="Extra Infos">}}
Example usage is explained in the tutorials for [Open Inventor](tutorials/openinventor).
{{</alert>}}
