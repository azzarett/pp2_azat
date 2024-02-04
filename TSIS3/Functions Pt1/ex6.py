def reverse(myList):
      for i in range(len(myList)-1, -1, -1):
          print(myList[i], end=" ")
inp = input("Введите строку: ")
myList = inp.split()
reverse(myList)
