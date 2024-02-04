class Shape:
    def __init__(self, width):
        self.width = width

        
    def printArea(self):
        self.width = self.width * self.width
        print("Area is: " + str(self.width))
        
    
class Square(Shape):
    def __init__(self, width):
        Shape.__init__(self, width)
    
getWidth = int(input("Type width: "))
area = Square(getWidth)
area.printArea()