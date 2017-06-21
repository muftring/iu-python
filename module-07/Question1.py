#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 7, Question 1
#
# A program which asks the user to enter some numbers, and shows the total number
# entered, and the min, max, and count of positive and negative values.
#
# An example of an interactive loop with sentinel.
#

import math

def main():
    count = 0
    min = math.inf
    max = -1 * math.inf
    positive = 0
    negative = 0
    
    value = input("Enter a number: ")
    while value != "":
        number = float(value)
        count += 1
        if number > max: max = number
        if number < min: min = number
        if number >= 0: positive += 1
        if number <  0: negative += 1
        value = input("Enter next number: ")
    if count > 0:
        print("You entered {} numbers.".format(count))
        print("The smallest number is {}".format(min))
        print("The largest number is {}".format(max))
        print("There are {} positive and {} negative numbers.".format(positive, negative))
    else:
        print("No numbers were entered.")

if __name__ == '__main__':
     main()
