import Load_CSV_File 
import Quantist_Removing_Files

def Remove_Outliers():
  quantist = Aliases.Quantist
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "TestData.csv")
    ProjectSuite.Variables.Long_Delay    

    #Regions.TestData_main_before.Check(Aliases.Quantist.MainWindowView.MainView)
    Regions.TestData_main_before.Check(Aliases.Quantist.MainWindowView.MainView, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
    
    # DataPoints -"Current Curve Remove Outliers" for config at "Recovery Range 90-110%" 
    main = Aliases.Quantist.MainWindowView.MainViewRunCtr
    analyte = quantist.MainWindowView.MainView.CurvePanel.AnalyteBox
    curvePanel = Aliases.Quantist.MainWindowView.MainView.CurvePanel
    
    configCurve = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
    tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions

    #Select Recovery Range 90-110%
    configCurve.RecoverRangeBox.ClickItem("From90To110")
    ProjectSuite.Variables.Short_Delay

    #Remove Outliers for current curve
    configCurve.ButtonForCurrentCurveOnly.ClickButton()

    #Verify that the outliers have been removed from calculation + curve plot
    Regions.TestData_main_after_removeOutliers.Check(Aliases.Quantist.MainWindowView.MainView, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)

    #Reset Include Standards + config at "Recovery Range 80-120%" should bring back DataPoints as they were initially loaded  
    ProjectSuite.Variables.Short_Delay    
    
    if (tblOption.ButtonStandards.IsEnabled):
      tblOption.ButtonStandards.ClickButton()
      configCurve.RecoverRangeBox.ClickItem("From80To120")
      ProjectSuite.Variables.Short_Delay    
      Regions.TestData_main_before.Check(Aliases.Quantist.MainWindowView.MainView, False, False, 4423, ProjectSuite.Variables.COLOR_TOLERANCE)

  #Verify MIP_3alpha analyte before applying removing outliers 
  analyte.ClickItem(4)
  Regions.CurveView_MIP_3alpha_before.Check(main, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
  #Verify MDC analyte
  analyte.ClickItem(5)
  Regions.CurveView_MDC_before.Check(main, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
  #Verify MIP_1alpha analyte
  analyte.ClickItem(6)
  Regions.CurveView_MIP_1alpha_before.Check(main, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)

  #Apply Remove Outliers for ALL- Recovery Range of 80-120%
  curvePanel.ConfigureCurve.ButtonForAll.ClickButton()

  #Verify MIP_3alpha analyte after applying removing outliers
  analyte.ClickItem(4)
  Regions.CurveView_MIP_3alpha_after.Check(main, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
  
  #Verify MDC analyte after applying removing outliers
  analyte.ClickItem(5)
  Regions.CurveView_MDC_after.Check(main, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
  
  #Verify MIP_1alpha analyte after applying removing outliers
  analyte.ClickItem(6)
  Regions.CurveView_MIP_1alpha_after.Check(main, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)

  #Reset Included Standards
  #curvePanel.GroupboxTableOptions.ButtonStandards.ClickButton()
      
      
def Test2():
  configCurve = Aliases.Quantist.MainWindowView.MainView.ScrollViewer.ConfigureCurve
  configCurve.RecoverRangeBox.ClickItem("From80To120")
  configCurve.ButtonForCurrentCurveOnly.ClickButton()
  configCurve.ButtonForAll.ClickButton()
  configCurve.CurveWeightingBox.ClickItem("None")
  configCurve.CurveFitBox.ClickItem("FourPL")
def Test3():
  tblOption = Aliases.Quantist.MainWindowView.MainView.ScrollViewer.GroupboxTableOptions
  tblOption.ButtonStandards.ClickButton()
  tblOption.ButtonUnksCtrls.ClickButton()
  tblOption.ButtonAggregates.ClickButton()
  tblOption.ButtonReplicates.ClickButton()
  tblOption.ButtonExpandAll.ClickButton()
  tblOption.ButtonCollapseAll.ClickButton()
