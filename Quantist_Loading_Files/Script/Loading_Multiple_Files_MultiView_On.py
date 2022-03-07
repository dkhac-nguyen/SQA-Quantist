﻿import Load_CSV_File 
import Quantist_Removing_Files

def Loading_Multiple_Files_MultiView_On():
  
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()  

  #Enable ShareView (Click on ShaveView button)
  state = quantist.MainWindowView.ToggleShareView.wState
  Log.Message("ShareView button is enabled: " + str(bool(state)))
  if (quantist.MainWindowView.ToggleShareView.wState == cbUnchecked):
    Log.Message("Enable ShareView button")
    quantist.MainWindowView.ToggleShareView.ClickButton(cbChecked)

  if (not treeView.HasItems):
    main.LoadButton.ClickButton()
    dlgOpen = quantist.dlgOpen
    
    pane = dlgOpen.DUIViewWndClassName.Explorer_Pane
    tree = pane.CtrlNotifySink2.NamespaceTreeControl.tvNamespaceTreeControl
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data")
    tree.ClickItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data|67 files")
    UIItem = pane.CtrlNotifySink.ShellView.Items_View.HMHMAG_with_Controls_csv

    UIItemsView = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View
    UIItemsView.HMHMAG_with_Controls_csv.Name.Click()
    UIItemsView.Plate_2_Panel_1_Acquisition_1_PlateRunResults_csv.Name.Click(33, 9, skShift)
    dlgOpen.btnOpen.ClickButton()
    
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  #To be continued:
  #Add more checking here

def Test1():
  pass
