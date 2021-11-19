def About():

  Aliases.Quantist.MainWindowView.Menu.WPFMenu.Click("Help|About")
  #BuiltIn.ShowMessage("About Box is clicked but nothing here to verify, yet!")
  
  OCR.Recognize(Aliases.Quantist.MainWindowView.Text_Version).CheckText("*Release Version: 0.0.0.3*")
  OCR.Recognize(Aliases.Quantist.MainWindowView.Text_CopyRight).CheckText("*© Copyright 2021 Bio-Techne. All Rights Reserved*")
