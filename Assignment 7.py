''' Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not. '''

#This is the input section
#Promt the user to enter a year

year = int (input('Please enter a year:'))

#Processing : We check if year is a leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} IS A LEAP YEAR!")
else:
    print(f"{year} IS NOT A LEAP YEAR")