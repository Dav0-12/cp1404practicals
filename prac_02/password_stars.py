"""Password Program"""


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    min_password_length = int(input("Password length: "))
    password = input("Enter password: ")
    while len(password) < min_password_length:
        password = input("Enter password: ")
    return password


main()
