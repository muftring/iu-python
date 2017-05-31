#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 4, Question 2
#
# Write a program that takes an unsigned integer number from the user 
# and prints the number in words.

def main():
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = input("Please enter a number: ")
    print("You typed a number:", number)
    print("The number in words is: ", end = '')
    for i in range(len(number)):
        digit = number[i]
        word = numbers[int(digit)]
        print(word+" ", end='')
    print("\n")
    
main()
