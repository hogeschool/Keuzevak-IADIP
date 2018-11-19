Week 3
=========================

![Logo](../docs/img/logo.png "Logo")

![Cover Image](../docs/img/cover.jpg "Cover Image")

Description
-----------

This week we will extend the commands that we have implemented last week by commands that resemble the mathematical functions that will be implemented in week 4 and week 5.

Up to now, we have implemented the following commands:

- *help* displays the available commands
- *version* displays version information
- *quit* exits the application

Next, we will assume that any string entered into the calculator is a command that will contain an expression. Often, when we calculate expressions, we implicitly make use of what is named the *infix* notation. i.e. `1+2*3`, where the operators are in between what we name the operands (1, 2 being the operands of the + operator, the result of the + operation and 3 being the operands of the * operator). To simplify the implementation of processing the expression string entered into our calculator, we will instead make use of a different notation called the prefix notation.

- *infix*: `1+2*3`
- *prefix*: `multiply add 1 2 3`

As we will see, processing such a prefix expression is far easier than processing an infix expression. Also note that we will use the full names of the functions (e.g. *multiply* instead of the operator *). Lastly, we will initially limit ourselves to simple expressions containing only one function per expression. The implementation of the processing of expressions that are more complex, i.e. multiple functions in one expression, is left as an optional implementation.

Topics
------

- String operations
- List operations
- Loops
- Functions
- Typecasting

Criteria
--------

(1) Processing expressions
-----------------------

We will focus on the implementation of a function *process_line* that will try to process user input in case the provided input is none of the already implemented commands *help*, *version* or *quit*. Please refer to the overview diagram of last week in case you want to recheck the flow of the application.

Since our *process_line* function takes care of processing expressions entered into our application, we assume that the format of the input that should be processed by the *process_line* function is as follows:

`<function-name><space><operands>`

Where *\<function-name\>* is one of the available function names in the functions table, *\<space\>* is a single space character and *\<operands\>* is composed of one of more operand*s*, separated by *\<space\>*.

Some examples of expression that will need to be processed:

- `sum 1 1`
- `sqrt 1`
- `divide 2 1`
- `divide 2 2`

For now, we have not yet implemented the actual functions (note that these functions do have stubs in the [code/arith.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/arith.py) file, this will be part of the assignments of week 4 and week 5. Therefore, we will limit ourselves to processing the expression and calling the associated function.

This week, keep the implementation of the arithmetic functions as it is. The AutoGradr test cases will assume the return values as they are in **arith.py**.

The examples above introduce what we call the *arity* of a function. By arity, we denote the number of operands a function takes. In the example above, we notice that the *sum* and *divide* functions have arity *2*, while the *sqrt* function has arity 1. We will use this information as it tells us how many operands we still need to find in the string that was provided as input by the user.

The code provided to you in the [code/functions.py](https://github.com/hogeschool/Keuzevak-IADIP/blob/master/code/functions.py) file contains a number of helper functions that can be used for the implementation of expression processing. Functions that may come in handy are:

- *is_function* will return *True* iff the string provided as a parameter is a known function name in the functions table.
- *get_function* will return a function from the functions table based on the string provided as a parameter.
- *get_arity* will return the arity of the function from the functions table based on the string provided as a parameter.
- *get_type* will return the type of all parameters from the functions table based on the string provided as a parameter. (This assumes that all parameters are of equal type)

Note that we introduce the *functions_table* here. It is not required to make changes to either the functions above or the *functions* or *arity* table. This table acts as storage for the functions that are available in our calculator.

Now that we know the format of the expressions that our calculator will need to process, we know that we have helper functions available that we can use and we know the concept of the arity of a function, we can start to sketch the algoritm for processing expressions.

Provided that *process_line* is the function that we will implement that takes one string as input, being the line that needs to be processed;

1. Tokenize string.
    1. Is the token a function name?
        1. Retrieve function
    2. Is the token an operand?
        1. Correct type
            1. Store operand
        2. Wrong type
            1. Output: 'invalid operand type'
    3. Otherwise
        1. Output: 'unknown token'
2. Correct arity?
    1. Call function and output result
3. Otherwise
    1. Output: 'invalid number of operands'

Note that the error cases *invalid operand type*, *unknown token* and *invalid number of operands* should be precisely these strings, as the output will be automatically verified.

Hint: In case you use a list to store the operands that were found while processing the tokens, you can make use of the list unpacking functionality in Python. Please check reference *1* below for a tutorial.

Hint: Make sure to correctly typecast the operands. As the implementations of the functions will require arguments of a certain type (typically integers).

Implement the *process_line* function. Note that, since the functions are not yet implemented (we will start working on those implementations next week), most functions will return wrong answers. We will fix this next week.

(2). Advanced
-----------

We have limited ourselves to expressions containing only one function per expression. While this offers us basic calculation abilities (after we have implemented the actual functions), in would be more interesting to extend the implementation such that we allow users to enter more complex expressions. For example:

`sum 1 multiply divide 10 2 2`

This will eventually allow us to even process expressions like:

`sum bin 1111 sub 2 1`

(Add to the binary number *1111* the result of *2* subtracted by *1*)

In addition, we can implement postfix:

`2 1 sub 1 add`

(Add 2 subtracted by 1 to 1)

And, *infix*:

`1 sum 1 multiply 3`

(Multiply 1 added to 1 by 3)

(7) References
--------------

1. <https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/>
2. <https://www.programiz.com/python-programming/type-conversion-and-casting#type-casting>
3. <https://en.wikipedia.org/wiki/Reverse_Polish_notation>
4. <https://www.geeksforgeeks.org/evaluation-prefix-expressions/>
5. <https://en.wikipedia.org/wiki/Shunting-yard_algorithm>