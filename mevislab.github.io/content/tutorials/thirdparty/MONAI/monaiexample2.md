---
title: "Example 2: Applying a spleen segmentation model from MONAI in MeVisLab"
date: 2025-11-13
status: "OK"
draft: false
weight: 879
tags: ["Advanced", "Tutorial", "MONAI", "Python", "PythonPip", "AI"]
menu: 
  main:
    identifier: "monaiexample2"
    title: "Applying a spleen segmentation model from MONAI in MeVisLab."
    weight: 879
    parent: "monai"
---
# Example 2: Applying a spleen segmentation model from MONAI in MeVisLab

## Introduction
In the following, we will perform a spleen segmentation using a model from the *MONAI Model Zoo*. The MONAI Model Zoo is a collection of pre-trained models for medical imaging, offering standardized bundles for tasks like segmentation, classification, and detection across MRI, CT, and pathology data, all built for easy use and reproducibility within the MONAI framework. Further information and the required files can be found [here](https://github.com/Project-MONAI/model-zoo/tree/dev "here").

This example shows how to use the model for **Spleen CT Segmentation** directly in MeVisLab.

## Steps to do
### Download necessary files
Create a folder named *spleen_ct_segmentation* somewhere on your system.
Inside this folder, create two subfolders, one named *configs* and another named *models*  and remember their paths.

![Directory Structure](/images/tutorials/thirdparty/monai_example2_1.png "Directory Structure").

Download all *config* files from [MONAI-Model-Zoo](https://github.com/Project-MONAI/model-zoo/tree/dev/models/spleen_ct_segmentation/configs "MONAI Model-Zoo") and save them in your local *configs* directory.


Download *model* files from [NVIDIA Download Server](https://developer.download.nvidia.com/assets/Clara/monai/tutorials/model_zoo/model_spleen_ct_segmentation_v1.pt "NVIDIA Download Server") and save it in your local *models* directory.

{{<alert class="info" caption="Additional information">}}
The path to the latest model \**.pt*-file can be found in [large_files.yml](https://github.com/Project-MONAI/model-zoo/blob/dev/models/spleen_ct_segmentation/large_files.yml "large_files.yml").
{{</alert>}}

### Download example images
The recommended CT images used for training the algorithm, can be found [here](https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar "here").

### Create a macro module and add inputs and outputs
Add a `PythonImage` module and save the network as *MONAISpleenSegmentation.mlab*.

![PythonImage module](/images/tutorials/thirdparty/monai_example2_1a.png "PythonImage module").

Now, right-click {{< mousebutton "right" >}} on the `PythonImage` module, select {{< menuitem "“Grouping”" "Add to new Group">}}, and name the group *MONAIDemo*.

Right-click {{< mousebutton "right" >}} on the group's name and choose *Convert to Local Macro* using the same name.

Our new module does not provide an input or output.

![Local Macro Module MONAIDemo](/images/tutorials/thirdparty/monai_example2_2.png "Local Macro Module MONAIDemo")

Right-click {{< mousebutton "right" >}} on the Macro Module and select {{< menuitem "Related Files" "MONAIDemo.script">}}.

Add the following code into the \**.script*-file and save.

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  Inputs {
    Field inputImage { type = Image }
  }
  Outputs {
    Field outImage { internalName = PythonImage.output0 }
  }
  Parameters {
    Field start { type = Trigger }
  }
}
```
{{</highlight>}}

If you now reload your module in MeVisLab, you can see the new in- and output.

![MONAIDemo with in- and output](/images/tutorials/thirdparty/monai_example2_3.png "MONAIDemo with in- and output")

Add a *Commands* section to your \**.script*-file.

{{< highlight filename="MONAIDemo.script" >}}
```Stan
...
Commands {
  source = $(LOCAL)/MONAIDemo.py
}
...
```
{{</highlight>}}

Right-click {{< mousebutton "right" >}} on the MONAIDemo.py and select {{< menuitem "Open File $(LOCAL)/MONAIDemo.py">}}. An empty Python file is created and opens automatically. Save the empty Python file.

### Create the network for the segmentation
Right-click {{< mousebutton "right" >}} on the Macro Module and select {{< menuitem "Related Files" "MONAIDemo.mlab">}}. Create the network seen below.

![MONAIDemo Network](/images/tutorials/thirdparty/monai_example2_3a.png "MonaiDemo Network")

Fields of the internal network can be left default, we will change them later.

The left part defines actions executed on the input image, the right part defines what shall happen on the output after the *MONAI* segmentation has been done. A detailed descripion will be provided later.

Open your *\*.script* file via right-click {{< mousebutton "right" >}} on the Macro Module and select {{< menuitem "Related Files" "MONAIDemo.script">}}.

Define your input image field to re-use the internal name of the left input of the `Resample3D` module.

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  Inputs {
    Field inputImage { internalName = Resample3D.input0 }
  }
  ...
}
```
{{</highlight>}}

If you now open the internal network of your macro module, you can see that the input image is connected to the input of the `Resample3D` module.

![MONAIDemo Internal Network](/images/tutorials/thirdparty/monai_example2_3b.png "MonaiDemo Internal Network")

Again open the *\*.script* file and change the internal name of your *outImage* field to re-use the field *Resample3D1.output0*.

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  ...
  Outputs {
    Field outImage { internalName = Resample3D1.output0 }
  }
  ...
}
```
{{</highlight>}}


If you now open the internal network of your macro module, you can see that the output image is connected to the output of the `Resample3D1` module.

![MONAIDemo Internal Network](/images/tutorials/thirdparty/monai_example2_3c.png "MonaiDemo Internal Network")

### Adapt input image to *MONAI* parameters from training
The model has been trained for strictly defined assumptions for the input image. All values can normally be found in the *inference.json* file in your *configs* directory.

Use the `itkImageFileReader` module to load the file *Task09_Spleen/Task09_Spleen/imagesTr/spleen_7.nii.gz* from dowloaded example patients. The *Output Inspector* shows the image and additional information about the size.

We can see that the image size is 512 x 512 x 114 and the voxel size is 0.9766 x 0.9766 x 2.5.

![Output Inspector](/images/tutorials/thirdparty/monai_example2_3d.png "Output Inspector")

Connect the module to your local macro module `MonaiDemo`. The result of the segmentation shall be visualized as a semi-transparent overlay on your original image.

Add a `SoView2DOverlay` and a `View2D` module and connect them to your local macro module `MonaiDemo`.

![Final network](/images/tutorials/thirdparty/monai_example2_4.png "Final network")

The **Spleen CT Segmentation** network expects images having a defined voxel size of 1.5 x 1.5 x 2. We want to define these values via fields in the Module inspector.

Open the *\*.script* file and add the fields *start* and *voxelSize* to your local macro module `MonaiDemo`:

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  ...
  Parameters {
    Field start { type = Trigger }
    Field voxelSize { internalName = Resample3D.voxelSize }
  }
  ...
}
```
{{</highlight>}}

If you reload your module now, we can set the voxel size to use for the segmentation directly in our macro module `MonaiDemo`. Additionally we can trigger a start function for running the segmentation. This is implemented later.

![Voxel Size](/images/tutorials/thirdparty/monai_example2_4a.png "Voxel Size")

If you select the output field of the `Resample3D` module in the internal network, you can see the dimensions of the currently opened image after changing the voxel size to 1.5 x 1.5 x 2. It shows 333 x 333 x 143.

![Original Image Size](/images/tutorials/thirdparty/monai_example2_5.png "Original Image Size")

The algorithm expects image sizes of 160 x 160 x 160. We add this expected size of the image to our macro module in the same way.

Open the *\*.script* file and add the following fields to your local macro module `MonaiDemo`:

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  ...
  Parameters {
    ...
    Field sizeX { type = Int }
    Field sizeY { type = Int }
    Field sizeZ { type = Int }
    ...
  }
  ...
}
```
{{</highlight>}}

Reload your macro module and enter the following values for your new fields:
* sizeX = 160
* sizeY = 160
* sizeZ = 160

Next, we change the grey values of the image, because the algorithm has been trained on values between -57 and 164. Again, the values can be found in the *inference.json* file in your *configs* directory.

Open the *\*.script* file and add the following fields to your local macro module `MonaiDemo`:

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  ...
  Parameters {
    ...
    Field thresholdMin { internalName = IntervalThreshold.threshMin }
    Field thresholdMax { internalName = IntervalThreshold.threshMax }
    ...
  }
  ...
}
```
{{</highlight>}}

As already done before, we can now defined the threshold values for our module via Module Inspector. Set the following:
* thresholdMin = -57
* thresholdMax = 164

As defined in the *inference.json* file in your *configs* directory, the grey values in the image must be between 0 and 1.

Open the *\*.script* file and add the following fields to your local macro module `MonaiDemo`:

{{< highlight filename="MONAIDemo.script" >}}
```Stan
Interface {
  ...
  Parameters {
    ...
    Field scaleMin { internalName = Scale.outputMin }
    Field scaleMax { internalName = Scale.outputMax }
    ...
  }
  ...
}
```
{{</highlight>}}

Set the following:
* scaleMin = 0
* scaleMax = 1

The algorithm expects NumPy images. NumPy uses the order Z, Y, X, other than MeVisLab. We are using X, Y, Z. The image needs to be transformed.

Open the panel of the `SwapFlipDimensions` module and select X as *Axis 1* and Z as *Axis 2*. 

![SwapFlipDimensions](/images/tutorials/thirdparty/monai_example2_11.png "SwapFlipDimensions")

After the algorithm has been executed, we have to flip the images back to the priginal order. Open the panel of the `SwapFlipDimensions1` module and select X as *Axis 1* and Z as *Axis 2*. 

Finally we want to show the results o the algorithm as a semi-transparent overlay on the image. Open tha panel of the `View2DOverlay` and define the following settings:
* Blend Mode: Blend
* Alpha Factor: 0.5
* Base Color: red

![View2DOverlay](/images/tutorials/thirdparty/monai_example2_12.png "View2DOverlay")

### Field Listeners
We add some Field Listeners to our Commands section of the *\*.script* file. They are necessary to react on changes the user does on the fields of our module.

{{< highlight filename="MONAIDemo.script" >}}
```Stan
...
Commands {
  source = $(LOCAL)/MONAIDemo.py
  
  FieldListener start {
    command = onStart
  }
  
  FieldListener sizeX {
    command = _sizeChanged
  }
  
  FieldListener sizeY {
    command = _sizeChanged
  }
  
  FieldListener sizeZ {
    command = _sizeChanged
  }
  
  FieldListener inputImage {
    command = _setDefaultValues
  }
}
...
```
{{</highlight>}}

If the user touches the trigger *start*, a Python function *onStart* will be executed. Whenever the size of our image is changed, we call a function called *_sizeChanged* and if the input image changes, we want to reset the module to its default values.

### Python scripting
The next step is to write our Python code. 

Right-click {{< mousebutton "right" >}} *MONAIDemo.py* in *Commands* section line *source*. MATE opens showing the *\*.py* file of our module.

Insert the following code:

{{< highlight filename="MONAIDemo.py" >}}
```Python
import torch
import numpy as np
import mevislab
from monai.bundle import load_bundle_config

# Paths
MODEL_DIR = r"C:\tmp\spleen_ct_segmentation"
MODEL_PATH = MODEL_DIR + r"\models\model_spleen_ct_segmentation_v1.pt"
TRAIN_JSON = MODEL_DIR + r"\configs\train.json"

# using cpu or cude
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def onStart():
    print("\n--- Start ---")

def _setDefaultValues():
    print("\n--- Reset ---")

def _getImage():
    print("\n--- Get Image ---")

def _sizeChanged():
    print("\n--- Size Changed ---")

```
{{</highlight>}}

These functions should be enough to run th module. You can try them by changing the input image of our module, by changing any of the size values in *Module Inspector* or by clicking *start*.

Lets implement the *_getImage* function first:

{{< highlight filename="MONAIDemo.py" >}}
```Python
...
  def _getImage():
    if ctx.field("SwapFlipDimensions.output0").isValid():
        # Get image after all modifications have been done
        image = ctx.field("SwapFlipDimensions.output0").image()

        return image
    else:
        return None
...
```
{{</highlight>}}

We want to use the image that has been modified according to our pre-trained network requirements discussed above. We use the output image of the `SwapFlipDimensions` module when clicking *start*.

{{< highlight filename="MONAIDemo.py" >}}
```Python
...
  def onStart():
    print("\n--- Start ---")
    try:
        inputImage = _getImage()

        if inputImage:
            imageArray = inputImage.getTile(
                (0, 0, 0, 0, 0, 0), inputImage.imageExtent()
            )
            # We only need x, y and z-dimensions
            image = imageArray[0, 0, 0, :, :, :]

            print(f"Using image {image.shape}")

            # prepare tensor
            inputTensor = torch.tensor(image[None, None, :, :, :]).to(DEVICE)
            print(f" Tensorform: {tuple(inputTensor.shape)}")
            # Load Bundle-Configuration
            parser = load_bundle_config(MODEL_DIR, "train.json")

            # Create network from train.json
            model = parser.get_parsed_content("network_def")
            model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
            model.to(DEVICE)
            model.eval()
            print("Model loaded and initialized.")

            # Inference
            with torch.no_grad():
                output = model(inputTensor)
                prediction = output.argmax(dim=1, keepdim=True).cpu().numpy()[0, 0]

            print("Inference done.")

            # Result back into MeVisLab
            interface = ctx.module("PythonImage").call("getInterface")
            interface.setImage(
                prediction, voxelToWorldMatrix=inputImage.voxelToWorldMatrix()
            )

            print("--- Segmentation done ---\n")

    except Exception as e:
        print("Error:", e)
        import traceback

        traceback.print_exc()
...
```
{{</highlight>}}

This function now already calculates the segmentation using the *MONAI* model. The problem is, that it may happen that our sub image with the size 160 x 160 x 160 is located somewhere in our original image, where no spleen is visible.

We have to calculate a bounding box in our `ROISelect` module and need to be able to move this bounding box to the correct location.

{{< highlight filename="MONAIDemo.py" >}}
```Python
...
  def _sizeChanged(field: "mevislab.MLABField"):
    if ctx.field("Resample3D.output0").isValid():
        voxelSizeImage = ctx.field("Resample3D.output0").image()
        # Get the size of this image
        voxelSizeImageExtent = voxelSizeImage.imageExtent()

        # Calculate region of interest by defining start point and size
        roiStartX = voxelSizeImageExtent[0] - ctx.field("sizeX").value
        roiStartY = voxelSizeImageExtent[1] - ctx.field("sizeY").value
        roiStartZ = voxelSizeImageExtent[2] - ctx.field("sizeZ").value

        ctx.field("ROISelect.startVoxelX").value = roiStartX
        ctx.field("ROISelect.startVoxelY").value = roiStartY
        ctx.field("ROISelect.startVoxelZ").value = roiStartZ

        # Subtract 1 because the pixel values start with 0
        ctx.field("ROISelect.endVoxelX").value = voxelSizeImageExtent[0] - 1
        ctx.field("ROISelect.endVoxelY").value = voxelSizeImageExtent[1] - 1
        ctx.field("ROISelect.endVoxelZ").value = voxelSizeImageExtent[2] - 1
...
```
{{</highlight>}}

Whenever our size fields are modified, the bounding box is re-calculated using the size of the given image and the values of the sizes defined by the user. The calculated bounding box is not positioned. This needs to be done manually, if necessary.

Open the *\*.script* file and add a *Window* section. In this window, we re-use the panel of the `ROISelect` module to manually correct the location of our calculated bounding box.

{{< highlight filename="MONAIDemo.script" >}}
```Stan
...
Window {
  height = 100
  width = 100
  Category {
    Viewer ROISelect.scene.self {
      type = SoRenderArea
      expandX = True
      expandY = True
    }
  }
}
...
```
{{</highlight>}}

If you now open the panel of our `MONAIDemo` module, we can manually move the box in all three dimensions.

![MONAIDemo panel](/images/tutorials/thirdparty/monai_example2_5.png "MONAIDemo panel").

Back to Python, we now need to reset our module to default,m in case the input image changes. This also removed previous segmentations from the `PythonImage` module.

{{< highlight filename="MONAIDemo.py" >}}
```Python
...
  def _setDefaultValues():
    ctx.field("voxelSize").value = [1.5, 1.5, 2]
    ctx.field("sizeX").value = 160
    ctx.field("sizeY").value = 160
    ctx.field("sizeZ").value = 160
    ctx.field("thresholdMin").value = -57
    ctx.field("thresholdMax").value = 164
    ctx.field("scaleMin").value = 0
    ctx.field("scaleMax").value = 1

    interface = ctx.module("PythonImage").call("getInterface")
    interface.unsetImage()
...
```
{{</highlight>}}

## Execute the segmentation
If you now load an image using the `itkImageFileReader` module, you can manually adapt your bounding box to include the spleen ans start segmentation.

The results are shown as a sem-transparent overlay.

![Segmentation result](/images/tutorials/thirdparty/monai_example2_6.png "Segmentation result").

You can also use the other examples from *MONAI Model Zoo* the same way, just make sure to apply necessary changes on the input images like size, voxel size and other parameters defined in the *inference.json* file of the model.

## Summary
* Pre-trained *MONAI* networks can be used directly in MeVisLab via `PythonImage` module
* The general principles are always the same for all models

{{< networkfile "examples/thirdparty/monai/MONAIDemo.zip" >}}

