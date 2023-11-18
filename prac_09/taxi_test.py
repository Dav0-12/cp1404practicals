"""
Prac 09 - Taxi Testing Code
"""
from prac_09.taxi import Taxi


def main():
    """Test code for testing Taxi class."""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)  # Drive 40 kilometres
    print_taxi_details(taxi)
    taxi.start_fare()  # Restart the meter (start a new fare)
    taxi.drive(100)  # Drive 100 kilometres
    print_taxi_details(taxi)


def print_taxi_details(taxi):
    """Prints the taxi and the current taxi fare."""
    print(taxi)  # Print the taxi's details
    print(taxi.get_fare())  # Print the current fare


main()
