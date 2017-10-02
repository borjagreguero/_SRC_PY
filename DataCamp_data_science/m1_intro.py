# -*- coding: utf-8 -*-
"""
# DATACAMP / PYTHON INTRODUCTION 
"""

# # Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print(100*1.1**7)

# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.1

# Calculate result
result = savings*factor**7

# Print out result
print(result)

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True 

type(profitable)
type(desc)


# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

# LISTS 
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Adapt list areas
areas = ["hallway",hall,"kitchen", kit, "living room", liv, "bedroom",bed, "bathroom", bath]

# Print areas
print(areas)

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv], 
         ["bedroom",bed],
         ["bathroom",bath]
         ]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Print out second element from areas
print(areas[1])
# Print out last element from areas
print(areas[-1])
# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Alternative slicing to create downstairs
downstairs = areas[:6]
# Alternative slicing to create upstairs
upstairs = areas[6:]

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]

# LIST MANIPULATION 
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse",24.5]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage",15.45]

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Same line
#command1; command2

# Separate lines
#command1
#command2

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = list(areas)
areas_copy2 = areas # DIFFERENT 
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)
print(areas_copy)

######### FUNCTIONS 
help(round)
round(1.57,2)
round(1.57,1)
round(1.57)

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)


# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)

# Print out the number of o's in room
print(room.count('o'))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

import scipy 
import numpy 
numpy.array([1,2,3])
import numpy as np 
np.array([1, 2, 3])
from numpy import array 

# Definition of radius
r = 0.43

# Import the math package
import math 
# Calculate C
C = 2*math.pi * r
# Calculate A
A = math.pi * r**2
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians 
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)
# Print out dist
print(dist)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np 
# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))

# height is available as a regular list

# Import numpy
#import numpy as np
# Create a numpy array from height: np_height
np_height = np.array(height)
# Print out np_height
print(np_height)
# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254
# Print np_height_m
print(np_height_m)

# height and weight are available as a regular lists


# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254
# Create array from weight with correct units: np_weight_kg
np_weight = np.array(weight) 
np_weight_kg = np_weight*0.453592
# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m **2
# Print out bmi
print(bmi)

# height and weight are available as a regular lists


# subsetting in numpy 
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]

high = y > 5
y[high]

# height and weight are available as a regular lists

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
# Create the light array
light = np.array(bmi<21)
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


np.array([True, 1, 2]) + np.array([3, 4, False])

x = ["a", "b", "c"]
x[1]
np_x = np.array(x)
np_x[1]

# Import numpy
import numpy as np
# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)
# Print out the weight at index 50
print(np_weight[50])
# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])


# 2D ARRAYS - MULTI DIMS
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)


