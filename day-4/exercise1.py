#in this exercise we are creating a program that randomises the side of a coin
# we are using the random module
#if the outcome is 1 then it prints an output message its heads 

import random

coin=random.randint(0,1)

if coin == 1:
    print("its heads")
else:
    print("Its tails")