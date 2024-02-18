import datetime

x = datetime.date.today()
y = x - datetime.timedelta(days=1)
z = x + datetime.timedelta(days=1)

print("Yesterday->", y)
print("Today->", x)
print("Tomoroow->", z)