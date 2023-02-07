#Assignment 4.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 9/20/20
#Purpose: Demonstration defining custom/programmer-defined function, function call, and return.

#Define an average function that takes 4
#arguments, calculates the average of the
#4 numbers passed to it, and  returns the
#result back to the caller.

#Capture the 4 values from the user in main()  and pass them to the function average.
#Call  the average function from main. Print the results returned in the main function.

def average(num1,num2,num3,num4): #fucntion made to find the average of 4 numbers
    return (num1+num2+num3+num4)/4 #Returns result of 4 inputs averaged to main
 
def main():

    print("---Group 1---")
    num1 = float(input("First number: "))   #asks user for number
    num2 = float(input("Second number: "))  #asks user for number
    num3 = float(input("Third number: "))   #asks user for number
    num4 = float(input("Fourth number: "))  #asks user for number
    average_1 = average(num1,num2,num3,num4) #Takes 4 inputs and finds the average using the average function
                                             #Result is returned here and saved as average_1
                        
    print("---Group 2---")
    num1 = float(input("First number: "))  #asks user for number
    num2 = float(input("Second number: ")) #asks user for number
    num3 = float(input("Third number: "))  #asks user for number
    num4 = float(input("Fourth number: ")) #asks user for number
    average_2 = average(num1,num2,num3,num4)#Takes 4 inputs and finds the average using the average function
                                            #Result is returned here and saved as average_1

    print("---Group 3---")
    num1 = float(input("First number: "))   #asks user for number
    num2 = float(input("Second number: "))  #asks user for number
    num3 = float(input("Third number: "))   #asks user for number
    num4 = float(input("Fourth number: "))  #asks user for number
    average_3 = average(num1,num2,num3,num4)#Takes 4 inputs and finds the average using the average function
                                            #Result is returned here and saved as average_1

    print("---Group 4---")
    num1 = float(input("First number: "))   #asks user for number
    num2 = float(input("Second number: "))  #asks user for number
    num3 = float(input("Third number: "))   #asks user for number
    num4 = float(input("Fourth number: "))  #asks user for number
    average_4 = average(num1,num2,num3,num4)#Takes 4 inputs and finds the average using the average function
                                            #Result is returned here and saved as average_1

    avg = average(average_1,average_2,average_3,average_4) #Finds the average of 4 averages
    
    print("Group 1 Average:", average_1) #prints average 1
    print("Group 2 Average:", average_2) #prints average 2
    print("Group 3 Average:", average_3) #prints average 3
    print("Group 4 Average:", average_4) #prints average 4
    print("Total Average:", avg)         #prints average of averages


main()
