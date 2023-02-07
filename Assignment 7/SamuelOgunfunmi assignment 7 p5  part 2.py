#Assignment 7.py problem 6 
#Author: Samuel Ogunfunmi
#Date last modified: 10/9/20
#Purpose:
"""
#WGiven the string "Midterm Exam is almost here"

1. Iterate over the string using a for-each loop and print each element of the string
on one line.

2. Iterate over the string using a  for-each loop and print each element of the string
separated by commas on one line. Remove the blank spaces in the string first.

3. Iterate over the sequence using a range-based for loop,  and for each index access
the character from string using operator. Print each index position and the
corresponding character in the string .

4. Iterate over a portion of string, the slice "Exam" using a for loop.
Print the slice on one line.
"""

def main():
    
    phrase = "Midterm Exam is almost here"
    comma = ","
    print("1. Traverse/iterate over string using standard for loop:")
    for statement in phrase: 
        print(statement, end=" ")

    print("\n")
    print("2. Spaces removed from the string:")
    print(phrase.replace(" ","")) #Replaces the spaces with no space
    print(comma.join(phrase)) #inserts a comma inbetween each character
    print("\n")
    print("3. Index Position and the Corresponding Character")

    phrase2 = "CIS 122 Exam 1 is almost here"
    count = 0
    while (count < len(phrase2)): 
        letter = phrase2[count]
        print("Index:", count ,"Element:", phrase2[count]) #prints the index # and the character on new lines 
                                                           #until there are no more characters to print
        
        count +=1
        
    print("\n")
    print("4. Iterate over a sub-string/slice using standard for loop:")
    for statement in phrase:
        print(phrase[ 8:12]) #prints characters 8 through 12 in the string phrase "Exam"
        break
main()


