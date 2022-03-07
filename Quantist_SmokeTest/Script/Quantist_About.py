def About():
  #BuiltIn.ShowMessage("About Box is clicked but nothing here to verify, yet!")
  Aliases.Quantist.MainWindowView.Menu.WPFMenu.Click("Help|About")
  Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()  
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Version, "Text", cmpEqual, "Release Version: 0.9.0.0")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  #verify Quantist TM top left corner
  Regions.Quantist_TM.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView, 30, 9, 64, 21, False), False, False, 89, 17)
  
  #verify Quantist splash view
  Regions.QuantistSplashView.Check(Aliases.Quantist.MainWindowView.MainView.Grid)

  
def Main_Menu():
  main = Aliases.Quantist.MainWindowView
  menu = main.Menu
  menu.WPFMenu.Click("Help|User Guide")
  button = main.MaxButtonOk
  button.ClickButton()
  menu.WPFMenu.Click("Help|Save Diagnostic")
  button.ClickButton()
  menu.WPFMenu.Click("Help|About")
  button.ClickButton()
  #menu.WPFMenu.Click("File|Open Runs")
