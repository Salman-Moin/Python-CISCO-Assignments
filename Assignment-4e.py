#Assignment 4e
#Guess the number game - Write a program which randomly generate a number between 1 to 30 
# and ask the user in input field to guess the correct number. Give three chances to user 
# guess the number and also give hint to user if hidden number is greater or smaller than 
# the number he given to input field.
#Author: Salman Moin
#Date: 29-Nov-2019 

import random

random_number = random.randrange(1, 30)
print(random_number)

for i in range(1, 4):
    guess_number = int(input('Guess your number: '))
    if guess_number == random_number:
        print('WOW.....you WON it.....Congrats!!')
        break
    elif guess_number > random_number:
        print('Your guess is greater than the target number.')
    else:
        print('Your guess is less than the target number.')

