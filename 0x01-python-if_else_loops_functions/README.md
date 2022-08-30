
n - Hello, World

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/ZvYINw7KnieWmwtPp2KhNw "explain to anyone"),  **without the help of Google**:

### General

-   Why Python programming is awesome
-   Who created Python
-   Who is Guido van Rossum
-   Where does the name ‘Python’ come from
-   What is the Zen of Python
-   How to use the Python interpreter
-   How to print text and variables using  `print`
-   How to use strings
-   What are indexing and slicing in Python
-   What is the official Holberton Python coding style and how to check your code with  `PEP 8`
-   Why indentation is so important in Python
-   How to use the  `if`,  `if ... else`  statements
-   How to use comments
-   How to affect values to variables
-   How to use the  `while`  and  `for`  loops
-   How is Python’s  `for`  different from  `C`‘s?
-   How to use the  `break`  and  `continues`  statements
-   How to use  `else`  clauses on loops
-   What does the  `pass`  statement do, and when to use it
-   How to use  `range`
-   What is a function and how do you use functions
-   What does return a function that does not use any  `return`  statement
-   Scope of variables
-   What’s a traceback
-   What are the arithmetic operators and how to use them

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file at the root of the  `holbertonschool-higher_level_programming`  repo, containing a description of the repository
-   A  `README.md`  file, at the root of the folder of  _this_  project, is mandatory
-   Your code should use the  `PEP 8`  style (version  `1.7.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`

NOTE: This project contains tasks that are listed in two repositories; 0x00-python-hello_world and 0x01-python-if_else_loops_functions. The file names will not correlate with the task numbers, because that's just the way Holberton has this project structured as of August 2022. 
## Tasks

### 0. Hello, print

Write a Python script that prints exactly  `"Programming is like building a multilingual puzzle`, followed by a new line.

-   Use the function  `print`
### 1. Copy - Cut - Paste

Complete this  [1-edges.py](https://holbertonintranet.s3.amazonaws.com/uploads/text/2021/3/fd5bb0d5f7712e088ad80eec4fe394d036ee7029.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T154118Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=1ba6ee514645928f9155c7095546c7dc09478f13f8e3236e61aacc870b560507 "1-edges.py")

-   You can find the source code  [1-edges.py](https://holbertonintranet.s3.amazonaws.com/uploads/text/2021/3/fd5bb0d5f7712e088ad80eec4fe394d036ee7029.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T154118Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=1ba6ee514645928f9155c7095546c7dc09478f13f8e3236e61aacc870b560507 "1-edges.py")
-   You are not allowed to use any loops or conditional statements
-   Your program should be exactly 8 lines long
-   `word_first_3`  should contain the first 3 letters of the variable  `word`
-   `word_last_2`  should contain the last 2 letters of the variable  `word`
-   `middle_word`  should contain the value of the variable  `word`  without the first and last letters
### 3. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

-   You can only use one  `print`  function with string format
-   You can only use one loop in your code
-   You are not allowed to store characters in a variable
-   You are not allowed to import any module
### 2. Positive anything is better than negative nothing

This program will assign a random signed number to the variable  `number`  each time it is executed. Complete the source code in order to print whether the number stored in the variable  `number`  is positive or negative.

-   You can find the source code  [2-pon.py](https://holbertonintranet.s3.amazonaws.com/uploads/text/2021/3/94656edc7118841481bb3e6396215a78aedd75b2.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T154118Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=e0e089211640ce4c6921942c4240c0c9e20fa0c09ae07ac278e815149ce7bce6 "2-pon.py")
-   The variable  `number`  will store a different value every time you will run this program
-   You don’t have to understand what  `import`,  `random. randint`  do. Please do not touch this code
-   The output of the program should be:
    -   The number, followed by
        -   if the number is greater than 0:  `is positive`
        -   if the number is 0:  `is zero`
        -   if the number is less than 0:  `is negative`
    -   followed by a new line
### 5. When I was having that alphabet soup, I never thought that it would pay off

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

-   Print all the letters except  `q`  and  `e`
-   You can only use one  `print`  function with string format
-   You can only use one loop in your code
-   You are not allowed to store characters in a variable
-   You are not allowed to import any module
### 4. The last digit

This program will assign a random signed number to the variable  `number`  each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable  `number`.

-   You can find the source code  [3-last_digit.py](https://holbertonintranet.s3.amazonaws.com/uploads/text/2021/3/b53c4f6618802f61b84b941a758073c8f6426935.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T154118Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=9fd1f4eefe50d969dede848986bde28e17f254181079c52e2883dc2516dd2e72 "3-last_digit.py")
-   The variable  `number`  will store a different value every time you will run this program
-   You don’t have to understand what  `import`,  `random.randint`  do.  **Please do not touch this code**. This line should not change:  `number = random.randint(-10000, 10000)`
-   The output of the program should be:
    -   The string  `Last digit of`, followed by
    -   the number, followed by
    -   the string  `is`, followed by the last digit of  `number`, followed by
        -   if the last digit is greater than 5: the string  `and is greater than 5`
        -   if the last digit is 0: the string  `and is 0`
        -   if the last digit is less than 6 and not 0: the string  `and is less than 6 and not 0`
    -   followed by a new line
### 6. Hexadecimal printing

Write a program that prints all numbers from  `0`  to  `98`  in decimal and in hexadecimal (as in the following example)

-   You can only use one  `print`  function with string format
-   You can only use one loop in your code
-   You are not allowed to store numbers or strings in a variable
-   You are not allowed to import any module
### 7. 00...99

Write a program that prints numbers from  `0`  to  `99`.

-   Numbers must be separated by  `,`, followed by a space
-   Numbers should be printed in ascending order, with two digits
-   The last number should be followed by a new line
-   You can only use no more than 2  `print`  functions with string format
-   You can only use one loop in your code
-   You are not allowed to store numbers or strings in a variable
-   You are not allowed to import any module
### 8. Inventing is a combination of brains and materials. The more brains you use, the less material you need

Write a program that prints all possible different combinations of two digits.

-   Numbers must be separated by  `,`, followed by a space
-   The two digits must be different
-   `01`  and  `10`  are considered the same combination of the two digits  `0`  and  `1`
-   Print only the smallest combination of two digits
-   Numbers should be printed in ascending order, with two digits
-   The last number should be followed by a new line
-   You can only use no more than 3  `print`  functions with string format
-   You can only use no more than 2 loops in your code
-   You are not allowed to store numbers or strings in a variable
-   You are not allowed to import any module
### 10. islower

Write a function that checks for lowercase character.

-   Prototype:  `def islower(c):`
-   Returns  `True`  if  `c`  is lowercase
-   Returns  `False`  otherwise
-   You are not allowed to import any module
-   You are not allowed to use  `str.upper()`  and  `str.isupper()`
-   [Tips: ord()](https://intranet.hbtn.io/rltoken/2ZFSMWiqAHrwg_SbT8RRmg "Tips: ord()")

You don’t need to understand  `__import__`
### 9. a + b

Write a function that adds two integers and returns the result.

-   Prototype:  `def add(a, b):`
-   Returns the value of  `a + b`
-   You are not allowed to import any module

You don’t need to understand  `__import__`
### 12. To uppercase

Write a function that prints a string in uppercase followed by a new line.

-   Prototype:  `def uppercase(str):`
-   You can only use no more than 2  `print`  functions with string format
-   You can only use one loop in your code
-   You are not allowed to import any module
-   You are not allowed to use  `str.upper()`  and  `str.isupper()`
-   [Tips: ord()](https://intranet.hbtn.io/rltoken/2ZFSMWiqAHrwg_SbT8RRmg "Tips: ord()")

You don’t need to understand  `__import__`
### 11. a ^ b

Write a function that computes  `a`  to the power of  `b`  and return the value.

-   Prototype:  `def pow(a, b):`
-   Returns the value of  `a ^ b`
-   You are not allowed to import any module

You don’t need to understand  `__import__`
### 13. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important

Write a function that prints the last digit of a number.

-   Prototype:  `def print_last_digit(number):`
-   Returns the value of the last digit
-   You are not allowed to import any module

You don’t need to understand  `__import__`
### 14. Fizz Buzz

Write a function that prints the numbers from 1 to 100 separated by a space.

-   For multiples of three print  `Fizz`  instead of the number and for multiples of five print  `Buzz`.
-   For numbers which are multiples of both three and five print  `FizzBuzz`.
-   Prototype:  `def fizzbuzz():`
-   Each element should be followed by a space
-   You are not allowed to import any module

You don’t need to understand  `__import__`
