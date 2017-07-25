#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:25:41 2017

@author: uftringfamily
"""

class Foo:
    def m1(self):
        print("m1")
    def m2(self):
        self.m1()

def main():
    f = Foo()
    f.m2()

if __name__ == '__main__':
    main()
