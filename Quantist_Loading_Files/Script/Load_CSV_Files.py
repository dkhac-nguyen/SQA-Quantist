def Load_CSV_Files():
  quantist = Aliases.Quantist
  
  quantist.MainWindowView.Button.ClickButton()
  dlgOpen = quantist.dlgOpen
  dlgOpen.cbxFileName.ComboBox.Edit.Keys("^a")
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv
  UIItem.Name.Click(62, 10)
  UIItem.Keys("^a")

  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)