"""
Find Uncopyrighted Songs
7/10/2020
This program finds and displays songs in Lyrics that do not have a copyright string.
"""

import os


def main():
    """Walk through directory files, opening each one.
    If it has no copyright string, add it to a list. Then print that list."""
    uncopyrighted_songs = []
    os.chdir("Lyrics")
    for directory_name, subdirectories, filenames in os.walk('.'):
        filenames = [os.path.join(directory_name, filename) for filename in filenames]
        for filename in filenames:
            with open(filename, 'r') as file_in:
                contents = file_in.read()
                if ".i " not in contents:
                    uncopyrighted_songs.append(filename)
    print("Uncopyrighted Songs:")
    for song in uncopyrighted_songs:
        print(song)


main()
