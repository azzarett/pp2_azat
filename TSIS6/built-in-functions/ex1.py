list_numbers = input("Введите числа(через пробел): ").split()

c = 1

for x in list_numbers:
    c *= int(x)

print("Результат умножения всех чисел:", c)