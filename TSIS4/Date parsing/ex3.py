import datetime

x = datetime.datetime.now()

y = x.replace(microsecond=0)

print("время с микросекунами:", x)
print("время без микросекунд:", y)