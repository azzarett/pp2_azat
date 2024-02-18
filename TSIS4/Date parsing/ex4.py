import datetime
import random

first = datetime.datetime(2024, 1, 1, 12, 0, 0)  
second = datetime.datetime(2024, 1, 1, 12, 0, 30)

print(first)
print(second)

raznica = (abs(first - second))
print(raznica.seconds)