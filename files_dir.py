from pathlib import Path #pathlib is module and Path is class

# Absolute Path: Root of our hard disk eg:c:/
#Relative Path : Path staring from current directory

# path = Path("Modules") #checking existence of folder
# print(path.exists()) #return boolean result

# path = Path("Emails")
# print(path.mkdir()) #for creating new folder/directory

# path = Path("Emails")
# print(path.rmdir()) #for deleting folder/directory

path = Path()
for file in path.glob('*'):  #for searching files *: all type file *.py pytho file
    print(file)