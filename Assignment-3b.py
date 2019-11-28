#Assignment 3b
#Write a program to check if there is any numeric value in list using for loop
#Author Salman Moin

list = ['a', 'b','c', 'd', 4, 'e', '9', 'f', '25', 19]
for i in list:
    if str(i).isnumeric():
        print(i)
