'''
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose:	Convert farenheit to celsius

Author:		Lau.J

Created:	01/10/2019
------------------------------------------------------------------------------
'''

# get farenheit from user
farenheit = float(input("Enter the farenheit: "))

# compute farenheit to celsius
celsius = (5/9)*(farenheit-32)

# output celsius 
print("The temperature in celsiuis is " + str(celsius)) 