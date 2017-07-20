#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Final Project, Phase 2
#
# Phase 1: statistical analysis of the data, including plotting histograms
# Phase 2: classification of the data using k-means method
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFile = "Breast-Cancer-Wisconsin.csv"
NAValues = ['?']
ColumnNames = ['SampleCodeNumber', 
               'ClumpThickness', 
               'UniformityOfCellSize', 
               'UniformityOfCellShape', 
               'MarginalAdhesion', 
               'SingleEpithelialCellSize',
               'BareNuclei',
               'BlandChromatin',
               'NormalNucleoli',
               'Mitoses',
               'Class']

AnColumns = ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
AttributeColumns = ColumnNames
AttributeColumns.remove('SampleCodeNumber')
AttributeColumns.remove('Class')

AttributeValueMin = 1
AttributeValueMax = 10
AttributeValueRange = range(AttributeValueMin, AttributeValueMax+1)

a2cIndex = pd.Series(AttributeColumns, index = AnColumns)
c2aIndex = pd.Series(AnColumns, index = AttributeColumns)

Benign = 2
Malignant = 4

KMeansIterations = 1500
ShowFirstN = 20

#
"""
loadData(): loads the CSV file into a DataFrame, and performs some initial cleanup
    Returns:
        DataFrame
"""
#
def loadData():
    fileName = input("Please enter file name [default: {}]: ".format(DataFile))
    if fileName == "":
        fileName = DataFile
    # read CSV into DataFrame, convert NA values to NaN
    df = pd.read_csv(fileName, na_values=NAValues)
    # drop extraneous columns
    df.drop('Unnamed: 11', axis=1, inplace=True)
    df.drop('Unnamed: 12', axis=1, inplace=True)
    return df

#
"""
cleanData(df): applies data cleaning rules on some of the data
    currently just fills in missing values for A7 attribute with the median

    Returns:
        nothing, but rather modifes the DataFrame in place
"""
#
def cleanData(df):
    # fill missing value in A7 using median
    df.fillna(df.median(), inplace=True)

#
"""
generateSummaryTable(df, variables):
    generates a summary table of the specified variables in the DataFrame
    statistics included: min, max, mean, median, standard deviation, variance
"""
#
def generateSummaryTable(df, variables):
    print("\Statistic Summary Table")
    print("%-30s%9s%9s%9s%9s%9s%9s" % (
                "Attribute", 
                "Min", 
                "Max", 
                "Mean", 
                "Median", 
                "StdDev", 
                "Variance"))
    for variable in variables:
        attribute = a2cIndex[variable]
        series = df[variable]
        label = "{0:3s} {1}".format(variable, attribute)
        print("%-30s%9.3f%9.3f%9.3f%9.3f%9.3f%9.3f" % (
                label,
                series.min(), 
                series.max(), 
                series.mean(), 
                series.median(),
                series.std(),
                series.var()))

#
"""
plotHistogram(series, variable, title):
    generates a histogram from the Series, uses title for the plot title
    and variable for the output PNG file name
"""
#
def plotHistogram(series, variable, title):
    fig = plt.figure()
    sp = fig.add_subplot(1, 1, 1)
    sp.hist(series, bins=10, color="b", align='mid', alpha=0.5)
    #sp.set_xlim(AttributeValueMin, AttributeValueMax)
    #sp.set_xticks([1,2,3,4,5,6,7,8,9,10])
    #sp.hist(series, range=(AttributeValueMin, AttributeValueMax), align='mid', color="b", alpha=0.5)
    sp.set_title(title) 
    sp.set_xlabel('Value') 
    sp.set_ylabel('Count')
    fileName = variable + ".png"
    plt.savefig(fileName, dpi=100)

#
"""
generateHistograms(df, variables):
    generates a histogram for each Series in the DataFrame identified by the
    list of variables
"""
#
def generateHistograms(df, variables):
    print("\nGenerating Histograms...")
    for variable in variables:
        attribute = a2cIndex[variable]
        title = variable + " : " + attribute
        series = df[variable]
        plotHistogram(series, variable, title)

#
"""
distance(p1, p2):
    compute the Euclidian distance between two points
"""
#
def distance(p1, p2):
    return np.sqrt(((p1[AnColumns] - p2[AnColumns]) ** 2).sum())

#
"""
classify(df, u2, u4):
    assign each entry in the DataFrame to one of two groups using k-means approach:
    compute the distance between each entry and the two prior computed means (points)
    whichever point is closer represents the group to which the entry is assigned
"""
#
def classify(df, u2, u4):
    group2 = []
    group4 = []
    for index, row in df.iterrows():
        d2 = distance(row, u2)
        d4 = distance(row, u4)
        if d2 < d4:
            group2.append(index)
        else:
            group4.append(index)
    return group2, group4

#
"""
recomputeMeans(df, group2, group4):
    generate new mean values for each group based on the current members of
    the group
"""
#
def recomputeMeans(df, group2, group4):
    u2 = df.loc[df.index.isin(group2)].mean()
    u4 = df.loc[df.index.isin(group4)].mean()
    return u2, u4

#
"""
initialMeans(df):
    randomly select two sets of attributes from the DataFrame as the initial means
"""
#
def initialMeans(df):
    i2, i4 = np.random.randint(low=0, high=len(df), size=2)
    u2 = df.ix[i2]
    u4 = df.ix[i4]
    return u2, u4

#
"""
showFirstN(df, group, N):
    display the first N rows in df (a DataFrame), show the Class and Predicted Class
"""
#
def showFirstN(df, group, N):
    print("%5s%5s%10s%10s%10s" % ("N", "Index", "Id", "Class", "Predicted"))
    for n in range(N):
        idx = group[n]
        print("%5d%5d%10d%10d%10d" % (n, idx, df.ix[idx].Scn, df.ix[idx].CLASS, df.ix[idx].Predicted))

#
"""
printMeans(name, means, columns):
    display values in mean (which is a Series) specified by columns
"""
#
def printMeans(name, means, columns):
    print("{0}:".format(name), end='')
    for idx in columns:
        print(" {0}={1:.5f}".format(idx,means[idx]), end='')
    print("")

#
"""
runClassification(df):
    using k-means, attempt to classify the data in df (a DataFrame) into one of the
    two classes: 2-Benign, 4-Malignant
"""
#
def runClassification(df):
    print("\nRunning k-means Classification with",KMeansIterations,"iterations (please be patient)")
    # randomly select inital means
    u2, u4 = initialMeans(df)
    # iteratively run classification -> recompute means
    for i in range(KMeansIterations):
        # print a "progress dot" every iteration
        print(".", end = "", flush=True)
        group2, group4 = classify(df, u2, u4)
        u2, u4 = recomputeMeans(df, group2, group4)
    # add Predicted column to DataFrame, and store predicted classifications
    predicted = pd.Series(0, index=df.index)
    predicted[group2] = 2
    predicted[group4] = 4
    df['Predicted'] = predicted
    # display summary
    print("")
    print("Final Means")
    printMeans("u2", u2, AnColumns)
    printMeans("u4", u4, AnColumns)
    print("")
    print("Cluster Assignment: u2")
    showFirstN(df, group2, ShowFirstN)
    print("")
    print("Cluster Assignment: u4")
    showFirstN(df, group4, ShowFirstN)
    print("")

#
"""
main():
    load data, clean data, generate histograms and summary table
"""
#
def main():
    df = loadData()
    cleanData(df)
    generateHistograms(df, AnColumns)
    generateSummaryTable(df, AnColumns)
    runClassification(df)

if __name__ == '__main__':
    main()
