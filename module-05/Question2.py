#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 5, Question 2
#
# Write a function which squares all values in a provided list.
# The function should place the squared value in the provided list, overwriting 
# the original value (which was squared).
# 

#
""" squareEach(nums): square each integer value in the provided list, place result in the provided list """
#
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def main():
    userInput = input("Please enter numbers separated by spaces: ")
    userList = []
    for i in userInput.split(): 
        userList.append(int(i))
    # copy the user list, because squareEach() will mutate the argument list
    squareList = userList[:]
    squareEach(squareList)
    for i in range(len(userList)):
        print("Number",userList[i],"squared is",squareList[i])
    
main()
