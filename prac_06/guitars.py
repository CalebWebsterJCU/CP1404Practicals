"""
Guitars
1/09/2020
This program gets and stores a user's guitars in Guitars class (from guitar.py)
"""

from prac_06.guitar import Guitar
from datetime import datetime

CURRENT_YEAR = datetime.now().year


def main():
    """Get guitar names, years, and cost and store the details in objects of class Guitar."""
    guitars = []
    print("My guitars!")
    name = input("Name: ").title()
    while name != '':
        year = get_positive_integer("Year: ")
        cost = get_positive_float("Cost: ")
        guitars.append(Guitar(name, year, cost))
        print(Guitar(name, year, cost), "added.")
        name = input("Name: ").title()
    # guitars.append(Guitar("Mario", 1995, 2400))
    # guitars.append(Guitar("Luigi", 2013, 45))
    # guitars.append(Guitar("Peach", 1970, 35))
    print("My guitars:")
    longest_name_length = 0
    for guitar in guitars:
        if len(guitar.name) > longest_name_length:
            longest_name_length = len(guitar.name)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")


def get_positive_integer(prompt: str = "Number: ", error: str = "Invalid input; enter a valid number") -> int:
    """Get an integer, making sure it is greater than a given value."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            if number >= 0:
                is_valid = True
            else:
                print("Number must be >= 0")
        except ValueError:
            print(error)
    return number


def get_positive_float(prompt: str = "Number: ", error: str = "Invalid input; enter a valid number") -> float:
    """Get an integer, making sure it is greater than a given value."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = float(input(prompt))
            if number >= 0:
                is_valid = True
            else:
                print("Number must be >= 0")
        except ValueError:
            print(error)
    return number


def run_tests():
    """Test functions."""
    print(get_positive_integer())
    print(get_positive_float())


if __name__ == '__main__':
    # run_tests()
    main()
