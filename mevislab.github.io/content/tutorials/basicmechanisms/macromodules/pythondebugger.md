---
title: "Example 5: Debugging Python in MATE"
date: 2025-01-09
status: "OK"
draft: false
weight: 455
tags: ["Advanced", "Tutorial", "Python", "Debugging", "MATE"]
menu: 
  main:
    identifier: "pythondebugger"
    title: "Debugging Python in MATE"
    weight: 455
    parent: "basicmechanisms"
---
# Example 5: Debugging Python files in MATE
## Introduction
MeVisLab provides the powerful integrated text editor MATE. By default, MATE is used to create/edit files like Python scripts. In this tutorial, we want to show you how to debug Python scripts in MeVisLab. 

## Prepare your network
We are using a very simple network of pre-defined modules, but you can also debug your self-written Python scripts. Add a `LocalImage` module to your workspace and connect it to a `DicomTagBrowser` module. The `DicomTagBrowser` module shows a table containing the DICOM tags of your currently opened file.

![Example Network](/images/tutorials/basicmechanics/Debug1.png "Example Network")

## Open Python script in MATE
To debug our module, we need to open the Python file. Right-click {{< mousebutton "right" >}} the module `DicomTagBrowser` and select {{< menuitem "Related Files (3)" "DicomTagBrowser.py" >}}. The file is opened in MATE.

{{<alert class="info" caption="Attention">}}
MATE only opens Python files if default configuration in *MeVisLab/Preferences* is not changed for *Supportive Programs*.
{{</alert>}}

![MATE](/images/tutorials/basicmechanics/Debug2.png "MATE")

{{<alert class="info" caption="Information">}}
You can not only debug your own files, but also Python scripts of pre-defined MeVisLab modules.
{{</alert>}}

The user interface of MATE provides some relevant views for debugging.

### Outline view
The *Outline* view shows a list of all functions defined in your currently opened script.

### Project Workspace view
The *Project Workspace* view shows the content of the directories for all of your opened files. In this case, we only opened one file and only see the content of the directory for the `DicomTagBrowser` module.

### Debug Output view
The *Debug Output* view shows the messages you also see in MeVisLab. Additional views are available as soon as we start debugging our file.

## Debug a Python script
First we need to enable debugging. In the MATE main menu, select {{< menuitem "Debug" "Enable Debugging" >}}. You can see some new panels appearing in MATE.

### Debugging panel
The *Debugging* panel allows you to step through your code.

![Debugging Panel](/images/tutorials/basicmechanics/Debug3.png "Debugging Panel")

### Stack Frames panel
The *Stack Frames* panel shows your current stack trace while debugging.

![Stack Frames](/images/tutorials/basicmechanics/Debug4.png "Stack Frames")

### Variables/Watches/Evaluate Expression panel
Another panel *Variables/Watches/Evaluate Expression* appears, where you can see all current local and global variables. Add your own variables to watch their current value and evaluate your own expressions.

![Variables/Watches/Evaluate Expression](/images/tutorials/basicmechanics/Debug5.png "Variables/Watches/Evaluate Expression")

Scroll to line 180 and left click {{< mousebutton "left" >}} on the line number.

{{< highlight >}}
```Python
  179 def copyCurrentTagName():
> 180     item = ctx.control("dicomTree").currentItem()
  181     if item:
  182         MLAB.copyToPasteboard(item.text(1))
```
{{</highlight>}}

You can see a red dot marking a break point for debugging. Whenever this line of code is executed, execution will stop here and you can evaluate your variables. This line will be reached whenever you right-click {{< mousebutton "right" >}} on the list in the `DicomTagBrowser` module and select {{< menuitem "Copy Tag Name" >}}.

Go back to MeVisLab and right click {{< mousebutton "right" >}} on any DICOM tag in the `DicomTagBrowser` module. Select {{< menuitem "Copy Tag Name" >}}.

![Copy Tag Name](/images/tutorials/basicmechanics/Debug6.png "Copy Tag Name")

MATE opens automatically and you can see an additional yellow arrow indicating the line about to be executed next.

![MATE Debugger](/images/tutorials/basicmechanics/Debug7.png "MATE Debugger")

You can now use the controls of the *Debugging* panels to step through your code or just continue execution of your code. Whenever your execution is stopped, you can use the *Stack Frames* and the *Variables/Watches/Evaluate Expression* panel to see the current value of all or just watched variables.

We want to see the name of the DICOM tag we selected in the `DicomTagBrowser` module. You can access the values the following way:

{{< highlight >}}
```Python
item.text(0) # shows the tag ID (first column)
item.text(1) # shows the tag Name
item.text(2) # shows the tag VR
item.text(3) # shows the tag Value
```
{{</highlight>}}

Select *Watches* panel and enter **item.text(1)**. Again copy any tag name in MeVisLab `DicomTagBrowser` module. You will see that MATE shows an error. The reason is that the execution stops before executing the current line of code. Your Python code in line 180 defines the variable *item*, and therefore it is not yet defined at this moment. 

Use the *Debugging* panel (fifth button *Step to next line*) or press {{< keyboard "F10" >}}. The debugger jumps to the next line (**181**) and the variable *item* is defined. You can see the value of the *Tag Name* you just copied. You can add any variables you are interested in the same way.

![Watches panel](/images/tutorials/basicmechanics/Debug7b.png "Watches panel")

The *Variables* panel now shows all currently available local and global variables including their value(s). The *Stack Trace* panel shows that the *copyCurrentTagName* function has been called after the *DicomTagBrowser.MenuItem.command* from the \*.script file of the `DicomTagBrowser` module.

![Variables/Watches panel](/images/tutorials/basicmechanics/Debug7a.png "Variables/Watches panel")

## Conditions for Breakpoints
You can also define conditions for your breakpoints. Remove breakpoint in line 180 and set a new one in line 181. In case you only want to stop the execution of your script if a specific condition is met, right click {{< mousebutton "right" >}} on your breakpoint and select {{< menuitem "Set Condition for Breakpoint" >}}. A dialog opens where you can define your condition. Enter **item.text(1) == 'SOPClassUID'** as condition.

![Conditions for Breakpoints](/images/tutorials/basicmechanics/Debug8.png "Conditions for Breakpoints")

Now, the code execution is only stopped if you copy the tag name *SOPClassUID*. In case another line is copied, the execution does not stop and just continues.

## Evaluate Expression
The *Evaluate Expression* tab allows you to modify variables during execution. In our example you can set the result **item.text(1)** to something like **item.setText(1, "Hello")**. If you now step to the next line via {{< keyboard "F10" >}}, your watched value shows *"Hello"* instead of *"SOPClassUID"*.

{{< imagegallery 2 "/images/tutorials/basicmechanics" "Debug9" "Debug9a" >}}

## Summary
* MATE allows debugging of any Python files including files pre-defined in MeVisLab.
* Values of variables can be watched.
* It is possible to define conditions for breakpoints, so that the execution is only stopped if the condition is met.
* It is possible to change values of variables while program execution is stopped via *Evaluate Expression* panel.
