

# import programs
from sympy import *
import numpy as np


# creating function
def dunk(height_user, weight_user, rim_height_user, ball_user):

# takes into account if user wants to dunk ball or touch rim
    if ball_user == 0:
        weight_bball = 0
        height_bball = 0

# uses dimentions of a basketball
    else:
        weight_bball = 1.3
        height_bball = .883

#converts imperial to mertric
    height_m = height_user * .0254
    weight_kg = (weight_user + weight_bball) * .453592
    rim_height_m = rim_height_user * .3048
    height_bball_m = height_bball * .3048

# changing height to max reach using ration
    reach_user = height_m * 1.35

# finding distance from user to rim
    height_GPE = rim_height_m - reach_user

#setting gravity constant
    gravity = 9.81


# GPE = KE
# .5mv^2 = mgh
# v^2 = 2gh
# v = (2gh)^.5
    velocity = sqrt(2 * gravity * height_GPE)


# turns height_GPE from a number to varrible
    height_GPE = Symbol('height_GPE')

#v -> v'
    velocityp = velocity.diff(height_GPE)


#F = m * a
#a = v'
#F = m * v'
    force_newtons = weight_kg * velocity

# convert into pounds
    force_pounds = force_newtons * .224809

# add the user weight to force needed
    force_needed = force_pounds +  weight_user

# display results
    print("You would need", force_needed, "of force inorder to dunk")

# running function
# enter "0" for touching the rim, and "1" to dunk"
# examples / proof

# Me (jake): 180 pounds of force needed
dunk(68, 130, 10, 1)

# Stephane: 175 pounds of force needed
dunk(72, 130, 10, 1)

# Mr. James: 202 pounds of force needed
dunk(72, 150, 10, 1)

# follows laws of physics 
# shows that weigth matters far more than height
# this beucase the typical range of weight is greater than that of height










# https://mcanv.com/Answers/qa_vjc.html
# https://www.whatsmyvertical.com/standing-reach/
