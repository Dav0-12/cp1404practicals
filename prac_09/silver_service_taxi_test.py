"""
Prac 09 - Test code for silver service taxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Taxi", 100, 2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())
