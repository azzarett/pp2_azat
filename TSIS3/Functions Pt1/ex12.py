def histogramm(mylist):
    for i in mylist:
        j=0
        while j<int(i):
            print("*", end='')
            j=j+1
        print('')
mylist = input("Введите числа: ").split()
histogramm(mylist)