"""
Sort Files 1
6/10/2020
This program sorts the files in FilesToSort folder into new folders based on file type.
"""

import os
import shutil


def main():
    """Move files with the same file extension into a directory with the name of the extension."""
    # Change to File directory
    os.chdir("FilesToSort")

    # Get a list of all the filenames
    filenames = [filename for filename in os.listdir('.') if not os.path.isdir(filename)]
    directories_created = []
    print("Files in {}:".format(os.getcwd()))
    for filename in filenames:
        print("\nFile Name: {}".format(filename))

        # Find file extension
        extension = filename[filename.find('.') + 1:]
        print("Extension: {}".format(extension))

        # If extension is not already a directory,
        # create a directory with the name of the extension
        try:
            directory_name = extension
            if directory_name not in directories_created:
                directories_created.append(directory_name)
                os.mkdir(directory_name)
            print("{} moved to {}".format(filename, directory_name))

            # Move all files into their respective directories
            shutil.move(filename, "{}/".format(directory_name) + filename)
        except FileExistsError:
            pass
        except shutil.Error:
            pass


main()
