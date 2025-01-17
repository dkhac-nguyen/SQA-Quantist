﻿import Load_CSV_File 
import Quantist_Removing_Files


def MA_All_Curve_Data():
  
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.ButtonMA_Curve_Data
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  hwndSource = Aliases.Quantist.MainWindowView
  border = hwndSource.MainView
  groupBox = border.CurvePanel.ConfigureCurve
  groupBox.CurveFitBox.ClickItem("FivePL")
  groupBox.Btn_CopyToAll_CurveFit.ClickButton()
  groupBox.CurveWeightingBox.ClickItem("OneOverY")
  groupBox.Btn_CopyToAll_CurveWeighting.ClickButton()
  groupBox.RecoverRangeBox.ClickItem("From90To110")
  groupBox.Btn_CopyToAll_RecoveryRange.ClickButton()
  hwndSource.RunTreeView.ClickItem("|[0]|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Regions.MA_CurveData_All_5PL_1OverY.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)
  
  main = Aliases.Quantist.MainWindowView
  for i in range(8):
    main.MainViewRunCtr.Click(1880, 995)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_CurveData_All_1OverY_90_110.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)
  
  main = Aliases.Quantist.MainWindowView
  for i in range(12):
    main.MainViewRunCtr.Click(1880, 995)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_CurveData_All_LLOQ.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)

#  all_data = Aliases.Quantist.MainWindowView.MainView.CurveData.All_Curve_Data
#  all_data.Drag(159, 715, 29, -9)
#  main = Aliases.Quantist.MainWindowView
  for i in range(20):
    main.MainViewRunCtr.Click(1880, 995)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_CurveData_All_ULOQ_Rsq.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)

  #all_data.Drag(190, 714, 28, -4)
  for i in range(20):
    main.MainViewRunCtr.Click(1880, 995)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_CurveData_All_Coeff_A_B.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)
  
  #all_data.Drag(215, 715, 29, -4)
  for i in range(20):
    main.MainViewRunCtr.Click(1880, 995)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_CurveData_All_Coeff_C_D.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)
  
  #all_data.Drag(249, 716, 29, 0)
  for i in range(20):
    main.MainViewRunCtr.Click(1880, 995)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_CurveData_All_G_Units.Check(Aliases.Quantist.MainWindowView.MainView.dockPanel, False, False, 21869, 17)


