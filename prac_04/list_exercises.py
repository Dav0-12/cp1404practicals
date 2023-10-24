"""
List Exercises Practical
"""


numbers = []
number = int(input("Number 1: "))
count = 1
while number > 0:
    count += 1
    numbers.append(number)
    number = int(input(f"Number {count}: "))


print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


"""
Woefully inadequate security checker
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please enter you username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
