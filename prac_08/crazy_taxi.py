"""
Crazy Taxi
27/09/2020
This class inherits from taxi and represents a taxi
from the 2010 SEGA game "Crazy Taxi", which can do
stunts, smash other cars, drift, and... Become a bowling ball???!!!
"""

from prac_08.taxi import Taxi
import random as r


class CrazyTaxi(Taxi):
    """Represent a crazy taxi that has the basic functionality of a normal taxi but can do crazy stunts."""
    welcome_message = "Hey hey, come on over, have some fun with craaaaaazy taxi!!!"
    craziness = 50
    base_cash_per_stunt = 10
    drivers = ["Axel", "B.D. Joe", "Gena", "Gus"]

    def __init__(self, name, fuel):
        """Initialize CrazyTaxi Class."""
        super().__init__(name, fuel)
        self.stunt_cash_earned = 0
        self.driver = r.choice(self.drivers)
        self.total_pins = 0
        self.total_damage_done = 0
        self.total_distance_drifted = 0
        self.total_air_time = 0

    def __str__(self):
        """Define rules for printing class objects."""
        return super().__str__() + " driver={} (Crazy)".format(self.driver)

    def start_fare(self):
        """Begin a new fare."""
        super().start_fare()
        self.stunt_cash_earned = 0

    def get_fare(self):
        """Return the current fare, adding stunt_cash."""
        return super().get_fare() + self.stunt_cash_earned

    def bowl(self):
        """Knock bowling pins over with the taxi."""
        pins_toppled = r.randint(0, 10)
        self.stunt_cash_earned += pins_toppled * self.base_cash_per_stunt
        return pins_toppled

    def smash_stuff(self):
        """Smash another car with the taxi."""
        damage_done = r.randint(0, self.craziness)
        self.stunt_cash_earned += damage_done * self.base_cash_per_stunt
        return damage_done

    def drift(self):
        """Drift."""
        distance_drifted = r.randint(0, self.craziness)
        self.stunt_cash_earned += distance_drifted * self.base_cash_per_stunt
        return distance_drifted

    def jump(self):
        """Jump."""
        air_time = r.randint(0, self.craziness)
        self.stunt_cash_earned += air_time * self.base_cash_per_stunt
        return air_time

    def drive(self, distance):
        """Drive the taxi, performing random stunts."""
        distance_driven = super().drive(distance)
        number_of_stunts = round(distance_driven / 5)
        for x in range(number_of_stunts):
            if str(x).endswith("1"):
                pins_toppled = self.bowl()
                self.total_pins += pins_toppled
                # print("{} pins toppled".format(pins_toppled))
            elif str(x).endswith("2"):
                damage_done = self.smash_stuff()
                self.total_damage_done += damage_done
                # print("{} damage done".format(damage_done))
            elif str(x).endswith("3"):
                distance_drifted = self.drift()
                self.total_distance_drifted += distance_drifted
                # print("drifted {}m".format(distance_drifted))
            elif str(x).endswith("4"):
                air_time = self.jump()
                self.total_air_time += air_time
                # print("Jumped for {}s".format(air_time))
        return distance_driven


if __name__ == '__main__':
    crazy_taxi = CrazyTaxi("Bugatti", 500)
    print(crazy_taxi.welcome_message)
    for x in range(10):
        crazy_taxi.drive(60)
        print("Fuel: {}".format(crazy_taxi.fuel))
