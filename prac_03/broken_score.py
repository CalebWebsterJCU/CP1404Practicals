"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random as r


def main():
    """Get score and determine and print category."""
    score = get_valid_score(minimum=0, maximum=100)
    category = determine_score_category(score=score)
    print(category)
    # Generate random score and print category.
    random_score = r.randint(0, 100)
    print("Random score: {}".format(random_score))
    print(determine_score_category(score=random_score))


def get_valid_score(minimum: int, maximum: int) -> float:
    """Get a valid score between minimum and maximum values."""
    score = float(input("Enter score: "))
    while score < minimum or score > maximum:
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score


def determine_score_category(score: float) -> str:
    """Determine category based on grade."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def run_tests():
    """Test determine_score function."""
    for x in range(0, 101, 10):
        print("{} - {}".format(x, determine_score_category(x)))


# run_tests()
main()
