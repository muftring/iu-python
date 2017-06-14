#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 6, Question 4
#
# A simple game of points.
#

Neither = 0
PlayerA = 1
PlayerB = 2
MaxCombinedPoints = 13
MaxPlayerPoints = 7
MinWinningPoints = 3
MinAdvantage = 2

def point():
    player = input("Enter player which scores a point, A or B: ")
    if player.lower() == "a":
        return PlayerA
    elif player.lower() == "b":
        return PlayerB
    else:
        print("Error: invalid input, must be A or B")
        return Neither

def enough(p1, p2):
    if p1 > p2 and p1 >= MinWinningPoints and (p1 - p2) >= MinAdvantage:
        return True
    else:
        return False

def winner(scoreForA, scoreForB):
    if scoreForA == MaxPlayerPoints:
        return PlayerA
    if scoreForB == MaxPlayerPoints:
        return PlayerB
    if enough(scoreForA, scoreForB):
        return PlayerA
    if enough(scoreForB, scoreForA):
        return PlayerB
    return Neither
    
def game():
    scoreForA = scoreForB = 0
    winningPlayer = Neither
    for round in range(MaxCombinedPoints):
        score = point()
        if score == PlayerA:
            scoreForA += 1
        elif score == PlayerB:
            scoreForB += 1
        print("The score is Player A: {} - Player B: {}".format(scoreForA, scoreForB))
        winningPlayer = winner(scoreForA, scoreForB)
        if winningPlayer != Neither:
            break
    return winningPlayer

def test1():
    score = point()
    print(score)

def test2():
    a,b = eval(input("input a, b: "))
    result =  enough(a, b)
    print("for {} - {} the result is {}".format(a, b, result))

def test3():
    a,b = eval(input("input a, b: "))
    result =  winner(a, b)
    print("for {} - {} the result is {}".format(a, b, result))

def Main():
    winner = game()
    if winner == PlayerA:
        winner = "A"
    else:
        winner = "B"
    print("The winner is Player {}".format(winner))
    
def main():
    Main()

if __name__ == '__main__':
     main()
