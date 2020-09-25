"""
Unreliable Car
25/09/2020
This class inherits from Car and represents an unreliable car object.
"""

from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Unreliable Car class."""

    def __init__(self, name, fuel, reliability):
        """Initialize class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the unreliable car if it doesn't break down."""
        distance_driven = 0
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
