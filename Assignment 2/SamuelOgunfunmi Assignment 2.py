#Assignment 2
#Author:Samuel Ogunfunmi
#Date last modified: 09/07/20
# Purpose:  Use variables abstraction to make your programs more general purpose

#---------------------------------------------------------------------------------------------
#PROBLEM 1
#Write a step-by-step algorithm to calculate the average of 3 numbers: (9, 7, and 15)

"""
def main():     #include this line in every program
    int_1 = 9 #Hard code the first integer
    int_2 = 7 #Hard code the second integer.
    int_3 = 15 #Hard code the third integer
    int_sum = int_1 + int_2 + int_3 #Create Variables for sum of numbers

    Average = (int_sum / 3) #Average formula

    print("The average is ", Average) #Display the average to the user. 

main()          #Call to main() is also required at the end of every program
"""
#---------------------------------------------------------------------------------------------
#PROBLEM 2

#Write a program that asks the user their name and greets the user using the name they entered.
#Then the program prompt the user for hours they worked and rate per hour to compute gross pay

'''
def main():     #include this line in every program
    
    name = input("What's your name? ")#Asks user for name
    
    print ("Hello ", name)#Greeting
    hours = input ("Enter Hours: ")#Ask for hours worked
    h = float(hours)
    rate = input ("Enter Rate: ")#Ask for rate
    r = float(rate)

    
    grosspay = h * r #Calculate total gross pay
    print ("Pay: ", grosspay) #Display gross pay total
    
main()
'''
#---------------------------------------------------------------------------------------------
#PROBLEM 3

#Write a program that asks the user their name and greets the user using the name they entered.
#Then the program prompt the user for hours they worked and rate per hour to compute gross pay
'''

def main(): #include this line in every program
    
    Celsius = input("What is the temperature in Celsius? ")#Input from the user
    C = float(Celsius)
    
    Fahrenheit = ((C * 9/5) +32)#Converts C to F

    print ("This temperature in Fahrenheit is ", Fahrenheit, " degrees") #Prints converted temperature

main()
'''
