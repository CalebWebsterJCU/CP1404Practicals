"""
Eco Taxi
26/09/2020
This class inherits from Taxi and represents a economic taxi which
uses less fuel and gives a percentage discount on fares.
"""

from prac_08.taxi import Taxi


class EcoTaxi(Taxi):
    """Economic Taxi that uses less fuel and costs less."""
    fuel_usage = 0.5
    fare_discount = 0.5

    def __init__(self, name, fuel):
        """Initialize EcoTaxi class."""
        super().__init__(name, fuel, 1.2)

    def __str__(self):
        """Define rules for printing class objects."""
        return super().__str__() + " fuel usage=%{}, discount=%{}".format(self.fuel_usage * 100, self.fare_discount * 100)

    def get_fare(self):
        """Return the price for the taxi trip, with discount applied."""
        fare = self.price_per_km * self.current_fare_distance
        fare -= self.fare_discount * fare
        return round(fare, 1)

    def drive(self, distance):
        """Drive the taxi, calculating fare distance and using less fuel."""
        if distance > self.fuel / self.fuel_usage:
            distance = round(self.fuel / self.fuel_usage)
            self.fuel = 0
        else:
            self.fuel -= distance * self.fuel_usage
        self.odometer += distance
        self.current_fare_distance += distance
        return distance


if __name__ == '__main__':
    taxi = EcoTaxi("Tesla", 100)
    print(taxi)
    taxi.start_fare()
    taxi.drive(200)
    print(taxi)
    print(taxi.get_fare())
