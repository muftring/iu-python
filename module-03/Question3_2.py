#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 3, Question 3.2
#
# Calculate and display the number of combinations of `n` objects taken `r` at a time.
# 

def factorial(n):
    f = 1
    for i in range(1, n+1, 1): 
        f *= i
    return f

def main():
    print("Combinations calculator!")
    n = eval(input("How many items? "))
    r = eval(input("How many at a time? "))
    if n > r:
        p = factorial(n) / (factorial(n - r) * factorial(r))
        print("The number of combinations for",n,"objects taken",r,"at at time is",p)
    else:
        print("Error - the number of items (",n,") must be greater than the take (",r,").")

main()
