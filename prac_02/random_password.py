"""This program generates a random password based on the user's specifications."""
import random as r

CHARACTERS = ["aeioubcdfghjklmnpqrstvwxyz", "AEIOUBCDFGHJKLMNPQRSTVWXYZ", "0123456789", "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"]


def main():
    """Gets password length, number of uppercase, lowercase, numbers and symbols and generate a random password."""

    length = get_integer_greater_than_value("Password Length: ", 0)
    number_of_uppercase = get_integer_greater_than_value("Uppercase: ", -1)
    number_of_numbers = get_integer_greater_than_value("Numbers: ", -1)
    number_of_symbols = get_integer_greater_than_value("Symbols: ", -1)
    total_requirements = number_of_numbers + number_of_symbols + number_of_uppercase

    while total_requirements > length:
        print("Requirements cannot be more than password length")
        number_of_uppercase = get_integer_greater_than_value("Uppercase: ", -1)
        number_of_numbers = get_integer_greater_than_value("Numbers: ", -1)
        number_of_symbols = get_integer_greater_than_value("Symbols: ", -1)
        total_requirements = number_of_numbers + number_of_symbols + number_of_uppercase

    # Calculate number of lowercase characters to fill the gaps
    number_of_lowercase = length - total_requirements
    requirements = [number_of_lowercase, number_of_uppercase, number_of_numbers, number_of_symbols]

    password = build_password(requirements, length)
    print("Your randomly generated password is {}".format(password))


def build_password(requirements, length):
    """Construct a password meeting all requirements by randomly choosing character sets and characters."""
    password = ""
    for character_number in range(length):
        # choose a random character set
        character_set = r.randint(0, 3)
        while requirements[character_set] == 0:  # check that the character set requirement needs to be filled
            character_set = r.randint(0, 3)
        # choose a random character from selected character set
        password += r.choice(CHARACTERS[character_set])
        requirements[character_set] -= 1
    return password


def get_positive_integer(prompt):
    """Gets a positive integer input from the user."""

    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            if number >= 0:
                is_valid = True
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Please enter a positive integer")
    return number


def get_integer_greater_than_value(prompt, value):
    """Gets an integer value that is greater than a specified value."""

    number = 0
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            if number >= value:
                is_valid = True
            else:
                print("integer is greater than specified value")
        except ValueError:
            print("Please enter a positive integer")
    return number


def run_tests():
    """Test functions."""
    print(build_password([5, 3, 2, 2], 12))


# run_tests()
main()
