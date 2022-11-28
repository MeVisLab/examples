---
title: "Example 3: Iterative tests in MeVisLab with Screenshots"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
tags: ["Advanced", "Tutorial", "Testing", "Python", "Automated Tests", "Iterative Test", "Screenshot"]
menu: 
  main:
    identifier: "testingexample3"
    title: "Writing an iterative test in MeVisLab"
    weight: 765
    parent: "testing"
---
# Example 3: Iterative tests in MeVisLab

{{<youtube "1JidUyfz0xU">}}

## Introduction
In this example, you are writing an iterative test. Iterative test functions run a function for every specified input. They return a tuple consisting of the function object called and the inputs iterated over. The iterative test functions are useful if the same function should be applied to different input data. These could be input values, names of input images, etc.

## Steps to do
### Creating the network to be used for testing
Add a `LocalImage` and a `DicomTagViewer` module to your workspace and connect them.

![Example Network](/images/tutorials/testing/network_test3.png "Example Network")

### TestCase creation
Open the panel of the `DicomTagViewer` and set *Tag Name* to *WindowCenter*. The value of the DICOM tag from the current input image is automatically set as value.

Save the network.

Start MeVisLab TestCaseManager and create a new test case called *IterativeTestCase* as seen in [Example 1: Writing a simple testcase in MeVisLab](/tutorials/testing/testingexample1).

![DicomTagViewer](/images/tutorials/testing/DicomTagViewer.png "DicomTagViewer")

### Defining the test data
In TestCaseManager open the testcase Python file via *Edit File*.

Add a list for test data to be used as input and a prefix for the path of the test data as seen below.

{{< highlight filename="IterativeTestCase.py" >}}
```Python
from mevis import *
from TestSupport import Base, Fields, ScreenShot
from TestSupport.Macros import *

patientPathPrefix = "$(DemoDataPath)/BrainMultiModal/"

testData = { "ProbandT1":("ProbandT1.dcm", "439.9624938965"),
     "ProbandT2":("ProbandT2.dcm", "234.91")}
```
{{</highlight>}}

The above list contains an identifier for the test case (*ProbandT1/2*), the file names and a number value. The number value is the value of the DICOM tag (0028,1050) WindowCenter for each file.

### Create your iterative test function
Add the python function to your script file:
{{< highlight filename="IterativeTestCase.py" >}}
```Python
def ITERATIVETEST_TestWindowCenter():
  return testData, testPatient
```
{{</highlight>}}

This function defines that *testPatient* shall be called for each entry available in the defined list *testData*. Define the function *testPatient*:
{{< highlight filename="IterativeTestCase.py" >}}
```Python
def testPatient(path, windowCenter):
  ctx.field("LocalImage.name").value = patientPathPrefix + path
  tree = ctx.field("LocalImage.outImage").getDicomTree()
  importValue = str(tree.getTag("WindowCenter").value())
  dicomValue = str(ctx.field("DicomTagViewer.tagValue0").value)
  ASSERT_EQ(windowCenter, importValue, "Checking expected WindowCenter value against DICOM tree value.")
  ASSERT_EQ(windowCenter, dicomValue, "Checking expected WindowCenter value against DicomTagViewer value.")
```
{{</highlight>}}

1. Initially, the path and filename for the module `LocalImage` are set. The data is loaded automatically, because the module has the *AutoLoad* flag enabled by default.
![LocalImage](/images/tutorials/testing/LocalImage.png "LocalImage")
2. Then, the DICOM tree of the loaded file is used to get the *WindowCenter* value (*importValue*).
3. The previously defined value of the `DicomTagViewer` is set as *dicomValue*.
4. The final test functions *ASSERT_EQ* evaluate if the given values are equal.

{{<alert class="info" caption="Info">}}
You can use many other *ASSERT** possibilities, just try using the MATE auto completion and play around with them.
{{</alert>}}

### Run your iterative test
Open MeVisLab TestCase Manager and select your package and test case. You will see 2 test functions on the right side.

![Iterative Test](/images/tutorials/testing/TestCaseManager_TestWindowCenter.png "Iterative Test")

The identifiers of your test functions are shown as defined in the list (*ProbandT1/2*). The *TestWindowCenter* now runs for each entry in the list and calls the function *testPatient* for each entry using the given values.

### Adding screenshots to your TestReport
Now, extend your network by adding a `View2D` module and connect it with the `LocalImage` module. Add the following lines to the end of your function *testPatient*:
{{< highlight filename="IterativeTestCase.py" >}}
```Python
def testPatient(path, windowCenter):
  ...
  Fields.setValue("View2D.startSlice", 0)
  result = ScreenShot.createOffscreenScreenShot("View2D.self", "screentest.png")
  Logging.showImage("My screenshot", result)
  Logging.showFile("Link to screenshot file", result)
```
{{</highlight>}}

Your ReportViewer now shows a screenshot of the image in the `View2D`.

![Screenshot in ReportViewer](/images/tutorials/testing/Screenshot.png "Screenshot in ReportViewer")

## Summary
* Iterative tests allow you to run the same test function on multiple input entries.
* It is possible to add screenshots to test cases