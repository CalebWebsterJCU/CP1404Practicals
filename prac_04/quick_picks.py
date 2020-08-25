"""This program gets a number from the user, then generates that many lines of random numbers between two constraints."""

import random as r
MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_PICK = 6


def main():
    """Get number of lines, then generate that many lines of random numbers."""
    number_of_picks = get_int_greater_than_value("Number of quick picks: ", 0)
    for x in range(number_of_picks):
        numbers = list(range(MINIMUM, MAXIMUM + 1))

        # Choose a random number from numbers, then remove
        # it and return the value, appending it to pick... All in one line
        pick = [numbers.pop(numbers.index(r.choice(numbers))) for i in range(NUMBERS_PER_PICK)]

        # Find the largest number in a pick for formatting purposes
        largest_number = 0
        for number in pick:
            if number > largest_number:
                largest_number = number

        for number in sorted(pick):
            print("{:{}}".format(number, len(str(largest_number))), end=" ")
        print()


def get_int_greater_than_value(prompt: str = "Number: ", value: int = 0) -> int:
    """Get an integer value that is greater than a specified value."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            if number > value:
                is_valid = True
            else:
                print("Number must be > {0}".format(value))
        except ValueError:
            print("Please enter an integer")
    return number


main()
