"""Unreliable Car Class Definition"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, reliability is {self.reliability}"

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            super().drive(distance)
        else:
            return 0
