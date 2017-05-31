#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 4, Question 1
#
# Write a program that takes an input string from the user and prints 
# the string in a reverse order.
#

def main():
    forward = input("Please enter a string: ")
    reverse = ""
    for i in range(1, len(forward)+1, 1):
        reverse += forward[-1*i]
    print("You typed a string:", forward)
    print("The string in reverse order is:", reverse)
    
main()
