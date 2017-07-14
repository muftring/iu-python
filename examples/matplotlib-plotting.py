#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:40:45 2017

@author: uftringfamily
"""

import matplotlib.pyplot as plt

# create the figure
fig2 = plt.figure()

rows = 3
cols = 2

# add two sub-plots in a 2x2 grid
sp1 = fig2.add_subplot(rows, cols, 1) 
sp2 = fig2.add_subplot(rows, cols, 2)

# and plot some random data
sp1.plot(randn(50))
sp2.hist(randn(50), bins = 20, color = "yellow")

# some non-random data
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y = [ 3, 4, 4, 5, 4, 3, 3, 2, 3, 1]

# plot x versus y with red dashes
sp3 = fig2.add_subplot(rows, cols, 3)
sp3.plot(x, y, linestyle = "--", color = "r")

# same thing again, simplified syntax
sp4 = fig2.add_subplot(rows, cols, 4)
sp4.plot(x, y, "r--")

# again, but with markers to highlight actual data points
sp5 = fig2.add_subplot(rows, cols, 5)
sp5.plot(x, y, linestyle = "--", color = "r", marker = "o")

# finally, plot some random noise with cumsum()
sp6 = fig2.add_subplot(rows, cols, 6)
sp6.plot(randn(1000).cumsum())
