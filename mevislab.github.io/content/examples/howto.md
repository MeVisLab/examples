---
title: "Using deposited examples"
date: 2022-06-15T08:56:33+02:00
draft: false
status: "OK"
menu: 
  main:
    identifier: "how_to_examples"
    weight: 649
    parent: "examples"
---

## How to use the available examples:
The examples provided on this site are (normally) either \*.mlab files or *.zip archives. Sometimes there are also Python (\*.py) or Script (\*.script) files. This page shall explain how to use them in your local MeVisLab installation.

### MeVisLab (\*.mlab) files
MeVisLab files are networks stored as \*.mlab file. They can be opened in MeVisLab via double-click {{<mousebutton "left" >}} or via {{< menuitem "File" "Open">}}.

### Archives (\*.zip files)
Archives are mostly Macro Modules. They require a user package. See [Example 2.1: Package creation](/tutorials/basicmechanisms/macromodules/package/) for more information about MeVisLab packages.

Having a package, the examples can be extracted into the directory of your package. Make sure to keep the directory structure inside the package so that the examples are loaded correctly.

The directory structure of a MeVisLab package looks like this:
![Package directory structure](/images/examples/howto_1.png "Package directory structure")

In this example, we have the package *TutorialSummary* in the package group *MeVis*. A package normally at least contains a *Projects* directory. This directory should include your Macro Modules. If you extract a \*.zip file of a Macro Module, the *Projects* folder of your package should be the target directory.

In some cases we also provide test cases. Extract them into a directory *TestCases*.
![Package directory structure](/images/examples/howto_2.png "Package directory structure")

In case the directories do not exist, for example in an empty package, you can create them. Make sure to use the same names for the *Projects* and *TestCases* directories.

Back in MeVisLab, you might need to reload the module cache after extracting the example. Open {{< menuitem "Extras" "Reload Module Database (Clear Cache)" >}}.

### Python (\*.py) or Script (\*.script) files
Sometimes we provide Python or Script files. Make sure to follow the steps of the tutorial and then paste the content of the provided files into your file. Python and Script files without having a Macro Module or test case do not make sense in MeVisLab, therefore the tutorial needs to be done first.
