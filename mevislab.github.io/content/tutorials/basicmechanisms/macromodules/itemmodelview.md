---
title: "Example 7: Creating you own ItemModel by using the ItemModelView"
date: 2025-06-03
status: "OK"
draft: false
weight: 465
tags: ["Advanced", "Tutorial", "ItemModel", "ItemModelView"]
menu: 
  main:
    identifier: "itemmodel"
    title: "Creating your own ItemModel by using the ItemModelView"
    weight: 465
    parent: "basicmechanisms"
---
# Example 7: Creating your own ItemModel by using the ItemModelView

## Introduction
In this example, we will show how to use the *ItemModelView* MDL control to represent an abstract hierarchical item model with generically named attributes. You will see how to select the displayed attributes in the resulting table and how to interact with this table.

We create a macro module that receives an input image and then showing some selected DICOM attributs of this patient in our own *ItemModelView*.

## Prepare your network

### Create a Macro Module
{{<alert class="info" caption="Info">}}
Make sure to create a package first. Packages are the way MeVisLab organizes different development projects. You can find an example in chapter [Package creation](/tutorials/basicmechanisms/macromodules/package/).
{{</alert>}} 

Use the *Project Wizard* via menu entry {{< menuitem "File" "Run Project Wizard ..." >}} to create a new macro module named `MyItemModelView`.

Start with an empty network and add a Python file.

We can leave the *Fields* empty for now. We can add them in the *\*.script* file.

Click *Create* {{< mousebutton "left" >}}.

{{< imagegallery 3 "/images/tutorials/basicmechanics" "ItemModel_1" "ItemModel_2" "ItemModel_3">}}

If you cannot find your module via *Module Search*, reload module cache by clicking the menu item {{< menuitem "Extras" "Reload Module Database (Clear Cache)" >}}

### Define the necessary fields
Add your new module `MyItemModelView` to your workspace. It does not provide a user interface and you do not have any *Fields* available.

![Empty Module](/images/tutorials/basicmechanics/ItemModel_4.png "Empty Module")

Open the *\*.script* file of your module via right-click {{< mousebutton "right" >}} and {{< menuitem "Related Files (4)" "MyItemModelView.script" >}}.

We first define the input for the image.
{{< highlight filename="MyItemModelView.script" >}}
```Stan
Interface {
  Inputs {
    Field inImage            { type = Image  }
  }
  Outputs {}
  Parameters {}
}
```
{{</highlight>}}

Then, we define all attributes of the input image we want to use in our *ItemModel*.
* **Patient**
  * PatientName
  * PatientBirthDate
  * **Study**
    * StudyDescription
    * StudyDate
    * Modality
    * **Series**
      * SeriesDescription
      * SeriesDate
      * **Image**
        * SOPInstanceUID

All of them have to be defined as a *Field* in the *Parameters* section of the script.

{{< highlight filename="MyItemModelView.script" >}}
```Stan
Interface {
  Inputs {
    Field inImage            { type = Image  }
  }
  Outputs {}
  Parameters {
    Field id                 { type = Int    }
    Field patientName        { type = String }
    Field patientBirthdate   { type = String }
    Field studyDescription   { type = String }
    Field studyDate          { type = String }
    Field modality           { type = String }
    Field seriesDescription  { type = String }
    Field seriesDate         { type = String }
    Field sopInstanceUID     { type = String }
  }
}
```
{{</highlight>}}

If you now open your panel, you should see the *Input* *inImage* and the just created *Fields*. The *Field* *id* is necessary to identify unique objects in your *ItemModel* later. In order to make this example easier to understand, we defined all types of the *Fields* as *String*. You can also use different types, if you like.

![Module Input and Fields](/images/tutorials/basicmechanics/ItemModel_5.png "Module Input and Fields")

### Add the ItemModelView to your panel
We can now add the *ItemModelView* to our panel and define the columns of the view, that we want to see. Add a *Window* section to your script file and define it as seen below.

{{< highlight filename="MyItemModelView.script" >}}
```Stan
Window {
  Category {
  Vertical {
      ItemModelView myItemModel {
        name                 = itemModelView
        idAttribute          = id
        Column id {}
        Column patientName {}
        Column patientBirthdate {}
        Column studyDescription {}
        Column studyDate {}
        Column modality {}
        Column seriesDescription {}
        Column seriesDate {}
        Column sopInstanceUID {}
      }
    }
  }
}
```
{{</highlight>}}

Every *Field* that we defined in the *Parameters* section is now used as a column in our view. The *Field* *id* has been defined to be the *idAttribute*. If you now open your panel, MeVisLab will complain that you did not define the *Field* *myItemModel*. You have to add a *Field* with this name to your *Parameters* section or as an *Output Field*. We will add an *Output Field*, so that our model can also be used by other modules, if necessary. The type is *MLBase*.

{{< highlight filename="MyItemModelView.script" >}}
```Stan
Outputs {
    Field myItemModel {
        type = MLBase
    }
}
```
{{</highlight>}}

Your module now also shows an output *MLBase* object and the columns you defined for the *ItemModelView*.

![Module Output and Columns](/images/tutorials/basicmechanics/ItemModel_6.png "Module Output and Columns")

### Fill your table with data
We want to get the necessary information from the defined input image *inImage*. We want the module to update the content whenever the input image changes. Therefore we need a *Field Listener* calling a Python function whenever the input image changes. Add it to your *Commands* section.

{{< highlight filename="MyItemModelView.script" >}}
```Stan
Commands {
  source = $(LOCAL)/MyItemModelView.py
  
  FieldListener inImage {
    command = imageChanged
  }
}
```
{{</highlight>}}

Whenever the input image changes, the Python function *imageChanged* is executed. Right-click on the {{< mousebutton "right" >}} *imageChanged* and select {{< menuitem "Create Python Function 'imageChanged'" >}}. MATE automatically opens the Python file and creates the function.

Before implementing the Python function, we have to add necessary imports and global parameters.

{{< highlight filename="MyItemModelView.py" >}}
```Python
import mevislab
from mevis import *

gAttributes = ["Patient Name", "patientBirthdate", "studyDescription", "studyDate", "modality", "seriesDescription", "seriesDate", "sopInstanceUID"]
gModel = None
gNextId = 0
```
{{</highlight>}}

We need *mevis* to use the network context *ctx* in Python. We additionally want to define the attributes of our resulting view.

The unique *id* is an increasing *Integer* and we can now initialize our model.

#### Implement the model
In Python, we have to define some basic classes and functions for our final model. Define a class *MyItem* which represents a single item. Each item may have children of the same type to provide a hierarchical structure.

{{< highlight filename="MyItemModelView.py" >}}
```Python
class MyItem:
    def __init__(self, parent=None):
        self.children = []
        self.parent = parent
        self.data = {}
```
{{</highlight>}}

Now we implement a very simple and basic model named *MyItemModel*. Initially we create a new *MLBase* object using the existing *StandardItemModel* and define the structure of our items as already done using the attributes.

Some additional functions are necessary to get the root item and the selected index of the model. We also need functions to add and insert items and to clear all items.

{{< highlight filename="MyItemModelView.py" >}}
```Python
class MyItemModel:
    def __init__(self):
        self.model = MLAB.createMLBaseObject("StandardItemModel", [["id"] + gAttributes])
        root = MyItem()
        self.root = root
        self.map = {}

    def makeCurrent(self):
        ctx.field("myItemModel").setObject(self.model)

    def getRootItem(self):
        return self.root

    def getSelectedIndex(self):
        ids = [int(x) for x in ctx.field("selection").value.split()]
        if ids:
            return self.model.findFirst("id", ids[0])
        else:
            return None

    def addBefore(self):
        index = self.getSelectedIndex()
        if index:
            parent = self.model.getParent(index)
            pos = self.model.getChildPosition(index)
        else:
            parent = None
            pos = 0
        self.insertItem(parent, pos, True)

    def addChild(self):
        parent = self.getSelectedIndex()
        pos = self.model.getChildCount(parent)
        self.insertItem(parent, pos)

    def insertItem(self, parent, pos, updateSelection=False, data=None):
        self.model.insertItems(parent, pos, data)
        self.map[data["id"]] = data
        if updateSelection:
            ctx.field("selection").value = str(data["id"])

    def updateValues(self):
        index = self.getSelectedIndex()
        if index:
            for attr in gAttributes:
                value = ctx.field(attr).value
                if value != self.model.getData(index, attr):
                    self.model.setData(index, attr, value)

    def clearAll(self):
        self.model.clear()
```
{{</highlight>}}

You can see that the above Python code uses a field *selection* which contains the ID of the selected item in our table. We have to add this *Field* to our *\*.script* file, too.

{{< highlight filename="MyItemModelView.script" >}}
```Stan
Interface {
  ...
  Parameters {
    ...    
    Field selection          { type = String }
    ...
  }
}
Window {
  Category {
    Vertical {
      ItemModelView myItemModel {
        ...
        selectionField       = selection
        ...
      }
    }
  }
}
```
{{</highlight>}}

#### Fill the model with your data
Now, we can implement the function *imageChanged*.

{{< highlight filename="MyItemModelView.py" >}}
```Python
def imageChanged(field: "mevislab.MLABField "):
    global gModel, gNextId
    gModel = MyItemModel()
    gNextId = 0
    gModel.makeCurrent()

    if field.isValid():
        patientName, patientBirthdate, studyDescription, studyDate, modality, seriesDescription, seriesDate, numberOfSlices = _getImageData()
        
        gModel.insertItem(
            None,
            0,
            True,
            {
                "id": getNextId(),
                "patientName": patientName,
                "patientBirthdate": patientBirthdate,
                "studyDescription": studyDescription,
                "studyDate": studyDate,
                "modality": modality,
                "seriesDescription": seriesDescription,
                "seriesDate": seriesDate,
                "sopInstanceUID": "",
            },
        )
        
        tmpSelectedIndex = gModel.getSelectedIndex()
        
        for sliceNumber in range(0, numberOfSlices):
            instanceUid = field.getFrameSpecificDicomTag("SOPInstanceUID", sliceNumber)

            gModel.insertItem(
                tmpSelectedIndex,
                0,
                True,
                {
                    "id": getNextId(),
                    "patientName": "",
                    "patientBirthdate": "",
                    "studyDescription": "",
                    "studyDate": "",
                    "modality": "",
                    "seriesDescription": "",
                    "seriesDate": "",
                    "sopInstanceUID": instanceUid.value(),
                },
            )
```
{{</highlight>}}

Whenever the image changes, we create a new and empty model (*gModel*) and reset the next ID (*gNextId*) to *0*. If the image is valid, we get the image data.

{{< highlight filename="MyItemModelView.py" >}}
```Python
def _getImageData():
    imageField = ctx.field("inImage")
    patientName = imageField.getDicomTagValueByName("PatientName")
    patientBirthdate = imageField.getDicomTagValueByName("PatientBirthDate")
    studyDescription = imageField.getDicomTagValueByName("StudyDescription")
    studyDate = imageField.getDicomTagValueByName("StudyDate")
    modality = imageField.getDicomTagValueByName("Modality")
    seriesDescription = imageField.getDicomTagValueByName("SeriesDescription")
    seriesDate = imageField.getDicomTagValueByName("SeriesDate")
    numberOfSlices = imageField.sizeZ()
    
    return patientName, patientBirthdate, studyDescription, studyDate, modality, seriesDescription, seriesDate, numberOfSlices
```
{{</highlight>}}

The image data is then used to create the root item of our model. We use the selected index of our first entry to walk through all available slices of the image and add the *SOP Instance UID* of each slice as a child object to our root item.

If you now open the panel of your module, you can already see the results.

![Module Panel](/images/tutorials/basicmechanics/ItemModel_7.png "Module Panel")

The first line shows the information of the patient, the study and the series and each child item represents a single slice of the image.

## Interact with your model
We can now add options to interact with the *ItemModelView*. Open the *\*.script* file of your module and go to the *Commands* section. We add a *FieldListener* to our *selection* field. Whenever the user selects a different item in our view, the Python function *itemClicked* in the *FieldListener* is executed.

{{< highlight filename="MyItemModelView.script" >}}
```Stan
Commands {
  ...
  FieldListener selection {
    command = itemClicked
  }
  ...
}
```
{{</highlight>}}

Before adding the new Python function, we need a function in our model that returns the values of items from our model. Implement the function *getItemByID* in our model the following way:

{{< highlight filename="MyItemModelView.py" >}}
```Python
def getItemByID(self, id):
    return self.map[id]
```
{{</highlight>}}

It uses *id* to find the selected item and returns all values of this item.

Now add the Python function of our *FieldListener* to your Python script:

{{< highlight filename="MyItemModelView.py" >}}
```Python
def itemClicked(field: "mevislab.MLABField"):
    columnIndex = 8
    column = gAttributes[columnIndex - 1]
    itemID = int(ctx.field("selection").value)
    data = gModel.getItemByID(itemID)[column]
    print(f"Click: {data}")
```
{{</highlight>}}

The *itemClicked* function uses *id* from the selected item to get the value of column 8 (in this case it is the *SOP Instance UID* of the image) and prints this value.

![Clicked Item](/images/tutorials/basicmechanics/ItemModel_8.png "Clicked Item")

The problem is that the *Field* *selection* also changes whenever a new item is added to the model. Your debug output is already flooded with SOP Instance UIDs without interaction.

![Debug Output](/images/tutorials/basicmechanics/ItemModel_9.png "Debug Output")

Add another global parameter to your Python script to prevent the *FieldListener* from executing during the *imageChanged* event.

{{< highlight filename="MyItemModelView.py" >}}
```Python
...
gInitializing = False
...
def imageChanged(field: "mevislab.MLABField "):
    global gModel, gNextId, gInitializing
    gInitializing = True
    ...
    gInitializing = False


def itemClicked(field: "mevislab.MLABField"):
    if not gInitializing:
        ...
```
{{</highlight>}}

While the *imageChanged* function is executed, the parameter is set to *False* and the *itemClicked* function does not print anything.

## Summary
* *ItemModelViews* allow you to define your own abstract hierarchical item model with generically named attributes
* This model can be provided as Output and added to the Panel of your module
* Interactions with the model can be implemented by using a *FieldListener*.

{{< networkfile "examples/basic_mechanisms/Modules.zip" >}}
