#Assignment 9.py problem 3
#Author: Samuel Ogunfunmi
#Date last modified: 11/3/20
#Purpose: Write a program that calls a function to filter out the elements with values less than 7 and return a sublist. 

def main():

    Matrix_1 = [[1, 1, 1, 1],[2, 5, 2, 5],[3, 3, 3, 3],[4, 7, 4, 7]]
    Matrix_2 = [[1, 1, 1, 1],[2, 2, 2, 2],[3, 3, 3, 3],[4, 4, 4, 4]]
    
    for i in range(len(Matrix_1)):#will loop to the length of matrix_1
        M1 = Matrix_1[i]
        M2 = Matrix_2[i]
        for x in range(len(M1)):
            if M1[x] == M2[x]:
                print("Matrix_1 element", M1[x], "is equal to Matrix_2 element", M2[x],"\n")
            else:
                print("Matrix_1 element", M1[x], "is not equal to Matrix_2 element", M2[x],"\n")
     
main()

