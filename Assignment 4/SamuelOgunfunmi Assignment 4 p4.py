#Assignment 4.py problem 4
#Author: Samuel Ogunfunmi
#Date last modified: 9/20/20
#Purpose: Demonstration defining custom/programmer-defined function,function call
#Constructs use: def, docstring, function call


def calorie_conversion(fat_g,carb_g):
        
    fat_cal = fat_g * 9 #Converts fat grams to calories
    carb_cal = carb_g * 4 #Converts carb grams to calories
    return fat_cal,carb_cal #Returns new calories values to main
 
def main():

    fatgrams = float(input("Fat grams: ")) #Asks user for total fat grams eaten
    carbgrams = float(input("Carbohydrate grams: ")) #Asks user for total carb grams eaten

    fat_calories, carb_calories = calorie_conversion(fatgrams,carbgrams) #Calls function and defines variables for calories

    print("Calories from fat grams:", fat_calories) #Prints fat calories
   
    print("Calories from carbohydrate grams:", carb_calories) #Prints carb calories



main()
