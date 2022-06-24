from pathlib import Path
import os

programContents = """from pathlib import Path
import shutil
import os

directoryCurrent = Path.cwd()

print("Ensure project file is .pyw")
projectFilenameFull = input("Project file full name: ")
projectFilenameSplitted = projectFilenameFull.partition(".")
projectFilename = projectFilenameSplitted[0]
projectExtension = projectFilenameSplitted[2]

directoryToBAT = "C:\\\\Users\\\\Willie\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python39\\\\Scripts"
directoryToPYW = "C:\\\\Users\\\\Willie\\\\Desktop\\\\Personal\\\\Stuff"

if not (os.path.exists(directoryCurrent / projectFilenameFull)):
    exit()

pathToBat = Path(directoryToBAT) / (projectFilename + ".bat")

batFile = open(pathToBat, "w")
batFile.write("start /min C:\\\\Users\\\\Willie\\\\Desktop\\\\Personal\\\\Stuff\\\\" + projectFilename + ".pyw " + "%*")
batFile.close()

shutil.copy(Path(directoryCurrent) / projectFilenameFull, Path(directoryToPYW) / (projectFilename + ".pyw"))"""

os.chdir(Path.home() / "Desktop")
theFile = open("converter.py", "w")
theFile.write(programContents)
theFile.close()
