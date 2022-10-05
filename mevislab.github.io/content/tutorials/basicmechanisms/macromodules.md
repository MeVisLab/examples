---
title: "Example 2: Macro Modules and Module Interaction"
date: 2022-06-15T08:58:44+02:00
draft: false
status: "OK"
tags: ["Beginner", "Tutorial", "Macro", "Macro Modules"]
menu: 
  main:
    identifier: "macro_modules"
    title: "Examples for Creating Macro Modules, adding User Interfaces and Python scripting."
    weight: 370
    parent: "basicmechanisms"
---

# Example 2: Macro Modules {#TutorialChapter6}

## Macro Modules and Module Interactions via User Interface and Python Scripting

MeVisLab provides different types of modules, which can be distinguished by their color. The brown modules are called macro modules. Macro modules condense a whole network into one module. You can open the internal network by pressing the middle mouse button {{< mousebutton "middle" >}} or via right mouse click {{< mousebutton "right" >}} and select {{< menuitem "Help" "Show Internal Network" >}}. Macro modules provide the possibility to create customized user interfaces and and python interactions.

In [Chapter I - Basic Mechanics](./tutorials/basicmechanisms) we built a
contour filter and condensed all the modules into one local macro module.
Until now, the local macro module containing the contour filter can only
be used in the current network. In the following chapters, we like to make
the macro module commonly available throughout projects and equip this
macro module with panels and help pages. Commonly available macro
modules are called global macros and can be found in MeVisLab {{< menuitem "Module Search" >}}. Global macros and projects are stored
in packages. A package structure makes it easy to exchange projects and
different functionalities between people.

Therefore, this chapter will cover:
1. [Package creation](./tutorials/basicmechanisms/macromodules/package/)
2. [Creation of global macro modules](./tutorials/basicmechanisms/macromodules/globalmacromodules/)
3. [Creation of help files and example networks](./tutorials/basicmechanisms/macromodules/helpfiles/)
4. [GUI development: Interactions with macro modules via user interfaces (using MDL)](./tutorials/basicmechanisms/macromodules/guidesign/)
5. [Interactions with macro modules via Python scripting](./tutorials/basicmechanisms/macromodules/pythonscripting/)
