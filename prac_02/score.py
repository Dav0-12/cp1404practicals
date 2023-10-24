"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    """Get score from user, get a random score, and then print the grade of both"""
    score = float(input("Enter score: "))
    evaluation = evaluate_grade(score)
    print(evaluation)

    score = random.randint(0, 100)
    evaluation = evaluate_grade(score)
    print(evaluation)


def evaluate_grade(score):
    """From given score determine the grade"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


main()
