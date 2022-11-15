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
Connect the modules as seen below and save your network.

![Example Network](/images/tutorials/testing/network_test1.png "Example Network")

### TestCase creation
Start MeVisLab TestCaseManager via {{<menuitem "File" "Run TestCaseManager...">}}. Select tab *Test Creation* and enter a name for your TestCase, i.e. *NetworkTestCase". Select Type *Other* and your custom Package.

{{<alert class="info" caption="Info">}}
Packages need to be created before test cases. See [Example 2.1: Package creation](/tutorials/basicmechanisms/macromodules/package) for details.
{{</alert>}}

In section *Test Network*, select *Import Network* and load your previously saved example network from above. Then click *Create*.

![Test Creation](/images/tutorials/testing/TestCaseManager_TestCreation.png "Test Creation")
