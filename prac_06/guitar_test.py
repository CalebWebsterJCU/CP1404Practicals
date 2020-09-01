"""
Guitar Test
1/09/2020
This program serves as a test run for Guitar class in guitar.py
"""

from prac_06.guitar import Guitar
from datetime import datetime
CURRENT_YEAR = datetime.now().year

g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
g2 = Guitar("Awesome Guitar", 2013, 2500.00)
print(g1, g2)
print([g1], [g2])
print(f"{g1.name} get_age() - Expected 98. Got {g1.get_age(CURRENT_YEAR)}")
print(f"{g2.name} get_age() - Expected 7. Got {g2.get_age(CURRENT_YEAR)}")
print(f"{g1.name} is_vintage() - Expected True. Got {g1.is_vintage(CURRENT_YEAR)}")
print(f"{g2.name} is_vintage() - Expected False. Got {g2.is_vintage(CURRENT_YEAR)}")
print("Guitar is a weird word. Think about it. G U I T A R")
print("Say it ten times:")
for x in range(10):
    print("Guitar")
