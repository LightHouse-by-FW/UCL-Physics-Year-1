#The following code is able to calculate
#the time taken and final velocity of any
#particle depending on the intial conditions,
#which in this case are of a ball falling from a height
#of 15 metres to 0, on earth.
#This was debeggued by Frederico Wieser and ...
from math import sqrt

g = -9.81 #earth's gravitational constant
v0 = 10 #Inital velocity
z0 = 15 #Intial height
z = 0 #Final displacement

v2 = v0**2 + 2*g*(z-z0)
#Equation to calculate the final velocity of the particle, in metres per second

speed = sqrt(v2)

if v0 > 0:
    print("v0 is positive")
else:
    print("v0 is less than or equal to zero")

time_taken = -(speed + v0)/g
#time taken to reach the final velocity, in seconds
print(str(speed) + " m/s", str(time_taken) + " s")