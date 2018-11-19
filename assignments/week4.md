Week 4
======

![Logo](../docs/img/logo.png "Logo")

![Cover Image](../docs/img/cover.jpg "Cover Image")

Description
-----------

This week we will implement the basic arithmetic operations addition,
subtraction, division and multiplication. Typically, these operations are
implemented in the electronic circuitry of the CPU itself. In this weekly
assignment, we will implement functions for these arithmetic operations with
only making little use of the existing operators. For the implementation, we
will refer to the algorithms that we were thought in high school and implement
them in Python. When we have implemented these functions, we can start to solve
simple arithmetic problems using our calculator.

Topics
------

- Loops
- Arithmetic
- Functions
- Conditions

(1) Addition
-----------

You will implement what we will call the "high school addition algorithm". This
algorithm will take two numbers, both represented in the decimal number system.
As an example, take the numbers 234 and 456. Let these numbers consist of
**digits** such that 123 consists of the digits 1, 2 and 3 and the number 456
consists of the digits 4, 5 and 6. In the decimal number system, digits can only
take the values 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9.

This means that if we want to represent a number beyond the digit 9, we need one
extra digit. Let us consider the expression `9+3`, the result of which will
overflow one digit:

| Carry  | 1 |   |    |
|--------|---|---|----|
|        |   | 9 |    |
|        |   | 3 |    |
|        |   |   | \+ |
| Result | 1 | 2 |    |

Adding the digits from right-to-left, we get:

**Step 1: (Add Digits, start with right-most digits)**

`9 + 3 = 12`

Since the number that we calculated is greater than 9, we need one more digit to
represent this number. We say that, since the result of adding the digits 9 and
3 overflows our maximum digit value 9, we **carry** over one digit to the left.

The part of the calculated numbers greater than 10 is our calculated digit at
the current position. For `9 + 3 = 12`, the amount greater than 10 is 2,
therefore, 2 is the resulting digit at the right-most position.

**Step 2: (Move one step to the left, add digits)**

`1 + 0 + 0 = 1`

The first number in this calculation is the carry, the rest of the digits are 0,
since no second digit is present in either 9 or 3.

Since 1 is not greater than 9, we can immediately write down 1 as the second
digit.

**Another example**

64182 + 5499 = 69681

| Carry →  |   |   | 1 | 1 |   |    |
|----------|---|---|---|---|---|----|
|          | 6 | 4 | 1 | 8 | 2 |    |
|          |   | 5 | 4 | 9 | 9 |    |
|          |   |   |   |   |   | \+ |
| Result → | 6 | 9 | 6 | 8 | 1 |    |

Carry is 0 initially.

1. `carry + 2 + 9 = 11, carry = 1, digit: 1`
2. `carry + 8 + 9 = 18, carry = 1, digit: 8`
3. `carry + 1 + 4 = 6, carry = 0, digit: 6`
4. `carry + 4 + 5 = 9, carry = 0, digit: 9`
5. `carry + 6 + 0 = 6, carry = 0, digit: 6`

Your calculator will implement the high school addition algorithm for positive
numbers. Your function should be provided two integer parameters and return an
integer.

Implement the high school addition algorithm, you may choose to use the function
*sum* in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting point. In addition to providing a
starting point for the function structure, the function also makes use of the
functions *get_digit* and *get_number_length*. The first function returns the
*n*-th digit from the right (starting at 0) of *number*. The second function
returns the number of digits for *number*. A third function *set_digit* may be
used to set the *n*-th digit of *number* to the digit *v*.

(2) Multiplication
------------------

The next function that will be implemented is multiplication using the
previously implemented function for adding two positive integers. i.e. Let's
suppose that we want to find the outcome of `5 * 5`, we will be able to write
this as `5 + 5 + 5 + 5 + 5`. In other words, we can write the expression `a * b`
as adding *a b* times.

Your calculator will implement multiplication for positive numbers by making use
of the addition function. Your function should be provided two integer parameters and return an integer.

You make choose to use the function *multiply* in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting
point.

(3) Subtraction
---------------

Similar to the algorithm for adding two numbers, we can implement functionality
for calculating the subtraction of two numbers.

For the subtraction version of the algorithm, most steps will be equal. We will
start at the right, processing digits and moving one digit to the left
afterwards. Instead of adding digits, however, we will now subtract digits. And,
instead of computing the **carry**, we will now **borrow** from the digit to the
left in case the result of subtracting the digits is less than 0. In case we
borrow from the next digit, we add 10 to the calculation of the subtraction of
the two digits.

**An example**

64182 - 5499 = 58683

| Borrow → | 0 | 1 | 1 | 1 | 0 |    |
|----------|---|---|---|---|---|----|
|          | 6 | 4 | 1 | 8 | 2 |    |
|          |   | 5 | 4 | 9 | 9 |    |
|          |   |   |   |   |   | \- |
| Result → | 5 | 8 | 6 | 8 | 3 |    |

Borrow is 0 initially.

1. `2 - 9 - borrow = -7, borrow = 1, digit: 3`
2. `8 - 9 - borrow = -2, borrow = 1, digit: 8`
3. `1 - 4 - borrow = -4, borrow = 1, digit: 6`
4. `4 - 5 - borrow = -2, borrow = 1, digit: 8`
5. `6 - 0 - borrow = 5, borrow = 0, digit: 5`

As we can see, when we calculate two digits and need to borrow from the digit to
the left:

1. `2 - 9 - borrow = -7` We determine borrow to be 1, as the result of
    subtracting the digits is less than 0. This requires us to add 10 (the
    amount that we borrowed from the next digit), to be added to the result.
    Which yields `-7+10=3` as the outcome of subtracting the digits at the
    right-most position.

Your calculator will implement the high school subtraction algorithm for
positive numbers. Your function should be provided two integer parameters and
return an integer.

You make choose to use the function *sub* in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting
point.

(4) Division
------------

The last function that will be added to our calculator is the division of two
positive integers. Similar to multiplication, division can also be implemented
using the functionality that we've implemented earlier in this assignment. For
division, we will be able to make us of the subtraction of two positive
integers. i.e. Let's suppose that we want to calculate the outcome of the
expression `25 / 6`, we will be able to write this as `25 - 6 - 6 - 6 - 6`, such
that the outcome of the latter expression is smaller than 6. In other words, we
keep subtracting the *divisor* until we cannot subtract anymore. In this case,
we would find the outcome to be 4, since `4 * 6=24`. We will only be dealing
with integers.

Implement the multiplication function. Your function should be provided two
integer parameters and return an integer.

You make choose to use the function *divide* in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting
point.

(5) Advanced
---------

Thus far, we have limited ourselves to positive numbers. We can, however, extend
our implementation to also support negative numbers. Moreover, we can even
implement subtraction by means of addition, i.e. a - b = a + -b.

For refinement of the arithmetic functionality implemented this week, implement
support for negative numbers. Please refer to the final assignment description
criteria for the appropriate format such that your final solution can be
correctly evaluated.

As a reference, you can use the following table:

| Variables   | a, b          | \-a,-b                | \+a,-b        | \-a, +b               |
|-------------|---------------|-----------------------|---------------|-----------------------|
| Addition    | (+a)+(+b)=a+b | (-a)+(-b)=(-1)\*(a+b) | (+a)+(-b)=a-b | (-a)+(+b)=b-a         |
| Subtraction | (+a)-(+b)=a-b | (-a)-(-b)=(-a +b)=b-a | (+a)-(-b)=a+b | (-a)-(+b)=(-1)\*(a+b) |

(6) References
--------------

1. <https://en.wikipedia.org/wiki/Carry_(arithmetic)>
2. <https://en.wikipedia.org/wiki/Sign_(mathematics)>
