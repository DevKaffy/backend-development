employees = [
  {
    "Name": "Balikis",
    "Details": {
      "age": 23,
      "tasks": ["handling data", "procurement"],
    },
  },
    {
    "Name": "Mariam",
    "Details": {
      "age": 30,
      "tasks": ["supervising", "advisory"],
    },
  },
    {
    "Name": "Kafilat",
    "Details": {
      "age": 15,
      "tasks": ["coding", "debugging"],
    },
  },
      {
    "Name": "Mufidah",
    "Details": {
      "age": 25,
      "tasks": ["administration", "supervising"],
    },
  },
];

# First task of the first employee
# first_employee_tasks1 = employees[0]["Details"]["tasks"][0]
# print(first_employee_tasks1)


# Print names of employee
# for emp in employees:
#     print(emp["Name"].upper())


# use generator comprehension
# def employee():
#     for emp in employees:
#       yield emp["Name"].upper()
# print(employee())
# employees_name = iter(employee())
# print(next(employees_name))


# list_instance = [1, 2, 3, 4, 5]
# convert list to an iterator
# iterator = iter(list_instance)

# return items at a time
# print(next(iterator))
# print(next(iterator))

# for i in list_instance:
#     print(i)


# def factors(n):
#     for val in range(1, n+1):
#         if n % val == 0:
#             yield val
# print(factors(20))

# factors_of_20 = iter(factors(20))
# print(next(factors_of_20))
# print(next(factors_of_20))
# print(next(factors_of_20))

# for i in factors_of_20:
#     print(i)


# Use generator to print out each name in the list
users = ["sarah", "Ade", "Sola", "Hamidah"]
def user_names(users):
   for i in users:
      yield(i)
print(user_names(users))
names_of_users = iter(user_names(users))
print(next(names_of_users))
print(next(names_of_users))


#generator comprehansion
# print((val for val in range(1, 20+1) if n % val == 0))