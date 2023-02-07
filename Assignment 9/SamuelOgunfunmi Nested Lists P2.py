#Assignment 9.py problem 2
#Author: Samuel Ogunfunmi
#Date last modified: 11/3/20
#Purpose: Write a program that calls a function to filter out the elements with values less than 7 and return a sublist. 

def main():
    
    Main_list = []
    
    for i in range(3): #loop 3 times
        sub_list = [] 
        for j in range(3):
            a = int(input("Enter element:"))
            sub_list.append(a)   #add input into sublist 
        Main_list.append(sub_list)#add sublist into main list

    print("\n")
    print("3x3 list: ") #print main list
    for i in range(3):
        for j in range(3):
            print(Main_list[i][j], end= " ")#print main list in 3x3
        print("\n")
    print("-------------------------")
    print("\n")
    print("Doubled 3x3 list: ")
    for i in range(3):
        Main_list[i][0] = (Main_list[i][0]*2)#doubles the first elements in the firt column
        for j in range(3):
            print(Main_list[i][j], end= " ")#print doubled main list in 3x3
        print("\n")
main()

