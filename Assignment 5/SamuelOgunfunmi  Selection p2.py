#Assignment 5.py problem 2
#Author: Samuel Ogunfunmi
#Date last modified: 9/26/20
#Purpose: Write a grade conversion program that takes a numeric grade
       #(type float) input from the user and converts it to a letter grade (A-F), 

def main():
    
    A_grade = 90
    B_grade = 80
    C_grade = 70
    D_grade = 60

test_score = float(input("Enter your test score: ")) # Ask user for test score 
 
# Determine the grade.
if test_score >= 90:
    print("Your grade is A.")
elif test_score >= 80:
    print("Your grade is B.")
elif test_score >= 70:
    print("Your grade is C.")
elif test_score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
    
main()
