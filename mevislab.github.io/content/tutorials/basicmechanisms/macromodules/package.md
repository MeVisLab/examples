---
title: "Example 2.1: Package Creation"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 380
tags: ["Beginner", "Tutorial", "Package"]
menu: 
  main:
    identifier: "packageCreation"
    title: "Creation of packages necessary for Macro modules."
    weight: 380
    parent: "macro_modules"
---


# Example 2.1: Package creation

{{< youtube "1wrGsYtAs3g">}}

## Introduction

Packages are the way MeVisLab organizes different development projects.

Macro modules and projects are stored in packages. If you like to create a global macro module, you need a package in which this macro module can be stored in. In this chapter, we will create our own package. We start our package creation by creating a package group, because every package needs to be stored in a package group. You can find detailed information about packages and package groups {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch08.html" "here" >}} and in the {{< docuLinks "/Resources/Documentation/Publish/SDK/PackageStructure/index.html" "package documentation" >}}.

[//]: <> (MVL-651)

[//]: <> (MVL-653)

## Steps to do
To create packages and package groups, we will use the Project Wizard. Open the Project Wizard via {{< menuitem "File" "Run Project Wizard ..." >}}. Then, select {{< menuitem "Package" "New Package" >}} and *Run Wizard*.

![The Project Wizard](/images/tutorials/basicmechanics/GUI_01.png "The Project Wizard")

Next you need to:

1.  Find a name for your package group, for example your company name or
    in our example the name *MyPackageGroup*.

2.  Find a name for your package, in our example we call it *General*.

3.  Select the path your package group is supposed to be stored in (If you
    like to add a package to an existing package group, select its name
    and chose the path the package group is stored in)

If you now create the package, you can find a folder structure in the
desired directory. The folder of your package group contains the folder
of your package. We have now successfully created a package in which we can store our
global macro module.

![Package creation](/images/tutorials/basicmechanics/GUI_02.png "Package creation")

## Summary
* Packages are needed to store global macro modules and projects.
* Package groups contain packages.
* Packages and package groups can be created using the *Project Wizard*.
* Detailed information about packages can be found in the {{< docuLinks "/Resources/Documentation/Publish/SDK/PackageStructure/index.html" "package documentation" >}}.

[//]: <> (MVL-653)