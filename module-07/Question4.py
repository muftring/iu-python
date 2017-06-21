#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 7, Question 4
#
# Display the sequence of prime numbers within upper and lower bounds.
#

import math

def isPrime(n):
    if n <= 1: return False
    sqrt = int(math.sqrt(n))
    for i in range(2,sqrt+1,1):
        if n % i == 0: return False
    return True

def printPrime(lowerLimit, upperLimit):
    print("The sequence of prime numbers in the given interval:")
    for n in range(lowerLimit, upperLimit+1, 1):
        if isPrime(n):
            print(n)

def main():
    try:
        lowerLimit = int(input("Enter the lower limit of the range: "))
    except ValueError:
        print("Error - Invalid input: lower limit should be a positive integer")
        return
    if lowerLimit <= 0:
        print("Error - Invalid input: lower limit should be a positive integer")
        return
    try:
        upperLimit = int(input("Enter the upper limit of the range: "))
    except ValueError:
        print("Error - Invalid input: lower limit should be a positive integer")
        return
    if upperLimit <= 0:
        print("Error - Invalid input: upper limit should be a positive integer")
        return
    if upperLimit < lowerLimit:
        print("Error - Invalid input: the upper limit is less than the lower limit")
        return
    printPrime(int(lowerLimit), int(upperLimit))

if __name__ == '__main__':
     main()
