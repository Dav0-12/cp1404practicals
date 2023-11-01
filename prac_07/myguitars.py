"""
Prac 07 - More Guitars Exercise
Estimated Duration: 15 mins
Actual Duration:
"""

import csv
from prac_07.guitar import Guitar

guitars = []
with open('guitars.csv', 'r', newline='') as in_file:
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))

for guitar in sorted(guitars):
    print(guitar)


