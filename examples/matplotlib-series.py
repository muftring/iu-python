#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:15:53 2017

@author: uftringfamily
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
sp = fig.add_subplot(1, 1, 1)
s = pd.Series(np.random.randn(10).cumsum(), index = np.arange(0, 100, 10)) 
s.plot()
