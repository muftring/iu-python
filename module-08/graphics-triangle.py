#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:13:35 2017

@author: uftringfamily
"""

# triangle.py
# Interactive graphics program to draw a triangle

from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    message = Text(Point(100, 20), "Click on three points") 
    message.draw(win)
    # Get and draw three vertices of triangle 
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1,p2,p3) 
    triangle.setFill("yellow") 
    triangle.setOutline("black") 
    triangle.draw(win)
    # and wrap up
    message.setText("Click anywhere to quit.") 
    win.getMouse()
    win.close()
    
main()
