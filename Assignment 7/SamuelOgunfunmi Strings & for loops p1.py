#Assignment 7.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 10/9/20
#Purpose:
"""
What is the value returned by each index position?
"""
def main():

    phrase = "Hello world!"

    print("What is the value returned by index position 0?")
    print(phrase[0])
    
    print("What is the value returned by index position 1?")
    print(phrase[1])
    
    print("What is the value returned by index position -1?")
    print(phrase[-1])

    print("What is the value returned by index position -2?")
    print(phrase[-2])

    print("What is the value returned by index position 15?")
    print(phrase[15]) #IndexError: String index out of range
    
    
main()


