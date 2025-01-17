﻿import Quantist_Removing_Files
import Load_CSV_File

def Analyte_Results_Curve_Configuration_View():

  analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  ##
  Regions.PM8800_Tree.Check(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem)
  Regions.PM8800_Chart.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  Regions.PM8800_Options.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.PM8800_main.Check(Aliases.Quantist.MainWindowView)    

  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurvePanel.LabelAnalyte, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurvePanel.LabelAnalyte, "WPFControlText", cmpEqual, "Analyte:")
  Regions.GroupboxConfigureCurve_PM8800.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxConfigureCurve)
  Regions.GroupboxCurrentCurveData_PM8800.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxCurrentCurveData)
  Regions.GroupboxGraphOptions_PM8800.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxGraphOptions)
  Regions.GroupboxTableOptions_PM8800.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions)
  Regions.PM8800_GridCurveData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData)

  analyte.ClickItem(1)
  Regions.CurveView_CD40.Check(mainWindowView)
  analyte.ClickItem(2)
  Regions.CurveView_EGF.Check(mainWindowView)
  analyte.ClickItem(3)
  Regions.CurveView_Eotaxin.Check(mainWindowView)
  analyte.ClickItem(4)
  Regions.CurveView_FGF_basic_CDXY.Check(mainWindowView)
  analyte.ClickItem(5)
  Regions.CurveView_FGF_basic_HR.Check(mainWindowView)
  analyte.ClickItem(6)
  Regions.CurveView_Fit_3_Lig.Check(mainWindowView)
  analyte.ClickItem(7)
  Regions.CurveView_Fractalkine.Check(mainWindowView)
  analyte.ClickItem(8)
  Regions.CurveView_G_CSF.Check(mainWindowView)

  analyte.ClickItem(38)
  Regions.CurveView_MIP_1alpha.Check(mainWindowView)
  analyte.ClickItem(39)
  Regions.CurveView_MIP_1beta.Check(mainWindowView)
  analyte.ClickItem(40)
  Regions.CurveView_MIP_3alpha.Check(mainWindowView)
  analyte.ClickItem(41)
  Regions.CurveView_MIP_3beta.Check(mainWindowView)
  analyte.ClickItem(42)
  Regions.CurveView_PDGF_AA.Check(mainWindowView)
  analyte.ClickItem(43)
  Regions.CurveView_PDGF_AB_BB.Check(mainWindowView)
  analyte.ClickItem(44)
  Regions.CurveView_RANTES.Check(mainWindowView)
  analyte.ClickItem(45)
  Regions.CurveView_TGF_alpha.Check(mainWindowView)
  analyte.ClickItem(46)
  Regions.CurveView_TNF_alpha.Check(mainWindowView)
  analyte.ClickItem(47)
  Regions.CurveView_TNF_beta.Check(mainWindowView)
  analyte.ClickItem(48)
  Regions.CurveView_TRAIL.Check(mainWindowView)
  analyte.ClickItem(49)
  Regions.CurveView_VEGF.Check(mainWindowView)
