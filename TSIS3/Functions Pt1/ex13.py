import random
x=random.randint(1, 20)
name=input("Hello! What is your name? ")
guess=int(input("Well " + name + ", I am thinking of a number between 1 and 20. \nTake a guess. "))
i=1
while guess!=x:
    if (x>guess):
        print("Your guess is too low. ")
    elif (x<guess):
        print("Your guess is too high")
    i=i+1
    guess = int(input("Take a guess. "))
print("Good job, " + name + "! you guessed my number in " + str(i) + " guesses!")