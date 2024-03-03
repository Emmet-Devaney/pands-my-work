#Write a program (floor.py), that takes in a float and outputs an int rounded 
#down, you will need the math module math.floor()

# floors a number.
#
# Author: Andrew Beatty
import math
numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))
