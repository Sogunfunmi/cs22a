#Assignment 5.py problem 2
#Author: Samuel Ogunfunmi
#Date last modified: 9/26/20
#Purpose: Write a program that converts Celsius temperatures to Fahrenheit temperatures and vice versa.
def C_to_F():

    Celsius = input("What is the temperature in Celsius? ")#Input from the user
    C = float(Celsius) #makes input a float
    
    Fahrenheit = ((C * 9/5) +32)#Converts C to F

    print ("This temperature in Fahrenheit is ", Fahrenheit, " degrees") #Prints converted temperature
    
def F_to_C():

    Fahrenheit = input("What is the temperature in Fahrenheit? ")#Input from the user
    F = float(Fahrenheit)
    
    Celsius = ((F-32) * 5/9) #Converts F to C

    print ("This temperature in Celsius is ", Celsius, " degrees") #Prints converted temperature

def main():
    print("1. Celsius to Fahrenheit")   #option 1
    print("2. Fahrenheit to Celsius")   #option 2
    option = int(input("Select which number conversion you would like to run: ")) #ask user to select an option

    if option == 1: #if user selects option 1 run the Cel to Fah conversion 
        C_to_F()

    if option == 2: #if user selects option 2 run the Fah to Cel conversion 
        F_to_C()    
      
main()
