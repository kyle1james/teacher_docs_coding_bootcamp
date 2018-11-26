# Basic Conditionals

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [If/else](#if/else)
2. [Operators](#operators)
3. [Day Two](#day_two)
4. [Design Cycle](#Design-cycle-for-programming)


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

This program is able to make a decision. What decision is it making?

Right, it makes a decision based on age.


When you create a program, you will have to control the direction your program moves. That is, how does your program make decisions? For example, you will want to execute a certain line of code if one condition is satisfied, and a different set of code if it is not. In Python, you have the if, elif and the else statements for this purpose [source](https://www.datacamp.com/community/tutorials/python-if-elif-else)

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

The syntax for an if/else statement is as follows
```python
if(condition):
      #Indented statement block for when condition is TRUE
elif(condition):
      #Indented statement block for when condition is True
else:
      #Indented statement block for when condition is FALSE
```
