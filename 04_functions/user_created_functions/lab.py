# after you test your code, comment it out with a #

################ Defining a function #######################################################

# create a function called hello
# take in a name as input
# return a special hello message with the user's name

def hello(name):
    message = "hello", name
    return message


################ Calling a function  ##################################################################

# call your function here
print(hello('kyle'))

################ Multiple-argument Methods  ###########################################################


# create a function that takes in two numbers as arguments
# output the sum of the two numbers
def sum_me(a,b):
    return a + b

print(sum_me(1000000,-102020))

################ Functions With Multiple Returns ########################################################

# age

# create a function that takes in a user's height as an argument
# output what roller coaster rides the user may ride based on their height
def can_i_ride(height):
    if height > 42:
        print('you can ride these rides...')
    elif height > 52:
        print('you can ride these rides...')
    else:
        print('you did not enter a correct height')



################ Labs  #################################################################################

# lift_off

# create a function that takes in weight and fuel in pounds
# output True or False if your spaceship can make it to orbit
# conditions: 1 pound of weight uses 9.33 pounds of rocket fuel

def lift_off(weight,fuel):
    orbit = fuel - (weight * 9.33)
    if fuel >= 1:
        return True
    else:
        return False

# Mild: return how much more fuel you need to lift_off or how much extra fuel you have
def lift_off(weight,fuel):
    orbit = fuel - (weight * 9.33)
    if fuel >= 1:
        return "you have", fuel, "extra"
    else:
        return "you need" fuel, "more pounds of fuel"
# Spicy: return how many 180 pound humans you can bring on your trip
def lift_off(weight,fuel):
    orbit = fuel - (weight * 9.33)
    if fuel >= 1:
        humans = fuel// 180
        return humans
    else:
        return "you need" fuel, "more pounds of fuel just for lift off with no humans"

# what_to_eat

# create a function that takes in the weather: sunny, rainy, cold, and hot
# output what type of food you should eat based on the weather
def what_should_i_eat(weather):
    if weather == 'sunny':
        print('some food')
    elif weather == 'rainy':
        print('some food')
    elif weather == 'cold':
        print('some food')

# mild: add temperature as an additional argument

# just add info to conditionals
# if weather == 'sunny' and temp > 60:

# spicy: add temperature and time of day as input but not as arguments
def what_should_i_eat():
    weather = ['sunny', 'rainy', 'snow', 'fog']
    # when called, the user will see this list printed
    for x in weather:
        print 'here are your choices', x
    # get the user input
    weather_choice = input('what weather did you pick?')
    # to normalize user input all to lower case
    weather_choice = weather_choice.lower()
    # repeat for temp
    # then just add conditionals
# who_am_i

# create a function that asks your user several questions
# output which fictional character the user is based on their answers to the questions
# examples: superhero, hogwarts house, etc.

# mild: have at least 5 output options

# spicy: use Multiple conditional statements such as 'and', 'or', 'not'



################ Create Your Own function  #######################################################

# create a function for a classmate
