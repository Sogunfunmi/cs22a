#Assignment 9.py problem 5
#Author: Samuel Ogunfunmi
#Date last modified: 11/3/20
#Purpose: 

def matrix(x,y):
    
    sign = '$' 
    MainList = [[sign for i in range(x)] for i in range(y)] #Enter sign for every column in each row
    for i in MainList:
       print(i) #prints list

def main():

    row = int(input("How many rows?: ")) #ask user for num rows
    column = int(input("How many columns?: "))#ask user for num columns
    matrix(row,column) #calls matrix function

main()
