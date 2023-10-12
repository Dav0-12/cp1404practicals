"""
Wimbledon
Estimate: 50 minutes
Actual:   30 minutes
"""

import csv
FILENAME = "wimbledon.csv"


def main():
    """Extract Wimbledon data and display it"""
    champion_to_victories, countries = extract_data()
    display_champions(champion_to_victories)
    display_countries(countries)


def extract_data():
    """Extract champion and country data from file"""
    champion_to_victories = {}
    countries = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Remove header
        for record in reader:
            champion = record[2]
            country = record[1]
            champion_to_victories[champion] = champion_to_victories.get(champion, 0) + 1
            countries.append(country)
    return champion_to_victories, countries


def display_champions(champion_to_victories):
    """Display Wimbledon champions and their number of victories"""
    print("\nWimbledon Champions: ")
    for champion, victory in champion_to_victories.items():
        print(f"{champion} {victory}")


def display_countries(countries):
    """Display champion countries without duplicates"""
    victorious_countries = sorted(list(set(countries)))
    victorious_countries_string = ",".join(victorious_countries)
    print(f"\nThese countries {len(victorious_countries)} have won Wimbledon: ")
    print(victorious_countries_string)


main()
