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

def compute(start, end): 
    all = 0
    even = 0
    print("\ni\teven\tall")
    print("---\t----\t---")
    for i in range(start, end+1, 1):
        all += i
        if (i % 2 == 0):
            even += i
        print(i, "\t", even, "\t", all)
    return even/all

def main():
    print("Range sum(even) to sum(all) ratio computer!")
    start = int(input("Enter the start number of range: "))
    end = int(input("Enter the end number of range: "))
    ratio = compute(start, end)
    print("\nThe ratio of the sume of all even numbers to the sum of all numbers is:")
    print(ratio)
    
main()
