# Multi Case Conditionals

[Return to Overview](./README.md)

#### Sequence

1. [Framing](#framing)
2. [Terminology](#terminology)
3. [Multiple-argument Methods](#multiple-argument-methods)
4. [Methods Without Arguments](#methods-without-arguments)
5. [Methods With Multiple Returns](#methods-with-multiple-returns)
6. [Methods Without Returns](#methods-without-returns)
7. [Returns as Breakpoints](#returns-as-breakpoints)

## Framing

We've already been using methods - but they are all built into the core of Python, like len() and range() all take in an **argument** as *input* and produce some data called a **return value** as an *output*.

So far, you've seen methods used like this:
* methodName(argument) => returnValue
* len("shiba") => 5

Consider the following methods:

```python
len("shiba")
```
This method takes in a string "shiba" as an argument, and returns an integer 5 as a return value.

```python
"Taylor".upper()
```
This method takes in a string "Taylor" as an argument, and returns the string 'TAYLOR' as a return value.

But even though methods like this are built-in, if we want to build powerful programs, we'll need to create some custom methods.

## Terminology

#### Defining a method

Here's the general form for DEFINING a method:

```python
# DEFINE a method
def methodName(parameters, separated, by, commas):
  internalCode
  return return_value

```

So with that in mind, try to name the parts of this function

```python
def shout(name):
  name = name.upper()
  return "HELLO",name,"!"

```

Questions to ask:
* What is the name of this method?
* How many parameters does this method have?
* What datatype will we use for the name parameter? *reference the anchor chart*
* What datatype is the return value?

#### Calling a method

```python
# DEFINE the method
def shout(name):
  name = name.upper()
  return name


# CALL the method (use it)
shout("Britney")
```

When we **call** a method, the data we fill in for the parameter is called an **argument**. What datatype is the argument we provided?

Ask students to predict what will come out - most will say "BRITNEY!". This is an intentional error. Run the program and identify that nothing comes out. Then ask "What did we do to make information print out to the console?" Refactor the program with a `print` wrapped around the call.

```python
def shout(name):
  name = name.upper()
  return name


print(shout("Britney"))
```

Ask students why we use the general word name as a parameter of the definition, but use a specific string "Britney" as the argument of the call?

Ask students to come up with an explanation for why a method needs a puts statement to show you the answer. *Why is it better that the computer only prints information when you explicitly code it to do so?* One answer: Imagine if you're writing a complex program like a videogame, and hundreds of methods are being run every second. Would a user really want to see ALL that behind-the-scenes information?

That's why we primarily use puts statements to debug our code. Ultimately, we want the computer to do most of the work behind the scenes, and only share *final* information with the user.

## Multiple-argument Methods

Tell students that we will build a method that tells us how much it costs to go to Disney Land. Prices change a lot so if you want to look up that day's prices you can, but these rounded numbers are good for easy math.

Share this information with students:
Cost for adults: $100/ticket per day
Cost for children: $90/ticket per day

Ask students:
* How much will it cost for 1 adult and 1 child to go for one day?
* How much will it cost for 2 adults to go for three days?
* How much will it cost for 1 adult and 2 children for one day?

Ask students how they did these problems, and write their code somewhere they can see it. Identify that they're saying they did these things:
1. Multiply adults times 100.
2. Multiply children times 90.
3. Add these two values together.
4. Multiply that by the number of days.
(Obviously, some kiddos will have different methods. Validate these and high five these students for finding different solutions)

Before starting, ask "So which pieces of information do we need from a family before we can calculate their cost?"
Students will identify number of adults, number of children, and number of days as the necessary information. Once these are identified, say "So we'll need three parameters to define our method, and we'll provide three arguments when we call it. "

```python
def costOfDisneyFor(number_of_adults, number_of_children, number_of_days):
  adult_cost = number_of_adults * 100
  print("Calculated adult cost at", adult_cost) # We'll use this debug statement to make sure our code is running.
  child_cost = number_of_children * 90
  print("Calculated child cost at", child_cost) # This is another debug statement.
  daily_cost = adult_cost + child_cost
  total_cost = daily_cost * number_of_days
  return total_cost

```

Once this is on the board, but before you run it, ask these questions:
* How many parameters did we use to define this argument?
* What datatype will we use as arguments when we call the function?
* What datatype will the return value be?
* How many internal lines of code are there in this method?
* Right now, if we ran this program, nothing would actually happen. Why is that?

Once students identify that the method has never been called, and that the return is never printed out, refactor the program.

```python
costOfDisneyFor(*,*,*)
# OR
print(costOfDisneyFor(*,*,*))
```

When you arrive at the asterisks, ask students "What information do I need for my first argument? What datatype should it be?" Make up any number of adults, children, and days, but make sure that students identify them and can tell you WHAT you're calculating before you run it.

Once you run this successfully on a few test cases, ask "How would I compute the cost of bringing 43 adults and 67 children to Disney for 5 days?"

Ask what questions students have. Try to push them to think through some edge cases:
* What happens if we put in strings instead of numbers?
* What happens if we forget to include the third piece of information: number of days?
* What happens if we don't puts the call of the function?

#### Playtime

* Write a method that takes in a string as an argument and returns the number of letters in that string

```python
def how_long(string):
  return len(string)
```

* Write a method that takes in three numbers and product of all three

```python
def product_three(num1, num2, num3):
  ans = num1 * num2 * num3
  return ans
```
* Write a method that takes in a user's name and then returns their name with a greeting

```python
def name(user_name):
  greeting = "hello "+ user_name +" what a strange name"
  return greeting
```
#### Takeaways

* METHODS - explain what a method is and why it's used
* METHODS - use built in methods for each data type and structure
* METHODS - create a custom method using def and end key words
* METHODS - explain what a return value is and what it's used for
* METHODS - explain and determine the return value of a method
* METHODS - explain that puts is used to debug a method, and that return is used to provide output
* METHODS - explain the difference between defining and calling a method
* METHODS - call previously defined custom methods
* METHODS - use correct syntax in naming methods
* METHODS - create a custom method with multiple arguments

## Methods Without Arguments

Sometimes you need a function performed that doesn't require any arguments. For example, if you wanted to remember what Pi is to 14 digits, you wouldn't need ANY information from the user. You could wrap that in a method like this.

```python
def pi_reminder():
  return 3.14159265358979

```

Ask students if they already know another way to store information like this - students will identify variables as the way to do it. Acknowledge that for that very reason, methods without arguments are uncommon.

## Methods With Multiple Returns

```python
# Define the method!
def personalized_age_check(name, age):
  if age >= 18:
    return "Congratulations "+ name + " ! You're old enough to vote"
  else:
    time_left = 18 - age
    return "Sorry, "+ name + ". You can't vote for another "+ str(time_left) + " years."

# Note: we wrap time_left with the built-in function str so that an int datatype may be printed out in string interpolation

# Call the method
print(personalized_age_check("Jeff", 28))
print(personalized_age_check("Zara", 14))
```

Have students predict what will happen when this program is run.

## Break for Labs

At this point, students have been exposed to enough information to understand how to do these labs:
- TODO: Add labs once made

## Methods Without Returns

```python
def add(x, y):
  print("Adding your numbers")
  total = x + y
  print("Your numbers add up to", total)
```
# Note: we did not use string interpolation so no need to change that datatype of total

Have students identify that this method needs to be called, and that without a print statement, nothing will be visible.

```python
# Definition
def add(x, y):
  "Adding your numbers"
  total = x + y
  "Your numbers add up to", total


# Call
print(add(5, 22))
```

Before you run this, ask students what they think will happen since there are no return values. Anticipate that students will ID one of the following:
* Nothing will be printed since nothing is returned.
* It will print all the lines of code, since nothing was specified as the return value.



## Returns as Breakpoints

What about this?

```python
# Definition
def add(x, y):
  return "Adding your numbers"
  total = x + y
  return total
  return "Your numbers add up to", total
  return "Program finished!"


# Call
print(add(5, 22))
```

Ask students to predict what will happen when we try to return EVERY line of code. Anticipate the following:
* It will print out all four.
* It will print only the last one.
* It will print only the first one.

Clarify that a when a method reaches a return value, it stops executing the method and immediately returns that value. This is great! It saves time and processing power; why keep looking for more returns when you've already found one?

#### Takeaways

* METHODS - describe what will happen when there is no explicit return
* METHODS - explain that the first return will prevent the rest of a method from running
