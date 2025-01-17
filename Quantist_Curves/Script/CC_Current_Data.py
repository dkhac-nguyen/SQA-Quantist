﻿import Load_CSV_File 
import Quantist_Removing_Files

def CC_Current_Data():
  
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxCurrentCurveData
  gridData = Aliases.Quantist.MainWindowView.MainView.CurveData.GridData
  
  # Verify not include B1, then C1, C2 into calculation -
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  curvedata = Aliases.Quantist.MainWindowView.MainView.CurveData
  # Expanding Standard1
  curvedata.RowMarginControl2.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  # Expanding Standard2
  curvedata.RowMarginControl3.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  # Uncheck B1
  curvedata.InplaceBaseEdit11.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  Regions.PM8800_B7_H1_5PL_None_60_B1_Uncheked.Check(curveData, False, False, 6591, 17)
  
  # Uncheck Standard2 both C1/C2
  curvedata.InplaceBaseEdit12.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  Regions.PM8800_B7_H1_5PL_None_60_B1_C1_C2_Uncheked.Check(curveData, False, False, 6591, 17)
  Regions.PM8800_B7_H1_5PL_None_60_B1_C1_C2_Unchecked_Grid.Check(gridData, False, False, 22513, 17)
  
  # Reset - Included all Standards (B1/C1/C2)
  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions
  tblOption.ButtonStandards.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  Regions.PM8800_B1_H7_Included_All.Check(curveData, False, False, 6591, 17)
  tblOption.ButtonCollapseAll.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  
def Test():
  mainWindowView = Aliases.Quantist.MainWindowView
  mainWindowView.InplaceBaseEdit5.Click(78, 11)
  rowMarginControl = mainWindowView.RowMarginControl
  rowMarginControl.Click(11, 9)
  mainWindowView.InplaceBaseEdit6.Click(32, 9)
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "Enabled", cmpEqual, True)
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "Id", cmpEqual, 355) #Not a constant
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "displayText_2", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "Enabled", cmpEqual, True)
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "Id", cmpEqual, 692) #Not a constant
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "displayText_2", cmpEqual, "2")
  rowMarginControl.Click(11, 12)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140, "Enabled", cmpEqual, True)
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140, "Id", cmpEqual, 732)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140, "displayText_2", cmpEqual, "98.15")

  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "displayText_2", cmpEqual, "1")

  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "displayText_2", cmpEqual, "2")

  Aliases.Quantist.MainWindowView.RowMarginControl2.Click(11, 9)

  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit3, "displayText_2", cmpEqual, "1")

  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "WPFControlIndex", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "WPFControlOrdinalNo", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit4, "displayText_2", cmpEqual, "2")

def Test1():
  mainWindowView = Aliases.Quantist.MainWindowView
  inplaceBaseEdit = mainWindowView.InplaceBaseEdit8
  inplaceBaseEdit.Click(31, 8)
  checkEdit = inplaceBaseEdit.CheckEdit
  checkEdit.Click(36, 8)
  checkEdit.Click(36, 13)
  #mainWindowView.InplaceBaseEdit9.Click(35, 11)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.InplaceBaseEdit7, "displayText_2", cmpEqual, "1")
  mainWindowView.ztreeListView1.Drag(1226, 53, 3, 30)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140, "zEditValueCache_k__BackingField", cmpEqual, 38.568176435345919)

def Test2():
  mainWindowView = Aliases.Quantist.MainWindowView
  mainWindowView.RowMarginControl3.Click(8, 12)
  mainWindowView.InplaceBaseEdit8.Click(33, 8)
  #OCR.Recognize(Aliases.Quantist.MainWindowView.InplaceBaseEdit10).CheckText("*1\n*")
  Regions.Std1_B1_Unchecked.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.Std1_B1_Unchecked, 2, 1, 1218, 274, False))
  Regions.CC_Data_B1_Unchecked.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.CC_Data_B1_Unchecked, 14, 282, 311, 308, False))
  mainWindowView.RowMarginControl4.Click(11, 11)
  mainWindowView.InplaceBaseEdit11.Click(35, 9)
  Regions.Std2_C1_C2_Unchecked.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.Grid, 3, 684, 1213, 277, False))
  Regions.CC_Data_C1_C2_Unchecked.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.CC_Data_C1_C2_Unchecked, 13, 286, 314, 309, False))
  mainWindowView.ButtonStandards.ClickButton()
  Regions.Std1_Std2_Reset.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.Border, 3, 691, 1220, 278, False))
  Regions.CC_Data_Std1_Std2_Reset.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.ScrollViewer, 13, 284, 311, 307, False))
  mainWindowView.RowMarginControl3.Click(11, 13)
  mainWindowView.RowMarginControl4.Click(10, 8)

