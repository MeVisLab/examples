---
title: "Tips and Tricks"
date: 2023-11-29
status: "OK"
draft: false
weight: 890
tags: ["Basic", "Tutorial"]
menu: 
  main:
    identifier: "shorts"
    title: "Short Tips and Tricks in MeVisLab"
    weight: 890
    parent: "tutorials"
---

# MeVisLab Tips and Tricks

This chapter shows some features and functionalities which are helpful but do not provide its own tutorial.

* [Keyboard Shortcuts](/tutorials/shorts#shortcuts)
* [Using Snippets](/tutorials/shorts#snippets)
* [Scripting Assistant](/tutorials/shorts#scriptingassistant)
* [User Scripts](/tutorials/shorts#user_scripts)

## Keyboard Shortcuts {#shortcuts}
This is a collection of useful keyboard shortcuts in MeVisLab, hopefully it grows continuously.
<table class="table table-striped">
  <thead>
    <tr>
      <th>Shortcut</th>
      <th>Functionality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ctrl+1</td>
      <td>Automatically arrange selection of modules / in the current network</td>
    </tr>
    <tr>
      <td>Ctrl+2</td>
      <td>Open most recent network file</td>
    </tr>
    <tr>
      <td>Ctrl+3</td>
      <td>Run most recent test case (extremely useful for developers)</td>
    </tr>
      <td>Ctrl+A then Ctrl+1</td>
      <td>Layout network</td>
    </tr>
      <td>Ctrl+A then Tab</td>
      <td>Layout .script file (in MATE)</td>
    </tr>
      <td>Ctrl+D</td>
      <td>Duplicate currently selected module (including all field values)</td>
    </tr>
      <td>Ctrl+Left Mouse or Middle Mouse Button</td>
      <td>Show Internal Network</td>
    </tr>
      <td>Space</td>
      <td>Show hidden outputs of the currently selected module</td>
    </tr>
      <td>Ctrl+Alt+T</td>
      <td>Start test center</td>
    </tr>
      <td>Ctrl+K	</td>
      <td>Restart MeVisLab </td>
    </tr>
  </tbody>
</table>



## Using Snippets {#snippets}

{{< youtube "xX7wJiyfxhA" >}}

Sometimes you have to create the same network over and over again -- for example, to quickly preview DICOM files. Generally, you will at least add one module to load and another module to display your images. Sometimes you may also want to view the DICOM header data. A network you possibly generate whenever opening DICOM files will be the following:

![Open DICOM files](/images/tutorials/Snippets_Network.png "Open DICOM files")

Create a snippet of your commonly used networks by adding the snippets list from the main menu. Open {{< menuitem "View" "Views" "Snippets List">}}. A new panel is shown. Select all modules of your network and double-click *New...* in your *Snippets List*.

Enter a name for your snippet like *DICOM Viewer* and click *Add*.

A new snippet will be shown in your Snippets List. You can drag and drop the snippet to your workspace and the modules are re-used, including all defined field values.

![Snippets List](/images/tutorials/Snippets_Panel.png "Snippets List")

## Scripting Assistant {#scriptingassistant}

{{< youtube "y6110PW5N_w" >}}

If you are new to Python or don't have experiences in accessing fields in MeVisLab via Python scripting, the Scripting Assistant might help you.

Open {{< menuitem "View" "Views" "Scripting Assistant">}}. A new panel is shown. 

If you now interact with a network, module or macro module, your user interactions are converted into Python calls. You can see the calls in the panel of the Scripting Assistant and copy and paste them for your Python script.

![Scripting Assistant](/images/tutorials/ScriptingAssistant_Panel.png "Scripting Assistant")

## User Scripts {#user_scripts}

User scripts allow you to call any Python code from the main menu entry {{< menuitem "Scripting">}}. MeVisLab already comes with some user scripts you can try. You can also view the sources for example code via right-click {{< mousebutton "right" >}} on the menu entry under {{< menuitem "Scripting">}}.

This example shows you how to change the color of the MeVisLab IDE to a dark mode.

Right-click {{< mousebutton "right" >}} menu entry {{< menuitem "Scripting" "Utilities" "Close Unselected Panels">}} and select *Edit User Script*. The Python file opens in *MATE*. Right-click {{< mousebutton "right" >}} on the tab in the editor and select *Show Enclosing Folder*.

The opened directory contains all available user scripts. Add a new file *MyScripts.def* and open the file in *MATE*.

Enter the following:
{{< highlight filename="MyScripts.def" >}}
```Stan
UserIDEActions {
  Action "Set Dark Theme" {
    name       = changeTheme
    userScript = $(LOCAL)/changeTheme.py
    statusTip  = "Change Theme to dark mode."
    accel      = "ctrl+F9"
  }

}

UserIDEMenus {
  SubMenu "Theme" {
    ActionReference = changeTheme
  }
}
```
{{</highlight>}}

We define an action *Set Dark Theme*, which is added to the submenu *Theme* in the MeVisLab IDE menu item {{< menuitem "Scripting">}}. The action is named *changeTheme* and a reference to a Python script is added as *$(LOCAL)/changeTheme.py*. We also defined a keyboard shortcut {{< keyboard "ctrl+F9" >}}.

Change to MeVisLab IDE and select menu item {{< menuitem "Extras" "Reload Module Database (Clear Cache)">}}. Open the menu item {{< menuitem "Scripting">}}. You can see the new submenu {{< menuitem "Theme" "Set Dark Theme">}}. If you select this entry, you get an error in MeVisLab console: *Could not locate user script: .../changeTheme.py*

We did not yet create the Python file containing the code of your script.

Open the directory where your *MyScripts.def* file is located and create a new Python file *changeTheme.py*. Open the file in *MATE* and enter the following:

{{< highlight filename="changeTheme.py" >}}
```Python
from PythonQt.QtGui import QApplication, QColor, QPalette

fgColor = QColor("#888888")
bgColor = QColor("#333333")
palette = QApplication.palette()
palette.setColor(QPalette.Window, bgColor)
palette.setColor(QPalette.Background, bgColor)
palette.setColor(QPalette.Base, bgColor)
palette.setColor(QPalette.Button, bgColor)
palette.setColor(QPalette.WindowText, fgColor)
palette.setColor(QPalette.Text, fgColor)
QApplication.setPalette(palette)
```
{{</highlight>}}

This script defines the color of the MeVisLab user interface elements. You can define other colors and more items, this is just an example of what you can do with user scripts.

Switch back to the MeVisLab IDE and select the menu item {{< menuitem "Extras" "Reload Module Database (Clear Cache)">}} again. The colors of the MeVisLab IDE change as defined in our Python script. This change persists until you restart MeVisLab and can always be repeated by selecting the menu entry or the keyboard shortcut {{< keyboard "ctrl+F9" >}}.
