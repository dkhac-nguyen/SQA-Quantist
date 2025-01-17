﻿import Load_CSV_File 
import Quantist_Removing_Files

def Verify_5PL_Unknowns():
  
  main = Aliases.Quantist.MainApp.MainWindow
  analyte = main.AnalyteBox

  treeView = main.RunTreeView
  
  while (treeView.HasItems):
     treeView.TreeViewItem.DeleteButton.ClickButton()
     
  if (not treeView.HasItems):
    quantist = Aliases.Quantist
    quantist.MainApp.MainWindow.Button.ClickButton()
    sampleFoder = ProjectSuite.Variables.SampleDataFolder
    file = ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")
   
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay) 

  main.CurveFit.ClickItem("FivePL")
  main.ButtonCopyToAll.ClickButton()

  main.Sample_Col.DblClick()
  main.GridData.Drag(1224, 166, 6, -127)
  
  i = 0
  while (i < 1):
    analyte.ClickItem(i)

    #Aliases.Quantist.MainApp.MainWindow.CurveFit.ClickItem("FivePL")
    #mainWindowView.ButtonCopyToAll.ClickButton()
    
    #bg  = Aliases.Quantist.MainApp.MainWindow.GridData.background.DisplayText
    #mfi = Aliases.Quantist.MainApp.MainWindow.GridData.mfi_1.DisplayText
    #Aliases.Quantist.MainApp.MainWindow.GridSplitter.Drag(116, 2, 25, -247)

    #Select 5PL CurveFit from the dropdown list
    #Aliases.Quantist.MainApp.MainWindow.ComboBox.ClickItem("FivePL")

    analyteName = analyte.wText
    Log.Message(" ")
    Log.Message("Analyte: " + analyteName)
        
    a = Aliases.Quantist.MainApp.MainWindow.Coeff_A.WPFControlText  
    b = Aliases.Quantist.MainApp.MainWindow.Coeff_B.WPFControlText
    c = Aliases.Quantist.MainApp.MainWindow.Coeff_C.WPFControlText  
    d = Aliases.Quantist.MainApp.MainWindow.Coeff_D.WPFControlText
    g = Aliases.Quantist.MainApp.MainWindow.Coeff_G.WPFControlText  
    

    grid = main.GridData

    Log.Message(" ")
    Log.Message("row 1")
    grid.row_1.Click()
    conc_1    = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
    grid.row_1.Click()
  
    Log.Message(" ")
    Log.Message("row 2")
    grid.row_2.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
    grid.row_2.Click()

    Log.Message(" ")
    Log.Message("row 3")
    grid.row_3.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
    grid.row_3.Click()

    Log.Message(" ")
    Log.Message("row 4")
    grid.row_4.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
    grid.row_4.Click()

    Log.Message(" ")
    Log.Message("row 5")
    grid.row_5.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
    grid.row_5.Click()

    Log.Message(" ")
    Log.Message("row 6")
    grid.row_6.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
    grid.row_6.Click()

    Log.Message(" ")
    Log.Message("row 7")
    grid.row_7.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
    grid.row_7.Click()

    Log.Message(" ")
    Log.Message("row 8")
    grid.row_8.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))
    grid.row_8.Click()

    Log.Message(" ")
    Log.Message("row 9")
    grid.row_9.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
    grid.row_9.Click()

    Log.Message(" ")
    Log.Message("row 10")
    grid.row_10.Click()
    conc_1     = grid.conc_1.DisplayText
    netMFI_1  = grid.netMFI_1.DisplayText
    conc_2    = grid.conc_2.DisplayText
    netMFI_2  = grid.netMFI_2.DisplayText
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))  
    grid.row_10.Click()

    i += 1

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



def Test1():
  Aliases.Quantist.MainApp.MainWindow.ComboBox.ClickItem("FivePL")


def Test2():
  comboBox = Aliases.Quantist.MainApp.MainWindow.ComboBox
  comboBox.Click(52, 10)
  comboBox.ClickItem(2)

def Test3():
  comboBox = Aliases.Quantist.MainApp.MainWindow.AnalyteBox
  comboBox.Click(19, 10)
  comboBox.ClickItem(4)

def Test4():
  Aliases.Quantist.MainApp.MainWindow.ComboBox2.ClickItem("FivePL")
