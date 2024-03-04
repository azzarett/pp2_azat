

my_list = ["Aibyn", "Amir", "Alih", "KAZZZ"]

# Открываем файл для добавления списка
file = open('/vs/PP2/tsis6/write1.txt', "a")
file.write(str(my_list))
file.close()


f = open('/vs/PP2/tsis6/write1.txt', "r")
print(f.read())