---
title: "Example 4: Review - Automated Tests"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Advanced", "Tutorial", "Prototyping", "Automated Tests", "Python"]
menu: 
  main:
    identifier: "summaryexample4"
    title: "Test your Macro Module in MeVisLab. Your requirements are translated into test cases written in Python."
    weight: 820
    parent: "summary"
---
# Example 4: Review - Automated Tests
## Introduction
In the previous chapters you developed a Macro Module with User Interface and Python scripting. In this example you will see how to implement an automated test to verify and validate the Requirements defined in [Overview](/tutorials/summary).

## Steps to do
### Create a test network using your Macro Module
Create a new and empty network and save it as \*.mlab file. Remember the location.

Use Module Search and add your Macro Module developed in previous examples to your Workspace.

![Macro Module](/images/tutorials/summary/Example4_1.png "Macro Module")

You can see that the module does not have any inputs or outputs. You cannot connect it to other modules. For testing purposes it makes sense to provide the viewers and images as outputs so that you can use them for generating screenshots.

Open the \*.script file in MATE as already explained in [Example 3](/tutorials/summary/summary3). In the *Outputs* section, add the following:

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
  Inputs {}
  Outputs {
    Field out2D { internalName = LocalImage.outImage }
    Field out3D { internalName = SoSwitch.self }
    Field outSegmentationMask { internalName = CloseGap.output0 }
  }
  ...
}
```
{{</highlight>}}

![Macro Module with outputs](/images/tutorials/summary/Example4_2.png "Macro Module with outputs")

You can now add a viewer or any other module to your Macro Module and use them for testing. In our example, we add a `CalculateVolume` module to the segmentation mask and a `SoCameraInteraction` with two `OffscreenRenderer` modules to the 3D output. In the end, we need an `ImageCompare` module to compare expected and real image in our test.

![Test Network](/images/tutorials/summary/Example4_3.png "Test Network")

### Create test case
Open MeVisLab TestCaseManager via {{< menuitem "File" "Run TestCaseManager..." >}}. On tab *Test Creation* define a name of your test case, for example *TutorialSummaryTest*. Select Type as *Macros*, define the package and use the same as for your Macro Module, select *Import Network* and Select your saved \*.mlab file from the step above. Click *Create*.

![Test Creation](/images/tutorials/summary/Example4_4.png "Test Creation")

MATE automatically opens the Python file of your test case and it appears in MeVisLab TestCaseManager. 

![Test Creation](/images/tutorials/summary/Example4_5.png "Test Creation")

### Write test functions in Python
#### Preparations
Before writing a test case, we need some helper functions in Python, which we will use in our test cases. The first thing we need is a function to load images.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
from mevis import *
from TestSupport import Base, Fields, Logging, ScreenShot
from TestSupport.Macros import *

path_to_image = "$(DemoDataPath)/BrainMultiModal/ProbandT1.dcm"
marker_location = [-29, -26, 45]
marker_location_new = [-20, -30, 35]
new_color = [0.5, 0.5, 0]

def loadImage(full_path):
  MLAB.log("Setting image path to '" + full_path + "'...")
  ctx.field("TutorialSummary.openFile").value = full_path
```
{{</highlight>}}

We define the path to a file to be loaded. The function *loadImage* sets the *openFile* field of the `TutorialSummary` module.

The arrays for the marker location and color will be used later.

Next we need a function to check if the loaded image available at the first output of our Macro Module (*out2D*) is valid.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
def isImageValid():
  MLAB.log("Checking if image is valid...")
  data_valid = ctx.field("TutorialSummary.out2D").isValid()
  if data_valid:
    return True
  else:
    return False
...
```
{{</highlight>}}

We also need to set a marker in our Macro Module.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
def setMarkerPosition(vector):
  MLAB.log("Setting marker position to [" + str(vector[0]) + "," + str(vector[1]) + "," + str(vector[2]) + "]...")
  ctx.field("TutorialSummary.markerPosition").setValue(vector[0], vector[1], vector[2])
  ctx.field("TutorialSummary.applyMarker").touch()
  MLAB.processEvents()
  while not ctx.field("TutorialSummary.outSegmentationMask").isValid():
    MLAB.msleep(100)
    MLAB.processEvents()
  MLAB.log("Marker position set to '" + str(ctx.field("TutorialSummary.markerPosition").value) + "'...")
...
```
{{</highlight>}}

The *setMarkerPosition* function gets a 3-dimensional vector and sets the *markerPosition* field of our module. Then the *applyMarker* trigger is touched. As the region growing algorithm might need some time to segment, we need to wait until the *outSegmentationMask* output field is valid, means there is a valid segmentation mask at the segmentation mask output of our Macro Module.

Finally, we need to reset the application to its initial state, so that each test case has the initial start conditions of the application. A test case should never depend on another test case so that they all can be executed exclusively.

Example:
Having one test case for the requirement to load images and one for setting the marker depending on the image to be loaded by previous test case, you will never be able to execute the marker test case without executing the load image first.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
def reset():
  MLAB.log("Resetting application...")
  ctx.field("TutorialSummary.resetApplication").touch()
...
```
{{</highlight>}}

For a reset, we just touch the *resetApplication* field of our Macro Module `TutorialSummary`.

#### Requirement 1: The application shall be able to load DICOM data
The first requirement we want to test is the possibility to load DICOM data. After setting the file to be loaded, the output provides a valid image. Resetting the application shall unload the image.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
# Requirement 1: The application shall be able to load DICOM data
def TEST_LoadDICOMData():
  # Set path to image and expect a valid image
  loadImage(path_to_image)
  ASSERT_TRUE(isImageValid())
  # Reset again and expect an invalid image
  reset()
  ASSERT_FALSE(isImageValid())
...
```
{{</highlight>}}

#### Requirement 4: The 2D viewer shall provide the possibility to segment parts of the image based on a RegionGrowing algorithm
##### Requirement 4.1: It shall be possible to click into the image for defining a marker position for starting the RegionGrowing
This test case shall make sure the `RegionGrowing` module calculates the total volume and number of voxels to be larger than 0 in case a marker has been set. Without loading an image or after resetting the application, the values shall be 0.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
# Requirement 4: The 2D viewer shall provide the possibility to segment parts of the image based on a RegionGrowing algorithm
# Requirement 4.1: It shall be possible to click into the image for defining a marker position for starting the RegionGrowing
def TEST_RegionGrowing():
  # Load image and expect volumes and voxels without marker to be 0
  loadImage(path_to_image)
  region_growing_voxels = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_EQ(region_growing_voxels, 0)
  ASSERT_EQ(region_growing_volume, 0)
  # Set marker and expect volumes and voxels to be larger than 0
  setMarkerPosition(marker_location)
  region_growing_voxels = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_GT(region_growing_voxels, 0)
  ASSERT_GT(region_growing_volume, 0)
  # Reset application and expect volumes and voxels to be 0 again
  reset()
  region_growing_voxels = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_EQ(region_growing_voxels, 0)
  ASSERT_EQ(region_growing_volume, 0)
...
```
{{</highlight>}}

##### Requirement 4.2: It shall be possible to define a threshold for the RegionGrowing algorithm
For the threshold of the region growing it makes sense to extend previous test case instead of writing a new one. We already have a segmentation based on the default threshold value and can just change the threshold and compare the resulting volumes.

Increasing the threshold shall result in larger volumes, decreasing shall result in smaller values.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
# Requirement 4: The 2D viewer shall provide the possibility to segment parts of the image based on a RegionGrowing algorithm
# Requirement 4.1: It shall be possible to click into the image for defining a marker position for starting the RegionGrowing
# Requirement 4.2: It shall be possible to define a threshold for the RegionGrowing algorithm
def TEST_RegionGrowing():
  # Load image and expect volumes and voxels without marker to be 0
  loadImage(path_to_image)
  region_growing_voxels = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_EQ(region_growing_voxels, 0)
  ASSERT_EQ(region_growing_volume, 0)
  # Set marker and expect volumes and voxels to be larger than 0
  setMarkerPosition(marker_location)
  region_growing_voxels = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_GT(region_growing_voxels, 0)
  ASSERT_GT(region_growing_volume, 0)
  # Test the threshold functionality by changing the value and comparing the results
  current_threshold = ctx.field("TutorialSummary.thresholdInterval").value
  current_threshold = current_threshold + 0.5
  ctx.field("TutorialSummary.thresholdInterval").value = current_threshold
  region_growing_voxels_new = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume_new = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_GT(region_growing_voxels_new, region_growing_voxels)
  ASSERT_GT(region_growing_volume_new, region_growing_volume)
  current_threshold = current_threshold - 0.7
  ctx.field("TutorialSummary.thresholdInterval").value = current_threshold
  region_growing_voxels_new = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume_new = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_LT(region_growing_voxels_new, region_growing_voxels)
  ASSERT_LT(region_growing_volume_new, region_growing_volume)
  # Reset application and expect volumes and voxels to be 0 again
  reset()
  region_growing_voxels = ctx.field("TutorialSummary.RegionGrowing.numSegmentedVoxels").value
  region_growing_volume = ctx.field("TutorialSummary.RegionGrowing.segmentedVolume_ml").value
  ASSERT_EQ(region_growing_voxels, 0)
  ASSERT_EQ(region_growing_volume, 0)
...
```
{{</highlight>}}

#### Requirement 5: The 2D viewer shall display the segmentation results as a semi-transparent overlay
##### Requirement 5.1: It shall be possible to define the color of the overlay
The requirement 5 can not be tested automatically. Transparencies should be tested by a human being.

Nevertheless, we can write an automated test checking the possibility to define the color of the overlay and the 3D segmentation.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
def TEST_OverlayColor():
  reset()
  loadImage(path_to_image)
  setMarkerPosition(marker_location)
  ctx.field("SoCameraInteraction.viewAll").touch()
  ctx.field("SoCameraInteraction.viewFromLeft").touch()
  MLAB.processInventorQueue()
  ctx.field("OffscreenRenderer.update").touch()
  MLAB.processInventorQueue()
  current_color = ctx.field("TutorialSummary.selectOverlayColor").value
  ctx.field("TutorialSummary.selectOverlayColor").setValue(new_color)
  ctx.field("SoCameraInteraction.viewAll").touch()
  ctx.field("SoCameraInteraction.viewFromLeft").touch()
  MLAB.processInventorQueue()
  ctx.field("OffscreenRenderer1.update").touch()
  MLAB.processInventorQueue()
  ASSERT_NE(current_color, ctx.field("TutorialSummary.selectOverlayColor").value)
  ASSERT_EQ(ctx.field("TutorialSummary.selectOverlayColor").value, ctx.field("TutorialSummary.SoView2DOverlay.baseColor").value)
  ASSERT_EQ(ctx.field("TutorialSummary.selectOverlayColor").value, ctx.field("TutorialSummary.SoWEMRendererSegmentation.faceDiffuseColor").value)
  ASSERT_FALSE(ctx.field("ImageCompare.testPassed").value)
...
```
{{</highlight>}}

Again, we reset the application to an initial state, load the image and set a marker. We remember the initial color and set a new color for our Macro Module. Then we check if the new color differs the old color and if the colors used by the internal modules `SoWEMRendererSegmentation` and `SoView2DOverlay` changed to our new color.

In the end an image comparison is done for the 3D rendering using the old and the new color. The images shall differ.

The call *MLAB.processInventorQueue()* is sometimes necessary if an inventor scene changed via Python scripting, because the viewers might not update immediately after changing the field. MeVisLab is now forced to process the queue in inventor and to update the renderings.

#### Requirement 8: The total volume of the segmented area shall be calculated and shown (in ml)
For the correctness of the volume calculation, we added the `CalculateVolume` module to our test network. The volume given by our macro is compared to the volume of the segmentation from output *outSegmentationMask* calculated by the `CalculateVolume`module.

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
# Requirement 8: The total volume of the segmented area shall be calculated and shown (in ml)
def TEST_VolumeCalculation():
  # Reset and expect all volumes and number of voxels to be 0
  reset()
  reference_volume = ctx.field("CalculateVolume.totalVolume").value
  ASSERT_EQ(reference_volume, 0)
  # Load patient, set marker and expect all volumes and number of voxels to be > 0
  loadImage(path_to_image)
  reference_volume = ctx.field("CalculateVolume.totalVolume").value
  ASSERT_EQ(reference_volume, 0)
  setMarkerPosition(marker_location)  
  reference_volume = ctx.field("CalculateVolume.totalVolume").value
  current_volume = ctx.field("TutorialSummary.totalVolume").value
  # Expect the total volume of the application to be the same as our additional CalculateVolume module
  ASSERT_GT(reference_volume, 0)
  ASSERT_EQ(reference_volume, current_volume)
  #set marker to a different location and check if volumes change.
  setMarkerPosition(marker_location_new)  
  reference_volume_new = ctx.field("CalculateVolume.totalVolume").value
  current_volume_new = ctx.field("TutorialSummary.totalVolume").value
  ASSERT_NE(reference_volume, reference_volume_new)
  ASSERT_NE(current_volume, current_volume_new)
  ASSERT_EQ(reference_volume_new, current_volume_new)
...
```
{{</highlight>}}

#### Requirement 9: It shall be possible to toggle the visible 3D objects
##### Requirement 9.1: Original data
##### Requirement 9.2: Segmentation results
##### Requirement 9.3: All
In the end, we want to develop a testcase for the 3D toggling of the view. We can not exactly test if the rendering is correct, therefore we will check if the 3D rendering image changes when toggling the 3D view. We will use the modules `OffscreenRenderer`, `ImageCompare` and `SoCameraInteraction` we added to our test network.

Initially, without any marker and segmentation, the views *Both* and *Head* 

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
# Requirement 9: It shall be possible to toggle the visible 3D objects
# Requirement 9.1: Original data
# Requirement 9.2: Segmentation results
# Requirement 9.3: All
def TEST_Toggle3DVolumes():
  # Set ImageCompare.postErrorOnDiff to False because otherwise differences will lead to a failed test
  ctx.field("ImageCompare.postErrorOnDiff").value = False
  # Reset application and check if number of voxels is 0 on output
  reset()
  loadImage(path_to_image)
  # Without marker, the content of the 3D viewer should be the same for File and All
  ctx.field("NetworkTest.selected3DView").value = "Both"
  MLAB.processInventorQueue()
  ctx.field("SoCameraInteraction.viewFromLeft").touch()
  MLAB.processInventorQueue()
  ctx.field("OffscreenRenderer.update").touch()
  ctx.field("NetworkTest.selected3DView").value = "File"
  MLAB.processInventorQueue()
  ctx.field("OffscreenRenderer1.update").touch()
  ctx.field("ImageCompare.compare").touch()
  ASSERT_TRUE(ctx.field("ImageCompare.testPassed").value)
  # With marker, the content of the 3D viewer should be different
  setMarkerPosition(marker_location)
  ctx.field("NetworkTest.selected3DView").value = "Both"
  MLAB.processInventorQueue()
  ctx.field("OffscreenRenderer.update").touch()
  ctx.field("NetworkTest.selected3DView").value = "File"
  ctx.field("OffscreenRenderer1.update").touch()
  MLAB.processInventorQueue()
  ctx.field("ImageCompare.compare").touch()
  ASSERT_FALSE(ctx.field("ImageCompare.testPassed").value)
  ctx.field("NetworkTest.selected3DView").value = "Segmented"
  ctx.field("OffscreenRenderer1.update").touch()
  MLAB.processInventorQueue()
  ctx.field("ImageCompare.compare").touch()
  ASSERT_FALSE(ctx.field("ImageCompare.testPassed").value)
  ctx.field("NetworkTest.selected3DView").value = "Both"
  ctx.field("OffscreenRenderer.update").touch()
  MLAB.processInventorQueue()
  ctx.field("ImageCompare.compare").touch()
  ASSERT_FALSE(ctx.field("ImageCompare.testPassed").value)
...
```
{{</highlight>}}

### Sorting order in TestCaseManager
The MeVisLab TestCaseManager sorts your test cases alphabetically. Your test cases should look like this now:

![TestCaseManager Sorting](/images/tutorials/summary/Example4_6.png "TestCaseManager Sorting")

Executing all testcases results in exactly this order. If you want to change the sorting order - for example in this case it makes sense to test the possibility of region growing before testing the color of the resulting overlay - you can just add numeric prefixes to your test cases. This might look like this then:

![TestCaseManager Custom Sorting](/images/tutorials/summary/Example4_7.png "TestCaseManager Custom Sorting")

### Not testable requirements
As already mentioned, some requirements can not be tested in an automated environment. Human eyes cannot be replaced completely.

In our application, the following tests have not been tested automatically:
* Requirement 2: The application shall provide a 2D and a 3D viewer.
* Requirement 3: The 2D viewer shall display the loaded images
* Requirement 5: The 2D viewer shall display the segmentation results as a semi-transparent overlay
* Requirement 6: The 3D viewer shall visualize the loaded data in a 3-dimensional volume rendering
* Requirement 7: The 3D viewer shall additionally show the segmentation result as a 3-dimensional mesh

### Test Reports
The results of your tests are shown in a Report Viewer. You can also export the results to JUnit for usage in build environments like [Jenkins](https://www.jenkins.io/).

![ReportViewer](/images/tutorials/summary/Example4_8.png "ReportViewer")

### Screenshots
You can also add screenshots of your inventor scene to the report. Add the following to your Python script and a Snapshot of your 3D scene is attached to your test report:

{{< highlight filename="<TEST_CASE_NAME>.py" >}}
```Python
...
result = ScreenShot.createOffscreenScreenShot("SoCameraInteraction.self", "screenshot.png")
Logging.showImage("My screenshot", result)
Logging.showFile("Link to screenshot file", result)
...
```
{{</highlight>}}

## Summary
* Define accessible fields for Macro Modules so that they can be set in Python tests
* Add outputs to your Macro Modules for automated testing and connecting testing modules
* Testcase numbering allows you to sort them and define execution order

{{<alert class="info" caption="Info">}}
Additional information about MeVisLab TestCenter can be found in {{< docuLinks "/Resources/Documentation/Publish/SDK/TestCenterManual/index.html" "TestCenter Manual" >}}
{{</alert>}}

{{< networkfile "examples/summary/TutorialSummaryTest.zip" >}}
