"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394070"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

from random import randint
fortune = randint(0, 100)

print("Your fortune cookie says...")

if fortune < 25: 
    print("An adventure lies ahead.")
else: 
    if fortune < 50:
        print("Your soulmate lies just around the corner.")
    else:
        if fortune < 75:
            print("Expect much of yourself and little of others.")
        else: 
            if fortune < 90:
                print("Don't worry; prosperity will knock on your door soon.")
            else: 
                print("You have had a good start. Work harder!")
            
print("Now, go spread postitive vibes!")
