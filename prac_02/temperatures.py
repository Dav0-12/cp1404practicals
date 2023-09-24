"""
CP1404/CP5632 - Practical
Code for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Get user input from menu to decide what temperature conversion is required"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_c_to_f(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_f_to_c(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_f_to_c(fahrenheit):
    """Convert from Fahrenheit to Celsius"""
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


def convert_c_to_f(celsius):
    """Convert from Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
