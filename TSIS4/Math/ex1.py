import math

degree = input('Input degree: ')

radByPi = (int(degree)*math.pi)/180
radByFunction = math.radians(int(degree))

print(radByPi)
print(radByFunction)
