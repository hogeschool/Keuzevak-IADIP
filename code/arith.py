import arith_tools

from typing import List
from functools import reduce
from operator import add

'''
Calculates the sum of a and b.

Only supports positive integers.
'''
def sum(a, b):
    r = 0                                     # Result
    c = 0                                     # Carry

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    # Implement algorithm

    return r

'''
Calculates the subtraction of a and b.

Only supports positive integers.
'''
def sub(a, b):
    r = 0                                           # Result
    c = 0                                           # Borrow

    s = 1                                           # Sign is positive
    if b > a:
        pass # Implement algorithm, replace pass by your own code

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    # Implement algorithm

    return r * s                                    # Note the sign

'''
Calculates the multiplication of a and b.

Only supports positive integers.
'''
def multiply(a, b):
    r = 0                                     # Result
    # Implement algorithm
    return r

'''
Calculates the division of a and b.

Only supports positive integers.
'''
def divide(a, b):                       
    i = 0                                     # Result
    # Implement algorithm
    return i

'''
MANDATORY WEEK 5
'''

'''
Calculates the power of a and b.

Only supports positive integers.
'''
def power(a, b):
    r = 1                                     # Result
    # Implement algorithm
    return r

'''
Calculates the square root of a and b.

Only supports positive integers.
'''
def sqrt(a):
    if a <= 1:                                      # Early escape
        return a

    i = 1                                           # Increments
    r = 1                                           # Result of multiplication with i
    
    # Implement algorithm

    return sub(i, 1)                                # Subtract one from increment

'''
Calculates the modulo of a and b.

Only supports positive integers.
'''
def mod(a, b):
    return sub(a, multiply(divide(a, b), b))        # Calculate a - ((a / b) * b)

'''
Calculates the gcd of a and b.

Only supports positive integers.
'''
def gcd(a, b):
    return

'''
Calculates the lcm of a two integers.

Only supports positive integers.
'''
def lcm(a, b):
    return

'''
Converts a binary string to a decimal integer.
'''
def bin(a : str):
    return
