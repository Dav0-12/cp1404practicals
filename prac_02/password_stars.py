"""Password Program"""


def main():
    min_password_length = int(input("Password length: "))
    password = get_valid_password(min_password_length)
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_valid_password(minimum_length):
    password = input("Enter password: ")
    while len(password) < minimum_length:
        password = input("Enter password: ")
    return password


main()
