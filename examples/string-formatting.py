#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:16:07 2017

@author: sherpa
"""

def compare(n, c):
    if (n < c):
        comp = "less than"
    elif (n == c):
        comp = "equal to"
    else:
        comp = "greater than"
    print("Comparing {0} with {1}, {0} is {2} {1}".format(n, c, comp))

def main():
    a, b = eval(input("Enter two numbers: "))
    compare(a, b)

main()
