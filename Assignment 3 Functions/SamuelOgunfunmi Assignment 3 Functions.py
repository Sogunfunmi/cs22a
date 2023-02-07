#Assignment 3.py
#Author: Samuel Ogunfunmi
#Date last modified: 9/13/20
#Purpose: Demonstration defining custom/programmer-defined function,function call
#Constructs use: def, docstring, function call

def banner():
   
    print(" _   _  _ ") 
    print("| | | ||_|")
    print("| |_| || |")
    print("|  _  || |")
    print("|_| |_||_|")

def greeting(phrase):
    
    print("Hello, how are you ")#greeting
    print(phrase)

def cube(x,y):
    
    int1_cubed = x**3 #cubes x
    int2_cubed = y**3 #cubes y
    cubedtotal = int1_cubed + int2_cubed #adds the cubed values of x and y
    
    print(cubedtotal) #prints the total of x^3 + y^3
    

def main():

    banner() #call function to print banner
    
    name = input("What is your name? ") #asks user to input name
    greeting(name)                      #prints greetings and user name


    int_1 = input("Enter 1st integer: ") #Input for value 1
    x = float(int_1)
    int_2 = input("Enter 2nd integer: ") #Input for value 2
    y = float(int_2)

    cube(x,y) #calls the cube function which prints the cubedtotal


main()
