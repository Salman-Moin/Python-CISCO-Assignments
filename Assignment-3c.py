#Assignment 3c
#Write a Python script to add a key to a dictionary
#Author Salman Moin

customer = {"first name": "David", "lastname": "Elliott", "address": "4803 Wellesley St."}
customer["eamil "] = "david.elliott@gmail.com"

for each_key, each_value in customer.items():
    print("The customer's " + each_key + "is " + each_value)
