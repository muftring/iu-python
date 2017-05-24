#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 3, Question 1
#
# Given a user-provided inclusive range of integer values,
# calculate and display the ratio of the sum of even numbers to
# the sum of all the numbers in the range.
#
# Notes:
#  (1) there is no protection against division by zero in compute()
#  (2) ranges which include negative numbers will work
# 
def compute(start, end): 
    all = 0
    even = 0
    for i in range(start, end+1, 1):
        all += i
        if (i % 2 == 0):
            even += i
    return even/all

def main():
    print("Range sum(even) to sum(all) ratio computer!")
    start = int(input("Enter the start number of the range: "))
    end = int(input("Enter the end number of the range: "))
    if (start <= end):
        ratio = compute(start, end)
        print("\nThe ratio of the sum of all even numbers to the sum of all numbers in the range", start, "to", end, "is:")
        print(ratio)
    else:
        print("\nError - the range `start` value must be less than or equal to the `end` value")
    
main()
