---
title: "Example 2.3: Creation of module help"
date: 2022-06-15T08:58:44+02:00
status: "OK"
draft: false
weight: 400
tags: ["Beginner", "Tutorial", "Macro", "Macro modules", "Global Macro", "Help"]
menu: 
  main:
    identifier: "helpfiles"
    title: "Creation of module help files in MATE"
    weight: 400
    parent: "macro_modules"
---
# Example 2.3: Creation of Module Help
Generating help of a macro module is part of the video about macro modules from [Example 2: Creation of global macro modules](tutorials/basicmechanisms/macromodules/globalmacromodules)
{{< youtube "M4HnA0d1V5k">}}

## Introduction
In this chapter, you will learn how to create a help page and an example network. For hands-on training, we will use the macro module `Filter`, which was created in the [previous chapter](tutorials/basicmechanisms/macromodules/globalmacromodules).

Depending on the way the macro module was created, the default help page and example network might or might not exist. In the case they exist, the help page only contains information about module inputs and outputs as well as module fields. The example network only contains the macro module itself. Both, the help page and the example network, can be created and edited after module creation.

## Steps to Do

### Creation of Help Files Using MeVisLab MATE
We will start by creating a help file using the built-in text editor {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MeVisLab MATE">}} (MeVisLab Advanced Text Editor). If you open the context menu of your global macro module and select {{< menuitem "Help" >}}, it might be that no help page is given. We will start to create a help file by selecting {{< menuitem "Help" "Create Help" >}}. If a help page already exists, select {{< menuitem "Help" "Edit Help" >}}.

[//]: <> (MVL-653)

![Creation of module help](images/tutorials/basicmechanics/GUI_06.png "Creation of module help")

{{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MeVisLab MATE">}} opens. An *.mhelp* file (*Filter.mhelp*) is created automatically and stored in the folder your macro module `Filter` is stored in. You can find the folder structure in MATE on the left side. Editing the text field, you can edit the help file. 

[//]: <> (MVL-653)

![Edit module help file via MATE](images/tutorials/basicmechanics/GUI_07.png "Edit module help file via MATE")

When creating the help file of a module, all important information of the
module down to the field specifications are extracted and created automatically. Thus, the
basic module information is always available in the module
help. Additional documentation should be added by the module's author. On the left
side, you can find the outline of the help file. Each section can be
edited. In this example, we added the purpose of the module
to the help file.

![Edit module help file via MATE](images/tutorials/basicmechanics/GUI_08.png "Edit module help file via MATE")

MATE offers the possibility to format the text. By using the button *M*, module names can be formatted in such a way that links to the respective help file of the modules are created.

![Edit module help file via MATE](images/tutorials/basicmechanics/GUI_08_2.png "Edit module help file via MATE")

After finishing your documentation, you can click *Generate Help* or {{< keyboard "F7" >}} and your final help file is generated.

{{<alert class="info" caption="Extra Infos">}}
More information on MeVisLab MATE can be found {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "here">}}
The Module Help Editor is explained {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26s09.html" "here" >}}
{{</alert>}}

[//]: <> (MVL-653)

The result can be seen when opening the help file via context menu in MeVisLab IDE (or by pressing {{< keyboard "F1" >}}).

![Help file of the module](images/tutorials/basicmechanics/GUI_09.png "Help file of the module")

{{<alert class="warning" caption="Watch out">}}
Depending on the way the macro module was created, more or less features are automatically given in the help file and the example network. All missing features can be added manually.
{{</alert>}}

### Creation of an Example Network
To add an example network to your module, you need to add a reference to the respective *.mlab* file to the module definition file (.def). Open the file *Filter.def*. You can find the line *exampleNetwork     = "$(LOCAL)/networks/FilterExample.mlab"*, which defines the reference to the *.mlab* file containing the example network. By default, the name of the example network is *ModulenameExample.mlab*. An *.mlab* file containing only the module *Filter* is created inside the folder *networks*.

It is possible that the reference to the example network or the file *FilterExample.mlab* is missing. One reason could be that its creation was not selected when creating the macro module. In this case, add the reference and the file manually.

![Reference to Example Network](images/tutorials/basicmechanics/ExpNetwork_01.png "Reference to Example Network")

To create the example network, open the file *FilterExample.mlab* in MeVisLab and create an appropriate example.

![Example Network](images/tutorials/basicmechanics/ExpNetwork_02.png "Example Network")


## Summary
* {{< docuLinks "/Resources/Documentation/Publish/SDK/MeVisLabManual/ch26.html" "MeVisLab MATE">}} is a built-in text editor that can be used to create module help files and module panels, or to create module interactions via Python scripting.
* You can create help files via the module context menu using MeVisLab's MATE.
* You can add an example network to your macro module via the *.def* file.

[//]: <> (MVL-653)