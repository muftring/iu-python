#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 4, Question 4
#
# Determines if the string is a palindrome, and show an appropriate message.
#

def main():
    forward = input("Enter a string to check: ")
    reverse = ""
    for i in range(1, len(forward)+1, 1):
        reverse += forward[-1*i]
    if (forward == reverse):
        print("The string is a palindrome.")
    else:
        print("he string is not a palindrome.")
    
main ()
