import math

numberOfSides = int(input('Input number of sides: '))
lengthOfSide = int(input('Input length of side: '))

print((numberOfSides/4)*pow(lengthOfSide, 2)*(math.cos(math.radians(180/numberOfSides))/math.sin(math.radians(180/numberOfSides))))