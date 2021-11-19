def Import_Data_File(varDir, varFileName):
  
  try:
    quantist = Aliases.Quantist
    quantist.MainWindowView.Menu.WPFMenu.Click("File|Import Data Files")
    file = varDir + varFileName #+ "Consumable Files (*.csv;*.quantist)"
    
    dlgOpen = quantist.dlgOpen
    dlgOpen.cbxFileName.SetText(file)
    dlgOpen.btnOpen.ClickButton()
    
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