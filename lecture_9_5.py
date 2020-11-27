from pathlib import Path
from zipfile import ZipFile

# gaaketa ubralod carieli files.zip
zipFile = ZipFile("files.zip","w")

# zipshi chakara kvela is faili rac am pathshi shedis
for path in Path("G:\\Projects\\MoshHamedaniPython").rglob("*.*"):
    zipFile.write(path)
zipFile.close()

# igive kodi ufro lakonurad
with ZipFile("files.zip","w") as zipFile:
    for path in Path("G:\\Projects\\MoshHamedaniPython").rglob("*.*"):
        zipFile.write(path)

# amobechdos kvela failis saxeli rac shedis am arqivshi
with ZipFile("files.zip") as zipFile:
    print(zipFile.namelist())
    #getinfo metodi gasarkvevia windowsistvis
    #info = zipFile.getinfo()
    #print(info.)
    # Extracted - folder name in project directory
    zipFile.extractall("Extracted")
