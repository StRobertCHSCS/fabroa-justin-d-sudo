'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	How many heating days are there

Author:		Lau.J

Created:	09/12/2019
------------------------------------------------------------------------------
'''

# get the n input how many numbers you want
number = int(input("Enter how many numbers you want: "))

# initialize total
total = 0

# output and compute the temperatures for each day
for i in range(number):
    temperature = int(input("Enter the average temperature: "))
    if temperature < 15:
        total = total + 1
        print("****** Heating Days Tracker *****")
        print("There are " +str(total), "heating days")
    else:
        print("There are no heating days")
    


