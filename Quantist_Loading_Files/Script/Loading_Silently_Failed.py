import Load_CSV_File 
import Quantist_Removing_Files

def silently_failed():
  
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  while (treeView.HasItems):
     treeView.TreeViewItem.DeleteButton.ClickButton()
     
  if (not treeView.HasItems):
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    sampleFoder = ProjectSuite.Variables.SampleInvalidCSVFolder
    file = ProjectSuite.Variables.sample_csv_silent_failed
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox, "Enabled", cmpEqual, True)
  Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()
