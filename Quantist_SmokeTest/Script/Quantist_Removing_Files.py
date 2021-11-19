def Removing_CSV_Files():
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.delete_Button

  while (treeView.HasItems): 
    Xbutton.ClickButton()
    if (not treeView.HasItems):
      break
            
#  for i in range(16):
#    Xbutton.ClickButton()
#    Log.Message("Tree View now has " + aqConvert.VarToStr(15-i) + " loaded CSV files")

def Test():
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.delete_Button
  
  while (treeView.HasItems): 
    Xbutton.ClickButton()
    #if (aqObject.CheckProperty(treeView, "HasItems", cmpEqual, False)):
    if (not treeView.HasItems):
      break

