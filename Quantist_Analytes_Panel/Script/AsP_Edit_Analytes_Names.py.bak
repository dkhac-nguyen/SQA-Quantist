import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Edit_Analyte_Names():
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView  
  md = Aliases.Quantist.MainWindowView.MainView.Btn_MoveDown
  mu = Aliases.Quantist.MainWindowView.MainView.Btn_MoveUp
  copy = Aliases.Quantist.MainWindowView.MainView.Btn_Selected_Copy
  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button

  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800-Mod.csv")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on Analytes Panel View - PM8800-Mod
  treeView.ClickItem("|[1]|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
          
  #Select a range of analytes (7)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 222, skShift)

  #Copy selected ClickButton()
  mainWindowView.Click(1775, 200) 
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    
  #Click on Analytes Panel View - PM8800
  treeView.ClickItem("|[0]|[3]")

  #Select a range of different number of analytes (6)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 200, skShift)

  #Paste selected ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1775, 230) 
  
  #Confirm error dialog  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Aliases.Quantist.dlg.btnOK.ClickButton()  

  #Select a range of correct number of analytes (7)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 222, skShift)

  #Paste selected ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1775, 230) 

  Regions.AP_copy_paste_selected.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr, False, False, 141659, 17)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on Well Assignments View - PM8800
  treeView.ClickItem("|[0]|[2]")
  extendedDataGrid = Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2
  Regions.WA_data_grid_analytes_names_changed_1.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid, False, False, 37578, 17)

  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  extendedDataGrid.Drag(52, 941, 105, -8)
  Regions.WA_data_grid_analytes_names_changed_2.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid, False, False, 37578, 17)
  extendedDataGrid.Drag(158, 940, 103, -7)
  Regions.WA_data_grid_analytes_names_changed_3.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid, False, False, 37578, 17)
  extendedDataGrid.Drag(283, 941, 107, -20)
  Regions.WA_data_grid_analytes_names_changed_4.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid, False, False, 37578, 17)
  extendedDataGrid.Drag(389, 943, 103, -15)
  Regions.WA_data_grid_analytes_names_changed_5.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid, False, False, 37578, 17)
  extendedDataGrid.Drag(517, 944, 35, 0)
  Regions.WA_data_grid_analytes_names_changed_6.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid, False, False, 37578, 17)

  #Click on Multi Analytes View - PM8800
  treeView.ClickItem("|[0]|[1]")
  treeListView = Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid

  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Regions.MA_data_grid_analytes_names_changed_1.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid, False, False, 79168, 17)
  treeListView.Drag(106, 949, 256, -5)
  Regions.MA_data_grid_analytes_names_changed_2.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid, False, False, 79525, 17)
  treeListView.Drag(341, 949, 267, 0)
  Regions.MA_data_grid_analytes_names_changed_3.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid, False, False, 79168, 17)
  treeListView.Drag(561, 949, 271, 27)
  Regions.MA_data_grid_analytes_names_changed_4.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid, False, False, 79168, 17)
  treeListView.Drag(963, 953, 182, 6)
  Regions.MA_data_grid_analytes_names_changed_5.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid, False, False, 79168, 17)

  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  treeView.ClickItem("|[1]|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)