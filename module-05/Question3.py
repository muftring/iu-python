#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 5, Question 3
#
# Calculate and display the number of combinations of `n` objects taken `r` at a time.
# (refactor of Assignment 3, Question 3.2)
# (Note: I had already written factorial(n) as a function in the prior assignment)
# 

#
""" factorial(n): compute the factorial of n """
#
def factorial(n):
    f = 1
    for i in range(1, n+1, 1): 
        f *= i
    return f

def main():
    print("Combinations calculator!")
    n = eval(input("Enter a positive integer n: "))
    r = eval(input("Enter a positive integer r: "))
    if (n <= 0) or (r <= 0):
        print("Error! n and r must both be positive integers!")
    else:
        if n < r:
            print("Error! n is less than r!")
        else:
            p = factorial(n) / (factorial(n - r) * factorial(r))
            print("Number of combinations C( {} , {} ) = {}".format(n, r, p))

main()
