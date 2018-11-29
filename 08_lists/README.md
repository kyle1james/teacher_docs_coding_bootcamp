# Lists

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [lists](#lists)
2. [index](#index-value)
3. [list built-in functions](#list-built-in-functions)
4. [iteration](#iteration)



## lists
Lists are a basic and powerful data structure in Python. Lists are made with square brackets [], each item is separated by a comma,

A list is a collection of items. The items can be ints, strings, booleans, etc.

Code Together:

Ask students to create a list of their favorite foods

```python

snacks = ['pizza', 'tacos', 'sushi', 'banh-mi']

```
## index value
Each item has an address called an index value

Ask students to predict what

```python
snacks[1]
```
will print out

In a list, we count starting from 0. So, to get pizza one writes...

```python
snacks[0]
```
## list built-in functions

### len()
Ask: Who can predict the outcome?

```Python
len(snacks)
```

The len() method returns how many items are in a list where index value counts from 0 and is an address.


### append
What if you want to add or remove something from a list?

Ask students to predict where pasta will be added: at the start or end of the list?


```python
snacks.append('pasta')
```
append adds an item to end of a list.
Have students add two new foods

### remove
```python
snacks.remove('pizza')
```
have students remove one food item

## iteration
Have students code with you.

Let's create a short program that will print out all the food in our list.

```python
for food in snacks:
  print(snacks)
```
