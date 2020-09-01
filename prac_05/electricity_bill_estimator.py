"""
Electricity Bill Estimator
This program estimates total electricity bill
cost based on details entered by the user.
"""

TARIFF_VALUES = {'11': 0.244618, '31': 0.136928, '18': 0.322678, '6': 0.189432, '21': 0.492736}


def main():
    """Get values and calculate total cost of electricity bill."""
    print("Electricity Bill Estimator 2.0")
    print("Choose from the following tariffs: ")
    for key in TARIFF_VALUES:
        print(key, end=", ")
    print()
    tariff = get_string_in_dict(TARIFF_VALUES, ">>> ")
    dollars_per_kwh = TARIFF_VALUES.get(tariff)
    kwh_per_day = float(input("Enter daily use in kWh: "))
    days = int(input("Enter number of billing days: "))
    total_cost = dollars_per_kwh * kwh_per_day * days
    print(f"Estimated Bill: ${total_cost:.2f}")


def get_string_in_dict(valid_strings, prompt: str = "Input: "):
    """Get a string from the user, making sure it is in a specified list."""
    string = input(prompt)
    while string not in valid_strings:
        print(f"Invalid input; must be in {valid_strings}")
        string = input(prompt)
    return string


if __name__ == '__main__':
    main()
