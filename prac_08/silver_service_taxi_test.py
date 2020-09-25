"""
Silver Service Taxi Test
25/09/2020
This program tests the SilverServiceTaxi class from prac_08/silver_service_taxi.py
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Subaru", 100, 2)
print(taxi)
taxi.drive(18)
print(taxi.get_fare())
