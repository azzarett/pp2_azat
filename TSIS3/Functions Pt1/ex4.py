def filterprimes(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
inp = input("Введите ряд чисел: ")
array = inp.split()
for i in range(len(array)):
    if (filterprimes(int(array[i]))==True):
        print(str(array[i]), end=" ")
