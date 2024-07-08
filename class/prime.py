num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]

#list comprehension to get the square of the prime numbers
squares = [x**2 for x in num if x > 0 and x < 20 if x%2 ==1]
primes = [n for n in num if all  ( n % i !=0 for i in range(2, n)) and n > 1]
print(squares)
print(primes)


words = ["list", "create", "word", "each", "new"]
capitalize_word = [n.capitalize() for n in words]
print(capitalize_word)

# Print string that have length greater than 4
strings =[n for n in words if len(n) > 4]
print(strings)


# Create a list of tuples where each tuple contains the number and the cubes
cube = [(x, x**3) for x in num]
print(cube)

"""
FizzBuzz Problem

Write a problem that prints numbers from 1 to 1000 (or any other specified)
for multiples of 3, print "Fizz" instead of the number.
for multiples of 5, print "Buzz" instead of the number.
for multiples of oth 3 and 5, print "FizzBuzz" instead of the number.
"""


# fizzBuzz = ["FizzBuzz" if a % 15 == 0 else "fizz" if a % 3 == 0 else "buzz" if a % 5 == 0  else str(a) for a in range(1, 101)]
# print(fizzBuzz)


"""
FizzBuzz Problem

Write a problem that prints numbers from 1 to 1000 (or any other specified)
for multiples of 3, print "Fizz" instead of the number.
for multiples of 5, print "Buzz" instead of the number.
for multiples of oth 3 and 5, print "FizzBuzz" instead of the number.
"""

fizzBuzz = ["Fizz" if y % 3 == 0 else "fizz" if y % 5 == 0 else "FizzBuzz" if y % 15 == 0 else str(y) for y in range (1, 101)]
print(fizzBuzz)



#lamda method
