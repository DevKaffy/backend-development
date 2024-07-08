# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def addition(a, b):
    sum = a + b
    return sum
print(addition(a=6, b=5))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle(PI, r):
    area_of_a_circle = PI * r * r
    return area_of_a_circle
print(circle(PI = 100, r= 5))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print(add_all_nums(2, 3, 4))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    lower_case_month = month.lower()
    if lower_case_month in ['january', 'march', 'february']:
        print("Autumn")
    elif lower_case_month in ["july", "august","september", "october"]:
        print("Spring")
    elif lower_case_month in ["april", "may","june"]:
        print("Winter")
    elif lower_case_month in ["november", "december"]:
        print("summer")
    else: 
        print("Not a month")
check_season("December")


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(*list):
    for i in list:
        print(i)
print_list(3, 5, 6, 7, 1)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]



