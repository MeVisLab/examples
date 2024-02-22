---
title: "Example 2.4: GUI development"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 410
tags: ["Beginner", "Tutorial", "Macro", "Macro modules", "Global Macro", "User Interface", "GUI"]
menu: 
  main:
    identifier: "gui_development"
    title: "Custom User Interfaces for macro modules."
    weight: 410
    parent: "macro_modules"
---
# Example 2.4: Building a Panel Layout: Interactions with macro modules

{{< youtube "tdQUkkROWBg">}}

## Introduction
This chapter will give you an introduction into the creation of module panels and user
interfaces. For the implementation you will need to
use the {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html" "MeVisLab Definition Language (MDL)">}}.

{{<alert class="info" caption="Extra Infos">}}
More information about GUI design in MeVisLab can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/GettingStarted/ch11.html" "here">}}
{{</alert>}}

[//]: <> (MVL-653)
[//]: <> (MVL-651)

## Creating a panel for the macro module flilter {#Example_Paneldesign}
### Creation of a module panel
In [Example 2.2](/tutorials/basicmechanisms/macromodules/globalmacromodules) we created the global macro module `Filter`. By now, this module does not have a proper panel. When double-clicking {{< mousebutton "left" >}} the module, the *Automatic Panel* is shown.

The *Automatic Panel* contains fields, as well as module in and outputs. In this case, no fields exists except the *instanceName*. Accordingly, there is no possibility to interact with the module. Only the input and the output of the module are given.

![Automatic Panel](/images/tutorials/basicmechanics/GUI_10.png "Automatic Panel")

To add and edit a panel, open the context menu and select {{< menuitem "Related Files" "Filter.script" >}}. The text editor {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MATE">}} opens. You can see the file *Filter.script*, which you can edit to define a custom User Interface for the Module.

![Module script file](/images/tutorials/basicmechanics/GUI_11.png "Module script file")

### Module interface
Per default, the *\*.script* file contains the {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Interface" "interface" >}} of the module.
In the interface section (everything insight the curled brackets behind the name *Interface*) you can define the module inputs, the module outputs and also all module fields (or *Parameters*).

[//]: <> (MVL-653)
{{< highlight filename="Filter.script" >}}
```Stan
Interface {
    Inputs {
        Field input0 {
            internalName = Convolution.input0
        }
    }
    Outputs {
        Field output0 {
            internalName = Arithmetic2.output0
        }
    }
}
```
{{</highlight>}}

##### Module inputs and outputs

To create an input/output, you need to define a *Field* in the respective input/output environment. Each input/output gets a name (here *input0/output0*) which you can use to reference this field. The module input maps to an input of the internal network. You need to define this mapping. In this case the input of the macro module `Filter` maps to the input of the module `Convolution` of the internal network (*internalName = Convolution.input0*). Similarly, you need to define which output of the internal network maps to the output of the macro module `Filter`. In this example, the output of the internal module `Arithmethic2` maps to the output of our macro module `Filter` (*internalName = Arithmetic2.output0*).

Creating an input/output causes:
1. Input/output connectors are added to the module.
2. You can find placeholders for the input and output in the internal network (see image).
3. Input/output fields are added to the automatic panel.
4. A description of the input/output fields is automatically added to the module help file, when opening the *\*.mhelp* file after input/output creation. Helpfile creation is explained in [Example 2.3](/tutorials/basicmechanisms/macromodules/helpfiles/).

![Internal Network of your macro module](/images/tutorials/basicmechanics/BM_23.png "Internal Network of your macro module")

##### Module fields

In the environment *Parameters* you can define *fields* of your macro module. These fields may map to existing fields of the internal network (*internalName = ...* ), but they do not need to and can also be completely new. You can reference these fields when creating a panel, to allow interactions with these fields. All fields appear in the *Automatic Panel*.

### Module panel layout

To create your own User Interface, we need to create a {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Window" "Window" >}}. A window is one of the layout elements which exist in MDL. These layout elements are called {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#Controls" "controls" >}}. The curled brackets define the window environment, in which you can define properties of the window and insert further controls like a {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Box" "Box" >}}.

Initially, we call the window *MyWindowTitle*, which can be used to reference this window.

Double-clicking {{< mousebutton "left" >}} on your module now opens your first self developed User Interface.

[//]: <> (MVL-653)
{{< highlight filename="Filter.script" >}}
```Stan
Interface {
    Inputs {
        Field input0 {
            internalName = Convolution.input0
        }
    }
    Outputs {
        Field output0 {
            internalName = Arithmetic2.output0
        }
    }
    Parameters {

    }
}

Window MyWindowName {
    title = MyWindowTitle

    Box MyBox {

    }
}
```
{{</highlight>}}

![Module Panel](/images/tutorials/basicmechanics/ModulePanel.png "Module Panel")

You can define different properties of your control. For a window, you can for example define a title, or whether the
window should be shown in full screen (*fullscreen = True*).

These properties are called {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/#SyntaxTagsAndValues" "tags" >}} and are individually different for each control. Which tags exist for the control window can be found
{{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Window" "here" >}}.
The control box has different tags. You can for example define a
title for the box, but you can not define whether to present the box in
full screen.

If you like to add more than one control to your window,
for example one box and one label, you can specify their design like in
the following examples:

[//]: <> (MVL-653)
{{< highlight filename="Filter.script" >}}
```Stan
Window MyWindowName {
    title = MyWindowTitle
    w = 100
    h = 50

    Vertical {
        Box MyBox {
            title = "Title of my Box"
        }
        Label MyLabel {
            title = "This is a label below the box"
        }
    }
}
```
{{</highlight>}}

![Vertical layout of Box and Text](/images/tutorials/basicmechanics/VerticalLayout.png "Vertical layout of Box and Text")

{{< highlight filename="Filter.script" >}}
```Stan
Window MyWindowName {
    title = MyWindowTitle
    w = 100
    h = 50

    Horizontal {
        Box MyBox {
            title = "Title of my Box"
        }
        Label MyLabel {
            title = "This is a label below the box"
        }
    }
}
```
{{</highlight>}}

![Horizontal layout of Box and Text](/images/tutorials/basicmechanics/HorizontalLayout.png "Horizontal layout of Box and Text")


There are much more controls, which can be used. For example a CheckBox,
a Table, a Grid, a Button, \... . To find out more, take a look into the {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#Controls" "MDL Reference" >}}.

[//]: <> (MVL-653)

### Module interactions {#mdlInteractions}

Until now, we learned how to create the layout of a panel. As a next step, we like to get an overview over interactions.

{{<alert class="info" caption="Extra Infos">}}
You can add the module `GUIExample` to your workspace and play around with is.
{{</alert>}}

#### Access to existing fields of the internal network

To interact with fields of the internal network in your User Interface, we
need to access these fields. To access the field of the internal module
`Convolution`, which defines the kernel, we need to use the internal
network name. To find the internal field name, open the internal network of the macro module `Filter` (click on the module using the middle mouse button {{< mousebutton "middle" >}}).

Then, open the panel of the module `Convolution` and right-click {{< mousebutton "right" >}} the field title *Use* of the box *Predefined Kernel* and select *Copy Name*. You now copied the internal network name of the field to your clipboard. The name is made up of *ModuleName.FieldName*, in this case *Convolution.predefKernel*.

![Convolution Module](/images/tutorials/basicmechanics/Convolution.png "Convolution Module")

In the panel of the module `Convolution`, you can change this variable *Kernel* via a drop-down menu. In
MDL a drop-down menu is called a {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_ComboBox" "ComboBox" >}}. We can take over the field *predefKernel*, its drop-down menu and all its properties by
creating a new field in our panel and reference to the internal
field *Convolution.predefKernel*, which already exist in the internal network.

Changes of the properties of this field can be done in the curled brackets using tags (here, we changed the title).

[//]: <> (MVL-653)

{{< highlight filename="Filter.script" >}}
```Stan
Window MyWindowName {
    title = MyWindowTitle
    
    Field Convolution.predefKernel {
        title = Kernel
    }
}
```
{{</highlight>}}

![Selecting the kernel](/images/tutorials/basicmechanics/SelectingKernel.png "Selecting the kernel")

As an alternative, you can define the field *kernel* in the *Parameters* environment, and reference the defined field by its name. The result in the panel is the same. You can see a difference in the Automatic Panel. All fields, which are defined in the interface in the *Parameters* environment appear in the Automatic Panel. Fields of the internal network, which are used but not declared in the section *Parameters* of the module interface do not appear in the Automatic Panel.

{{< highlight filename="Filter.script" >}}
```Stan
Interface {
    Inputs {
        Field input0 {
            internalName = Convolution.input0
        }
    }
    Outputs {
        Field output0 {
            internalName = Arithmetic2.output0
        }
    }
    Parameters {
        Field kernel {
            internalName = Convolution.predefKernel
            title = Kernel:
        }
    }
}

Window MyWindowName {
    title = MyWindowTitle
    Field kernel {}
}
```
{{</highlight>}}

#### Commands

We can not only use existing functionalities, but also add new interactions via Python scripting.

In below example we added a *wakeupCommand* to the Window and a simple *command* to the Button.

{{< highlight filename="Filter.script" >}}
```Stan
Window MyWindowName {
    title = MyWindowTitle
    wakeupCommand = myWindowCommand
    
    Button MyButton {
        command = myButtonAction
    }
}
```
{{</highlight>}}

The *wakeupCommand* defines a Python function which is executed as soon as the Window is opened. The Button *command* is executed when the user clicks on the Button.

Both commands reference a Python function which is executed whenever both actions (open the Window or click the Button) are executed.

If you like to learn more about Python scripting, take a look at [Example 2.5](tutorials/basicmechanisms/macromodules/pythonscripting).

We need to define the Python script, which contains our Python functions. In order to do this, add a {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#mdl_Commands" "Command">}} section outside your window and define the tag source.

**Example:**
{{< highlight filename="Filter.script" >}}
```Stan
Commands {
    source = $(LOCAL)/Filter.py
}
```
{{</highlight>}}

{{<alert class="info" caption="Infos">}}
The section Source should already be available and generated automatically in case you enable the Wizard to add a Python file to your module.
{{</alert>}}

[//]: <> (MVL-653)

You can right-click {{< mousebutton "right" >}} on the command (*myWindowCommand* or *myButtonAction*) in your *\*.script* file and select {{< menuitem "Create Python Funtion......" >}}. The text editor MATE opens automatically and generates an initial Python function for you. You can simply add a logging function or implement complex logic here.

**Example:**
{{< highlight filename="Filter.py" >}}
```Python
def myWindowCommand:
    MLAB.log("Window opened")

def myButtonAction:
    MLAB.log("Button clicked")
```
{{</highlight>}}

## Available examples
MeVisLab provides a lot of example modules for GUI development. All of these examples provides the \*.script file for UI development and the \*.py file containing the Python script.

### Layouting examples
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestVerticalLayout" "TestVerticalLayout Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestHorizontalLayout" "TestHorizontalLayout Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestTableLayout" "TestTableLayout Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestGridLayout" "TestGridLayout Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestSplitterLayout" "TestSplitterLayout Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestBoxLayout" "TestBoxLayout Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestTabViewLayout" "TestTabViewLayout Module">}}

### Other examples
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestHyperText" "TestHyperText Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestListBox" "TestListBox Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestListView" "TestListView Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestIconView" "TestIconView Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestPopupMenu" "TestPopupMenu Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestViewers" "TestViewers Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestEventFilter" "TestEventFilter Module">}}
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html#TestStyles" "TestStyles Module">}}
* {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/TestButtonGroups.html" "TestButtonGroups Module">}}
* {{< docuLinks "/Standard/Documentation/Publish/ModuleReference/TestImageMap.html" "TestImageMap Module">}}

Please use the *Module Search* with the prefix *Test* for more examples.

## Summary
* User interfaces and several module panels can be created for each macro module.
* You can create a panel, define inputs and outputs as well as interactions, in your *\*.script* file in {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MATE">}} by using the {{< docuLinks "/Resources/Documentation/Publish/SDK/MDLReference/index.html" "MeVisLab Definition Language (MDL)">}}.
* Module interactions can be implemented using commands, which are linked to Python functions.
* You can implement field listeners, which trigger actions after a field value changes.

{{< networkfile "examples/basic_mechanisms/macro_modules_and_module_interaction/example1/FilterExample.zip" >}}
