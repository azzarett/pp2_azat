def spy_game(nums):
    myString = ""
    for i in nums:
        if int(i)==0:
            myString+="0"
        elif int(i)==7:
            myString+="7"
    x=myString.find("007")
    if x==-1:
        return False
    else:
        return True
inp = input("Введите числа: ")
nums=inp.split()
if spy_game(nums)==True:
    print("True")
else:
    print("False")