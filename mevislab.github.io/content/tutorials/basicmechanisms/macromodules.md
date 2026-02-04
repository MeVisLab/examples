---
title: "Example 2: Macro Modules and Module Interaction"
date: 2025-05-19
draft: false
weight: 370
status: "OK"
tags: ["Beginner", "Tutorial", "Macro", "Macro modules"]
menu: 
  main:
    identifier: "macro_modules"
    title: "Examples for Creating Macro Modules, Adding User Interfaces, and Python Scripting"
    weight: 370
    parent: "basicmechanisms"
---

# Example 2: Macro Modules {#TutorialChapter6}

## What is a Macro Module? 
A macro module can be used to develop your own functionality in MeVisLab.

Like all other standard MeVisLab modules, macro modules have a defined interface with inputs, outputs, and parameters (fields). This interface allows it to interact with other modules in a larger network. They hide the complexity of the internal network or Python code, presenting a more simplified and manageable unit to the user.

Macro modules are primarily defined using the *MeVisLab Definition Language (MDL)* and often incorporate Python scripting for added functionality, especially for dynamic user interfaces. Importantly, you don't need to write C++ code to create them.

The internal network of a macro module is saved in an *.mlab* file, often referred to as the macro network. The interface and other definitions are stored in *.def* and *.script* files.

You have two main options for developing a macro module:

* **With Internal Networks**: Use a macro module to reuse a network of modules. For example, if you build a network that applies a specific image filter and you want to use this setup in multiple projects, you can wrap the entire network into a single macro module. This way, you don’t need to manually reconnect all the individual modules each time — you just use your macro module. You can also add inputs and outputs to connect your internal network with other modules.

An example can be found in chapter [Basic Mechanics of MeVisLab (Example: Building a Contour Filter)](tutorials/basicmechanisms#TutorialMacroModules).

* **Without Internal Networks**: Use a macro module to add your own Python code. If MeVisLab is missing a specific functionality, you can write your own Python script and execute it in a macro module. This allows you to extend the software with custom behavior that integrates smoothly into your project. You can see the Python code at the right side of the image below.

The image shows these two options. The left side encapsulates a network of three modules into one macro module. The right side shows a macro module without an internal network, only containing your custom Python script.

A typical example for macro modules without an internal network is the execution of a pretrained AI model on an input ML image, see [Example 2: Brain Parcellation using PyTorch](tutorials/thirdparty/pytorch/pytorchexample2/) for details.

It is also possible to combine both approaches. You can add internal networks and additionally write Python code for user interaction and processing.

 ![Internal Processing and Python Interaction](images/tutorials/basicmechanics/with.png "Internal Processing and Python Interaction")

### Benefits of Macro Modules
* **Encapsulation:** 
Macro modules take an existing network of modules or Python code. To the user interacting with the macro module, it appears as a single entity with its own defined inputs, outputs, and parameters. You don't need to know or interact with the internal functionality unless you specifically open the macro module for editing.
* **Reusability:**
Once created, macro modules can be easily added to different networks, saving time and effort in rebuilding common processing pipelines. See below for the scope of a macro module. It can be local or global.
* **Organization and Clarity:**
Macro modules help to structure complex networks, making them easier to understand, maintain, and debug. By encapsulating a set of modules into one, you reduce visual clutter and focus on the higher-level workflow.
* **Simplified Interface:**
The interface of a macro module can be more compact and user-friendly than the combined interfaces of all the modules within it. You can expose only the necessary parameters and inputs/outputs.
* **Abstraction of Complexity:**
Users of a macro module don't need to know the details of its internal workings. They interact with it through its well-defined interface.
* **Custom Functionality:**
Macro modules allow you to create custom modules tailored to your specific needs by combining and configuring existing MeVisLab functionalities.
* **GUI Development:**
They are often used to encapsulate dynamic user interfaces built with scripting, sometimes without any underlying image processing network.

### Scope of Macro Modules 

#### Local Macro Module
A Local Macro module in MeVisLab exists within the context of the current network document - i.e., it’s defined *locally* rather than being installed into the global module database. It does not require a package. It lives inside the directory of the current network file (*.mlab*) you’re working on.

*	A local macro is visible and editable in the directory of your current network.
*	A local macro is not listed in the Modules panel and module search.
*	A local macro can only be reused elsewhere by copying it into another folder with your network file.

#### Global Macro Module
 A global macro module is stored in a central location within your MeVisLab installation. The directory is called Package. Once a global macro module is created, it appears in the module browser and can be used in any MeVisLab network you open. See [Package creation](tutorials/basicmechanisms/macromodules/package/) for details about Packages.

 Local macro modules can be converted to global macro modules. MeVisLab then adds a definition file containing the name and package of the module and copies the content to your selected package directory. Package directories are loaded automatically when you start MeVisLab in the case they have been added to your user packages via main menu {{< menuitem "Edit" "Preferences" "Packages" >}}.

*	A global macro can be used in any MeVisLab network.
*	A global macro is listed in the Modules panel and module search.
   
{{<alert class="info" caption="Info">}}
Packages are the way MeVisLab organizes different development projects. You can organize your own modules, test cases, or C++ modules in a package.
{{</alert>}} 

### Inputs, Outputs, and Parameter Fields
Macro modules can have input and output connectors that receive data and/or provide the results of the processing performed by their internal networks or Python scripts.

They are typically defined in the macro module's *.script* file.

#### Inputs
Input connectors accept data from other modules in the network. These inputs define what information the encapsulated network or Python script within the macro module receives and processes.

Data input connectors, represented by triangles for ML images, half-circles for Open Inventor scenes, or squares for Base objects, receive data objects from other modules. The type of data an input accepts is determined by the modules within the macro that are connected to this input.

#### Outputs
Output connectors provide the results of the processing performed by their internal networks. These outputs can then be connected to the inputs of other modules.

Data Outputs (triangle, half-circle, square) provide the processed data from the internal network or Python file. The type of data an output provides depends on the outputs of the modules within the macro that are connected to this output.

#### Parameter Fields
Parameter Fields allow users to control the behavior of the internal network. They can be connected to the parameters/fields of other modules or manually adjusted by the user. They also allow other modules to read values or states from within the encapsulated network or Python file. 

You have two options when adding fields to your macro module:

* **Define your own fields:** You can define your own fields by specifying their name, type, and default value in the *.script* file. This allows you to provide custom parameters for your macro module, tailored to your specific needs. These parameters can be use as input from the user or output from the modules processing.
* **Reuse fields from the internal network:**  Instead of defining your own field, you can expose an existing field from one of the modules of your internal network. To do this, you reference the <attribute>internalName</attribute> of the internal field you want to reuse. This makes the internal field accessible at the macro module level, allowing users to interact with it directly without duplicating parameters. Changes of the field value are automatically applied in your internal network.

![Inputs, Outputs, and Fields](images/tutorials/basicmechanics/fields.png "Inputs, Outputs, and Fields")

### Files Associated with a Macro Module
Macro modules typically need the following files:
* **Definition file (*.def*):** The module definition file contains the definition and information about the module like name, author, or package. **Definition files are only available for global macro modules**.
* **Script file (*.script*):** The script file defines inputs, outputs, parameter fields, and the user interface of the macro module. In the case you want to add Python code, it includes the reference to the Python file. The *.script* file allows you to define short Python functions to be called on field changes and user interactions.

![user interface and the internal interface](images/tutorials/basicmechanics/mycountourFilter.png "user interface and the internal interface")

* **Python file (*.py*):** *(Optional)* The Python file contains the Python code that is used by the module. See section [Python functions and Script files](tutorials/basicmechanisms/macromodules#PythonAndScripts) for different options to add Python functions to user interactions.
* **Internal network file (*.mlab*):** *(Optional)* Stores the internal network of the module if available. This file essentially defines the macro module's internal structure and connections.
* **Macro module help file (*.mhelp*):** *(Optional)* Provides help documentation for the macro module. This file is used to display information to users about the module’s functionality, usage, and any specific instructions.

Additionally, a macro module may provide an additional Python (*.py*) and network (*.mlab*) that defines your automated test(s). Both files are also stored in your Package and can only be added for global macro modules.

### Python Functions and Script Files {#PythonAndScripts}
Python functions can be executed on any user interaction with your macro module. Examples are:
* **Module initialization**: You can add the *initCommand* to the *Commands* section and the given Python function is called whenever the module is added to the workspace or reloaded.
* **Window creation**: You can add the *initCommand* to the *Window* section and the given Python function is called whenever the panel of the module is opened.
* **User interaction**: You can add commands to any user interface element like *Buttons* to call Python functions on user interactions with this element. The image below shows you the user interface and the internal interface.
* **Field changes**: You can also react on any changes of fields in your module and create field listeners. See section [Field Listeners](tutorials/basicmechanisms/macromodules#FieldListeners) for details.

### Field Listeners {#FieldListeners}
Field listeners are mechanisms to execute Python code automatically any time the value of a field changes. This allows you to create dynamic responses to user interactions in the module's parameter panel.

You can define field listeners within the *Commands* sections of the *.script* file. You get a reference to the field object and then use a method to add a callback function that will be executed when the field's value is modified.

For an example see [Example 2.5.2: Module interactions via Python scripting](tutorials/basicmechanisms/macromodules/scriptingexample2/).

## Summary
* Macro modules allow you to add your own functionality to MeVisLab. You can add inputs and outputs and connect existing modules to your new macro module.
* Macro modules may contain an internal network to encapsulate this functionality or Python code to implement your own functionalities to MeVisLab.
* Benefits are encapsulation, reusability, abtraction of complexity, and the possibility to add your own functionality to MeVisLab.
* There are different types of macro modules:
	*	Local macro modules are only available in the directory of your current network.
	*	Global macro modules are available in all projects but must be part of a package.