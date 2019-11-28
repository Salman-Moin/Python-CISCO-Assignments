#Assignment 2b
#Write a program which takes input from user and identify that the given number is even or odd?
#Author Salman Moin
no1 = input('Enter first number: ')
no2 = input('Enter second number:')
if no1 % 2 == 0:
    print('First number ' + str(no1) + ' is even number')
else: 
    print('First number ' + str(no1) + ' is odd number')
if no2 % 2 != 0:
    print('Second number ' +str(no2) + ' is odd number')
else:
    print('Second number ' + str(no2) + ' is even number')
