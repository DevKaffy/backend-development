# for number in range (2, 20, 3):
#     print(number)



# fruits = ["mango", "orange", "apple", "banana"]
# for fruit in fruits:
#     print(fruit)



#Calculate area of a rectangle
# def area(length, breath):
#     return length * breath
# print(area(4, 5))


# write simple function that calculate interest.
    
# def interest(P:int, R, T, a=100):
#     result = (P * R * T) / a
#     return result
# print(interest(30, 12, 7))


#Assignment
# principal, rate and time should only take regular number  but not more than 100 while the time must be in months.

"""
principal: only int
rate: int but not more than 100
time: must be in months (optional: if value is greater than 12 divide by 12)
"""

def calculate(P:int, R:int, T:int, a=100):
    if not isinstance(P, int):
        print("principal must be an integer")
    elif not isinstance(R, int) or R > 100:
        print("Rate must be an integer and not greater than 100")
    elif not isinstance(T, int):
        print("Time is representing months and must be an integer")

    if T > 12:
        T= T / 12

    interestResult = (P * R * T)/a
    return interestResult
interestResult = calculate(5.7, 10, 24)
print(f"interestResult: {interestResult}") 


""" Write a function count_movies_by_genre(movies) that takes the list of movies as input.
The function should iterate through the movie list and count the occurrences of each genre.
Use a dictionary to store genre names (as keys) and their corresponding movie counts (as values). """

""" Write another function find_movies_after_year(movies, year) that takes the movie list and a year as input.
The function should iterate through the movie list and return a new list containing only movies released after the specified year (including the given year).
Use list comprehension or a loop with conditional statements to filter movies based on the year. """

""" Write code to call the functions and process the movie data.
Use range to iterate through specific elements or a loop to iterate through the entire data structure.
Print the results in a user-friendly format, ( the total number of movies, movie counts by genre, and a list of movies released after a specific year) """

# movies = [
#     ["Casablanca", "Michael Curtiz", 1942, "Drama"],
#     ["The Godfather", "Francis Ford Coppola", 1972, "Crime"],
#     ["The Shawshank Redemption", "Frank Darabont", 1994, "Drama"],
#     ["The Dark Knight", "Christopher Nolan", 2008, "Action, Thriller"],
#     ["Living in Bondage", "Ola Balogun", 1992, "Drama"],
#     ["Nneka the Pretty Serpent", "Christian Chukwu", 1994, "Drama, Thriller"],
#     ["Rattlesnake", "Amaka Igwe", 1995, "Crime, Thriller"],
#     ["Aki na Ukwa", "Chico Ejiro", 2002, "Comedy"],
#     ["Saworo IDE", "unknown ", 1997, "Drama"]
# ]

x = 0
while x < 5:
    x += 1
    print(x)