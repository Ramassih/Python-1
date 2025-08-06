'''
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
    Under 18: Minor
    18-65: Adult
    Above 65: Senior citizen
Output: Display the category based on the entered age.
'''

#This is the input section
#Promt the user to enter their age

age_input = input('Please enter your age:')

#check if input is a number and not an empty string
if age_input.isdigit():
    age = int(age_input)

    #We need to make sure the age is positive
    if age > 0:
        #start my classification
        if age < 18:
            print ('Minor')
        elif 18 <= age <=65:
            print ('Adult')
        else:
            print ('Senior Citizen')

    else:
        Print('Age must be a positive number.')
else:
    print('Error:Invalid input! Please enter a positive number.')




