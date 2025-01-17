﻿def Load_CSV_Files():
  quantist_WPF = Aliases.Quantist_WPF
  
  quantist_WPF.HwndSource_MainWindowView.MainWindowView.Button.ClickButton()
  dlgOpen = quantist_WPF.dlgOpen
  dlgOpen.cbxFileName.ComboBox.Edit.Keys("^a")
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.MS_B0_wk_28_repeat_PM8800_20180110_133338_csv
  OCR.Recognize(UIItem.Name).BlockByText("repeat").Click()
  UIItem.Keys("^a")
  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  mainWindowView = Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView
  mainWindowView.GridSplitter.Drag(3, 147, 84, 2)
  
  BuiltIn.ShowMessage("We can either load all or single CSV file at a time!")
  #OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.RunTreeView.TreeViewItem.Textblock011018MsB0Wk28RepeatPm88002018011).CheckText("*01-10-18 MS BO wk 28 re*")
  #aqObject.CheckProperty(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.RunTreeView.TreeViewItem2.Textblock2PlatesWith1Std, "Enabled", cmpEqual, True)
  #BuiltIn.ShowMessage("Successfully verify the first few strings from the custom listbox!")