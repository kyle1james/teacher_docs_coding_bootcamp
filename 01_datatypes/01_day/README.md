
# Intro to Programming

[Return to Overview](https://github.com/kyle1james/teacher_docs_coding_bootcamp/blob/master/README.md)

#### Sequence

1. [Hello World](#strings)
2. [String Concatenation](#string-concatenation)
3. [User Input](#user-input)
4. [Lab](#chatbot-lab)

## Hello World

First, code the following. Have students wait until you are done to do the same but for their name.

```python
print(“hello Kyle”)
```


Explain that `print` will print what is inside the parentheses. And anything in quotes is a **String** of characters. A string essentially represents a word or phrase.


#### Playtime

* Print out a few more statements. Examples:
Say “hello” a few different ways or even in a few different languages
Ask a few follow up questions. Ex. How are you?

#### Variables

```python
name = “Kyle”
print('hello '+ name)
```
Explain that name is a variable, not a string. In computer science, a variable is a placeholder and we assign a value to it.

Questions:
- have students predict what will happen
- ask students what name did?


In python, to define a variable you give a name and then a value. The name is always on the left side and the value is always on the right side.


Let’s try changing our variable. Underneath let’s add a new value for name and print again.

```python
name = “Kyle”
print(“hello “+ name)
name = “Matt”
print(“hello “+ name)
```

Questions:
- What happened to the name?
- Why do you think this happened?

## String Concatenation

Let's code a few variables together. Ask students, make sure to stay with string datatypes!

```python
name = “Eddie”
food = “Pizza”

print(“hello my name is '+name+'and I love” + food)

```

## User Input
So far this great, but we are just printing out the same statements that we coded. What if you want to get user input?

```python
name = input(“what is your name?”)
print(“hello” +name)
```

- Have students predict what will happen, then run the code.

Explain that what you type is the input
And the output is the variable


Let’s add to program. We now know enough to create a basic chatbot.

```python
name = input(“what is your name?”)
print(“hello” +name)
age = input(“how old are you, ” + name + “ ?”)
print(“Wow, you are ” + age + “ years old”)
```

Before you run the program, have students predict what will happen.

This will trigger an intentional error since numbers are a different data type than string. For now, just explain that we will not use numbers as user input for today’s lesson. We will begin using them next time.

Run the program and change the variables based on students in the class.


Change the second question from an age question to something else such as favorite food.

```python
name = input(“what is your name?”)
print(“hello” +name)
food = input(“What is your favorite food?”)
print(food + “, sounds yummy!”)
```


## Chatbot lab
Today you are going to create a chatbot program.

- Create a chatbot that will talk with the user to ask them about the following
Name
Favorite food
Secret word or phrase

- Take the user input and return it back to them in the chatbot’s response before moving onto the next question.

### CHALLENGE ZONE

The Turing test is a test of artificial intelligence proposed by Alan Turing. If a computer can participate in a conversation with a human without that human suspecting that it is a computer, then the computer could be said to be artificially intelligent.

See how convincing you can make your chatbot’s conversation.

#### PANIC ZONE!

- Print out a 5-sentence story with 5 different statements
