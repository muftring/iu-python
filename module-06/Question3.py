#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 6, Question 3
#
# Ask user to enter a date in `Month Day, Year` format.
# Verify that the month is valid, and that the day is valid within the specified month.
# Check that the year is within the bounds of 1 to 2017, and also check if it is a Leap Year.
# Display findings to user.
#

#
""" isLeapYear(year): returns True or False depending on whether `year` is a Leap Year """
#
def isLeapYear(year):
    # a century evenly divisible by 400 -> True
    if (year % 100 == 0) and (year % 400 == 0):
        return True
    # a century otherwise -> False 
    elif (year % 100 == 0):
        return False
    # a year evenly divisble by 4 -> True
    elif (year % 4 == 0):
        return True
    # else -> False
    else:
        return False

#
""" isMonth(month): chacks whether `month` is a valid month name (in English) """
#
# uses try-except
def isMonth(month):
    months = ["January", "February", "March", \
              "April", "May", "June", \
              "July", "August", "September", \
              "October", "November", "December"]
    try:
        months.index(month)
        return True
    except:
        return False

#
""" isDay(month, day): returns True or False if `day` is valid for `month` (assumes `month` itself is valid) """
#
# implemented in Decision Tree fashion
def isDay(month, day):
    # anything outside the range of 1-31 is invalid
    if day < 1 or day > 31:
        return False
    # February can have 28 or 29 (in a Leap Year)
    if month == "February":
        if day <= 29:
            return True
        else:
            return False
    # 30 days hath...
    if month == "April" or month == "June" or month == "September" or month == "November":
        if day <= 30:
            return True
        else:
            return False
    # all the rest have 31...
    return True

#
""" inDate(): prompts user to enter date in `Month Day, Year` format; returns a List [month, day, year] """
#
def inDate():
    date = input("Enter a date in Month Day, Year format (ex: January 1, 2000): ")
    date, year = date.split(",")
    month, day = date.split()
    return [month, int(day), int(year)]

#
# test functions used during development of each required function.
# Used to verify that functions were implemented correctly
#
def test1():
    year = eval(input("Enter year: "))
    print(year,"is a Leap Year?", isLeapYear(year))

def test2():
    month = input("Enter a month name: ")
    print(month,"is a valid month?", isMonth(month))

def test3():
    date = input("Enter month name and day number (ex: January 1): ")
    month,day = date.split()
    print(month,day,"is valid?",isDay(month,int(day)))

def test4():
    date = inDate()
    print(date)
    
def Main():
    yearLowerBound = 1
    yearUpperBound = 2017
    
    # values used to index the List returned from inDate()
    month, day, year = 0, 1, 2
    
    # get user input
    date = inDate()
    if not isMonth(date[month]):
        print(date[month], "is not a valid month")
        return
    if not isDay(date[month], date[day]):
        print(date[day],"is not a valid day in the month of",date[month])
        return
    if date[year] < yearLowerBound or date[year] > yearUpperBound:
        print("The year", date[year], "is outside the bounds of",yearLowerBound,"to",yearUpperBound)
        return
    if not isLeapYear(date[year]):
        print(date[year],"is not a Leap Year")
        return
    print("{} {}, {} is a valid date in a Leap Year!".format(date[month], date[day], date[year]))

# for assignment submission main() calls Main()
# during development and testing, main() called one of the test() functions
def main():
    Main()

if __name__ == '__main__':
     main()
