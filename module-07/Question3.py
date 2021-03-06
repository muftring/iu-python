#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 7, Question 3
#
# User inputs a matrix, it is transposed, and both are displayed.
#

#
""" inData(m, n): prompts user through entering an m-by-n sized matrix, returns 2-dimensional list (the matrix)"""
#
def inData(m, n):
    mx = []
    for i in range(m):
        row = []
        for j in range(n):
            prompt = "Enter value for row {} column {}: ".format(i,j)
            value = eval(input(prompt))
            row.append(value)
        mx.append(row)
    return mx

#
""" transMx(mx): transposes an m-by-n matrix into an n-by-m matrix, returns 2-dimensional list (the transposed matrix) """
#
def transMx(mx):
    tx = []
    cols = len(mx[0])
    rows = len(mx)
    for c in range(cols):
        row = []
        for r in range(rows):
            row.append(mx[r][c])
        tx.append(row)
    return tx

#
""" printMx(mx): displays a matrix in row-column style, very simple attempt at formatting values to pretty print """
#
def printMx(mx):
    for r in range(len(mx)):
        for c in range(len(mx[0])):
            print("{}\t".format(mx[r][c]), end='')
        print("")
        
def main():
    m = eval(input("Enter the number of rows? "))
    n = eval(input("Enter the number of columns? "))
    mx = inData(m,n)
    print("Original matrix:")
    printMx(mx)
    tx = transMx(mx)
    print("Transposed matrix:")
    printMx(tx)

if __name__ == '__main__':
     main()
