#Assignment 5.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 9/26/20
#Purpose: Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year.
#         The program should then determine whether the month times the day equals the year.
#         If so, it should display a message saying the date is magic.
#         Otherwise, it should display a message saying the date is not magic.


def main():
    
    print("Enter a date using numeric values \nFor example: June 10, 1960 would be written as 06/10/60 \n") #prints instructions
    month = int(input("Month: ")) #ask user for month date year
    date = int(input("Date: ")) #ask user for date
    year = int(input("Year: "))#ask user for year

    magic_number = (month*date)

    if magic_number == year:
        print("This is a magic date")
    else:
        print("This date is not a magic")
main()
