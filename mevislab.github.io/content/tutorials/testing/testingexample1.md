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
import the following modules and connect them as below : 

![Testcase network ](/images/tutorials/testing/testNetwork1.png "Testcase network ")

## Test creation
you can creat a test via  menu item {{<menuitem "File" "Run TestCaseManager" >}}. After clicking on Run TestCaseManager the following window will appear.
![TestCaseManager window ](/images/tutorials/testing/testCaseManagerWindow.png "TestCaseManager window ")

Click on **Test Creation** tab and fullfill the felds like name,Type and Package ([see Example 2.1: Package creation](./tutorials/basicmechanisms/macromodules/package/)).
 Dont forget to choose the network, that you want to test. The name of our project is NetworkTestCase and we will choose the created network **NetworkTestCase**.
 ![Test Creation window ](/images/tutorials/testing/fullfillThe_fields.png "Test Creation window ")
After clicking on **create** button the python file will open automaticlay . At first we define our test objectives and then implement them. The syntax of test function will be like: </br>
<span style="color:purple;font-weight:400;font-size:18px">
   <span style="color:blue;font-weight:400;font-size:18px">
      def
      </span>
 TEST_NameOfYourFunction():
</span>

#### Test objectives
* Testing, if the dicom-data is correctly imported.
* Testing, if the file exist.
* Testing, if max value of dicom-file is greater than zero.
* Testing, if the View3D-input has the same data like DicomImport-output
In order to achieve those test objectives , add the following code in the created python file.


{{< highlight filename="NetworkTestCase.py" >}}
```Python
from mevis import *
from TestSupport import Base, Fields, Logging, ScreenShot
from TestSupport.Macros import *
#give your own filePath
filePath="C:/Local/MeVisLab3.5.90/Packages/MeVisLab/Resources/DemoData/BrainT1Dicom" 

def OpenDicom ():
  ctx.field("DicomImport.inputMode").value = "Directory"
  ctx.field("DicomImport.source").value=filePath
  ctx.field("DicomImport.triggerImport").touch()
  MLAB.processEvents()
  # if you receive error because of DicomImport uncomment the following line
  #Base.ignoreWarningAndError(MLAB.processEvents)
  while not ctx.field("DicomImport.ready").value:  
    MLAB.sleep(1)
    Base.ignoreWarningAndError(MLAB.processEvents)
  ctx.field("DicomImport.selectNextItem").touch()
  MLAB.log("Path: "+ctx.field("DicomImport.source").value)
 
def TEST_FileExist():
  isExist=os.path.exists(filePath)
  ASSERT_TRUE(isExist)
  
def TEST_DicomImport():
  expectValue= 1.0
  OpenDicom() 
  actualValue= ctx.field("DicomImport.progress").value
  ASSERT_FLOAT_EQ(expectValue,actualValue)
    
def TEST_MaxValue():
  OpenDicom()
  maxValue=ctx.field("MinMaxScan.trueMaxValue").value
  condition= maxValue >0
  if not condition :
    MLAB.logError("Max value is zero")
  else :
    print(str(maxValue) + "Ok: is not zero")
#This function check if the View3D-input and DicomImport-output have the same data   
def TEST_CheckInputAndOutput() :
 OpenDicom()
 view3DInput= ctx.field("View3D.inImage").size3D()
 dicomImportOutput= ctx.field("DicomImport.output0").size3D()
 ASSERT_EQ(dicomImportOutput,view3DInput)
```
{{</highlight>}}
After finishing the code, open the TestCaseManager und run your test.
![Run TestCase ](/images/tutorials/testing/runTestCase.png "Run TestCase ")
The following window should be appear after running the test.
![TestCase run successfully ](/images/tutorials/testing/successTestCase.png "TestCase run successfully  ")
#### Writing test for global macro module
If you have your own global macro module  you can also create a test. For Example we create from the previous network  **NetworkTestCase** a global macro modul (see how to create a global macro moudle [Example 2.2: Global Macro Modules](/tutorials/basicmechanisms/macromodules/globalmacromodules)) and name it  **DicomTestCase**. Finally we save it as network and name ist ***MacroModuleTestCase***
![global macro module ](/images/tutorials/testing/macroModuleTest.png "global macro module ") 
Follow the steps to create a test and choose as network the ***MacroModuleTestCase.mlab***. In python file we will implement our test objectives. To access the field of submodules we should follow the following syntax.
 <span style="color:green;font-weight:400;font-size:18px">
 { NameOfGlobalMacroModule.NameOfSubmodule.NameOfField }
 </span>
  </br> The python code looks like following:

{{< highlight filename="MacroModulTestCase.py" >}}
```Python
from mevis import *
from TestSupport import Base, Fields, Logging, ScreenShot
from TestSupport.Macros import *
#give your own filePath
filePath="C:/Local/MeVisLab3.5.90/Packages/MeVisLab/Resources/DemoData/BrainT1Dicom" 

def OpenDicom ():
  ctx.field("DicomTestCase.DicomImport.inputMode").value = "Directory"
  ctx.field("DicomTestCase.DicomImport.source").value=filePath
  ctx.field("DicomTestCase.DicomImport.triggerImport").touch()
  MLAB.processEvents()
  # if you receive error because of DicomImport uncomment the following line
  #Base.ignoreWarningAndError(MLAB.processEvents)
  while not ctx.field("DicomTestCase.DicomImport.ready").value:  
    MLAB.sleep(1)
    Base.ignoreWarningAndError(MLAB.processEvents)
  ctx.field("DicomTestCase.DicomImport.selectNextItem").touch()
  MLAB.log("Path: "+ctx.field("DicomTestCase.DicomImport.source").value)
 
def TEST_FileExist():
  isExist=os.path.exists(filePath)
  ASSERT_TRUE(isExist)
  
def TEST_DicomImport():
  expectValue= 1.0
  OpenDicom() 
  actualValue= ctx.field("DicomTestCase.DicomImport.progress").value
  ASSERT_FLOAT_EQ(expectValue,actualValue)
    
def TEST_MaxValue():
  OpenDicom()
  maxValue=ctx.field("DicomTestCase.MinMaxScan.trueMaxValue").value
  condition= maxValue >0
  if not condition :
    MLAB.logError("Max value is zero")
  else :
    print(str(maxValue) + "Ok: is not zero")
    
#This function check if the View3D-input and DicomImport-output have the same data
def TEST_CheckInputAndOutput() :
 OpenDicom()
 view3DInput= ctx.field("DicomTestCase.View3D.inImage").size3D()
 dicomImportOutput= ctx.field("DicomTestCase.DicomImport.output0").size3D()
 ASSERT_EQ(dicomImportOutput,view3DInput)
```
{{</highlight>}}
After finishing the code open TestCaseManager and run it.
![Run TestCase ](/images/tutorials/testing/macroModuleTestCaseRun.png "Run TestCase ") 
The result should be like previous example.
![Test result ](/images/tutorials/testing/resultGlobalMacroModule.png "Test result ") 








