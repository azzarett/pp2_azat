def unique(myList):
    uniqueList = []
    for i in myList:
        if i not in uniqueList:
            uniqueList.append(i)
    print(uniqueList)
inp = input("Введите числа: ")
mylist = inp.split()
unique(mylist)