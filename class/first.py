# name = input ("What is your name?")
# year = input ("What year were you born?")
# print("Hello " + name + " nice to meet you")
# print("Hello world!")


# Assignment
""" 
lastName = input("What is your surname?")
firstName = input("What is your firstname?")
yearOfBirth = int(input("What year were you born?"))
currentYear = int(input("What is the current year?"))
age = (str(currentYear - yearOfBirth))
print("Hello " + lastName + " " + firstName + "." + " You are " + (age) + " years old.") 
"""





""" 
Define value
Define attempts
while user has not exhuasted attempts
If input is equal to value print "you guessed it right"
If input is greater than value print "your guess is too high"
If input is lesser than value print "your guess is too low"
"""

# import random
# n = random.randrange(1, 10)
# attempts = 5

# while attempts > 0:
#     number = int(input("Make your guess: "))
#     if number < n:
#         print("Your guess is too low")
#     elif number > n:
#         print("Your guess is too high")
#     else:    
#         print("you guessed it right!")
#         break
#     attempts -= 1

#     if attempts > 0:
#         print(f"you have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
#     else:
#         print(f"Sorry, you have exceeded your attempt limit.")

class Dog:
    number = 0
    #_protected = I am a protected variable

    def __init__(self, name):
        self.name = name
        Dog.number += 1
        self.__dognumber = Dog.number

    # def get_dognumber(self):
    #     return self.__dognumber
    @property
    def dognumber(self):
        return self.__dognumber

    # def set_dognumber(self, value):
    #     self.__dognumber = value

    @dognumber.setter
    def dognumber(self, value):
        self.__dognumber = value

    def bark(self):
        print(f"{self.name} says woof!")

Jack = Dog("Jack")
# print(Jack.get_dognumber())
print(Jack.dognumber)
# Jack.set_dognumber(9)
Jack.dognumber = 9
print(Jack.dognumber)
Jack.name = 'bingo'
print(Jack.name)



# getter method is used to make number visible but unchangeable
# setter method is used to make number invisible but changeable.

