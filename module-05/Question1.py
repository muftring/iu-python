#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 5, Question 1
#
# Write definitions for two functions:
#   sumN(n) which computes the sum of the first `n` positive integers
#   sumNcubes(n) which computes the sum of the cube of the first `n` positive integers
#
# These functions will be invoked by a main() function, which will ask the
# user to provide the value for `n` and will display the results.
#

#
""" firstN(n): produce a list of the first `n` positive integers """
#
def firstN(n):
    result = []
    for i in range(n):
        result.append(i+1)
    return result

#
""" sumN(n): compute the sum of the first `n` positive integers """
#
def sumN(n):
    result = 0
    for i in firstN(n):
        result += i
    return result

#
""" sumNcubes(n): compute the sum of cubes of the first `n` positive integers """
#
def sumNcubes(n):
    result = 0
    for i in firstN(n):
        result += i**3
    return result

def main():
    n = eval(input("Please enter a positive integer: "))
    if (n > 0):
        print("The sum of the first",n,"positive integers is",sumN(n))
        print("The sum of the cubes of the first",n,"integers is",sumNcubes(n))
    else:
        print("You entered a number which is not a positive integer.")

main()
