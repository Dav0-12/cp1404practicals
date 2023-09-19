"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    evaluation = evaluate_grade(score)
    print(evaluation)

    score = random.randint(0, 100)
    evaluation = evaluate_grade(score)
    print(evaluation)


def evaluate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


main()
