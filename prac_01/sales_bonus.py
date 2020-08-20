"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
THRESHOLD = 1000
LOW_PERCENTAGE = 0.1
HIGH_PERCENTAGE = 0.15


def main():
    """Calculate bonus based on sales input."""
    sales = float(input("Sales: "))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print("Bonus: ${:.2f}".format(bonus))
        sales = float(input("Sales: "))
    print("Goodbye!")


def calculate_bonus(sales):
    if sales < THRESHOLD:
        percentage = LOW_PERCENTAGE
    else:
        percentage = HIGH_PERCENTAGE
    return sales * percentage


main()
