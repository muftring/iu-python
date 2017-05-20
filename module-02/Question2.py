# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 2, Question 2
#
# An interactive Python mathematical expression calculator.
#

def calculate(nbTimes):
    for n in range(nbTimes):
        expr = input("Please enter a mathematical expresion: ")
        print(expr,"=",eval(expr))

def main():
    print("Welcome to an Interactive Python Calculator")
    nbTimes = int(input("How many calculations would you like to execute? "))
    calculate(nbTimes)

main()
