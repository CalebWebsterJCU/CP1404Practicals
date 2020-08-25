"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random as r

# Minimum / maximum length of random word format.
MAX_LENGTH = 8
MIN_LENGTH = 3
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    """Get word format, then append random consonants and vowels to a list to build a word following that format."""
    # length = r.randint(MIN_LENGTH, MAX_LENGTH)
    # word_format = ''
    # for x in range(length):
    #     word_format += r.choice(['c', 'v'])
    # word_format = "ccvcvvc"
    word_format = input("Word Format: ").lower()
    while not is_valid_format(word_format=word_format):
        print("Invalid word format")
        word_format = input("Word Format: ").lower()

    word = ""
    for kind in word_format:
        if kind == "c":
            word += r.choice(CONSONANTS)
        else:
            word += r.choice(VOWELS)
    print(word)


def is_valid_format(word_format: str):
    """Check whether a given word format eg. 'ccvvccvvcc' is valid or not."""
    for letter in word_format:
        if letter not in 'cv':
            return False
    return True


def run_tests():
    """Test functions."""
    print(is_valid_format('0cv0ccvo'))


# run_tests()
main()
