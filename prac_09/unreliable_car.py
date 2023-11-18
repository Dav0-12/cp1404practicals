"""Unreliable Car Class Definition"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return the same string as Car but with reliability added"""
        return f"{super().__str__()}, reliability is {self.reliability}"

    def drive(self, distance):
        """
        Generate a random float between 0 and 100 and only drive if it is below reliability value.
        Return distance driven (0 if the car breaks down)
        """
        if random.uniform(0, 100) < self.reliability:
            super().drive(distance)
        else:
            return 0
