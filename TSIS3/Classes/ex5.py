class bankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def tellInfo(self):
        print("Your name: " + self.owner + "; And you have " + str(self.balance) + "$")
    
    def putMoney(self):
        print("Hello")
        
    def takeMoney(self):
        print("Hello")
        
class bankOperations(bankAccount):
    def __init__(self, owner, balance, take, put):
        bankAccount.__init__(self, owner, balance)
        self.take = take
        self.put = put
        
    def putMoney(self):
        self.balance = int(self.balance) + int(self.put)
        print("Ваш баланс: " + str(self.balance) + "$")
        
    def takeMoney(self):
        if(int(self.balance) < int(self.take)):
            print("У вас недостаточно средств!")
        else:
            self.balance = int(self.balance) - int(self.take)
            print("Ваш баланс: " + str(self.balance) + "$")
    
name = input("Type your name: ")
balance = int(input("Type balance: "))
sendInfo = bankAccount(name, balance)
sendInfo.tellInfo()


loop = True
while loop == True:
    option = int(input("Выберите опцию: 1(Пополнить); 2(Снять); 3(Закончить): "))
    if(option == 1):
        money = int(input("Введите сумму: "))
        sendToBalance = bankOperations(name, balance, 0, money)
        sendToBalance.putMoney()
        balance = balance + money
    elif(option == 2):
        money = int(input("Введите сумму: "))
        sendToBalance = bankOperations(name, balance, money, 0)
        sendToBalance.takeMoney()
        balance = balance - money
    elif(option == 3):
        loop = False
    else:
        print("No such option")


        