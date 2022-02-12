def Launch():
  
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()

  TestedApps.Quantist.Run(1, True)
  
def Test1():
  aqObject.CheckProperty(Aliases.Quantist2.HwndSource_MainWindowView.MainWindowView.TextblockReleaseVersion0600, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.Quantist2.HwndSource_MainWindowView.MainWindowView.TextblockReleaseVersion0600, "Text", cmpEqual, "Release Version: 0.6.0.0")
