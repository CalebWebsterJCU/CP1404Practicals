"""
Dict from Lists
1/09/2020
This program gets peoples names and DOB's and creates a dictionary from the two parallel lists.
"""
from datetime import datetime as d

CURRENT_DATE = d.now()
CURRENT_YEAR = CURRENT_DATE.year
NUMBER_OF_PEOPLE = 5


def main():
    """Get names & DOB's, append to 2 lists, create dictionaries from lists."""
    names = []
    birth_dates = []
    for x in range(NUMBER_OF_PEOPLE):
        name = input("Name: ").title()
        birth_date = get_valid_date_string("Date of birth: ")
        birth_date = convert_date_string(birth_date)
        names.append(name)
        birth_dates.append(birth_date)
    names_to_birth_dates = convert_lists_to_dict(names, birth_dates)
    for name in names_to_birth_dates:
        print(f"{name} is {CURRENT_YEAR - names_to_birth_dates[name][2]}")


def get_valid_date_string(prompt: str) -> str:
    """Get a valid date string input eg. '01/01/2000'"""
    date_string = ""
    is_valid = False
    while not is_valid:
        try:
            date_string = input(prompt)
            day, month, year = convert_date_string(date_string)
            if month not in range(1, 13) or day not in range(1, 32):
                print("Invalid date")
            else:
                is_valid = True
        except ValueError:
            print("Invalid date")
        except IndexError:
            print("Invalid date")
    return date_string


def convert_date_string(date_string: str) -> tuple:
    """Convert date string to day, month and year."""
    date_list = [int(part) for part in date_string.split('/')]
    day, month, year = date_list[0], date_list[1], date_list[2]
    return day, month, year


def convert_lists_to_dict(list1: list, list2: list):
    """Convert two parallel lists to a dictionary."""
    the_dict = {}
    if len(list1) == len(list2):
        for x in range(len(list1)):
            the_dict[list1[x]] = list2[x]
    else:
        print("Error: lists are not the same length")
    return the_dict


if __name__ == '__main__':
    main()
