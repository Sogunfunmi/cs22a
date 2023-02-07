#Assignment 6.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 10/4/20
#Purpose: Write a program that calls a function to decide whether the average is a passing grade

def calcAverage(tot,count): #fucntion made to find the average of 3 numbers
    avg = tot / count
    return avg #Returns result of 3 inputs averaged to main

def main():
    tot = 0.0
    count = 0
    #Priming Read
    x = float(input("Enter a test score: ")) #ask user for input
    while x >= 0:          #Determines if user input is a positive or negative number
        tot = tot + x      #adds to running total
        count = count + 1  #Adds to counter
        x = float(input("Enter another test score (negative to quit): "))

    avg = calcAverage(tot,count)                #call variable from calcAverage function 
    print("\nThe tests score average is", avg)  #Tells the user their test score average

    if avg >= 70:           #Determines if the user test score average
                            #results in a passing or failing grade
        print("You have a passing grade.")
    else:
        print("You do not have a passing grade.") 
main()


