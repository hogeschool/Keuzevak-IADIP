Week 5
=========================

![Logo](../docs/img/logo.png "Logo")

![Cover Image](../docs/img/cover.jpg "Cover Image")

Description
-----------

This week we will add three new functions to our calculator; greatest common
divisor, least common multiple, power of two and square root.

Topics
------

- Loops
- Arithmetic
- Functions
- Conditions
- Optionally: Recursion

(1) Power
---------

The first function that we will add to our calculator this week is the power
function. Recall that the outcome of the expression `2^8` is `2*2*2*2*2*2*2*2`. In other words, an expression of the kind `a^b` (raise the *base*,
*a* to the power of the *exponent*, *b*) multiplies the base an amount of times
indicated by the exponent. Since we implemented our multiplication function last
week, we should have the required tools to implement this function.

Your calculator will implement the power function for positive numbers. Two
integers should be provided to your function and one integer should be returned.

You may choose to use the *power* function in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting
point.

Note: You can also choose to implement the power function as a recursive
function.

(1) Square root
---------------

The square root function is our next target for implementation. This function is
defined as a function that, for a number *a*, calculates an output that raised
to the power of two yields *a*.

An example:

`sqrt(25)=5`

Because:

`25=5^2=5*5`

This might sound like a difficult problem to solve, after all, how do we find
this number especially when we are dealing with floating-point numbers. However,
we will limit ourselves to an integer parameter provided to the square root
function. Moreover, we will only return integers from our square root function.
i.e. We won't bother about `sqrt(26)` being slightly above the value 5.

Since we've limited ourselves to this much simpler scenario, we can sketch the
algorithm for implementing the square root function as; count up to the outcome,
such that the squared outcome is less than or equal to the provided argument.

Your calculator will implement the square root function for positive numbers.
One integer should be provided to your function and one integer should be
returned.

You may choose to use the *sqrt* function in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting
point.

Note: You can also choose to implement the square root function as a recursive
function.

(3) Greatest common divisor
---------------------------

The greatest common divisor of two integers is defined as the largest integer
that divides the two integers. For example, take the integers 8 and 12, the
greatest common divisor of these two integers is 4. The integer 4 for the
integers 8 and 12 is the greatest integer that divides both integers.

Let us take the integers 54 and 24 and determine the greatest common divisor.
Intuitively, it makes sense to first determine what the integers are that divide
each number.

- 54 = 54 x 1 = 27 x 2 = 18 x 3 = 9 x 6
- 24 = 24 x 1 = 12 x 2 = 8 x 3 = 6 x 4

So the divisors of these two integers are:

| In common? | No | No | No | No | No | No | No | Yes | No | Yes | Yes | Yes |
|------------|----|----|----|----|----|----|----|-----|----|-----|-----|-----|
| **24**     |    |    | 24 |    | 12 |    | 8  | 6   | 4  | 3   | 2   | 1   |
| **54**     | 54 | 27 |    | 18 |    | 9  |    | 6   |    | 3   | 2   | 1   |

The top row denotes whether or not the integers have the divisor in common.

Note that four divisors are in common, 6, 3, 2, and 1. Of these divisors 6 is
the greatest. Therefore, 6 is the greatest common divisor of 54 and 24.

A common algorithm for calculating the greatest common divisor is the Euclidean
algorithm. This algorithm makes use of the fact that the greatest common divisor
of two integers is equal to the greatest common divisor of the second integer
and the remainder of the two integers. An example:

| Quotient | a  | b  | Remainder |
|----------|----|----|-----------|
| 2        | 48 | 18 | 12        |
| 1        | 18 | 12 | **6**     |
| 2        | 12 | 6  | 0         |

The algorithm:

1. Take two integers (e.g. 48 and 18) as *a* and *b* respectively.
2. Compute the modulo of two arguments a and b.
3. Take *a* as the previous *b* and take *b* to be the result of the module
    calculation in step 2.
4. Continue 1, 2 and 3 until the remainder is 0.
5. Take the greatest common divisor of the two integers to be the last non-zero
    remainder (e.g. 6 in the example).

Your calculator will implement the greatest common divisor function for positive
even numbers. Your function will be provided two integers and should return one
integer.

You may choose to use the *gcd* function in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting point.

(4) Least common multiple
-------------------------

The least common multiple of two integers *a* and *b* is defined as the smallest
positive integer that is divisible by both *a* and *b*. For example, take the
integers 4 and 6, we can list the multiples of 4 and 6.

- 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, ...
- 6, 12, 18, 24, 30, 36, 42, 48, 54, ...

The common multiples of these integers are:

| In common? | No | No | No | Yes | No | No | No | Yes | No | No | No | Yes | No | No | No | Yes | No | No |
|------------|----|----|----|-----|----|----|----|-----|----|----|----|-----|----|----|----|-----|----|----|
| **6**      |    | 6  |    | 12  |    | 18 |    | 24  |    | 30 |    | 36  |    | 42 |    | 48  |    | 54 |
| **4**      | 4  |    | 8  | 12  | 16 |    | 20 | 24  | 28 |    | 32 | 36  | 40 |    | 44 | 48  | 52 |    |

Of the multiples that both integers have in common, 12 is their least common
multiple. Since it is the smallest positive integer that is divisible by *a* and
*b*.

The least common multiple can be calculated by using the following formula:

`lcm(a,b) = a * b / gcd(a, b)`

The proof of this formula can be found in the references below.

Your calculator will implement the least common multiple function for positive
even numbers. Your function will be provided two integers and should return one
integer.

You may choose to use the *lcm* function in [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) as a starting point.

(6) Calculate
-------------

Exercise 1
----------

A disco has a ceiling full of lights, 11 in total. Each light flashes at a fixed
interval, but most lights flash out of phase with respect to the other lights in
the ceiling. Let the following table define the flashing intervals (in seconds)
for each light:

| Light | 1  | 2  | 3 | 4 | 5  | 6  | 7 | 8  | 9  | 10 | 11 |
|-------|----|----|---|---|----|----|---|----|----|----|----|
|       | 32 | 24 | 6 | 6 | 10 | 16 | 8 | 14 | 56 | 34 | 30 |

Calculate after how many seconds all lights flash together.

(7) Advanced
---------

The following functions can be added:

- Binary string to decimal number (integer) conversion.

Refer to the final assignment description document for the specifications of
additional functionality.

(8) References
--------------

1. <https://en.wikipedia.org/wiki/Greatest_common_divisor>
2. <https://en.wikipedia.org/wiki/Exponentiation>
3. <https://en.wikipedia.org/wiki/Nth_root>
4. <https://en.wikipedia.org/wiki/Square_root>
5. <https://en.wikipedia.org/wiki/Euclidean_algorithm>
6. <https://en.wikipedia.org/wiki/Least_common_multiple>
7. <https://www.youtube.com/watch?v=H_2_nqKAZ5w>
8. <http://www.cut-the-knot.org/arithmetic/GcdLcmProperties.shtml>