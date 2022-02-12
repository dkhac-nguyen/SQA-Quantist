def Import_Data_File(varDir, varFileName):
  
  try:
    quantist = Aliases.Quantist
    quantist.MainWindowView.Menu.WPFMenu.Click("File|Import Data Files")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
    file = varDir + varFileName #+ "Consumable Files (*.csv;*.quantist)"
    
    dlgOpen = quantist.dlgOpen
    quantist.dlgOpen.OpenFile(file, "Consumable Files (*.csv;*.quantist)")    

  except ValueError as Error:
    Log.Warning("Can not load run file to Run Control View {Error}")
        
  except OSError as err:
    print("OS error: {0}".format(err))
    
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

def Loading_File():
  try:
    quantist = Aliases.Quantist
    mainWindowView = quantist.MainWindowView
    gridSplitter = mainWindowView.GridSplitter
    mainWindowView.Button.ClickButton()
    quantist.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800, "Consumable Files (*.csv;*.quantist)")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
    #f = open('myfile.txt')
    #s = f.readline()
    #i = int(s.strip())
  except OSError as err:
      print("OS error: {0}".format(err))
  #except ValueError:
  #    print("Could not convert data to an integer.")
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
    
def test():
  Import_Data_File(Project.Variables.Sample_Files_Dir, Project.Variables.Sample_FileName)
  

def Test1():
  quantist_Wpf = Aliases.Quantist
  quantist_Wpf.MainWindowView.Menu.WPFMenu.Click("File|Import Data Files")
  quantist_Wpf.dlgOpen.OpenFile("C:\\Quantist\\SQA-Quantist\\Test_Data\\SampleQuantistFiles\\TestData.csv", "Consumable Files (*.csv;*.quantist)")

def Test2():
  quantist = Aliases.Quantist
  quantist.MainWindowView.LoadButton.ClickButton()
  quantist.dlgOpen.Drag(517, 25, 34, 66)

def Test3():
  Aliases.Quantist.MainWindowView.Menu.WPFMenu.Click("File|Import Data Files")
