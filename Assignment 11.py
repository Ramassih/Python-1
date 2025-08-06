'''Use a loop structure to generate the Collatz sequence until it reaches 1.
Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given
positive integer entered by the user. The Collatz sequence is generated iteratively
by repeatedly applying the following rules:

    If the current number is even, divide it by 2.
    If the current number is odd, multiply it by 3 and add 1.
'''

#This is the input section
# Prompt the user to enter a positive number

user_input = input('Enter a positive number:')

#Check if input is a number and convert it to an integer
# we will need to use a loop to repeatedly ask for input until its a valid number

while True:
    if user_input.isdigit(): #check if the input contains only numbers
        number = int(user_input)
        if number > 0:
            break
        else:
            user_input = input('The number must be a positive number. Enter again:')

    else:
        user_input =('Invalid input. Please enter a positive number:')


#generate and print collatz sequence

print ("Collatz sequence:")

while number != 1:
    print (number, end=' -> ')
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number +1

print(1)