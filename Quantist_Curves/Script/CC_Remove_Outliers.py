import Load_CSV_File 
import Quantist_Removing_Files

def CC_Remove_Outliers_Current():
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "TestData.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.TestData_B7_H1_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

    
  # DataPoints - Clicked on current Curve Remove Outliers Recovery Range 90-110% 
  configCurve = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
  configCurve.RecoverRangeBox.ClickItem("From90To110")
  configCurve.Btn_ForCurrent_RemoveOutliers.ClickButton()
    

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    

  Regions.TestData_B7_H1_90_110_RemoveOutliers_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
    
  # Reset Include Standard button should bring back DataPoints as before Remove Outliers
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions.ButtonStandards.ClickButton()
  configCurve.RecoverRangeBox.ClickItem("From80To120")
        
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.TestData_B7_H1_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
    
def CC_Remove_Outliers_All():

  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
        
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  main = Aliases.Quantist.MainWindowView.MainView
  curvePanel = main.CurvePanel
  treeview = Aliases.Quantist.MainWindowView.RunTreeView #List of files
  ma_listControl = Aliases.Quantist.MainWindowView.MainView.CurveData #Multi Analytes List
  
  configCurve = curvePanel.ConfigureCurve
  configCurve.CurveFitBox.ClickItem("FivePL")
  configCurve.CurveWeightingBox.ClickItem("OneOverYSquared")
  configCurve.RecoverRangeBox.ClickItem("From90To110")

  # Verify  B7_H1 Curve Data and Grid data before applying Remove Outliers for All
  Regions.PM8800_B7_H1_CurveData_before.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_B7_H1_GridData_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte = curvePanel.AnalyteBox
  analyte.ClickItem(1)   # Select CD40 analyte, then
  # Verify CD40 Curve Data and Grid data before applying Remove Outliers for All  
  Regions.PM8800_CD40_CurveData_before.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_CD40_GridData_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte.ClickItem(5)   # Select FGF Basis analyte, then    
  # Verify FGF basis Curve Data and Grid data before applying Remove Outliers for All                                                                                                                                                           
  Regions.PM8800_FGFbasis_CurveData_before.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_FGFbasis_GridData_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  # Apply Remove Outliers for All analytes
  configCurve.Btn_ForAll_RemoveOutliers.ClickButton()
  Regions.PM8800_FGFbasis_CurveData_after.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_FGFbasis_GridData_after.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)  

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte.ClickItem(1)   # Select CD40 analyte, then
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte.ClickItem(1)   # Select CD40 analyte, then   
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  # Verify CD40 Curve Data and Grid data after applying Remove Outliers for All
  Regions.PM8800_CD40_CurveData_after.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_CD40_GridData_after.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  analyte.ClickItem(0)  # Select B7_H1 analyte, then
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  analyte.ClickItem(0)  # Select B7_H1 analyte, then  
  # Verify B7_H1 Curve Data and Grid data after applying Remove Outliers for All
  Regions.PM8800_B7_H1_CurveData_after.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_B7_H1_GridData_after.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  # Switch to Multi Analytes View
  treeView.ClickItem("|[0]|[1]")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  #Expand Standard1 - Standard2
  ma_listControl.RowMarginControl2.Click()
  ma_listControl.RowMarginControl3.Click()
  ma_listControl.RowMarginControl4.Click()
  ma_listControl.RowMarginControl5.Click()
  ma_listControl.RowMarginControl6.Click()
  ma_listControl.RowMarginControl7.Click()
  ma_listControl.RowMarginControl8.Click()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  main.MA_Replicates.ClickButton()
  
  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.Edit.Keys("^v")
  wndNotepad.MainMenu.Click("File|Save As...")
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("RemoveOutliers_All_Replicates.txt")
  dlgSaveAs.btnSave.ClickButton()
  Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
  Files.RemoveOutliers_All_Replicates.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\RemoveOutliers_All_Replicates.txt")
  wndNotepad.Close()
  main.MA_Standards.ClickButton()
  treeView.ClickItem("|[0]|[0]")
   