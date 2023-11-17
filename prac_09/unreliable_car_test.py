"""
Prac 09 - Unreliable Car Class Testing
"""
from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Car", 100, 40)
my_car.drive(30)
print(f"Car has fuel: {my_car.fuel}")
print(my_car)

limo = UnreliableCar("Limo", 80, 90)
limo.add_fuel(20)
print(f"Car has fuel: {limo.fuel}")
limo.drive(115)
print(limo)
