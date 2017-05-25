#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 3, Question 2.1
#
# Given the length of the two short sides of a right triangle,
# compute the length of the longest side (the hypotenuse).
#
# Pythagoras Theorum tells us that given an 'a' and 'b' which are the short sides
# and a 'c' which is the hypotenuse, a^2 + b^2 = c^2 (that is, a squared plus b sqaured
# equals c squared).
# 

import math

def main():
    print("Right Triangle hypotenuse computer!")
    a, b = eval(input("Enter the length of the two short sides of a right triangle (a, b): "))
    c = math.sqrt(a**2 + b**2)
    print("The longest side of a right triangle with short sides of length",a,"and",b,"is",c)

main()
