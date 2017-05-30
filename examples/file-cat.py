#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:39:16 2017

@author: sherpa
"""

def fileOpenClose(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    for line in lines:
        print(line[:-1])
    file.close()

def main():
    fileName = input("Enter file name: ")
    fileOpenClose(fileName)

main()
