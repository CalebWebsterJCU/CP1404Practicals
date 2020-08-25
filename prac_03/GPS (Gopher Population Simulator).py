"""This program simulates the growth of a gopher population over time."""

import random as r

YEARS = 100
INITIAL_POPULATION = 1000
MAX_BIRTH_PERCENTAGE = 0.5  # 0.20
MIN_BIRTH_PERCENTAGE = 0.1  # 0.20
MAX_DEATH_PERCENTAGE = 0.5  # 0.25
MIN_DEATH_PERCENTAGE = 0.1  # 0.05


def main():
    """Simulate gopher birth and death over a specified time period."""
    print('Welcome to the Gopher Population Simulator.')
    print('Starting Population: {0}'.format(INITIAL_POPULATION))
    print()
    year = 1
    population = INITIAL_POPULATION
    while year <= YEARS:
        births = r.randint(round(MIN_BIRTH_PERCENTAGE * population), round(MAX_BIRTH_PERCENTAGE * population))
        deaths = r.randint(round(MIN_DEATH_PERCENTAGE * population), round(MAX_BIRTH_PERCENTAGE * population))
        net_growth = births - deaths
        population += net_growth
        print("Year {0}".format(year))
        print("{0} gophers were born. {1} died.".format(births, deaths))
        print("Net growth: {0}".format(net_growth))
        print("Population: {0}".format(population))
        print()
        year += 1
    total_growth = population - INITIAL_POPULATION
    print("Total gopher population growth over {1} years: {0}".format(total_growth, YEARS))


main()
