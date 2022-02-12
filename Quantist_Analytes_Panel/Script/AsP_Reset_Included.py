import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Reset_Included():
  
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
    
  # Click on Copy Rows to Clipboard - All option
  mainWindowView.Click(1850, 200)

  
  p = Sys.WaitProcess("Notepad", 2000)
  if p.Exists:
    p.Terminate()
  else:
    TestedApps.notepad.Run(1, True)
    hwndSource = Aliases.Quantist.HwndSource_MainWindowView
    mainWindowView = hwndSource.MainWindowView

    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad
    edit = wndNotepad.Edit
    edit.Keys("^v")
    wndNotepad.MainMenu.Click("File|Save As...")
    dlgSaveAs = notepad.dlgSaveAs
    comboBox = dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox
    comboBox.SetText("AP_Copy_Uncheck_All.txt")
    btnSave = dlgSaveAs.btnSave
    btnSave.ClickButton()
    Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    Files.AP_Copy_Uncheck_All.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\AP_Copy_Uncheck_All.txt")
    notepad.Close()          

  #Reset button click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1775, 275) 
  Regions.Check_Included_Reset.Check(Aliases.Quantist.HwndSource_MainWindowView.MainWindowView)
    
def Analyte_Panel_Table_Options_Coordinators():
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Click(775, 87) # Include check/uncheck first row 
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 97) # Include check/uncheck second row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 122) # Include check/uncheck third row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 140) # Include check/uncheck fourth row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(775, 160) # Include check/uncheck fifth row


