"""
Find Files
7/10/2020
This program searches files on the hard drive that match the specified criteria.
"""
import os

# os.chdir("C:")
# for directory_name, subdirectories, filenames in os.walk('.'):
#     filenames = [os.path.join(directory_name, filename) for filename in filenames]
#     for filename in filenames:
#         print(os.path.getsize(filename))
#         if ".txt" in filename:
#             print(filename)
MENU = """
(N)ame
(S)ize
(E)xtension
(T)ext
(Q)uit"""


def main():
    """Find and print files that match the criteria the user selects from the menu."""
    directory =
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "n":
            name = get_nonempty_string("Name", "Name cannot be blank")

        elif choice == "s":
            pass
        elif choice == "e":
            pass
        elif choice == "t":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Goodbye!")


def get_filenames(directory="."):
    """Return all filenames in directory as a list."""
    all_filenames = []
    os.chdir(directory)
    for directory_name, subdirectories, filenames in os.walk('.'):
        all_filenames += [os.path.join(directory_name, filename) for filename in filenames]
    return all_filenames


def find_files_with_name(filenames=(), name=""):
    """Return files in list with the name passed in."""
    valid_filenames = []
    for filename in filenames:
        if name in filename:
            valid_filenames.append(filename)
    return valid_filenames


def get_nonempty_string(prompt="String: ", error="String cannot be blank"):
    """Get a string, making sure it is not empty."""
    string = input(prompt)
    while not string:
        print(error)
        string = input(prompt)
    return string


main()
