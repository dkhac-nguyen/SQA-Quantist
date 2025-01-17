﻿import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Not_Included():
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView  

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
        
  mainWindowView.Click(775, 87) # Include check/uncheck first row 
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 97) # Include check/uncheck second row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 122) # Include check/uncheck third row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 140) # Include check/uncheck fourth row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 160) # Include check/uncheck fifth row

  #Verify uncheck Included
  Regions.Uncheck_Included.Check(Aliases.Quantist.HwndSource_MainWindowView.MainWindowView)

  #Click on Well Assignments View
  treeView.ClickItem("|[0]|[2]")
  extendedDataGrid = Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2

  # Verify that the NOT INCLUDED analytes will not be listed in Well Assignments View
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.WA_data_grid_analytes_notIncluded_1.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)  
  extendedDataGrid.Drag(52, 941, 105, -8)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.WA_data_grid_analytes_notIncluded_2.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)
  extendedDataGrid.Drag(170, 942, 107, 6)
  Regions.WA_data_grid_analytes_notIncluded_3.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  extendedDataGrid.Drag(281, 941, 112, 3)
  Regions.WA_data_grid_analytes_notIncluded_4.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  extendedDataGrid.Drag(385, 942, 155, -1)
  Regions.WA_data_grid_analytes_notIncluded_5.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)