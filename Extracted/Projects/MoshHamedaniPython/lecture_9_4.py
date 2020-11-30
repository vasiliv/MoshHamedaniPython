from pathlib import Path
from time import ctime

path = Path("G:\\Projects\\MoshHamedaniPython\\lecture_9_4.py")
print(path.exists())

#path.rename("lecture_9_4.py")
#print(path)

#creation time of this file, ctime - builtin function, stat.ST_CTIME - creation time
print(ctime(path.stat().st_ctime))

# returnes contents of path file as string
print(path.read_text())

# pathis failshi rame textis chacera
#path.write_text("blablabla")

