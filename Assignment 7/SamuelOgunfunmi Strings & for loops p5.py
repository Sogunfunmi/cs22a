#Assignment 7.py problem 3
#Author: Samuel Ogunfunmi
#Date last modified: 10/9/20
#Purpose:
"""
Write a program using selection and repetition to simulate the user login authentication process.
Check the user's password against a pre-set password of your choice,
and grant or deny the user access based on the password entered.
Give the user 3 tries for incorrect password entry.
Test your program with at least 3 datasets.
"""

def main():
    count = 0

    while count < 3:  #While loop that gives users 3 tries
        password = input("Enter password: ")
        if password == "Password":  #Correct password
            print("Access granted")
            count = 3
        else:                       #Incorrect passwords
            print("Access denied.")
            count += 1

    if count == 3 and password != "Password":  #After 3rd try, lock the user out
        print("Too many tries. Account Locked")
  
main()


