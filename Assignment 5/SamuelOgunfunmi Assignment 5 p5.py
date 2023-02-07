#Assignment 5.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 9/26/20
#Purpose: Write a program that calculates and displays a person’s body mass index (BMI).
#         The BMI is often used to determine whether a person is overweight or underweight
#         for his or her height.
def main():

    weight = float(input("Enter weight in pounds: "))
    height = float(input("Enter height in inches: "))
    
    BMI = weight * 703 /(height ** 2) #Calculates BMI
    print (BMI, "is your BMI")
    
    
    if BMI < 18.5:
            print("You are underweight.")
    elif BMI <= 25:
            print("You are at an optimal weight.")
    else: 
            print("You are overweight.")

    
main()
