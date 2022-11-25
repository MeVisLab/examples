---
title: "Example 1: Writing a simple testcase in MeVisLab"
date: 2022-06-15T08:56:33+02:00
status: "open"
draft: false
tags: ["Beginner", "Tutorial", "Testing", "Python", "Automated Tests"]
menu: 
  main:
    identifier: "testingexample1"
    title: "Writing a simple testcase for the module DicomImport in MeVisLab using Python and MeVisLab TestCenter."
    weight: 755
    parent: "testing"
---
# Example 1: Writing a simple testcase in MeVisLab

## Introduction
In this example, you will learn how to write an automated test for a simple network using the `DicomImport`, `MinMaxScan` and `View3D` modules. You can write testcases for any other module and network yourself.

## Steps to do
### Creating the network to be used for testing
Add the following modules to your workspace and connect them as seen below: 

![Testcase network ](/images/tutorials/testing/testNetwork1.png "Testcase network ")

Save your network as *NetworkTestCase.mlab*.

## Test creation
Open MeVisLab TestCaseManager via menu {{<menuitem "File" "Run TestCaseManager" >}}. The following window will appear.

![TestCaseManager window ](/images/tutorials/testing/testCaseManagerWindow.png "TestCaseManager window ")

On *Test Creation* tab, enter the details of your testcase as seen below. Make sure to have a package available already. For details about packages, see ([Example 2.1: Package creation](./tutorials/basicmechanisms/macromodules/package/)).
Select the just saved network *NetworkTestCase.mlab*.

 ![Test Creation window ](/images/tutorials/testing/TestCreation.png "Test Creation window ")

Click *Create*. The MeVisLab text editor MATE opens automatically showing the Python file of your test. Create your first test function in Python:

{{< highlight filename="NetworkTestCase.py" >}}
```Python
from mevis import *
from TestSupport import Base, Fields, Logging, ScreenShot
from TestSupport.Macros import *

filePath="C:/Program Files/MeVisLab3.6.0/Packages/MeVisLab/Resources/DemoData/BrainT1Dicom" 

def OpenFiles():
  ctx.field("DicomImport.inputMode").value = "Directory"
  ctx.field("DicomImport.source").value = filePath
  ctx.field("DicomImport.triggerImport").touch()
  MLAB.processEvents()
  while not ctx.field("DicomImport.ready").value:  
    MLAB.sleep(1)
    Base.ignoreWarningAndError(MLAB.processEvents)
  ctx.field("DicomImport.selectNextItem").touch()
  MLAB.log("Files imported from: "+ctx.field("DicomImport.source").value)
  
def TEST_DicomImport():
  expectedValue=1.0
  OpenFiles() 
  currentValue=ctx.field("DicomImport.progress").value
  ASSERT_FLOAT_EQ(expectedValue,currentValue)
```
{{</highlight>}}

The *filePath* defines the DICOM files to load by using the `DicomImport` module. When calling the function *TEST_DicomImport*, an expected value of *1.0* is defined. Then, the DICOM files are opened.

The *OpenFiles* function defines the `DicomImport` field *inputMode* to be a *Directory*. In case you want to open single files, set this field value to *Files*. Then the *source* field is set to your previously defined *filePath*. After clicking *triggerImport*, the `DicomImport` module needs some time to load all images in the directory and process the DICOM tree. We have to wait until the field *ready* is *TRUE*. While the import is not ready, we wait for 1 millisecond and check again.

*MLAB.processEvents()* lets MeVisLab continue execution while waiting for the `DicomImport`to be ready.

In case you get error messages in MeVisLab console about invalid DICOM tags, you can ignore these errors by calling *Base.ignoreWarningAndError(MLAB.processEvents)* instead of *MLAB.processEvents()*.

After the field *ready* is true, the test touches the *selectNextItem* trigger, so that the first images of the patient are selected and shown. The additional log message only writes the source directory for information purposes into the MeVisLab console.

Back to the *TEST_DicomImport()* function, we get the current value of the field *progress* from the `DicomImport`. This field shows the progress as number between 0 and 1.

In the end, we check if *currentValue* and *expectedValue* of the progress are equal.

### Run your testcase

After finishing the code, open the TestCaseManager und run your test.

![Run TestCase](/images/tutorials/testing/runTestCase.png "Run TestCase")

After the test finished execution, the ReportViewer opens automatically showing the results of your test.

![ReportViewer](/images/tutorials/testing/successTestCase.png "ReportViewer")


### Writing a test for global macro modules
Writing automated tests for global macro modules works a little different. If you create a global macro module from your above network (for details, see [Example 2.2: Global Macro Modules](/tutorials/basicmechanisms/macromodules/globalmacromodules/)), the Python script remains the same, just the module access differs. You always need the name of your macro module as a prefix.

{{< highlight filename="NetworkTestCase.py" >}}
```Python
  ...
  # Testing a network file
  ctx.field("DicomImport.inputMode").value = "Directory"
  # Testing a macro module
  ctx.field("<MACRO_MODULE_NAME>.DicomImport.inputMode").value = "Directory"
```
{{</highlight>}}

## Exercise
Create a global macro module and implement the following test objectives for both (network and macro module) 
* check, if the file exists.
* check, if the max value of file is greater than zero.
* check, if the `View3D`-Input and `DicomImport`-output have the same data.

## Summary
* MeVisLab provides a TestCenter for writing automated tests in Python
* Tests can be executed on networks and macro modules
* The test results are shown in a ReportViewer


{{<alert class="info" caption="Info">}}
You can download the Python files [here](/examples/testing/example1/TestCases.zip)
{{</alert>}}
