"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for index, char in enumerate(filename):
        if index != 0 and char == ' ':
            new_name += '_'
        elif filename[index + 1:] in (".txt", ".TXT"):
            new_name += (char + ".txt")
            break
        elif char not in "\\(" and index < len(filename) - 1 and filename[index + 1].isupper():
            new_name += (char + "_")
        elif index == 0 or index - 1 == ' ':
            new_name += char.upper()
        else:
            new_name += char
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        filenames = [os.path.join(directory_name, filename) for filename in filenames]
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print(filename, new_name)
            # os.rename(filename, new_name)


# main()
demo_walk()
