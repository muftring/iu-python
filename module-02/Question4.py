#!/usr/bin/env python
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 2, Question 4
#
# From a U.S. fuel economy (miles/gallon) value, compute and display 
# the European fuel consumption (L/100km).

kmPerMile = 1.6
litersPerGallon = 3.785

def fuelEff():
    milesPerGallon = eval(input("Please enter mileage (miles per gallon): "))
    litersPer100Km = 1 / ((milesPerGallon * kmPerMile) * (1 / litersPerGallon)) * 100
    print("Vehicle consumption is",milesPerGallon,"miles per gallon.")
    print("Vehicle economy is ",litersPer100Km,"liters per 100 km.")

def main():
    fuelEff()

main()
