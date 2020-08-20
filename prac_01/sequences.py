"""
Number Sequence Generator
This program allows the user to display various
number sequences by selecting options from a menu.
"""

import math

MENU = """(E)ven numbers
(O)dd numbers
(S)quares
(Q)uit
"""


def main():
    """Display different number sequences between min and max values, based on user's choice."""
    print("Number Sequence Generator")
    print(MENU)
    selection = input(">>> ").lower()
    while selection != 'q':
        minimum, maximum = get_min_max_values()
        if selection == 'e':
            display_even_numbers(minimum, maximum)
        elif selection == 'o':
            display_odd_numbers(minimum, maximum)
        elif selection == 's':
            display_squares(minimum, maximum)
        else:
            print("Invalid option")
        print(MENU)
        selection = input(">>> ").lower()
    print("Goodbye!")


def get_min_max_values():
    """Get valid minimum and maximum integer values."""
    is_valid = False
    while not is_valid:
        try:
            minimum = int(input("Minimum: "))
            maximum = int(input("Maximum: "))
            if minimum > maximum:
                print("Minimum cannot be greater than maximum")
            else:
                is_valid = True
        except ValueError:
            print("Please enter integer values")
    return minimum, maximum


def display_even_numbers(x, y):
    """Display even numbers between minimum and maximum values."""
    for number in range(x, y + 1):
        if number % 2 == 0:
            print(number, end=' ')
    print()


def display_odd_numbers(x, y):
    """Display odd numbers between minimum and maximum values."""
    for number in range(x, y + 1):
        if number % 2 != 0:
            print(number, end=' ')
    print()


def display_squares(x, y):
    """Display squares between minimum and maximum values."""
    for number in range(x, y + 1):
        if math.sqrt(number) % 1 == 0:
            print(number, end=' ')
    print()


def run_tests():
    """Test functions."""
    display_squares(0, 100)
    display_even_numbers(0, 100)
    display_odd_numbers(0, 100)
    get_min_max_values()


# run_tests()
main()
