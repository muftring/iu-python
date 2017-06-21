#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 7, Question 5
#
# A game of points, revisited; with Tennis style scoring!
# An interestng description of Tennis scoring can be found
# here: https://en.wikipedia.org/wiki/Tennis_scoring_system#History
# This WikiPedia article provides some interesting historical perspective
# into why the scores progress: 0 -> 15 -> 30 -> 40 -> deuce -> win (60)
#

#
""" point(): ask user who scores, returns A or B, or Q to quit, or whatever the user entered """
#
def point():
    player = input("Who wins a point, player A or player B? ")
    return player.upper()

#
""" tennis(score): return Tennis style score for number of points """
#
def tennis(score):
    if score == 0: 
        return 0
    elif score == 1:
        return 15
    elif score == 2:
        return 30
    else:
        return 40

#
""" display(scoreA, scoreB): show each player's score, when beyond 40 show which has the advantage """
#
def display(scoreA, scoreB):
    if scoreA >= 4 and scoreA > scoreB:
        playerA = "Adv"
        playerB = ""
    elif scoreB >= 4 and scoreB > scoreA:
        playerA = ""
        playerB = "Adv"
    else:
        playerA = tennis(scoreA)
        playerB = tennis(scoreB)
    print("Score of Player A: {}".format(playerA))
    print("Score of Player B: {}".format(playerB))

#
""" winner(scoreA, scoreB): determine if there is a winner of this game yet """
#
def winner(scoreA, scoreB):
    if scoreA >= 4 and scoreA - scoreB >= 2:
        return "A"
    elif scoreB >= 4 and scoreB - scoreA >= 2:
        return "B"
    else:
        return ""

#
""" game(): play until there is a winner, or opt to quit """
#
def game():
    scoreA = scoreB = 0
    while True:
        score = point()
        if score == "A":
            scoreA += 1
        elif score == "B":
            scoreB += 1
        elif score == "Q":
            print("You quit the game")
            return
        else:
            print("Error - invalid input: please enter A, B or Q (to quit)")
            continue
        player = winner(scoreA, scoreB)
        if player != "":
            print("Player {} wins the game".format(player))
            break
        else:
            display(scoreA, scoreB)

def main():
    game()

if __name__ == '__main__':
     main()
