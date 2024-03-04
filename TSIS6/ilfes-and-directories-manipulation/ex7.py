file1 = open('/vs/PP2/tsis6/primer.txt', "r")

file2 = open('/vs/PP2/tsis6/xopy.txt', "w")

x = file1.read()
file2.write(x)


file2.close()
file1.close()