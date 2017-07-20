#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:31:02 2017

@author: uftringfamily
"""

import time
from graphics import GraphWin, Point, Circle, Text

def pause(seconds):
    time.sleep(seconds)

def main():
    # create the window
    win = GraphWin("Cllick Me!")
    # create a point and draw it in the window
    p1 = Point(50, 60)
    p1.draw(win)
    # and another point..
    p2 = Point(80, 80)
    p2.draw(win)
    # then a circle, which has a center point
    center = Point(60, 120)
    c1 = Circle(center, 30)
    c1.setFill('blue')
    c1.draw(win)
    # clone the circle and move it some
    c2=c1.clone()
    c2.move(100, -50)
    c2.draw(win)
    # add some text labels
    label1 = Text(Point(50, 100), "c1") 
    label1.draw(win)
    label2 = Text(Point(150, 50), "c2") 
    label2.draw(win)
    # wait for user to click in the window
    click = win.getMouse()
    print("You clicked", click.getX(), click.getY())
    # close the window
    win.close()
    return 0

if __name__ == '__main__':
    main()
