def CC_Configuration():

  config = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
  Regions.PM8800_B7_H1_5PL_1Y2_80_120.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel, False, False, 21869, 17)
  Regions.PM8800_B7_H1_5PL_1Y2_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)

  config = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
  config.CurveWeightingBox.ClickItem("None")
  Regions.PM8800_B7_H1_5PL_None_80_120.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel, False, False, 21869, 17)
  Regions.PM8800_B7_H1_5PL_None_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  
  config.CurveWeightingBox.ClickItem("OneOverY")
  Regions.PM8800_B7_H1_5PL_1Y_80_120.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel, False, False, 21869, 17)
  Regions.PM8800_B7_H1_5PL_1Y_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  
  config.CurveFitBox.ClickItem("FourPL")
  Regions.PM8800_B7_H1_4PL_1Y_80_120.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel, False, False, 21869, 17)
  Regions.PM8800_B7_H1_4PL_1Y_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  
  config.CurveWeightingBox.ClickItem("None")
  Regions.PM8800_B7_H1_4PL_None_80_120.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel, False, False, 21869, 17)
  Regions.PM8800_B7_H1_4PL_None_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  
  config.CurveWeightingBox.ClickItem("OneOverYSquared")
  Regions.PM8800_B7_H1_4PL_1Y2_80_120.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel, False, False, 21869, 17)
  Regions.PM8800_B7_H1_4PL_1Y2_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 22513, 17)
  
def CC_Configuration_BK():
  
  config = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
  config.CurveFitBox.ClickItem("FourPL")
  config.CurveWeightingBox.ClickItem("None")
  config.RecoverRangeBox.ClickItem("From60To140")
  Regions.PM8800_B7_H1_CurveData_4PL_None_60.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxCurrentCurveData, False, False, 6591, 17)
  Regions.PM8800_B7_H1_CurveConfig_4PL_None_60.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve, False, False, 4515, 17)

  ############################################  
  config.CurveFitBox.ClickItem("FivePL")
  config.CurveWeightingBox.ClickItem("None")
  config.RecoverRangeBox.ClickItem("From60To140")
  Regions.PM8800_B7_H1_CurveData_5PL_None_60.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxCurrentCurveData, False, False, 6591, 17)    

  gridData = Aliases.Quantist.MainWindowView.MainView.CurveData
  #aqObject.CheckProperty(gridData.InplaceBaseEdit, "DisplayText", cmpEqual, "88.35")
  
  # Verify Standard7 (both H1/H2) are out of recovery range: 60-140%
  aqObject.CheckProperty(gridData.InplaceBaseEdit2, "DisplayText", cmpEqual, "55.13")
  
  # Verify Standard6 and Standard7 Concentration are < LLOQ= 192.06
  aqObject.CheckProperty(gridData.InplaceBaseEdit5, "DisplayText", cmpEqual, "<LLOQ")
  aqObject.CheckProperty(gridData.InplaceBaseEdit6, "DisplayText", cmpEqual, "<LLOQ")
  aqObject.CheckProperty(gridData.InplaceBaseEdit3, "DisplayText", cmpEqual, "175.99")
  aqObject.CheckProperty(gridData.InplaceBaseEdit4, "DisplayText", cmpEqual, "35.29")

  # Verify Standard1 Concentration is > ULOQ= 46670  
  aqObject.CheckProperty(gridData.InplaceBaseEdit7, "DisplayText", cmpEqual, "46743.60") #std 1 Conc
  aqObject.CheckProperty(gridData.GridData.InplaceBaseEdit5, "DisplayText", cmpEqual, ">ULOQ")   #std 1 status

  ############################################
  config.CurveFitBox.ClickItem("FivePL")
  config.CurveWeightingBox.ClickItem("None")
  config.RecoverRangeBox.ClickItem("From90To110")
  Regions.PM8800_B7_H1_CurveData_5PL_None_90.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxCurrentCurveData, False, False, 6591, 17)

  # Verify Standard7 is out of recovery range: 90-110%  
  aqObject.CheckProperty(gridData.InplaceBaseEdit2, "DisplayText", cmpEqual, "55.13")
  
  # Verify Standard6 and Standard7 Concentration are < LLOQ= 192.06  
  aqObject.CheckProperty(gridData.InplaceBaseEdit5, "DisplayText", cmpEqual, "<LLOQ")  #std 6 status
  aqObject.CheckProperty(gridData.InplaceBaseEdit6, "DisplayText", cmpEqual, "<LLOQ")  #std 7 status

  aqObject.CheckProperty(gridData.InplaceBaseEdit3, "DisplayText", cmpEqual, "175.99") #std 6 Conc
  aqObject.CheckProperty(gridData.InplaceBaseEdit4, "DisplayText", cmpEqual, "35.29")  #std 7 Conc
  
  # Verify Standard1 Concentration is > ULOQ= 46670   
  aqObject.CheckProperty(gridData.GridData.InplaceBaseEdit, "DisplayText", cmpEqual, "46743.60") #std 1 Conc
  aqObject.CheckProperty(gridData.GridData.InplaceBaseEdit5, "DisplayText", cmpEqual, ">ULOQ")   #std 1 status

