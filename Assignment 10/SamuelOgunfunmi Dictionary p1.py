#Assignment 10.py problem 1
#Author: Samuel Ogunfunmi
#Date last modified: 11/10/20
#Purpose:

def scrabble(word):
    total = 0
    word = word.upper() #makes input upper case to match dictionary
    score = {'A': 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1,
             "S": 1, "T": 1, "U": 1, "D": 2, "G": 2,"B": 3, "C": 3,
             "M": 3, "P": 3,"F": 4, "H": 4,"V": 4, "W": 4, "Y": 4,
             "K": 5,"J": 8, "X": 8, "Q": 10, "Z": 10}

    for i in word:
        score[i]
        total += score[i]
    return total
        
def main():
    
    word = input("Enter a word:")
    scrabblescore = scrabble(word)
    print("The score is: ",scrabble(word))
  
main()

