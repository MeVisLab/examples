---
title: "Example 2.5: Interactions via Python scripting"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
tags: ["Beginner", "Tutorial", "Macro", "Macro Modules", "Global Macro", "Python", "Scripting"]
menu: 
  main:
    identifier: "pythonscripting"
    title: "Interactions with macro modules via Python scripting"
    weight: 420
    parent: "macro_modules"
---
# Example 2.5: Module Interactions Using Python Scripting {#TutorialPythonScripting}
## Introduction

This chapter will give you an overview over Python scripting in MeVisLab. Here, no introduction into Python will be given. However, basic knowledge in Python is helpful. Instead, we will show how to integrate and use Python in the MeVisLab SDK. 

In fact, nearly everything in MeVisLab can be done via Python scripting: You can add modules to your network, or remove modules, you can dynamically establish and remove connections and so on. But, much more important: You can access module inputs and outputs, as well as module fields to process their parameters and data. You can equip user interfaces and panel with custom functionalities. Python can be used to implement module interactions. When you open a panel or you press a button in a panel, the executed actions are implemented via Python scripting.

## Basics

To see how to access modules, fields, and so on, open the *Scripting Console* Via {{< menuitem "Scripting" "Show Scripting Console" >}}.
### Internal field names

You can find the internal name of one module field in the respective network. Open a panel, for example the Automatic Panel and right-click {{< mousebutton "right" >}} the field's title to open the field's context menu. Now, you can select *Copy Name*, to copy the internal name of the field. This name can be used to access the field via scripting.

### Scripting context

When entering *ctx* to the console, you can see the context you are working with. In the context of the *Scripting Console*, you have access to your workspace, meaning the whole network, its modules and the module fields.

![Scripting context](/images/tutorials/basicmechanics/Scripting_02.png "Scripting context")

### Editing the workspace

In the *Scripting Console*, you can add and connect modules using the following commands:

* *ctx.addModule("*< ModuleName >*")* : Add the desired module to your workspace.
* *ctx.field("* < ModuleName.FieldName> *")* : Access a field of a module.
* *ctx.field("* < ModuleInput > *").conntectFrom("* < ModuleOutput > *")* : Draw a connection from one module's output to another module's input.

In this case we added the modules `DicomImport` and `View2D` to the workspace and connected both modules.

![Add and connect modules via scripting](/images/tutorials/basicmechanics/Scripting_03.png "Add and connect modules via scripting")

It is also possible to add notes to your workspace.

![Add a note to the workspace](/images/tutorials/basicmechanics/Scripting_04.png "Add a note to your workspace")

### Access modules and module fields

You can access modules via *ctx.module("* < ModuleName > *")*. From this object, you can access module fields, module inputs and outputs and everything in context of this module. 

You can also directly access a module field via *ctx.field("* < ModuleName.FieldName > *")*. Different methods can be called on this object. Take a look at the {{< docuLinks "/Resources/Documentation/Publish/SDK/ScriptingReference/group__scripting.html" "Scripting Reference" >}} to find out which methods can be called for which object or class. You can for example access the value of the respective field.

[//]: <> (MVL-653)

![Access modules and module fields](/images/tutorials/basicmechanics/Scripting_05.png "Access modules and module fields")

### Python Scripting Reference

{{< docuLinks "/Resources/Documentation/Publish/SDK/ScriptingReference/group__scripting.html" "Here" >}}, you can find the Scripting Reference. In the Scripting Reference you can find information about different Python classes used in MeVisLab and their methods.

[//]: <> (MVL-653)

## Where and how to use Python scripting
#### Scripting View

Under {{< menuitem "View" "Views" "Scripting" >}} you can find the View *Scripting*. The view offers a standard Python console, without any meaningful network or module context. This means only general Python functionalities can be tested and used. Access to modules or your network is not possible.

#### Scripting Console

You can open the *Scripting Console* via {{< menuitem "Scripting" "Show Scripting Console" >}}. In the context of your workspace, you can access your network and modules.

#### Scripting console of modules

Every module offers a scripting console. Open the context menu of a module and select {{< menuitem "Show Window" "Scripting Console" >}}. You can work in the context (*ctx.*) of this module. 

#### Module `RunPythonScript`

The module `RunPythonScript` allows to execute Python scripts from within a MeVisLab network. You can draw parameter connection from modules to `RunPythonScript` and back, to process parameter fields using Python scripting. An example for the usage of `RunPythonScript` can be found [here](../scriptingexample1/).

#### Module interactions via Python scripting

You can reference to a Python function inside a *.script* file of a macro module. With this, you can for example execute a Python function, whenever you open a panel, define the action which is executed when pressing a button or specify the command triggered by a [field listener](tutorials/basicmechanisms/macromodules/scriptingexample2). An example for module interactions via Python scripting is given in the same example.

## Tips and tricks
#### Scripting Assistant

Under {{< menuitem "View" "Views" "Scripting Assistant" >}} you can find the view *Scripting Assistant*. In this view, the actions you execute in the workspace are translated into Python script.

For example: Open the *Scripting Assistant*. Add the module `WEMInitialize` to your workspace. You can select a *Model*, for example the cube. In addition, you can change the *Translation* and press *Apply*. All these actions can be seen in the *Scripting Assistant*, translated into Python code. Therefore, the *Scripting Assistant* is a powerful tool to help you to script you actions.

![Scripting Assistant](/images/tutorials/basicmechanics/Scripting_01.png "Scripting Assistant")

## Examples
See the following examples for Python Scripting:
1. [The module RunPythonScript](./tutorials/basicmechanisms/macromodules/scriptingexample1/)
2. [Module interactions via Python scripting](./tutorials/basicmechanisms/macromodules/scriptingexample2/)

## Summary

* Python can be used to access, create and process networks, modules, fields and panels.
* You can use Python via different scripting consoles.
* You can also define module costume module interactions by referencing to Python functions from the *.script* file