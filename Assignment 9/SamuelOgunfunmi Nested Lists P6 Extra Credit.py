#Assignment 9.py Problem 6 Extra Credit
#Author: Samuel Ogunfunmi
#Date last modified: 11/3/20
#Purpose: 

def Palindromes(List2):
    Palwords = [] #new list for palindromes

    for w in List2:
            if w == w[-1::-1]: #if a palindrome add to new list
                Palwords.append(w)
    return Palwords

def main():
 
    List2 = ['racecar', 'Python', 'mom', 'java','level', 'DNA','101101' ]  
    print("The words that are Palindromes are", Palindromes(List2))#calls Palindrome function using List2
    
main()
