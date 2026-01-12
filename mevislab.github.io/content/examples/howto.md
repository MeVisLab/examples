---
title: "Using provided examples"
date: 2022-06-15T08:56:33+02:00
draft: false
status: "OK"
menu: 
  main:
    identifier: "how_to_examples"
    weight: 649
    parent: "examples"
---
### Structure

Each tutorial chapter was used as an umbrella theme to structure related examples that are linked in a list. 
After clicking any of the linked examples, you will be forwarded to a short description of the feature and have the option to download the resource that produces your desired effect.

The provided files are usually either *.mlab* files or *.zip* archives. You will find a short tutorial on how to add those files into your MeVisLab application to work with them below.

### MeVisLab (\*.mlab) files
MeVisLab files are networks stored as *.mlab* files. <br>

{{<alert class="info" caption="Info">}}
Double-clicking the left mouse button within your MeVisLab workspace works as a shortcut to open files. 
{{</alert>}}

Files can also be opened using the menu option {{< menuitem "File" "Open">}}.

### Archives (\*.zip files)
Archives mostly contain macro modules. <br>
To use those macro modules, you will need to know how to handle user packages. 

{{<alert class="check" caption="Check">}}
See [Example 2.1: Package creation](/tutorials/basicmechanisms/macromodules/package/) for more information on packages in MeVisLab.
{{</alert>}}

The contents can be extracted into the directory of your package. Make sure to keep the directory's structure for the examples to be loaded and displayed correctly.

The typical directory structure of a MeVisLab package looks like this:
![Package directory structure](/images/examples/howto_1.png "Package directory structure")

The package *TutorialSummary* within the package group *MeVis* is shown above. A package typically contains at least a *Projects* directory, which is where the macro modules are located. When extracting the contents of a *.zip* file, the *Projects* folder of your package should be the target directory.

Sometimes we even provide test cases. Extract them into the *TestCases* directory.
![Package directory structure](/images/examples/howto_2.png "Package directory structure")

{{<alert class="info" caption="Notice">}}
Feel free to create certain directories if they do not exist yet, but make sure to name them conforming the directory structure shown above.
{{</alert>}}

Continuing on your MeVisLab workspace: You might need to reload the module cache after adding macro modules out of *.zip* archives for them to be displayed and ready to be used. To do so, open {{< menuitem "Extras" "Reload Module Database (Clear Cache)" >}}.

### Python (\*.py) or Script (\*.script) Files
In the rare case that a *.py* or *.script* file is provided, make sure to firstly follow the tutorials related to macro modules and test cases. 

{{<alert class="warning" caption="Warning">}}
The integration of Python scripts might not add a lot of value for someone that lacks the knowledge conveyed by the tutorials.
{{</alert>}}


