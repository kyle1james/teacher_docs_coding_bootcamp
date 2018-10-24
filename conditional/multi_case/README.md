# Multi Case Conditionals

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [Review](#Review)
2. [Operators](#operators)


## Review

While writing code in any language, you will have to control the flow of your program. This is generally the case when there is decision making involved - you will want to execute a certain line of codes if a condition is satisfied, and a different set of code incase it is not. In Python, you have the if, elif and the else statements for this purpose [source](https://www.datacamp.com/community/tutorials/python-if-elif-else)

- You can have zero or more elif statements
- You can have one or no else statement
- The elif keyword is a way of saying "if the previous conditions were not true, then try this condition".
- The else statement should be the final case. There are no conditions following an else

The syntax for and if else statement is as follows
```python
if(condition):
      #Indented statement block for when condition is TRUE
elif(condition):
      #Indented statement block for when condition is True
else:
      #Indented statement block for when condition is FALSE
```
Questions to ask:
  * How do you start an if/else statement?
  * How many elif statements can I have?
  * What is a condition?
  * Why doesn't the else statement need a condition?


## Operators

We've already been using if/else statements for control flow, but it's been pretty binary. This can be a problem as life is more complicated than simple black and white options.

So far, you've seen if/else statements used like this:

```python
if time_of_day == 'morning':
  print('stay in bed')
else:
  print('go outside')
```
But what if it's raining, snowing, or warm outside?

Consider the following operators:

- **and**
- **or**


These operators help make more complex decisions.

### And
```python
if weather == 'warm' and time_of_day == 'afternoon':
  print('go to the pool')
```
This condition equates two logical statements. If both are true, the condition is met and we fire the code below. If one if true and one is false, we aren't going to the pool.

That's nice, but I don't mind swimming if in an inside pool if it is cold.
### Or

```python
if weather == 'warm' or pool == 'inside':
  print('go to the pool')
```
This condition equates two logical statements. If one is true, the condition is met and we fire the code below.

```python
dogs = 7
cats = 8
puppers = 10

if (dogs > cats) or (puppers > cats):
  print('We should get more cats')
elif (cats < dogs) and (dogs < puppers):
  print('We should get more puppies')
else:
  print('We should get more dogs')

```


Questions to ask:
* What is the predicted outcome of this program?
* What would the outcome be if we change the value of cats to 11?
* What is the predicted outcome if we replaced all OR conditions with AND



```python
dogs = 7
cats = 8
puppers = 10

if (dogs > cats) or (cats < puppers):
  print('We should get more cats')
elif (cats < puppers) and (dogs < puppers):
  print('We should get more puppies')
else:
  print('We should get more dogs')

```

For this program, there is a logical error. The elif statement can never fire. Have students predict the outcome of this program. Ask students to come up with an explanation for why the elif statement can never fire and then ask students to describe a solution to this programs bug.

Break for multi_case lab
