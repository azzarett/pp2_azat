class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def printArea(self):
        self.width = self.width * self.length
        print("Area is: " + str(self.width))
        
    
class Rectangle(Shape):
    def __init__(self, width, length):
        Shape.__init__(self, width, length)
    
getWidth = int(input("Type width: "))
getLength = int(input("Type length: "))
area = Rectangle(getWidth, getLength)
area.printArea()