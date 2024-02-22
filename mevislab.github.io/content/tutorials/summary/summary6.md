---
title: "Step 6: Refine - Update Application"
date: "2023-01-20"
status: "open"
draft: false
weight: 830
tags: ["Advanced", "Tutorial", "Prototyping"]
menu: 
  main:
    identifier: "summaryexample6"
    title: "Integrate feedback from customers having installed your executable and adapt your test cases from Example 4."
    weight: 830
    parent: "summary"
---
# Step 6: Refine - Update Application
## Introduction
In previous step you developed an application which can be installed on your customers systems for usage. In this step we are going to integrate simple feedback into our executable and re-create the installer.

We want to show you how easy it is to update your application using MeVisLab.

Your customer requests an additional requirement to define the transparency of your 2D overlay in addition to defining the color.
* **Requirement 5.2**: It shall be possible to define the alpha value of the overlay

## Steps to do
### Adapt your macro module
Use the module search to add your macro module to your workspace. We need an additional UI element for setting the alpha value of the overlay.

Right-click {{< mousebutton "right" >}} your module and select {{< menuitem "Related Files" "<MACRO_NAME>.script" >}}.

In MATE, add another field to your *Parameters* section and re-use the field by setting the *internalName*. Add the field to the *Settings* section of your *Window*, maybe directly after the color selection.

{{< highlight filename="<MACRO_NAME>.script" >}}
```Stan
Interface {
...
  Parameters {
    ...
    Field selectOverlayTransparency {
      internalName = SoView2DOverlay.alphaFactor
    }
    ...
  }
}

Window {
...
    Box Settings {
    ...
      Field selectOverlayTransparency {
        title   = Alpha
      }
    ...
    }
...
}
```
{{</highlight>}}

Back in MeVisLab IDE, your user interface should now provide the possibility to define an alpha value of the overlay. Changes are applied automatically because you re-used the field of the `SoView2DOverlay` module directly.

![Updated User Interface](/images/tutorials/summary/Example6_1.png "Updated User Interface")

You can also update your Python files for new or updated requirements. In this example we just want to show the basic principles, therefore we only add this new element to the Script file.

If you want to write an additional Python test case, you can also do that.

## Summary
* Your application can be updated by modifying the macro module and/or internal network of your application
* Any changes will be applied to your installable executable in the next step

{{< networkfile "examples/summary/TutorialSummaryUpdated.zip" >}}
