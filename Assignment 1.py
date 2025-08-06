'''

    Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
    =============================
    Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
    Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
    Output: Display the calculated simple interest.

'''

#starting the input section below
principal = float(input ("Enter the principal rate"))
rate = float(input ("Enter interest rate:"))
time = float(input("Enter the time period:"))

#This is the processing section

simple_int = (principal * rate * time)/100

#this is the output
print ("The calculated simple interest is:", simple_int)
print(f"The calculated simple interest is: {simple_int}")