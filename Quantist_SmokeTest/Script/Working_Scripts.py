﻿def Test1():
  ####### B7-H1
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.ComboBox.ClickItem(0) #Analyte
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverYSquared") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From80To120")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*")
  Regions.B7_H1_5PL_1OverYsq_80_120Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)  

  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverYSquared") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From60To140")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*")
  #Regions.B7_H1_5PL_1OverYsq_60_140Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)  
  Regions.B7_H1_5PL_1OverYsq_60_140Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)  

  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverYSquared") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From70To130")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*")
  Regions.B7_H1_5PL_1OverYsq_70_130Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)    

  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverYSquared") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From90To110")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 1371.74897119342\nULOQ: 4115.24691358025\nR? 0.997614\nA:\n5.005\nB: 0.963\nC:\n164261.222\nD:\n9888.035\nG: 0.596\nUnits:\n*")
  Regions.B7_H1_5PL_1OverYsq_90_110Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)    
    
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("None") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From80To120")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 192.057613168724\nULOQ: 46670\nR? 0.998794\nA: 20.465\nB: 0.904\nC: 90302.944\nD:\n20783.555\nG: 0.845\nUnits:\n*")  
  Regions.B7_H1_5PL_None_80_120Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)
  
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("None") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From80To120")
   
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem("FivePL") #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverY") #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem("From80To120")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*")
  Regions.B7_H1_5PL_1OverY_80_120Pct.Check(Aliases.Quantist.MainWindowView.Border2.Pane)  


  ####### CD40-LIG 
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.ComboBox.ClickItem(1) 
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverYSquared") #Curve Weighting
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 1371.74897119342\nULOQ: 12345.7407407407\nR? 0.999929\nA:\n12.163\nB: 1.015\nC:\n167576.274\nD:\n7960.666\nG: 0.793\nUnits:\n*")

  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("None") #Curve Weighting
  #OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("")  
  
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem("OneOverY") #Curve Weighting
  #OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("")

def test2():
  CurveData1 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*"
  CurveData2 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*"
  CurveData3 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*"
  CurveData4 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 15556.6666666667\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:\n*"
  
  CurveData5 = "*Current Curve Data\nLLOQ: 192.057613168724\nULOQ: 46670\nR? 0.998794\nA: 20.465\nB: 0.904\nC: 90302.944\nD:\n20783.555\nG: 0.845\nUnits:\n*"
  CurveData6 = "*Current Curve Data\nLLOQ: 192.057613168724\nULOQ: 46670\nR? 0.998794\nA: 20.465\nB: 0.904\nC: 90302.944\nD:\n20783.555\nG: 0.845\nUnits:\n*"
  CurveData7 = "*Current Curve Data\nLLOQ: 192.057613168724\nULOQ: 46670\nR? 0.998794\nA: 20.465\nB: 0.904\nC: 90302.944\nD:\n20783.555\nG: 0.845\nUnits:\n*"
  CurveData8 = "*Current Curve Data\nLLOQ: 576.172839506173\nULOQ: 46670\nR? 0.998794\nA: 20.465\nB: 0.904\nC: 90302.944\nD:\n20783.555\nG: 0.845\nUnits:\n*"

  CurveData9  = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*"
  CurveData10 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*"
  CurveData11 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*"
  CurveData12 = "*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*"
  
  Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From60To140", CurveData1, "B7_H1_5PL_1OverYsq_60_140Pct")
  Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From70To130", CurveData2, "B7_H1_5PL_1OverYsq_70_130Pct")
  Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From80To120", CurveData3, "B7_H1_5PL_1OverYsq_80_120Pct")
  Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From90To110", CurveData4, "B7_H1_5PL_1OverYsq_90_110Pct")
  
  Config_Current_Curve_Analyte("FivePL", "None", "From60To140", CurveData5, "B7_H1_5PL_1OverYsq_60_140Pct")
  Config_Current_Curve_Analyte("FivePL", "None", "From70To130", CurveData6, "B7_H1_5PL_1OverYsq_70_130Pct")
  Config_Current_Curve_Analyte("FivePL", "None", "From80To120", CurveData7, "B7_H1_5PL_1OverYsq_80_120Pct")
  Config_Current_Curve_Analyte("FivePL", "None", "From90To110", CurveData8, "B7_H1_5PL_1OverYsq_90_110Pct")

  Config_Current_Curve_Analyte("FivePL", "OneOverY", "From60To140", CurveData9, "B7_H1_5PL_1OverYsq_60_140Pct")
  Config_Current_Curve_Analyte("FivePL", "OneOverY", "From70To130", CurveData10, "B7_H1_5PL_1OverYsq_70_130Pct")
  Config_Current_Curve_Analyte("FivePL", "OneOverY", "From80To120", CurveData11, "B7_H1_5PL_1OverYsq_80_120Pct")
  Config_Current_Curve_Analyte("FivePL", "OneOverY", "From90To110", CurveData12, "B7_H1_5PL_1OverYsq_90_110Pct")

    
def Config_Current_Curve_Analyte(CurveFit, CurveWeight, RecoveryRange, CurveData, CurveImage):
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox.ClickItem(CurveFit) #Curve Fit
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox2.ClickItem(CurveWeight) #Curve Weighting
  Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3.ClickItem(RecoveryRange)
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText(CurveData)

  #w = Sys.Desktop.ActiveWindow()
  #w = Aliases.Quantist.MainWindowView.Border2.Pane
  #if not Regions.CurveImage.Check(w):
  #  Log.Error("The compared regions are not identical.", w.Name)    
  
  #temCurveImg = Regions.GetPicture(CurveImage)
  #Log.Message(temCurveImg)
  #Regions.CurveImage.Check(Aliases.Quantist.MainWindowView.Border2.Pane)     
  
def Test2():
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*")
  comboBox = Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox3
  comboBox.Click(85, 7)
  comboBox.ClickItem("From70To130")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*")
  comboBox.Click(57, 12)
  comboBox.ClickItem("From80To120")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*")
  comboBox.Click(76, 15)
  comboBox.ClickItem("From90To110")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999925\nA:\n4.143\nB: 0.885\nC: 75405.653\nD: 28944.227\nG: 0.499\nUnits:\n*")

def Test3():
  quantist_Wpf = Aliases.Quantist_WPF
  mainWindowView = quantist_Wpf.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Button.ClickButton()
  quantist_Wpf.dlgOpen.OpenFile("E:\\TestComplete\\Quantist\\SampleQuantistFiles\\01-10-18 MS B0 wk 28 repeat PM8800_20180110_133338.csv", "Consumable Files (*.csv;*.quantist)")
  treeView = mainWindowView.RunTreeView
  treeView.ExpandItem("|[0]")
  treeView.ClickItem("|[0]|[1]")
  Regions.MS_B0_Concentration_Curve.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 8, 5, 702, 473, False))
  mainWindowView.GridSplitter.Drag(146, 1, 26, -191)
  dataGrid = mainWindowView.zdataGrid1
  dataGrid.DatagridcolumnheaderRecovery.Drag(1, 12, 2, 8)
  dataGrid.DatagridcolumnheaderWell.Drag(1, 17, -55, 1)
  dataGrid.DatagridcolumnheaderExpConc.Drag(96, 12, 17, 0)
  Regions.MS_B0_Concentration_Data.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Border, 12, 292, 706, 325, False))
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderSample).CheckText("*Sample*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderWell).CheckText("*Well*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderNetMfi).CheckText("*Net MFI*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderNetMfiCv).CheckText("*Net MFI CV%*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderBackfitConc).CheckText("*Backfit Conc*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderExpConc).CheckText("*Exp Conc*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderRecovery).CheckText("*% Recovery*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderIncluded).CheckText("*Included*")
  Tables.Analyte.Check()
  aqObject.CheckProperty(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.ComboBox, "wItemCount", cmpEqual, 50)
  aqObject.CheckProperty(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.ComboBox, "wText", cmpEqual, "B7-H1")

def Test4():
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Border2.ScrollViewer, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl, "wTabCount", cmpEqual, 2)
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 64.0192043895748\nULOQ: 46670\nR? 0.999995\nA:\n5.524\nB: 0.922\nC:\n42605.823\nD:\n15177.224\nG: 0.684\nUnits:*")
  scrollViewer = Aliases.Quantist.MainWindowView.Border2.ScrollViewer
  scrollViewer.VScroll.Pos = 129.80000000000007
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxGraphSettings).CheckText("*Graph Settings\nShow Unknowns\nShow Controls\nLogarithmic X Axis\n✓ Logarithmic Y Axis\nA Copy Image of Graph to Clipboard\n*")
  scrollViewer.VScroll.Pos = 0
  tabControl = scrollViewer.TabControl
  tabControl.ClickTab("Configure All Curves")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl).CheckText("*Configure Current Curve Configure All Curves\nCurve Fit: 5PL\nCurve Weighting: 1/72\nRecovery Range: 80% to 120%\nRemove Outliers Based on Recoveries (All)\n*")
  comboBox = tabControl.ComboBox
  aqObject.CheckProperty(comboBox, "wText", cmpEqual, "FivePL")
  aqObject.CheckProperty(comboBox, "wItemCount", cmpEqual, 2)
  aqObject.CheckProperty(comboBox, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(comboBox, "wSelectedItem", cmpEqual, 1)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl.ComboBox, "wItem[0]", cmpEqual, "FourPL")
  
def Test5():
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 1371.74897119342\nULOQ: 12345.7407407407\nR? 0.976443\nA:\n-72.567\nB: 0.750\nC: 462275.693\nD:\n13697.128\nG: 0.747\nUnits:\n*")
  tabControl = Aliases.Quantist.MainWindowView.Border2.ScrollViewer.TabControl
  comboBox = tabControl.ComboBox2
  comboBox.Click(186, 15)
  comboBox.ClickItem("OneOverY")
  comboBox2 = tabControl.ComboBox3
  comboBox2.Click(73, 7)
  comboBox2.ClickItem("From70To130")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 1371.74897119342\nULOQ: 12345.7407407407\nR? 0.997614\nA:\n5.005\nB: 0.963\nC:\n164261.222\nD:\n9888.035\nG: 0.596\nUnits:\n*")
  comboBox.Click(70, 8)
  comboBox.ClickItem("OneOverYSquared")
  comboBox2.Click(45, 14)
  comboBox2.ClickItem("From90To110")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Border2.ScrollViewer.GroupboxCurrentCurveData).CheckText("*Current Curve Data\nLLOQ: 1371.74897119342\nULOQ: 12345.7407407407\nR? 0.999929\nA:\n12.163\nB: 1.015\nC:\n167576.274\nD:\n7960.666\nG: 0.793\nUnits*")


def Curve_Analytes_bk():
  quantist_Wpf = Aliases.Quantist
  mainWindowView = quantist_Wpf.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Button.ClickButton()
  quantist_Wpf.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + "2 plates with 1 std.csv", "Consumable Files (*.csv;*.quantist)")
  treeView = mainWindowView.RunTreeView
  treeView.ExpandItem("|[0]")
  treeView.ClickItem("|[0]|[1]")
  #mainWindowView.GridSplitter.Drag(159, 1, 11, -185)
  #mainWindowView.zdataGrid1.DatagridcolumnheaderSample.Drag(170, 12, -72, -2)
  analyteBox = Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.ComboBox
  #analyteBox = mainWindowView.Grid.ComboBox
  #aqObject.CheckProperty(grid.zchart, "Enabled", cmpEqual, True)
  #Tables.GM_CSF.Check()
  #Regions.zchart.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 12, 8, 694, 283, False))
  #comboBox = grid.ComboBox
  
  for i in range(13):
    analyteBox.ClickItem(i)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  #Regions.IFNg.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 10, 6, 693, 284, False))
  #Regions.Border.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Border, 735, 465, 300, 128, False))
  #Regions.IL_10.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 13, 10, 694, 281, False))
  
  
  

def Test6():
  border = Aliases.Quantist.MainWindowView.Viewer
  border.GridSplitter2.Drag(962, 0, -47, -495)
  scrollViewer = border.ScrollViewer
  scrollViewer.ButtonCollapseAll.ClickButton()
  scrollViewer.ButtonExpandAll.ClickButton()
  treeListView = border.ztreeListView1
  treeListView.RowMarginControl.Click(12, 8)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Viewer.ztreeListView1.InplaceBaseEdit, "DisplayText", cmpEqual, "Background0")
  rowMarginControl = treeListView.RowMarginControl2
  rowMarginControl.Click(13, 10)
  treeListView.InplaceBaseEdit2.Click(32, 9)
  treeListView.InplaceBaseEdit3.Click(34, 13)
  rowMarginControl.Click(9, 9)

def Test7():
  pass
