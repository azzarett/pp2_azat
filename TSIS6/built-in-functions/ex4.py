import time

number = int(input("Введите число: "))
delay = int(input("Введитев миллисекундах: "))

time.sleep(delay / 1000)


sqrtn = pow(number, 0,5)

print(f"Квадратный корень из {number} после {delay} миллисекунд равен {sqrtn}")