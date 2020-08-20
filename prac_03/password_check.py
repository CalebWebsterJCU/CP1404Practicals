"""This program gets a password from the user and prints asterisks as long as the password."""

MINIMUM_LENGTH = 5


def main():

    password = get_password()
    print_password_asterisks(password)


def print_password_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password


main()
