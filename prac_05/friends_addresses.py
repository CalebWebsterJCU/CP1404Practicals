"""
Friends Addresses
1/09/2020
This program stores friends' addresses and allows the user to add friends, change addresses, and display addresses of friends.
"""

MENU = """MENU
A - Add new name & address
C - Change existing address
D - Display address for name
Q - Quit"""
INPUT_PROMPT = ">>> "
FILE_NAME = 'friends_addresses.txt'


def main():
    """Store names: addresses as dict, add, change and display addresses."""
    names_to_addresses = read_data_to_dict(FILE_NAME)
    print(names_to_addresses)
    print("Friends' Addresses by Caleb Webster")
    print(MENU)
    choice = input(INPUT_PROMPT).lower()
    while choice != 'q':
        if choice == 'a':
            add_name_address(names_to_addresses)
        elif choice == 'c':
            change_address(names_to_addresses)
        elif choice == 'd':
            display_address(names_to_addresses)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(INPUT_PROMPT).lower()
    save_dict_to_file(FILE_NAME, names_to_addresses)
    print(f"{len(names_to_addresses)} addresses saved to {FILE_NAME}")


def read_data_to_dict(file_name):
    """Read data from a file into a dictionary."""
    the_dict = {}
    file_in = open(file_name, 'r')
    for line in file_in:
        key, value = line.strip().title().split(': ')
        the_dict[key] = value
    file_in.close()
    return the_dict


def add_name_address(names_addresses):
    """Get name and address and add it to a dictionary."""
    name = get_nonempty_string("Name: ").title()
    address = get_nonempty_string("Address: ").title()
    names_addresses[name] = address
    print(f"{name} with address {address} added!")


def change_address(names_addresses):
    """Get name and new address and add them to dictionary."""
    print("Enter the name of the person's address that you want to change")
    name = get_string_in_dict(names_addresses, INPUT_PROMPT).title()
    new_address = get_nonempty_string("New address: ").title()
    names_addresses[name] = new_address
    print(f"{name}'s address changed to {new_address}!")


def display_address(names_addresses):
    """Display address stored in dictionary for a given name."""
    name = get_string_in_dict(names_addresses, "Name: ").title()
    print(f"{name}'s address is {names_addresses.get(name)}")


def save_dict_to_file(file_name, data):
    """Write dictionary entries to a file."""
    file_out = open(file_name, 'w')
    for entry in data:
        print(f"{entry}: {data.get(entry)}", file=file_out)
    file_out.close()


def get_nonempty_string(prompt="String: ", error="Input cannot be blank"):
    """Get a string, making sure it is not empty."""
    string = input(prompt)
    while string == '':
        print(error)
        string = input(prompt)
    return string


def get_string_in_dict(valid_strings, prompt: str = "Input: "):
    """Get a string from the user, making sure it is in a specified list."""
    string = input(prompt).title()
    while string not in valid_strings:
        print(f"Invalid input; must be in {valid_strings}")
        string = input(prompt).title()
    return string


if __name__ == '__main__':
    main()
