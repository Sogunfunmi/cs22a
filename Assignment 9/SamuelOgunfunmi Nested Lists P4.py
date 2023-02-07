#Assignment 9.py problem 4
#Author: Samuel Ogunfunmi
#Date last modified: 11/3/20
#Purpose: 

def main():
    MainList = [[1, 1, 1, 1],[2, 2, 2, 2],[3, 3, 3, 3],[4, 4, 4, 4]]
    Intsum = 0 #running total
    count = 0 #counter

    for i in range(4):
        Intsum += MainList[count][count] #adds main elements to total
        count += 1 #adds to counter
    print("The sum of main elements is ", Intsum) #prints total of main elements
main()

