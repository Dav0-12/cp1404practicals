"""Password Program"""


def main():
    min_password_length = int(input("Password length: "))
    password = input("Enter password: ")
    while len(password) < min_password_length:
        password = input("Enter password: ")
    print("*" * len(password))


main()
