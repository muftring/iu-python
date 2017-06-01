#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 4, Question 5
#
# Count and print the number of words in a file.
#

def main():
    print("File word counter!")
    wordCount = 0
    fileName = input("Please enter a file name: ")
    inputFile = open(fileName, "r")
    for line in inputFile.readlines():
        words = line.split()
        wordCount += len(words)
    inputFile.close()
    result = "There are {0} words in the file.".format(wordCount)
    print(result)

main()
