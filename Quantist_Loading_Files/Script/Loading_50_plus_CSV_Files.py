﻿import Load_CSV_File 
import Quantist_Removing_Files

def Loading_50_Plus():
  
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
    #treeView.TreeViewItem.Button.ClickButton()
     
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
    UIItem.Keys("^a")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Aliases.Quantist.dlgOpen.btnOpen.ClickButton()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox, "Enabled", cmpEqual, True)
  main.MaxButtonOk.ClickButton()
  
