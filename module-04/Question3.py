#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 4, Question 3
#
# Write a program that calculates the numeric value of a single name 
# provided as input. This will be accomplished by summing up the values 
# of the letters of the name where ’a’ is 1, ’b’ is 2, ’c’ is 3 etc., 
# up to ’z’ being 26. 
#

base = ord("a")-1

def main():
    sum = 0
    name = input("Enter any name in lower case: ")
    for letter in name:
        sum += (ord(letter) - base)
    print("The numeric value of entered name is", sum)
    
main()
