"""This program gets a password from the user and prints asterisks as long as the password."""

MINIMUM_LENGTH = 5


def main():
    """Get password, then print asterisks."""

    password = get_password(MINIMUM_LENGTH)
    print_password_asterisks(password)


def print_password_asterisks(password):
    """Print asterisks based on length of password."""
    print("*" * len(password))


def get_password(min_length):
    """Get password, making sure that it is longer than minimum length."""
    password = input("Enter password: ")
    while len(password) < min_length:
        print("Invalid password")
        password = input("Enter password: ")
    return password


main()
