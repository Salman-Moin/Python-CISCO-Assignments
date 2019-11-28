#Assignment 3d
#Write a Python program to sum all the numeric items in a dictionary
#Author Salman Moin

gross_salary = 0.0
employees = {"name": "david", "basic_salary": "50000", "allowances": "10000"}
for each_value in employees.values():
    if each_value.isnumeric():
        gross_salary = float(each_value) + gross_salary

print("Gross Salary is: " + str(gross_salary))


