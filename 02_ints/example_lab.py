import random

money = random.randint(100,200)
print('you start with', money, 'cash')
health = random.randint(0,50)
money = money - health

print('oh no you got hit by a car and have to pay', health, 'you have', money, 'left')

bonus = random.randint(20, 40)
print('you got a bonus of', bonus, 'at work')
fun = int(input('how much money do you use for fun?'))
bonus = bonus - fun
print('you have', bonus, 'left')
savings = int(input('how much money do you put into savings?'))
money = money + savings - fun
print('cool, you have', money, ' left')
market = random.randint(100,200)
money = money - market
print('oh no, the market crashes and you lost', market, ' you now have', money, 'left')
