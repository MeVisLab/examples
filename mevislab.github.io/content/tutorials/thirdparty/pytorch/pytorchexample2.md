---
title: "Example 2: Brain Parcellation using PyTorch"
date: 2023-06-30
status: "OK"
draft: false
weight: 873
tags: ["Advanced", "Tutorial", "PyTorch", "Python", "PythonPip", "AI"]
menu: 
  main:
    identifier: "pytorchexample2"
    title: "Brain Parcellation using PyTorch"
    weight: 873
    parent: "pytorch"
---
# Example 2: Brain Parcellation using PyTorch

## Introduction
In this example, you are using a pre-trained PyTorch deep learning model (HighRes3DNet) to perform a full brain parcellation. HighRes3DNet is a 3D residual network presented by Li et al. in [On the Compactness, Efficiency, and Representation of 3D Convolutional Networks: Brain Parcellation as a Pretext Task](https://link.springer.com/chapter/10.1007/978-3-319-59050-9_28).

## Steps to do
Add a `LocalImage` module to your workspace and select the file *MRI_Head.dcm*. For PyTorch it is necessary to resample the data to a defined size. Add a `Resample3D` module to the `LocalImage` and open the panel. Change *Keep Constant* to *Voxel Size* and define *Image Size* as 176, 217, 160.

![Resample3D module](/images/tutorials/thirdparty/pytorch_example2_1.png "Resample3D module").

The coordinates in PyTorch are also a little different than in MeVisLab, therefore you have to rotate the image. Add an `OrthoSwapFlip` module and connect it to the `Resample3D` module. Change *View* to *Other* and set *Orientation* to *YXZ*. Also check *Flip horizontal*, *Flip vertical* and *Flip depth*. *Apply* your changes.

![OrthoSwapFlip module](/images/tutorials/thirdparty/pytorch_example2_2.png "OrthoSwapFlip module").

You can use the Output Inspector to see the changes on the images after applying the resample and a swap or flip.

{{< imagegallery 3 "images/tutorials/thirdparty/" "Original" "Resample3D" "OrthoSwapFlip">}}

Add an `OrthoView2D` module to your network and save the *\*.mlab* file.

![OrthoView2D module](/images/tutorials/thirdparty/pytorch_example2_3.png "OrthoView2D module").

## Integrate PyTorch and scripting
For integrating PyTorch and Python scripting, we need a `PythonImage` module. Add it to your workspace. Right-click {{< mousebutton "right" >}} on the `PythonImage` module and select {{< menuitem "Grouping" "Add to new Group...">}}. Right-click {{< mousebutton "right" >}} your new group and select {{< menuitem "Grouping" "Add to new Group...">}}. Name your new local macro *DemoAI*, select a directory for your project and leave all settings as default.

Our new module does not provide an input or output. 

![DemoAI local macro](/images/tutorials/thirdparty/pytorch_example2_4.png "DemoAI local macro").

### Adding an interface to the local macro
Right-click {{< mousebutton "right" >}} the local macro and select {{< menuitem "Related Files" "DemoAI.script">}}. MATE opens showing the *\*.script* file of our module. Add an input *Field* of type *Image*, an output *Field* using the *internalName* of the output of our `PythonImage` and a *Trigger* to start the segmentation.

You should also already add a Python file in the *Commands* section.

{{< highlight filename="DemoAI.script" >}}
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

Commands {
  source = $(LOCAL)/DemoAI.py
}
```
{{</highlight>}}

In MATE, right-click {{< mousebutton "right" >}} the Project Workspace and add a new file *DemoAI.py* to your project. The workspace now contains an empty Python file.

![Project Workspace](/images/tutorials/thirdparty/pytorch_example2_5.png "Project Workspace").

Change to MeVisLab IDE, right-click {{< mousebutton "right" >}} the local macro and select {{< menuitem "Reload Definition">}}. Your new input and output interface are now available and you can connect images to your module.

![DemoAI local macro with interfaces](/images/tutorials/thirdparty/pytorch_example2_6.png "DemoAI local macro with interfaces").

### Extend your network

We want to show the segmentation results as an overlay on the original image. Add a `SoView2DOverlayMPR` module and connect it to your `DemoAI` macro. Connect the output of the `SoView2DOverlayMPR` to a `SoGroup`. We also need a lookup table for the colors to be used for the overlay. We already prepared a *\*.xml* file you can simply use. Download the [lut.xml](/examples/thirdparty/pytorch2/lut.xml) file and save it in your current working directory of the project. 

Add a `LoadBase` module and connect it to a `SoMLLUT` module. The `SoMLLUT` needs to be connected to the `SoGroup` so that it is applied to our segmentation results.

![Final network](/images/tutorials/thirdparty/pytorch_example2_7.png "Final network").

{{<alert class="info" caption="Info">}}
If your PC is equipped with less than 16GBs of RAM/working memory we recommend to add a `SubImage` module between the `OrthoSwapFlip` and the `Resample3D` module. You should configure less slices in z-direction to prevent your system from running out of memory.

![SubImage module](/images/tutorials/thirdparty/pytorch_example2_7b.png "SubImage module").
{{</alert>}}

Inspect the output of the `LoadBase` module in the Output Inspector to see if the lookup table has been loaded correctly.

![LUT in LoadBase](/images/tutorials/thirdparty/pytorch_example2_8.png "LUT in LoadBase").

### Write Python script
You can now execute the pre-trained PyTorch network on your image. Right-click {{< mousebutton "right" >}} the local macro and select {{< menuitem "Related Files" "DemoAI.script">}}. The Python function is supposed to be called whenever the *Trigger* is touched.

Add the following code to your Commands section:

{{< highlight filename="DemoAI.script" >}}
```Stan
Commands {
  source = $(LOCAL)/DemoAI.py
  
  FieldListener start { command = onStart }
}
```
{{</highlight>}}

The *FieldListener* always calls the Python function *onStart* when the *Trigger* *start* is touched. We now need to implement the Python function. Right-click {{< mousebutton "right" >}} the command *onStart* and select {{< menuitem "Create Python Function 'onStart'">}}.

The Python file opens automatically and the function is created. 

{{< highlight filename="DemoAI.py" >}}
```Python
import torch

def onStart():
  # Step 1: Get input image
  image = ctx.field("inputImage").image()
  imageArray = image.getTile((0, 0, 0, 0, 0, 0), image.imageExtent())
  inputImage = imageArray[0,0,0,:,:,:].astype("float")
  
  # Step 2: Normalize input image
  values = inputImage[inputImage > inputImage.mean()]
  inputImage = (inputImage - values.mean()) / values.std()
  
  # Step 3: Convert into torch tensor of size: [Batch, Channel, z, y, x]
  inputTensor = torch.Tensor(inputImage[None, None, :, :, :])
  
  # Step 4: Load and prepare AI model
  device = torch.device("cpu")
  model = torch.hub.load("fepegar/highresnet", "highres3dnet", pretrained=True, trust_repo=True)
  model.to(device).eval()
  
  output = model(inputTensor.to(device))
    
  brainParcellationMap = output.argmax(dim=1, keepdim=True).cpu()[0]
  print('...done.')
  
  # Step 6: Set output image to module
  interface = ctx.module("PythonImage").call("getInterface")
  interface.setImage(brainParcellationMap.numpy(), voxelToWorldMatrix=image.voxelToWorldMatrix())
```
{{</highlight>}}

{{<alert class="warning" caption="Warning">}}
When executing your script for the first time, you will get a ScriptError message in MeVisLab console. This only happens because the file of the trained network is missing and downloaded initially. You can ignore the message.
{{</alert>}}

{{<alert class="info" caption="Info">}}
The script uses the CPU, in case you want to use CUDA, you can replace the line *device = torch.device("cpu")* with: *device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')*
{{</alert>}}

The function does the following:
* Get the input image of the module `PythonImage`
* Normalize the input image
* Convert the image into a torch tensor of size: [Batch, Channel, z, y, x]
* Load and prepare AI model
* Set output image to module output

## Execute the segmentation
Change alpha value of your `SoView2DOverlayMPR` to have a better visualization of the results.

Change to MeVisLab IDE and select your module `DemoAI`. In *Module Inspector* click *Trigger* for *start* and wait a little until you can see the results.

![Final result](/images/tutorials/thirdparty/pytorch_example2_9.png "Final result").

Without adding a `SubImage` the segmentation results should look like this:

![Results](/images/tutorials/thirdparty/pytorch_example2_10.png "Results").

## Summary
* Pre-trained PyTorch networks can be used directly in MeVisLab via `PythonImage` module

{{< networkfile "examples/thirdparty/pytorch2/DemoAI.zip" >}}

