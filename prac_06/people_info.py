"""
People Info
1/09/2020
This program stores inputted people's details into class Person as a list, then displays all people.
"""
from prac_06.person import Person


def main():
    """Get first name, last name, and age until blank first name is entered. Store people, then print."""
    people = []
    first_name = input("First Name: ").title()
    while first_name != '':
        last_name = get_nonempty_string("Last name: ").title()
        age = get_positive_integer("Age: ")
        new_person = Person(first_name, last_name, age)
        people.append(new_person)
        print(f"{new_person} added.")
        first_name = input("First Name: ").title()
    # people.append(Person("Caleb", "Webster", 19))
    # people.append(Person("Joel", "Webster", 17))
    # people.append(Person("Micah", "Webster", 13))
    print("People:")
    longest_first_name_length = 0
    longest_last_name_length = 0
    for person in people:
        if len(person.first_name) > longest_first_name_length:
            longest_first_name_length = len(person.first_name)
        if len(person.last_name) > longest_last_name_length:
            longest_last_name_length = len(person.last_name)
    for i, person in enumerate(people, 1):
        adult_string = " (adult)" if person.is_adult() else ""
        print(f"{i}. {person.first_name:{longest_first_name_length}} {person.last_name:{longest_last_name_length}}, age {person.age}{adult_string}")


def get_nonempty_string(prompt="String: ", error="Input cannot be blank"):
    """Get a string, making sure it is not empty."""
    string = input(prompt)
    while string == '':
        print(error)
        string = input(prompt)
    return string


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
                print("Number must be > 0")
        except ValueError:
            print(error)
    return number


if __name__ == '__main__':
    main()
