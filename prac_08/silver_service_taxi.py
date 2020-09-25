"""
Silver Service taxi
25/09/2020
This class inherits from Car and represents a Silver Service Taxi
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi class."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize SilverServiceTaxi class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Define rules for printing class objects."""
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip plus flagfall."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
