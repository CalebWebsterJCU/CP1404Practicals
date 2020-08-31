"""
Word Occurrences
31/08/2020
This program takes a string input and prints how many occurrences of each word are in the string.
"""


def main():
    """Get string, count how many occurrences of each word are in the string, append word: number to dict, print words and occurences."""
    string = get_nonempty_string("Text: ")
    words = string.split(" ")
    words_to_occurrences = {}
    longest_word_length = 0
    for word in words:
        words_to_occurrences[word] = words.count(word)
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    keys = words_to_occurrences.keys()
    for key in sorted(keys):
        print(f"{key:{longest_word_length}} : {words_to_occurrences[key]}")


def get_nonempty_string(prompt: str = "String: ", error: str = "Input cannot be blank"):
    """Get a string, making sure it is not empty."""
    string = input(prompt)
    while string == '':
        print(error)
        string = input(prompt)
    return string


main()
