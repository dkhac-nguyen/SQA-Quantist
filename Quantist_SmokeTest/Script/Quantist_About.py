def About():
  #BuiltIn.ShowMessage("About Box is clicked but nothing here to verify, yet!")
  Aliases.Quantist.MainWindowView.Menu.WPFMenu.Click("Help|About")
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.Version, "Text", cmpEqual, "Release Version: 0.8.0.0")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  #verify Quantist TM top left corner
  Regions.Quantist_TM.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView, 30, 9, 64, 21, False), False, False, 89, 17)
    