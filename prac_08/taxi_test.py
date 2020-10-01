"""
Taxi Test
25/09/2020
This program tests the Taxi class.
"""
from prac_08.taxi import Taxi
taxi_1 = Taxi("Prius 1", 100)
taxi_1.drive(40)
fare = taxi_1.get_fare()
print(taxi_1)
print("${:.2f}".format(fare))
taxi_1.start_fare()
taxi_1.drive(100)
fare = taxi_1.get_fare()
print(taxi_1)
print("${:.2f}".format(fare))
