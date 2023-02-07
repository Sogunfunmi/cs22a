#Assignment 10.py problem 5
#Author: Samuel Ogunfunmi
#Date last modified: 11/9/20
#Purpose:

def phrasecounter(string):
    a = {}
    for i in string:
        a[i] = a.get(i, 0) +1
    return a
        
def main():
    string = input("Enter a phrase:")
    phrasecounter(string)
    print(phrasecounter(string))
    
main()

