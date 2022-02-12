﻿import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Row_Ops():

  quantist = Aliases.Quantist
  #mainWindowView = Aliases.Quantist.MainWindowView
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView  
  md = Aliases.Quantist.MainWindowView.MainView.Btn_MoveDown
  mu = Aliases.Quantist.MainWindowView.MainView.Btn_MoveUp
  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button

  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on Analyte Panel View
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.HwndSource_MainWindowView.MainWindowView.RunTreeView.ClickItem("|[0]|[3]")
      
  #Select a range of analytes
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 200, skShift)
  for x in range (0,5):
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    md.ClickButton()
    

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.Selected_Analytes_moved_down.Check(Aliases.Quantist.HwndSource_MainWindowView.MainWindowView)

  mainWindowView.Click(400, 500)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 600, skShift)
  for y in range (0,5):
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    mu.ClickButton()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)        
  Regions.Selected_Analytes_moved_up.Check(Aliases.Quantist.HwndSource_MainWindowView.MainWindowView)

  
  
def Analyte_Panel_Table_Options_Coordinators():
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView
#  mainWindowView.Click(1775, 87) #Move Up button  
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
#  mainWindowView.Click(1825, 87) #Move Down button
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
#  mainWindowView.Click(1825, 117) #Selected button  
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
#  mainWindowView.Click(1775, 147) #Reset button
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
#
#  mainWindowView.Click(1825, 157) #Unit Cbx_arrow
#  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
#  mainWindowView.Click(1775, 182) #Select pg/mL  

  #Copy selected ClickButton()
  mainWindowView.Click(1775, 200) 

  #Copy All ClickButton()
  mainWindowView.Click(1850, 200) 
  
  #Paste selected ClickButton()
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
#  mainWindowView.Click(1775, 230) 
  
  #Reset ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1775, 275) 


