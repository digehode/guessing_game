#!/usr/bin/python3

import random

minimum=1
maximum=20

answer=random.randint(minimum,maximum)

guess=None

while guess!=answer:
    guess=int(input("Enter a guess:"))
    
    if guess==answer:
        print("Well done")
    elif guess>answer:
        print("Too high!")
    else:
        print("Too low!")
print("Game over")    
  
