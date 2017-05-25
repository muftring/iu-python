#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 3, Question 2.2
#
# Given the length of two sides of a right triangle: the hypotenuse, and adjacent;
# compute and display the angle between them.
# 

import math

def main():
    print("Angle between hypotenuse and adjacent side computer!")
    b = eval(input("Enter the length of the adjacent side: "))
    c = eval(input("Enter the length of the hypotenuse: "))
    radians = math.acos(b/c)
    degrees = radians * 180 / math.pi
    print("The angle in radians is", radians)
    print("The angle in degrees is", degrees)
    
main()
