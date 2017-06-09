#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:33:49 2017

@author: uftringfamily
"""

def printReverse(l):
    if len(l) > 1:
        printReverse(l[1:])
    print(l[0])

l = [1, 2, 3]
printReverse(l)
