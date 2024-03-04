import os

path = '/vs/PP2/tsis6/delete.txt'


if os.path.exists(path):
    print("Path exists")

    if os.access(path, os.R_OK or os.W_OK):
        print("Accessed")
        
        os.remove(path)
        print("deleted")
    else:
        print("not accessed")
else:
    print("Path does not exist")