# Create a Banking System that allows users to manage bank accounts. This system should be able to handle basic operations such as creating accounts, depositing and withdrawing funds, transferring money between accounts, and 
# viewing account details.

# 1.creat a function to find a acount by account number
#2. create a function to find an employee by id



class Account: 
    user = []
    def __init__(self, account_name, account_number, account_type, account_balance):
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        self.id = id
        self.account_balance = account_balance

    def create(self):
        Account.user.append(self)
        print(f"{self.account_name}, your account has been created")

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Amount must be greater than 0")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Amount must be greater than 0")

    def transfer(self, recipient_account, amount):

        for acc in Account.user:
            if acc.account_number == recipient_account:
                if self.account_balance >= amount:
                    self.account_balance -= amount
                    print(f"You transferred {amount} to {recipient_account}, new balance is {self.account_balance}")
                else:
                    print("insufficient fund")
            else:
                print("account does not exist")

    def find_account(self, account_number):
        for acc in self.user:
            if acc.account_number == account_number:
                print(f"account found: {acc}")
            else:
                print(f"account not found")
        

    def __str__(self):
        return f"{self.account_name} with account number: {self.account_number} {self.account_type} has a balance of {self.account_balance}"


first_user = Account("Kafilat Eniola", 124544453, "Savings Account", 25000)
second_user = Account("Balikis Olaide", 3455656565, "Savings Account", 20000)
third_user = Account("Adeola Adeboye", 45896565, "Current Account", 90000)
first_user.create()
second_user.create()
third_user.create()
print(first_user)
first_user.deposit(10000)
print(first_user)
first_user.withdraw(5000)
print(first_user)
first_user.transfer(3455656565, 3000)
# first_user.find_account(124544453)
# found_account = Account.find_account(124544453)
# if found_account:
#     print(f"Account found: {found_account}")
# else:
#     print("Account not found.")



#  Create an Employee Management System (EMS) that allows users to manage employee records. This system should be able to handle basic operations such as adding, removing, updating and viewing employee details.

#Initialize the attributes
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

#String representation of each employee
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, position: {self.position}, salary: {self.salary}"
    
    def update_position(self, new_position):
        self.position = new_position

    def update_salary(self, new_salary):
        self.salary = new_salary

class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        for employee in self.employees:
            if employee == name:
                self.employee.remove(employee)
            else:
                print("employee is not present")

    def update_employee(self, name, new_salary, new_position):
        for employee in self.employees:
            if employee.name == name:
                if new_position:
                    employee.update_employee(new_position)
                if new_salary:
                    employee.update_employee(new_salary)
            else:
                print(f"Employee named {name} not found.")

    def view_all_employees(self):
        for i in self.employees:
            print(i)

    def find_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                print(f"{employee}")
            else:
                print(f"Employee name not found")


        
        

        




