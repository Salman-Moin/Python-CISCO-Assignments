#Assignment 2a
#Write a program which takes 5 inputs from user for different subjects marks, 
#total it and generate mark sheet using grades.
#Author Salman Moin
physics   = int(raw_input("Enter Physics Marks: "))
chemistry = int(raw_input("Enter Chemistry Marks: "))
math      = int(raw_input("Enter Math Marks: "))
english   = int(raw_input("Enter English Marks: "))
computer  = int(raw_input("Enter Computer Marks: "))
total_marks_obtained = physics + chemistry + math + english + computer
percent = (float(total_marks_obtained)/ 500) * 100 
if percent >= 90:
    grade = 'A+'
elif percent >= 80 and percent <= 89:
    grade = 'A'
elif percent >= 70 and percent <= 79:
    grade = 'B'
elif percent >= 60 and percent <= 69:
    grade = 'C'
else:
    grade = 'F'

print("\nTotal Marks Obtained out of 500: " + str(total_marks_obtained))
print("Percentage(%): " + str(percent))
print("You have got grade: " + grade)



