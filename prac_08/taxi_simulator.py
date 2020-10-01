"""
Taxi Simulator
25/09/2020
This program simulates taxi rides and allows the user to
ride in different taxis and keeps track of their bill.
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """
C)hoose taxi
D)rive
Q)uit"""


def main():
    """Run simulator program that allows user to choose
    and drive taxis and keeps track of their bill."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_distance_driven = 0
    total_cost = 0
    print("Lets drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = taxis[get_taxi_number(taxis)]
            print("Bill to date: ${:.2f}".format(total_cost))
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi first!")
            else:
                cost, distance_driven = drive_taxi(current_taxi)
                total_cost += cost
                total_distance_driven += distance_driven
                print("Bill to date: ${:.2f}".format(total_cost))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Total distance driven: {}km".format(total_distance_driven))
    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def get_taxi_number(taxis):
    """Get a valid taxi from the user."""
    taxi_number = get_positive_integer("Choose Taxi: ", "Invalid taxi number")
    while taxi_number > len(taxis) - 1:
        print("Invalid taxi number")
        taxi_number = get_positive_integer("Choose Taxi: ", "Invalid taxi number")
    return taxi_number


def display_taxis(taxis):
    """Display taxi objects."""
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


def drive_taxi(taxi):
    """Drive the current taxi a certain distance, if any are selected."""
    distance = get_positive_float("Drive how far? ", "Invalid distance")
    taxi.start_fare()
    distance_driven = taxi.drive(distance)
    cost = taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxi.name, cost))
    return cost, distance_driven


def get_positive_integer(prompt="Number: ", error="Invalid input"):
    """Get an integer, making sure it is positive."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            if number >= 0:
                is_valid = True
            else:
                print(error)
        except ValueError:
            print(error)
    return number


def get_positive_float(prompt="Number: ", error="Invalid input"):
    """Get a float, making sure it is >= 0."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = float(input(prompt))
            if number >= 0:
                is_valid = True
            else:
                print(error)
        except ValueError:
            print(error)
    return number


def run_tests():
    """Test functions."""
    print(get_positive_integer())
    print(get_positive_float())
    taxis = [Taxi("Van", 100), Taxi("Ute", 100), SilverServiceTaxi("Limo", 100, 2)]
    display_taxis(taxis)
    print(get_taxi_number(taxis))


if __name__ == '__main__':
    # run_tests()
    main()
