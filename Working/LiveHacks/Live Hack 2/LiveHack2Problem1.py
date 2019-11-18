'''
-------------------------------------------------------------------------------
Name:		LiveHack2Problem1.py
Purpose:	Determine the BMI of the patient to assess their health

Author:		Lau.J

Created:	18/11/2019
-------------------------------------------------------------------------------1.73
'''

# GET the height and weight
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))

# COMPUTE the BMI(body mass index)
bodymassindex = weight/(height*height)

# OUTPUT the message to determine the health of patient
if bodymassindex > 25:
    print("Your BMI is more than twenty five which means you are overweight.")
elif bodymassindex > 18.5 and bodymassindex < 25.0:
    print("Your BMI is between eighteen and a half and twenty five so you are normal weight.")
else:
    print("Your BMI is less than eighteen and a half which means you are underweight.")
