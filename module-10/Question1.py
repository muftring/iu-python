#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 10, Question 1
#
# A stock trading simulation. Objective is to figure out the maximum best
# possible return employing a series of buy and sell options automatically.
# The decision to buy or sell is based on Up and Down trend determination
# with a simple threshold on consecutive days within the trend. Buy and Sell
# are executed on the daily Closing Price only.
#

import pandas_datareader.data as web

DataSource = 'google'
StartDate = '1/1/2015'
EndDate = '12/31/2015'
Investment = 10000.00
TransactionFee = 7.00
RangeM = [1, 2, 3]
RangeN = [1, 2, 3]

# Positions:
#   Buy (not invested) means we have cash and are waiting to purchase
#   Sell (invested) means we have shares and are waiting to cash out
Buy = 0
Sell = 1

# Trend directions
Up = 0
Down = 1

# Enable or Disable the traceInvest() function
TraceInvest = False

def positionDescr(p):
    if p == Buy:
        return "Buy"
    elif p == Sell:
        return "Sell"
    else:
        return "???"

def directionDescr(d):
    if d == Up:
        return "Up"
    elif d == Down:
        return "Down"
    else:
        return "???"

#
"""
newTrend(trend, previousValue, currentValue):
    Determine the trend given prior state (Up or Down, and count)
    and the previous and current price.
    
    Returns: the new trend: Up or Down, and consecutive count
"""
#
def newTrend(trend, previousValue, currentValue):
    if currentValue >= previousValue:
        # the trend is Up
        if trend[0] == Up:
            count = trend[1] + 1
        else:
            count = 1
        return Up, count
    else:
        # the trend is Down
        if trend[0] == Down:
            count = trend[1] + 1
        else:
            count = 1
        return Down, count

#
"""
buy(balance, price):
    Purchases shares at the given price; a transaction fee is subtracted from
    the balance before the transaction.
    
    Returns: the number of shares purchased
"""
#
def buy(balance, price):
    shares = (balance - TransactionFee) / price
    return shares

#
"""
sell(shares, price):
    Sells the shares at the given price; a transaction fee is subtracted from
    the balance after the transaction.
    
    Returns: the new cash balance
"""
#
def sell(shares, price):
    balance = (shares * price) - TransactionFee
    return balance

#
"""
exchange(position, balance, shares, price):
    Changes the current position:
        from Buy -> Sell, meaning we have cash and will purchase shares
        from Sell -> Buy, meaning we have shares and will sell to obtain cash
    Returns: new position, new balance, new number of shares
"""
#
def exchange(position, balance, shares, price):
    if position == Buy:
        shares = buy(balance, price)
        balance = 0
        position = Sell
    else:
        balance = sell(shares, price)
        shares = 0
        position = Buy
    return position, balance, shares

#
"""
change(position, trend, m, n):
    Determine whether our position (Buy or Sell) should change.
    Applies the current trend to the appropriate up or down threshold (m, n).
    
    Returns: True or False
"""
#
def change(position, trend, m, n):
    result = False
    if position == Buy:
        if trend[0] == Up and trend[1] >= n:
            result = True
    else:
        if trend[0] == Down and trend[1] >= m:
            result = True
    return result

#
"""
traceInvest(previousPrice, currentPrice, trend, m, n, position, balance, shares):
    a diagnostic function which prints the current state (used for debugging)
"""
#
def traceInvest(previousPrice, currentPrice, trend, m, n, position, balance, shares):
    if TraceInvest:
        print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7:.2f}\t{8:.2f}\t{9}".format(\
                                          previousPrice, \
                                          currentPrice, \
                                          directionDescr(trend[0]), \
                                          trend[1], \
                                          m,
                                          n,
                                          positionDescr(position),
                                          balance,
                                          shares,
                                          change(position, trend, m, n)))

#
"""
invest(d, m, n): 
    An investment simulation. Buys the Investment amount on the initial day,
    then based on Up and Down trends will sell and buy. At the end of the period
    of data provided, all shares will be sold (if still holding).
    There is a $7 fee on all transactions: applied before a buy, and after a sell.
    
    Parameters:
    d = DataFrame with a stock's data (date, open, high, low, close, volume)
        for some period of time
    m = number of consecutive Down trending days before selling
    n = number of consecutive Up trending days before buying
    
    Returns: the number of transactions (buys and sells) and the ending balance.
"""
#
def invest(d, m, n):
    closingPrices = d["Close"]
    initialPrice = closingPrices[0]
    finalPrice = closingPrices[len(closingPrices)-1]
    # initially buy at the Day 1 closing value
    position, balance, shares = exchange(Buy, Investment, 0, initialPrice)
    transactions = 1
    # initialize the trend as Down with count = 0
    trend = (Down, 0)
    previousPrice = initialPrice
    for i in closingPrices.index[1:]:
        currentPrice = closingPrices[i]
        trend = newTrend(trend, previousPrice, currentPrice)
        traceInvest(previousPrice, currentPrice, trend, m, n, position, balance, shares)
        previousPrice = currentPrice
        if change(position, trend, m, n):
            position, balance, shares = exchange(position, balance, shares, currentPrice)
            transactions += 1
    # if we still are holding shares (our position is Sell) then exchange at the final day price
    if position == Sell:
        position, balance, shares = exchange(position, balance, shares, finalPrice)
        transactions += 1
    return transactions, balance

#
"""
getStockData(): ask user for Stock Ticker, get data, return DataFrame 
"""
#
def getStockData():
    symbol = input("Please enter Stock Ticker Symbol: ")
    symbol = symbol.upper()
    d = web.DataReader(symbol, DataSource, StartDate, EndDate)
    return d

#
""" test1(): a test for the invest() function """
#
def test1():
    d = getStockData()
    m = 1
    n = 1
    t, b = invest(d,m,n)
    print(t, b)

#
"""
main(): get stock data, call invest, show results
"""
#
def Main():
    d = getStockData()
    print("\t{}\t{}\t{}\t{}".format("m", "n", "Trans", "Balance"))
    iteration = 0
    for m in RangeM:
        for n in RangeN:
            iteration += 1
            transactions, balance = invest(d, m, n)
            print("{0}\t{1}\t{2}\t{3}\t${4:.2f}".format(iteration,m,n,transactions,balance))

def main():
    Main()
    
if __name__ == '__main__':
    main()
