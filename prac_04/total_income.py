"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    incomes = [float(input("Enter income for month {}: ".format(month))) for month in range(1, number_of_months + 1)]

    # for month in range(1, number_of_months + 1):
    #     # income = float(input("Enter income for month " + str(month) + ": "))
    #     income = float(input("Enter income for month {}: ".format(month)))
    #     incomes.append(income)

    display_report(incomes, number_of_months)


def display_report(incomes, number_of_months):
    """Display income report, with incomes and totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, index in enumerate(range(number_of_months)):
        income = incomes[index]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()
