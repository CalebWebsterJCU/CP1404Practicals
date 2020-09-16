"""
Car Simulator
02/09/2020
This program allows the user to create, drive, and refuel their car. Uses the Car class imported from car.py
Pre Sick
"""

from prac_06.car import Car

MENU = """Menu:
d) Drive
r) Refuel
q) Quit"""
MENU_PROMPT = '>>> '
STARTING_FUEL = 100


def main():
    """Get name, create car object, drive and refuel car."""
    name = get_nonempty_string("Enter your car's name: ")
    car = Car(name, STARTING_FUEL)
    print(car)
    print(MENU)
    choice = input(MENU_PROMPT).lower()
    while choice != 'q':
        if choice == 'd':
            distance = get_positive_float(prompt="How many km do you want to drive? ", negative_error="Distance must be >= 0")
            distance_driven = car.drive(distance)
            out_of_fuel_string = " and ran out of fuel" if distance_driven <= car.fuel else ""
            print(f"{car.name} drove {distance_driven}km{out_of_fuel_string}.")
        elif choice == 'r':
            fuel_to_add = get_positive_float(prompt="How many units of fuel do you want to add to the car? ", negative_error="Fuel amount must be >= 0")
            car.add_fuel(fuel_to_add)
            print(f"Added {fuel_to_add} units of fuel.")
        else:
            print("Invalid menu choice")
        print(car)
        print(MENU)
        choice = input(MENU_PROMPT).lower()
    print(f"Goodbye {car.name}'s driver.")


def get_nonempty_string(prompt="String: ", error="Input cannot be blank"):
    """Get a string, making sure it is not empty."""
    string = input(prompt)
    while string == '':
        print(error)
        string = input(prompt)
    return string


def get_positive_float(prompt: str = "Number: ", value_error: str = "Invalid input; enter a valid number", negative_error: str = "Number must be >= 0") -> float:
    """Get an integer, making sure it is greater than a given value."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = float(input(prompt))
            if number >= 0:
                is_valid = True
            else:
                print(negative_error)
        except ValueError:
            print(value_error)
    return number


if __name__ == '__main__':
    main()
