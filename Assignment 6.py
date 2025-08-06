''' Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency. '''

#start input section below
dollar = float (input ("Enter dollar amount in USD:"))

# calculate exchange rate EGP
egp = (dollar * 49.51)

#output usd to egp

print ("The Egyptian currency amount:",egp)

