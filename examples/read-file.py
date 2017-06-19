#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:50:05 2017

@author: uftringfamily
"""

import math

def main():
    inputFile = open("numbers.txt","r")
    sum = 0.0
    min = math.inf
    max = -1 * math.inf
    count = 0
    for line in inputFile:
        number = float(line)
        sum += number
        if number > max: max = number
        if number < min: min = number
        count += 1
    print("sum:",sum,"count:",count,"agerage:",sum/count,"min:",min,"max:",max)
    inputFile.close()

if __name__ == '__main__':
    main()
