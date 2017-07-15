#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Final Project, Phase 1
#

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
    for variable in variables:
        attribute = a2cIndex[variable]
        title = variable + " : " + attribute
        series = df[variable]
        plotHistogram(series, variable, title)

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

if __name__ == '__main__':
    main()
