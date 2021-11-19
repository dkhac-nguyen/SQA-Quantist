def Curve_View():
  
  #try to reuse Load_CSV_Files from CSV_Files project
  quantist = Aliases.Quantist
  mainWindowView = quantist.MainWindowView
  gridSplitter = mainWindowView.GridSplitter
  mainWindowView.Button.ClickButton()
  quantist.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  ##
  Regions.PM8800_Tree.Check(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem)
  Regions.PM8800_Chart.Check(Aliases.Quantist.MainWindowView.MainView.zchart)
  Regions.PM8800_Options.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView, 1257, 5, 324, 873, False))
  Regions.PM8800_ListControl.Check(Aliases.Quantist.MainWindowView.MainView.ListControl)

  Regions.Header_Sample.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Sample_Header)
  Regions.Header_Use.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Use_Header)
  Regions.Header_Well.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Well_Header)
  Regions.Header_MFI.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.MFI_Header)
  Regions.Header_MFI_CV.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.MFI_CV_Header)
  Regions.Header_Net_MFI.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Net_MFI_Header)
  Regions.Header_Conc.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Conc_Header)
  Regions.Header_Status.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Status_Header)
  Regions.Header_Conc_CV.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Conc_CV_Header)
  Regions.Header_Exp_Conc.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Exp_Conc_Header)
  Regions.Header_Pct_Recovery.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Pct_Recovery_Header)
  Regions.Header_DF.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.DF_Header)
  Regions.Header_N.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.N_Header)
  Regions.Header_Included.Check(Aliases.Quantist.MainWindowView.MainView.ListControl.Included_Header)  
 

