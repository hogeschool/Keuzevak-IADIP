'''
Returns the n-th digit of number.

Note that n is 0-based. In case n is greater than the length in digits of the
number, 0 is returned. In addition, note that n is right-aligned (i.e. n=0 is
the right-most digit, n=1 is one digit to the left of the right-most digit, etc.).
'''
def get_digit(number, n):
    if (n >= get_number_length(number)):
        return 0
    return int(str(number)[-n - 1])                 # Returns the n-th digit

'''
Sets the n-th digit of number to v.

Note that n is right-aligned (i.e. n=0 is the right-most digit, n=1 is one digit to 
the left of the right-most digit, etc.). If number is too short (i.e. contains to few
digits, number is padded with zeroes).
'''
def set_digit(number : int, n : int, v : int):
    s = list(str(number))                           # Convert the number into a list of digits
    s = [0 for i in range(0, n + 1 - len(s))] + s   # Pad in case number is too short
    s[-n - 1] = v                                   # Set n-th digit
    return int(''.join([str(x) for x in s]))        # Convert list of digits to integer

'''
Returns the length in digits of number.
'''
def get_number_length(number):
    if number == 0:
        return 0
    return len(str(number))