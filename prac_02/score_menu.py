"""Score Menu System"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
print(MENU)


def main():
    choice = input(">> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            evaluation = evaluate_result(score)
            print(evaluation)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = input(">> ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Score: "))
    while score > 100 or score < 0:
        score = int(input("Score: "))
    return score


def evaluate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


def print_stars(score):
    print("*" * score)


main()
