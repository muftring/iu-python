#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 5, Question 4
#
# Compute and display the sum of squares of the numbers on each line read in from a file.

#
""" squareEach(nums): square each numeric value in the provided list, place result in the provided list """
#
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

#
""" sumList(nums): sum the numbers in the list, return the result """
#
def sumList(nums):
    result = 0
    for i in nums:
        result += i
    return result

#
""" toNumbers(strList): modify a list of strings to become a list of numbers """
#    
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

#
""" stringToList(str): convert a string to a list, using default string.split() delimeter """
#
def stringToList(str):
    strList = []
    for s in str.split():
        strList.append(s)
    return strList

def main():
    fileName = input("Enter the name of file with numbers: ")
    inputFile = open(fileName, "r")
    lineNumber = 0
    for inputLine in inputFile.readlines():
        lineNumber += 1
        strList = stringToList(inputLine)
        numList = strList[:]
        toNumbers(numList)
        squareList = numList[:]
        squareEach(squareList)
        sumOfSquares = sumList(squareList)
        print("Sum of squares in line {} is {}".format(lineNumber, sumOfSquares))
    inputFile.close()
    
main()
