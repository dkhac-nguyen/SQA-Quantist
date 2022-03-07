# Test data file: PM8880
# Analyte: B7-H1
# Curve Fit: 5PL / 4PL
# Curve Weighting: 1/Ysq
# Recovery Range: 80-120%

import Load_CSV_File 
import Quantist_Removing_Files

def Calculate_netMFI_5PL():
  
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve.CurveFitBox.ClickItem("FivePL")
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve.Btn_CopyToAll_CurveFit.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  i = 0
  while (i < 50):
    
#    if (i == 1):
#      Log.Message("Pause here")  
      
    Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.ClickItem(i)
    analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wText
    Log.Message(" ")
    Log.Message("Analyte: " + analyte)
  
    curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel

    a = curveData.AValue.WPFControlText
    b = curveData.BValue.WPFControlText
    c = curveData.CValue.WPFControlText
    d = curveData.DValue.WPFControlText
    g = curveData.GValue.WPFControlText

    grid = Aliases.Quantist.MainWindowView.MainView.CurveData
    grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl2.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  
    
    conc_B1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for B1
    conc_B2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for B2
    netMFI_B1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for B1
    netMFI_B2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for B2    

    #  conc = Aliases.Quantist.MainWindowView.Conc_Std1.DisplayText
    #  mainWindowView.InplaceBaseEdit2.Click()
    #  Regions.Standard1_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
    #  conc       = Aliases.Quantist.MainWindowView.Std1_5PL_None_60_140_Conc_ULOQ.DisplayText
    #  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std1.DisplayText
        
    Log.Message("Standard1")
    if ((conc_B1 != "") and (conc_B2 != "")):
      # perform 5PL calculation and verify displayed NetMFI value
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_B1), float(netMFI_B1))  
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_B2), float(netMFI_B2))  
    else:
      Log.Message("Concentration cannot be calculated. Net MFI > d coefficient!")

  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl2.Click() # Collapse Standard1
    grid.InplaceBaseEdit16.Click()  
    grid.RowMarginControl3.Click() # Expand Standard2
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_C1 = grid.InplaceBaseEdit14.DisplayText
    conc_C2 = grid.GridData.InplaceBaseEdit.DisplayText
    netMFI_C1 = grid.InplaceBaseEdit15.DisplayText
    netMFI_C2 = grid.GridData.InplaceBaseEdit2.DisplayText    

    # perform 5PL calculation and verify displayed NetMFI value
    Log.Message("Standard2")
    if ((conc_C1 != "") and (conc_C2 != "")):
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_C1), float(netMFI_C1))  
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_C2), float(netMFI_C2))  
    else:
      Log.Message("Concentration cannot be calculated. Net MFI > d coefficient!")

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl3.Click() # Collapse Standard2
    grid.InplaceBaseEdit17.Click()
    grid.RowMarginControl4.Click() # Expand Standard3
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  
  
    conc_D1 = grid.InplaceBaseEdit14.DisplayText
    conc_D2 = grid.GridData.InplaceBaseEdit.DisplayText
    netMFI_D1 = grid.InplaceBaseEdit15.DisplayText
    netMFI_D2 = grid.GridData.InplaceBaseEdit2.DisplayText    

    Log.Message("Standard3")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_D1), float(netMFI_D1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_D2), float(netMFI_D2))  

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl4.Click() # Collapse Standard3
    grid.InplaceBaseEdit18.Click()
    grid.RowMarginControl5.Click() # Expand Standard4
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_E1 = grid.InplaceBaseEdit14.DisplayText
    conc_E2 = grid.GridData.InplaceBaseEdit.DisplayText
    netMFI_E1 = grid.InplaceBaseEdit15.DisplayText
    netMFI_E2 = grid.GridData.InplaceBaseEdit2.DisplayText    

    Log.Message("Standard4")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_E1), float(netMFI_E1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_E2), float(netMFI_E2))    

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl5.Click() # Collapse Standard4
    grid.InplaceBaseEdit19.Click()
    grid.RowMarginControl6.Click() # Expand Standard5
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_F1 = grid.InplaceBaseEdit14.DisplayText
    conc_F2 = grid.GridData.InplaceBaseEdit.DisplayText
    netMFI_F1 = grid.InplaceBaseEdit15.DisplayText
    netMFI_F2 = grid.GridData.InplaceBaseEdit2.DisplayText    

    Log.Message("Standard5")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_F1), float(netMFI_F1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_F2), float(netMFI_F2))        
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl6.Click() # Collapse Standard5
    grid.InplaceBaseEdit20.Click()
    grid.RowMarginControl7.Click() # Expand Standard6
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_G1 = grid.InplaceBaseEdit14.DisplayText
    conc_G2 = grid.GridData.InplaceBaseEdit.DisplayText
    netMFI_G1 = grid.InplaceBaseEdit15.DisplayText
    netMFI_G2 = grid.GridData.InplaceBaseEdit2.DisplayText    

    Log.Message("Standard6")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_G1), float(netMFI_G1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_G2), float(netMFI_G2))  

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl7.Click() # Collapse Standard6
    grid.InplaceBaseEdit21.Click()
    grid.RowMarginControl8.Click() # Expand Standard7
    grid.GridData.InplaceBaseEdit4.Click()  
    grid.GridData.InplaceBaseEdit3.Click()  
  
    conc_H1 = grid.InplaceBaseEdit14.DisplayText
    conc_H2 = grid.GridData.InplaceBaseEdit.DisplayText
    netMFI_H1 = grid.InplaceBaseEdit15.DisplayText
    netMFI_H2 = grid.GridData.InplaceBaseEdit2.DisplayText    

    Log.Message("Standard7")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_H1), float(netMFI_H1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_H2), float(netMFI_H2))

    grid.RowMarginControl8.Click() # Collapse Standard7        

    i += 1
      
#  mainWindowView.InplaceBaseEdit3.Click()
#  Regions.Standard2_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std2.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std2.DisplayText
#  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc), float(netMFI_Std))
#
#  mainWindowView.InplaceBaseEdit4.Click()
#  Regions.Standard3_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std3.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std3.DisplayText
#  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc), float(netMFI_Std))  
#
#  mainWindowView.InplaceBaseEdit5.Click()
#  Regions.Standard4_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std4.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std4.DisplayText
#  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc), float(netMFI_Std))
#
#  mainWindowView.InplaceBaseEdit8.Click()
#  Regions.Standard5_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std5.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std5.DisplayText
#  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc), float(netMFI_Std))
#
#  mainWindowView.InplaceBaseEdit6.Click()
#  Regions.Standard6_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Std6_5PL_None_60_140_Conc_LLOQ.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std6.DisplayText
#  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc), float(netMFI_Std))  
#  
#  #conc       = Aliases.Quantist.MainWindowView.Conc_Std7.DisplayText
#  mainWindowView.InplaceBaseEdit7.Click()
#  Regions.Standard7_netMFI.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140_Conc_LLOQ.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std7.DisplayText
#  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc), float(netMFI_Std))

  #Exp_Conc = 54235.57   # ==> 6462.69089849102 vs 6457.50
  #Exp_Conc = 14971.56  # ==> 3012.984001793	 vs 3013.75
  #Exp_Conc = 4839.18  # ==>  1260.84274731892  vs 1262.00
  #Exp_Conc = 1739.15 # 526.255677533441 vs 527
  #Exp_Conc = 580.55  # 200.094123383476	 vs 200.50
  #Exp_Conc = 203.60  # 80.3015237124273  vs 80.50
  #Exp_Conc = 62.83 #30.9181897298859 vs 31.00
  #Exp_Conc = 95.15 # ==> 42.7203591172238  vs 38  Note: Out of range point
  #Exp_Conc = 30785.94 ==> 4794.60719341154	vs 4244.50 Note: Out of range point
  
def netMFI_5PL(a, b, c, d, g, conc, netMFI):
  netMFI_calc = (d + ((a-d) / pow((1+ pow((conc/c), b)), g)))
  if (int(netMFI_calc) == int(netMFI) or ((netMFI_calc / netMFI) < 1.0)):
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 5PL verification Passed")
    Log.Message(" ")
    #Log.Message((netMFI_calc / netMFI))  

  else:
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 5PL verification Failed")
    Log.Message(" ")

def Calculate_netMFI_4PL():
  
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")


  curve = Aliases.Quantist.MainWindowView.MainView.CurvePanel
  curve.ConfigureCurve.CurveFitBox.ClickItem("FourPL")

  i = 0
  while (i < 30):
    
    Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.ClickItem(i)
    analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wText
    Log.Message(" ")
    Log.Message("Analyte: " + analyte)

    grid = Aliases.Quantist.MainWindowView.MainView.CurveData
    curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel

    a = curveData.AValue.WPFControlText
    b = curveData.BValue.WPFControlText
    c = curveData.CValue.WPFControlText
    d = curveData.DValue.WPFControlText

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
    grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl2.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_B1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for B1
    conc_B2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for B2
    netMFI_B1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for B1
    netMFI_B2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for B2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard1")    
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_B1), float(netMFI_B1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_B2), float(netMFI_B2))  
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl2.Click() # To colapse Standard1
    grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl3.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_C1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for C1
    conc_C2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for C2
    netMFI_C1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for C1
    netMFI_C2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for C2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard2")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_C1), float(netMFI_C1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_C2), float(netMFI_C2))      
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl3.Click() # To colapse Standard2
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl4.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_D1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for D1
    conc_D2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for D2
    netMFI_D1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for D1
    netMFI_D2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for D2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard3")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_D1), float(netMFI_D1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_D2), float(netMFI_D2))

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl4.Click() # To colapse Standard3
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl5.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_E1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for E1
    conc_E2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for E2
    netMFI_E1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for E1
    netMFI_E2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for E2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard4")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_E1), float(netMFI_E1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_E2), float(netMFI_E2))  

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl5.Click() # To colapse Standard4
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl6.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_F1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for F1
    conc_F2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for F2
    netMFI_F1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for F1
    netMFI_F2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for F2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard5")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_F1), float(netMFI_F1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_F2), float(netMFI_F2))      
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl6.Click() # To colapse Standard5
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl7.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_G1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for G1
    conc_G2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for G2
    netMFI_G1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for G1
    netMFI_G2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for G2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard6")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_G1), float(netMFI_G1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_G2), float(netMFI_G2))    
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl7.Click() # To colapse Standard6
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl8.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_H1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for H1
    conc_H2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for H2
    netMFI_H1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for H1
    netMFI_H2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for H2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard7")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_H1), float(netMFI_H1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_H2), float(netMFI_H2)) 
   
    i += 1
        
#  mainWindowView.InplaceBaseEdit2.Click()
#  Regions.Standard1_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Std1_5PL_None_60_140_Conc_ULOQ.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std1.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))  
#
#  mainWindowView.InplaceBaseEdit3.Click()
#  Regions.Standard2_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std2.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std2.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))
#
#  mainWindowView.InplaceBaseEdit4.Click()
#  Regions.Standard3_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std3.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std3.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))  
#  
#  mainWindowView.InplaceBaseEdit5.Click()
#  Regions.Standard4_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std4.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std4.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))
#
#  mainWindowView.InplaceBaseEdit8.Click()
#  Regions.Standard5_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Conc_Std5.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std5.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))
#
#  mainWindowView.InplaceBaseEdit6.Click()
#  Regions.Standard6_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Std6_5PL_None_60_140_Conc_LLOQ.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std6.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))  
#
#  mainWindowView.InplaceBaseEdit7.Click()
#  Regions.Standard7_netMFI_4PL.Check(Aliases.Quantist.MainWindowView.Grid_B1_Unchecked)
#  conc       = Aliases.Quantist.MainWindowView.Std7_5PL_None_60_140_Conc_LLOQ.DisplayText
#  netMFI_Std = Aliases.Quantist.MainWindowView.NetMFI_Std7.DisplayText
#  netMFI_4PL (float(a), float(b), float(c), float(d), float(conc), float(netMFI_Std))  
  
def netMFI_4PL(a, b, c, d, conc, netMFI):
  netMFI_calc = (d + ((a-d) / (1+ pow((conc/c), b))))

  #if ((netMFI_calc / netMFI) < 1.1):
  if (int(netMFI_calc) == int(netMFI) or ((netMFI_calc / netMFI) < 1.0)):
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 4PL verification Passed:")
    Log.Message(" ")
    #Log.Message((netMFI_calc / netMFI))  

  else:
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 4PL verification Failed")
    Log.Message(" ")

def Test1():
  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData
  OCR.Recognize(treeListControl.InplaceBaseEdit13).BlockByText("Standard").Click()
  treeListControl.RowMarginControl2.Click(10, 10)
  aqObject.CheckProperty(treeListControl.InplaceBaseEdit14, "DisplayText", cmpEqual, "57459.38") #B1 Conc
  aqObject.CheckProperty(treeListControl.InplaceBaseEdit15, "DisplayText", cmpEqual, "6639.00") #B1 NetMFI
  treeListView = treeListControl.GridData
  aqObject.CheckProperty(treeListView.InplaceBaseEdit, "DisplayText", cmpEqual, "51011.76") #B2 Conc
  aqObject.CheckProperty(treeListView.InplaceBaseEdit2, "DisplayText", cmpEqual, "6276.00") #B2 NetMFI

def Test3():
  grid = Aliases.Quantist.MainWindowView.MainView.CurveData
  grid.RowMarginControl2.Click()
  NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.ztreeListControl1.RowControl9.LightweightCellEditor4.InplaceBaseEdit.Click(79, 7)
  gridSub = grid.GridData
  gridSub.InplaceBaseEdit3.Click()
  aqObject.CheckProperty(grid.InplaceBaseEdit14, "DisplayText", cmpEqual, "60946.55")
  aqObject.CheckProperty(grid.InplaceBaseEdit15, "DisplayText", cmpEqual, "6639.00")
  aqObject.CheckProperty(gridSub.InplaceBaseEdit, "DisplayText", cmpEqual, "53375.18")
  aqObject.CheckProperty(gridSub.InplaceBaseEdit2, "DisplayText", cmpEqual, "6276.00")

def Test2():
  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData
  rowMarginControl = treeListControl.RowMarginControl3
  rowMarginControl.Click(10, 11)
  rowMarginControl.Click(10, 11)
  rowMarginControl = treeListControl.RowMarginControl4
  rowMarginControl.Click(11, 8)
  rowMarginControl.Click(11, 8)
  rowMarginControl = treeListControl.RowMarginControl5
  rowMarginControl.Click(12, 10)
  rowMarginControl.Click(12, 10)
  rowMarginControl = treeListControl.RowMarginControl6
  rowMarginControl.Click(10, 7)
  rowMarginControl.Click(10, 7)
  rowMarginControl = treeListControl.RowMarginControl7
  rowMarginControl.Click(12, 10)
  rowMarginControl.Click(11, 10)
  rowMarginControl = treeListControl.RowMarginControl8
  rowMarginControl.Click(13, 7)
  rowMarginControl.Click(13, 7)


def Calculate_5PL_Unknowns():
  
  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData
  treeListView = treeListControl.GridData
  gridColumnHeader = treeListView.GridColumnHeader
  gridColumnHeader.Click()
  gridColumnHeader.Click()
  treeListView.Drag(1225, 200, -2, -153)
  
  curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel

  a = curveData.AValue.WPFControlText
  b = curveData.BValue.WPFControlText
  c = curveData.CValue.WPFControlText
  d = curveData.DValue.WPFControlText
  g = curveData.GValue.WPFControlText

#  grid = Aliases.Quantist.MainWindowView.MainView.CurveData
#  grid.InplaceBaseEdit13.Click()
#  grid.RowMarginControl2.Click()
#  grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for review works
#  grid.GridData.InplaceBaseEdit3.Click()  
    
#  conc_1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for B1
#  conc_2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for B2
#  netMFI_1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for B1
#  netMFI_2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for B2    
#  
  rowMarginControl = treeListControl.RowMarginControl2
  
  treeListControl.RowMarginControl.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  conc_1 = treeListControl.InplaceBaseEdit22.DisplayText
                    #aqObject.CheckProperty(inplaceBaseEdit, "DisplayText", cmpEqual, "0.00")
  conc_2 = treeListControl.InplaceBaseEdit14.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit3, "DisplayText", cmpEqual, "194.86")
  netMFI_1 = treeListControl.InplaceBaseEdit23.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit2, "DisplayText", cmpEqual, "-0.50")
  netMFI_2 = treeListControl.InplaceBaseEdit15.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit4, "DisplayText", cmpEqual, "78.00")
  treeListControl.RowMarginControl.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  

  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))

######################################################  
  treeListControl.RowMarginControl4.Click()
  conc_1 = treeListControl.InplaceBaseEdit.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit, "DisplayText", cmpEqual, "55.29")
  netMFI_1 = treeListControl.InplaceBaseEdit2.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit2, "DisplayText", cmpEqual, "28.00")
  conc_2 = treeListControl.InplaceBaseEdit3.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit3, "DisplayText", cmpEqual, "0.23")
  netMFI_2 = treeListControl.InplaceBaseEdit4.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit4, "DisplayText", cmpEqual, "5.00")
  treeListControl.RowMarginControl4.Click()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))

def Test4():
  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData

  treeListControl.RowMarginControl.Click(11, 14)
  treeListControl.RowMarginControl.Click(11, 14)
  
  treeListControl.RowMarginControl4.Click(12, 10)
  treeListControl.RowMarginControl4.Click(11, 11)

  treeListControl.RowMarginControl5.Click(9, 6)
  treeListControl.RowMarginControl5.Click(9, 7)

def Test5():
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve.CurveFitBox.ClickItem("FivePL")

def Test6():
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve.Btn_CopyToAll_CurveFit.ClickButton()
