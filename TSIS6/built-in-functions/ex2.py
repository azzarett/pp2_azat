mystring = input("Введите строку: ")

upper_c = 0
lower_c = 0

for x in mystring:
    if 'A' <= x <= 'Z':
        upper_c += 1
    elif 'a' <= x <= 'z':
        lower_c += 1


print("Количество больших букв:", upper_c)
print("Количество маленьких букв:", lower_c)