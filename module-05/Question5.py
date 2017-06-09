#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 5, Question 5
#
# Count and display the number of digits in each line of an input file.
# Digits are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#

#
""" countDigits(line): count the number of digits in line, return result"""
#
def countDigits(line):
    count = 0
    for i in range(len(line)):
        if line[i].isdigit():
            count += 1
    return count

def main():
    fileName = input("Enter the name of input text file: ")
    inputFile = open(fileName, "r")
    lineCount = 0
    for line in inputFile.readlines():
        lineCount += 1
        count = countDigits(line)
        print("There are {} digits in line {}".format(count, lineCount))
    inputFile.close()

main()
