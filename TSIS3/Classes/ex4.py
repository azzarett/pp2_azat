import math
class Point:
    def __init__(self, x, y, mx, my):
        self.x=x
        self.y=y
        self.mx=mx
        self.my=my
    def show(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")
    def move(self):
        print("(" + str(self.x+self.mx) + "," + str(self.y+self.my) + ")")
    def dist(self):
        print(math.sqrt((self.mx)**2+(self.my)**2))
x=int(input("Type x: "))
y=int(input("Type y: "))
mx=int(input("The steps you want x to move: "))
my=int(input("The steps you want y to move: "))
answer = Point(x, y, mx, my)
answer.show()
answer.move()
answer.dist()