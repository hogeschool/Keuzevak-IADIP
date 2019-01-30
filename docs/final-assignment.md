Final assignment
=========================

![Logo](../docs/img/logo.png "Logo")

![Cover Image](../docs/img/cover.jpg "Cover Image")

Description
-----------

Throughout this course you will implement a calculator application that makes us of a command-line (text only) interface. The calculator will feature various functions that are used to find answers to simple calculation problems. During 5 weeks, you will incrementally add functionality to the application such that at the end of this course the calculator is implemented according to the specifications below.

It is important to keep this document as a reference, describing the criteria for implementing the functionality of the calculator. Since the application is automatically graded through AutoGradr and AutoGradr will contain rules to check the criteria below, the criteria specified in this document should be considered as strict.

Application criteria
--------------------

Your application must adhere to the following criteria:

1. The application should be implemented in the Python programming language, version 3.
2. The application should read input from the command-line (stdin, by making use of the *input* function of Python).
3. The application should provide output through the command-line (stdout, by making use of the *print* function of Python).
4. No other programming language can be used.
5. Graphical user interfaces are not supported.
6. Additional program arguments should be provided via *argv*.

If we use the word *input* in this document, we refer to a string coming from the standard input. When we use the word *output* in this document, we refer to a string printed to the standard output unless explicitly stated otherwise.

Mandatory functionality should be implemented. Optional functionality can be implemented to receive a higher grade.

Pay close attention to the following criteria:

- __You are only allowed to use the in-built + and - operators for numbers smaller than 10.__ 
- __You are not allowed to use the built-in power, square, multiplication, division, GCD or LCM functions.__
- __You are not allowed to use packages that are not approved by your teacher.__

Requirement M1): The help command (mandatory)
---------------------------------------------

The *help* command outputs the available commands upon entering *help*.

- *input*: *help*
- *output*:

```
supported functions:
"sub" arity: 2
"sum" arity: 2
"divide" arity: 2
"multiply" arity: 2
"power" arity: 2
"sqrt" arity: 1
"mod" arity: 2
"gcd" arity: 2
"lcm" arity: 2
"bin" arity: 1
```

Please make sure that precisely this string is written to stdout.

Requirement M2): The version command (mandatory)
-----------------------------------------------

The *version* command outputs version information of the calculator application. Note that we will only work on version 0.1, therefore the version should remain 0.1.

- *input*: *version*
- *output*: *calculator version 0.1*

Requirement M3): The quit command (mandatory)
---------------------------------------------

The *quit* command should immediately terminate the application.

- *input*: *quit*
- *output*:

Requirement A1): Command-line arguments (advanced)
---------------------------------------------------

Every command described above except for the *quit* command should be accepted as an argument to the application via *argv*. Instead of continuing running, the application should terminate right after executing the command.

The commands *help* and *version* should be prefixed by the characters *\--* (dash dash). An argument starting without the characters *\--* should be treated as an expression.

```
python main.py --help
supported functions:
"sub" arity: 2
"sum" arity: 2
"divide" arity: 2
"multiply" arity: 2
"power" arity: 2
"sqrt" arity: 1
"mod" arity: 2
"gcd" arity: 2
"lcm" arity: 2
"bin" arity: 1
python main.py --version
calculator version 0.1
python main.py "sum 1 1"
2
```

In case multiple arguments are provided:

```
python main.py --help --version "sum 1 1"
```

Only the first command will be processed, after executing the command the application should immediately terminated as described above.

Requirement M4): Expression processing (mandatory)
--------------------------------------------------

The expression processing functionality will need to implement processing simple (that means one operation per expression) expressions in *prefix* notation. This means that an operator should precede the operands. With processing the expression, the input should be evaluated, the appropriate function should be called and the output of that function should be written to the standard output stream.

- *input*: *operation (e.g. sum) operands*
- *output*: *result of operation on operands*
- *errors*: 
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*
    - In case the operation is unknown (not present in the function table):
        - *output*: *unknown token*

Requirement A2): Expression processing (advanced)
-------------------------------------------------

The simple expressions of the mandatory criteria should be extended such that the operands can consist of operations on operands. This way, more complex expressions can be created such as:

`sum 1 power 2 5`

Requirement A3): Postfix expressions (advanced)
-----------------------------------------------

Implement processing of postfix expressions.

`2 3 sum 1 multiply`

Requirement A4): Prefix expressions (advanced)
----------------------------------------------

Implement processing of prefix expressions.

`2 sum 3 multiply 1`

Requirement A5): The ans keyword (advanced)
----------------------------------------------

Implement the *ans* keyword, that will be replaced by the result of the last operation.

- *input*: *res instead of operand for operator (e.g. sum ans 1)*
- *output*: *result of last operation is inserted instead of the ans keyword*
- *errors*:
    - In case there is no previous result:
        - *output*: *invalid use of ans*

Requirement M5): Addition (mandatory)
-------------------------------------

The addition operation should be implemented for two positive numbers. The name of the addition operation as a command should be *sum*.

- *input*: *sum operand1 operand2*
- *output*: sum of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M6): Subtraction (mandatory)
----------------------------------------

The subtraction operation should be implemented for two positive numbers. The name of the subtraction operation as a command should be *sub*. Negative numbers should be returned in case the second operand is greater than the first operand, zero should be returned if the operands are equal.

- *input*: *sub operand1 operand2*
- *output*: subtraction of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M7): Division (mandatory)
-------------------------------------

The division operation should be implemented for two positive numbers. The name of the division operation as a command should be *divide*. The division operation should be implemented as a floor division and should therefore return a positive integer or 0.

- *input*: *divide operand1 operand2*
- *output*: floor division of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M8): Multiplication (mandatory)
-------------------------------------------

The multiplication operation should be implemented for two positive numbers. The name of the multiplication operation as a command should be *multiply*.

- *input*: *multiply operand1 operand2*
- *output*: multiplication of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M9): Power (mandatory)
----------------------------------

The power operation should be implemented for two positive numbers. The name of the power operation as a command should be *power*.

- *input*: *power operand1 operand2*
- *output*: power of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M10): Square root (mandatory)
-----------------------------------------

The square root operation should be implemented for one positive number. The name of the square root operation as a command should be *sqrt*.

- *input*: *sqrt operand1*
- *output*: square root of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*
        
The square root operation must conform to the following rules:

- *sqrt x* outputs _y_ such that *y^2 <= x* **and**
- *(y+1)^2 > x*

For example:

```
input: sqrt 5
output: 2
```

Requirement M11): Greatest common divisor (mandatory)
-----------------------------------------------------

The gcd operation should be implemented for two positive numbers. The name of the gcd operation as a command should be *gcd*.

- *input*: *gcd operand1 operand2*
- *output*: gcd of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M12): Least common multiple (mandatory)
---------------------------------------------------

The lcm operation should be implemented for two positive numbers. The name of the lcm operation as a command should be *lcm*.

- *input*: *lcm operand1 operand2*
- *output*: lcm of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement M13): Modulo (mandatory)
------------------------------------

The modulo operation should be implemented for two positive numbers. The name of the modulo operation as a command should be *mod*.

- *input*: *mod operand1 operand2*
- *output*: modulo of operand1 and operand 2
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Requirement A6): Binary to decimal conversion (advanced)
--------------------------------------------------------

The binary to decimal operation should be implemented for binary strings. The name of the binary to decimal operation as a command should be *bin*.

- *input*: *bin operand1*
- *output*: binary string operand1 converted to decimal
- *errors*:
    - In case too little or too many operands are provided:
        - *output*: *invalid number of operands*
    - In case operands of the wrong type are provided:
        - *output*: *invalid operand type*

Grades and Assessment
----------

The final results of this course will be determined according to the following
criteria.

-   Weekly progress (0% - 100%): The programming tasks need to be evaluated by
    the teacher on a weekly basis. The final assessment of this criterium is as
    follows: `Progress = Number of approved weeks / 5`

-   Final assignment (0% - 100%): The final assignment should be submitted through
    AutoGradr. The assessment of the final assignment is automatic according to
    the criteria of the assignment. The deadline for the final assignment will
    be announced during the course. Each successfully implemented requirement
    accounts for 1/19 point. Thus, The final assessment of this criterium is as
    follows: `Final assignment = Number of implemented requirements / 19`

The final grade will be determined according to the following formula.

`Grade = Progress * 3 + Final assignment * 7`
      `= numberOfWeeks/5 * 3 + numberOfRequirements/19 * 7`

Example grade calculation:

Student has implemented all mandatory requirements and has shown weekly progress each time. So he has 5 out of 5 weeks, and implemented the 13 mandatory requirements out of the total of 19 requirements:

`(5/5) * 3 + (13/19) * 7 = 7.8`

__Assignments both weekly and final are individual work. In case of plagiarism student(s) will be reported to the exam committee.__

### Retake

Should the grade of the final assessment be insufficient, there will be an
opportunity to retake. The deadline for this retake will be announced during the
course.

__The grade received for the weekly progression will be maintained for the retake.__
