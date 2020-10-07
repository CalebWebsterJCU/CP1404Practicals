"""
Find Files
7/10/2020
This program searches files on the hard drive that match the specified criteria.
"""
import os

MENU = """
(N)ame
(S)ize
(T)ext
(Q)uit"""
DIRECTORY = "C:\\Users\\Caleb Webster\\"
WRITE_FILE = "files_found.txt"


def main():
    """Find and print files that match the criteria the user selects from the menu."""
    filenames = get_filenames(DIRECTORY)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "n":
            name = get_nonempty_string("Name: ", "Name cannot be blank")
            files_found = find_files_with_name(filenames, name)
            write_filenames(files_found, WRITE_FILE)
        elif choice == "s":
            size = round(get_positive_float("Size (MB): ") * 1000000)
            files_found = find_files_greater_than_size(filenames, size)
            write_filenames(files_found, WRITE_FILE)
        elif choice == "t":
            text = get_nonempty_string("Text: ", "Text cannot be blank")
            files_found = find_files_with_text(filenames, text)
            write_filenames(files_found, WRITE_FILE)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Goodbye!")


def get_filenames(directory):
    """Return all filenames in directory as a list."""
    all_filenames = []
    for directory_name, subdirectories, filenames in os.walk(directory):
        all_filenames += [os.path.join(directory_name, filename) for filename in filenames]
    return all_filenames


def write_filenames(filenames, write_file):
    """Write valid filenames to a file."""
    with open(write_file, 'w') as file_out:
        for filename in filenames:
            try:
                print(filename, file=file_out)
            except:
                continue


def find_files_greater_than_size(filenames=(), size=0):
    """Return files in list with size greater than value passed in."""
    valid_filenames = []
    for filename in filenames:
        try:
            if os.path.getsize(filename) > size:
                valid_filenames.append(filename)
        except:
            continue
    return valid_filenames


def find_files_with_name(filenames=(), name=""):
    """Return files in list with the name passed in."""
    valid_filenames = []
    for filename in filenames:
        try:
            if name in filename:
                valid_filenames.append(filename)
        except:
            continue
    return valid_filenames


def find_files_with_text(filenames=(), text=""):
    """Open each file in filenames, returning the files that contain the text passed in."""
    valid_filenames = []
    for filename in filenames:
        try:
            with open(filename, 'r') as file_in:
                if text in file_in.read():
                    valid_filenames.append(filename)
        except:
            continue
    return valid_filenames


def get_positive_float(prompt="Number: ", error="Invalid Number"):
    """Get a float, making sure it is positive."""
    number = 0.0
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


def get_nonempty_string(prompt="String: ", error="String cannot be blank"):
    """Get a string, making sure it is not empty."""
    string = input(prompt)
    while not string:
        print(error)
        string = input(prompt)
    return string


main()
