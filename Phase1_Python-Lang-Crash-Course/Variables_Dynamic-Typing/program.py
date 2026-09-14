"""
NUMBERS AND MATH.
There are two common types of numbers, they are integer and floats. There are also complex and long, but they are not commonly used like integer and floats. Integers are whole numbers, positive or negative (4, -20, 3000000, 76, -45) while floats are also positive or negative but they have decimals after them. Floats take more space in the memory because python has to accout for the decimal numbers that may come later (4.7783, 8.563, -6.5472, 9.6747, -8745, -20.1, 0.0).

Commonly used math operators are: addition(+), subtraction(-) multiplication(*), division(/), exponentiation(**), modulo(%), and integer division(//).
"""

"""
Python always return a float when there is a division, always, even if integers are divided, but if we don't want a float result, we can use the integer division. For instance:
"""
print(3/3)
print(3//3)

"""
DYNAMIC TYPING:
Python is highly flexible and gives us the ability to assign variables to DIFFERENT TYPES. Not just from example: string to string, bool to bool, int to int, float to float, but from a data type to another. We could go from 99 to a string, none or zero, 
"""

iAmAwesome = True;
print(iAmAwesome)

iAmAwesome = "Oluwabukola"
print(iAmAwesome)

iAmAwesome = None
print(iAmAwesome)

iAmAwesome = 22/7
print(iAmAwesome)