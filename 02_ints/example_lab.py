#Prompt user for birth year, month, and date and assign each to a unique variable
birthyear = input("What is your birth year? ")
birthmonth = input("What is your birth month? ")
birthdate = input("What is your birth date? ")

#Return user birthday
print("Your birthday is " + birthdate + "/" + birthmonth + "/" + birthyear)

#Prompt user for today's date, including the year, month, and date and assign each to a unique variable
currentyear = input("Next question: What year is it? ")
currentmonth = input("What month is it? ")
currentdate = input("What day is it? ")

print()
#Print confirmation message
print("Today is " + str(currentdate) + " " + str(currentmonth)+ " " + str(currentyear) + ".")
confirmbday = input("Is that correct? (Y or N) ")

#Check confirmation response
if confirmbday == "Y" or confirmbday == "y":
  print ("Great!")
else:
  print ("Sorry, let's confirm your birthday.")
  currentyear = input("Next question: What year is it? ")
  currentmonth = input("What month is it? ")
  currentdate = input("What day is it? ")

westernAge = int(currentyear) - int(birthyear)
koreanAge = int(currentyear) - int(birthyear) + 1

print()
print("Your Western age is " + str(westernAge))
print("Your Korean age is " + str(koreanAge))
