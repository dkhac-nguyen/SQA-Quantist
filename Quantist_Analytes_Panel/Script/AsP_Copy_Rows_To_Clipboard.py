﻿import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Copy_Rows():
  
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()

  try:
    TestedApps.Quantist.Run(1, True)
  
  except ValueError as Error:
    Log.Warning("Can not Launch Quantist {Error}")
        
  except OSError as err:
    print("OS error: {0}".format(err))
    
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
    
  quantist = Aliases.Quantist
  #mainWindowView = Aliases.Quantist.MainWindowView
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
      
  p = Sys.WaitProcess("Notepad", 2000)
  if p.Exists:
    p.Terminate()
  else:
    TestedApps.notepad.Run(1, True)
   
    # Click on Copy Rows to Clipboard - All option
    mainWindowView.Click(1850, 200)
   
    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad
    edit = wndNotepad.Edit
    edit.Keys("^v")
    wndNotepad.MainMenu.Click("File|Save As...")
    dlgSaveAs = notepad.dlgSaveAs
    comboBox = dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox
    comboBox.SetText("AP_Copy_All.txt")
    btnSave = dlgSaveAs.btnSave
    btnSave.ClickButton()
    
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    if (Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
       Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
       
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Files.AP_Copy_All.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\AP_Copy_All.txt")
    notepad.Close()

  p = Sys.WaitProcess("Notepad", 2000)
  if p.Exists:
    p.Terminate()
  else:
    TestedApps.notepad.Run(1, True)
    hwndSource = Aliases.Quantist.HwndSource_MainWindowView
    mainWindowView = hwndSource.MainWindowView    
    mainWindowView.Click(400, 100)  #Select B7-H1 to IL-1alpha (GX) range of Analytes 
    aqUtils.Delay(1000)
    mainWindowView.Click(400, 200, skShift)
    
    #Click on Copy to Clipboard - Selected option
    mainWindowView.Click(1775, 200)

    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad
    edit = wndNotepad.Edit
    edit.Keys("^v")
    wndNotepad.MainMenu.Click("File|Save As...")
    dlgSaveAs = notepad.dlgSaveAs
    comboBox = dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox    
    comboBox.SetText("AP_Copy_Selected.txt")
    btnSave = dlgSaveAs.btnSave    
    btnSave.ClickButton()
    
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    if (Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
        Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Files.AP_Copy_Selected.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\AP_Copy_Selected.txt")
    notepad.Close()
  

def Analyte_Panel_Table_Options_Coordinators():
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Click(1775, 87) #Down button coordinate
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1825, 87) #Up button coordinate
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1825, 117) #Selected button coordinate
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1775, 147) #Reset button coordinate


