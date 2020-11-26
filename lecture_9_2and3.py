from pathlib import Path

path = Path("G:\\Projects\\MoshHamedaniPython")
#returns true or false
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.absolute())

#shemdegshi
#path.mkdir()
#path.rmdir()
#path.rename()

# gadaurbens am direqtroriashi mkop kvela fails da direqtorias
print(path.iterdir())

for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir()]
print(paths)

#shegvidzlia pirobac davamatot
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

#direqtoriashi shesabamisi gafartoebiani failis dzebna
py_files = [p for p in path.glob("*.py")]
print(py_files)

# shvilobil direqtoriebshic edzebs
py_files = [p for p in path.rglob("*.py")]