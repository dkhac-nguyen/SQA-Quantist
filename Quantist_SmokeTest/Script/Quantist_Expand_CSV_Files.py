def Expanding_CSV_Files():
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.CollapseButton.ClickButton()
  i = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFControlOrdinalNo
  Log.Message("Total Number of loading items: " + aqConvert.VartoStr(i))

  Regions.RunTreeView_Collapse.Check(Aliases.Quantist.MainWindowView.RunTreeView)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Aliases.Quantist.MainWindowView.ExpandingButton.ClickButton()
  Regions.RunTreeView_Expand.Check(Aliases.Quantist.MainWindowView.RunTreeView)

  count=1
  j = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.ChildCount

  while (count < 6):  #maximum 6 expanding items in the tree
    if (Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFObject("TreeViewItem", "", count).Exists):
      Log.Message("Visible? " + aqConvert.VarToStr(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFObject("TreeViewItem", "", count).Visible))
      Log.Message("Item: " + aqConvert.VarToStr(count) + " is in the tree view") 
    else:
      Log.Message("Visible? " + aqConvert.VarToStr(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFObject("TreeViewItem", "", count).Visible))
    count += 1
  Log.Message("Total Number of expanding items: " + aqConvert.VartoStr(j))
    
def Expanding_Old():
  mainWindowView = Aliases.Quantist.MainWindowView
  treeView = mainWindowView.RunTreeView
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  treeView.ExpandItem("|[0]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ExpandItem("|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ExpandItem("|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ExpandItem("|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Togglebutton.ClickButton(cbChecked)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[1]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[2]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[3]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Togglebutton2.ClickButton(cbChecked)
  mainWindowView.Button2.ClickButton()
  #BuiltIn.ShowMessage("Successfully expanding Kit Results!")

