#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:26:36 2017

@author: uftringfamily
"""

def main():
    inputFile = open("numbers2.txt","r")
    line = inputFile.readline()
    while line != "":
        list = line.split(",")
        for item in list:
            number = float(item)
            print(number)
        line = inputFile.readline()
    inputFile.close()

if __name__ == '__main__':
    main()
