#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 10, Question 3
#
# Stock trend analysis: determine longest Up period, and longest Down period.
# Display longest trends with dates and price ranges.
#

import pandas_datareader.data as web

DataSource = 'google'

#
"""
getStockData(): ask user for Stock Ticker, get data, return DataFrame 
"""
#
def getStockData():
    symbol = input("Please enter Stock Ticker Symbol: ")
    symbol = symbol.upper()
    startDate = input("Please enter Start Date (mm/dd/yyyy): ")
    endDate = input("Please enter End Date (mm/dd/yyyy): ")
    d = web.DataReader(symbol, DataSource, startDate, endDate)
    return d

#
""" up(a, b): comparison used to determine if the trend is Up """
#
def up(a, b):
    if (a >= b):
        return False
    else:
        return True

#
""" down(a, b): comparison used to determine if the trend is Down """
#
def down(a, b):
    return not up(a, b)

#
""" longer(l1, l2): return the longer of two lists (preserves the former should the lengths be the same) """
#
def longer(l1, l2):
    if len(l1) >= len(l2):
        return l1
    else:
        return l2

#
"""
trend(d, f): determine the longest trend in the stock data set
    Parameters:
        d = DataFrame with stock data
        f = evaluation function which compares two values
    Returns:
        the longest trend, expressed as: start date, end date, starting price, ending price
"""
#
def trend(d, f):
    cp = d["Close"]
    # a list to hold the longest trend
    longest = []
    # a list to hold each running trend
    running = []
    for i in range(1,len(cp)):
        a, b = cp[i-1], cp[i]
        # compare a and b with provided comparison function
        # if the comparison returns True, then append to the running trend list
        if f(a, b):
            # date, date, price, price
            running.append((d.index[i],b))
        else:
            # the comparison returned False, so there is no trend..
            # set the longest trend to the longer of the existing longest or the running trend
            longest = longer(longest, running)
            # and erase the running trend
            running = []
    # final check for which is the longer trend: the longest, or the running
    longest = longer(longest, running)
    startDate = longest[0][0].date()
    startPrice = longest[0][1]
    endDate = longest[len(longest)-1][0].date()
    endPrice = longest[len(longest)-1][1]
    return startDate, endDate, startPrice, endPrice, len(longest)

#
""" days(startDate, endDate): return the number of days elapsed between start and end date"""
#
def days(startDate, endDate):
    return (endDate-startDate).days
    
def main():
    d = getStockData()
    print("Trend\tStart Date\tEnd Date\tConsecutive\tCalendar Days\tStart Price\tEnd Price")
    startDate, endDate, startPrice, endPrice, duration = trend(d, up)
    print("{0}\t{1}\t{2}\t{3}\t\t{4}\t\t${5:.2f}\t\t${6:.2f}".format("Up", startDate, endDate, duration, days(startDate, endDate), startPrice, endPrice))
    startDate, endDate, startPrice, endPrice, duration = trend(d, down)
    print("{0}\t{1}\t{2}\t{3}\t\t{4}\t\t${5:.2f}\t\t${6:.2f}".format("Down", startDate, endDate, duration, days(startDate, endDate), startPrice, endPrice))

if __name__ == '__main__':
    main()
