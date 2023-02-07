#Assignment 10.py problem 2
#Author: Samuel Ogunfunmi
#Date last modified: 11/10/20
#Purpose:

def main():
    n = int(input("Enter a number: "))
    a = dict()

    for x in range(1,n+1):
        a[x] = x * x 
    print(a)
main()
