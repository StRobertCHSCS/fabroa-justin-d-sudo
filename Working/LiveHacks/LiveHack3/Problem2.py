'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	How many days does it take to pass 100km

Author:		Lau.J

Created:	09/12/2019
------------------------------------------------------------------------------
'''

# initialize total
number_days = 0
distance = 0
average = 0

# loop to get use daily distances
while distance != 100:
    distance = int(input("Enter the distance travelled for the day (100 to stop): "))
    number_days = number_days + 1
    average = distance/number_days

#output totals
print("***** Welcome to the Distance Tracker *****")
print("It took " +str(number_days), "days")
print("The average distance travelled is " +str(average))


