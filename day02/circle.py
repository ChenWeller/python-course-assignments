# A programm that asks the user for the radius of a circle
# Then it will print the area and the circumference of the circle

radius = input("Please enter the radius of a circle to get the area and circumference: ")

#convert the input to a number using float() to consider for decimal numbers

radius = float(radius) # now the radius var is a number and can be used for calculations

#compute the area and the circumference

import math

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("The area of the circle is:", round(area, 2))
print("The circumference of the circle is:", round(circumference, 2))

print("Thank you for using our circle programm to compute your circle area and circumference")