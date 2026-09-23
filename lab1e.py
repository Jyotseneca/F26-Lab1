
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Tamanjyot Singh Sehgal
# Date:22/09/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module 
#% formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make
# sure the answer only goes to hundreadths (-.--) using the module % formatting.
quantity=3.5
stock=7.95
product=quantity*stock
print("the product is    %f" %product)
print("the product is       %.2f" %product)
#so in this section we have seen that, how we can multiply the float values, and later
#store them in some other variable. then, i used % formatting which was used to control
#the spacing and later, also showed how to show the number in two decimal places. 
