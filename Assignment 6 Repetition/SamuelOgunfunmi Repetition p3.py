#Assignment 6.py problem 3
#Author: Samuel Ogunfunmi
#Date last modified: 10/5/20
#Purpose: Write a while loop that validates user input.

def main():
    count = 0 #running count
    loop = True #Boolean variable

    print("This program validates inputs from 0 to 100\n") #Introduces program to user

    #Prime reading
    x = float(input("Enter a number (negative number to end program)\n Number: ")) #Ask user to enter a number
    
    while (loop):
        count = count + 1 #Keeps track of the number of times loop is run

        if x >=0 and x <= 100:  #Determines if input is in range
            print("This number is in range\n")
        if x > 100:             #Determines what is too high of a number
            print("ERROR! Number is too high. Try again.\n ") 
        if x < 0:               #Identifies negative numbers and ends the loop
            loop = False  #ends the loop(break)
        else:
            x = float(input("Enter a number from 0 to 100(negative number to end program)\n Number: "))#Ask user to enter a number

    print("\nThe End")

main()


