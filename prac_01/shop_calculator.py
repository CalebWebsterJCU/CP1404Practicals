"""
Shop Calculator
This program calculates the total price of a certain number of items.
"""
DISCOUNT_THRESHOLD = 100
DISCOUNT_PERCENTAGE = 0.1


def main():
    """Get number of items and prices and calculate total."""
    number_of_items = get_positive_integer("Number of items: ", "Invalid number of items!")
    total = 0
    for x in range(number_of_items):
        price = get_positive_integer(f"Price of item #{x + 1}: ", "Invalid price!")
        total += price
    if total > DISCOUNT_THRESHOLD:
        total -= total * DISCOUNT_PERCENTAGE
    print(f"Total price for {number_of_items} items is ${total:.2f}")


def get_positive_integer(prompt, error):
    """Get a positive integer input from the user."""
    number = int(input(prompt))
    while number < 0:
        print(error)
        number = int(input(prompt))
    return number


main()
