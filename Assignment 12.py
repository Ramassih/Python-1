'''
Challenge: Use nested loop structures to print the pattern efficiently and neatly.
Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern
and then prints a pattern of asterisks (*) in the form of a right triangle.
'''

#input section prompt the user to enter the number of rows

rows=int(input('Enter the number of rows:'))

#prompt the user to enter the pattern character
char = input ('Enter the characters to use for the pattern:')

for i in range(1, rows + 1):
    for j in range(i):
        print(char, end ='')

    print()