#Assignment 4.py problem 2
#Author: Samuel Ogunfunmi
#Date last modified: 9/20/20
#Purpose: Demonstrate defining custom/programmer-defined functions, function calls, and returns.


    #Define a function, access(), that captures two values:
    #user name and password and returns them to the caller.
    #Write a program that calls access() function from main().
    #The function should return both values to the caller.
    #The caller then prints the two values returned from the function access().

def access():
    u = input("Enter username: ") #Ask user to input username   
    p = input("Enter password: ") #Ask user to input password 
    return u, p #Returns inputs to main
 
def main():

    Username, Password = access()
    print("Your usename is:", Username)  #Prints username
    print("Your password is:", Password) #Prints Password
    
main()
