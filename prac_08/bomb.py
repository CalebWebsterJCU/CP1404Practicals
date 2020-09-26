"""
Bomb
25/09/2020
This class inherits from Car and represents a defective car that doesn't drive, but still burns fuel.
"""

from prac_08.car import Car


class Bomb(Car):
    """Crappy car that doesn't move when it drives."""
    push_distance = 10

    def __init__(self, name, fuel):
        """Initialize Bomb class."""
        super().__init__(name, fuel)

    def __str__(self):
        """Define rules for printing class objects."""
        return super().__str__() + " (Bomb)"

    def drive(self, distance):
        """Drive the car a given distance, consuming fuel, but not increasing distance."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += 0
        return distance

    def push(self):
        """Push the car a certain distance. Put ya back into it mate!"""
        self.odometer += self.push_distance
        return self.push_distance


if __name__ == '__main__':
    car = Bomb("Range Rover", 100)
    print(car)
    car.drive(100)
    print(car)
    car.push()
    print(car)
