# Intro to Programming

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)


#### Sequence

1. [Intro](#numbers)
2. [Debugging](#debugging)
3. [Random](#random)

## Warmup
Have students look up how much older they are than Cleopatra.

## Numbers
Have students predict the outcome:

```python
print('3' + '3')

```
Run the code. Ask the students to explain what happened.

Rewrite the code as follows:

```python
print(3 + 3)

```

Ask who can explain this?

In the first example, Python added two strings rather than numbers. Numbers are their own data type in programming.


## Debugging
Have students predict the outcome of this program

```python
number = input('give me a number')
print(number)
```
Run the code.

Now add a line of code with a simple operation.

```python
number = input('give me a number')
print(number)
number = input('give me a number')
print(number + 10)
```


#### Interpreting Errors


You should see something like this:

```python
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(number + 10)
TypeError: must be str, not int
```
Ask where is the error
- Traceback tells us where:

Ask what the problem is
- TypeError gives us the error.

This happens because the user types the answer, which is a string. You can't add a string and a number.

Have students predict the outcome of this program
```python

your_num = int(input('give me a num'))
print(0 + '3')
```

Have students explain why this worked. What did the computer do?


- ask students to guess what other mathematical operations you can preform
- run through subtraction, multiplication, and division.
- have students preform simple maths on large numbers

Operator     | Meaning
------------ | ------------
x + y  | Adds values on either side of the operator
x - y  | Subtracts right hand operand from left hand operand
x * y  | Multiplies values on either side of the operator
x // y | Divides left hand operand by right hand operand
x % y  | Modulus Divides left hand operand by right hand operand and returns remainder
x ** y | Performs exponential (power) calculation on operators

## random

To make a game of chance, you can use random numbers. This is pretty easy to do in python.

First, you import the random module

```python
import random
```

This allows us to use code that was already written.

Next, to make a random number

```python
import random

lotto = rand.randint(0,100)
print(lotto)

```

Who can guess what (0,100) does?
Right, it creates a random number between 0 and 100

Who can guess what rand.randint does?

rand.randint is how we call the code in the random module. Meaning, it is how we tell them computer we want a random integer.

Who can guess how rand.randint works?

rand.randint is a shortcut, which we call a function. A function accesses code that is already written. We can think of it as code neatly wrapped up into these words. Like a variable, but this variable does something. So, we call it a function.

Why are functions helpful?
- you don't have to keep rewriting code. It is reusable
- you don't have to know how it works just how you want to use it
- keeps our program looking nice and clean
