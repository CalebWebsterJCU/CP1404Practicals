"""This program gets strings from the user and then prints all of the strings that were repeated (entered more than once)."""


def main():
    """Get strings until an empty string is entered, then print each string that was repeated."""
    strings = []
    print("Enter strings, enter an empty string to quit")
    string = input("String: ")
    while string:  # Empty string returns False
        strings.append(string)
        string = input("String: ")
    repeated_strings = find_repeated_list_elements(strings)
    print("Strings repeated:")
    if repeated_strings:
        for string in repeated_strings:
            print(string)
    else:
        print("No repeated strings entered")


def find_repeated_list_elements(elements: list) -> list:
    """Return elements in a list that are repeated."""
    repeated_elements = []
    for element in elements:
        if elements.count(element) > 1:
            if element not in repeated_elements:
                repeated_elements.append(element)
    return repeated_elements


main()
