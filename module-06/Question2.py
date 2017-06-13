#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 6, Question 2
#
# Compute and display Body Mass Index (BMI), given values for height and weight.
# BMI is computed as body weight divided by height squared. Weight should be in 
# kilograms, and height should be in meters.
#

def inchesToMeters(inches):
    return 0.0254 * inches

def poundsToKilograms(pounds):
    return 0.4536 * pounds

#
""" bodyMassIndex(height, weight): BMI = weight / height squared """
#
def bodyMassIndex(height, weight):
    return weight / (height ** 2)

#
""" healthyRange(bmi): determine whether a BMI value is within what is considered the healthy range """
#
def healthyRange(bmi):
    if bmi > 19.0 and bmi <= 25.0:
        return True
    else:
        return False

#
""" healthy(bmi): given a value for BMI, check if in healty range and return a corresponding textaul answer """
#
def healthy(bmi):
    if healthyRange(bmi):
        return "are"
    else:
        return "are NOT"

def main():
    inches = eval(input("Enter your height in inches: "))
    pounds = eval(input("Enter your weight in pounds: "))
    bmi = bodyMassIndex(inchesToMeters(inches), poundsToKilograms(pounds))
    print("Your BMI is {0:0.2f}, you {1} in the healthy range!".format(bmi, healthy(bmi)))

if __name__ == '__main__':
     main()
