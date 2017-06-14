#!/usr/bin/env python3
#
# Michael Uftring, Indiana University
# I590 - Python, Summer 2017
#
# Assignment 6, Question 5
#
# A simple password checker.
#

MinLength = 4
MaxLength = 8
SpecialChars = "$#@"

def minLengthCheck(password):
    if len(password) >= MinLength:
        return True
    else:
        return False

def maxLengthCheck(password):
    if len(password) <= MaxLength:
        return True
    else:
        return False

def firstCharacterIsALetter(password):
    if password[0].isalpha():
        return True
    else:
        return False

def containsANumber(password):
    for char in password:
        if char.isdigit():
            return True
    return False    

def containsSpecialCharacter(password):
    for char in password:
        if char in SpecialChars:
            return True
    return False

def main():
    password = input("Please enter a password: ")
    if not minLengthCheck(password):
        print("Error: The password has less than {} characters!".format(MinLength))
        return
    if not maxLengthCheck(password):
        print("Error: The password has more than {} characters!".format(MaxLength))
        return
    if not firstCharacterIsALetter(password):
        print("Error: The password does not start with a letter!")
        return
    if not containsANumber(password):
        print("Error: The password does not contain a number!")
        return
    if not containsSpecialCharacter(password):
        print("Error: The password does not have at least one character from [{}]".format(SpecialChars))
        return
    print("You entered a valid password.")

if __name__ == '__main__':
     main()
