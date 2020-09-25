"""
Guitars File Reader
25/09/2020
This file reads information from guitars.csv and displays the guitars inside.
"""

from prac_06.guitar import Guitar

INPUT_FILE_NAME = "guitars.csv"
OUTPUT_FILE_NAME = "my_guitars.csv"


def main():
    """Read file and display contents as a list of tuples."""
    guitars = read_guitars(INPUT_FILE_NAME)
    guitars.sort()
    print("Your Guitars:")
    for guitar in guitars:
        print(guitar)

    name = input("Name: ").title()
    while name != '':
        year = get_positive_integer("Year: ")
        cost = get_positive_float("Cost: ")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ").title()

    # guitars.append(Guitar("Mario", 1995, 2400))
    # guitars.append(Guitar("Luigi", 2013, 45))
    # guitars.append(Guitar("Peach", 1970, 35))

    guitars.sort()
    write_guitars(guitars, OUTPUT_FILE_NAME)


def read_guitars(file_name):
    guitars = []
    file_in = open(file_name, "r")
    for line in file_in:
        parts = line.strip().split(",")
        parts[1], parts[2] = int(parts[1]), float(parts[2])
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    file_in.close()
    return guitars


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


def write_guitars(guitars, file_name):
    """Writes guitars in a list to a file."""
    file_out = open(file_name, "w")
    for guitar in guitars:
        print("{},{},{}".format(guitar.name, guitar.year, guitar.cost), file=file_out)
    file_out.close()


main()
