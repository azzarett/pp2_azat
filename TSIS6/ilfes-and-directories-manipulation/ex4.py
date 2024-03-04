import os

path = '/vs/PP2/tsis6/filehandling.txt'

count = 0

file = open(path, 'r')
for x in file:
    count += 1

file.close()

print("Total number of lines:", count)