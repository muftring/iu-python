#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 6, Question 1
#
# Compute and display the letter grade for a given numeric score. 
#

#
""" letterGrade(score): compute and return a letter grade for the given numeric score """
#
def letterGrade(score):
    grade = "?"
    if score >= 93.0:
        grade = "A"
    elif score >= 90.0 and score < 93.0:
        grade = "A-"
    elif score >= 86.0 and score < 90.0:
        grade = "B+"
    elif score >= 83.0 and score < 86.0:
        grade = "B"
    elif score >= 80.0 and score < 83.0:
        grade = "B-"
    elif score >= 76.0 and score < 80.0:
        grade = "C+"
    elif score >= 73.0 and score < 76.0:
        grade = "C"
    elif score >= 70.0 and score < 73.0:
        grade = "C-"
    elif score >= 66.0 and score < 70.0:
        grade = "D+"
    elif score >= 60.0 and score < 66.0:
        grade = "D"
    else:
        grade = "F"
    return grade
    
def main():
    score = float(input("Enter your total score: "))
    if score > 0.0 and score <= 100.0:
        grade = letterGrade(score)
        print("Your letter grade is", grade)
    else:
        print("Error: score must be between 0.0 and 100.0")
    
if __name__ == '__main__':
     main()
