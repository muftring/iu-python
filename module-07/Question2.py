#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 7, Question 2
#
# A program which promts the user for a list of numbers, then determines if
# the list is ordered (ascending or descending) and displays the result.
#

import math

#
""" isAscend(nums): check whether numbers in a list are sorted in ascending order, returns True/False """
#
def isAscend(nums):
    result = True
    prev = -1 * math.inf
    for curr in nums:
        if curr >= prev:
            prev = curr
        else:
            result = False
            break
    return result

#
""" isDescend(nums): check whether numbers in a list are sorted in descending order, returns True/False """
#
def isDescend(nums):
    result = True
    prev = math.inf
    for curr in nums:
        if curr <= prev:
            prev = curr
        else:
            result = False
            break
    return result

#
""" getNumbers(): prompt user to enter a list of numbers (separated by spaces), returns a list"""
#
def getNumbers():
    nums = []
    values = input("Enter numbers separated by a space: ")
    for value in values.split():
        number = int(value)
        nums.append(number)
    return nums

def main():
    nums = getNumbers()
    if isAscend(nums): 
        print("The numbers are in ascending order.")
    elif isDescend(nums): 
        print("The numbers are in descending order.")
    else:
        print("The numbers are not sorted.")

if __name__ == '__main__':
     main()
