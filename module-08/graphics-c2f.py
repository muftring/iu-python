#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:21:58 2017

@author: uftringfamily
"""

# convert_gui.pyw
# Converts Celsius to Fahrenheit # using graphical interface. 

from graphics import *

def main():
    win = GraphWin("Celsius Converter", 300, 200) 
    win.setBackground('peachpuff')

    # Draw the interface
    Text(Point(120, 50), " Celsius Temperature:").draw(win) 
    Text(Point(120,100), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(230,50), 5) 
    input.setText(" 0.0") 
    input.draw(win)
    output = Text(Point(230,100),"") 
    output.draw(win)
    button = Text(Point(120,150),"Convert it!") 
    button.draw(win)
    Rectangle(Point(80,130), Point(170,170)).draw(win)
    # wait for a mouse click
    win.getMouse()
    # convert input
    celsius = eval(input.getText()) 
    fahrenheit = 9.0/5.0 * celsius + 32
    # display output and change button 
    output.setText(fahrenheit) 
    button.setText("Quit")
    # wait for click and then quit 
    win.getMouse()
    win.close()
    
main()
