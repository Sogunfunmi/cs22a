#Assignment 4.py problem 3
#Author: Samuel Ogunfunmi
#Date last modified: 9/20/20
#Purpose: Demonstrate defining custom/programmer-defined functions, function calls, and returns.

#def payment():
    

def cost(rep_cost): #Function to calculate min insurance cost
    #rep_cost = 100
    min_insurance = rep_cost * 0.8 #Finds 80% of replacement cost
    #print("Minimum insurance value: ", min_insurance) #prints min insurance value
    return min_insurance
 
def main():

    rep_cost = float(input("Replacement cost: ")) #Asks user for replacement cost
    #cost(rep_cost) #Calls function cost
    minimum = cost(rep_cost)
    print(minimum)
    
main()
