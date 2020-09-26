"""
Gas Guzzler
25/09/2020
This class inherits from Car and represents a gas-guzzling car that uses more fuel than it should.
"""

from prac_08.car import Car


class GasGuzzler(Car):
    """Fuel inefficient car."""
    fuel_usage = 4

    def __init__(self, name, fuel):
        """Initialize GasGuzzler class."""
        super().__init__(name, fuel)

    def __str__(self):
        """Define rules for printing class objects."""
        return super().__str__() + " fuel usage={}".format(self.fuel_usage)

    def drive(self, distance):
        """Drive the car a given distance, consuming more fuel, based on fuel_usage."""
        if distance > self.fuel / self.fuel_usage:
            distance = self.fuel / self.fuel_usage
            self.fuel = 0
        else:
            self.fuel -= distance * self.fuel_usage
        self.odometer += distance
        return distance


if __name__ == '__main__':
    car = GasGuzzler("Toyota Land Cruiser", 100)
    print(car)
    car.drive(25)
    print(car)