import Quantist_Removing_Files
import Load_CSV_File 

def Load_CSV_Files():
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.MainWindowView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  if (treeView.HasItems):
     Quantist_Removing_Files.Removing_CSV_Files()  

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  quantist.MainWindowView.LoadButton.ClickButton()    
  dlgOpen = quantist.dlgOpen
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv
  UIItem.Keys("^a")

  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Aliases.Quantist.MainWindowView.ToggleShareView.ClickButton(cbChecked)  

  treeView = mainWindowView.RunTreeView
  treeView.ClickItem("|[0]|[0]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[1]|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[2]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[3]|[3]")  

  Regions.Horizontal_ShareView.Check(Aliases.Quantist.MainWindowView)
  Aliases.Quantist.MainWindowView.ToggleVerticalButton.ClickButton(cbChecked)

  ProjectSuite.Variables.Short_Delay  
  Regions.Vertical_ShareView.Check(Aliases.Quantist.MainWindowView)  

  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.ToggleVerticalButton.ClickButton(cbUnChecked)

  ProjectSuite.Variables.Short_Delay
  Regions.Horizontal_ShareView.Check(Aliases.Quantist.MainWindowView, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
    
      
def Load_A_file():
  quantist = Aliases.Quantist
  quantist.MainWindowView.LoadButton.ClickButton()
  dlgOpen = quantist.dlgOpen
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv

  UIItem.Name.Click(62, 10)
  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  

def double_Click_To_open_File():
  quantist_Wpf = Aliases.Quantist
  quantist_Wpf.MainWindowView.LoadButton.ClickButton()
  quantist_Wpf.dlgOpen.OpenFile("E:\\TestComplete\\Quantist\\SampleQuantistFiles\\PM6910.csv", "Consumable Files (*.csv;*.quantist)")

def Max_Load_Files():
  #dialog display max number (>50)
  Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()
