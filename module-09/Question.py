#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 9
#

import numpy as np

WeightForHomeworks     = 0.20
WeightForLabs          = 0.30
WeightForFinalProject  = 0.10
WeightForMidterm1      = 0.10
WeightForQuizes        = 0.15
WeightForMidterm2      = 0.15

GradesForHomeworks     = (0, 5)
GradesForLabs          = (6, 16)
GradeForFinalProject   = (17, 17)
GradeForMidterm1       = (18, 18)
GradesForQuizes        = (19, 27)
GradeForMidterm2       = (28, 28)

AssignmentLabels = ["HW 0","HW 1","HW 2","HW 3","HW 4","HW 5","Lab 01","Lab 02","Lab 03","Lab 04","Lab 05","Lab 06","Lab 07","Lab 08","Lab 09","Lab 10","Lab 11","Final Project","Midterm 1","Quiz 01","Quiz 02","Quiz 03","Quiz 05","Quiz 06","Quiz 07","Quiz 08","Quiz 09","Quiz 10","Midterm 2"]

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

def calculateStudentGrade(grades, divisors, weights):
    return np.sum((np.where(grades < 0, 0, grades) / divisors) * weights) * 100.0

def setWeightsFor(a, r, w):
    r = range(r[0], r[1]+1)
    n = len(r)
    for i in r:
        a[i] = w/n

def setupWeights():
    weights = np.zeros(29)
    setWeightsFor(weights, GradesForHomeworks,   WeightForHomeworks)
    setWeightsFor(weights, GradesForLabs,        WeightForLabs)
    setWeightsFor(weights, GradeForFinalProject, WeightForFinalProject)
    setWeightsFor(weights, GradeForMidterm1,     WeightForMidterm1)
    setWeightsFor(weights, GradesForQuizes,      WeightForQuizes)
    setWeightsFor(weights, GradeForMidterm2,     WeightForMidterm2)
    return weights

def main():
    weights = setupWeights()
    data = np.load("Grades.npy")
    rows, cols = data.shape
    divisors = data[0][1:]
    
    #
    # student average and grade
    #
    studentNumericGrades = np.zeros((rows-1, 2))
    studentLetterGrades = np.empty((rows-1, 2), dtype='<U5')
    
    for r in range(1, rows):
        studentId = data[r,0]
        studentNumericGrades[r-1] = (studentId, calculateStudentGrade(data[r][1:], divisors, weights))
        studentLetterGrades[r-1] = (studentId, letterGrade(studentNumericGrades[r-1,1]))
    
    studentGrades = np.hstack((studentLetterGrades[:,[0]], studentNumericGrades[:,[1]], studentLetterGrades[:,[1]]))
    print("")
    print("Per Student Grades")
    print("------------------")
    for sg in studentGrades:
        print("StudentId: {0} Average: {1:3.2f} Grade: {2}".format(sg[0], float(sg[1]), sg[2]))
        
    np.save("FinalGrades.npy", studentGrades)
    
    #
    # class average and grade
    #
    classAverage = np.empty((1, 2), dtype='<U5')
    classAvgNumeric = studentNumericGrades[:,[1]].sum() / len(studentNumericGrades[:,[1]])
    classAvgLetter = letterGrade(classAvgNumeric)
    classAverage[0] = (classAvgNumeric, classAvgLetter)
    print("")
    print("Class Average: {0:3.2f} Grade: {1}".format(classAvgNumeric, classAvgLetter))
    
    np.save("AverageGrades.npy", classAverage)
    
    #
    # average of each assignment
    #
    assignmentAverage = np.zeros((cols-1, 2))
    assignmentAverageLabeled = np.zeros((cols-1, 2), dtype='<U15')
    print("")
    print("Per Assignment Averages")
    print("-----------------------")
    for c in range(1,cols):
        assgt = data[1:,[c]]
        count = len(assgt)
        average = np.where(assgt < 0, 0, assgt).sum() / count
        print("{0} Average: {1:3.2f}".format(AssignmentLabels[c-1], average))
        assignmentAverage[c-1] = (c-1, average)
        assignmentAverageLabeled[c-1] = (AssignmentLabels[c-1], average)
    np.save("AverageAssig.npy", assignmentAverageLabeled)
    
    #
    # per assignment group
    #
    print("")
    print("Per Assignment Group Averages")
    print("-----------------------------")
    assignmentGroupAverage = np.zeros((6, 2), dtype='<U15')
    homeworkAverage = assignmentAverage[GradesForHomeworks[0]:GradesForHomeworks[1]+1,[1]].sum() / len(range(GradesForHomeworks[0], GradesForHomeworks[1]+1))
    print("Homework Average: {0:3.2f}".format(homeworkAverage))
    assignmentGroupAverage[0] = ("Homework", homeworkAverage)
    labsAverage = assignmentAverage[GradesForLabs[0]:GradesForLabs[1]+1,[1]].sum() / len(range(GradesForLabs[0], GradesForLabs[1]+1))
    print("Labs Average: {0:3.2f}".format(labsAverage))
    assignmentGroupAverage[1] = ("Labs", labsAverage)
    finalProjectAverage = assignmentAverage[GradeForFinalProject[0]:GradeForFinalProject[1]+1,[1]].sum() / len(range(GradeForFinalProject[0], GradeForFinalProject[1]+1))
    print("Final Project Average: {0:3.2f}".format(finalProjectAverage))
    assignmentGroupAverage[2] = ("Final Project", finalProjectAverage)
    midterm1Average = assignmentAverage[GradeForMidterm1[0]:GradeForMidterm1[1]+1,[1]].sum() / len(range(GradeForMidterm1[0], GradeForMidterm1[1]+1))
    print("Midterm 1 Average: {0:3.2f}".format(midterm1Average))
    assignmentGroupAverage[3] = ("Midterm 1", midterm1Average)
    quizAverage = assignmentAverage[GradesForQuizes[0]:GradesForQuizes[1]+1,[1]].sum() / len(range(GradesForQuizes[0], GradesForQuizes[1]+1))
    print("Quiz Average: {0:3.2f}".format(quizAverage))
    assignmentGroupAverage[4] = ("Midterm 1", quizAverage)
    midterm2Average = assignmentAverage[GradeForMidterm2[0]:GradeForMidterm2[1]+1,[1]].sum() / len(range(GradeForMidterm2[0], GradeForMidterm2[1]+1))
    print("Midterm 2 Average: {0:3.2f}".format(midterm2Average))
    assignmentGroupAverage[5] = ("Midterm 2", midterm2Average)
    np.save("AverageGroup.npy", assignmentGroupAverage)
    
if __name__ == '__main__':
    main()
