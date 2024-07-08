# birth_Year = int(input("Enter your birth year?"))
# age = 2024 - birth_Year
# print(age)

# course = "Python for Beginners"
# print(course.replace("for", "4"))
# print(course.find("for"))

# temperature = 50
# if temperature <= 30:
#     print("it's a hot day")
#     print("Drink a lot of water")
# elif temperature <= 20:
#     print("It's a nice day")
# else:
#     print("It's cold")


# weight = int(input("Weight: "))
# size = (input("(K)g or (L)bs: "))
# if size.upper() == "K":
#     converted = weight / 0.45
#     print("weight in kg: " + str(converted))
# elif size == "l":
#     converted = weight * 0.45
#     print("weight in lbs: " + str(converted))
# else:
#     print("It is not a weight")


# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    # i = i + 1

# x = 1
# while x <=10:
#     print(x * '*')
#     x = x + 1

# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)

digits = [1, 2, 3, 4, 5]
i = 0
while i < len(digits):
    print(digits[i])
    i = i + 1

numbers = range(5, 10, 2) 
# from (5) to (10) by (2 digits)
for number in numbers:
    print(number)

# We use square bracket to define a list and normal bracket to define tuples
    # tuples are unchangeable or immutable unlike array


temperature = 30
if temperature > 30:
    print("it's a hot day")
elif temperature > 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")



name = input("Enter your name ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good!")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit:
    your_guess = int(input("Make a guess "))
    guess_count += 1
    if your_guess == secret_number:
        print("You won!")
        break
else: 
    print("Soryy, you failed!")