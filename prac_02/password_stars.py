"""
CP1404/CP5632 - Practical
Program to print a number of stars equal to the length of a password
"""


def main():
    """Validate password and print password length number of stars"""
    min_password_length = int(input("Minimum password length: "))
    password = get_valid_password(min_password_length)
    print_asterisks(password)


def print_asterisks(password):
    """Print password length number of stars"""
    print("*" * len(password))


def get_valid_password(minimum_length):
    """Prompt user for password and validate that it is larger than or equal to minimum_length"""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        password = input("Enter password: ")
    return password


main()
