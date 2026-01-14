---
title: "Example 1: Writing a simple test case in MeVisLab"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 755
tags: ["Beginner", "Tutorial", "Testing", "Python", "Automated Tests"]
menu: 
  main:
    identifier: "testingexample1"
    title: "Writing a simple test case for the module DicomImport in MeVisLab using Python and MeVisLab TestCenter."
    weight: 790
    parent: "testing"
---
# Example 1: Writing a Simple Test Case in MeVisLab

{{< youtube "DqpVaKai_00" >}}

## Introduction
In this example, you will learn how to write an automated test for a simple network using the `DicomImport`, `MinMaxScan`, and `View3D` modules. Afterwards, you will be able to write test cases for any other module and network yourself.

## Steps to Do
### Creating the Network to be Used for Testing
Add the following modules to your workspace and connect them as seen below: 

![Testcase network ](/images/tutorials/testing/testNetwork1.png "Testcase network ")

Save your network as *NetworkTestCase.mlab*.

## Test Creation
Open the MeVisLab TestCaseManager via menu {{<menuitem "File" "Run TestCaseManager" >}}. The following window will appear.

![TestCaseManager window ](/images/tutorials/testing/testCaseManagerWindow.png "TestCaseManager window ")

Change to the *Test Creation* tab and enter details of your test case as seen below. Make sure to have a package available already. 

{{<alert class="info" caption="Info">}}
Details on package creation can be found in [Example 2.1: Package creation](./tutorials/basicmechanisms/macromodules/package/).
{{</alert>}}

Select your saved *NetworkTestCase.mlab* file.

 ![Test Creation window ](/images/tutorials/testing/TestCreation.png "Test Creation window ")

Click *Create*. The MeVisLab text editor MATE will automatically open and display the Python file of your test. Add the below listed code to the Python file.

{{< highlight filename="NetworkTestCase.py" >}}
```Python
from mevis import *
from TestSupport import Base, Fields, Logging
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

The *filePath* variable defines the absolute path to the DICOM files that will be given to *source* field of the `DicomImport` module in the second step of the *OpenFiles* function. 

The *OpenFiles* function first defines the `DicomImport` field *inputMode* to be a *Directory*. If you want to open single files, set this field's value to *Files*. Then, the *source* field is set to your previously defined *filePath*. After clicking *triggerImport*, the `DicomImport` module needs some time to load all images in the directory and process the DICOM tree. We have to wait until the field *ready* is *True*. While the import is not ready yet, we wait for 1 millisecond at a time and check again. *MLAB.processEvents()* lets MeVisLab continue execution while waiting for the `DicomImport` to be ready.

When calling the function *TEST_DicomImport*, an expected value of *1.0* is defined. Then, the DICOM files are opened.

{{<alert class="check" caption="Check">}}
Call *Base.ignoreWarningAndError(MLAB.processEvents)* instead of *MLAB.processEvents()* if you receive error messages regarding invalid DICOM tags.
{{</alert>}}

When *ready* is true, the test touches the *selectNextItem* trigger, so that the first images of the patient are selected and shown. The source directory will be written on the console as an additional log message for informative purposes. 

The value of our `DicomImport`s *progress* field is saved as the *currentValue* variable and compared to the *expectedValue* variable by calling *ASSERT_FLOAT_EQ(expectedValue,currentValue)* to determine if the DICOM import has finished (*currentValue* and *expectedValue* are equal) or not. 

### Run Your Test Case
Open the TestCase Manager und run your test by selecting your test case and clicking on the *Play* button in the bottom right corner.

![Run Test Case](/images/tutorials/testing/runTestCase.png "Run Test Case")

After execution, the ReportViewer will open automatically displaying your test's results.

![ReportViewer](/images/tutorials/testing/successTestCase.png "ReportViewer")


### Writing a Test for Global Macro Modules
Please observe that field access through Python scripting works differently for global macros. Instead of accessing a field directly by calling their respective module, the module itself needs to be accessed as part of the global macro first.

{{< highlight filename="NetworkTestCase.py" >}}
```Python
  ...
  # Testing a network file
  ctx.field("DicomImport.inputMode").value = "Directory"
  # Testing a macro module
  ctx.field("<MACRO_MODULE_NAME>.DicomImport.inputMode").value = "Directory"
```
{{</highlight>}}

*Imagine unpeeled nuts in a bag as a concept - the field as a nut, their module as their nutshell, and the bag as the global macro.* 

{{<alert class="info" caption="Info">}}
[Example 2.2: Global macro modules](/tutorials/basicmechanisms/macromodules/globalmacromodules/) provides additional info on global macro modules and their creation.
{{</alert>}}

## Exercise
Create a global macro module and implement the following test objectives for both (network and macro module): 
* Check if the file exists.
* Check if the max value of file is greater than zero.
* Check if the `View3D` input and `DicomImport` output have the same data.

## Summary
* MeVisLab provides a TestCenter for writing automated tests in Python.
* Tests can be executed on networks and macro modules.
* The test results are shown in a ReportViewer.

{{< networkfile "examples/testing/example1/TestCases.zip" >}}
