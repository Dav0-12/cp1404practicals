"""
CP1404/CP5632 - Practical
Score Menu System
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
print(MENU)


def main():
    """Print main menu and ask for input"""
    choice = input(">> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            grade = grade_score(score)
            print(grade)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = input(">> ").upper()
    print("Farewell")


def get_valid_score():
    """Get score from user, if it isn't between 0 and 100 inclusive continue to prompt"""
    score = int(input("Score: "))
    while score > 100 or score < 0:
        score = int(input("Score: "))
    return score


def grade_score(score):
    """Receives a score and determines the corresponding grade"""
    # Note: The validation is not required for this program as the score is already
    # validated, but for future flexibility it was kept
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


def print_stars(score):
    """Print score number of stars"""
    print("*" * score)


main()
