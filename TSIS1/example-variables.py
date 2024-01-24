#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#4
x = 5
y = "John"
print(type(x))
print(type(y))

#5
x = "John"
# is the same as
x = 'John'

#6
a = 4
A = "Sally"
#A will not overwrite a

#Variable names

#1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Assign Multiple Values

#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#2
x = y = z = "Orange"
print(x)
print(y)
print(z)

#3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables

#1
x = "Python is awesome"
print(x)

#2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


#3
x = 5
y = 10
print(x + y)

#4
x = 5
y = "John"
print(x, y)

#Global Variables

#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
