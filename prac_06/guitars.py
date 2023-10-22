"""
Prac 06 - Guitar prac
Estimated duration: 25 mins
Actual duration:
"""

from prac_06.guitar import Guitar

guitars = []


name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar)
    name = input("Name: ")

#  guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
#  guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars):
    vintage_string = "(vintage)" if guitar.is_vintage(2023) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

