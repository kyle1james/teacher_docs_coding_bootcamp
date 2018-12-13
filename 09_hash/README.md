# Dictionaries

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [Dictionaries](#dictionaries)
2. [Accessing Items](#accessing-items)
3. [list built-in functions](#list-built-in-functions)
4. [iteration](#iteration)



## Dictionaries
A dictionary is an unordered collection denoted by curly brackets. A dictionary is indexed by a key:value system with each pair separated by a comma. The data inside a hash can be anything we have covered.

- ints
- strings
- booleans
- arrays

Code Together:

Ask students to create a dictionary detailing their favorite music genre as the key, and band as the value

```python
my_fav_music = {'surf rock': 'Beach House', 'folk': 'Trampled by Turtles', 'Rap': 'Nas'}

```
Have students print out the dictionary.

## Accessing Items
Each item in a hash has a key:value. To access an item by key, simply follow the below sequence:

```python
dictionary_name[key]
```

Ask students to predict what

```python
my_fav_music['surf rock']
```
will print out

Right, it prints out the value to the key surf rock

### Change Value

Who here can predict how to change the key in a hash?

```python
my_fav_music['surf rock'] = 'The Babies'

```

Pretty simple. Once again, to access the value we provide the data structure name[key] and then define just like we would a variable. Go ahead and change a few of your values.

### Get Key from Value

What if you have the value and want to get the key?

Have students predict what the following code will do

```python
my_fav_music['Beach House']
```
Yikes, an error. Let's try to figure out what happened.

```Python
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    music['beach house']
KeyError: 'beach house'
```
KeyError means that
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
