import arith

'''
Contains the implemented functions and their names. This dictionary
is referenced when checking whether or not a command entered is a valid
function. The dictionary contains of key: value pairs, where key is a string
containing the function name and value is a reference to the function that
was implemented.

In case a new function is added to the calculator, make sure to update this
dictionary.
'''
function_table = {
    'sub': arith.sub,
    'sum': arith.sum,
    'divide': arith.divide,
    'multiply': arith.multiply,
    'power': arith.power,
    'sqrt': arith.sqrt,
    'mod': arith.mod,
    'gcd': arith.gcd,
    'lcm': arith.lcm,
    'bin': arith.bin
}

arity_table = {
    'sub': 2,
    'sum': 2,
    'divide': 2,
    'multiply': 2,
    'power': 2,
    'sqrt': 1,
    'mod': 2,
    'gcd': 2,
    'lcm': 2,
    'bin': 1
}

types_table = {
    'sub': int,
    'sum': int,
    'divide': int,
    'multiply': int,
    'power': int,
    'sqrt': int,
    'mod': int,
    'gcd': int,
    'lcm': int,
    'bin': str
}

'''
Returns True if function_name provided is a valid function, else False.
'''
def is_function(function_name):
    return function_name in function_table

'''
Returns the function according to function_name.
'''
def get_function(function_name):
    return function_table[function_name]

'''
Returns the arity of the function according to function_name.
'''
def get_arity(function_name):
    return arity_table[function_name]

'''
Returns the type of _all_ parameters of the function according to function_name.
'''
def get_type(function_name):
    return types_table[function_name]

'''
Prints the available functions and their arity.
'''
def print_functions():
    print('supported functions:')
    for function_name in function_table.keys():
        print('"%s" arity: %i' % (function_name, arity_table[function_name]))