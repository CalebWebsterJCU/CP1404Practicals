"""
Electricity Bill Estimator
This program estimates total electricity bill
cost based on details entered by the user.
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    """Get values and calculate total cost of electricity bill."""
    print("Electricity Bill Estimator 2.0")
    tariff = input("Which tariff? 11 or 31: ")
    if tariff == "11":
        dollars_per_kwh = TARIFF_11
    elif tariff == "31":
        dollars_per_kwh = TARIFF_31
    else:
        dollars_per_kwh = 0
    kwh_per_day = float(input("Enter daily use in kWh: "))
    days = int(input("Enter number of billing days: "))
    total_cost = dollars_per_kwh * kwh_per_day * days
    print(f"Estimated Bill: ${total_cost:.2f}")


main()
