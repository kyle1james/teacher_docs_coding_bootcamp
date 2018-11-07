# Intro to Programming

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [What is Programming](#what-is-programming)
2. [A deeper look](#a-deeper-look)
3. [Operators](#operators)
4. [Strings](#strings)
5. [Transformations](#transformations)
6. [String interpolation](#string-interpolation)
7. [Booleans](#returns-as-breakpoints)

# What is programming
What is programming and how does it work? A program can be said to be broken into a few main parts:

- data
- instructions

OR

- input
- what to do with the input
- output

### Variables
Variables are used to store data to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program. [source](https://launchschool.com/books/ruby/read/variables)

Typically, a program consists of instructions that tell the computer what to do and data that the program uses when it is running

### Assigning Value to Variables
There are four primary data types in programming:

| Data type     | Example       | Assigning    |
| ------------- |:-------------:| ------------:|
| int           | 110           | a = 30       |
| float         | 110.010101    | a = 1.0101   |
| boolean       | True or False | tacos = true |
| string        | "words"       | hi = 'hello' |

In computer science and computer programming, a data type or simply type is a classification of data which tells the computer how the programmer intends to use the data. [source](https://en.wikipedia.org/wiki/Data_type)

### Control Flow

In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated.

For now, we will be working from the top down. Meaning, that your program will read and execute line by line starting with line one until it reaches the end.

- [source](https://en.wikipedia.org/wiki/Control_flow)


Have students look at the following code and pick out the variables and their data types, and identify control flow.

Have students predict the outcome of this program

```python

pie_price = 3.14
name = 'Christina Tosi'
employed = True
number_of_pies_to_make = 32

if pie_price > 3:
  print(name, 'will make', number_of_pies_to_make)
else:
  print('no one will make pies for that cheap!')

```
Congrats! You read your first program!

## A deeper look


In computer science, a variable stores some sort of information. Think of a variable like a magic box. The information inside the box can be numbers, words, true, false, etc.

In python, to define a variable you give a name and then a value. The name is always on the left side and the value is always on the right side. For example,

```python
how_many_dogs = 0
puppies = 8
borkers = 10

```
To access the value inside the variable, one simply uses the name of the variable.

```python
print(how_many_dogs)
# >>> 0
```

But what if you need to change what is inside a variable?

```python
how_many_dogs = borkers + puppies
```
- ask students how can you see what is inside how_many_dogs (use print())
- ask students to predict the outcome of the following code

```python
borkers = 10
puppies = 10
how_many_dogs = borkers + puppies
how_many_dogs = 0
print(how_many_dogs)
```

What is important is that variables change- they are variable. In the example above we added borkers to puppies by using their names and the addition operator. We then saved the answer inside the variable how_many_dogs. The value of how_many_dogs changed while borkers and puppies stayed the same.

Variables change all the time and this is a central part of programming, changing data based on new data. Exciting!


## Operators

#### Arithmetic Operator

Operator     | Meaning
------------ | ------------
x + y  | Adds values on either side of the operator
x - y  | Subtracts right hand operand from left hand operand
x * y  | Multiplies values on either side of the operator
x // y | Divides left hand operand by right hand operand
x % y  | Modulus Divides left hand operand by right hand operand and returns remainder
x ** y | Performs exponential (power) calculation on operators


- ask students to guess what other mathematical operations you can preform
- run through subtraction, multiplication, and division.
- have students preform simple maths on large numbers

```python
bank_account = 1000000
monthly_bills = 10000
monthly_income = 20000
```
- find yearly bills cost
- find yearly income
- find end of the year back_account total

### Break for Lab

## Strings
### Getting User Input

## Transformations

## String interpolation

### Break for Lab

## Booleans
