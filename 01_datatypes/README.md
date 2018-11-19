# Intro to Programming

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [Intro](#strings)
2. [String Interpolation](#string-interpolation)
3. [User Input](#user-input)
4. [Lab](#madlib-lab)
5. [Operators](#operators)
6. [Debugging](#debugging)


## Intro

First, code the following. Have students wait until you are done to do the same but for their name.

```python
print('hello Kyle')
```

Awesome, now while this great, it can get very boring very quick. Imagine you have to say hello to 1000 people. Who wants to write 1000's hello's!? There has got to be a better way.

```python
name = 'Kyle'
print('hello '+ name)
```

- have students predict what will happen
- ask students what name did?

Name is a variable. In computer science, a variable stores some sort of information. Think of a variable like a magic box with information inside.

In python, to define a variable you give a name and then a value. The name is always on the left side and the value is always on the right side.

- program a few variables together

```python
name = 'Kyle'
food = 'Pizza'
```

## String Interpolation
Very cool, name is a variable. In computer science, a variable stores some sort of information. Think of a variable like a magic box. When we look inside the box, we see what data is inside.

When we use words in quotes, we call this a string.

Let's code a few variables together. Ask students, make sure to stay with string datatypes!

```python
name = 'Kyle'
food = 'Pizza'

print('hello my name is '+name+'and I love '+ food)
```
## User Input

What if you want to get user input to change the users?

- Have students predict what will happen

```python
name = input('what is your name?')
food = input('what is your fav food?')

print('hello my name is '+name+'and I love '+ food)
```

Explain that what you type is the input
And the output is the variable


Run the program and change the variables based on students in the class.

## Madlib lab
Today you are going to create a madlib program.

- explain what is a madlib

## Operators

Have students predict the outcome:

```python
print('3' + '3')

```


What happens if we run the following?

```python
print(3 + 3)

```

Ask who can explain this?

In the first example, Python added two strings rather than numbers. Numbers are their own data type in programming.


## Debugging
Have students predict the outcome of this program

```python

your_num = input('give me a num')
print(0 + '3')
```

Break it down:

```python
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(3+num)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Ask where is the error
- Traceback tells us where:
Ask what the problem is
- TypeError gives us the error

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
