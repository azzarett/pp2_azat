import os

path = '/vs/PP2/tsis4/date/ex4.py'


if os.path.exists(path):
    print("exists")
    
    
    directory, filename = os.path.split(path)
    
    print("Directory:", directory)
    print("Filename:", filename)
    
else:
    print("not exist")