'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Compute the chicken pieces each student and Mr. Fabroa gets

Author:		Lau.J

Created:	02/10/2019
------------------------------------------------------------------------------
'''

#GET the number of Popeyes chicken pieces and number of students
popeyes_chicken = int(input("Enter the number of chicken pieces: "))
number_of_students = int(input("Enter the number of students: "))

#COMPUTE the number of pieces ofr each student and how much Mr.Fabroa will get
student_pieces = popeyes_chicken//number_of_students
fabroa_pieces = popeyes_chicken%number_of_students

#OUTPUT the pieces of chicken for each student and Mr. Fabroa
print ("Each student will get " + str(student_pieces), "and Mr. Fabroa will get " + str(fabroa_pieces))