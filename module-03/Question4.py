#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 3, Question 4
#
# Compute and print Fibonacci numbers.
# 

def fibonacci(n):
    prev = 1
    curr = 1
    for i in range(n-1):
        prev, curr = curr, prev + curr
    return prev

def main():
    print("Fibonacci calculator!")
    n = eval(input("Enter a number: "))
    print("Fibonacci number",n ,"is", fibonacci(n))
    
main()
