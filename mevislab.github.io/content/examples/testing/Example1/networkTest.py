
from mevis import *
from TestSupport import Base, Fields, Logging, ScreenShot
from TestSupport.Macros import *

filePath="C:/Users/gmoradi/AppData/Local/MeVisLab3.5.90/Packages/MeVisLab/Resources/DemoData/BrainT1Dicom" 

def OpenDicom ():
  ctx.field("DicomTestCase.DicomImport.inputMode").value = "Directory"
  ctx.field("DicomTestCase.DicomImport.source").value=filePath
  ctx.field("DicomTestCase.DicomImport.triggerImport").touch()
  MLAB.processEvents()
 
  while not ctx.field("DicomTestCase.DicomImport.ready").value:  
    MLAB.sleep(1)
    Base.ignoreWarningAndError(MLAB.processEvents)
  ctx.field("DicomTestCase.DicomImport.selectNextItem").touch()
  MLAB.log("Path: "+ctx.field("DicomTestCase.DicomImport.source").value)
 
def TEST_FileExist():
  isExist=os.path.exists(filePath)
  ASSERT_TRUE(isExist)
  
def TEST_DicomImport():
  expectValue= 1.0
  OpenDicom() 
  actualValue= ctx.field("DicomTestCase.DicomImport.progress").value
  ASSERT_FLOAT_EQ(expectValue,actualValue)
    
def TEST_MaxValue():
  OpenDicom()
  maxValue=ctx.field("DicomTestCase.MinMaxScan.trueMaxValue").value
  condition= maxValue >0
  if not condition :
    MLAB.logError("Max value is zero")
  else :
    print(str(maxValue) + "Ok: is not zero")
    
#This function check if the View3D-input and DicomImport-output have the same date
def TEST_CheckInputAndOutput() :
 OpenDicom()
 view3DInput= ctx.field("DicomTestCase.View3D.inImage").size3D()
 dicomImportOutput= ctx.field("DicomTestCase.DicomImport.output0").size3D()
 ASSERT_EQ(dicomImportOutput,view3DInput)
