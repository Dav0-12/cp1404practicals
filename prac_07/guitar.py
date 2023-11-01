"""Guitar Class Creation"""


class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self, current_year):
        """Calculate the age of the guitar given the current year"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Calculate whether the guitar is vintage (50 years or older) given the current year"""
        return self.get_age(current_year) >= 50
