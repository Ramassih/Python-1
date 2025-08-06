'''
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

#ask the user to enter a character
char_input = input('Please enter a single character:')

#check if input is exactly one character and is a letter

if len(char_input) ==1 and char_input.isalpha():
    # convert the character to lowercase
    char =char_input.lower()

    if char in 'aeiou':
        print ('The character is a vowel')
    else:
        print('The character is a consonant')
else:
    if len(char_input) != 1:
        print('Error: Please only enter one character')
    else:
        print ('Error: The input is not a letter')