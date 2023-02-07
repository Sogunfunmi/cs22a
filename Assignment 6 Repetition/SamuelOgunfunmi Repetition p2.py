#Assignment 6.py problem 2
#Author: Samuel Ogunfunmi
#Date last modified: 10/5/20
#Purpose:
"""
Write a sentinel-based while loop that calculates the average weight of a doctor's patients.
Your program should include a priming read for the first weight.
The while loop must keep track of the number of patient weights entered.
Average should be displayed when the sentinel is entered.
Trace the program using a state table showing the state changes for all the variables and the output.
"""

def calcAverage(tot,count): #fucntion made to find the average of the inputs
    avg = tot / count
    return avg #Returns result of the inputs averaged to main


def main():
    tot = 0.0 #running total
    count = 0 #running count
    
    x = float(input("Enter patient weight: ")) #Ask user for test score Prime reading
    while x >= 0:         #Determine if input is a positive number
        tot = tot + x     #Adds new input to running total
        count = count + 1 #Keeps track of the number of times loop is run
        x = float(input("Enter patient weight(negative number to quit): ")) 

    avg = calcAverage(tot,count)  #Returning 
    print("\nThe average patient weight is ", avg)
    
main()


