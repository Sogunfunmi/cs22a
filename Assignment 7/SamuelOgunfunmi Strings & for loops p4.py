#Assignment 7.py problem 4
#Author: Samuel Ogunfunmi
#Date last modified: 10/12/20
#Purpose:
"""
Using string multiplication and a while loop draw a pyramid in Python.
Prompt the user for a character and use that character to draw a
5 story pyramid 
"""

def main():
    
    char = str(input("Enter a character for a pyramid:"))

    row = 0
    while(row < 5): #Continues until row is == 5
        row += 1
        spaces = 5 - row
        
        counter = 0  #Counts # of times loop runs
        while(counter < spaces):
            print(" ", end='')
            counter += 1

        characters = 2 * row-1
        while(characters > 0):
            print(char, end='')
            characters -= 1
        print()
        
main()


