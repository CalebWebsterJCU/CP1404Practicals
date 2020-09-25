"""
Guitars File Reader Version 2
25/09/2020
This file reads information from guitars.csv and displays the guitars inside.
"""

from prac_06.guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    """Read file and display contents as a list of tuples."""
    guitars = []
    file_in = open(FILE_NAME, "r")
    for line in file_in:
        parts = line.strip().split(",")
        parts[1], parts[2] = int(parts[1]), float(parts[2])
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    file_in.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
