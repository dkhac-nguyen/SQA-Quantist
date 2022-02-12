import Load_CSV_File 
import Quantist_Removing_Files

def Row_Operations_Expand_All():
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView.MainView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
        
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")
    
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions

  Regions.PM8800_B7_H1_Collapse.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  tblOption.ButtonExpandAll.ClickButton()
  Regions.PM8800_B7_H1_Expand_Top.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  main.CurveData.GridData.Drag(1223, 49, 6, 196)
  Regions.PM8800_B7_H1_Expand_Bottom.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)

def Row_Operations_Collapse_All():
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView.MainView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions

  tblOption.ButtonCollapseAll.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  Regions.PM8800_B7_H1_Collapse_Bottom.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  Aliases.Quantist.MainWindowView.MainView.CurveData.GridData.Drag(1229, 184, 0, -145)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  Regions.PM8800_B7_H1_Collapse_Top.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  
def Copy_Rows_To_Clipboard_Agg():
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView.MainView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
      
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
        
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions
  tblOption.ButtonAggregates.ClickButton()

  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad

  edit = wndNotepad.Edit
  edit.Keys("^v")

  wndNotepad.MainMenu.Click("File|Save As...")
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("PM8800-Agg.txt")
  dlgSaveAs.btnSave.ClickButton()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  if (notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
     notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)   
  Files.PM8800_Aggregates.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\PM8800-Agg.txt")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  wndNotepad.Close()   

        
def Copy_Rows_To_Clipboard_Replicates():
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    

  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions
  tblOption.ButtonReplicates.ClickButton()

  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad
  
  edit = wndNotepad.Edit
  edit.Keys("^v")
  
  wndNotepad.MainMenu.Click("File|Save As...")  
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("PM8800-Rep.txt")
  dlgSaveAs.btnSave.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  if (notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
     notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)     
  Files.PM8800_Replicates.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\PM8800-Rep.txt")
  wndNotepad.Close() 
  

def Reset_Included_Standards():
  pass

def Reset_Included_Unknowns_Ctrls():
  pass


