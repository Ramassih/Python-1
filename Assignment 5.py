''' Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds. '''

#start input section below
hr = float (input( "Enter amount of time in hours:"))


# calculate the hr in minutes and seconds
min = (1*60)
sec = (60*60)

 #output
print("The time in hours as minutes is :", min)
print("The time in hours as seconds is", sec)