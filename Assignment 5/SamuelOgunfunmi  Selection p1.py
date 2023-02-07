#Assignment 5.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 9/26/20
#Purpose: Determine whether the average of 3 numeric grades entered as floats by the user is a passing grade

def calcAverage(score1,score2,score3): #fucntion made to find the average of 3 numbers
    avg = (score1 + score2 + score3) / 3
    return avg #Returns result of 3 inputs averaged to main

def main():

    print("Enter test scores\n") #Tells user to enter test scores
    score1 = float(input("First score: "))   #asks user for number
    score2 = float(input("Second score: "))  #asks user for number
    score3 = float(input("Third score: "))   #asks user for number
    score_avg = calcAverage(score1,score2,score3)
    
    
    if score_avg >= 70:
        print("Your have a passing grade.")
    else:
        print("Your do not have a passing grade.")

main()
