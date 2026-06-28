#Write a program to create a class Employee and perform the following tasks:
#Create a class variable company_name.
#Create an __init__() method with instance variables emp_id, name, and salary.
#Create two employee objects.
#Print the class variable.
#Print the employee details.

class Employee:
    company = "Google"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

emp1 = Employee(101, "Alice", 5000)
emp2 = Employee(102, "Bob", 6000)

print(Employee.company_name)

print(emp1.emp_id, emp1.name, emp1.salary)
print(emp2.emp_id, emp2.name, emp2.salary)