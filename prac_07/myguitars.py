"""
Prac 07 - More Guitars Exercise
Estimated Duration: 15 mins
Actual Duration:
"""

import csv
from prac_07.guitar import Guitar

FILE_NAME = 'guitars.csv'

guitars = []
with open(FILE_NAME, 'r', newline='') as in_file:
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    price = float(input("Price: "))
    guitars.append(Guitar(name, year, price))
    name = input("Name: ")

with open(FILE_NAME, 'w') as out_file:
    for guitar in sorted(guitars):
        print(f'{guitar.name},{guitar.year},{guitar.cost}', file=out_file)
