'''
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
    90 and above: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
Output: Display the calculated grade.
'''

#This is the input section
#Promt the user to enter their marks for three subjects

mark_1 = float(input('Please enter your mark for subject 1:'))
mark_2 = float(input('Please enter your mark for subject 2:'))
mark_3 = float(input('Please enter your mark for subject 3:'))

#processing: calculate the average
average = (mark_1+mark_2+mark_3)/3

#determine the letter grade based on the average
if average >= 90:
    grade = 'A'
elif average >=80:
    grade = 'B'
elif average >=70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

#output: Display calculated grade as letter
print (f'Your average grade is {grade}. ')
