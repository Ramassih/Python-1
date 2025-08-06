
'''
Challenge: Use a loop structure to compare characters from
both ends of the string to determine whether it is a palindrome.

Description: Write a program that prompts the user to enter a string
and then checks whether it is a palindrome. A palindrome is a word,
phrase, number, or other sequence of characters that reads the same
forward and backward.
'''

# Prompt the user for input
user_input = input("Enter a string: ")

# Remove spaces and convert to lowercase for uniformity
palindrome = ''.join(user_input.split()).lower()

# Initialize pointers at both ends
left = 0
right = len(palindrome) - 1

# Assume it's a palindrome unless proven otherwise
is_palindrome = True

# Loop to compare characters from both ends
while left < right:
    if palindrome[left] != palindrome[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

# Display result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")