#Date: 12/10/2018
#Names: Daniel Santos and Frederico Wieser
#Task: The aim of this program is to be able to calculate pi/4 to
#any given accuracy given by a user, using loops.

import numpy

#This line prints the Numpy value of Pi/4
print("The exact value of pi/4 is " + str((numpy.pi)/4))
#The precision we require:
tolerance = float(input("The tolerance yo would like to use for this approximation? "))
n = 0 #Initialize the counter
newterm = 1 #Any number will start the loop long as its value is greater than the tolerance
value = 0 #Let the series start with value of zero
#This while function will act as the way we will do our summation for the approximation
#of Pi/4. 

#For the 'while' function to work, it is neccesaary that we made used the absolute value
#of the newterm since newterm will be negative for odd values of n, which would stop the loop.

while abs(newterm) > tolerance:
    newterm = ((-1)**n)/(2*n + 1) #Each terms for the series.
    value = value + newterm #Replaces the value 
    n = n + 1 #Increases value of n by one every loop


difference = abs(((numpy.pi)/4) - value)
print("The number of iteration of the loop is " + str(n))
print("Our value of pi/4 is " + str(value))
print("The difference of our approximation and the numpy value of pi/4 is " + str(difference))

#We think that we are justified in claiming that our result is accurate to n
#decimal places for the tolerance because for all of our results so far the
#difference between the actual value and our approximated value has always been
#close to half of the tolerance. At the same time we think that this difference 
#may change the nth decimal number, which would make it inaccurate to the nth decimal
#place.

#We extrapolated our results by timing how long it took to calculate up to
#7, 8, and 9 decimal places we noticed that as we increased the accuracy by one
#decimal place the time taken to approximate this value multiplied by ten.
#This is further supported by the fact that the number of iterations tenfold
#every time the accuracy incereases by 1 decimal place.

#We used this pattern to calculate that for 16 decimal places the time taken
#would be 100 years; and for 32 decimal places 10^18 years.

#We think that this method of approximation is effective for small number of 
#decimal places (e.g. up to 7 decimal places). And anything beyond takes 
#a significant amount of time.