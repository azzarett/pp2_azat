import datetime

x = datetime.date.today()
y = datetime.timedelta(days=5)
z = x-y
print(f"Todays {x}")
print("Overall", z)