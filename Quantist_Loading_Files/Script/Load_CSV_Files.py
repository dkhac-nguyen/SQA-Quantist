def Load_CSV_Files():
  quantist = Aliases.Quantist
  
  quantist.MainWindowView.LoadButton.ClickButton()
  dlgOpen = quantist.dlgOpen
  dlgOpen.cbxFileName.ComboBox.Edit.Keys("^a")
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv
  UIItem.Name.Click(62, 10)
  UIItem.Keys("^a")

  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  

def Test1():
  quantist_Wpf = Aliases.Quantist
  mainWindowView = quantist_Wpf.MainWindowView
  button = mainWindowView.LoadButton
  button.ClickButton()
  dlgOpen = quantist_Wpf.dlgOpen
  UIItemsView = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View
  OCR.Recognize(UIItemsView.MS_B0_wk_28_repeat_PM8800_20180110_133338_csv.Name).BlockByText("01-10-18").Click()
  UIItemsView.HMHMAG_with_Controls_csv.Name.MouseWheel(-1)
  UIProperty = UIItemsView.Plate_1_Panel_1_Acquisition_1_PlateRunResults_csv.Name
  UIProperty.MouseWheel(-1)
  UIItemsView.Plate_4_Panel_1_Acquisition_2_PlateRunResults_csv.Name.MouseWheel(-1)
  UIItemsView.Plate_8_Panel_3_Acquisition_2_PlateRunResults_RP1_csv.Name.MouseWheel(-1)
  UIItemsView.Plate_10_Panel_2_Acquisition_2_PlateRunResults_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_01_13_13_41_4_RP1_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_17_16_32_06_1_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_19_16_28_54_2_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_24_14_19_23_1_RP2_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_26_12_43_05_2_RP2_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_27_12_56_22_2_RP2_csv.Name.MouseWheel(-1)
  UIProperty.MouseWheel(-1)
  UIProperty.Click(155, 13, skShift)
  btnOpen = dlgOpen.btnOpen
  btnOpen.ClickButton()
  button2 = mainWindowView.ButtonOk
  button2.ClickButton()
  treeView = mainWindowView.RunTreeView
  treeView.ClickItem("|[1]|[1]")
  treeView.ClickItem("|[2]|[2]")
  grid = mainWindowView.Border.Grid
  grid.ZoomSlider.wPosition = 1
  treeView.ClickItem("|[3]|[3]")
  toggleButton = mainWindowView.Togglebutton
  toggleButton.ClickButton(cbChecked)
  treeView.ClickItem("|[0]|[0]")
  treeView.ClickItem("|[1]|[1]")
  treeView.ClickItem("|[2]|[2]")
  treeView.ClickItem("|[3]|[2]")
  grid.ZoomSlider2.wPosition = 1
  treeView.ClickItem("|[4]|[1]")
  treeView.ClickItem("|[7]|[0]")
  toggleButton.ClickButton(cbUnchecked)
  treeView.ClickItem("|[7]|[2]")
  grid.ZoomSlider3.wPosition = 1
  treeView.ClickItem("|[6]|[1]")
  treeView.ClickItem("|[5]|[2]")
  grid.ZoomSlider4.wPosition = 1
  button.ClickButton()
  UIProperty.MouseWheel(-1)
  UIItemsView.Plate_3_Panel_1_Acquisition_2_PlateRunResults_csv.Name.MouseWheel(-1)
  UIItemsView.Plate_7_Panel_3_Acquisition_2_PlateRunResults_RP2_csv.Name.MouseWheel(-1)
  UIItemsView.Plate_9_Panel_2_Acquisition_2_PlateRunResults_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_01_13_13_41_2_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_01_13_13_41_5_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_19_13_04_31_1_csv.Name.MouseWheel(-1)
  UIItemsView.PlateRunResults_Multiplate_2021_02_26_12_43_05_2_RP1_csv.Name.Click(145, 4)
  UIProperty.Click(155, 2, skShift)
  btnOpen.ClickButton()
  button2.ClickButton()
  scrollViewer = mainWindowView.ScrollViewer
  dataGrid = scrollViewer.DataGrid
  dataGrid.ClickRowIndicator(23)
  dataGrid.ClickRowIndicator(23)
  scrollViewer.HScroll.Pos = 0
  dataGrid.DblClickRowIndicator(23)
  dataGrid.DblClickRowIndicator(23)
  dataGrid.DblClickRowIndicator(23)
