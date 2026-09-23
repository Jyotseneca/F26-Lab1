
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Tamanjyot Singh Sehgal
# Date:22/09/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'
import math 
r=input("Enter tehe radius: ")
r=int(r)
area=math.pi*r**2
print("the area of the circle is:",area)