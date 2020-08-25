"""This program provides interesting information about a set of numbers."""

import statistics


def main():
    """Get numbers, add them to a list, then display useful information."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
                 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
                 'InterpreterInterface', 'StartServer', 'bob']
    numbers = []
    number_index = 1
    number = get_float("Number {}: ".format(number_index))
    while number >= 0:
        numbers.append(number)
        number_index += 1
        number = get_float("Number {}: ".format(number_index))

    for number in numbers:
        print(number, end=" ")
    print()
    display_information(numbers)
    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def display_information(numbers: list):
    """Displays useful information about a list of numbers."""
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The sum of the numbers is {}".format(sum(numbers)))
    print("The average of the numbers is {:.2f}".format(statistics.mean(numbers)))
    print("The median value is {:.2f}".format(statistics.median(numbers)))


def get_float(prompt: str = "Number: ") -> float:
    """Get an integer value that is greater than a specified value."""
    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = float(input(prompt))
            is_valid = True
        except ValueError:
            print("Please enter a number")
    return number


main()
