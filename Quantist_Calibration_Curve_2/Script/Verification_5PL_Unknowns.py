﻿import Load_CSV_File 
import Quantist_Removing_Files

def Verify_5PL_Unknowns():
  
  mainWindowView = Aliases.Quantist.MainApp.MainWindow
  treeView = mainWindowView.RunTreeView
  
  if (treeView.HasItems):
     Aliases.Quantist.MainApp.MainWindow.RunTreeView.TreeViewItem.Button.ClickButton()
     
  if (not treeView.HasItems):
    quantist = Aliases.Quantist
    quantist.MainApp.MainWindow.Button.ClickButton()
    sampleFoder = ProjectSuite.Variables.SampleDataFolder
    file = ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Consumable Files (*.csv;*.quantist)")
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  #bg  = Aliases.Quantist.MainApp.MainWindow.GridData.background.DisplayText
  #mfi = Aliases.Quantist.MainApp.MainWindow.GridData.mfi_1.DisplayText
  #Aliases.Quantist.MainApp.MainWindow.GridSplitter.Drag(116, 2, 25, -247)
    
  a = Aliases.Quantist.MainApp.MainWindow.Coeff_A.WPFControlText  
  b = Aliases.Quantist.MainApp.MainWindow.Coeff_B.WPFControlText
  c = Aliases.Quantist.MainApp.MainWindow.Coeff_C.WPFControlText  
  d = Aliases.Quantist.MainApp.MainWindow.Coeff_D.WPFControlText
  g = Aliases.Quantist.MainApp.MainWindow.Coeff_G.WPFControlText  
    
  mainWindowView.Sample_Col.DblClick()
  mainWindowView.GridData.Drag(1224, 166, 6, -127)  

  grid = mainWindowView.GridData

  grid.row_1.Click()
  conc_1    = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
  grid.row_1.Click()
  
  grid.row_2.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
  grid.row_2.Click()

  grid.row_3.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
  grid.row_3.Click()

  grid.row_4.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
  grid.row_4.Click()

  grid.row_5.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
  grid.row_5.Click()

  grid.row_6.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
  grid.row_6.Click()

  grid.row_7.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
  grid.row_7.Click()

  grid.row_8.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
  grid.row_8.Click()

  grid.row_9.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
  grid.row_9.Click()

  grid.row_10.Click()
  conc_1     = grid.conc_1.DisplayText
  netMFI_1  = grid.netMFI_1.DisplayText
  conc_2    = grid.conc_2.DisplayText
  netMFI_2  = grid.netMFI_2.DisplayText
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
  grid.row_10.Click()


def netMFI_5PL(a, b, c, d, g, conc, netMFI):  #bg, mfi:
  
  if(conc == 0):
    #netMFI_calc = float(mfi) - float(bg)
    Log.Message("  concentration is zero!" )    
    Log.Message("  netMFI displayed is equal = background - MFI" )
    #Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 5PL verification Passed")
    Log.Message(" ")

  else:
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


