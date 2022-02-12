import Quantist_Removing_Files
import Load_CSV_File

def Well_Assignments_View():
  
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.MainWindowView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
      
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.WellAssignmentsFolder, "PlateRunResults_Multiplate.csv")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on WAs View
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.HwndSource_MainWindowView.MainWindowView.RunTreeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  #Verify WAs displays two 96-Well plates
  Regions.Two_96_Well_Plates.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer, False, False, 46540, 17)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  scrollViewer = Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer
  scrollViewer.Keys("^a")
  Regions.Two_96_Well_Plates_HighLighted.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer, False, False, 46540, 17)

def Test():
  hwndSource = Aliases.Quantist.MainWindowView
  listView = hwndSource.MainView.PlatesViewScrollViewer.ItemsControl.wellplate  
  wellAssignmentsView = Aliases.Quantist.MainWindowView.MainView.WellAssignmentsView  
  main = hwndSource.MainView
  
  scrollViewer = main.PlatesViewScrollViewer
  #scrollViewer.VScroll.Pos = 0
  listView = scrollViewer.ItemsControl.wellplate

  listView.Ellipse1.Click()
  listView.Ellipse10.Click(19, 24, skShift)
  txt_Rep_Cnt = main.TextboxReplicateCount
  txt_Rep_Cnt.Click()
  txt_Rep_Cnt.SetText("1")
  main.Btn_Unknown.ClickButton()
  txt_Rep_Cnt = main.TextboxSampleName
  txt_Rep_Cnt.Click()
  txt_Rep_Cnt.SetText("Patient")
    
  txt_DF = main.TextboxDilutionFactor 
  txt_Rep_Cnt.Click()
  txt_DF.SetText("2")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  main.Btn_All_Sample.ClickButton()
  
  Aliases.Quantist.MainWindowView.MainView.Unknown_Details.ButtonSelected.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  #main.Btn_All_DF.ClickButton()

  #aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  wellAssignmentsView.Click(640, 160)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  Regions.Unknown_Details.Check(Aliases.Quantist.MainWindowView.MainView.Unknown_Details, False, False, 11303, 17)

  #Click on Cancel button from Unknown Details window
  wellAssignmentsView.Click(742, 425)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Regions.PlateAssignmentGroupsDataGrid.Check(Aliases.Quantist.MainWindowView.MainView.PlateAssignmentGroupsDataGrid, False, False, 10909, 17)

def Test1():
  hwndSource = Aliases.Quantist.MainWindowView
  border = hwndSource.MainView
  aqObject.CheckProperty(border.Unknown_Details, "Enabled", cmpEqual, True)
  button = hwndSource.MainViewRunCtr.ButtonCancel
  aqObject.CheckProperty(button, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(border.TextboxSampleName, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(border.TextboxDilutionFactor, "Enabled", cmpEqual, True)
  button.ClickButton()

def Test2():
  listView = Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.ItemsControl.wellplate
  aqObject.CheckProperty(listView.Ellipse1, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(listView.Ellipse10, "Enabled", cmpEqual, True)

def Test3():
  scrollViewer = Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer
  scrollViewer.VScroll.Pos = 0
  listView = scrollViewer.ItemsControl.wellplate
  listView.Ellipse1.Click(15, 27)
  listView.Ellipse10.Click(19, 24, skShift)


def Test4():
  hwndSource = Aliases.Quantist.MainWindowView
  border = hwndSource.MainView.Unknown_Details
  aqObject.CheckProperty(border.ButtonApply, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(hwndSource.MainViewRunCtr.ButtonCancel, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(border, "Enabled", cmpEqual, True)

def Test5():
  wellAssignmentsView = Aliases.Quantist.MainWindowView.MainView.WellAssignmentsView
  wellAssignmentsView.Click(742, 425)

def Test6():
  Aliases.Quantist.MainWindowView.MainView.WellAssignmentsView.Click(714, 425)

def Test7():
  border = Aliases.Quantist.MainWindowView.MainView
  textBox = border.TextboxDilutionFactor
  textBox.Click(66, 14)
  textBox.SetText("2")
  border.Unknown_Details.ButtonSelected.ClickButton()

def Test8():
  Aliases.Quantist.MainWindowView.MainView.Btn_All_DF.DblClick(26, 11)

def Test9():
  wellAssignmentsView = Aliases.Quantist.MainWindowView.MainView.WellAssignmentsView
  wellAssignmentsView.Click(640, 160)
  wellAssignmentsView.Click(608, 160)
