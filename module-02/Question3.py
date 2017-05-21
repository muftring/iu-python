#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 2, Question 3
#
# Distance Calculator, kilometers to miles
#

kmPerMile = 0.62

def main():
    km = eval(input("Please enter number of kilometers: "))
    miles = km * kmPerMile
    print(km, "is", miles, "miles")
    
main()
