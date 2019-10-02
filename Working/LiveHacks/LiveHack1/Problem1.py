'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	Calculate the degrees farenheit when given the celsius

Author:		Lau.J

Created:	02/10/2019
------------------------------------------------------------------------------
'''

#GET the celsius
celsius = float(input("Enter the degrees celsius: "))

#COMPUTE celsius to farenheit
farenheit = 9/5*celsius + 32

#OUTPUT the degrees farenheit
print ("The temperature in farenheit is " + str(farenheit))