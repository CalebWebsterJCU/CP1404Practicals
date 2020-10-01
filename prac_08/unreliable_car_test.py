"""
Unreliable Car Test
25/09/2020
This program tests the class UnreliableCar
"""

from prac_08.unreliable_car import UnreliableCar

car1 = UnreliableCar("Holden Commodore", 100, 25)
print(car1)
for x in range(5):
    car1.drive(20)
    print(car1)

car2 = UnreliableCar("Subaru WRX", 100, 75)
print(car2)
for x in range(5):
    car2.drive(20)
    print(car2)

car3 = UnreliableCar("Mitsubishi Evo", 100, 50)
print(car3)
for x in range(5):
    car3.drive(20)
    print(car3)
