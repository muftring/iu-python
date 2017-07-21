#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:17:06 2017

@author: uftringfamily
"""

from graphics import *

# Moves a circle to a point of mouse click 
def main():
    win = GraphWin("Move circle", 300, 200) 
    p = Point(50, 100)
    c1 = Circle(p, 30) 
    c1.setFill('yellow') 
    c1.setOutline('black')
    c1.draw(win)
    for i in range(10):
        pNew = win.getMouse()
        xDelta = pNew.getX() - p.getX() 
        yDelta = pNew.getY() - p.getY() 
        c1.move(xDelta, yDelta)
        p = pNew
    win.close()
    
main()
