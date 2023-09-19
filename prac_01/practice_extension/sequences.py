"""
Menu-driven number sequence generator
"""
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

MENU = """  i. Show the even number from x to y
 ii. Show the odd number from x to y
iii. Show the squares from x to y
 iv. Exit the program """
print(MENU)
choice = input("Please enter the selected function: ")
while choice != "iv":
    if choice == "i":
        for num in range(lower_limit, upper_limit + 1):
            if num % 2 == 0:
                print(num, end=" ")
    elif choice == "ii":
        for num in range(lower_limit, upper_limit + 1):
            if num % 2 == 1:
                print(num, end=" ")
    elif choice == "iii":
        for num in range(lower_limit, upper_limit + 1):
            squared_val = lower_limit ** ((num - lower_limit) + 1)
            if squared_val <= upper_limit:
                print(squared_val, end=" ")
    else:
        print("Invalid Choice")
    print()
    print(MENU)
    choice = input("Please enter the selected function: ")
print("Finish")
