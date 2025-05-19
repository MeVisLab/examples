---
title: "Example 2: Macro modules and Module Interaction"
date: 2025-05-19
draft: false
weight: 370
status: "OK"
tags: ["Beginner", "Tutorial", "Macro", "Macro modules"]
menu: 
  main:
    identifier: "macro_modules"
    title: "Examples for Creating Macro modules, adding User Interfaces and Python scripting."
    weight: 370
    parent: "basicmechanisms"
---

# Example 2: Macro modules {#TutorialChapter6}

## Macro Module 
A macro module can be used to develop your own functionality in MeVisLab. You have two main options for how to use it:

* **With Internal Networks**: Use a macro module to reuse a network of modules. For example, if you build a network that applies a specific image filter and you want to use this setup in multiple projects, you can wrap the entire network into a single macro module. This way, you don’t need to manually reconnect all the individual modules each time — you just use your macro module. You can see the internal network at the left side of the image below. You can see an example in [Basic Mechanics of MeVisLab (Example: Building a Contour Filter)](/tutorials/basicmechanisms#TutorialMacroModules).

* **Without Internal Networks**: Use a macro module to add your own Python code. If MeVisLab is missing a specific functionality, you can write your own Python script and include it in a macro module.
 This allows you to extend the software with custom behavior that integrates smoothly into your project. You can see the Python code at the right side of the image.


You can combine both approaches: have a macro module containing a module network, and additionally Python code to add your own logic or functionality:

 ![Internal Processing and Python Interaction](/images/tutorials/basicmechanics/with.png "Internal Processing and Python Interaction")

### Benefits:

* **Encapsulation:** 
It takes an existing network of modules or Python code. To the user, interacting with the macro module, it appears as a single entity with its own defined inputs, outputs, and parameters. You don't need to know or interact with the internal functionality unless you specifically open the macro module for editing.
* **Reusability:**
 Once you've created a macro module, you can easily add it to any other MeVisLab network, just like any built-in module. This promotes modularity and avoids the need to rebuild common processing pipelines repeatedly. For example, if you have a standard preprocessing pipeline for medical images, you can encapsulate it into a macro module and reuse it across different projects.
* **Simplified Interface:**
 Often, a macro module will expose a simplified and more focused interface compared to the combined interfaces of all the modules within it. You can choose which inputs, outputs, and parameters of the internal network are exposed at the macro module's level. This makes it easier to use for specific tasks without being overwhelmed by too many options.

 ### Key characteristics:
* **Implementation:**
Macro modules are primarily defined using the MeVisLab Definition Language (MDL) and often incorporate Python scripting for more dynamic behavior. You don't need to write C++ code to create a macro module.
* **User Interface:**
  You can define your own User Interface for macro modules using MDL.
* **Scope:**
Macro modules can be either global (available in all your MeVisLab projects) or local (specific to the current network you are working on).

### Types of Macro modules: 
#### Local Macro module:
A Local Macro in MeVisLab is a macro module that exists only within the context of the current network document - i.e. it’s defined *locally* rather than being installed into the global module database. It does not require a package, it lives only inside the current network file (.mlab) you’re working on.

*	A local macro is visible and editable only in the current network.
*	A local macro is not listed in the Modules panel and module search.
*	A local macro can only be reused elsewhere by copying it into another folder with your network file.

#### Global Macro module:
 A global macro module is stored in a central location within your MeVisLab installation's module directories (or a custom path) called Package. Once created, it appears in the module browser and can be used in any MeVisLab network you open. See [Package creation](/tutorials/basicmechanisms/macromodules/package/) for details about Packages.

*	A global macro can be used in any MeVisLab network.
*	A global macro is listed in the Modules panel and module search.
   
{{<alert class="info" caption="Info">}}
Packages are the way MeVisLab organizes different development projects. You can organize your own modules, test cases or C++ modules in a package.
{{</alert>}} 

### Inputs, Outputs, and Fields:
You can add inputs and outputs to your macro module to connect it with the other modules:
* **Inputs:** These are connection points through which the module receives data from other modules. You define inputs in the *\*.script* file using the Input keyword. You can also define the type for each input.
* **Outputs:** These are connection points through which the module sends processed data to other modules. You define outputs in the *\*.script* file using the Output keyword. You can also define the type for each output.

You can add fields to your macro module. Fields allow you to change parameters for your module or to see the values of results. Fields can also be added to the panel of the macro module so that the user can change them.
* **Fields:** These are parameters that control the module's behavior, typically visible in the module's panel or in the Module Inspector. You define fields in the *\*.script* file using the Field keyword, specifying the data type, default value, and other properties.
The below figure shows the input, output and fields:
![Inputs, Outputs, and Fields](/images/tutorials/basicmechanics/fields.png "Inputs, Outputs, and Fields")

### Files Associated with a Macro Module:
Macro modules typically contain the following files:
* **Definition file (*\*.def*):** The module definition file contains the definition and information about the module like name, author, package, etc. **Definition files are only available for global macro modules**.

* **Script file (*\*.script*):** The script file defines inputs, outputs, fields and the user interface of the macro module. In case you want to add Python code, it includes the reference to the Python script file. The *\*.script* file allows you to define Python functions to be called on field changes and user interactions.

  * **Module Initialization**: You can add the *initCommand* to the *Commands* section and the given Python function is called whenever the module is added to the workspace or reloaded.
  * **Window creation**: You can add the *initCommand* to the *Window* section and the given Python function is called whenever the panel of the module is opened.
  * **User interaction**: You can add commands to any user interface element like *Buttons* to call Python functions on user interactions with this element. The image below shows you the user interface and the internal interface:
  ![user interface and the internal interface](/images/tutorials/basicmechanics/mycountourFilter.png "user interface and the internal interface")

  * **Field changes**: You can also react on any changes of fields in your module and create Field Listeners. See below for details.
* **Python file (*\*.py*):** *(Optional)*: The Python file contains the Python code that is used by the module. You can add Python functions to fields or UI elements to react on user interactions in the *\*.script* file.

### Field Listeners:
Field listeners are mechanisms to execute Python code automatically when the value of a field changes. This allows you to create dynamic responses to user interactions in the module's parameter panel.

You create field listeners within the *Commands* sections of the *\*.script* file. You get a reference to the field object and then use a method to add a callback function that will be executed when the field's value is modified.

For an example see [Example 2.5.2: Module interactions via Python scripting](/tutorials/basicmechanisms/macromodules/scriptingexample2/).

## Summary
* Macro Module: a custom block in MeVisLab used to group a network of modules or custom Python code into a single reusable unit. 

* Benefits:
	* Organized structure.
	*	Easy to reuse across projects.
	*	Simplified user interface.

* Types:
	*	Local: Only available in the current network, not shown in the module browser.
	*	Global: Available in all projects, must be part of a package.

* Files
	*	(*\*.script*): Defines inputs, outputs, fields, and user interface.
	*	(*\*.py*): Contains Python code.
	*	(*\*.def*): Definition file (only for global macros).
  *	(*\*.mlab*): Stores the internal network of modules within the macro module.
  * (*\*.mhelp*): Provides documentation or user assistance for the module.

* Components
	*	Inputs/Outputs: For connecting the module with other modules. 
	*	Fields: Parameters for user control
	*	Field Listeners: Run Python code when a field value changes

* Packages: are the way MeVisLab organizes different development projects. Required for global macros.