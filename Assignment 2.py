
'''Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.'''
#starting the input section below
Length = float(input ("Enter Length of rectangle"))
Width = float(input ("Enter Width of rectangle:"))

#This is the processing section

Area = (Length * Width)

#this is the output
print (f"The calculated area is:", {Area})

