class getAndPrintString:
    def __init__(self, getString):
        self.getString = getString
        
    def printString(self):
        print("You typed " + self.getString)
        
getString = input("Type something: ")
answer = getAndPrintString(getString)
answer.printString()