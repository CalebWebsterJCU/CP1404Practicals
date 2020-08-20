"""This program gets a number of scores, generates that number of random scores
between minimum and maximum values, and writes each result to a text file."""

import random as r

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
FILE_NAME = 'results.txt'


def main():
    """Get number of scores, generate random scores, write categories to text file."""
    number_of_scores = get_positive_integer(prompt='Number of scores: ')
    file_out = open(FILE_NAME, 'w')
    for x in range(number_of_scores):
        # Generate random score, determine category, write both to text file.
        score = r.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
        category = determine_score_category(score)
        print("{0} is {1}".format(score, category), file=file_out)
    file_out.close()
    print("Wrote {0} results to '{1}'".format(number_of_scores, FILE_NAME))


def determine_score_category(score: float) -> str:
    """Determine category based on grade."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_positive_integer(prompt: str = 'Number: ', error: str = 'Please enter a positive integer'):
    """Get a positive integer input from the user."""
    is_valid = False
    number = 0
    while not is_valid:
        try:
            number = int(input(prompt))
            is_valid = True
        except ValueError:
            print(error)
    return number


def run_tests():
    """Test functions."""
    print(get_positive_integer())


# run_tests()
main()
