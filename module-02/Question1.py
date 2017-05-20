# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 2, Question 1
#
# A program to produce a table of Celsius to Fahrenheit conversions
# every 10 degrees from 0C to 100C.
# 

def main():
    print("Celsius\tFahrenheit")
    print("------------------")
    for i in range(11):
        celsius = i*10
        fahrenheit = (9/5) * celsius + 32
        print(celsius,"\t",fahrenheit)
    
main()
