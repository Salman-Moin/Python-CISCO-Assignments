#Assignment 3a
#Make a calculator using Python with addition , subtraction , multiplication , division and power.
#Author Salman Moin

i = 1
no1 = float(input('Enter First Number: '))
no2 = float(input('Enter Second Number: '))
while i > 0:
    operation = raw_input("Select anyone operation to perform: 'add', 'sub', 'mul', 'div', 'exp': ")
    if operation == 'add':
        result = no1 + no2
    elif operation == 'sub':
        result = no1 - no2
    elif operation == 'mul':
        result = no1 * no2
    elif operation == 'div':
        result = no1 / no2
    elif operation == 'exp':
        result = no1 ** no2
    else:
        print('Invalid option selected, please enter the right choice.')
        continue
    break
print('The result of your operation is: ' + str(result))
