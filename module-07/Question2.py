#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 7, Question 2
#

import math

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
