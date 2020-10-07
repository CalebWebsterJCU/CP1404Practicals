"""
Sort Files 2
06/10/2020
This program sorts file types into new/existing directories specified by the user.
"""

import os
import shutil


def main():
    """Get file extensions. For each extension (file type), ask user for a directory.
    If directory does not exist, create it. Then move all files of that extension
    into said directory."""

    extensions_to_directories = {}
    extensions = []
    os.chdir("FilesToSort")
    filenames = [filename for filename in os.listdir('.') if not os.path.isdir(filename)]
    for filename in filenames:
        extension = return_extension(filename)
        if extension in extensions:
            continue
        extensions.append(extension)
        directory = input("What category would you like to sort {} files into? ".format(extension))
        extensions_to_directories[extension] = directory
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

    # print(extensions_to_directories)

    for filename in filenames:
        extension = return_extension(filename)
        directory = extensions_to_directories.get(extension)
        try:
            shutil.move(filename, "{}/".format(directory) + filename)
            print("{0} moved to {1}/{0}".format(filename, directory))
        except shutil.Error:
            pass


def return_extension(filename):
    """Given a filename, return the extension."""
    return filename[filename.find('.'):]


main()
