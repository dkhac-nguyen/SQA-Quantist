import Load_CSV_File 
import Quantist_Removing_Files

def Graph_Options_Show_Unknowns_Controls():
  #TestedApps.Quantist.Run(1, True)
  #BuiltIn.ShowMessage("Launching Quantist successful!")

  main = Aliases.Quantist.MainWindowView.MainView
  curvePanel = main.CurvePanel
  treeView = Aliases.Quantist.MainWindowView.RunTreeView #List of files
  analyte = curvePanel.AnalyteBox
    
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()  
    
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_unknown_control
    quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")

#  curvePanel.CheckboxShowUnknowns.ClickButton(cbChecked)
#  curvePanel.CheckboxShowControls.ClickButton(cbChecked)
    
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  analyte.ClickItem(0)
  Regions.BAFF_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  analyte.ClickItem(1)
  Regions.CCL2_Before.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  analyte.ClickItem(2)
  Regions.CCL3_Before.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  checkBox = curvePanel.CheckboxShowUnknowns
  checkBox.ClickButton(cbChecked)
  analyte.ClickItem(0)
  Regions.BAFF_Unks_after.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  
  analyte.ClickItem(1)
  Regions.CCL2_Unks_after.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)  

  analyte.ClickItem(2)
  Regions.CCL3_Unks_after.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)  

  checkBox2 = curvePanel.CheckboxShowControls
  checkBox2.ClickButton(cbChecked)
  Regions.CCL3_Unks_Ctrls_After.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  analyte.ClickItem(1)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte.ClickItem(1)
  Regions.CCL2_Unks_Ctrls_After.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  analyte.ClickItem(0)
  Regions.BAFF_Unks_Ctrls_After.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  checkBox.ClickButton(cbUnchecked)
  checkBox2.ClickButton(cbUnchecked)
  Regions.BAFF_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  analyte.ClickItem(1)
  Regions.CCL2_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  analyte.ClickItem(2)
  Regions.CCL3_before.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

def Graph_Options_Show_Controls():
  pass

def Graph_Options_Log_X_Y_Axis():

  main = Aliases.Quantist.MainWindowView.MainView
  curvePanel = main.CurvePanel
  treeView = Aliases.Quantist.MainWindowView.RunTreeView #List of files
  analyte = curvePanel.AnalyteBox

  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
    
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_unknown_control
    quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)        
    
  analyte.ClickItem(2)
#  curvePanel.CheckboxLogarithmicYAxis.ClickButton(cbUnchecked)
#  curvePanel.CheckboxLogarithmicXAxis.ClickButton(cbUnchecked)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  chkBoxX = curvePanel.CheckboxLogarithmicXAxis
  chkBoxX.ClickButton(cbUnchecked)
  Regions.CCL3_LogX_off.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  chkBoxY = curvePanel.CheckboxLogarithmicYAxis
  chkBoxY.ClickButton(cbUnchecked)
  Regions.CCL3_LogX_LogY_off.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  chkBoxX.ClickButton(cbChecked)
  Regions.CCL3_LogY_off.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  chkBoxY.ClickButton(cbChecked)
  Regions.CCL3_LogX_LogY_on.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  
  
def Graph_Options_Log_Y_Axis():
  pass



