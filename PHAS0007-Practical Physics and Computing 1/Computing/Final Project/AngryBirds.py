#Importing the libraries we will be needing in this notebook.
import numpy as np
#Importing the necessary VPython functions which we will be using in the program
from vpython import sphere, color, rate, canvas, vector, curve, label, box, cross, mag, random, arrow

###PARAMETERS###

#The parameters of the target
#Position Vector of the centre of mass of the target


#Dimensions of the target
target_length = 0.5 #metres
target_height = 2 #metres
target_width = 0.5 #metres
target_mass = 100 #kg


#Parameters of the platform
platform_length_half = 0.5


#The parameters of the bird
bird_mass = 0.1 #kg
bird_radius_calculations = 0.05 #metres. This radius will be used in all the back-end calculations.
bird_radius_animation = 0.3 #metres. This radius will be used when showing the ball in animations.

def initialise_game():
    #Creating the background of the whole game
    scene = canvas(width=640,
                   height=480,
                   center=vector(8,5,0),
                   range=8)

    #Creating the ground
    ground = curve(pos=[(0,0,0),(16,0,0)],
                   color=color.green)

    #Creaing Platform for the bird
    #First we set the variable "platform_height" to be equal to a random number between 1 and 0
    platform_height = random()

    #Here We have finally defined our platform using the variables we have set above.
    platform = curve(pos=[((-platform_length_half),platform_height,0),(platform_length_half,platform_height,0)], 
                     color=color.white)
    
    #Target parameters
    x_random_centre = 10*random() + 5
    target_x_centre = x_random_centre
    target_y_centre = target_height/2
    target_z_centre = 0
    target_position_vector = vector(target_x_centre, target_y_centre, target_z_centre)
    
    #Create target
    target = box(pos=target_position_vector,
                 length=target_length,
                 height=target_height,
                 width=target_width)

    #Initial Position of the bird
    bird_x0 = 0
    bird_y0 = platform_height
    bird_z0 = 0

    #Create bird
    bird = sphere(pos=vector(bird_x0, bird_y0, bird_z0),
                  radius=bird_radius_animation, 
                  color=color.red)
    
    return;


#Before we begin our simulation we will need to define

def ask_values():
    angle0_degrees = float(input("What angle (degrees) would you like to launch your bird at? "))
    v0 = float(input("What velocity (m/s) would you like to launch your bird at? "))
    return;

def bird_position(t):
    r_x = bird_x0 + v0*t*np.cos(angle0)
    r_y = bird_y0 + v0*t*np.sin(angle0) - ((g*(t**2))/2)
    r = vector(r_x,r_y)
    return;



