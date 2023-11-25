"""
Prac 09 - Taxi Simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator. Allow users to keep track of their current fare while driving in different taxis."""
    current_taxi = None
    current_bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "d":
            current_bill = drive_taxi(current_bill, current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill:.2f}")
        print(MENU)
        choice = input(">>>").lower()
    print(f"Total trip cost: ${current_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_bill, current_taxi):
    """
    Prompt the user for a distance to drive in the current taxi, then update the current bill.
    Note: If the current taxi is empty (None) a notification will be printed
    """
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        try:
            distance = float(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you: ${cost:.2f}")
            current_bill += cost
        except ValueError:
            print("Not a valid number")
    return current_bill


def choose_taxi(current_taxi, taxis):
    """Prompt the user with a list of taxis, and update the current taxi with their choice."""
    print("Taxi's available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        chosen_taxi_number = int(input("Choose taxi: "))
        current_taxi = taxis[chosen_taxi_number]
    except ValueError:
        print("Not a valid number")
    except IndexError:
        print("Invalid option")
    return current_taxi


main()
