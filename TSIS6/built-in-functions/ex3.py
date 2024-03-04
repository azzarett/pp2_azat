mystring = input("Введите строку: ")

mystring = mystring.replace(" ", "").lower()

if mystring == mystring[::-1]:
    print("палиндромом")
else:
    print("не палиндромом")