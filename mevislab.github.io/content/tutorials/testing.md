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

## Testing, Profiling, and Debugging in MeVisLab {#TutorialTesting}

The MeVisLab Integrated Development Environment (IDE) provides tools to write automated tests in Python, to profile your network performance, and to debug your Python code.
All of these funtionalities will be addressed in this chapter.

### Testing
The MeVisLab TestCenter is the starting point of your tests. Select {{<menuitem "File" "Run TestCaseManager" >}} to open the user interface of the TestCaseManager.

![MeVisLab TestCaseManager](images/tutorials/testing/TestCaseManager.png "MeVisLab TestCaseManager")

#### Test Selection
The Test Selection allows you to define a selection of test cases to be executed. The list can be configured by defining a filter, manually selecting the packages ([see Example 2.1: Package Creation](tutorials/basicmechanisms/macromodules/package)) to be scanned for test cases. All test cases found in the selected packages are shown.

On the right side of the Test Selection tab, you can see a list of functions in the test case. Each list entry is related to a Python function. You can select the functions to be executed. If your test case contains a network, you can open the *.mlab* file or edit the Python file in MATE.

#### Test Reports
The results of your tests are shown as a report after execution. 

#### Test Creation
You can create your own test cases here. A package is necessary to store your network and Python file.

#### Configuration
Here you can configure details of your tests and reports. The filepath to the directory of your MeVisLab installation is configured automatically.  
{{<alert class="check" caption="Check">}}
If you have multiple versions installed, make sure to check and, if needed, alter the automatically configured filepath.
{{</alert>}}

### Profiling
Profiling allows you to get detailed information on the behavior of your modules and networks. You can add the profiling view via {{<menuitem "View" "Views" "Profiling" >}}. The Profiling will be displayed in the Views area of the MeVisLab IDE.

![MeVisLab Profiling](images/tutorials/testing/Profiling.png "MeVisLab Profiling")

With enabled profiling, your currently opened network will be inspected and the CPU and memory usage and many more details of each module and function are logged. 

### Debugging
Debugging can be enabled whenever the integrated text editor MATE is opened. Having a Python file opened, you can enable debugging via {{<menuitem "Debug" "Enable Debugging" >}}. You can define break points in Python, add variables to your watchlist, and walk through your break points just like in other editors and debuggers.

![MeVisLab Debugging](images/tutorials/testing/MATE_debugging.png "MeVisLab Debugging")
