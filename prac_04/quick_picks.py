"""Quick Picks Programme"""

import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Calculate and display quick picks"""
    try:
        number_of_quick_picks = int(input("How many quick picks do you want to generate? "))
        quick_picks = create_quick_picks(number_of_quick_picks)
        display_quick_picks(quick_picks)
    except ValueError:
        print("Not a valid integer")


def create_quick_picks(number_of_quick_picks):
    """Create an n x 6 matrix of random numbers between MINIMUM_NUMBER and MAXIMUM_NUMBER"""
    quick_picks = []
    validated = False
    for line in range(number_of_quick_picks):
        quick_pick = []
        for number in range(NUMBERS_PER_LINE):
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while not validated:
                if random_number not in quick_pick:
                    validated = True
                else:
                    random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(random_number)
            validated = False
        quick_picks.append(sorted(quick_pick))
    return quick_picks


def display_quick_picks(numbers):
    """Display matrix of numbers"""
    for line in range(len(numbers)):
        # string = " ".join([str(number) for number in numbers[line]])
        for column in range(len(numbers[line])):
            print(f"{numbers[line][column]:2}", end=" ")
        print("\r")


main()
