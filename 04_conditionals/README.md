# Basic Conditionals

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [If/else](#if/else)
2. [code-a-long](#code-a-long)
3. [len](#len)
4. [planning](#planning)


## if/else
Ask students: how could we make the chat bot program better?

What if the chat bot could give unique responses based on a users input?

Have students program the following. Before they run the program have students predict what will happen?

```python
age = int(input('how old are you?'))

if age > 18:
  print('you can vote!')
else:
  print('you can not vote')

```

Right, this program is able to make a decision. What decision is it making?

Right, it makes a decision based on age.


When you create a program, you will have to control the direction your program moves. For example, you will want to execute a certain line of code if one condition is satisfied, like age, and a different set of code if it is not. In Python, you have the if, elif and the else statements for this purpose [source](https://www.datacamp.com/community/tutorials/python-if-elif-else)

The syntax for an if/else statement is as follows

Have students write this down in there notes

```python
if(condition):
      #Indented statement block for when condition is TRUE
elif(condition):
      #Indented statement block for when condition is TRUE
else:
      #Indented statement block for when condition is FALSE
```

Ask the following facts/facts to students about if/else statements

- What is a condition: a statement that equates to TRUE or False
- How do you start an if/else statement: The if statement starts the if/else
- How many elif statements can I have?: You can have zero or more elif statements
- How many else statements can you have: You can have one or no else statement
- What is an elif statement: The elif keyword is a way of saying "if the previous conditions were not true, then try this condition".
- Why doesn't the else statement need a condition?: The else statement should be the final case. There are no conditions following an else. It is the logical last choice.

## Code A Long
Have students code with you a quick age check program.

Let's create a short program that will print out a unique message based on your age.

```Python

age = int(input('how old are you?'))

if age > 10:
  print('you are soooo young!')
elif age > 15:
  print('you should get a job')
else:
  print('you are so old')

```
Have students predict how they could break this program

- If you put any age from 0-10, the program will print out you are so old. It is very important to think your conditions through when creating an if/else

- what if you want a condition to be 15 or greater for an age? Simple, use the correct operator. It is very important to think your operators through when using if/else statements.

```Python
if age >= 15:
  # do something
```


## conditional operators
Have students fix the above code after going over operators

![operators](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdun9nPP7I_h_fuVYgJzqMwdahubYrbD8cmuOGWYNN4UGo1eGIWw)

Looking at these operators, what changes can we make to help our program?

- using less than or equal to

## len()
A fun and useful built-in function is len()

Who can guess what len() does

```python
len('shibas')
```

Right, Len returns the number of characters in the string. This is useful when testing requirements, say for a password or correct credit card number.

How does this built-in function work?


## planning
For your lab, you will create a login for a user. We want to plan this program out, then complete the lab.

Questions:
- What is the input?: user input to set password and to login
- How will you check the password: equal to operator
- Have a user set a password: variable
- Have user try to login using password: variable
- Spicy: try using a username and password

Use this diagram to help students plan
![logic](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/If-Then-Else-diagram.svg/220px-If-Then-Else-diagram.svg.png)
