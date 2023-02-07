#Assignment 9.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 11/3/20
#Purpose: Write a program that calls a function to filter out the elements with values less than 7 and return a sublist. 

def main():
    
    IntList1 = [1,1,1,1]
    IntList2 = [2,2,2,2]
    IntList3 = [3,3,1,1]

    nestedList = [IntList1,IntList2,IntList3] #create nested list
    for i in nestedList: #display the 2d list as rows and col
        print(i)

    #calculate the sum: nested lists and nesting indexing
    total = 0
    for i in nestedList: #nested for-each loop
        for j in i: 
            total += j


    print("The sum of elements is ", total)
            
    
main()

