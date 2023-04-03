---
title: "Chapter VI: Testing"
date: 2022-06-15T08:56:33+02:00
status: "OK"
draft: false
weight: 750
tags: ["Beginner", "Tutorial", "Testing", "Python", "Automated Tests", "Profiling", "Debugging"]
menu: 
  main:
    identifier: "testing"
    title: "Testing, Profiling and Debugging in MeVisLab"
    weight: 785
    parent: "tutorials"
---
# MeVisLab Tutorial Chapter VI {#TutorialChapter6}

## Testing, Profiling and Debugging in MeVisLab {#TutorialTesting}

The MeVisLab Integrated Development Environment (IDE) provides tools for writing automated tests in Python, profiling your network performance and debugging your Python code.

In this chapter, all of these tools will be explained.

### Testing
The MeVisLab TestCenter is the starting point of your tests. Select {{<menuitem "File" "Run TestCaseManager" >}} to open the user interface of the TestCaseManager.

![MeVisLab TestCaseManager](/images/tutorials/testing/TestCaseManager.png "MeVisLab TestCaseManager")

#### Test Selection
The Test Selection allows you to define a selection of test cases to be executed. The list can be configured by defining a filter by manually selecting the packages ([see Example 2.1: Package Creation](/tutorials/basicmechanisms/macromodules/package)) to be scanned for test cases. All test cases found in the selected packages are shown.

On the right side of the Test Selection tab, you can see a list of functions in the test case. Each list entry is related to a Python function. You can select the functions to be executed. If your test case contains a network, you can open the \*.mlab file or edit the Python file in MATE.

#### Test Reports
The results of your tests are shown as a report after execution. 

#### Test Creation
You can create your own test cases here. A package is necessary to store your network and Python file.

#### Configuration
Here you can configure details of your tests and reports. The installation directory of your MeVisLab is configured automatically but maybe needs to be updated in case you have multiple versions of MeVisLab installed.

### Profiling
Profiling allows you to get detailed information about the behavior of your modules and networks. You can add the profiling view via {{<menuitem "View" "Views" "Profiling" >}}. The Profiling will be shown in the Views Area of the MeVisLab IDE.

![MeVisLab Profiling](/images/tutorials/testing/Profiling.png "MeVisLab Profiling")

With enabled profiling, your currently opened network will be inspected and the CPU and memory usage and many more details of each module and function are logged. 

### Debugging
Debugging can be enabled whenever the integrated text editor MATE is opened. Having a Python file opened, you can enable debugging via {{<menuitem "Debug" "Enable Debugging" >}}. You can define break points in Python, add variables to your watchlist and walk through your break points as known for other editors and debuggers.

![MeVisLab Debugging](/images/tutorials/testing/MATE_debugging.png "MeVisLab Debugging")
