"""
Emails
Estimate: 30 minutes
Actual:   19 minutes
"""


def main():
    email_to_name = {}
    email = input("Gimme your email: ")
    while email != "":
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n)").upper()
        if choice == "" or choice == "Y":
            email_to_name[email] = name
        else:
            actual_name = input("Name: ")
            email_to_name[email] = actual_name
        email = input("Gimme your email: ")
        extract_name(email)

    print("\n")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    name = email.split("@")[0].replace(".", " ").title()  # Remove the .my.jcu.edu.au, etc from the end
    return name


main()
