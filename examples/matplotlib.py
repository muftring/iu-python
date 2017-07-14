#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:35:39 2017

@author: uftringfamily
"""

import matplotlib.pyplot as plt

# create a new figure
fig1 = plt.figure()

# create a sub-plot, add it to the figure
# Note: the figure will have 2x3 sub-plots
rows = 2
cols = 3
subplotId = 1
sp1 = fig1.add_subplot(rows, cols, subplotId)

# and add two more..
sp2 = fig1.add_subplot(2, 3, 2)
sp3 = fig1.add_subplot(2, 3, 3)
