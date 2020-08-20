"""This program gets a number of scores, generates that number of random scores between minimum and maximum values, """
def determine_score_category(score: float) -> str:
    """Determine category based on grade."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"